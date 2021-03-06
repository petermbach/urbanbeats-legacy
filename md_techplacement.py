# -*- coding: utf-8 -*-
"""
@file
@author  Peter M Bach <peterbach@gmail.com>
@version 1.0
@section LICENSE

This file is part of UrbanBEATS
Copyright (C) 2013  Peter M Bach

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
"""
import tech_templates as tt
import tech_design as td
import tech_designbydcv as dcv          #sub-functions that design based on design curves
import tech_designbyeq as deq           #sub-functions that design based on design equations
import tech_designbysim as dsim         #sub-functions that design based on miniature simulations
import ubseriesread as ubseries         #sub-functions responsible for processing climate data
from md_techplacementguic import *
import os, sqlite3, gc, random
import numpy as np

from PyQt4.QtCore import *
from PyQt4.QtGui import *

import urbanbeatsdatatypes as ubdata    #UBCORE
from urbanbeatsmodule import *      #UBCORE

class Techplacement(UBModule):
    """Log of Updates made at each version:
	@ingroup UrbanBEATS
	@author Peter M Bach
	"""
        
    def __init__(self, activesim, tabindex):
        UBModule.__init__(self)
        self.block_size = 0        
        self.ubeatsdir = activesim.getGlobalOptionsRoot()  #Current directory of the file
        self.cycletype = "pc"       #UBCORE: contains either planning or implementation (so it knows what to do and whether to skip)
        self.tabindex = tabindex        #UBCORE: the simulation period (knowing what iteration this module is being run at)
        self.activesim = activesim      #UBCORE
        self.datalib = activesim.showDataArchive()  #UBCORE: entire data library
        print self.ubeatsdir
        ##########################################################################
        #---DESIGN CRITERIA INPUTS                                               
        ##########################################################################
        
        #DESIGN RATIONALE SETTINGS
        self.createParameter("ration_runoff", BOOL,"")
        self.createParameter("ration_pollute", BOOL,"")
        self.createParameter("ration_harvest",BOOL,"")
        self.createParameter("runoff_pri", DOUBLE,"")
        self.createParameter("pollute_pri", DOUBLE,"")
        self.createParameter("harvest_pri",DOUBLE,"")
        self.ration_runoff = 0                #Design for flood mitigation?
        self.ration_pollute = 1               #Design for pollution management?
        self.ration_harvest = 0              #Design for harvesting & reuse? Adds storage-sizing to certain systems
        self.runoff_pri = 0.0                      #Priority of flood mitigation?
        self.pollute_pri = 1.0                     #Priority of pollution management?
        self.harvest_pri = 0.0                     #Priority for harvesting & reuse
	
        self.priorities = []            #ADVANCED PARAMETER, holds the final weights for MCA
	
        #WATER MANAGEMENT TARGETS
        self.createParameter("targets_runoff", DOUBLE,"")
        self.createParameter("targets_TSS", DOUBLE,"")
        self.createParameter("targets_TP", DOUBLE,"")
        self.createParameter("targets_TN", DOUBLE,"")
        self.createParameter("targets_reliability", DOUBLE, "")
        self.targets_runoff = 30.0            #Runoff reduction target [%]
        self.targets_TSS = 80.0               #TSS Load reduction target [%]
        self.targets_TP = 45.0                #TP Load reduction target [%]
        self.targets_TN = 45.0                #TN Load reduction target [%]
        self.targets_reliability = 70.0       #required reliability of harvesting systems
        
        self.system_tarQ = 0            #INITIALIZE THESE VARIABLES
        self.system_tarTSS = 0
        self.system_tarTP = 0
        self.system_tarTN = 0
        self.system_tarREL = 0
        self.targetsvector = []         #---CALCULATED IN THE FIRST LINE OF RUN()
        
        #WATER MANAGEMENT SERVICE LEVELS
        self.createParameter("service_swmQty", DOUBLE, "")
        self.createParameter("service_swmWQ", DOUBLE, "")
        self.createParameter("service_rec", DOUBLE, "")
        self.createParameter("service_res", BOOL, "")
        self.createParameter("service_hdr", BOOL, "")
        self.createParameter("service_com", BOOL, "")
        self.createParameter("service_li", BOOL, "")
        self.createParameter("service_hi", BOOL, "")
        self.createParameter("service_redundancy", DOUBLE, "")
        self.service_swmQty = 50.0                #required service level for stormwater management
        self.service_swmWQ = 50.0                 #required service level for stormwater management
        self.service_rec = 50.0                   #required service level for substituting potable water demand through recycling
        self.service_res = 1
        self.service_hdr = 1
        self.service_com = 1
        self.service_li = 1
        self.service_hi = 1
        self.service_redundancy = 25.0
        self.servicevector = []
        
        #STRATEGY CUSTOMIZE
        self.createParameter("strategy_lot_check", BOOL, "")
        self.createParameter("strategy_street_check", BOOL, "")
        self.createParameter("strategy_neigh_check", BOOL, "")
        self.createParameter("strategy_subbas_check", BOOL, "")
        self.createParameter("lot_rigour", DOUBLE, "")
        self.createParameter("street_rigour", DOUBLE, "")
        self.createParameter("neigh_rigour", DOUBLE, "")
        self.createParameter("subbas_rigour", DOUBLE, "")
        self.strategy_lot_check = 1
        self.strategy_street_check = 1
        self.strategy_neigh_check = 1
        self.strategy_subbas_check = 1
        self.lot_rigour = 4.0
        self.street_rigour = 4.0
        self.neigh_rigour = 4.0
        self.subbas_rigour = 4.0
        
        #ADDITIONAL STRATEGIES
        self.createParameter("scalepref", DOUBLE,"")
        self.scalepref = 3  #Ranges from 1 (high priority on at-source) to 5 (high priority on end-of-pipe)

        self.scalingprefmatrix = [{"L":0.40, "S":0.30, "N":0.20, "B":0.10},
                                  {"L":0.25, "S":0.35, "N":0.25, "B":0.15},
                                  {"L":0.25, "S":0.25, "N":0.25, "B":0.25},
                                  {"L":0.15, "S":0.25, "N":0.35, "B":0.25},
                                  {"L":0.10, "S":0.20, "N":0.30, "B":0.40},]
        self.curscalepref = {"L":0.25, "S":0.25, "N":0.25, "B":0.25}

        ##########################################################################
        #---WATER USE EFFICIENCY AND RECYCLING STRATEGY DESIGN INPUTS            
        ##########################################################################
        
        #WATER DEMAND PATTERNS
        #--> Water Demands
        self.createParameter("freq_kitchen", DOUBLE, "")
        self.createParameter("freq_shower", DOUBLE, "")
        self.createParameter("freq_toilet", DOUBLE, "")
        self.createParameter("freq_laundry", DOUBLE, "")
        self.createParameter("dur_kitchen", DOUBLE, "")
        self.createParameter("dur_shower", DOUBLE, "")
        self.createParameter("demandvary_kitchen", DOUBLE, "")
        self.createParameter("demandvary_shower", DOUBLE, "")
        self.createParameter("demandvary_toilet", DOUBLE, "")
        self.createParameter("demandvary_laundry", DOUBLE, "")
        self.createParameter("ffp_kitchen", STRING, "")
        self.createParameter("ffp_shower", STRING, "")
        self.createParameter("ffp_toilet", STRING, "")
        self.createParameter("ffp_laundry", STRING, "")
        self.createParameter("priv_irr_vol", DOUBLE, "")
        self.createParameter("ffp_garden", STRING, "")
        self.freq_kitchen = 2.0                   #Household Demands START
        self.freq_shower = 2.0
        self.freq_toilet = 2.0
        self.freq_laundry = 2.0
        self.dur_kitchen = 10.0
        self.dur_shower = 5.0
        self.demandvary_kitchen = 0.00
        self.demandvary_shower = 0.00
        self.demandvary_toilet = 0.00
        self.demandvary_laundry = 0.00
        self.ffp_kitchen = "SW"
        self.ffp_shower = "SW"
        self.ffp_toilet = "SW"
        self.ffp_laundry = "SW"
        self.priv_irr_vol = 1.0                   #Private irrigation volume [ML/ha/yr]
        self.ffp_garden = "SW"
        
        self.createParameter("com_demand", DOUBLE, "")
        self.createParameter("com_demandvary", DOUBLE, "")
        self.createParameter("com_demandunits", STRING, "")
        self.createParameter("li_demand", DOUBLE, "")
        self.createParameter("li_demandvary", DOUBLE, "")
        self.createParameter("li_demandunits", STRING, "")
        self.createParameter("hi_demand", DOUBLE, "")
        self.createParameter("hi_demandvary", DOUBLE, "")
        self.createParameter("hi_demandunits", STRING, "")
        self.createParameter("ffp_nonres", STRING, "")
        self.com_demand = 40.0
        self.com_demandvary = 10.0
        self.com_demandunits = 'cap'    #sqm = per square metres floor area, cap = per capita
        self.li_demand = 40.0
        self.li_demandvary = 10.0
        self.li_demandunits = 'cap'
        self.hi_demand = 40.0
        self.hi_demandvary = 10.0
        self.hi_demandunits = 'cap'
        self.ffp_nonres = "SW"

        self.createParameter("public_irr_vol", DOUBLE, "")
        self.createParameter("irrigate_nonres", BOOL, "")
        self.createParameter("irrigate_parks", BOOL, "")
        self.createParameter("irrigate_refs", BOOL, "")
        self.createParameter("public_irr_wq", STRING, "")
        self.public_irr_vol = 1.0
        self.irrigate_nonres = 1
        self.irrigate_parks = 1
        self.irrigate_refs = 0
        self.public_irr_wq = "SW"       #PO = potable, NP = non-potable, RW = rainwater, SW = stormwater, GW = greywater
        
        #WATER EFFICIENCY
        self.createParameter("LOSS_status", BOOL, "")
        self.createParameter("LOSS_amount", DOUBLE, "")
        self.LOSS_status = 0
        self.LOSS_amount = 10.0     #% of losses from system (from total demand)

        self.createParameter("WEFstatus", BOOL,"")
        self.WEFstatus = 0
        
        self.createParameter("WEF_rating_system", STRING,"")
        self.createParameter("WEF_loc_house", BOOL,"")
        self.createParameter("WEF_loc_apart", BOOL,"")
        self.createParameter("WEF_loc_nonres", BOOL,"")
        self.WEF_rating_system = "AS"
        self.WEF_loc_house = 1
        self.WEF_loc_apart = 1
        self.WEF_loc_nonres = 1
        
        self.createParameter("WEF_method", STRING, "")
        self.createParameter("WEF_c_rating", DOUBLE, "")
        self.createParameter("WEF_d_rating", DOUBLE, "")
        self.createParameter("WEF_distribution", STRING, "")
        self.createParameter("WEF_includezero", BOOL, "")
        self.WEF_method = 'C'   #C = constant, D = distribution
        self.WEF_c_rating = 2.0   #Number of stars
        self.WEF_d_rating = 5.0  #Maximum number of stars
        self.WEF_distribution = "UF"     #UF = Uniform, LH = log-normal (high-end), LL = log-normal (low-end), NM = normal
        self.WEF_includezero = 1
        
        #REGIONAL RECYCLING-SUPPLY ZONES
        self.createParameter("rec_demrange_min", DOUBLE, "")
        self.createParameter("rec_demrange_max", DOUBLE, "")
        self.createParameter("ww_kitchen", BOOL, "")
        self.createParameter("ww_shower", BOOL, "")
        self.createParameter("ww_toilet", BOOL, "")
        self.createParameter("ww_laundry", BOOL, "")
        self.createParameter("hs_strategy", STRING, "")
        self.rec_demrange_min = 10.0
        self.rec_demrange_max = 100.0
        self.ww_kitchen = 0         #Kitchen WQ default = GW
        self.ww_shower = 0          #Shower WQ default = GW
        self.ww_toilet = 0          #Toilet WQ default = BW --> MUST BE RECYCLED
        self.ww_laundry = 0         #Laundry WQ default = GW
        self.hs_strategy = "ud"         #ud = upstream-downstream, uu = upstream-upstream, ua = upstream-around
        
        #ADDITIONAL INPUTS
        self.createParameter("sb_method", STRING, "")
        self.createParameter("rain_length", DOUBLE, "")
        self.createParameter("swh_benefits", BOOL, "")
        self.createParameter("swh_unitrunoff", DOUBLE, "")
        self.createParameter("swh_unitrunoff_auto", BOOL, "")
        self.sb_method = "Sim"  #Sim = simulation, Eqn = equation
        self.rain_length = 2.0   #number of years.
        self.swh_benefits = 1   #execute function to calculate SWH benefits? (1 by default, but perhaps treat as mutually exclusive)
        self.swh_unitrunoff = 0.545  #Unit runoff rate [kL/sqm impervious]
        self.swh_unitrunoff_auto = 0

        #SWH Harvesting algorithms
        self.createParameter("rainfile", STRING, "")    #Rainfall file for SWH
        self.rainfile = "<none>"
        #self.rainfile = self.ubeatsdir+"/ancillary/MelbourneRain1998-2007-6min.csv"
        self.createParameter("rain_dt", DOUBLE, "")
        self.rain_dt = 6        #[mins]
        self.createParameter("evapfile", STRING, "")
        self.evapfile = "<none>"
        #self.evapfile = self.ubeatsdir+"/ancillary/MelbourneEvap1998-2007-Day.csv"
        self.createParameter("evap_dt", DOUBLE, "")
        self.evap_dt = 1440     #[mins]



        ##########################################################################
        #---RETROFIT CONDITIONS INPUTS                                           
        ##########################################################################
        
        #SCENARIO DESCRIPTION
        self.createParameter("retrofit_scenario", STRING,"")
        self.createParameter("renewal_cycle_def", BOOL,"")
        self.createParameter("renewal_lot_years", DOUBLE,"")
        self.createParameter("renewal_street_years", DOUBLE,"")
        self.createParameter("renewal_neigh_years", DOUBLE,"")
        self.createParameter("renewal_lot_perc", DOUBLE,"")
        self.createParameter("force_street", BOOL,"")
        self.createParameter("force_neigh", BOOL,"")
        self.createParameter("force_prec", BOOL,"")
        self.retrofit_scenario = "N"    #N = Do Nothing, R = With Renewal, F = Forced
        self.renewal_cycle_def = 1      #Defined renewal cycle?
        self.renewal_lot_years = 10.0         #number of years to apply renewal rate
        self.renewal_street_years = 20.0      #cycle of years for street-scale renewal
        self.renewal_neigh_years = 40.0       #cycle of years for neighbourhood-precinct renewal
        self.renewal_lot_perc = 5.0           #renewal percentage
        self.force_street = 0              #forced renewal on lot?
        self.force_neigh = 0           #forced renewal on street?
        self.force_prec = 0            #forced renewal on neighbourhood and precinct?
        
        #LIFE CYCLE OF EXISTING SYSTEMS
        self.createParameter("lot_renew", BOOL,"")
        self.createParameter("lot_decom", BOOL,"")
        self.createParameter("street_renew", BOOL,"")
        self.createParameter("street_decom", BOOL,"")
        self.createParameter("neigh_renew", BOOL,"")
        self.createParameter("neigh_decom", BOOL,"")
        self.createParameter("prec_renew", BOOL,"")
        self.createParameter("prec_decom", BOOL,"")
        self.createParameter("decom_thresh", DOUBLE,"")
        self.createParameter("renewal_thresh", DOUBLE,"")
        self.createParameter("renewal_alternative", STRING,"")
        self.lot_renew = 0      #NOT USED UNLESS LOT RENEWAL ALGORITHM EXISTS
        self.lot_decom = 0
        self.street_renew = 0
        self.street_decom = 0
        self.neigh_renew = 0
        self.neigh_decom = 0
        self.prec_renew = 0
        self.prec_decom = 0
        self.decom_thresh = 40.0
        self.renewal_thresh = 30.0
        self.renewal_alternative = "K"          #if renewal cannot be done, what to do then? K=Keep, D=Decommission
        
        ##########################################################################
        #---TECHNOLOGIES LIST AND CUSTOMIZATION                                  
        ##########################################################################
        
        #---ADVANCED STORMWATER HARVESTING PLANT [ASHP]---###TBA###-------------
        self.createParameter("ASHPstatus", BOOL,"")
        self.ASHPstatus = 0
        self.ASHPlot = 0
        self.ASHPstreet = 0
        self.ASHPneigh = 0
        self.ASHPprec = 0
        
        #---AQUACULTURE/LIVING SYSTEMS [AQ]---###TBA###-------------------------
        self.createParameter("AQstatus", BOOL,"")
        self.AQstatus = 0
        
        #---AQUIFER STORAGE & RECOVERY SYSTEM [ASR]---###TBA###-----------------
        self.createParameter("ASRstatus", BOOL,"")
        self.ASRstatus = 0
        
        #---BIOFILTRATION SYSTEM/RAINGARDEN [BF]--------------------------------
        self.createParameter("BFstatus", BOOL,"")
        self.BFstatus = 1
        
        #Available Scales
        self.createParameter("BFlot", BOOL,"")
        self.createParameter("BFstreet", BOOL,"")
        self.createParameter("BFneigh", BOOL,"")
        self.createParameter("BFprec", BOOL,"")
        self.BFlot = 1
        self.BFstreet = 1
        self.BFneigh = 1
        self.BFprec = 1
        
        #Available Applications
        self.createParameter("BFflow", BOOL, "")
        self.createParameter("BFpollute", BOOL,"")
        self.createParameter("BFrecycle", BOOL, "")
        self.BFflow = 1
        self.BFpollute = 1
        self.BFrecycle = 1
	
        #Design Curves
        self.createParameter("BFdesignUB", BOOL,"")
        self.createParameter("BFdescur_path", STRING,"")
        self.BFdesignUB = 1          #use DAnCE4Water's default curves to design system?
        self.BFdescur_path = "no file"  #path for design curve
        
        #Design Information
        self.createParameter("BFspec_EDD", DOUBLE,"")
        self.createParameter("BFspec_FD", DOUBLE,"")
        self.createParameter("BFminsize", DOUBLE, "")
        self.createParameter("BFmaxsize", DOUBLE,"")
        self.createParameter("BFavglife", DOUBLE,"")
        self.createParameter("BFexfil", DOUBLE,"")
        self.BFspec_EDD = 0.4
        self.BFspec_FD = 0.6
        self.BFminsize = 5.0              #minimum surface area of the system in sqm
        self.BFmaxsize = 999999.0         #maximum surface area of system in sqm
        self.BFavglife = 20.0             #average life span of a biofilter
        self.BFexfil = 0.0
        
        #---GREEN ROOF [GR]---###TBA###-----------------------------------------
        self.createParameter("GRstatus", BOOL,"")
        self.GRstatus = 0
        
        #---INFILTRATION SYSTEM [IS]--------------------------------------------
        self.createParameter("ISstatus", BOOL,"")
        self.ISstatus = 1
        
        #Available Scales
        self.createParameter("ISlot", BOOL,"")
        self.createParameter("ISstreet", BOOL,"")
        self.createParameter("ISneigh", BOOL,"")
        self.createParameter("ISprec", BOOL, "")
        self.ISlot = 1
        self.ISstreet = 1
        self.ISneigh = 1
        self.ISprec = 1
        
        #Available Applications
        self.createParameter("ISflow", BOOL,"")
        self.createParameter("ISpollute", BOOL,"")
        self.ISflow = 1
        self.ISpollute = 1
        self.ISrecycle = 0      #Permanently zero
        
        #Design Curves
        self.createParameter("ISdesignUB", BOOL,"")
        self.createParameter("ISdescur_path", STRING,"")
        self.ISdesignUB = 1          #use DAnCE4Water's default curves to design system?
        self.ISdescur_path = "no file"  #path for design curve
        
        #Design Information        self.createParameter("ISspec_EDD", DOUBLE,"")
        self.createParameter("ISspec_FD", DOUBLE,"")
        self.createParameter("ISspec_EDD", DOUBLE,"")
        self.createParameter("ISminsize", DOUBLE, "")
        self.createParameter("ISmaxsize", DOUBLE,"")
        self.createParameter("ISavglife", DOUBLE,"")
        self.createParameter("ISexfil", DOUBLE, "")
        self.ISspec_EDD = 0.2
        self.ISspec_FD = 0.8
        self.ISminsize = 5.0
        self.ISmaxsize = 99999.0          #maximum surface area of system in sqm
        self.ISavglife = 20.0             #average life span of an infiltration system
        self.ISexfil = 3.6
        
        #---GROSS POLLUTANT TRAP [GPT]------------------------------------------
        self.createParameter("GPTstatus", BOOL,"")
        self.GPTstatus = 0
        
        #---GREYWATER TREATMENT & DIVERSION SYSTEM [GT]-------------------------
        self.createParameter("GTstatus", BOOL,"")
        self.GTstatus = 0
        
        #---PACKAGED PLANT [PPL]---###TBA###------------------------------------
        self.createParameter("PPLstatus", BOOL,"")
        self.PPLstatus = 0
        
        #---PONDS & SEDIMENTATION BASIN [PB]------------------------------------
        self.createParameter("PBstatus", BOOL,"")
        self.PBstatus = 1
        
        #Available Scales
        self.createParameter("PBneigh", BOOL,"")
        self.createParameter("PBprec", BOOL,"")
        self.PBneigh = 1
        self.PBprec = 1
        
        #Available Applications
        self.createParameter("PBflow", BOOL,"")
        self.createParameter("PBpollute", BOOL,"")
        self.createParameter("PBrecycle", BOOL, "")
        self.PBflow = 1
        self.PBpollute = 1
        self.PBrecycle = 0
        
        #Design Curves
        self.createParameter("PBdesignUB", BOOL,"")
        self.createParameter("PBdescur_path", STRING,"")
        self.PBdesignUB = 1          #use DAnCE4Water's default curves to design system?
        self.PBdescur_path = "no file"  #path for design curve
        
        #Design Information
        self.createParameter("PBspec_MD", STRING,"")
        self.createParameter("PBminsize", DOUBLE, "")
        self.createParameter("PBmaxsize", DOUBLE,"")
        self.createParameter("PBavglife", DOUBLE,"")
        self.createParameter("PBexfil", DOUBLE, "")
        self.PBspec_MD = "0.75" 	#need a string for the combo box
        self.PBminsize = 100.0
        self.PBmaxsize = 9999999.0           #maximum surface area of system in sqm
        self.PBavglife = 20.0             #average life span of a pond/basin
        self.PBexfil = 0.36

        #---POROUS/PERVIOUS PAVEMENT [PP]---###TBA###---------------------------
        self.createParameter("PPstatus", BOOL,"")
        self.PPstatus = 0
        
        #---RAINWATER TANK [RT]-------------------------------------------------
        self.createParameter("RTstatus", BOOL,"")
        self.RTstatus = 0
        
        self.createParameter("RTlot", BOOL,"")
        self.createParameter("RTneigh", BOOL,"")
        self.createParameter("RTflow", BOOL,"")
        self.createParameter("RTrecycle", BOOL,"")
        self.RTlot = 1
        self.RTneigh = 0
        self.RTflow = 0
        self.RTpollute = 0      #permanently zero
        self.RTrecycle = 1
        
        self.createParameter("RT_maxdepth", DOUBLE,"")
        self.createParameter("RT_mindead", DOUBLE,"")
        self.createParameter("RTdesignUB", BOOL,"")
        self.createParameter("RTdescur_path", STRING,"")
        self.createParameter("RTavglife", DOUBLE,"")
        self.RT_maxdepth = 2.0            #max tank depth [m]
        self.RT_mindead = 0.1           #minimum dead storage level [m]
        self.RTdesignUB = 1         #use DAnCE4Water's default curves to design system?
        self.RTdescur_path = "no file"  #path for design curve
        self.RTavglife = 20.0             #average life span of a raintank
        
        self.RTminsize = 0.0             #placeholders, do not actually matter
        self.RTmaxsize = 9999.0
        
        #---SAND/PEAT/GRAVEL FILTER [SF]----------------------------------------
        self.createParameter("SFstatus", BOOL,"")
        self.SFstatus = 0
        
        #---SUBSURFACE IRRIGATION SYSTEM [IRR]---###TBA###----------------------
        self.createParameter("IRRstatus", BOOL,"")
        self.IRRstatus = 0
        
        #---SUBSURFACE WETLAND/REED BED [WSUB]----------------------------------
        self.createParameter("WSUBstatus", BOOL,"")
        self.WSUBstatus = 0
        
        #---SURFACE WETLAND [WSUR]----------------------------------------------
        self.createParameter("WSURstatus", BOOL,"")
        self.WSURstatus = 1
        
        #Available Scales
        self.createParameter("WSURneigh", BOOL,"")
        self.createParameter("WSURprec", BOOL,"")
        self.WSURneigh = 1
        self.WSURprec = 1
        
        #Available Applications
        self.createParameter("WSURflow", BOOL,"")
        self.createParameter("WSURpollute", BOOL,"")
        self.createParameter("WSURrecycle", BOOL, "")
        self.WSURflow = 1
        self.WSURpollute = 1
        self.WSURrecycle = 0
        
        #Design Curves
        self.createParameter("WSURdesignUB", BOOL,"")
        self.createParameter("WSURdescur_path", STRING,"")
        self.WSURdesignUB = 1          #use DAnCE4Water's default curves to design system?
        self.WSURdescur_path = "no file"  #path for design curve
        
        #Design Information
        self.createParameter("WSURspec_EDD", STRING,"")
        self.createParameter("WSURminsize", DOUBLE, "")
        self.createParameter("WSURmaxsize", DOUBLE,"")
        self.createParameter("WSURavglife", DOUBLE,"")
        self.createParameter("WSURexfil", DOUBLE, "") 
        self.WSURspec_EDD = "0.75"
        self.WSURminsize = 200.0
        self.WSURmaxsize = 9999999.0           #maximum surface area of system in sqm
        self.WSURavglife = 20.0             #average life span of a wetland
        self.WSURexfil = 0.36

        #---SWALES & BUFFER STRIPS [SW]-----------------------------------------
        self.createParameter("SWstatus", BOOL,"")
        self.SWstatus = 0
        
        #Available Scales
        self.createParameter("SWstreet", BOOL,"")
        self.createParameter("SWneigh", BOOL,"")
        self.SWstreet = 1
        self.SWneigh = 1
        
        #Available Applications
        self.createParameter("SWflow", BOOL,"")
        self.createParameter("SWpollute", BOOL,"")
        self.createParameter("SWrecycle", BOOL, "")
        self.SWflow = 1
        self.SWpollute = 1
        self.SWrecycle = 0
        
        #Design Curves
        self.createParameter("SWdesignUB", BOOL,"")
        self.createParameter("SWdescur_path", STRING,"")
        self.SWdesignUB = 1          #use DAnCE4Water's default curves to design system?
        self.SWdescur_path = "no file"  #path for design curve
        
        #Design Information
        self.createParameter("SWspec", DOUBLE,"")
        self.createParameter("SWminsize", DOUBLE, "")
        self.createParameter("SWmaxsize", DOUBLE,"")
        self.createParameter("SWavglife", DOUBLE,"")
        self.createParameter("SWexfil", DOUBLE, "")
        self.SWspec = 0.0
        self.SWminsize = 20.0
        self.SWmaxsize = 9999.0           #maximum surface area of system in sqm
        self.SWavglife = 20.0             #average life span of a swale
        self.SWexfil = 3.6              
        
        #---TREE PITS [TPS]---###TBA###-----------------------------------------
        self.createParameter("TPSstatus", BOOL,"")
        self.TPSstatus = 0
        
        #---URINE-SEPARATING TOILET [UT]---###TBA###----------------------------
        self.createParameter("UTstatus", BOOL,"")
        self.UTstatus = 0
        
        #---WASTEWATER RECOVERY & RECYCLING PLANT [WWRR]---###TBA###------------
        self.createParameter("WWRRstatus", BOOL,"")
        self.WWRRstatus = 0
        
        #---WATERLESS/COMPOSTING TOILETS [WT]---###TBA###-----------------------
        self.createParameter("WTstatus", BOOL,"")
        self.WTstatus = 0
        
        #---REGIONAL INFORMATION -----------------------------------------------
        self.createParameter("regioncity", STRING,"")
        self.regioncity = "Melbourne"
        
        #---MULTI-CRITERIA INPUTS-----------------------------------------------
        #SELECT EVALUATION METRICS
        self.createParameter("scoringmatrix_path", STRING,"")
        self.createParameter("scoringmatrix_default", BOOL,"")
        self.scoringmatrix_path = self.ubeatsdir+"/ancillary/mcadefault.csv"
        self.scoringmatrix_default = 0
        
        #CUSTOMIZE EVALUATION CRITERIA
        self.createParameter("bottomlines_tech", BOOL,"")
        self.createParameter("bottomlines_env", BOOL,"")
        self.createParameter("bottomlines_ecn",BOOL,"")
        self.createParameter("bottomlines_soc", BOOL,"")
        self.createParameter("bottomlines_tech_n", DOUBLE,"")
        self.createParameter("bottomlines_env_n", DOUBLE,"")
        self.createParameter("bottomlines_ecn_n", DOUBLE,"")
        self.createParameter("bottomlines_soc_n", DOUBLE,"")
        self.createParameter("bottomlines_tech_w", DOUBLE,"")
        self.createParameter("bottomlines_env_w", DOUBLE,"")
        self.createParameter("bottomlines_ecn_w", DOUBLE,"")
        self.createParameter("bottomlines_soc_w", DOUBLE,"")
        self.bottomlines_tech = 1   #Include criteria? Yes/No
        self.bottomlines_env = 1
        self.bottomlines_ecn = 1
        self.bottomlines_soc = 1
        self.bottomlines_tech_n = 4.0     #Metric numbers
        self.bottomlines_env_n = 5.0
        self.bottomlines_ecn_n = 2.0
        self.bottomlines_soc_n = 4.0
        self.bottomlines_tech_w = 1.0     #Criteria Weights
        self.bottomlines_env_w = 1.0
        self.bottomlines_ecn_w = 1.0
        self.bottomlines_soc_w = 1.0
        self.mca_techlist, self.mca_tech, self.mca_env, self.mca_ecn, self.mca_soc = [], [], [], [], [] #initialize as globals
        
        #SCORING OF STRATEGIES
        self.createParameter("score_strat", STRING, "")
        self.createParameter("scope_stoch", BOOL,"")
        self.createParameter("score_method", STRING,"")
        self.createParameter("ingroup_scoring", STRING,"")
        self.createParameter("iao_influence", DOUBLE, "")
        self.scope_stoch = 0
        self.score_strat = "SNP"        #SNP = service-no-penalty, SLP = service-linear-penalty, SPP = service-nonlinear-penalty
        self.score_method = "WSM"       #MCA scoring method
        self.ingroup_scoring = "Avg"
        self.iao_influence = 10.0
        
        #RANKING OF STRATEGIES
        self.createParameter("ranktype", STRING,"")
        self.createParameter("topranklimit", DOUBLE,"")
        self.createParameter("conf_int", DOUBLE,"")
        self.createParameter("pickingmethod", STRING, "")
        self.ranktype = "RK"            #CI = Confidence Interval, RK = ranking
        self.topranklimit = 10.0
        self.conf_int = 95.0
        self.pickingmethod = "TOP"  #TOP = score-based, RND = random sampling
        
        ########################################################################
        #---ADVANCED PARAMETERS & VARIABLES
        ########################################################################
        self.technames = ["ASHP", "AQ", "ASR", "BF", "GR", "GT", 
                          "GPT", "IS", "PPL", "PB", "PP", "RT", 
                          "SF", "IRR", "WSUB", "WSUR", "SW", 
                          "TPS", "UT", "WWRR", "WT"]

        self.scaleabbr = ["lot", "street", "neigh", "prec"]
        self.ffplevels = {"PO":1, "NP":2, "RW":3, "SW":4, "GW":5}  #Used to determine when a system is cleaner than the other

        #DEBUG - Database writing option of tech planning information, enable if wanting a dump of info from module outputs
        #self.sqlDB = 0  #Global variable to hold the sqlite database
        #self.dbcurs = 0 #cursor to execute sqlcommands for the sqlite database


        self.lot_incr = []
        self.street_incr = []
        self.neigh_incr = []
        self.subbas_incr = []

        self.createParameter("num_output_strats", DOUBLE, "")
        self.num_output_strats = 5      #number of output strategies
        
        self.createParameter("startyear", DOUBLE, "")
        self.createParameter("prevyear", DOUBLE, "")
        self.createParameter("currentyear", DOUBLE, "")
        self.startyear = 1960  #Retrofit Advanced Parameters - Set by Model Core
        self.prevyear = 1960
        self.currentyear = 1980
        
        self.lot_raintanksizes = [1,2,3,4,5,7.5,10,15,20,50,100]       #[kL]
        self.raindata = []      #Globals to contain the data time series
        self.evapdata = []
        self.evapscale = []
        self.sysdepths = {}     #Holds all calculated system depths

        self.swhbenefitstable = []

        self.createParameter("relTolerance", DOUBLE, "")
        self.createParameter("maxSBiterations", DOUBLE, "")
        self.relTolerance = 1
        self.maxSBiterations = 100

        self.createParameter("maxMCiterations", DOUBLE, "")
        self.createParameter("defaultdecision", STRING, "")
        self.createParameter("temp_dir", STRING, "")
        self.maxMCiterations = 1000
        self.defaultdecision = "H"
        self.temp_dir = ""

        #MCA Penalties
        self.createParameter("penaltyQty", BOOL, "")
        self.createParameter("penaltyWQ", BOOL, "")
        self.createParameter("penaltyRec", BOOL, "")
        self.createParameter("penaltyFa", DOUBLE, "")
        self.createParameter("penaltyFb", DOUBLE, "")
        self.penaltyQty = 1
        self.penaltyWQ = 1
        self.penaltyRec = 1
        self.penaltyFa = 2.0
        self.penaltyFb = 1.2

        #Plan Revision
        self.createParameter("Revise", BOOL, "")
        self.Revise = 0

        
    def run(self):
        #self.notify(self.ubeatsdir)
        map_attr = self.activesim.getAssetWithName("MapAttributes")
        self.curscalepref = self.scalingprefmatrix[int(self.scalepref)-1]

        ###-------------------------------------------------------------------###
        #--- PRE-PROCESSING
        ###-------------------------------------------------------------------###        

        #MODIFY PARAMETERS IF REVISION IS NOT WANTED
        if self.Revise == 1:
            self.ration_runoff = 0
            self.ration_pollute = 0
            self.ration_harvest = 0

        #CALCULATE SOME GLOBAL VARIABLES RELATING TO TARGETS
        self.system_tarQ = self.ration_runoff * self.targets_runoff     #Runoff reduction target
        self.system_tarTSS = self.ration_pollute * self.targets_TSS     #TSS reduction target
        self.system_tarTP = self.ration_pollute * self.targets_TP       #TP reduction target
        self.system_tarTN = self.ration_pollute * self.targets_TN       #TN reduction target
        self.system_tarREL = self.ration_harvest * self.targets_reliability     #Reliability  of recycling
        self.targetsvector = [self.system_tarQ, self.system_tarTSS, self.system_tarTP, self.system_tarTN, self.system_tarREL]
        self.notify(str(self.targetsvector))
        self.servicevector = [self.service_swmQty, self.service_swmWQ, self.service_rec]
        self.notify(str(self.servicevector))
        #-> targetsvector TO BE USED TO ASSESS OPPORTUNITIES

        #CALCULATE SYSTEM DEPTHS
        self.sysdepths = {"RT": self.RT_maxdepth - self.RT_mindead, "GW": 1, "WSUR": self.WSURspec_EDD, "PB": self.PBspec_MD}
        
        #SET DESIGN CURVES DIRECTORY        
        #To be done later.

        #GET NECESSARY GLOBAL DATA TO DO ANALYSIS
        blocks_num = map_attr.getAttribute("NumBlocks")     #number of blocks to loop through
        self.block_size = map_attr.getAttribute("BlockSize")    #size of block
        map_w = map_attr.getAttribute("WidthBlocks")        #num of blocks wide
        map_h = map_attr.getAttribute("HeightBlocks")       #num of blocks tall
        input_res = map_attr.getAttribute("InputReso")      #resolution of input data
        basins = map_attr.getAttribute("TotalBasins")
        map_attr.addAttribute("OutputStrats", self.num_output_strats)

        #CREATE TECHNOLOGIES SHORTLIST - THIS IS THE USER'S CUSTOMISED SHORTLIST
        userTechList = self.compileUserTechList()               #holds the active technologies selected by user for simulation
        self.notify(str(userTechList))
        
        #CREATE TECHNOLOGY LISTS FOR DIFFERENT SCALES
        techListLot = self.fillScaleTechList("lot", userTechList)
        techListStreet = self.fillScaleTechList("street", userTechList)
        techListNeigh = self.fillScaleTechList("neigh", userTechList)
        techListSubbas = self.fillScaleTechList("subbas", userTechList)
        self.notify("Lot"+str(techListLot))
        self.notify("Street"+str(techListStreet))
        self.notify("Neighbourhood"+str(techListNeigh))
        self.notify("Sub-basin"+str(techListSubbas))

        #INITIALIZE SWH BENEFITS DATA
        if self.swh_benefits:
            self.swhbenefitstable = dcv.initializeSWHbenefitsTable(self.ubeatsdir+"/ancillary")

        #PROCESS MCA PARAMETERS AND SCORING DETAILS
        self.mca_techlist, self.Fmca_tech, self.mca_env, self.mca_ecn, self.mca_soc = self.retrieveMCAscoringmatrix()
        self.notify(self.mca_techlist)
        self.notify(self.mca_tech)
        self.notify(self.mca_env)
        self.notify(self.mca_ecn)
        self.notify(self.mca_soc)
        
        #Calculate MCA weightings for different PURPOSES - used to penalize MCA score if tech does not meet particular purpose
        self.priorities = [int(self.ration_runoff)*float(self.runoff_pri), 
                           int(self.ration_pollute)*float(self.pollute_pri),
                           int(self.ration_harvest)*float(self.harvest_pri)]
        prioritiessum = sum(self.priorities)
        for i in range(len(self.priorities)):       #e.g. ALL and priorities 3,2,1 --> [3/6, 2/6, 1/6]
            if prioritiessum == 0:
                self.priorities[i] = 1
            else:
                self.priorities[i] = self.priorities[i]/prioritiessum               #1, 2 and priorities 3,2,1 --> [3/5, 2/5, 0]
        self.notify(self.priorities)
        self.notify("Now planning technologies")

        ###-------------------------------------------------------------------###
        #--- FIRST LOOP - WATER DEMANDS AND EFFICIENCY
        ###-------------------------------------------------------------------###
        for i in range(int(blocks_num)):
            currentID = i+1
            currentAttList = self.activesim.getAssetWithName("BlockID"+str(currentID))

            if currentAttList.getAttribute("Status") == 0:
                continue
            wdDict = self.calculateBlockWaterDemand(currentAttList)
            currentAttList.addAttribute("wd_Rating", wdDict["Efficiency"])      #[stars]
            currentAttList.addAttribute("wd_RES_K", wdDict["RESkitchen"])       #[kL/day]
            currentAttList.addAttribute("wd_RES_S", wdDict["RESshower"])        #[kL/day]
            currentAttList.addAttribute("wd_RES_T", wdDict["REStoilet"])        #[kL/day]
            currentAttList.addAttribute("wd_RES_L", wdDict["RESlaundry"])       #[kL/day]
            currentAttList.addAttribute("wd_RES_I", wdDict["RESirrigation"])    #[kL/day]
            currentAttList.addAttribute("wd_RES_IN", wdDict["REStotalIN"])      #[kL/yr]
            currentAttList.addAttribute("wd_RES_OUT", wdDict["REStotalOUT"])    #[kL/yr]
            currentAttList.addAttribute("wd_HDR_K", wdDict["HDRkitchen"])       #[kL/day]
            currentAttList.addAttribute("wd_HDR_S", wdDict["HDRshower"])        #[kL/day]
            currentAttList.addAttribute("wd_HDR_T", wdDict["HDRtoilet"])        #[kL/day]
            currentAttList.addAttribute("wd_HDR_L", wdDict["HDRlaundry"])       #[kL/day]
            currentAttList.addAttribute("wd_HDR_I", wdDict["HDRirrigation"])    #[kL/day]
            currentAttList.addAttribute("wd_HDR_IN", wdDict["HDRtotalIN"])      #[kL/yr]
            currentAttList.addAttribute("wd_HDR_OUT", wdDict["HDRtotalOUT"])    #[kL/yr]
            currentAttList.addAttribute("wd_PrivIN", wdDict["TotalPrivateIN"])  #[kL/yr]
            currentAttList.addAttribute("wd_PrivOUT", wdDict["TotalPrivateOUT"])#[kL/yr]
            
            currentAttList.addAttribute("wd_LI", wdDict["LIDemand"])            #[kL/day]
            currentAttList.addAttribute("wd_HI", wdDict["HIDemand"])            #[kL/day]
            currentAttList.addAttribute("wd_COM", wdDict["COMDemand"])          #[kL/day]
            currentAttList.addAttribute("wd_ORC", wdDict["ORCDemand"])          #[kL/day]
            currentAttList.addAttribute("wd_Nres_IN", wdDict["TotalNonResDemand"]) #[kL/yr]
            
            currentAttList.addAttribute("Apub_irr", wdDict["APublicIrrigate"])  #[sqm]
            currentAttList.addAttribute("wd_PubOUT", wdDict["TotalOutdoorPublicWD"]) #[kL/yr]
            currentAttList.addAttribute("Blk_WD", wdDict["TotalBlockWD"])       #[kL/yr]
            currentAttList.addAttribute("Blk_WD_OUT", wdDict["TotalOutdoorWD"]) #[kL/yr]
            currentAttList.addAttribute("Blk_W_LOST", wdDict["TotalLosses"])   #[kL/yr]

            currentAttList.addAttribute("Blk_kitchen", wdDict["Blk_kitchen"])   #[kL/day]
            currentAttList.addAttribute("Blk_shower", wdDict["Blk_shower"])     #[kL/day]
            currentAttList.addAttribute("Blk_toilet", wdDict["Blk_toilet"])     #[kL/day]
            currentAttList.addAttribute("Blk_laundry", wdDict["Blk_laundry"])   #[kL/day]
            currentAttList.addAttribute("Blk_irrigation", wdDict["Blk_irrigation"])     #[kL/day]
            currentAttList.addAttribute("Blk_com", wdDict["Blk_com"])           #[kL/day]
            currentAttList.addAttribute("Blk_ind", wdDict["Blk_ind"])           #[kL/day]
            currentAttList.addAttribute("Blk_publicirri", wdDict["Blk_publicirri"])     #[kL/day]
            currentAttList.addAttribute("Blk_losses", wdDict["Blk_losses"])  #[kL/day]

            self.readjustLandCoverProportions(currentAttList)

        ###-------------------------------------------------------------------###
        #---  INTERMEDIATE LOOP - RECALCULATE IMP AREA TO SERVE
        ###-------------------------------------------------------------------###
        #DETERMINE IMPERVIOUS AREAS TO MANAGE BASED ON LAND USES
        for i in range(int(blocks_num)):
            currentID = i+1
            currentAttList = self.activesim.getAssetWithName("BlockID"+str(currentID))

            if currentAttList.getAttribute("Status") == 0:
                continue
            block_EIA = currentAttList.getAttribute("Blk_EIA")
            if self.service_res == False:
                AimpRes = currentAttList.getAttribute("ResLotEIA") * currentAttList.getAttribute("ResAllots")
                AimpstRes = currentAttList.getAttribute("ResFrontT") - currentAttList.getAttribute("avSt_RES")
                block_EIA -= AimpRes - AimpstRes
            if self.service_hdr == False:
                block_EIA -= currentAttList.getAttribute("HDR_EIA")
            if self.service_com == False:
                block_EIA -= currentAttList.getAttribute("COMAeEIA")
            if self.service_li == False:
                block_EIA -= currentAttList.getAttribute("LIAeEIA")
            if self.service_hi == False:
                block_EIA -= currentAttList.getAttribute("HIAeEIA")

            # print "Block", currentID, "imp: ", block_EIA
            currentAttList.addAttribute("Manage_EIA", block_EIA)

        ###-------------------------------------------------------------------###
        #---  SECOND LOOP - RETROFIT ALGORITHM
        ###-------------------------------------------------------------------###
        totsystems = self.activesim.getAssetWithName("SysPrevGlobal").getAttribute("TotalSystems")
        ubeatsfile = self.activesim.getAssetWithName("SysPrevGlobal").getAttribute("UBFile")

        self.notify("Total Systems in Map: "+str(totsystems))

        sysIDs = self.activesim.getAssetsWithIdentifier("SysPrevID")
        #Grab the list of systems and sort them based on location into a dictionary
        system_list = {}        #Dictionary
        for i in range(int(blocks_num)):
            system_list[i+1] = []
        for i in range(len(sysIDs)):
            curSys = sysIDs[i]
            locate = int(curSys.getAttribute("Location"))
            system_list[locate].append(curSys)  #Block ID [5], [curSys, curSys, curSys]

        #Do the retrofitting
        for i in range(int(blocks_num)):
            currentID = i+1
            currentAttList = self.activesim.getAssetWithName("BlockID"+str(currentID))
            if currentAttList.getAttribute("Status") == 0:
                continue

            sys_implement = system_list[currentID]
            if len(sys_implement) == 0:
                continue

            if self.retrofit_scenario == "N":
                self.retrofit_DoNothing(currentID, sys_implement)
            elif self.retrofit_scenario == "R":
                self.retrofit_WithRenewal(currentID, sys_implement)
            elif self.retrofit_scenario == "F":
                self.retrofit_Forced(currentID, sys_implement)

        ###-------------------------------------------------------------------###
        #--- THIRD LOOP - OPPORTUNITIES MAPPING OF INDIVIDUAL TECHS
        #            ACROSS SCALES & IN-BLOCK TOP RANKED OPTIONS (ACROSS BLOCKS)                         #
        ###-------------------------------------------------------------------###

        #INITIALIZE THE DATABASE
        #INITIALIZE THE DATABASE ---- COMMENT FROM HERE TO REMOVE DATABASE WRITING
        #
        #DEBUG - Database path
        # ubdbpath = self.temp_dir+"/ubeatsdb1.db"
        # if os.path.isfile(ubdbpath):
        #     try:
        #         os.remove(ubdbpath)     #Attempts to remove the file, if it fails, it creates another with an incremented
        #     except:                     #index.
        #         ubdbpath = self.temp_dir+"/ubeatsdb"+str(int(ubdbpath[len(ubdbpath)-4])+1)+".db"
        #
        # self.sqlDB = sqlite3.connect(ubdbpath)
        # self.dbcurs = self.sqlDB.cursor()
        #
        # #Create Table for Individual Systems
        # self.dbcurs.execute("CREATE TABLE watertechs(BlockID,Type,Size,Scale,Aimpdesign,Service,Areafactor,Landuse,Designdegree,Recycled,Integrated,Storetype,Storesize,qtyIAO,wqIAO)")
        # self.dbcurs.execute("CREATE TABLE blockstrats(BlockID,Bin,RESType,RESQty,RESservice,HDRType,HDRQty,HDRService,LIType,LIQty,LIService,HIType,HIQty,HIService,COMType,COMQty,COMService,StreetType,StreetQty,StreetService,NeighType,NeighQty,NeighService,TotService,MCATech,MCAEnv,MCAEcn,MCASoc,MCATotal,ImpTotal)")
        # self.dbcurs.execute("CREATE TABLE blockstratstop(BlockID,Bin,RESType,RESQty,RESservice,HDRType,HDRQty,HDRService,LIType,LIQty,LIService,HIType,HIQty,HIService,COMType,COMQty,COMService,StreetType,StreetQty,StreetService,NeighType,NeighQty,NeighService,TotService,MCATech,MCAEnv,MCAEcn,MCASoc,MCATotal,ImpTotal)")
        # #END OF DATABASE STUFF ------ COMMENT OUT UNTIL HERE TO REMOVE DATABASE WRITING

        inblock_options = {}
        subbas_options = {}

        #Initialize increment variables
        self.notify(str(self.lot_rigour)+" "+str(self.street_rigour)+" "+str(self.neigh_rigour)+" "+str(self.subbas_rigour))
        self.lot_incr = self.setupIncrementVector(self.lot_rigour)
        self.street_incr = self.setupIncrementVector(self.street_rigour)
        self.neigh_incr = self.setupIncrementVector(self.neigh_rigour)
        self.subbas_incr = self.setupIncrementVector(self.subbas_rigour)
        self.notify(str(self.lot_incr)+" "+str(self.street_incr)+" "+str(self.neigh_incr)+" "+str(self.subbas_incr))

        if bool(self.ration_harvest):   #if harvest is a management objective
            #Initialize meteorological data vectors: Load rainfile and evaporation files,
            #create the scaling factors for evap data
            self.notify("Loading Climate Data... ")
            self.raindata = ubseries.loadClimate(self.rainfile, 1440, self.rain_length)
            self.evapdata = ubseries.loadClimate(self.evapfile, 1440, self.rain_length)

            #self.raindata = ubseries.loadClimateFile(self.rainfile, "csv", self.rain_dt, 1440, self.rain_length)
            #self.evapdata = ubseries.loadClimateFile(self.evapfile, "csv", self.evap_dt, 1440, self.rain_length)

            self.evapscale = ubseries.convertClimateToScalars(self.evapdata, "SUB", 0)

            #self.evapscale = ubseries.convertVectorToScalingFactors(self.evapdata)
            #self.raindata = ubseries.removeDateStampFromSeries(self.raindata, 2)             #Remove the date stamps
            self.raindata = ubseries.removeDateStampFromSeries(self.raindata, 1)            #Removes the date stamps

        for i in range(int(blocks_num)):
            currentID = i+1
            self.notify("Currently on Block "+str(currentID))
            currentAttList = self.activesim.getAssetWithName("BlockID"+str(currentID))
            if currentAttList.getAttribute("Status") == 0:
                self.notify("Block not active in simulation")
                continue

            #INITIALIZE VECTORS
            lot_techRES = [0]
            lot_techHDR = [0]
            lot_techLI = [0]
            lot_techHI = [0]
            lot_techCOM = [0]
            street_tech = [0]
            neigh_tech = [0]
            subbas_tech = {}    #initialised as empty


            #Assess Opportunities and Calculate SWH Benefits

            #Assess Lot Opportunities
            if len(techListLot) != 0:
                lot_techRES, lot_techHDR, lot_techLI, lot_techHI, lot_techCOM = self.assessLotOpportunities(techListLot, currentAttList)
            #self.notify(lot_techRES)
            #self.notify(lot_techHDR)
            #self.notify(lot_techLI)
            #self.notify(lot_techHI)
            #self.notify(lot_techCOM)

            #Assess Street Opportunities
            if len(techListStreet) != 0:
                street_tech = self.assessStreetOpportunities(techListStreet, currentAttList)
            #self.notify(street_tech)

            #Assess Neigh Opportunities
            if len(techListNeigh) != 0:
                neigh_tech = self.assessNeighbourhoodOpportunities(techListNeigh, currentAttList)
            #self.notify(neigh_tech)

            #Assess Precinct Opportunities
            if len(techListSubbas) != 0:
                subbas_tech = self.assessSubbasinOpportunities(techListSubbas, currentAttList)
            #self.notify(subbas_tech)

            subbas_options["BlockID"+str(currentID)] = subbas_tech

            #--- THIRD LOOP - CONSTRUCT IN-BLOCK OPTIONS
            inblock_options["BlockID"+str(currentID)] = self.constructInBlockOptions(currentAttList, lot_techRES, lot_techHDR, lot_techLI, lot_techHI, lot_techCOM, street_tech, neigh_tech)

        #DEBUG - COMMIT THE SQL DATABSE
        #self.sqlDB.commit()     #DATABASE WRITING ----- COMMENT OUT TO REMOVE DATABASE WRITING FUNCTIONALITY
        # DEBUG END

        ###-------------------------------------------------------------------###
        #  FOURTH LOOP - MONTE CARLO (ACROSS BASINS)                            #
        ###-------------------------------------------------------------------###
        gc.collect()

        #DEBUG - Database execute
        #self.dbcurs.execute('''CREATE TABLE basinbrainstorm(BasinID, )''')
        #DEBUG END

        for i in range(int(basins)):
            currentBasinID = i+1
            self.notify("Currently on Basin ID"+str(currentBasinID))

            basinBlockIDs, outletID = self.getBasinBlockIDs(currentBasinID, blocks_num)
            self.notify("basinBlockIDs "+str(basinBlockIDs)+" "+str(outletID))

            dP_QTY, basinRemainQTY, basinTreatedQTY, basinEIA = self.calculateRemainingService("QTY", basinBlockIDs)
            dP_WQ, basinRemainWQ, basinTreatedWQ, basinEIA = self.calculateRemainingService("WQ", basinBlockIDs)
            dP_REC, basinRemainREC, basinTreatedREC, basinDem = self.calculateRemainingService("REC", basinBlockIDs)

            self.notify("Basin Totals: "+str([basinRemainQTY, basinRemainWQ, basinRemainREC]))
            self.notify("Must choose a strategy now that treats: "+str([dP_QTY*100.0, dP_WQ*100.0, dP_REC*100.0])+"% of basin")

            subbasPartakeIDs = self.findSubbasinPartakeIDs(basinBlockIDs, subbas_options) #Find locations of possible WSUD

            updatedService = [dP_QTY, dP_WQ, dP_REC]

            #SKIP CONDITIONS
            if basinRemainQTY == 0.0 and basinRemainWQ == 0.0 and basinRemainREC == 0.0:
                #self.notify("Basin ID: ", currentBasinID, " has no remaining service requirements, skipping!")
                print "Transferring existing systems across"
                for stratnum in range(int(self.num_output_strats)):
                    self.transferExistingSystemsToOutput(int(stratnum+1), 0, currentBasinID)
                continue
            if sum(updatedService) == 0:
                print "Transferring existing systems across"
                for stratnum in range(int(self.num_output_strats)):
                    self.transferExistingSystemsToOutput(int(stratnum+1), 0, currentBasinID)
                continue

            iterations = self.maxMCiterations   #MONTE CARLO ITERATIONS - CAN SET TO SENSITIVITY VALUE IN FUTURE RELATIVE TO BASIN SIZE

            if len(basinBlockIDs) == 1: #if we are dealing with a single-block basin, reduce the number of iterations
                iterations = self.maxMCiterations/10        #If only one block in basin, do different/smaller number of iterations
            #Begin Monte Carlo
            basin_strategies = []
            for iteration in range(iterations):   #1000 monte carlo simulations
                self.notify("Current Iteration No. "+str(iteration+1))
                #Draw Samples
                subbas_chosenIDs, inblocks_chosenIDs = self.selectTechLocationsByRandom(subbasPartakeIDs, basinBlockIDs)
                #self.notify("Selected Locations: Subbasins ", subbas_chosenIDs, " In Blocks ", inblocks_chosenIDs

                #Create the Basin Management Strategy Object
                current_bstrategy = tt.BasinManagementStrategy(iteration+1, currentBasinID,
                                                               basinBlockIDs, subbasPartakeIDs,
                                                               [basinRemainQTY, basinRemainWQ, basinRemainREC])

                #Populate Basin Management Strategy Object based on the current sampled values
                self.populateBasinWithTech(current_bstrategy, subbas_chosenIDs, inblocks_chosenIDs,
                                           inblock_options, subbas_options, basinBlockIDs)

                tt.updateBasinService(current_bstrategy)
                #self.notify(current_bstrategy.getSubbasinArray())
                #self.notify(current_bstrategy.getInBlocksArray())

                tt.calculateBasinStrategyMCAScores(current_bstrategy,self.curscalepref, self.priorities, self.mca_techlist, self.mca_tech, \
                                                  self.mca_env, self.mca_ecn, self.mca_soc, \
                                                      [self.bottomlines_tech_w, self.bottomlines_env_w, \
                                                               self.bottomlines_ecn_w, self.bottomlines_soc_w], self.iao_influence/100.0)

                #Add basin strategy to list of possibilities
                service_objfunc = self.evaluateServiceObjectiveFunction(current_bstrategy, updatedService)        #Calculates how well it meets the total service

                self.penalizeMCAscore(current_bstrategy, self.score_strat, updatedService)

                basin_strategies.append([service_objfunc,current_bstrategy.getServicePvalues(), current_bstrategy.getTotalMCAscore(), current_bstrategy])

            #Pick the final option by narrowing down the list and choosing (based on how many
            #need to be chosen), sort and grab the top ranking options
            basin_strategies.sort()
            self.notify(basin_strategies)
            self.debugPlanning(basin_strategies, currentBasinID)
            acceptable_options = []
            for j in range(len(basin_strategies)):
                if basin_strategies[j][0] < 0:  #if the OF is <0 i.e. -1, skip
                    continue
                else:
                    acceptable_options.append(basin_strategies[j])
            #self.notify(acceptable_options)
            if self.ranktype == "RK":
                acceptable_options = acceptable_options[0:int(self.topranklimit)]
            elif self.ranktype == "CI":
                acceptableN = int(len(acceptable_options)*(1.0-float(self.conf_int)/100.0))
                acceptable_options = acceptable_options[0:acceptableN]

            topcount = len(acceptable_options)
            acceptable_options.sort(key=lambda score: score[2], reverse=True)
            self.notify(acceptable_options)

            #Choose final option
            numselect = min(topcount, self.num_output_strats)   #Determines how many options out of the matrix it should select
            final_selection = []
            if self.pickingmethod == "TOP":
                checkvar = []
                for j in range(int(numselect)):
                    checkvar.append(acceptable_options[j])
                    final_selection.append([acceptable_options[j][3],acceptable_options[j][2]]) #[strategy object, score]
                print checkvar
            elif self.pickingmethod == "RND":
                for j in range(int(numselect)):
                    score_matrix = []       #Create the score matrix
                    for opt in acceptable_options:
                        score_matrix.append(opt[2])
                    selection_cdf = self.createCDF(score_matrix)    #Creat the CDF
                    choice = self.samplefromCDF(selection_cdf)
                    final_selection.append([acceptable_options[choice][3],acceptable_options[j][2]])   #[strategy object , score]
                    acceptable_options.pop(choice)  #Pop the option at the selected index from the matrix
                    #Repeat for as many options as requested

            #Write WSUD strategy attributes to output vector for that block
            self.notify(final_selection)
            if len(final_selection) == 0:
                self.transferExistingSystemsToOutput(1, 0, currentBasinID)
                #If there are no additional plans, just transfer systems across, only one output as StrategyID1

            for j in range(len(final_selection)):       #Otherwise it'll loop
                cur_strat = final_selection[j]
                stratID = j+1
                self.writeStrategyView(stratID, currentBasinID, basinBlockIDs, cur_strat)
                self.transferExistingSystemsToOutput(stratID, cur_strat[1], currentBasinID)

            #Clear the array and garbage collect
            basin_strategies = []
            acceptable_options = []
            final_selection = []
            gc.collect()
            #END OF BASIN LOOP, continues to next basin

#        output_log_file.write("End of Basin Strategies Log \n\n")
#        output_log_file.close()

        #DEBUG - CLOSE THE SQL DATABASE
        #self.sqlDB.close()      #Close the database
        #DEBUG END

        #END OF MODULE
        
    ########################################################
    #    TECHPLACEMENT SUBFUNCTIONS                        #
    ########################################################

    ######################################
    #--- FUNCTIONS FOR PRE-PROCESSING ---#
    ######################################
    def compileUserTechList(self):
        """Compiles a dictionary of the technologies the user should use and at
        what scales these different technologies should be used. Results are 
        presented as a dictionary:
            userTechList = { "TechAbbreviation" : [boolean, boolean, boolean, boolean], }
                            each boolean corresponds to one of the four scales in the order
                            lot, street, neighbourhood, sub-basin
        """
        userTechList = {}
        for j in self.technames:
            if eval("self."+j+"status == 1"):
                userTechList[j] = [0,0,0,0]
                for k in range(len(self.scaleabbr)):
                    k_scale = self.scaleabbr[k]
                    try:
                        if eval("self."+str(j)+str(k_scale)+"==1"):
                            userTechList[j][k] = 1
                    except NameError:
                        pass
                    except AttributeError:
                        pass
        return userTechList
    
    
    def fillScaleTechList(self, scale, userTechList):
        """Returns a vector of tech abbreviations for a given scale of application
        by scanning the userTechList dictionary. Used to fill out the relevant variables
        that will be called when assessing opportunities
            - Inputs: scale (the desired scale to work with, note that subbas and prec are interchangable)
                    userTechList (the created dictionary output from self.compileUserTechList()
        """
        techlist = []
        if eval("self.strategy_"+scale+"_check") == 1:
            if scale == "subbas":
                scalelookup = "prec"
            else:
                scalelookup = scale
            scaleindex = self.scaleabbr.index(scalelookup)
            for key in userTechList.keys():
                if userTechList[key][scaleindex] == 1:
                    techlist.append(key)
                else:
                    pass
            return techlist
        else:
            return techlist


    def retrieveMCAscoringmatrix(self):
        """Retrieves the Multi-Criteria Assessment Scoring Matrix from either the file
        or the default UrbanBEATS values. Returns the vector data containing all scores.
        """
        mca_scoringmatrix, mca_tech, mca_env, mca_ecn, mca_soc = [], [], [] ,[] ,[]
        if self.scoringmatrix_default:
            mca_fname = self.ubeatsdir+"/ancillary/mcadefault.csv"  #uses UBEATS default matrix
            #Do something to retrieve UrbanBEATS default matrix, specify default path            
        else:
            mca_fname = self.scoringmatrix_path #loads file
        
        f = open(str(mca_fname), 'r')
        for lines in f:
            readingline = lines.split(',')
            readingline[len(readingline)-1] = readingline[len(readingline)-1].rstrip()
            #self.notify(readingline)
            mca_scoringmatrix.append(readingline)
        f.close()
        total_metrics = len(mca_scoringmatrix[0])-1    #total number of metrics
        total_tech = len(mca_scoringmatrix)-1          #for total number of technologies
        
        #Grab index of technologies to relate to scores
        mca_techlist = []
        for i in range(len(mca_scoringmatrix)):
            if i == 0:
                continue        #Skip the header line
            mca_techlist.append(mca_scoringmatrix[i][0])
            
        metrics = [self.bottomlines_tech_n, self.bottomlines_env_n, self.bottomlines_ecn_n, self.bottomlines_soc_n]
        if total_metrics != sum(metrics):
            self.notify("Warning, user-defined number of metrics does not match that of loaded file! Attempting to identify metrics!")
            metrics, positions = self.identifyMCAmetriccount(mca_scoringmatrix[0])
        else:
            self.notify("User-defined number of metrics matches that of loaded file!")
            metrics = [self.bottomlines_tech_n, self.bottomlines_env_n, self.bottomlines_ecn_n, self.bottomlines_soc_n, 0]
            techpos, envpos, ecnpos, socpos = [], [], [], []
            poscounter = 1
            for i in range(int(self.bottomlines_tech_n)):
                techpos.append(int(poscounter))
                poscounter += 1
            for i in range(int(self.bottomlines_env_n)):
                envpos.append(int(poscounter))
                poscounter += 1
            for i in range(int(self.bottomlines_ecn_n)):
                ecnpos.append(int(poscounter))
                poscounter += 1
            for i in range(int(self.bottomlines_soc_n)):
                socpos.append(int(poscounter))
                poscounter += 1
            positions = [techpos, envpos, ecnpos, socpos, []]
                
        for lines in range(len(mca_scoringmatrix)):
            if lines == 0:
                continue
            mca_tech.append(self.filloutMCAscorearray(mca_scoringmatrix[lines], metrics[0], positions[0]))
            mca_env.append(self.filloutMCAscorearray(mca_scoringmatrix[lines], metrics[1], positions[1]))
            mca_ecn.append(self.filloutMCAscorearray(mca_scoringmatrix[lines], metrics[2], positions[2]))
            mca_soc.append(self.filloutMCAscorearray(mca_scoringmatrix[lines], metrics[3], positions[3]))
        
        for i in ["tech", "env", "ecn", "soc"]:                     #Runs the check if the criteria was selected
            if eval("self.bottomlines_"+str(i)) == False:           #if not, creates a zero-length empty array
                exec("mca_"+str(i)+" = []")
        
        mca_tech = self.rescaleMCAscorelists(mca_tech)
        mca_env = self.rescaleMCAscorelists(mca_env)
        mca_ecn = self.rescaleMCAscorelists(mca_ecn)
        mca_soc = self.rescaleMCAscorelists(mca_soc)
        return mca_techlist, mca_tech, mca_env, mca_ecn, mca_soc

    def penalizeMCAscore(self, bstrategy, method, services):
        """Penalty function that modifies the MCA score of the total basin strategy based on the required service
        level. There are three possible methods:
            (1) SNP - no penalty, nothing happens,
            (2) SLP - linear penalty function: revised score = current_score - (a*diff._service)*current_score
            (3) SPP - non-linear penalty as a power function: revised score = current_score - (a*diff._service^b)*current_score
        The coefficients a and b are set in UrbanBEATS' advanced options.
        """
        if method == "SNP":
            return True

        bSvalues = bstrategy.getServicePvalues()
        dSQty = max(0, (bSvalues[0] - services[0])*int(self.penaltyQty))   #only applies to overtreatment
        dSWQ = max(0, (bSvalues[1] - services[1])*int(self.penaltyWQ))
        dSRec = max(0, (bSvalues[2] - services[2])*int(self.penaltyRec))

        if method == "SLP":
            a = 1.0
            bstrategy.setTotalMCAscore(max(0, bstrategy.getTotalMCAscore() - a* sum([dSQty, dSWQ, dSRec]) * bstrategy.getTotalMCAscore()))
        elif method == "SPP":
            a = self.penaltyFa
            b = self.penaltyFb
            bstrategy.setTotalMCAscore(max(0, bstrategy.getTotalMCAscore() - a* pow(sum([dSQty, dSWQ, dSRec]),b)))
        return True


    def identifyMCAmetriccount(self, metriclist):
        """A function to read the MCA file and identify how many technical, environmental
        economics and social metrics have been entered into the list. Returns a vector of
        the suggested correct metric count based on the four different criteria. Note that
        identification of metrics can only be done if the user-defined file has entered
        the criteria titles correctly, i.e. acceptable strings include
            Technical Criteria: "Te#", "Tec#", "Tech#", "Technical#", "Technology#"
                                    or "Technological#"
            Environmental Criteria: "En#", "Env#", "Enviro#", Environ#", Environment#" or
                                    "Environmental#"
            Economics Criteria: "Ec#", "Ecn#", "Econ#", "Economic#", "Economics#" or
                                    "Economical#"
            Social Criteria: "So#", "Soc#", "Social#", "Society#", "Socio#", "Societal#" or
                                    "People#" or "Person#"
        These acceptable strings can either be 'first-letter capitalized', 'all uppsercase'
        or 'all lowercase' format.
        """
        tec, env, ecn, soc, unid = 0,0,0,0,0
        tecpos, envpos, ecnpos, socpos, unidpos = [], [], [], [], []
        
        #List of acceptable strings
        tecstrings = ["Te", "TE", "te", "Tec", "TEC", "tec", "Tech", "TECH", "tech",
                      "Technical", "TECHNICAL", "technical", "Technology", "TECHNOLOGY",
                      "technology", "Technological", "TECHNOLOGICAL", "technological"]
        envstrings = ["En", "EN", "en", "Env", "ENV", "env", "Enviro", "ENVIRO", "enviro",
                      "Environ", "ENVIRON", "environ", "Environment", "ENVIRONMENT",
                      "environment", "Environmental", "ENVIRONMENTAL", "environmental"]
        ecnstrings = ["Ec", "EC", "ec", "Ecn", "ECN", "ecn", "Econ", "ECON", "econ",
                      "Economic", "ECONOMIC", "economic", "Economics", "ECONOMICS", 
                      "economics", "Economical", "ECONOMICAL", "economical"]
        socstrings = ["So", "SO", "so", "Soc", "SOC", "soc", "Social", "SOCIAL", "social",
                      "Society", "SOCIETY", "society", "Socio", "SOCIO", "socio", "Societal",
                      "SOCIETAL", "societal", "People", "PEOPLE", "people", "Person",
                      "PERSON", "person"]
        
        for i in range(len(metriclist)):
            #self.notify(metriclist[i])
            if i == 0:
                continue
            if str(metriclist[i][0:len(metriclist[i])-1]) in tecstrings:
                tec += 1
                tecpos.append(i)
            elif str(metriclist[i][0:len(metriclist[i])-1]) in envstrings:
                env += 1
                envpos.append(i)
            elif str(metriclist[i][0:len(metriclist[i])-1]) in ecnstrings:
                ecn += 1
                ecnpos.append(i)
            elif str(metriclist[i][0:len(metriclist[i])-1]) in socstrings:
                soc += 1
                socpos.append(i)
            else:
                unid += 1
                unidpos.append(i)
        
        criteriametrics = [tec, env, ecn, soc, unid]
        criteriapos = [tecpos, envpos, ecnpos, socpos, unidpos]
        return criteriametrics, criteriapos


    def filloutMCAscorearray(self, line, techcount, techpos):
        """Extracts scores for a particular criteria from a line in the loaded scoring matrix
        and transfers them to the respective array, also converts the value to a float"""
        line_index = []
        #self.notify(line)
        for i in range(int(techcount)):
            line_index.append(float(line[techpos[i]]))
        return line_index


    def rescaleMCAscorelists(self, list):
        """Rescales the MCA scores based on the number of metrics in each criteria. This gives
        each criteria an equal weighting to start with and can then influence the evaluation
        later on with user-defined final criteria weights.
        """
        for i in range(len(list)):
            for j in range(len(list[i])):
                list[i][j] = list[i][j]/len(list[i])
        return list


    ####################################
    #--- WATER DEMAND SUB-FUNCTIONS ---#
    ####################################
    def calculateBlockWaterDemand(self, currentAttList):
        """Calculates the sub-components and total water demand for the current
        Block and writes the information to the attributes list based on current
        settings for usage patterns, water efficiency, etc. Returns a dictionary with
        all the water demand information for the Block"""

        blockKitchen = 0        #Total Kitchen End use  [kL/day]
        blockShower = 0         #Total Shwoer End use
        blockToilet = 0         #Total Toilet End use
        blockLaundry = 0        #Total Laundry End use
        blockIrrigation = 0     #Total Irrigation End use
        blockCom = 0            #Total Commercial/Office End use
        blockInd = 0            #Total Industrial End use
        blockPubIrr = 0         #Total Public Irrigation

        block_TInWD = 0             #Block total indoor water demand
        block_TOutWD = 0            #Block total outdoor water demand
        block_TInPrivWD = 0         #Block total indoor private water demand
        block_TOutPrivWD = 0        #Block Total outdoor private water demand
        block_TOutPubWD = 0         #Block total outdoor public water demand
        block_TotalWD = 0           #Block total water demand
        totalBlockNonResWD = 0      #Block total nonresidential demand
        waterDemandDict = {}
        
        #Determine Efficiency
        blockrating = self.determineBlockWaterRating()
        waterDemandDict["Efficiency"] = blockrating
        flowratesEff = self.retrieveFlowRates(blockrating)  #for areas with water efficiency
        flowratesZero = self.retrieveFlowRates(0)        #for areas without water efficiency
        flowratesVary = [self.demandvary_kitchen/100, self.demandvary_shower/100, self.demandvary_toilet/100, self.demandvary_laundry/100]

        #Residential Water Demand
        if int(currentAttList.getAttribute("HasHouses")):
            #Indoor demands
            if self.WEF_loc_house:
                resflows = flowratesEff
            else:
                resflows = flowratesZero
                
            occup = currentAttList.getAttribute("HouseOccup")
            houses = currentAttList.getAttribute("ResHouses")
            kitchendem, showerdem, toiletdem, laundrydem = self.getResIndoorDemands(occup, resflows, flowratesVary)
            totalHouseIndoor = (kitchendem + showerdem + toiletdem + laundrydem)/1000.0 #[kL/hh/day]
            totalIndoorAnn = totalHouseIndoor*365*houses
            waterDemandDict["RESkitchen"] = round(float(kitchendem*houses/1000.0),2)  #[kL/day]
            blockKitchen += waterDemandDict["RESkitchen"]
            waterDemandDict["RESshower"] = round(float(showerdem*houses/1000.0),2)
            blockShower += waterDemandDict["RESshower"]
            waterDemandDict["REStoilet"] = round(float(toiletdem*houses/1000.0),2)
            blockToilet += waterDemandDict["REStoilet"]
            waterDemandDict["RESlaundry"] = round(float(laundrydem*houses/1000.0),2)
            blockLaundry += waterDemandDict["RESlaundry"]

            #Irrigation demand
            gardenSpace = currentAttList.getAttribute("ResGarden")
            allots = currentAttList.getAttribute("ResAllots")
            irrigationDem = (self.priv_irr_vol * gardenSpace/10000.0) * 1000.0/365.0 * allots  #[kL/day]
            waterDemandDict["RESirrigation"] = round(irrigationDem,2)
            blockIrrigation += waterDemandDict["RESirrigation"]

            totalOutdoorAnn = irrigationDem*365     #[kL/year]
            waterDemandDict["REStotalIN"] = round(totalIndoorAnn,2)
            waterDemandDict["REStotalOUT"] = round(totalOutdoorAnn,2)
            totalRES = totalIndoorAnn + totalOutdoorAnn     #[kL/yr]

            block_TInPrivWD += totalIndoorAnn       #[kL/yr]
            block_TOutPrivWD += totalOutdoorAnn     #[kL/yr]
            block_TInWD += totalIndoorAnn
            block_TOutWD += totalOutdoorAnn
            block_TotalWD += totalRES
        else:
            waterDemandDict["RESkitchen"] = 0
            waterDemandDict["RESshower"] = 0
            waterDemandDict["REStoilet"] = 0
            waterDemandDict["RESlaundry"] = 0
            waterDemandDict["RESirrigation"] = 0
            waterDemandDict["REStotalIN"] = 0
            waterDemandDict["REStotalOUT"] = 0
            
        #HDR Water Demand
        if int(currentAttList.getAttribute("HasFlats")):
            #Indoor Demands
            if self.WEF_loc_apart:
                resflows = flowratesEff
            else:
                resflows = flowratesZero
            
            occup = currentAttList.getAttribute("HDROccup")
            houses = currentAttList.getAttribute("HDRFlats")
            kitchendem, showerdem, toiletdem, laundrydem = self.getResIndoorDemands(occup, resflows, flowratesVary)
            totalFlatIndoor = (kitchendem + showerdem + toiletdem + laundrydem)/1000        #[kL/day]
            totalIndoorAnn = totalFlatIndoor*365*houses
            waterDemandDict["HDRkitchen"] = round(kitchendem*houses/1000,2)
            blockKitchen += waterDemandDict["HDRkitchen"]
            waterDemandDict["HDRshower"] = round(showerdem*houses/1000,2)
            blockShower += waterDemandDict["HDRshower"]
            waterDemandDict["HDRtoilet"] = round(toiletdem*houses/1000,2)
            blockToilet += waterDemandDict["HDRtoilet"]
            waterDemandDict["HDRlaundry"] = round(laundrydem*houses/1000,2)
            blockLaundry += waterDemandDict["HDRlaundry"]
            
            #Irrigation demand
            gardenSpace = currentAttList.getAttribute("HDRGarden")
            irrigationDem = (gardenSpace/10000 * self.priv_irr_vol) * 1000/365        #[kL/day]
            waterDemandDict["HDRirrigation"] = round(irrigationDem,2)
            blockIrrigation += waterDemandDict["HDRirrigation"]

            totalOutdoorAnn = irrigationDem*365 #[kL/yr]
            waterDemandDict["HDRtotalIN"] = round(totalIndoorAnn,2)
            waterDemandDict["HDRtotalOUT"] = round(totalOutdoorAnn,2)
            totalHDR = totalIndoorAnn + totalOutdoorAnn

            block_TInPrivWD += totalIndoorAnn       #[kL/yr]
            block_TOutPrivWD += totalOutdoorAnn     #[kL/yr]
            block_TInWD += totalIndoorAnn
            block_TOutWD += totalOutdoorAnn
            block_TotalWD += totalHDR
        else:
            waterDemandDict["HDRkitchen"] = 0
            waterDemandDict["HDRshower"] = 0
            waterDemandDict["HDRtoilet"] = 0
            waterDemandDict["HDRlaundry"] = 0
            waterDemandDict["HDRirrigation"] = 0
            waterDemandDict["HDRtotalIN"] = 0
            waterDemandDict["HDRtotalOUT"] = 0
        
        waterDemandDict["TotalPrivateIN"] = round(block_TInPrivWD,2)
        waterDemandDict["TotalPrivateOUT"] = round(block_TOutPrivWD, 2)

        #Non-Res Water Demand
        lipublic, hipublic, compublic, orcpublic = 0,0,0,0  #initialize public space variables
        if int(currentAttList.getAttribute("Has_LI")):    
            if self.li_demandunits == 'sqm':
                Afloor = currentAttList.getAttribute("LIAeBldg") * \
                    currentAttList.getAttribute("LIFloors") * \
                        currentAttList.getAttribute("LIestates")
                demand = self.getNonResIndoorDemand(Afloor, self.li_demand, self.li_demandvary/100)
            elif self.li_demandunits == 'cap':
                employed = currentAttList.getAttribute("LIjobs")
                demand = self.getNonResIndoorDemand(employed, self.li_demand, self.li_demandvary/100)
            lipublic = currentAttList.getAttribute("avLt_LI")*currentAttList.getAttribute("LIestates")
            waterDemandDict["LIDemand"] = demand/1000   #[kL/day]
            blockInd += waterDemandDict["LIDemand"]
            totalBlockNonResWD += demand/1000
        else:
            waterDemandDict["LIDemand"] = 0

        if int(currentAttList.getAttribute("Has_HI")):
            if self.hi_demandunits == 'sqm':
                Afloor = currentAttList.getAttribute("HIAeBldg") * \
                    currentAttList.getAttribute("HIFloors")* \
                        currentAttList.getAttribute("HIestates")
                demand = self.getNonResIndoorDemand(Afloor, self.hi_demand, self.hi_demandvary/100)
            elif self.hi_demandunits == 'cap':
                employed = currentAttList.getAttribute("HIjobs")
                demand = self.getNonResIndoorDemand(employed, self.hi_demand, self.hi_demandvary/100)
            hipublic = currentAttList.getAttribute("avLt_HI")*currentAttList.getAttribute("HIestates")
            waterDemandDict["HIDemand"] = demand/1000   #[kL/day]
            blockInd += waterDemandDict["HIDemand"]
            totalBlockNonResWD += demand/1000
        else:
            waterDemandDict["HIDemand"] = 0
            
        if int(currentAttList.getAttribute("Has_Com")):
            if self.com_demandunits == 'sqm':
                Afloor = currentAttList.getAttribute("COMAeBldg") * \
                    currentAttList.getAttribute("COMFloors")* \
                        currentAttList.getAttribute("COMestates")
                demand = self.getNonResIndoorDemand(Afloor, self.com_demand, self.com_demandvary/100)
            elif self.com_demandunits == 'cap':
                employed = currentAttList.getAttribute("COMjobs")
                demand = self.getNonResIndoorDemand(employed, self.com_demand, self.com_demandvary/100)
            compublic = currentAttList.getAttribute("avLt_COM")*currentAttList.getAttribute("COMestates")
            waterDemandDict["COMDemand"] = demand/1000
            blockCom += waterDemandDict["COMDemand"]
            totalBlockNonResWD += demand/1000
        else:
            waterDemandDict["COMDemand"] = 0
            
        if int(currentAttList.getAttribute("Has_ORC")):
            if self.com_demandunits == 'sqm':
                Afloor = currentAttList.getAttribute("ORCAeBldg") * \
                    currentAttList.getAttribute("ORCFloors") * \
                        currentAttList.getAttribute("ORCestates")
                demand = self.getNonResIndoorDemand(Afloor, self.com_demand, self.com_demandvary/100)
            elif self.com_demandunits == 'cap':
                employed = currentAttList.getAttribute("ORCjobs")
                demand = self.getNonResIndoorDemand(employed, self.com_demand, self.com_demandvary/100)
            orcpublic = currentAttList.getAttribute("avLt_ORC")*currentAttList.getAttribute("ORCestates")
            waterDemandDict["ORCDemand"] = demand/1000
            blockCom += waterDemandDict["COMDemand"]
            totalBlockNonResWD += demand/1000
        else:
            waterDemandDict["ORCDemand"] = 0
            
        waterDemandDict["TotalNonResDemand"] = totalBlockNonResWD*(52*5)        #52 weeks a yr, 5 days a week working [kL/yr]
        block_TotalWD += totalBlockNonResWD*(52*5)

        pa_nonres = (lipublic + hipublic + compublic + orcpublic)*self.irrigate_nonres     #pa = public area outdoor
        waterDemandDict["APublicNonRes"] = pa_nonres
        
        #Public Open Space
        pa_parks = currentAttList.getAttribute("AGardens")* self.irrigate_parks
        pa_ref = currentAttList.getAttribute("REF_av")*self.irrigate_refs
        waterDemandDict["APublicPG"] = pa_parks
        waterDemandDict["APublicRef"] = pa_ref

        totalPublicSpace = pa_nonres + pa_parks + pa_ref
        waterDemandDict["APublicIrrigate"] = totalPublicSpace
        if totalPublicSpace <= 0:
            pass    #No irrigation demand
        else:
            block_TOutPubWD += totalPublicSpace/10000 * self.public_irr_vol * 1000  #[kL/yr]
            blockPubIrr += block_TOutPubWD / 365    #[kL/day]
            block_TOutWD += block_TOutPubWD
            block_TotalWD += block_TOutPubWD
        
        waterDemandDict["TotalOutdoorPublicWD"] = block_TOutPubWD
        waterDemandDict["TotalOutdoorWD"] = block_TOutWD
        waterDemandDict["TotalBlockWD"] = block_TotalWD

        # Losses
        totalLosses = float(self.LOSS_amount / 100.0) * self.LOSS_status * waterDemandDict["TotalBlockWD"]
        waterDemandDict["TotalLosses"] = totalLosses

        waterDemandDict["Blk_kitchen"] = blockKitchen
        waterDemandDict["Blk_shower"] = blockShower
        waterDemandDict["Blk_toilet"] = blockToilet
        waterDemandDict["Blk_laundry"] = blockLaundry
        waterDemandDict["Blk_irrigation"] = blockIrrigation
        waterDemandDict["Blk_com"] = blockCom
        waterDemandDict["Blk_ind"] = blockInd
        waterDemandDict["Blk_publicirri"] = blockPubIrr
        waterDemandDict["Blk_losses"] = totalLosses/ 365.0  # Convert to [kL/day]
        return waterDemandDict


    def determineBlockWaterRating(self):
        """Determine the efficiency of the indoor appliances based on user 
        inputs. Several options available including different sampling distirbutions."""
        if self.WEFstatus == 0:
            return 0
        elif self.WEF_method == "C":
            return self.WEF_c_rating
        elif self.WEF_method == "D":
            maxrating = self.WEF_d_rating
            minrating = 1   #initialize then check if zero is to be included and revise
            if self.WEF_includezero:
                minrating = 0
            if self.WEF_distribution == "UF":
                return int(random.randint(minrating, maxrating))
            #Not uniform distribution --> Use Normal Variations instead
            mu = (minrating + maxrating)/2         #mean is in the 'centre of the distribution'
            sigma = (maxrating - minrating)*0.63/2      #63% of data lies within +/- 1 stdev of the mean
            samplerating = -1   #initialize
            while samplerating < minrating or samplerating > maxrating:
                if self.WEF_distribution == "NM":
                    samplerating = int(random.normalvariate(mu, sigma))
                elif self.WEF_distribution == "LL":
                    samplerating = int(random.normalvariate(log(mu), log(sigma)))
                elif self.WEF_distribution == "LH":
                    samplerating = int(random.normalvariate(log(mu), log(sigma)))
                    samplerating = (maxrating + minrating) - samplerating #Reverse the rating
            return samplerating
        self.notify("Error with blockwater rating function")
        return 0


    def retrieveFlowRates(self, rating):
        """Retrieves the flow rates for the given rating input from the collection of flow 
        rates depending on the type of rating system used."""
        #AS6400 Rating - Units in [L/min] for end uses with duration and L for the rest
        #       - Toilet : Average flush volume used (do not differentiate between full/half)
        #       - Laundry: 5kg Load capacity assumes as the mid-range
        frdAS6400 = {"Kitchen": [16.0,12.0,9.0,7.5,6,4.5,4.5],
                    "Toilet": [11,5.5,4.5,4.0,3.5,3.0,2.5],
                    "Shower": [16.0,12.0,9.0,7.5,6.0,4.5,4.5],
                    "Laundry": [200,150,105,73.5,51.5,36.0,25.2] }

        frdUSEPA = {"Kitchen": [8.3, 0.0, 0.0, 0.0, 0, 0.0, 0.0],
                    "Toilet": [6.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                    "Shower": [9.46, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                    "Laundry": [269.0, 0, 0, 0, 0, 0.0, 0.0] }

        #Other ratings dictionaries
        if self.WEF_rating_system == "AS":
            return [frdAS6400["Kitchen"][int(rating)], frdAS6400["Toilet"][int(rating)],
                    frdAS6400["Shower"][int(rating)], frdAS6400["Laundry"][int(rating)]]
        elif self.WEF_rating_system == "Others":
            return [frdAS6400["Kitchen"][int(rating)], frdAS6400["Toilet"][int(rating)],
                    frdAS6400["Shower"][int(rating)], frdAS6400["Laundry"][int(rating)]]
        elif self.WEF_rating_system == "USEPA":
            return [frdUSEPA["Kitchen"][int(rating)], frdUSEPA["Toilet"][int(rating)],
                    frdUSEPA["Shower"][int(rating)], frdUSEPA["Laundry"][int(rating)]]
        return True


    def getResIndoorDemands(self, occup, flowrates, flowvary):
        """Calculates and varies indoor demands based on input occupancy and flowrates.
        Returns four values of demands for kitchen, shower, toilet and laundry end uses"""
        kitchendem = self.freq_kitchen * self.dur_kitchen * occup * flowrates[0]
        showerdem = self.freq_shower * self.dur_shower * occup * flowrates[1]
        toiletdem = self.freq_toilet * occup * flowrates[2]
        laundrydem = self.freq_laundry * flowrates[3]    #for total household
       
        #Vary demands
        kitchendemF = -1
        while kitchendemF <= 0:
            kitchendemF = kitchendem + random.uniform(kitchendem*flowvary[0]*(-1),
                                                 kitchendem*flowvary[0])
        showerdemF = -1
        while showerdemF <= 0:
            showerdemF = showerdem + random.uniform(showerdem*flowvary[1]*(-1),
                                               showerdem*flowvary[1])
        toiletdemF = -1
        while toiletdemF <= 0:
            toiletdemF = toiletdem + random.uniform(toiletdem*flowvary[2]*(-1),
                                               toiletdem*flowvary[2])
        laundrydemF = -1
        while laundrydemF <= 0:
            laundrydemF = laundrydem + random.uniform(laundrydem*flowvary[3]*(-1),
                                                 laundrydem*flowvary[3])
        return kitchendemF, showerdemF, toiletdemF, laundrydemF
    
    
    def getNonResIndoorDemand(self, unitvariable, demand, vary):
        """Calculates the total indoor demand based on a single value of [L/sqm/day] and
        adds variation to this value if specified
            - unitvariable = total floor space of the facility [sqm] or total employed at facility [cap]
            - demand = total indoor demand rate [L/sqm/day]
            - vary = proportionate variation +/- value * demand
        """
        demand = unitvariable * demand  #either L/cap/day x capita or L/sqm/day x sqm
        demandF = -1
        while demandF < 0:
            demandF = demand + random.uniform(demand*vary*(-1), demand*vary)
        return demandF

    def readjustLandCoverProportions(self, currentAttList):
        """Checks whether irrigation settings coincide with the land cover definition from the
        previous module and adjusts the land cover proportions accordingly.
        :return:
        """
        if self.irrigate_nonres == 0 or self.public_irr_vol == 0:
            # Move all IG land cover in commercial land uses to DG
            lukeys = ["LI", "HI", "COM", "ORC", "NA", "RD"]
            lckeys = ["LC_LI_", "LC_HI_", "LC_COM_", "LC_ORC_", "LC_NA_", "LC_RD_"]
            keys = []
            for i in range(len(lukeys)):
                if currentAttList.getAttribute("pLU_"+lukeys[i]) != 0.0:
                    keys.append(lckeys[i])
            for i in keys:
                dg = currentAttList.getAttribute(i + "DG")
                ig = currentAttList.getAttribute(i + "IG")
                currentAttList.changeAttribute(i + "DG", dg + ig)
                currentAttList.changeAttribute(i + "IG", 0.0)
        if (self.irrigate_parks == 0 or self.public_irr_vol == 0) and currentAttList.getAttribute("pLU_PG") != 0:
            # Move all IG land cover from parks to DG
            dg = currentAttList.getAttribute("LC_PG_DG")
            ig = currentAttList.getAttribute("LC_PG_IG")
            print "Park stuff: ", dg, ig
            currentAttList.changeAttribute("LC_PG_DG", dg + ig)
            currentAttList.changeAttribute("LC_PG_IG", 0.0)
        if self.irrigate_refs == 0 or self.public_irr_vol == 0:
            lukeys = ["REF", "UND", "SVU"]
            lckeys = ["LC_REF_", "LC_UND_", "LC_SVU_"]
            keys = []
            for i in range(len(lukeys)):
                if currentAttList.getAttribute("pLU_"+lukeys[i]) != 0.0:
                    keys.append(lckeys[i])
            for i in keys:
                dg = currentAttList.getAttribute(i + "DG")
                ig = currentAttList.getAttribute(i + "IG")
                currentAttList.changeAttribute(i + "DG", dg + ig)
                currentAttList.changeAttribute(i + "IG", 0.0)
        if self.priv_irr_vol == 0 and currentAttList.getAttribute("pLU_RES") != 0:
            # Move all IG land cover in RES to DG
            dg = currentAttList.getAttribute("LC_RES_DG")
            ig = currentAttList.getAttribute("LC_RES_IG")
            currentAttList.changeAttribute("LC_RES_DG", dg + ig)
            currentAttList.changeAttribute("LC_RES_IG", 0.0)


    ################################
    #--- RETROFIT SUB-FUNCTIONS ---#
    ################################
    def retrofit_DoNothing(self, ID, sys_implement):
        """Implements the "DO NOTHING" Retrofit Scenario across the entire map Do Nothing:
            Technologies already in place will be left as is
         - The impervious area they already treat will be removed from the outstanding impervious 
            area to be treated
         - The Block will be marked at the corresponding scale as "occupied" so that techopp 
            functions cannot place anything there ('no space case')
        """
        self.notify("Block: "+str(ID))
        self.notify(sys_implement)     #[curSys, curSys, curSys, ...]
        
        #currentAttList = self.getBlockUUID(ID,city)
        currentAttList = self.activesim.getAssetWithName("BlockID"+str(ID))
        inblock_imp_treated = 0 #Initialize to keep track of treated in-block imperviousness
        
        #LOT, STREET, NEIGH Systems
        for luc_code in ["L_RES", "L_HDR", "L_LI", "L_HI", "L_COM", "S", "N"]:
            sys_descr = self.locatePlannedSystems(sys_implement, luc_code)
            if sys_descr == None:       #None found for that particular land use
                inblock_imp_treated += 0
                currentAttList.addAttribute("Has"+str(luc_code)+"Sys", 0)
            else:
                currentAttList.addAttribute("Has"+str(luc_code)+"Sys", 1) #mark the system as having been taken
                self.notify(luc_code+" Location: "+str(sys_descr.getAttribute("Location")))
                Aimplot = currentAttList.getAttribute("ResLotEIA")
                if luc_code == "L_RES":
                    imptreated = min(self.retrieveNewAimpTreated(ID, luc_code, sys_descr), Aimplot)
                else:
                    imptreated = self.retrieveNewAimpTreated(ID, luc_code, sys_descr)
                inblock_imp_treated += imptreated * sys_descr.getAttribute("GoalQty")
                sys_descr.changeAttribute("ImpT", imptreated)   #UNIT IMPERVIOUSNESS TREATED
                sys_descr.changeAttribute("CurImpT", imptreated * sys_descr.getAttribute("Qty"))
                #Do Nothing Scenario: ImpT changes and CurImpT changes, but Status remains 1
                
        currentAttList.addAttribute("ServWQ", inblock_imp_treated)
        inblock_impdeficit = max(currentAttList.getAttribute("Manage_EIA") - inblock_imp_treated, 0)
        currentAttList.addAttribute("DeficitWQ", inblock_impdeficit)
        self.notify("Deficit Area still to treat inblock: "+str(inblock_impdeficit))
        
        #Calculate the maximum degree of lot implementation allowed (no. of houses)
        allotments = currentAttList.getAttribute("ResAllots")
        if allotments == 0:
            max_houses = 0
            self.notify("There are no houses in this Block, therefore no lot-scale systems can be implemented")
        else:
            Aimplot = currentAttList.getAttribute("ResLotEIA")
            self.notify("Allotments = "+str(allotments)+" of each "+str(Aimplot)+" sqm impervious")
            max_houses = min((inblock_impdeficit/Aimplot)/allotments, 1)
        self.notify("A Lot Strategy in this Block would permit a maximum implementation in: "+str(max_houses*100)+"% of houses")
        currentAttList.addAttribute("MaxLotDeg", max_houses)
        
        #PRECINCT SYSTEMS
        sys_descr = self.locatePlannedSystems(sys_implement, "B")
        if sys_descr == None:
            currentAttList.addAttribute("HasBSys", 0)
            currentAttList.addAttribute("ServUpWQ", 0)
        else:
            currentAttList.addAttribute("HasBSys", 1)
            subbasimptreated = self.retrieveNewAimpTreated(ID, "B", sys_descr)
            self.notify("Subbasin Location: "+str(sys_descr.getAttribute("Location")))
            currentAttList.addAttribute("ServUpWQ", subbasimptreated)
            sys_descr.changeAttribute("ImpT", subbasimptreated)
            sys_descr.changeAttribute("CurImpT", subbasimptreated * sys_descr.getAttribute("Qty"))
        return True
    
    
    def retrofit_Forced(self, ID, sys_implement):
        """Implements the "FORCED" Retrofit Scenario across the entire map
        Forced: Technologies at the checked scales are retrofitted depending on the three
         options available: keep, upgrade, decommission
         - See comments under "With Renewal" scenario for further details
        """
        self.notify("Block: "+str(ID))
        self.notify(sys_implement)
        
        #currentAttList = self.getBlockUUID(ID,city)
        currentAttList = self.activesim.getAssetWithName("BlockID"+str(ID))
        inblock_imp_treated = 0 #Initialize to keep track of treated in-block imperviousness
        
        #LOT, STREET & NEIGH
        for luc_code in ["L_RES", "L_HDR", "L_LI", "L_HI", "L_COM", "S", "N"]:
            sys_descr = self.locatePlannedSystems(sys_implement, luc_code)
            
            if sys_descr == None: #Skip condition, no system at the particular scale/luc-code
                inblock_imp_treated += 0
                currentAttList.addAttribute("Has"+str(luc_code)+"Sys", 0)
                continue
            
            oldImp = sys_descr.getAttribute("ImpT")
            decision, newImpT = self.dealWithSystem(currentAttList, sys_descr, luc_code,)
            
            #CONDITIONS THAT WILL FORCE A DECISION == 1
            if luc_code in ["L_RES", "L_HDR", "L_LI", "L_HI", "L_COM"]:
                decision = 1 #YOU CANNOT FORCE RETROFIT ON LOT, SO KEEP THE SYSTEMS
            if luc_code == "S" and self.force_street == 0: #if we do not force retrofit on neighbourhood, just keep the system
                decision = 1
            if luc_code == "N" and self.force_neigh == 0: #if we do not force retrofit on neighbourhood, just keep the system
                decision = 1
        
            if decision == 1:   #KEEP SYSTEM
                currentAttList.addAttribute("Has"+str(luc_code)+"Sys", 1)
                Aimplot = currentAttList.getAttribute("ResLotEIA")
                if luc_code == "L_RES":
                    imptreated = min(newImpT, Aimplot)
                else:
                    imptreated = newImpT
                inblock_imp_treated += imptreated
                sys_descr.changeAttribute("ImpT", imptreated)
                sys_descr.changeAttribute("CurImpT", imptreated * sys_descr.getAttribute("Qty"))
            
            elif decision == 2: #RENEWAL
                self.notify("Renewing the System - Redesigning and Assessing Space Requirements")
                newAsys, newEAFact = self.redesignSystem(currentAttList, sys_descr, luc_code, oldImp) #get new system size & EA
                
                #Get available space - depends on scale/luc-code
                if luc_code == "S":
                    avlSpace = currentAttList.getAttribute("avSt_RES")
                elif luc_code == "N":
                    if sys_descr.getAttribute("Type") in ["BF", "WSUR", "PB","RT", "SW", "IS"]: #CHECK WHAT SVU Land use area is available
                        svu_space = currentAttList.getAttribute("SVU_avSW") + currentAttList.getAttribute("SVU_avWS")
                    elif sys_descr.getAttribute("Type") in ["GT"]:
                        svu_space = currentAttList.getAttribute("SVU_avWW")
                    else:
                        svu_space = 0
                    avlSpace = currentAttList.getAttribute("PG_av") + currentAttList.getAttribute("REF_av") + svu_space
                
                if newAsys > avlSpace and self.renewal_alternative == "K": #if system does not fit and alternative is 'Keep'
                    self.notify("Cannot fit new system design, keeping old design instead")
                    currentAttList.addAttribute("Has"+str(luc_code)+"Sys", 1)
                    inblock_imp_treated += newImpT
                    sys_descr.changeAttribute("ImpT", newImpT)
                    sys_descr.changeAttribute("CurImpT", newImpT * sys_descr.getAttribute("Qty"))
                elif newAsys > avlSpace and self.renewal_alternative == "D": #if system does not fit and alternative is 'Decommission'
                    self.notify("Cannot fit new system design, decommissioning instead")
                    inblock_imp_treated += 0 #quite self-explanatory but is added here for clarity
                    currentAttList.addAttribute("Has"+str(luc_code)+"Sys", 1)
                    sys_implement.remove(sys_descr)
                    #city.removeComponent(sys_descr.getUUID())
                    self.activesim.removeAssetByName("SysPrevID"+str(sys_descr.getAttribute("SysID")))
                else: #otherwise it'll fit, transfer new information
                    self.notify("New System Upgrades fit, transferring this information to output")
                    currentAttList.addAttribute("Has"+str(luc_code)+"Sys", 1)
                    self.defineUpgradedSystemAttributes(sys_descr, newAsys, newEAFact, oldImp)
                    inblock_imp_treated += oldImp
                
            elif decision == 3: #DECOMMISSIONING
                self.notify("Decommissioning the system")
                inblock_imp_treated += 0 #quite self-explanatory but is added here for clarity
                #remove all attributes, wipe the attributes entry in techconfigout with a blank attribute object
                currentAttList.addAttribute("Has"+str(luc_code)+"Sys", 0) #Remove system placeholder
                sys_implement.remove(sys_descr)
                #city.removeComponent(sys_descr.getUUID())
                self.activesim.removeAssetByName("SysPrevID"+str(sys_descr.getAttribute("SysID")))
                
        currentAttList.addAttribute("ServWQ", inblock_imp_treated)
        inblock_impdeficit = max(currentAttList.getAttribute("Manage_EIA") - inblock_imp_treated, 0)
        currentAttList.addAttribute("DeficitIA", inblock_impdeficit)
        
        allotments = currentAttList.getAttribute("ResAllots")
        if allotments != 0:
            Aimplot = currentAttList.getAttribute("ResLotEIA")
            self.notify("Allotments = "+str(allotments)+" of each "+str(Aimplot)+" sqm impervious")
            max_houses = min((inblock_impdeficit/Aimplot)/allotments, 1)
            self.notify("A Lot Strategy in this Block would permit a maximum implementation in: "+str(max_houses*100)+"% of houses")
            currentAttList.addAttribute("MaxLotDeg", max_houses)
        else:
            self.notify("No houses in this block")
            currentAttList.addAttribute("MaxLotDeg", 0)
        
        #SUBBASIN
        sys_descr = self.locatePlannedSystems(sys_implement, "B")
        if sys_descr == None:
            currentAttList.addAttribute("HasBSys", 0)
        else:
            oldImp = sys_descr.getAttribute("ImpT")
            decision, newImpT = self.dealWithSystem(currentAttList, sys_descr, "B")
            if self.force_prec == 0: #if we do not force retrofit on precinct, just keep the system
                decision = 1
                
            if decision == 1: #KEEP
                self.notify("Keeping the System")
                currentAttList.addAttribute("HasBSys", 1)
                currentAttList.addAttribute("ServUpWQ", newImpT)
                sys_descr.changeAttribute("ImpT", newImpT)
                sys_descr.changeAttribute("CurImpT", newImpT * sys_descr.getAttribute("Qty"))
            
            elif decision == 2: #RENEWAL
                self.notify("Renewing the System - Redesigning and Assessing Space Requirements")
                newAsys, newEAFact = self.redesignSystem(currentAttList, sys_descr, "B", oldImp) #get new system size & EA
                if sys_descr.getAttribute("Type") in ["BF", "WSUR", "PB","RT", "SW", "IS"]: #CHECK WHAT SVU Land use area is available
                    svu_space = currentAttList.getAttribute("SVU_avSW") + currentAttList.getAttribute("SVU_avWS")
                elif sys_descr.getAttribute("Type") in ["GT"]:
                    svu_space = currentAttList.getAttribute("SVU_avWW")
                else:
                    svu_space = 0
                avlSpace = currentAttList.getAttribute("PG_av") + currentAttList.getAttribute("REF_av") + svu_space
                if newAsys > avlSpace and self.renewal_alternative == "K": #if system does not fit and alternative is 'Keep'
                    self.notify("Cannot fit new system design, keeping old design instead")
                    currentAttList.addAttribute("HasBSys", 1)
                    currentAttList.addAttribute("ServUpWQ", newImpT)
                    sys_descr.changeAttribute("ImpT", newImpT)
                    sys_descr.changeAttribute("CurImpT", newImpT * sys_descr.getAttribute("Qty"))
                elif newAsys > avlSpace and self.renewal_alternative == "D": #if system does not fit and alternative is 'Decommission'
                    self.notify("Cannot fit new system design, decommissioning instead")
                    currentAttList.addAttribute("ServUpWQ", 0)
                    currentAttList.addAttribute("HasBSys", 0) #Remove system placeholder
                    sys_implement.remove(sys_descr)
                    #city.removeComponent(sys_descr.getUUID())
                    self.activesim.removeAssetByName("SysPrevID"+str(sys_descr.getAttribute("SysID")))
                else: #otherwise it'll fit, transfer new information
                    self.notify("New System Upgrades fit, transferring this information to output")
                    currentAttList.addAttribute("HasBSys", 1)
                    self.defineUpgradedSystemAttributes(sys_descr, newAsys, newEAFact, oldImp)
                    currentAttList.addAttribute("ServUpWQ", oldImp)        #OLD IMP BECAUSE THE REDESIGNED SYSTEM IS NOW LARGER
                                                                                #AND BETTER TO HANDLE SAME IMP AREA AS BEFORE!
            elif decision == 3: #DECOMMISSIONING
                self.notify("Decommissioning the system")
                currentAttList.addAttribute("ServUpWQ", 0)
                #remove all attributes, wipe the attributes entry in techconfigout with a blank attribute object
                currentAttList.addAttribute("HasSubbasS", 0)
                sys_implement.remove(sys_descr)
                #city.removeComponent(sys_descr.getUUID())
                self.activesim.removeAssetByName("SysPrevID"+str(sys_descr.getAttribute("SysID")))
        return True


    def retrofit_WithRenewal(self, ID, sys_implement):
        """Implements the "WITH RENEWAL" Retrofit Scenario across the entire map
        With Renewal: Technologies at different scales are selected for retrofitting
         depending on the block's age and renewal cycles configured by the user
         - Technologies are first considered for keeping, upgrading or decommissioning
         - Keep: impervious area they already treat will be removed from the outstanding
         impervious area to be treated and that scale in said Block marked as 'taken'
         - Upgrade: technology targets will be looked at and compared, the upgraded technology
         is assessed and then implemented. Same procedures as for Keep are subsequently
         carried out with the new design
         - Decommission: technology is removed from the area, impervious area is freed up
         scale in said block is marked as 'available'"""

        time_passed = self.currentyear - self.prevyear
        
        self.notify("Block: "+str(ID))
        self.notify(sys_implement)
        
        #currentAttList = self.getBlockUUID(ID,city)
        currentAttList = self.activesim.getAssetWithName("BlockID"+str(ID))
        inblock_imp_treated = 0
        
        if self.renewal_cycle_def == 0:
            self.retrofit_DoNothing(ID, sys_implement) #if no renewal cycle was defined
            return True #go through the Do Nothing Loop instead
            
        #LOT, STREET, NEIGH
        for luc_code in ["L_RES", "L_HDR", "L_LI", "L_HI", "L_COM", "S", "N"]:
            sys_descr = self.locatePlannedSystems(sys_implement, luc_code)
            if sys_descr == None:
                inblock_imp_treated += 0
                currentAttList.addAttribute("Has"+str(luc_code)+"Sys", 0)
                continue
            
            #Get Renewal Cycle Variable
            if luc_code in ["L_RES", "L_HDR", "L_LI", "L_HI", "L_COM"]:
                renewalyears = self.renewal_lot_years
            elif luc_code == "S":
                renewalyears = self.renewal_street_years
            elif luc_code == "N":
                renewalyears = self.renewal_neigh_years
            
            #DO SOMETHING TO DETERMINE IF YES/NO RETROFIT, then check the decision
            if time_passed - (time_passed // renewalyears)*renewalyears == 0:
                go_retrofit = 1 #then it's time for renewal
                self.notify("Before: "+str(sys_descr.getAttribute("GoalQty")))
                #modify the current sys_descr attribute to take into account lot systems that have disappeared.
                #If systems have disappeared the final quantity of lot implementation (i.e. goalqty) will drop
                if luc_code == "L_RES":
                    sys_descr = self.updateForBuildingStockRenewal(currentAttList, sys_descr)
                self.notify("After: "+str(sys_descr.getAttribute("GoalQty")))
            else:
                go_retrofit = 0
                
            #NOW DETERMINE IF ARE RETROFITTING OR NOT: IF NOT READY FOR RETROFIT, KEEP, ELSE GO INTO CYCLE
            oldImp = sys_descr.getAttribute("ImpT") #Old ImpT using the old GoalQty value
            decision, newImpT = self.dealWithSystem(currentAttList, sys_descr, luc_code) #gets the new ImpT using new GoalQty value (if it changed)
            if go_retrofit == 0:        #If the decision is to NOT retrofit yet, then KEEP the system
                decision = 1
                
            if decision == 1: #KEEP
                self.notify("Keeping the System")
                currentAttList.addAttribute("Has"+str(luc_code)+"Sys", 1)
                Aimplot = currentAttList.getAttribute("ResLotEIA")
                if luc_code == "L_RES":
                    imptreated = min(newImpT, Aimplot)
                else:
                    imptreated = newImpT
                inblock_imp_treated += imptreated
                sys_descr.changeAttribute("ImpT", imptreated)
                sys_descr.changeAttribute("CurImpT", imptreated * sys_descr.getAttribute("Qty"))
                
            elif decision == 2: #RENEWAL
                if luc_code in ["L_RES", "L_HDR", "L_COM", "L_LI", "L_HI"]:
                    self.notify("Lot-scale systems will not allow renewal, instead the systems will be kept as is until plan is abandoned")
                    currentAttList.addAttribute("Has"+str(luc_code)+"Sys", 1)
                    Aimplot = currentAttList.getAttribute("ResLotEIA")
                    if luc_code == "L_RES":
                        imptreated = min(newImpT, Aimplot)
                    else:
                        imptreated = newImpT
                    inblock_imp_treated += imptreated
                    sys_descr.changeAttribute("ImpT", imptreated)
                    sys_descr.changeAttribute("CurImpT", imptreated * sys_descr.getAttribute("Qty"))
                    #FUTURE DYNAMICS TO BE INTRODUCED
                else:
                    self.notify("Renewing the System - Redesigning and Assessing Space Requirements")
                    newAsys, newEAFact = self.redesignSystem(currentAttList, sys_descr, luc_code, oldImp) #get new system size & EA
                
                    #Get available space - depends on scale/luc-code
                    if luc_code == "S":
                        avlSpace = currentAttList.getAttribute("avSt_RES")
                    elif luc_code == "N":
                        if sys_descr.getAttribute("Type") in ["BF", "WSUR", "PB","RT", "SW", "IS"]: #CHECK WHAT SVU Land use area is available
                            svu_space = currentAttList.getAttribute("SVU_avSW") + currentAttList.getAttribute("SVU_avWS")
                        elif sys_descr.getAttribute("Type") in ["GT"]:
                            svu_space = currentAttList.getAttribute("SVU_avWW")
                        else:
                            svu_space = 0
                        avlSpace = currentAttList.getAttribute("PG_av") + currentAttList.getAttribute("REF_av") + svu_space
                    
                    if newAsys > avlSpace and self.renewal_alternative == "K": #if system does not fit and alternative is 'Keep'
                        self.notify("Cannot fit new system design, keeping old design instead")
                        currentAttList.addAttribute("Has"+str(luc_code)+"Sys", 1)
                        inblock_imp_treated += newImpT
                        sys_descr.changeAttribute("ImpT", newImpT)
                        sys_descr.changeAttribute("CurImpT", newImpT * sys_descr.getAttribute("Qty"))
                    elif newAsys > avlSpace and self.renewal_alternative == "D": #if system does not fit and alternative is 'Decommission'
                        self.notify("Cannot fit new system design, decommissioning instead")
                        inblock_imp_treated += 0 #quite self-explanatory but is added here for clarity
                        currentAttList.addAttribute("Has"+str(luc_code)+"Sys", 1)
                        sys_implement.remove(sys_descr)
                        self.activesim.removeAssetByName("SysPrevID"+str(sys_descr.getAttribute("SysID")))
                    else: #otherwise it'll fit, transfer new information
                        self.notify("New System Upgrades fit, transferring this information to output")
                        currentAttList.addAttribute("Has"+str(luc_code)+"Sys", 1)
                        self.defineUpgradedSystemAttributes(sys_descr, newAsys, newEAFact, oldImp)
                        inblock_imp_treated += oldImp

            elif decision == 3: #DECOMMISSIONING
                self.notify("Decommissioning the system")
                inblock_imp_treated += 0 #quite self-explanatory but is added here for clarity
                #remove all attributes, wipe the attributes entry in techconfigout with a blank attribute object
                currentAttList.addAttribute("Has"+str(luc_code)+"Sys", 0) #Remove system placeholder
                sys_implement.remove(sys_descr)
                #city.removeComponent(sys_descr.getUUID())
                self.activesim.removeAssetByName("SysPrevID"+str(sys_descr.getAttribute("SysID")))
                
        currentAttList.addAttribute("ServWQ", inblock_imp_treated)
        inblock_impdeficit = max(currentAttList.getAttribute("Manage_EIA") - inblock_imp_treated, 0)
        currentAttList.addAttribute("DeficitIA", inblock_impdeficit)
        
        allotments = currentAttList.getAttribute("ResAllots")
        Aimplot = currentAttList.getAttribute("ResLotEIA")
        self.notify("Allotments = "+str(allotments)+" of each "+str(Aimplot)+" sqm impervious")
        if allotments == 0:
            max_houses = 0
        else:
            max_houses = min((inblock_impdeficit/Aimplot)/allotments, 1)
        self.notify("A Lot Strategy in this Block would permit a maximum implementation in: "+str(max_houses*100)+"% of houses")
        currentAttList.addAttribute("MaxLotDeg", max_houses)
        
        #SUBBASIN
        sys_descr = self.locatePlannedSystems(sys_implement, "B")
        if sys_descr == None:
            currentAttList.addAttribute("HasBSys", 0)
        else:
            #DO SOMETHING TO DETERMINE IF YES/NO RETROFIT, then check the decision
            if time_passed - (time_passed // self.renewal_neigh_years)*self.renewal_neigh_years == 0:
                go_retrofit = 1 #then it's time for renewal
            else:
                go_retrofit = 0 #otherwise do not do anything
                
            #NOW DETERMINE IF ARE RETROFITTING OR NOT: IF NOT READY FOR RETROFIT, KEEP, ELSE GO INTO CYCLE
            oldImp = sys_descr.getAttribute("ImpT")
            decision, newImpT = self.dealWithSystem(currentAttList, sys_descr, "B")
            if go_retrofit == 0:
                decision = 1
                
            if decision == 1: #keep
                self.notify("Keeping the System")
                currentAttList.addAttribute("HasBSys", 1)
                currentAttList.addAttribute("ServUpWQ", newImpT)
                sys_descr.changeAttribute("ImpT", newImpT)
                sys_descr.changeAttribute("CurImpT", newImpT * sys_descr.getAttribute("Qty"))
            
            elif decision == 2: #renewal
                self.notify("Renewing the System - Redesigning and Assessing Space Requirements")
                newAsys, newEAFact = self.redesignSystem(currentAttList, sys_descr, "B", oldImp) #get new system size & EA
                if sys_descr.getAttribute("Type") in ["BF", "WSUR", "PB","RT", "SW", "IS"]: #CHECK WHAT SVU Land use area is available
                    svu_space = currentAttList.getAttribute("SVU_avSW") + currentAttList.getAttribute("SVU_avWS")
                elif sys_descr.getAttribute("Type") in ["GT"]:
                    svu_space = currentAttList.getAttribute("SVU_avWW")
                else:
                    svu_space = 0
                avlSpace = currentAttList.getAttribute("PG_av") + currentAttList.getAttribute("REF_av") + svu_space
                if newAsys > avlSpace and self.renewal_alternative == "K": #if system does not fit and alternative is 'Keep'
                    self.notify("Cannot fit new system design, keeping old design instead")
                    currentAttList.addAttribute("HasBSys", 1)
                    currentAttList.addAttribute("ServUpWQ", newImpT)
                    sys_descr.changeAttribute("ImpT", newImpT)
                    sys_descr.changeAttribute("CurImpT", newImpT * sys_descr.getAttribute("Qty"))
                elif newAsys > avlSpace and self.renewal_alternative == "D": #if system does not fit and alternative is 'Decommission'
                    self.notify("Cannot fit new system design, decommissioning instead")
                    currentAttList.addAttribute("ServUpWQ", 0)
                    currentAttList.addAttribute("HasBSys", 0) #Remove system placeholder
                    sys_implement.remove(sys_descr)
                    #city.removeComponent(sys_descr.getUUID())
                    self.activesim.removeAssetByName("SysPrevID"+str(sys_descr.getAttribute("SysID")))
                else: #otherwise it'll fit, transfer new information
                    self.notify("New System Upgrades fit, transferring this information to output")
                    currentAttList.addAttribute("HasBSys", 1)
                    self.defineUpgradedSystemAttributes(sys_descr, newAsys, newEAFact, oldImp)
                    currentAttList.addAttribute("ServUpWQ", oldImp)        #OLD IMP BECAUSE THE REDESIGNED SYSTEM IS NOW LARGER
                                                                                #AND BETTER TO HANDLE SAME IMP AREA AS BEFORE!
            elif decision == 3: #DECOMMISSIONING
                self.notify("Decommissioning the system")
                currentAttList.addAttribute("ServUpWQ", 0)
                #remove all attributes, wipe the attributes entry in techconfigout with a blank attribute object
                currentAttList.addAttribute("HasSubbasS", 0)
                sys_implement.remove(sys_descr)
                #city.removeComponent(sys_descr.getUUID())
                self.activesim.removeAssetByName("SysPrevID"+str(sys_descr.getAttribute("SysID")))
        return True


    def locatePlannedSystems(self, system_list, scale):
        """Searches the input planned technologies list for a system that fits the scale in the block
        Returns the system attribute list. System_list is a vector of Components [curSys, curSys, curSys]
        """
        for curSys in system_list:
            if curSys.getAttribute("Scale") == scale:
                return curSys
        return None


    def retrieveNewAimpTreated(self, ID, scale, sys_descr):
        """Retrieves the system information for the given scale from the city datastream and
        assesses how well the current system's design can meet the current targets by comparing its
        performance on the design curves.
        """
        #Determine impervious area to deal with depending on scale
        currentAttList = self.activesim.getAssetWithName("BlockID"+str(ID))
        ksat = currentAttList.getAttribute("Soil_k")
        sysexfil = sys_descr.getAttribute("Exfil")
        Asyseff = sys_descr.getAttribute("SysArea")/sys_descr.getAttribute("EAFact")
        wtype = sys_descr.getAttribute("Type")
        #need to be using the effective area, not the planning area
        
        #self.notify("Type: "+str(type)+" AsysEffective: "+str(Asyseff)+"ksat: "+str(ksat))
        
        ### EXCEPTION FOR SWALES AT THE MOMENT WHILE THERE ARE NO DESIGN CURVE FILES ###
        if wtype == "SW":
            return 0
        ### END OF EXCEPTION - CHANGE WHEN DESIGN CURVES ARE AVAILABLE ###
        
        #Grab targets and adjust for particular system type
        #self.notify("Targets: "+str(self.targetsvector))
        
        #Piece together the pathname from current system information: FUTURE
        #NOTE: CURRENT TECH DESIGNS WILL NOT BE CHANGED! THEREFORE PATHNAME WE RETRIEVE FROM
        #DESIGN DETAILS VECTOR LIST

        #Depending on the type of system and classification, will need to retrieve design in different
        #ways
        if wtype in ["BF", "SW", "WSUR", "PB", "IS"]:    #DESIGN by DCV Systems
            sys_perc = dcv.retrieveDesign(self.getDCVPath(wtype), wtype, min(ksat, sysexfil), self.targetsvector)
            #self.notify("Sys Percentage: "+str(sys_perc))
        elif wtype in ["RT", "PP", "ASHP", "GW"]:        #DESIGN by EQN or SIM Systems
            #Other stuff
            sys_perc = np.inf #deq.retrieveDesign(...)
        
        if sys_perc == np.inf:
            #Results - new targets cannot be met, system will not be considered
            #release the imp area, but mark the space as taken!
            imptreatedbysystem = 0
        else:
            #Calculate the system's current Atreated
            imptreatedbysystem = Asyseff/sys_perc
            
#            #Account for Lot Scale as exception
#            if scale in ["L_RES", "L_HDR", "L_LI", "L_HI", "L_COM"]:
#                imptreatedbysystem *= goalqty #imp treated by ONE lot system * the desired qty that can be implemented
#            else:
#                imptreated += imptreatedbysystem
        #self.notify("impervious area treated by system: "+str(imptreatedbysystem))
        return imptreatedbysystem


    def findDCVpath(self, wtype, sys_descr):
        #Finds the correct pathname of the design curve file based on system type and specs
        if wtype in ["IS", "BF"]: #then file = BF-EDDx.xm-FDx.xm.dcv
            pathname = 0
        elif wtype in ["WSUR"]: #then file = WSUR-EDDx.xm.dcv
            pathname = 0
        elif wtype in ["PB"]: #then file = PB-MDx.xm.dcv
            pathname = 0
        return pathname
        
        
    def dealWithSystem(self, currentAttList, sys_descr, scale):
        """Checks the system's feasibility on a number of categories and sets up a decision matrix
        to determine what should be done with the system (i.e. keep, upgrade, decommission). Returns
        a final decision and the newly treated impervious area.
        """
        
        currentID = int(currentAttList.getAttribute("BlockID"))
        scalecheck = [[self.lot_renew, self.lot_decom], 
                      [self.street_renew, self.street_decom], 
                      [self.neigh_renew, self.neigh_decom], 
                      [self.prec_renew, self.prec_decom]]
        
        if scale in ["L_RES", "L_HDR", "L_LI", "L_HI", "L_COM"]:
            scaleconditions = scalecheck[0]
        else:
            scalematrix = ["L", "S", "N", "B"]
            scaleconditions = scalecheck[scalematrix.index(scale)]
        
        decision_matrix = [] #contains numbers of each decision 1=Keep, 2=Renew, 3=Decom
                                    #1st pass: decision based on the maximum i.e. if [1, 3], decommission
        
        ###-------------------------------------------------------
        ### DECISION FACTOR 1: SYSTEM AGE
        ### Determine where the system age lies
        ###-------------------------------------------------------
        sys_yearbuilt = sys_descr.getAttribute("Year")
        sys_type = sys_descr.getAttribute("Type")
        avglife = float(eval("self."+str(sys_type)+"avglife"))
        age = float(self.currentyear - sys_yearbuilt)
        #self.notify("System Age: "+str(age))
        
        if scaleconditions[1] == 1 and age > avglife: #decom
            #self.notify("System too old, decommission")
            decision_matrix.append(3)
        elif scaleconditions[0] == 1 and age > avglife/float(2.0): #renew
            #self.notify("System needs renewal because of age")
            decision_matrix.append(2)
        else: #keep
            decision_matrix.append(1)
        
        ###-------------------------------------------------------
        ### DECISION FACTOR 2: DROP IN PERFORMANCE
        ### Determine where the system performance lies
        ###-------------------------------------------------------
        old_imp = sys_descr.getAttribute("ImpT")
        if old_imp == 0: #This can happen if for example it was found previously that
            perfdeficit = 1.0 #the system can no longer meet new targets, but is not retrofitted because of renewal cycles.
            new_imp = 0
        else:           #Need to catch this happening or else there will be a float division error!
            new_imp = self.retrieveNewAimpTreated(currentID, scale, sys_descr)
            perfdeficit = (old_imp - new_imp)/old_imp
            
        #self.notify("Old Imp: "+str(old_imp))
        #self.notify("New Imp: "+str(new_imp))
        #self.notify("Performance Deficit of System: "+str(perfdeficit))
        
        if scaleconditions[1] == 1 and perfdeficit >= (float(self.decom_thresh)/100.0): #Decom = Checked, threshold exceeded
            #self.notify("System's performance not up to scratch, decommission")
            decision_matrix.append(3)
        elif scaleconditions[0] == 1 and perfdeficit >= (float(self.renewal_thresh)/100.0): #Renew = checked, threshold exceeded
            #self.notify("System's performance ok, needs renewal")
            decision_matrix.append(2)
        else:
            decision_matrix.append(1)
        
        ### MAKE FINAL DECISION ###
        #self.notify(decision_matrix)
        final_decision = max(decision_matrix)           #worst-case chosen, i.e. maximum
                                                    #future passes: more complex decision-making
        return final_decision, new_imp
    
    
    def redesignSystem(self, currentAttList, sys_descr, scale, originalAimpTreated):
        """Redesigns the system for BlockID at the given 'scale' for the original Impervious
        Area that it was supposed to treat, but now according to new targets.
            - ID: BlockID, i.e. the system's location
            - sys_descr: the original vector of the system
            - scale: the letter denoting system scale
            - originalAimpTreated: the old impervious area the system was meant to treat
        """
        type = sys_descr.getAttribute("Type")
        
        #TO BE CHANGED LATER ON, BUT FOR NOW WE ASSUME THIS IS THE SAME PATH
        dcvpath = self.getDCVPath(type)
        #GET THE DCV FILENAME
        #dcvpath = self.findDCVpath(type, sys_descr)
        
        #Some additional arguments for the design function
        maxsize = eval("self."+str(type)+"maxsize")                     #FUTURE >>>>>> MULTI-oBJECTIVE DESIGN
        minsize = eval("self."+str(type)+"minsize")
        soilK = currentAttList.getAttribute("Soil_k")
        systemK = sys_descr.getAttribute("Exfil")
        
        #Current targets
        targets = self.targetsvector
        tech_applications = self.getTechnologyApplications(type)
        purpose = [0, tech_applications[1], 0]

        #Call the design function using eval, due to different system Types
        newdesign = eval('td.design_'+str(type)+'('+str(originalAimpTreated)+',"'+str(dcvpath)+'",'+str(self.targetsvector)+','+str(purpose)+','+str(soilK)+','+str(systemK)+','+str(minsize)+','+str(maxsize)+')')    
        
        Anewsystem = newdesign[0]
        newEAFactor = newdesign[1]
        
        return Anewsystem, newEAFactor


    def defineUpgradedSystemAttributes(self, sys_descr, newAsys, newEAFact, impT):
        """Updates the current component with new attributes based on the newly designed/upgraded
        system at a particular location.
        """
        sys_descr.changeAttribute("SysArea", newAsys)
        sys_descr.changeAttribute("EAFact", newEAFact)
        sys_descr.changeAttribute("ImpT", impT)
        sys_descr.changeAttribute("CurImpT", impT*sys_descr.getAttribute("GoalQty"))
        
        #System was upgraded, add one to the upgrade count
        sys_descr.changeAttribute("Upgrades", sys_descr.getAttribute("Upgrades") + 1)
        return True
    
    
    def updateForBuildingStockRenewal(self, currentAttList, sys_descr):
        """Number of houses removed from area = total currently there * lot_perc
        evenly distribute this across those that have lot system and those that don't
        we therefore end up calculate how many systems lost as lot-perc * how many in place
        """
        self.notify("YEARS")
        self.notify(str(self.currentyear)+" "+str(self.prevyear)+" "+str(self.renewal_lot_years))
        cycles = (float(self.currentyear) - float(self.prevyear)) // float(self.renewal_lot_years)
        self.notify("Cycles"+str( cycles ))
        currentQty = float(sys_descr.getAttribute("Qty"))
        num_lots_lost = currentQty*self.renewal_lot_perc/100*cycles
        newQty = currentQty - num_lots_lost
        goalquantity = sys_descr.getAttribute("GoalQty")
        
        adjustedgoalQty = goalquantity - num_lots_lost
        #Update goal quantity: This is how many we can only reach now because we lost some
        sys_descr.changeAttribute("GoalQty", int(adjustedgoalQty))
        
        #Update current quantity: This is how many current exist in the map
        sys_descr.changeAttribute("Qty", int(newQty))
        return sys_descr
    
    
    ###########################################
    #--- OPPORTUNITY MAPPING SUB-FUNCTIONS ---#
    ###########################################
    def setupIncrementVector(self, increment):
        """A global function for creating an increment list from the user input 'rigour levels'.
        For example:
            - If Rigour = 4
            - Then Increment List will be:  [0, 0.25, 0.5, 0.75, 1.0]
        Returns the increment list
        """
        incr_matrix = [0.0]
        for i in range(int(increment)):
            incr_matrix.append(round(float(1.0/float(increment))*(float(i)+1.0),3))
        return incr_matrix
    
    
    def assessLotOpportunities(self, techList, currentAttList):
        """Assesses if the shortlist of lot-scale technologies can be put into the lot scale
        Does this for one block at a time, depending on the currentAttributesList and the techlist
        """
        currentID = int(currentAttList.getAttribute("BlockID"))
        
        tdRES = [0]     #initialize with one option = no technology = 0
        tdHDR = [0]     #because when piecing together options, we want options where there are
        tdLI = [0]      #no lot technologies at all.
        tdHI = [0]
        tdCOM = [0]
        
        #Check first if there are lot-stuff to work with
        hasHouses = int(currentAttList.getAttribute("HasHouses")) * int(self.service_res)
        lot_avail_sp = currentAttList.getAttribute("avLt_RES") * int(self.service_res)        
        Aimplot = currentAttList.getAttribute("ResLotEIA")          #effective impervious area of one residential allotment
        
        hasApts = int(currentAttList.getAttribute("HasFlats")) * int(self.service_hdr)
        hdr_avail_sp = currentAttList.getAttribute("av_HDRes") * int(self.service_hdr)        
        Aimphdr = currentAttList.getAttribute("HDR_EIA")
        
        hasLI = int(currentAttList.getAttribute("Has_LI")) * int(self.service_li)
        LI_avail_sp = currentAttList.getAttribute("avLt_LI") * int(self.service_li)
        AimpLI = currentAttList.getAttribute("LIAeEIA")
        
        hasHI = int(currentAttList.getAttribute("Has_HI")) * int(self.service_hi)
        HI_avail_sp = currentAttList.getAttribute("avLt_HI") * int(self.service_hi)
        AimpHI = currentAttList.getAttribute("HIAeEIA")
        
        hasCOM = int(currentAttList.getAttribute("Has_Com")) * int(self.service_com)
        com_avail_sp = currentAttList.getAttribute("avLt_COM") * int(self.service_com)
        AimpCOM = currentAttList.getAttribute("COMAeEIA")
        
        #Check SKIP CONDITIONS - return zero matrix if either is true.
        if hasHouses + hasApts + hasLI + hasHI + hasCOM == 0:   #SKIP CONDITION #1 - No Units to build on
            #self.notify("No lot units to build on")
            return tdRES, tdHDR, tdLI, tdHI, tdCOM
        
        if lot_avail_sp + hdr_avail_sp + LI_avail_sp + HI_avail_sp + com_avail_sp < 0.0001:    #SKIP CONDITION #2 - no space
            #self.notify("No lot space to build on")
            return tdRES, tdHDR, tdLI, tdHI, tdCOM
        
        #GET INFORMATION FROM VECTOR DATA
        soilK = currentAttList.getAttribute("Soil_k")               #soil infiltration rate on area
        
        #self.notify("Impervious Area on Lot: "+str(Aimplot))
        #self.notify("Impervious Area on HDR: "+str(Aimphdr))
        #self.notify("Impervious Area on LI: "+str(AimpLI))
        #self.notify("Impervious Area on HI: "+str(AimpHI))
        #self.notify("Impervious Area on COM: "+str(AimpCOM))
        
        #Size the required store to achieve the required potable supply substitution.
        storeVols = []
        if bool(int(self.ration_harvest)):
            store_volRES = self.determineStorageVolForLot(currentAttList, self.raindata, self.evapscale, "RW", "RES")
            store_volHDR = self.determineStorageVolForLot(currentAttList, self.raindata, self.evapscale, "RW", "HDR")
            storeVols = [store_volRES, store_volHDR] #IF 100% service is to occur
            #self.notify(storeVols)
        else:
            storeVols = [np.inf, np.inf]        #By default it is "not possible"
        
        for j in techList:
            tech_applications = self.getTechnologyApplications(j)
            #self.notify("Current Tech: "+str(j)+" applications: "+str(tech_applications))

            minsize = eval("self."+j+"minsize")         #gets the specific system's minimum allowable size
            maxsize = eval("self."+j+"maxsize")          #gets the specific system's maximum size

            #Design curve path
            dcvpath = self.getDCVPath(j)            #design curve file as a string
            #self.notify(dcvpath)
            
            #RES Systems
            hasRESsystems = int(currentAttList.getAttribute("HasL_RESSys"))
            if hasRESsystems == 0 and hasHouses != 0 and Aimplot > 0.0001 and j not in ["banned","list","of","tech"]:    #Do lot-scale house system
                sys_objects = self.designTechnology(1.0, Aimplot, j, dcvpath, tech_applications, soilK, minsize, maxsize, lot_avail_sp, "RES", currentID, storeVols[0])
                for sys_object in sys_objects:
                    tdRES.append(sys_object)
            
            #HDR Systems
            hasHDRsystems = int(currentAttList.getAttribute("HasL_HDRSys"))
            if hasHDRsystems == 0 and hasApts != 0 and Aimphdr > 0.0001 and j not in ["banned","list","of","tech"]:    #Do apartment lot-scale system
                for i in self.lot_incr:
                    if i == 0:
                        continue
                    sys_objects = self.designTechnology(i, Aimphdr, j, dcvpath, tech_applications, soilK, minsize, maxsize, hdr_avail_sp, "HDR", currentID, np.inf)
                    for sys_object in sys_objects:
                        tdHDR.append(sys_object)
            
            #LI Systems
            hasLIsystems = int(currentAttList.getAttribute("HasL_LISys"))  
            if hasLIsystems == 0 and hasLI != 0 and AimpLI > 0.0001 and j not in ["banned","list","of","tech"]:
                for i in self.lot_incr:
                    if i == 0:
                        continue
                    sys_objects = self.designTechnology(i, AimpLI, j, dcvpath, tech_applications, soilK, minsize, maxsize, LI_avail_sp, "LI", currentID, np.inf)
                    for sys_object in sys_objects:
                        tdLI.append(sys_object)
            
            #HI Systems                        
            hasHIsystems = int(currentAttList.getAttribute("HasL_HISys"))
            if hasHIsystems == 0 and hasHI != 0 and AimpHI > 0.0001 and j not in ["banned","list","of","tech"]:
                for i in self.lot_incr:
                    if i == 0:
                        continue
                    sys_objects = self.designTechnology(i, AimpHI, j, dcvpath, tech_applications, soilK, minsize, maxsize, HI_avail_sp, "HI", currentID, np.inf)
                    for sys_object in sys_objects:
                        tdHI.append(sys_object)
            
            #COM Systems
            hasCOMsystems = int(currentAttList.getAttribute("HasL_COMSys"))
            if hasCOMsystems == 0 and hasCOM != 0 and AimpCOM > 0.0001 and j not in ["banned","list","of","tech"]:
                for i in self.lot_incr:
                    if i == 0:
                        continue
                    sys_objects = self.designTechnology(i, AimpCOM, j, dcvpath, tech_applications, soilK, minsize, maxsize, com_avail_sp, "COM", currentID, np.inf)
                    for sys_object in sys_objects:
                        tdCOM.append(sys_object)
            
            #Can insert more land uses here in future e.g. municipal
        return tdRES, tdHDR, tdLI, tdHI, tdCOM    
    
    
    def assessStreetOpportunities(self, techList, currentAttList):
        """Assesses if the shortlist of street-scale technologies can be put into the streetscape
        Does this for one block at a time, depending on the currentAttributesList and the techlist
        """
        currentID = int(currentAttList.getAttribute("BlockID"))
        technologydesigns = [0]
         
        #Check first if there is residential lot to manage
        hasHouses = int(currentAttList.getAttribute("HasHouses")) * int(self.service_res)
        hasSsystems = int(currentAttList.getAttribute("HasSSys"))
        if hasHouses == 0 or hasSsystems == 1:  #SKIP CONDITION 2 - no houses to design for
            return technologydesigns
        
        street_avail_Res = currentAttList.getAttribute("avSt_RES")
        if street_avail_Res < 0.0001:
            #self.notify("No space on street")
            return technologydesigns
        
        #GET INFORMATION FROM VECTOR DATA
        allotments = currentAttList.getAttribute("ResAllots")
        soilK = currentAttList.getAttribute("Soil_k")
        
        Aimplot = currentAttList.getAttribute("ResLotEIA")
        AimpRes = Aimplot * allotments
        AimpstRes = currentAttList.getAttribute("ResFrontT") - currentAttList.getAttribute("avSt_RES")
        
        Aimphdr = currentAttList.getAttribute("HDR_EIA")
        
        storeObj = np.inf       #No storage recycling for this scale
        
        for j in techList:
            tech_applications = self.getTechnologyApplications(j)
            #self.notify("Assessing street techs for "+str(j)+" applications: "+str(tech_applications))
            
            minsize = eval("self."+j+"minsize")
            maxsize = eval("self."+j+"maxsize")          #gets the specific system's maximum size
            
            #Design curve path
            dcvpath = self.getDCVPath(j)
            
            for lot_deg in self.lot_incr:
                AimpremainRes = AimpstRes + (AimpRes *(1-lot_deg))      #street + remaining lot
                AimpremainHdr = Aimphdr*(1.0-lot_deg)
                
                for street_deg in self.street_incr:
                    #self.notify("CurrentStreet Deg: "+str(street_deg)+" for lot-deg "+str(lot_deg))
                    if street_deg == 0:
                        continue
                    AimptotreatRes = AimpremainRes * street_deg
                    AimptotreatHdr = AimpremainHdr * street_deg
                    #self.notify("Aimp to treat: "+str(AimptotreatRes))
                    
                    if hasHouses != 0 and AimptotreatRes > 0.0001:
                        sys_objects = self.designTechnology(street_deg, AimptotreatRes, j, dcvpath,
                                                           tech_applications, soilK, minsize, maxsize, 
                                                           street_avail_Res, "Street", currentID, storeObj)
                        for sys_object in sys_objects:
                            sys_object.setDesignIncrement([lot_deg, street_deg])
                            technologydesigns.append(sys_object)
        return technologydesigns


    def assessNeighbourhoodOpportunities(self, techList, currentAttList):
        """Assesses if the shortlist of neighbourhood-scale technologies can be put in local parks 
        & other areas. Does this for one block at a time, depending on the currentAttributesList 
        and the techlist
        """
        currentID = int(currentAttList.getAttribute("BlockID"))
        technologydesigns = [0]
        
        #Grab total impervious area and available space
        AblockEIA = currentAttList.getAttribute("Manage_EIA")
        hasNsystems = int(currentAttList.getAttribute("HasNSys"))
        hasBsystems = int(currentAttList.getAttribute("HasBSys"))
        if AblockEIA <= 0.0001 or hasNsystems == 1 or hasBsystems == 1:
            return technologydesigns    #SKIP CONDITION 1 - already systems in place or no impervious area to treat
        
        av_PG = currentAttList.getAttribute("PG_av")
        av_REF = currentAttList.getAttribute("REF_av")
        av_SVU_sw = currentAttList.getAttribute("SVU_avSW")
        av_SVU_ws = currentAttList.getAttribute("SVU_avWS")
        totalavailable = av_PG + av_REF + av_SVU_sw + av_SVU_ws
        if totalavailable < 0.0001:
            return technologydesigns    #SKIP CONDITION 2 - NO SPACE AVAILABLE
        
        #GET INFORMATION FROM VECTOR DATA
        soilK = currentAttList.getAttribute("Soil_k")
        
        #Size a combination of stormwater harvesting stores
        if bool(int(self.ration_harvest)):
            neighSWstores = self.determineStorageVolNeigh(currentAttList, self.raindata, self.evapscale, "SW")
            #self.notify(neighSWstores)
                
        for j in techList:
            tech_applications = self.getTechnologyApplications(j)
            #self.notify("Currently designing tech: "+str(j)+" available applications: "+str(tech_applications))
            
            minsize = eval("self."+j+"minsize")
            maxsize = eval("self."+j+"maxsize")         #Gets the specific system's maximum size
            #Design curve path
            dcvpath = self.getDCVPath(j)
            for neigh_deg in self.neigh_incr:
                #self.notify("Current Neigh Deg: "+str(neigh_deg))
                if neigh_deg == 0: 
                    continue
                
                Aimptotreat = neigh_deg * AblockEIA

                if bool(int(self.ration_harvest)) and neighSWstores != np.inf:
                    curStoreObjs = neighSWstores[neigh_deg]
                    for supplyincr in self.neigh_incr:
                        if supplyincr == 0: 
                            continue
                        storeObj = curStoreObjs[supplyincr]
                        sys_objects = self.designTechnology(neigh_deg, Aimptotreat, j, dcvpath, tech_applications,
                                         soilK, minsize, maxsize, totalavailable, "Neigh", currentID, storeObj)
                        for sys_object in sys_objects:
                            sys_object.setDesignIncrement(neigh_deg)
                            technologydesigns.append(sys_object)
                else:
                    storeObj = np.inf
                    sys_objects = self.designTechnology(neigh_deg, Aimptotreat, j, dcvpath, tech_applications,
                                                       soilK, minsize, maxsize, totalavailable, "Neigh", currentID, storeObj)
                    for sys_object in sys_objects:
                        sys_object.setDesignIncrement(neigh_deg)
                        technologydesigns.append(sys_object)
                    
#            for lot_deg in self.lot_incr:
#                Aimpremain = AblockEIA - lot_deg*allotments*Aimplot - lot_deg*Aimphdr
#                for neigh_deg in self.neigh_incr:
#                    #self.notify("CurrentNeigh Deg: "+str(neigh_deg)+" for lot-deg "+str(lot_deg))
#                    if neigh_deg == 0:
#                        continue
#                    Aimptotreat=  neigh_deg * Aimpremain
#                    #self.notify("Aimp to treat: "+str(Aimptotreat))
#                    if Aimptotreat > 0.0001:
#                        sys_objects = self.designTechnology(neigh_deg, Aimptotreat, 0, j,
#                                                           dcvpath, tech_applications, soilK, minsize,
#                                                           maxsize, totalavailable, "Neigh", currentID, storeObj)
#                        for sys_object in sys_objects:
#                            sys_object.setDesignIncrement([lot_deg, neigh_deg])
#                            technologydesigns.append(sys_object)
        return technologydesigns


    def assessSubbasinOpportunities(self, techList, currentAttList):
        """Assesses if the shortlist of sub-basin-scale technologies can be put in local parks 
        & other areas. Does this for one block at a time, depending on the currentAttributesList 
        and the techlist
        """
        currentID = int(currentAttList.getAttribute("BlockID"))        
        
        technologydesigns = {}  #Three Conditions: 1) there must be upstream blocks
                                                 # 2) there must be space available, 
                                                 # 3) there must be impervious to treat
                                                 
        soilK = currentAttList.getAttribute("Soil_k")
        
        #SKIP CONDITION 1: Grab Block's Upstream Area
        upstreamIDs = self.retrieveStreamBlockIDs(currentAttList, "upstream")
        hasBsystems = int(currentAttList.getAttribute("HasBSys"))
        hasNsystems = int(currentAttList.getAttribute("HasBSys"))
        if len(upstreamIDs) == 0 or hasBsystems == 1 or hasNsystems == 1:
            #self.notify("Current Block has no upstream areas, skipping")
            return technologydesigns
        
        #SKIP CONDITION 2: Grab Total available space, if there is none, no point continuing
        av_PG = currentAttList.getAttribute("PG_av")
        av_REF = currentAttList.getAttribute("REF_av")
        av_SVU_sw = currentAttList.getAttribute("SVU_avSW")
        av_SVU_ws = currentAttList.getAttribute("SVU_avWS")
        totalavailable = av_PG + av_REF + av_SVU_sw + av_SVU_ws
        if totalavailable < 0.0001:
            #self.notify("Total Available Space in Block to do STUFF: "+str(totalavailable)+" less than threshold")
            return technologydesigns
        
        #SKIP CONDITION 3: Get Block's upstream Impervious area
        upstreamImp = self.retrieveAttributeFromIDs(upstreamIDs, "Manage_EIA", "sum")
        if upstreamImp < 0.0001:
            #self.notify("Total Upstream Impervious Area: "+str(upstreamImp)+" less than threshold")
            return technologydesigns
        
        #Initialize techdesignvector's dictionary keys
        for j in self.subbas_incr:
            technologydesigns[j] = [0]

        if bool(int(self.ration_harvest)):
            subbasSWstores = self.determineStorageVolSubbasin(currentAttList, self.raindata, self.evapscale, "SW")
            #self.notify("Subbasin: "+str(subbasSWstores))
        
        for j in techList:
            tech_applications = self.getTechnologyApplications(j)
            #self.notify("Now designing for "+str(j)+" for applications: "+str(tech_applications))
            
            minsize = eval("self."+j+"minsize")
            maxsize = eval("self."+j+"maxsize")     #Gets the specific system's maximum allowable size
            
            #Design curve path
            dcvpath = self.getDCVPath(j)
            for bas_deg in self.subbas_incr:
                #self.notify("Current Basin Deg: "+str(bas_deg))
                if bas_deg == 0:
                    continue
                Aimptotreat = upstreamImp * bas_deg
                #self.notify("Aimp to treat: "+str(Aimptotreat))
                
                #Loop across all options in curStoreObj
                if bool(int(self.ration_harvest)) and subbasSWstores != np.inf:
                    curStoreObjs = subbasSWstores[bas_deg]  #current dict of possible stores based on harvestable area (bas_Deg)
                    for supplyincr in self.subbas_incr:
                        if supplyincr == 0 or Aimptotreat < 0.0001: 
                            continue
                        storeObj = curStoreObjs[supplyincr]
                        sys_objects = self.designTechnology(bas_deg, Aimptotreat, j, dcvpath, tech_applications,
                                        soilK, minsize, maxsize, totalavailable, "Subbas", currentID, storeObj)
                        for sys_object in sys_objects:
                            sys_object.setDesignIncrement(bas_deg)
                            technologydesigns[bas_deg].append(sys_object)
                else:
                    storeObj = np.inf
                    sys_objects = self.designTechnology(bas_deg, Aimptotreat, j, dcvpath, tech_applications,
                                        soilK, minsize, maxsize, totalavailable, "Subbas", currentID, storeObj)
                    for sys_object in sys_objects:
                        sys_object.setDesignIncrement(bas_deg)
                        technologydesigns[bas_deg].append(sys_object)
        return technologydesigns


    def getDCVPath(self, techType):
        """Retrieves the string for the path to the design curve file, whether it is a custom loaded
        design curve or the UB default curves.
        """
        if eval("self."+techType+"designUB"):
            if techType in ["BF", "IS"]:
                return self.ubeatsdir+"/ancillary/wsudcurves/Melbourne/"+techType+"-EDD"+str(eval("self."+techType+"spec_EDD"))+"m-FD"+str(eval("self."+techType+"spec_FD"))+"m-DC.dcv"
            elif techType in ["PB"]:
                return self.ubeatsdir+"/ancillary/wsudcurves/Melbourne/"+techType+"-MD"+str(eval("self."+techType+"spec_MD"))+"m-DC.dcv"
            elif techType in ["WSUR"]:
                return self.ubeatsdir+"/ancillary/wsudcurves/Melbourne/"+techType+"-EDD"+str(eval("self."+techType+"spec_EDD"))+"m-DC.dcv"
            else:
                return "No DC Located"
        else:
            return eval("self."+techType+"descur_path")


    def getTechnologyApplications(self, j):
        """Simply creates a boolean list of whether a particular technology was chosen for flow management
        water quality control and/or water recycling, this list will inform the sizing of the system.
        """
        try:
            purposeQ = eval("self."+j+"flow")
            if purposeQ == None:
                purposeQ = 0
        except NameError:
            purposeQ = 0
        except AttributeError:
            purposeQ = 0
        try:
            purposeWQ = eval("self."+j+"pollute")
            if purposeWQ == None:
                purposeWQ = 0
        except NameError:
            purposeWQ = 0
        except AttributeError:
            purposeWQ = 0
        try:
            purposeREC = eval("self."+j+"recycle")
            if purposeREC == None:
                purposeREC = 0
        except NameError:
            purposeREC = 0
        except AttributeError:
            purposeREC = 0
        purposes = [purposeQ, purposeWQ, purposeREC]
        purposebooleans = [int(self.ration_runoff), int(self.ration_pollute), int(self.ration_harvest)]
        for i in range(len(purposes)):
            purposes[i] *= purposebooleans[i]
        return purposes
            

    def designTechnology(self, incr, Aimp, techabbr, dcvpath, tech_applications, soilK, minsize, maxsize, avail_sp, landuse, currentID, storeObj):
        """Carries out the design for a given system type on a given land use and scale. This function is
        used for the different land uses that can accommodate various technologies in the model.
        Input Arguments:            
            -incr = design increment                             -minsize = minimum system size
            -Aimp = effective imp. area                          -maxsize = maximum system size
            -techabbr = technology's abbreviation                -avail_sp = available space
            -dcvpath = design curve path                         -landuse = current land use being designed for
            -tech_applications = types of uses for technology    -currentID = currentBlockID
            -soilK = soil exfiltration rates                     -storeObj = object containing storage info in case of recycling objective
        Output Argument:
            - a WSUD object instance
        """            
        scalematrix = {"RES":'L', "HDR":'L', "LI":'L', "HI":'L', "COM":'L', "Street":'S', "Neigh":'N', "Subbas":'B'}
        
        try:
            curscale = scalematrix[landuse]
        except KeyError:
            curscale = 'NA'

        Adesign_imp = Aimp * incr       #Target impervious area depends on the increment/i.e. level of treatment service
        
        if storeObj != np.inf:
            design_Dem = storeObj.getSupply()
            #self.notify("Size of Tank: "+str(storeObj.getSize()))
        else:
            design_Dem = 0
        #self.notify("Design Demand :"+str(design_Dem))
        
        #Get Soil K to use for theoretical system design
        if techabbr in ["BF", "SW", "IS", "WSUR", "PB"]:
            systemK = eval("self."+str(techabbr)+"exfil")
        else:
            systemK = 0

        Asystem = {"Qty":[None, 1], "WQ":[None,1], "Rec":[None,1], "Size":[None, 1]}  #Template for system design, holds designs

        #OBJECTIVE 1 - Design for Runoff Control
        if tech_applications[0] == 1:
            purpose = [tech_applications[0], 0, 0]
            Asystem["Qty"] = eval('td.design_'+str(techabbr)+'('+str(Adesign_imp)+',"'+str(dcvpath)+'",'+str(self.targetsvector)+','+str(purpose)+','+str(soilK)+','+str(systemK)+','+str(minsize)+','+str(maxsize)+')')
            #self.notify(Asystem["Qty"])
        else:
            Asystem["Qty"] = [None, 1]
        Asystem["Size"] = Asystem["Qty"]    #First target, set as default system size, even if zero
        
        #OBJECTIVE 2 - Design for WQ Control
        if tech_applications[1] == 1:
            purpose = [0, tech_applications[1], 0]
            Asystem["WQ"] = eval('td.design_'+str(techabbr)+'('+str(Adesign_imp)+',"'+str(dcvpath)+'",'+str(self.targetsvector)+','+str(purpose)+','+str(soilK)+','+str(systemK)+','+str(minsize)+','+str(maxsize)+')')
            #self.notify(Asystem["WQ"])
        else:
            Asystem["WQ"] = [None, 1]
        if Asystem["WQ"][0] > Asystem["Size"][0]:
            Asystem["Size"] = Asystem["WQ"] #if area for water quality is greater, choose the governing one as the final system size

        sys_objects_array = []  #Initialise the array that will hold the tech designs

        #Add the WQ - Qty system combo first to the array. Assume no harvesting
        if Asystem["Size"][0] < avail_sp and Asystem["Size"][0] != None:        #if it fits and is NOT a NoneType:
            #IF THERE IS NO STORAGE, JUST CREATE THE TECH OBJECT WITHOUT THE STORE
            servicematrix = [0,0,0]
            if Asystem["Qty"][0] != None:
                servicematrix[0] = Adesign_imp
            if Asystem["WQ"][0] != None:
                servicematrix[1] = Adesign_imp
            if Asystem["Rec"][0] != None:
                servicematrix[2] = design_Dem

            #DEBUG - Database writing
            # servicematrixstring = tt.convertArrayToDBString(servicematrix)
            # self.dbcurs.execute("INSERT INTO watertechs VALUES ("+str(currentID)+",'"+str(techabbr)+"',"+
            #                     str(Asystem["Size"][0])+",'"+curscale+"',"+str(Adesign_imp)+",'"+
            #                     str(servicematrixstring)+"',"+str(Asystem["Size"][1])+",'"+str(landuse)+"',"+
            #                     str(incr)+",'N',"+str(0)+",'"+str('None')+"',"+str(0)+","+str(0)+","+str(0)+")")
            #DEBUG END

            sys_object = tt.WaterTech(techabbr, Asystem["Size"][0], curscale, servicematrix, Asystem["Size"][1], landuse, currentID)
            sys_object.setDesignIncrement(incr)
            sys_objects_array.append(sys_object)

        #OBJECTIVE 3 - If system type permits storage, design for Recycling - this includes WQ control first, then adding storage!
        #   Only works if:
        #       #1 - the harvesting application is checked
        #       #2 - there is a store object that is not infinity
        #       #3 - the system is one of those that supports harvesting
        addstore = []   #Has several arguments [store object, WQsize, QTYsize, type of store, integrated?]
        if tech_applications[2] == 1 and storeObj != np.inf:
            #First design for WQ control (assume raintanks don't use natural treatment)
            purpose = [0, 1, 0]
            if techabbr in ["RT", "GW"]:        #If a raintank or greywater system, then no area required. Assume treatment is through some
                AsystemRecWQ = [0, 1]           #   non-green-infrastructure means
            else:   #Design for a fully lined system!
                AsystemRecWQ = eval('td.design_'+str(techabbr)+'('+str(Adesign_imp)+',"'+str(dcvpath)+'",'+str(self.targetsvector)+','+str(purpose)+','+str(soilK)+','+str(0)+','+str(minsize)+','+str(maxsize)+')')
                #Required surface are of a system that only does water quality management...

            vol = storeObj.getSize()
            #self.notify("Volume "+str(vol))
            if vol == np.inf:       #Strange error where volume return is inf, yet the name 'inf' is not defined
                vol = np.inf

            design_harvest = True
            if AsystemRecWQ[0] in [np.inf, None] or vol == np.inf:
                #self.notify("Skip harvesting design! Cannot fulfill treatment + storage")
                design_harvest = False

            #Harvesting System Design: Part 1 - INTEGRATED Design extra storage space as integrated storage
            #   WSUR = open water body as extra area
            #   PB = part of the storage area
            #   RT = standard storage volume
            #   GW = standard storage volume
            if techabbr in ["RT", "GW", "PB", "WSUR"] and design_harvest:        #Turn the WQ system into a SWH system based on hybrid combos
                sysdepth = float(self.sysdepths[techabbr])     #obtain the system depth
                AsystemRecQty = eval('td.sizeStoreArea_'+str(techabbr)+'('+str(vol)+','+str(sysdepth)+','+str(0)+','+str(9999)+')')
                #self.notify("AsysrecQty[RT, GW, PB. WSUR] "+str(AsystemRecQty))
                if AsystemRecQty[0] != None:
                    addstore.append([storeObj, AsystemRecWQ, AsystemRecQty, techabbr, 1])     #Input arguments to addstore function

            #Harvesting System Design: Part 2 - HYBRID A Design extra storage space as closed auxillary storage
            #   WSUR = into tank
            #   BF = into tank
            #   SW = into tank
            if techabbr in ["WSUR", "BF", "SW"] and design_harvest:
                sysdepth = float(self.sysdepths["RT"])
                AsystemRecQty = td.sizeStoreArea_RT(vol, sysdepth, 0, 9999)
                #self.notify("AsysrecQty[WSUR, BF, SW] "+str(AsystemRecQty))
                if AsystemRecQty[0] != None:
                    addstore.append([storeObj, AsystemRecWQ, AsystemRecQty, "RT", 0])

            #Harvesting System Design: Part 3 - HYBRID B Design extra storage space as open auxillary storage
            #   BF = into pond
            #   SW = into pond
            if techabbr in ["BF", "SW"] and curscale in ["N", "B"] and design_harvest:
                sysdepth = float(self.sysdepths["PB"])
                AsystemRecQty = td.sizeStoreArea_PB(vol, sysdepth, 0.0, 9999.0)
                #self.notify("AsysrecQty[BF, SW] "+str(AsystemRecQty))
                if AsystemRecQty[0] != None:
                    addstore.append([storeObj, AsystemRecWQ, AsystemRecQty, "PB", 0])

        if len(addstore) == 0:
            return sys_objects_array

        for i in range(len(addstore)):
            curstore = addstore[i]
            if len(curstore) == 0:
                #self.notify("No Addstore Data, continuing")
                continue
            #CHECK WHAT THE TOTAL SYSTEM SIZE IS FIRST BY COMPARING LARGEST SYSTEM TO DATE VS. HARVESTING SYSTEM
            recsize = curstore[1][0] + curstore[2][0]   #AsystemRecWQ + AsystemRecQTY
            eafact = recsize/(curstore[1][0]/curstore[1][1] + curstore[2][0]/curstore[2][1])    #area factor, does not indicate relative factors for different systems!
            #eafact is the same as WQfact and QtyFact if the system is integrated (e.g. Wetland buffer is ALWAYS 1.3)

            Asystem["Rec"] = [recsize, eafact]  #This is the total recycling storage size
            if curstore[4] == 1:                #Check if the system integrated? Differentiate between integrated and non-integrated systems!
                Asystem["Size"] = Asystem["Rec"]    #Because the integrated system has same planning rules so EAFACT is the same
            else:
                Asystem["Size"] = curstore[1]   #if non-integrated, then base system is defined ONLY as WQ area/treatment...

            #self.notify("Asystem "+str(Asystem))

            #NOW CHECK AVAILABLE SPACE - CREATE OBJECT AND PASS TO FUNCTION RETURN
            if recsize < avail_sp and recsize != None:        #if it fits and is NOT a NoneType
                #self.notify("Fits")
                servicematrix = [0,0,0]     #Skip water quantity, this is assumed negligible since the treatment system is lined and will not reduce flow
                if AsystemRecWQ[0] != None:             #Harvesting system cannot do runoff reduction through normal means!
                    servicematrix[1] = Adesign_imp
                if AsystemRecQty[0] != None:
                    servicematrix[2] = design_Dem

                # DEBUG - CONVERT TO DATABSE STRING
                # servicematrixstring = tt.convertArrayToDBString(servicematrix)

                sys_object = tt.WaterTech(techabbr, Asystem["Size"][0], curscale, servicematrix, Asystem["Size"][1], landuse, currentID)
                sys_object.addRecycledStoreToTech(curstore[0], curstore[2], curstore[3], curstore[4])     #If analysis showed that system can accommodate store, add the store object
                sys_object.setDesignIncrement(incr)

                #Work out SWH Benefits for Quantity and Quality
                if self.swh_benefits:
                    if self.ration_runoff:      #NOW HAVE TO DETERMINE WHETHER TO DO THIS BASED ON UNIT RUNOFF RATE OR SOMETHING ELSE
                        dcv.treatQTYbenefits(sys_object, self.swh_unitrunoff, Adesign_imp)
                    if self.ration_pollute:
                        dcv.treatWQbenefits(sys_object, self.swh_unitrunoff, self.targetsvector[1:4], Adesign_imp, self.swhbenefitstable)   #only the three pollution targets
                    # print sys_object.getIAO("all")

                #DEBUG INSERT DATA INTO THE SQLITE Database
                # self.dbcurs.execute("INSERT INTO watertechs VALUES ("+str(currentID)+",'"+str(techabbr)+"',"+
                #                     str(Asystem["Size"][0])+",'"+curscale+"',"+str(Adesign_imp)+",'"+str(servicematrixstring)+
                #                     "',"+str(Asystem["Size"][1])+",'"+str(landuse)+"',"+str(incr)+",'Y',"+str(curstore[4])+",'"+
                #                     str(curstore[3])+"',"+str(curstore[0].getSize())+","+str(sys_object.getIAO("Qty"))+
                #                     ","+str(sys_object.getIAO("WQ"))+")")

                sys_objects_array.append(sys_object)
        return sys_objects_array    #if no systems are design, returns an empty array


    def retrieveStreamBlockIDs(self, currentAttList, direction):
        """Returns a vector containing all upstream block IDs, allows quick collation of 
        details.
        """
        if direction == "upstream":
            attname = "UpstrIDs"
        elif direction == "downstream":
            attname = "DownstrIDs"
            
        streamstring = currentAttList.getAttribute(attname)
        #self.activesim.debugAssets("BlockID", attname)
        streamIDs = streamstring.split(',')
        streamIDs.remove('')
        
        for i in range(len(streamIDs)):
            streamIDs[i] = int(streamIDs[i])
        if len(streamIDs) == 0:
            return []
        else:
            return streamIDs

    def retrieveAttributeFromIDs(self, listIDs, attribute, calc):
        """Retrieves all values from the list of upstreamIDs with the attribute name
        <attribute> and calculates whatever <calc> specifies
            Input:
                - listIDs: the vector list of upstream IDs e.g. [3, 5, 7, 8, 10, 15, 22]
                - attribute: an exact string that matches the attribute as saved by other
                            modules
                - calc: the means of calculation, options include
                            'sum' - calculates total sum
                            'average' - calculates average
                            'max' - retrieves the maximum
                            'min' - retrieves the minimum
                            'minNotzero' - retrieves the minimum among non-zero numbers
                            'list' - returns the list itself
                                                            """
        output = 0
        datavector = []
        
        for i in listIDs:
            blockFace = self.activesim.getAssetWithName("BlockID"+str(i))
            #blockFace = self.getBlockUUID(i, city)
            if blockFace.getAttribute("Status") == 0:
                continue
            datavector.append(blockFace.getAttribute(attribute))
        
        if calc == 'sum':
            output = sum(datavector)
        elif calc == 'average':
            pass
        elif calc == 'max':
            pass
        elif calc == 'min':
            pass
        elif calc == 'minNotzero':
            pass
        elif calc == 'list':
            output = datavector
        else:
            self.notify("Error, calc not specified, returning sum")
            output = sum(datavector)
        return output

    def determineStorageVolForLot(self, currentAttList, rain, evapscale, wqtype, lottype):
        """Uses information of the Block's lot-scale to determine what the required
        storage size of a water recycling system is to meet the required end uses
        and achieve the user-defined potable water reduction
            - currentAttList:  current Attribute list of the block in question
            - rain: rainfall data for determining inflows if planning SW harvesting
            - evapscale: scaling factors for outdoor irrigation demand scaling
            - wqtype: the water quality being harvested (determines the type of end
                                                        uses acceptable)
        
        Function returns a storage volume based on the module's predefined variables
        of potable water supply reduction, reliability, etc."""
        
        if int(currentAttList.getAttribute("HasRes")) == 0:
            return np.inf       #Return infinity if there is no res land use
            #First exit
        if lottype == "RES" and int(currentAttList.getAttribute("HasHouses")) == 0:
            return np.inf
        if lottype == "HDR" and int(currentAttList.getAttribute("HasFlats")) == 0:
            return np.inf
        
        #WORKING IN [kL/yr] for single values and [kL/day] for timeseries
        
        #Use the FFP matrix to determine total demands and suitable end uses

        wqlevel = self.ffplevels[wqtype]    #get the level and determine the suitable end uses
        if lottype == "RES":    #Demands based on a single house
            reshouses = float(currentAttList.getAttribute("ResHouses"))
            resallots = float(currentAttList.getAttribute("ResAllots"))
            lotdemands = {"Kitchen":currentAttList.getAttribute("wd_RES_K")*365.0/reshouses,
                      "Shower":currentAttList.getAttribute("wd_RES_S")*365.0/reshouses,
                      "Toilet":currentAttList.getAttribute("wd_RES_T")*365.0/reshouses,
                      "Laundry":currentAttList.getAttribute("wd_RES_L")*365.0/reshouses,
                      "Irrigation":currentAttList.getAttribute("wd_RES_I")*365.0/resallots }
        elif lottype == "HDR": #Demands based on entire apartment sharing a single roof
            hdrflats = float(currentAttList.getAttribute("HDRFlats"))
            lotdemands = {"Kitchen":currentAttList.getAttribute("wd_HDR_K")*365.0,
                      "Shower":currentAttList.getAttribute("wd_HDR_S")*365.0,
                      "Toilet":currentAttList.getAttribute("wd_HDR_T")*365.0,
                      "Laundry":currentAttList.getAttribute("wd_HDR_L")*365.0,
                      "Irrigation":currentAttList.getAttribute("wd_HDR_I")*365.0 }
        totalhhdemand = sum(lotdemands.values())    #Total House demand, [kL/yr]
        
        enduses = {}        #Tracks all the different types of end uses
        objenduses = []
        if self.ffplevels[self.ffp_kitchen] >= wqlevel:
            enduses["Kitchen"] = lotdemands["Kitchen"]
            objenduses.append('K')
        if self.ffplevels[self.ffp_shower] >= wqlevel:
            enduses["Shower"] = lotdemands["Shower"]
            objenduses.append('S')
        if self.ffplevels[self.ffp_toilet] >= wqlevel:
            enduses["Toilet"] = lotdemands["Toilet"]
            objenduses.append('T')
        if self.ffplevels[self.ffp_laundry] >= wqlevel:
            enduses["Laundry"] = lotdemands["Laundry"]
            objenduses.append('L')
        if self.ffplevels[self.ffp_garden] >= wqlevel:
            enduses["Irrigation"] = lotdemands["Irrigation"]
            objenduses.append('I')
        totalsubdemand = sum(enduses.values())
        
        if totalsubdemand == 0:
            return np.inf
        
        #Determine what the maximum substitution can be, supply the smaller of total substitutable demand
        #or the desired target.
        recdemand = min(totalsubdemand, self.service_rec/100*totalhhdemand)     #the lower of the two
        #self.notify("Recycled Demand Lot: "+str(recdemand))
        #Determine inflow/demand time series
        if lottype == "RES":
            Aroof = currentAttList.getAttribute("ResRoof")
        elif lottype == "HDR":
            Aroof = currentAttList.getAttribute("HDRRoofA")
        
        #Determine demand time series
        if "Irrigation" in enduses.keys():
            #Scale to evap pattern
            demandseries = ubseries.createScaledDataSeries(recdemand, evapscale, False)
        else:
            #Scale to constant pattern
            demandseries = ubseries.createConstantDataSeries(recdemand/365, len(rain))
        
        #Generate the inflow series based on the kind of water being harvested
        if wqtype in ["RW", "SW"]:      #Use rainwater to generate inflow
            inflow = ubseries.convertDataToInflowSeries(rain, Aroof, False)     #Convert rainfall to inflow
            maxinflow = sum(rain)/1000 * Aroof / self.rain_length         #average annual inflow using whole roof
            tank_templates = self.lot_raintanksizes     #Use the possible raintank sizes
        elif wqtype in ["GW"]:  #Use greywater to generate inflow
            inflow = 0
            maxinflow = 0
            tank_templates = [] #use the possible greywater tank sizes
        
        if (self.rec_demrange_max/100.0)*maxinflow < recdemand or (self.rec_demrange_min/100.0)*maxinflow > recdemand:
            #If Vdem not within the bounds of total inflow
            return np.inf       #cannot size a store that is supplying more than it is getting or not economical to size
        
        #Depending on Method, size the store
        if self.sb_method == "Sim":
            mintank_found = 0
            storageVol = np.inf      #Assume infinite storage for now
            for i in tank_templates:        #Run through loop
                if mintank_found == 1:
                    continue
                rel = dsim.calculateTankReliability(inflow, demandseries, i)
                #print rel
                if rel > self.targets_reliability:
                    mintank_found = 1
                    storageVol = i
                    #print storageVol
        
        elif self.sb_method == "Eqn":
            vdemvsupp = recdemand / maxinflow
            storagePerc = deq.loglogSWHEquation(self.regioncity, self.targets_reliability, inflow, demandseries)
            reqVol = storagePerc/100*maxinflow  #storagePerc is the percentage of the avg. annual inflow
            
            #Determine where this volume ranks in reliability
            storageVol = np.inf     #Assume infinite storage for now, readjust later
            tank_templates.reverse()        #Reverse the series for the loop
            for i in range(len(tank_templates)):
                if reqVol < tank_templates[i]: #Begins with largest tank
                    storageVol = tank_templates[i] #Begins with largest tank    #if the volume is below the current tank size, use the 'next largest'
            tank_templates.reverse()        #Reverse the series back in case it needs to be used again
        storeObj = tt.RecycledStorage(wqtype, storageVol,  objenduses, Aroof, self.targets_reliability, recdemand, "L")
        #End of function: returns storageVol as either [1kL, 2kL, 5kL, 10kL, 15kL, 20kL] or np.inf
        return storeObj
    
    def determineEndUses(self, wqtype):
        """Returns an array of the allowable water end uses for the given water
        quality type 'wqtype'. Array is dependent on user inputs and is subsequently
        used to determine water demands substitutable by that water source. This 
        function is only for neighbourhood and sub-basin scales"""
        wqlevel = self.ffplevels[wqtype]
        enduses = []
        if self.ffplevels[self.ffp_kitchen] >= wqlevel: enduses.append("K")
        if self.ffplevels[self.ffp_shower] >= wqlevel: enduses.append("S")
        if self.ffplevels[self.ffp_toilet] >= wqlevel: enduses.append("T")
        if self.ffplevels[self.ffp_laundry] >= wqlevel: enduses.append("L")
        if self.ffplevels[self.ffp_garden] >= wqlevel: enduses.append("I")
        if self.ffplevels[self.public_irr_wq] >= wqlevel: enduses.append("PI")
        return enduses
    
    def determineStorageVolNeigh(self, currentAttList, rain, evapscale, wqtype):
        """Uses information of the Block to determine the required storage size of
        a water recycling system to meet required end uses and achieve the user-defined
        potable water reduction and reliability targets
            - currentAttList:  current Attribute list of the block in question
            - rain: rainfall data for determining inflows if planning SW harvesting
            - evapscale: scaling factors for outdoor irrigation demand scaling
            - wqtype: water quality being harvested (determines the type of end
                                                        uses acceptable)
        
        Function returns an array of storage volumes in dictionary format identified
        by the planning increment."""
        
        #WORKING IN [kL/yr] for single values and [kL/day] for time series
        if currentAttList.getAttribute("Blk_EIA") == 0:
            return np.inf
        
        enduses = self.determineEndUses(wqtype)
        houses = currentAttList.getAttribute("ResHouses")
        
        #Total water demand (excluding non-residential areas)
        storageVol = {}
        
        #Get the entire Block's Water Demand
        blk_demands = self.getTotalWaterDemandEndUse(currentAttList, ["K","S","T", "L", "I", "PI"])
        #self.notify("Block demands: "+str(blk_demands))
        
        #Get the entire Block's substitutable water demand
        totalsubdemand = self.getTotalWaterDemandEndUse(currentAttList, enduses)
        #self.notify("Total Demand Substitutable: "+str(totalsubdemand))
        
        if totalsubdemand == 0: #If nothing can be substituted, return infinity
            return np.inf    
        
        #Loop across increments: Storage that harvests all area/WW to supply [0.25, 0.5, 0.75, 1.0] of demand
        for i in range(len(self.neigh_incr)):   #Loop across harvestable area
            if self.neigh_incr[i] == 0:
                continue
            harvestincr = self.neigh_incr[i]
            storageVol[harvestincr] = {} #Initialize container dictionary
            
            for j in range(len(self.neigh_incr)):   #Loop across substitutable demands
                if self.neigh_incr[j] == 0:
                    continue
                
                supplyincr = self.neigh_incr[j]
                recdemand = supplyincr*blk_demands  #x% of total block demand
                if recdemand > totalsubdemand:      #if that demand is greater than what can be substituted, then
                    storageVol[harvestincr][supplyincr] = np.inf         
                    #make it impossible to size a system for that combo
                    continue
                #self.notify("Recycled Demand: "+str(recdemand))
                
                if recdemand == 0:
                    #If there is no demand to substitute, then storageVol is np.inf
                    storageVol[harvestincr][supplyincr] = np.inf
                    continue
                    
                #Harvestable area
                Aharvest = currentAttList.getAttribute("Blk_EIA")*harvestincr   #Start with this
                #self.notify("Harvestable Area :"+str(Aharvest))
                
                if "I" in enduses:      #If irrigation is part of end uses
                    #Scale to evap pattern
                    demandseries = ubseries.createScaledDataSeries(recdemand, evapscale, False)
                else:
                    #Scale to constant pattern
                    demandseries = ubseries.createScaledDataSeries(recdemand/365, len(rain))
                
                #Generate the inflow series based on kind of water being harvested
                if wqtype in ["RW", "SW"]:
                    inflow = ubseries.convertDataToInflowSeries(rain, Aharvest, False)
                    maxinflow = sum(rain)/1000*Aharvest / self.rain_length
                    #self.notify("Average annual inflow: "+str(maxinflow))
                elif wqtype in ["GW"]:
                    inflow = 0
                    maxinflow = 0
                
                if (self.rec_demrange_max/100.0)*maxinflow < recdemand or (self.rec_demrange_min/100.0)*maxinflow > recdemand:
                    storageVol[harvestincr][supplyincr] = np.inf 
                    #Cannot size a store that is not within the demand range specified
                    continue
                
                #Size the store depending on method
                if self.sb_method == "Sim":
                    reqVol = dsim.estimateStoreVolume(inflow, demandseries, self.targets_reliability, self.relTolerance, self.maxSBiterations)
                    #self.notify("reqVol: "+str(reqVol))
                elif self.sb_method == "Eqn":
                    vdemvsupp = recdemand / maxinflow
                    storagePerc = deq.loglogSWHEquation(self.regioncity, self.targets_reliability, inflow, demandseries)
                    reqVol = storagePerc/100*maxinflow  #storagePerc is the percentage of the avg. annual inflow
                storeObj = tt.RecycledStorage(wqtype, reqVol, enduses, Aharvest, self.targets_reliability, recdemand, "N")
                storageVol[harvestincr][supplyincr] = storeObj       #at each lot incr: [ x options ]
            #self.notify(storageVol[harvestincr])
        return storageVol

    def getTotalWaterDemandEndUse(self, currentAttList, enduse):
        """Retrieves all end uses for the current Block based on the end use matrix
        and the lot-increment. 
        """
        demand = 0
        #End use in houses and apartments - indoors + garden irrigation
        for i in enduse:    #Get Indoor demands first
            if i == "PI" or i == "I":
                continue    #Skip the public irrigation
            demand += currentAttList.getAttribute("wd_RES_"+str(i))*365.0
            demand += currentAttList.getAttribute("wd_HDR_"+str(i))*365.0
        #Add irrigation of public open space
        if "I" in enduse:
            demand += currentAttList.getAttribute("wd_RES_I")*365.0
            demand += currentAttList.getAttribute("wd_HDR_I")*365.0 #Add all HDR irrigation
        if "PI" in enduse:
            demand += currentAttList.getAttribute("wd_PubOUT")
        return demand
    
    def determineStorageVolSubbasin(self, currentAttList, rain, evapscale, wqtype):
        """Uses information of the current Block and the broader sub-basin to determine
        the required storage size of a water recycling system to meet required end uses
        and achieve user-defined potable water reduction and reliability targets. It does
        this for a number of combinations, but finds the worst case first e.g.
        
            4 increments: [0.25, 0.5, 0.75, 1.00] of the catchment harvested to treat
                          [0.25, 0.5, 0.75, 1.00] portion of population and public space
                          worst case scenario: 0.25 harvest to supply 1.00 of area
        
        Input parameters:
            - currentAttList: current Attribute list of the block in question
            - rain: rainfall data for determining inflows if planning SW harvesting
            - evapscale: scaling factors for outdoor irrigation demand scaling
            - wqtype: water quality being harvested (determines the type of end uses
                                                     accepable)
        
        Model also considers the self.hs_strategy at this scale, i.e. harvest upstream
        to supply downstream? harvest upstream to supply upstream? harvest upstream to
        supply basin?
        
        Function returns an array of storage volumes in dictionary format identified by
        planning increment."""
        
        #WORKING IN [kL/yr] for single values and [kL/day] for time series
        #(1) Get all Blocks based on the strategy
        harvestblockIDs = self.retrieveStreamBlockIDs(currentAttList, "upstream")
        harvestblockIDs.append(currentAttList.getAttribute("BlockID"))
        if self.hs_strategy == "ud":
            supplytoblockIDs = self.retrieveStreamBlockIDs(currentAttList, "downstream")
            supplytoblockIDs.append(currentAttList.getAttribute("BlockID"))
        elif self.hs_strategy == "uu":
            supplytoblockIDs = harvestblockIDs        #Try ref copy first
    #        supplytoblockIDs = []
    #        for i in range(len(harvestblockIDs)):
    #            supplytoblockIDs.append(harvestblockIDs[i])   #make a direct copy
        elif self.hs_strategy == "ua":
            supplytoblockIDs = self.retrieveStreamBlockIDs(currentAttList, "downstream")
            for i in range(len(harvestblockIDs)):   #To get all basin IDs, simply concatenate the strings
                supplytoblockIDs.append(harvestblockIDs[i])   
        
        #self.notify("HarvestBlocKIDs: "+str(harvestblockIDs))
        #self.notify("SupplyBlockIDs:" +str(supplytoblockIDs))
        
        #(2) Prepare end uses and obtain full demands
        enduses = self.determineEndUses(wqtype)
        bas_totdemand = 0
        bas_subdemand = 0
        for i in supplytoblockIDs:
            #block_attr = self.getBlockUUID(i, city)
            block_attr = self.activesim.getAssetWithName("BlockID"+str(i))
            bas_totdemand += self.getTotalWaterDemandEndUse(block_attr, ["K","S","T", "L", "I", "PI"])
            bas_subdemand += self.getTotalWaterDemandEndUse(block_attr, enduses)
        
        #self.notify("Total basin demands/substitutable "+str(bas_totdemand_+" "+str(bas_subdemand))
        
        #(3) Grab total harvestable area
        AharvestTot = self.retrieveAttributeFromIDs(harvestblockIDs, "Blk_EIA", "sum")
        #self.notify("AharvestTotal: "+str(AharvestTot))
        if AharvestTot == 0:    #no area to harvest
            return np.inf
            #Future - add something to deal with retrofit
        
        storageVol = {}
        #(4) Generate Demand Time Series
        for i in range(len(self.subbas_incr)):          #HARVEST x% LOOP
            if self.subbas_incr[i] == 0:
                continue        #Skip 0 increment

            harvestincr = self.subbas_incr[i]
            storageVol[harvestincr] = {}    #initialize container
            for j in range(len(self.subbas_incr)):      #SUPPLY y% LOOP
                if self.subbas_incr[j] == 0:
                    continue    #Skip 0 increment
                
                supplyincr = self.subbas_incr[j]
                recdemand = bas_totdemand * supplyincr
                if recdemand > bas_subdemand:      #if that demand is greater than what can be substituted, then
                    storageVol[harvestincr][supplyincr] = np.inf         
                    #make it impossible to size a system for that combo
                    continue
                
                Aharvest = AharvestTot * harvestincr
                #self.notify("Required demand: "+str(recdemand))
                if "I" in enduses:
                    demandseries = ubseries.createScaledDataSeries(recdemand, evapscale, False)
                else:
                    demandseries = ubseries.createScaledDataSeries(recdemand/365, len(rain))
                
                if wqtype in ["RW", "SW"]:
                    inflow = ubseries.convertDataToInflowSeries(rain, Aharvest, False)
                    maxinflow = sum(rain)/1000*Aharvest / self.rain_length
                    #self.notify("Average annual inflow: "+str(maxinflow))
                elif wqtype in ["GW"]:
                    inflow = 0
                    maxinflow = 0
                
                if (self.rec_demrange_max/100.0)*maxinflow < recdemand or (self.rec_demrange_min/100.0)*maxinflow > recdemand:
                    #Cannot design a storage for a demand that is not within the user-defined range of total annual inflow
                    storageVol[harvestincr][supplyincr] = np.inf
                    continue
                
                #(5) Size the store for the current combo
                if self.sb_method == "Sim":
                    reqVol = dsim.estimateStoreVolume(inflow, demandseries, self.targets_reliability, self.relTolerance, self.maxSBiterations)
                    #self.notify("reqVol: "+str(reqVol))
                elif self.sb_method == "Eqn":
                    vdemvsupp = recdemand / maxinflow
                    storagePerc = deq.loglogSWHEquation(self.regioncity, self.targets_reliability, inflow, demandseries)
                    reqVol = storagePerc/100*maxinflow  #storagePerc is the percentage of the avg. annual inflow
                
                storeObj = tt.RecycledStorage(wqtype, reqVol, enduses, Aharvest, self.targets_reliability, recdemand, "B")
                storageVol[harvestincr][supplyincr] = storeObj
        return storageVol


    ###################################
    #--- IN-BLOCK OPTIONS CREATION ---#
    ###################################
    def constructInBlockOptions(self, currentAttList, lot_techRES, lot_techHDR, lot_techLI, 
                                lot_techHI, lot_techCOM, street_tech, neigh_tech):
        """Tries every combination of technology and narrows down the list of in-block
        options based on MCA scoring and the Top Ranking Configuration selected by the
        user. Returns an array of the top In-Block Options for piecing together with
        sub-basin scale systems
        Input Arguments:
            - currentAttList - current Block's Attribute list
            - lot_techRES - list of lot-scale technologies for residential land use
            - lot_techHDR - list of lot-scale technologies for HDR land use
            - lot_techLI - list of lot-scale technologies for LI land use
            - lot_techHI - list of lot-scale technologies for HI land use
            - lot_techCOM - list of lot-scale technologies for COM land use
            - street_tech - list of street scale technologies limited to RES land use
            - neigh_tech - list of neighbourhood scale technologies for block
        """
        allInBlockOptions = {}      #Initialize dictionary to hold all in-block options
        currentID = int(currentAttList.getAttribute("BlockID"))
        blockarea = pow(self.block_size,2)*currentAttList.getAttribute("Active")
        
        for i in range(len(self.subbas_incr)):                #e.g. for [0, 0.25, 0.5, 0.75, 1.0]
            allInBlockOptions[self.subbas_incr[i]] = []       #Bins are: 0 to 25%, >25% to 50%, >50% to 75%, >75% to 100% of block treatment
        
        #Obtain all variables needed to do area balance for Impervious Area Service
        allotments = currentAttList.getAttribute("ResAllots")
        estatesLI = currentAttList.getAttribute("LIestates")
        estatesHI = currentAttList.getAttribute("HIestates")
        estatesCOM = currentAttList.getAttribute("COMestates")
        Aimplot = currentAttList.getAttribute("ResLotEIA")
        AimpRes = allotments * Aimplot
        AimpstRes = currentAttList.getAttribute("ResFrontT") - currentAttList.getAttribute("av_St_RES")
        Aimphdr = currentAttList.getAttribute("HDR_EIA")    
        AimpAeLI = currentAttList.getAttribute("LIAeEIA")
        AimpLI = AimpAeLI * estatesLI
        AimpAeHI = currentAttList.getAttribute("HIAeEIA")
        AimpHI = AimpAeHI * estatesHI
        AimpAeCOM = currentAttList.getAttribute("COMAeEIA")
        AimpCOM = AimpAeCOM * estatesCOM
        
        AblockEIA = currentAttList.getAttribute("Manage_EIA")          #Total block imp area to manage
        blockDem = currentAttList.getAttribute("Blk_WD") - currentAttList.getAttribute("wd_Nres_IN")

        if AblockEIA == 0 and blockDem == 0:
            return {}

        #CREATE COMBINATIONS MATRIX FOR ALL LOT SCALE TECHNOLOGIES FIRST
        #   for lot-scale technologies, these are pieced together based on the same increment
        #   combinations are either 0 or the technologies that fit at that increment
        lot_tech = []
        for a in range(len(self.lot_incr)):     #lot_incr = [0, ....., 1.0]
            lot_deg = self.lot_incr[a]          #currently working on all lot-scale systems of increment lot_deg
            if lot_deg == 0:
                lot_tech.append([lot_deg,0,0,0,0,0])      #([deg, res, hdr, li, hi, com])
                continue
            for b in lot_techRES:
                for c in lot_techHDR:
                    if c != 0 and c.getDesignIncrement() != lot_deg:
                        continue
                    for d in lot_techLI:
                        if d != 0 and d.getDesignIncrement() != lot_deg:
                            continue
                        for e in lot_techHI:
                            if e != 0 and e.getDesignIncrement() != lot_deg:
                                continue
                            for f in lot_techCOM:
                                if f != 0 and f.getDesignIncrement() != lot_deg:
                                    continue
                                lot_tech.append([lot_deg, b, c, d, e, f])
        if len(street_tech) == 0:
            street_tech.append(0)
        if len(neigh_tech) == 0:
            neigh_tech.append(0)
        
        #Combine all three scales together
        combocheck =[]
        for a in lot_tech:
            for b in street_tech:
                for c in neigh_tech:
                    lot_deg = a[0]
                    combo = [a[1], a[2], a[3], a[4], a[5], b, c]
                    #if combo in combocheck:
                    #    continue
                    combocheck.append(combo)
                    #self.notify("Combo: "+str(combo)+ " at lot deg: "+str(lot_deg))
                    lotcounts = [int(lot_deg * allotments), int(1), int(estatesLI), int(estatesHI), int(estatesCOM),int(1),int(1)]
                    
                    if allotments != 0 and int(lot_deg*allotments) == 0:
                        continue        #the case of minimal allotments on-site where multiplying by lot-deg and truncation returns zero
                                        #this results in totalimpserved = 0, therefore model crashes on ZeroDivisionError
                    
                    #Check if street + lot systems exceed the requirements
                    if a[1] != 0 and b != 0 and (a[1].getService("Qty")*allotments + b.getService("Qty")) > (AimpRes+AimpstRes):
                        continue    #Overtreatment occurring in residential district at the lot scale for "Qty"
                    if a[1] != 0 and b != 0 and (a[1].getService("WQ")*allotments + b.getService("WQ")) > (AimpRes+AimpstRes):
                        continue    #Overtreatment occurring in residential district at the lot scale for "WQ"
                    if combo.count(0) == 7: 
                        continue    #all options in the combo are zero, then we have no technologies, skip this as well
                    
                    servicematrix = self.getTotalComboService(combo, lotcounts)
                    offsetmatrix = self.getTotalIAOofCombo(combo, lotcounts)
                    #self.notify(servicematrix)
                    
                    if servicematrix[0] > AblockEIA or servicematrix[1] > AblockEIA:
                        #self.notify("Overtreatment on Qty or WQ side")
                        continue
                    elif servicematrix[2] > blockDem: #CHANGE TO DEMAND!
                        #self.notify("Oversupply of demand")
                        continue
                    else:
                        #self.notify("Strategy is fine")
                        #Create Block Strategy and put it into one of the subbas bins of allInBlockOptions
                        servicebin = self.identifyBin(servicematrix, AblockEIA, blockDem)
                        blockstrat = tt.BlockStrategy(combo, servicematrix, lotcounts, currentID, servicebin)
                        blockstrat.setIAO("Qty", offsetmatrix[0])
                        blockstrat.setIAO("WQ", offsetmatrix[1])

                        tt.CalculateMCATechScores(blockstrat,[AblockEIA, AblockEIA, blockDem],self.curscalepref, self.priorities, \
                                                    self.mca_techlist, self.mca_tech, self.mca_env, self.mca_ecn, \
                                                    self.mca_soc, self.iao_influence/100.0)
                        
                        tt.CalculateMCAStratScore(blockstrat, [self.bottomlines_tech_w, self.bottomlines_env_w, \
                                                               self.bottomlines_ecn_w, self.bottomlines_soc_w])
                        #DEBUG - Write to DB file
                        #dbs = tt.createDataBaseString(blockstrat, AblockEIA)
                        #self.dbcurs.execute("INSERT INTO blockstrats VALUES ("+str(dbs)+")")
                        
                    if len(allInBlockOptions[servicebin]) < 10:         #If there are less than ten options in each bin...
                        allInBlockOptions[servicebin].append(blockstrat)        #append the current strategy to the list of that bin
                    else:               #Otherwise get bin's lowest score, compare and replace if necessary
                        lowestscore, lowestscoreindex = self.getServiceBinLowestScore(allInBlockOptions[servicebin])
                        if blockstrat.getTotalMCAscore() > lowestscore:
                            allInBlockOptions[servicebin].pop(lowestscoreindex)      #Pop the lowest score and replace
                            allInBlockOptions[servicebin].append(blockstrat)
                            #dbs = tt.createDataBaseString(blockstrat)
                        elif blockstrat.getTotalMCAscore() == lowestscore:
                            if random.random() > 0.5:   #if the scores are equal: fifty-fifty chance
                                allInBlockOptions[servicebin].pop(lowestscoreindex)      #Pop the lowest score and replace
                                allInBlockOptions[servicebin].append(blockstrat)
                        else:
                            blockstrat = 0      #set null reference
        
        #DEBUG - Transfer all to database table
        # for key in allInBlockOptions.keys():
        #     for i in range(len(allInBlockOptions[key])):
        #         dbs = tt.createDataBaseString(allInBlockOptions[key][i], AblockEIA)
        #         self.dbcurs.execute("INSERT INTO blockstratstop VALUES ("+str(dbs)+")")
        return allInBlockOptions
    
    def getServiceBinLowestScore(self, binlist):
        """Scans none list of BlockStrategies for the lowest MCA total score and returns
        its value as well as the position in the list.
        """
        scorelist = []
        for i in range(len(binlist)):
            scorelist.append(binlist[i].getTotalMCAscore())
        lowscore = min(scorelist)
        lowscoreindex = scorelist.index(lowscore)
        return lowscore, lowscoreindex

    def getTotalIAOofCombo(self, techarray, lotcounts):
        """Tallies up the total impervious area offset for quantity and quality based on the WSUD objects' individual
        offsets.
        """
        service_abbr = ["Qty", "WQ"]
        offsetmatrix = [0, 0]
        for j in range(len(service_abbr)):
            abbr = service_abbr[j]
            for tech in techarray:
                if tech == 0:
                    continue
                if tech.getScale() == "L" and tech.getLandUse() == "RES":
                    offsetmatrix[j] += tech.getIAO(abbr) * lotcounts[0]
                elif tech.getScale() == "L" and tech.getLandUse() == "LI":
                    offsetmatrix[j] += tech.getIAO(abbr) * lotcounts[2]
                elif tech.getScale() == "L" and tech.getLandUse() == "HI":
                    offsetmatrix[j] += tech.getIAO(abbr) * lotcounts[3]
                elif tech.getScale() == "L" and tech.getLandUse() == "COM":
                    offsetmatrix[j] += tech.getIAO(abbr) * lotcounts[4]
                else:
                    offsetmatrix[j] += tech.getIAO(abbr)
        return offsetmatrix
    
    def getTotalComboService(self, techarray, lotcounts):
        """Retrieves all the impervious area served by an array of systems and returns
        the value"""
        service_abbr = ["Qty", "WQ", "Rec"]
        service_booleans = [int(self.ration_runoff), int(self.ration_pollute), int(self.ration_harvest)]
        servicematrix = [0,0,0]
        for j in range(len(servicematrix)):
            if service_booleans[j] == 0:        #If not interested in that particular part
                servicematrix[j] = 0    #Set that service matrix entry to zero and continue
                continue
            abbr = service_abbr[j]
            for tech in techarray:
                if tech == 0:
                    continue
                if tech.getScale() == "L" and tech.getLandUse() == "RES":
                    servicematrix[j] += tech.getService(abbr) * lotcounts[0]
                elif tech.getScale() == "L" and tech.getLandUse() == "LI":
                    servicematrix[j] += tech.getService(abbr) * lotcounts[2]
                elif tech.getScale() == "L" and tech.getLandUse() == "HI":
                    servicematrix[j] += tech.getService(abbr) * lotcounts[3]
                elif tech.getScale() == "L" and tech.getLandUse() == "COM":
                    servicematrix[j] += tech.getService(abbr) * lotcounts[4]
                else:
                    servicematrix[j] += tech.getService(abbr)
        return servicematrix

    def identifyBin(self, servicematrix, AblockEIA, totdemand):
        """Determines what bin to sort a particular service into, used when determining
        which bin a BlockStrategy should go into"""
        if AblockEIA == 0: AblockEIA = 0.0001    #Make infinitesimally small because the only case
        if totdemand == 0: totdemand = 0.0001    #that results from this would be where service == 0

        servicelevels = [servicematrix[0]/AblockEIA, servicematrix[1]/AblockEIA, servicematrix[2]/totdemand]
        #print servicelevels
        bracketwidth = 1.0/float(self.subbas_rigour)   #Used to bin the score within the bracket and penalise MCA score
        blockstratservice = max(servicelevels)
        #self.notify("Maximum service achieved is: "+str(blockstratservice)+" "+str(servicelevels))
        for i in self.subbas_incr:      #[0(skip), 0.25, 0.5, 0.75, 1.0]
            #Identify Bin using 'less than' rule. Will skip the zero increment bin!
#            if blockstratservice < i:   #bins will go from 0 to 0.25, 0.25, to 0.5 etc. (similar for other incr)
#                return i
#            else:
#                continue
            
            #Identify Bin using Bracket
            if blockstratservice >= max((i-(bracketwidth/2)),0) and blockstratservice <= min((i+(bracketwidth/2)),1):
                #self.notify("Bin: "+str(i))
                return i
            else:
                continue
            #self.notify("Bin: "+str(max(self.subbas_incr)))
        return max(self.subbas_incr)
     
     
    ######################################
    #--- GENERATING BASIN REALISATION ---#
    ######################################
    def getBasinBlockIDs(self, currentBasinID, numblocks):
        """Retrieves all blockIDs within the single basin and returns them in the order
        of upstream to downstream based on the length of the upstream strings."""
        basinblocksortarray = []
        basinblockIDs = []
        outletID = 0
        for i in range(int(numblocks)):
            currentID = i+1
            #currentAttList = self.getBlockUUID(currentID, city)
            currentAttList = self.activesim.getAssetWithName("BlockID"+str(currentID))
            if currentAttList.getAttribute("BasinID") != currentBasinID:
                continue
            else:
                upstr = currentAttList.getAttribute("UpstrIDs")
                upstreamIDs = upstr.split(',')
                upstreamIDs.remove('')
                basinblocksortarray.append([len(upstreamIDs),currentID])
            if currentAttList.getAttribute("Outlet") == 1:
                outletID = currentID
        basinblocksortarray.sort()      #sort ascending based on length of upstream string
        for i in range(len(basinblocksortarray)):
            basinblockIDs.append(basinblocksortarray[i][1])     #append just the ID of block
        return basinblockIDs, outletID


    def findSubbasinPartakeIDs(self, basinBlockIDs, subbas_options):
        """Searches the blocks within the basin for locations of possible sub-basin scale
        technologies and returns a list of IDs"""
        partake_IDs = []
        for i in range(len(basinBlockIDs)):
            currentID = int(basinBlockIDs[i])
            try:
                if len(subbas_options["BlockID"+str(currentID)]) != 0:
                    partake_IDs.append(currentID)
                else:
                    continue
            except KeyError:
                continue
        return partake_IDs

    
    def selectTechLocationsByRandom(self, partakeIDs, basinblockIDs):
        """Samples by random a number of sub-basin scale technologies and in-block locations
        for the model to place technologies in, returns two arrays: one of the chosen
        sub-basin IDs and one of the chosen in-block locations"""
        partakeIDsTEMP = []     #Make copies of the arrays to prevent reference-modification
        for i in partakeIDs:
            partakeIDsTEMP.append(i)
        basinblockIDsTEMP = []
        for i in basinblockIDs:
            basinblockIDsTEMP.append(i)
            
        techs_subbas = random.randint(0,len(partakeIDsTEMP))
        subbas_chosenIDs = []
        for j in range(techs_subbas):
            sample_index = random.randint(0,len(partakeIDsTEMP)-1)
            subbas_chosenIDs.append(partakeIDsTEMP[sample_index])
            basinblockIDsTEMP.remove(partakeIDsTEMP[sample_index]) #remove from blocks possibilities
            partakeIDsTEMP.pop(sample_index)    #pop the value from the partake list
        
        techs_blocks = random.randint(0, len(basinblockIDsTEMP))
        inblocks_chosenIDs = []
        for j in range(techs_blocks):
            sample_index = random.randint(0,len(basinblockIDsTEMP)-1)       #If sampling an index, must subtract 1 from len()
            inblocks_chosenIDs.append(basinblockIDsTEMP[sample_index])
            basinblockIDsTEMP.pop(sample_index)
        
        #Reset arrays
        basinblockIDsTEMP = []
        partakeIDsTEMP = []
        return subbas_chosenIDs, inblocks_chosenIDs
    
    
    def calculateRemainingService(self, servtype, basinBlockIDs):
        """Assesses the already treated area/demand for the current basin and returns
        the remaining area/demand to be treated with a strategy.
            - Type: refers to the type of objective "QTY" = quantity, WQ = quality, 
                    REC = recycling
            - basinBlockIDs: array containing all IDs within the current basin
        """
        #self.notify(basinBlockIDs)
        #self.notify(type)
        # print "Basin Blocks", basinBlockIDs
        # print servtype

        if servtype in ["WQ", "QTY"]:
            total = self.retrieveAttributeFromIDs(basinBlockIDs, "Manage_EIA", "sum")
        elif servtype in ["REC"]:
            total = self.retrieveAttributeFromIDs(basinBlockIDs, "Blk_WD", "sum") - \
                    self.retrieveAttributeFromIDs(basinBlockIDs, "wd_Nres_IN", "sum")

        # print "total", total
        #self.notify("Total Imp Area: "+str(total))
        basinTreated = self.retrieveAttributeFromIDs(basinBlockIDs, "Serv"+str(servtype), "sum")
        basinTreated += self.retrieveAttributeFromIDs(basinBlockIDs, "ServUp"+str(servtype), "sum")
        if int(basinTreated) == 0:
            basinTreated = 0.0

        # print "Treated: ", basinTreated
        #self.notify("Treated ImpArea: "+str(basinTreated))
        rationales = {"QTY": bool(int(self.ration_runoff)), "WQ": bool(int(self.ration_pollute)),
                      "REC": bool(int(self.ration_harvest)) }
        services = {"QTY": float(self.servicevector[0]), "WQ": float(self.servicevector[1]), "REC": float(self.servicevector[2])}
        
        if rationales[servtype]:
            basinRemain = max(total - basinTreated, 0)
        else:
            basinRemain = 0
        # print "Total remaining: ", basinRemain

        if total == 0:
            prevService = 1
        else:
            prevService = float(basinTreated)/float(total)

        if max(1- prevService, 0) == 0:
            delta_percent = 0.0
        else:
            delta_percent = max(services[servtype]/100.0*rationales[servtype] - prevService,0.0) / (1.0 - prevService)
        return delta_percent, basinRemain, basinTreated, total
    
    
    def populateBasinWithTech(self, current_bstrategy, subbas_chosenIDs, inblocks_chosenIDs, 
                              inblock_options, subbas_options, basinBlockIDs):
        """Scans through all blocks within a basin from upstream to downstream end and populates the
        various areas selected in chosenIDs arrays with possible technologies available from the 
        options arrays. Returns an updated current_bstrategy object completed with all details.
        """
        partakeIDs = current_bstrategy.getSubbasPartakeIDs()    #returned in order upstream-->downstream
        basintotals = current_bstrategy.getBasinTotalValues()

        if len(partakeIDs) == 0:
            subbas_treatedAimpQTY = 0  #Sum of already treated imp area in upstream sub-basins and the now planned treatment
            subbas_treatedAimpWQ = 0
            subbas_treatedDemREC = 0
            remainAimp_subbasinQTY = max(basintotals[0] - subbas_treatedAimpQTY, 0)
            remainAimp_subbasinWQ = max(basintotals[1] - subbas_treatedAimpWQ, 0)
            remainDem_subbasinRec = max(basintotals[2] - subbas_treatedDemREC, 0)

            #No sub-basin systems, the only populate with in-block technologies using entire basinBlockID list as a guide
            for rbID in basinBlockIDs:
                if rbID not in inblocks_chosenIDs:        #If the Block ID hasn't been chosen,
                    #self.notify("rbID not in inblocks_chosenIDs")
                    continue                            #then skip to next one, no point otherwise


                #Calculate max-degree (1 or less)
                max_deg_matrix = []

                block_Aimp = self.activesim.getAssetWithName("BlockID"+str(rbID)).getAttribute("Manage_EIA")
                block_Dem = self.activesim.getAssetWithName("BlockID"+str(rbID)).getAttribute("Blk_WD") - self.activesim.getAssetWithName("BlockID"+str(rbID)).getAttribute("wd_Nres_IN")

                #self.notify("Block details: "+str(block_Aimp)+" "+str(block_Dem))
                if block_Aimp == 0: #Impervious governs pretty much everything, if it is zero, don't even bother
                    continue
                if bool(int(self.ration_runoff)):
                    max_deg_matrix.append(float(remainAimp_subbasinQTY)/float(block_Aimp))
                if bool(int(self.ration_pollute)):
                    max_deg_matrix.append(float(remainAimp_subbasinWQ)/float(block_Aimp))
                if bool(int(self.ration_harvest)):      #If and only if we are harvesting, we do something to max_deg re block_Dem, otherwise...
                    if block_Dem == 0:
                        continue
                    else:
                        max_deg_matrix.append(float(remainDem_subbasinRec)/float(block_Dem))
                if len(max_deg_matrix) == 0:
                    continue    #If all three cases are not valid then the matrix remains empty

                max_degree = min(min(max_deg_matrix)+float(self.service_redundancy/100.0), 1.0)  #choose the minimum, bring in allowance using redundancy parameter

                deg, obj, treatedQTY, treatedWQ, treatedREC, iaoqty, iaowq = self.pickOption(rbID,max_degree,inblock_options, [block_Aimp*bool(int(self.ration_runoff)), block_Aimp*bool(int(self.ration_pollute)), block_Dem*bool(int(self.ration_harvest))], "BS")
                #self.notify("Option Treats: "+str([treatedQTY, treatedWQ, treatedREC]))
                #self.notify(obj)

                subbas_treatedAimpQTY += treatedQTY + iaoqty
                subbas_treatedAimpWQ += treatedWQ + iaowq
                subbas_treatedDemREC += treatedREC
                remainAimp_subbasinQTY = max(remainAimp_subbasinQTY - treatedQTY, 0)
                remainAimp_subbasinWQ = max(remainAimp_subbasinWQ - treatedWQ, 0)
                remainDem_subbasinRec = max(remainDem_subbasinRec - treatedREC, 0)
                #self.notify("Remaining: "+str([remainAimp_subbasinQTY, remainAimp_subbasinWQ, remainDem_subbasinRec]))
                if deg != 0 and obj != 0:
                    current_bstrategy.appendTechnology(rbID, deg, obj, "b")

            return True     #Exit the function after in-block placement

        #Make a copy of partakeIDs to track blocks
        partakeIDsTracker = []
        for id in partakeIDs:
            partakeIDsTracker.append(id)
        
        #Initialize variables to track objective fulfillment
        subbasID_treatedQTY = {}
        subbasID_treatedWQ = {}
        subbasID_treatedREC = {}
        for i in range(len(partakeIDs)):
            subbasID_treatedQTY[partakeIDs[i]] = 0
            subbasID_treatedWQ[partakeIDs[i]] = 0
            subbasID_treatedREC[partakeIDs[i]] = 0
        
        #Loop across partakeID blocks (i.e. all blocks, which have a precinct tech)
        for i in range(len(partakeIDs)):
            currentBlockID = partakeIDs[i]      #DENOTES CURRENT POSITION IN THE MAP
            currentAttList = self.activesim.getAssetWithName("BlockID"+str(currentBlockID))
            #self.notify("Currently on BlockID: "+str(currentBlockID))
            
            upstreamIDs = self.retrieveStreamBlockIDs(currentAttList, "upstream")
            downstreamIDs = self.retrieveStreamBlockIDs(currentAttList, "downstream")
            #self.notify("Upstream Blocks: "+str(upstreamIDs)+" downstream Blocks: "+str(downstreamIDs))
            
            remainIDs = []    #All blocks upstream of current location that are unique to that location in the sub-basin
            for id in upstreamIDs:
                remainIDs.append(id)
                
            #(1) See if there are existing sub-basins inside the current sub-basin
            subbasinIDs = []            #All blocks that are sub-basins within the subbasin denoted by the current location
            for id in partakeIDsTracker:
                if id in upstreamIDs:
                    subbasinIDs.append(id)
            #self.notify("Subbasins upstream of current location "+str(subbasinIDs))
            for sbID in subbasinIDs:                #then loop over the locations found and
                partakeIDsTracker.remove(sbID)      #remove these from the tracker list so
                                                    #that they are not doubled up
            for id in subbasinIDs:
                remainIDs.remove(id)            #remove the sub-basin ID's ID from remainIDs
                upstrIDs = self.retrieveStreamBlockIDs(self.activesim.getAssetWithName("BlockID"+str(id)), "upstream")
                for upID in upstrIDs:           #Also remove all sub-basinID's upstream block IDs from
                    remainIDs.remove(upID)      #remain IDs, leaving ONLY Blocks local to currentBlockID
            #self.notify("Blocks local to current location: "+str(remainIDs))
            
            #(2) Obtain highest allowable degree of treatment (Max_Degree)
            #------- 2.1 Get Total Imp/Dem needing to be treated at the current position
            upstreamIDs.append(currentBlockID)
            downstreamIDs.append(currentBlockID)        #Add currentBlockID to the array
            
            dp, totalAimpQTY, sv, cp = self.calculateRemainingService("QTY", upstreamIDs)
            
            dp, totalAimpWQ, sv, cp = self.calculateRemainingService("WQ", upstreamIDs)
            
            #self.notify("Total Quantity Aimp: "+str(totalAimpQTY))
            #self.notify("Total Water Quality Aimp: "+str(totalAimpWQ))

            if self.hs_strategy == "ud":
                dP, totalDemREC, sv,cp = self.calculateRemainingService("REC", downstreamIDs)
            elif self.hs_strategy == "uu":
                dP, totalDemREC, sv, cp = self.calculateRemainingService("REC", upstreamIDs)
            elif self.hs_strategy == "ua":
                dP, totalDemREC, sv, cp = self.calculateRemainingService("REC", basinBlockIDs)
            
            #------- 2.2 Subtract the already serviced parts from upstream sub-basin blocks
            max_deg_matrix = []
            subbas_treatedAimpQTY = 0  #Sum of already treated imp area in upstream sub-basins and the now planned treatment
            subbas_treatedAimpWQ = 0
            subbas_treatedDemREC = 0
            
            for sbID in subbasinIDs:
                subbas_treatedAimpQTY += subbasID_treatedQTY[sbID]  #Check all upstream sub-basins for their treated Aimp            
                subbas_treatedAimpWQ += subbasID_treatedWQ[sbID]    #Check all upstream sub-basins for their treated Aimp            
            
            #self.notify(subbas_treatedAimpQTY)
            #self.notify(subbas_treatedAimpWQ)

            remainAimp_subbasinQTY = max(totalAimpQTY - subbas_treatedAimpQTY, 0)
            if bool(int(self.ration_runoff)) and totalAimpQTY != 0:
                max_deg_matrix.append(remainAimp_subbasinQTY / totalAimpQTY)

            remainAimp_subbasinWQ = max(totalAimpWQ - subbas_treatedAimpWQ, 0)
            if bool(int(self.ration_pollute)) and totalAimpWQ != 0:
                max_deg_matrix.append(remainAimp_subbasinWQ / totalAimpWQ)

            if self.hs_strategy == 'ud':
                totSupply = 0
                downstreamIDs = []      #the complete matrix of all downstream IDs from all upstream sbIDs
                for sbID in subbasinIDs:
                    totSupply += subbasID_treatedREC[sbID]      #Get total supply of all combined upstream systems
                    downIDs = self.retrieveStreamBlockIDs(self.activesim.getAssetWithName("BlockID"+str(sbID)), "downstream")
                    downIDs.append(sbID)
                    for dID in downIDs:
                        if dID not in downstreamIDs: downstreamIDs.append(dID)
                #Get all blocks between currentID's upstream and sbIDs downstream blocks
                shareIDs = []
                for dID in downstreamIDs:
                    if dID in upstreamIDs and dID not in shareIDs:
                        shareIDs.append(dID)
                #Calculate Total Water Demand of Blocks in between the current point and highest upstream point
                totBetweenDem = self.retrieveAttributeFromIDs(shareIDs, "Blk_WD", "sum") - \
                    self.retrieveAttributeFromIDs(shareIDs, "wd_Nres_IN", "sum")
                #Remaining demand is total downstream demand minus the higher of (total upstream supply excess and zero)
                remainDem_subbasinRec = totalDemREC - max(totSupply - totBetweenDem, 0)
            elif self.hs_strategy in ['uu', 'ua']:
                for sbID in subbasinIDs:
                    subbas_treatedDemREC += subbasID_treatedREC[sbID]
                remainDem_subbasinRec = max(totalDemREC - subbas_treatedDemREC, 0)
            
            if bool(int(self.ration_harvest)) and totalDemREC != 0:
                max_deg_matrix.append(remainDem_subbasinRec / totalDemREC)

            # print "Max_deg_matrix", max_deg_matrix
            #self.notify("Max Degre matrix: "+str(max_deg_matrix)
            if len(max_deg_matrix) == 0:
                continue

            max_degree = min(max_deg_matrix)+float(self.service_redundancy/100.0)  #choose the minimum, bring in allowance using redundancy parameter
            
            current_bstrategy.addSubBasinInfo(currentBlockID, upstreamIDs, subbasinIDs, [totalAimpQTY,totalAimpWQ,totalDemREC])
            #self.notify([totalAimpQTY,totalAimpWQ,totalDemREC])
            #self.notify("Current State of Treatment: "+str([subbas_treatedAimpQTY, subbas_treatedAimpWQ, subbas_treatedDemREC]))
            
            #(3) PICK A SUB-BASIN TECHNOLOGY
            if currentBlockID in subbas_chosenIDs:
                deg, obj, treatedQTY, treatedWQ, treatedREC, iaoqty, iaowq = self.pickOption(currentBlockID, max_degree, subbas_options, [totalAimpQTY, totalAimpWQ, totalDemREC], "SB")
                #self.notify("Option Treats: "+str([treatedQTY, treatedWQ, treatedREC]))
                #self.notify(obj)

                subbas_treatedAimpQTY += treatedQTY + iaoqty
                subbas_treatedAimpWQ += treatedWQ + iaowq
                subbas_treatedDemREC += treatedREC
                remainAimp_subbasinQTY = max(remainAimp_subbasinQTY - treatedQTY, 0)
                remainAimp_subbasinWQ = max(remainAimp_subbasinWQ - treatedWQ, 0)
                remainDem_subbasinRec = max(remainDem_subbasinRec - treatedREC, 0)
                #self.notify("Remaining: "+str([remainAimp_subbasinQTY, remainAimp_subbasinWQ, remainDem_subbasinRec]))
                if deg != 0 and obj != 0:
                    current_bstrategy.appendTechnology(currentBlockID, deg, obj, "s")

            #(4) PICK AN IN-BLOCK STRATEGY IF IT IS HAS BEEN CHOSEN
            for rbID in remainIDs:
                if rbID not in inblocks_chosenIDs:        #If the Block ID hasn't been chosen,
                    #self.notify("rbID not in inblocks_chosenIDs")
                    continue                            #then skip to next one, no point otherwise
                
                max_deg_matrix = [1]
                block_Aimp = self.activesim.getAssetWithName("BlockID"+str(rbID)).getAttribute("Manage_EIA")
                block_Dem = self.activesim.getAssetWithName("BlockID"+str(rbID)).getAttribute("Blk_WD") - self.activesim.getAssetWithName("BlockID"+str(rbID)).getAttribute("wd_Nres_IN")
                #self.notify("Block details: "+str(block_Aimp)+" "+str(block_Dem))
                if block_Aimp == 0:     #Impervious governs pretty much everything, if it is zero, don't even bother
                    continue
                if block_Dem == 0 and bool(int(self.ration_harvest)):   #If demand is zero and we are planning for recycling, skip
                    continue
                #self.notify("Can select a block option for current Block")
                
                if bool(int(self.ration_runoff)):
                    max_deg_matrix.append(remainAimp_subbasinQTY/block_Aimp)
                if bool(int(self.ration_pollute)):
                    max_deg_matrix.append(remainAimp_subbasinWQ/block_Aimp)
                if bool(int(self.ration_harvest)):
                    max_deg_matrix.append(remainDem_subbasinRec/block_Dem)
                #self.notify("Block Degrees: "+str(max_deg_matrix))
                max_degree = min(max_deg_matrix) + float(self.service_redundancy/100)
                #self.notify(str([block_Aimp*int(self.ration_runoff))+" "+str(block_Aimp*int(self.ration_pollute))+" "+str(block_Dem*int(self.ration_harvest)]))
                
                #self.notify("In Block Maximum Degree: "+str(max_degree))
                deg, obj, treatedQTY, treatedWQ, treatedREC, iaoqty, iaowq = self.pickOption(rbID,max_degree,inblock_options, [block_Aimp*bool(int(self.ration_runoff)), block_Aimp*bool(int(self.ration_pollute)), block_Dem*bool(int(self.ration_harvest))], "BS")
                #self.notify("Option Treats: "+str([treatedQTY, treatedWQ, treatedREC]))
                #self.notify(obj)

                subbas_treatedAimpQTY += treatedQTY + iaoqty
                subbas_treatedAimpWQ += treatedWQ + iaowq
                subbas_treatedDemREC += treatedREC
                remainAimp_subbasinQTY = max(remainAimp_subbasinQTY - treatedQTY, 0)
                remainAimp_subbasinWQ = max(remainAimp_subbasinWQ - treatedWQ, 0)
                remainDem_subbasinRec = max(remainDem_subbasinRec - treatedREC, 0)
                #self.notify("Remaining: "+str([remainAimp_subbasinQTY, remainAimp_subbasinWQ, remainDem_subbasinRec]))
                if deg != 0 and obj != 0:
                    current_bstrategy.appendTechnology(rbID, deg, obj, "b")
            
            #(5) FINALIZE THE SERVICE VALUES FOR QTY, WQ, REC BEFORE NEXT LOOP
            #Impervious area offset will result in options going over treatment threshold.
            subbasID_treatedQTY[currentBlockID] = subbas_treatedAimpQTY #min(subbas_treatedAimpQTY, totalAimpQTY)
            subbasID_treatedWQ[currentBlockID] = subbas_treatedAimpWQ #min(subbas_treatedAimpWQ, totalAimpWQ)
            subbasID_treatedREC[currentBlockID] = min(subbas_treatedDemREC, totalDemREC)
            #self.notify(subbasID_treatedQTY)
            #self.notify(subbasID_treatedWQ)
        return True
    
    #################################################
    #--- RANKING AND CHOOSING BASIN REALISATIONS ---#
    #################################################
    def evaluateServiceObjectiveFunction(self, basinstrategy, updatedservice):
        """Calculates how close the basinstrategy meets the required service
        levels set by the user. A performance metric is returned. If one of the
        service levels has not been met, performance is automatically assigned
        a value of -1. It will then be removed in the main program.
        The objective function used to find the optimum strategies is calculated
        as:
            choice = min { sum(serviceProvided - serviceRequired) }, OF >0
            updatedservice = [serviceQty, serviceWQ, serviceREC] based on delta_percent
        """
        serviceQty = float(int(self.ration_runoff))*float(updatedservice[0])
        serviceWQ = float(int(self.ration_pollute))*float(updatedservice[1])
        serviceRec = float(int(self.ration_harvest))*float(updatedservice[2])
        serviceRequired = [serviceQty, serviceWQ, serviceRec]
        serviceBooleans = [int(self.ration_runoff), int(self.ration_pollute), int(self.ration_harvest)]
        
        serviceProvided = basinstrategy.getServicePvalues() #[0,0,0] P values for service
        for i in range(len(serviceProvided)):
            serviceProvided[i] *= float(serviceBooleans[i])     #Rescale to ensure no service items are zero
        #self.notify("Service Req "+str(serviceProvided))
        #self.notify("Service Provided "+str(serviceRequired))
        #Objective Criterion: A strategy is most suitable to the user's input
        #requirements if the sum(service-provided - service-required) is a minimum
        #and >0
        negative = False
        performance = 0
        for i in range(len(serviceProvided)):
            performance += (serviceProvided[i] - serviceRequired[i])
            if (serviceProvided[i] - serviceRequired[i]) < 0:
                negative = True
        if negative:
            performance = -1       #One objective at least, not fulfilled
        return performance
    
    def pickOption(self, blockID, max_degree, options_collection, totals, strattype):
        """Picks and returns a random option based on the input impervious area and maximum
        treatment degree. Can be used on either the in-block strategies or larger precinct 
        strategies. If it cannot pick anything, it will return zeros all around.
        """
        bracketwidth = 1.0/float(self.subbas_rigour)    #Use bracket to determine optimum bin
        
        #self.notify(options_collection["BlockID"+str(blockID)])
        if strattype == "BS":   #in-block strategy
            options = []
            
            #Continuous-based picking
            for i in options_collection["BlockID"+str(blockID)].keys():
                if (i-bracketwidth/2) >= max_degree:                
                    continue
                for j in options_collection["BlockID"+str(blockID)][i]:
                    options.append(j)
                        
            #Bin-based picking
#            degs = []   #holds all the possible increments within max_degree
#            for i in options_collection["BlockID"+str(blockID)].keys():
#                if (i-bracketwidth/2) <= max_degree:                
#                    degs.append(i)  #add as a possible increment
#            if len(degs) != 0:
#                chosen_deg = degs[random.randint(0, len(degs)-1)]
#                for j in options_collection["BlockID"+str(blockID)][chosen_deg]:
#                    options.append(j)
                    
            if len(options) == 0:
                return 0, 0, 0, 0, 0, 0, 0
            scores = []
            for i in options:
                scores.append(i.getTotalMCAscore())
            
            #self.notify("Scores: "+str(scores))

            #Pick Option
            scores = self.createCDF(scores)
            #self.notify("Scores CDF: "+str(scores))
            choice = self.samplefromCDF(scores)
            #self.notify(choice)
            chosen_obj = options[choice]
            
#            AimpQTY = totals[0]
#            AimpWQ = totals[1]
#            DemREC = totals[2]
#            treatedAimpQTY = chosen_deg * AimpQTY
#            treatedAimpWQ = chosen_deg * AimpWQ
#            treatedDemREC = chosen_deg * DemREC            
            treatedAimpQTY = chosen_obj.getService("Qty")
            iaoqty = chosen_obj.getIAO("Qty")
            treatedAimpWQ = chosen_obj.getService("WQ")
            iaowq = chosen_obj.getIAO("WQ")
            treatedDemREC = chosen_obj.getService("Rec")
            return chosen_obj.getBlockBin(), chosen_obj, treatedAimpQTY, treatedAimpWQ, treatedDemREC, iaoqty, iaowq
        
        elif strattype == "SB":  #sub-basin strategy
            #Continuous-based picking
            options = []
            for deg in self.subbas_incr:
                if(deg-bracketwidth/2) >= max_degree:
                    continue
                for j in options_collection["BlockID"+str(blockID)][deg]:
                    options.append(j)

            if len(options) != 0:
                chosen_obj = options[random.randint(0, len(options)-1)]
                
            #Bin-based picking
#            AimpQTY = totals[0]
#            AimpWQ = totals[1]
#            DemREC = totals[2]
#            indices = []
#            for deg in self.subbas_incr:
#                if (deg-bracketwidth/2) <= max_degree:
#                    indices.append(deg)
#            if len(indices) != 0:
#                choice = random.randint(0, len(indices)-1)
#                chosen_deg = self.subbas_incr[choice]
#            else:
#                return 0, 0, 0, 0, 0
#            
#            Nopt = len(options_collection["BlockID"+str(blockID)][chosen_deg])
#            
#            if Nopt != 0:
#            #if chosen_deg != 0 and Nopt != 0:
##                treatedAimpQTY = chosen_deg * AimpQTY
##                treatedAimpWQ = chosen_deg * AimpWQ
##                treatedDemREC = chosen_deg * DemREC
#                choice = random.randint(0, Nopt-1)
#                chosen_obj = options_collection["BlockID"+str(blockID)][chosen_deg][choice]
#                
                if chosen_obj == 0:
                    return 0, 0, 0, 0, 0, 0, 0
                chosen_deg = chosen_obj.getDesignIncrement()
                treatedAimpQTY = chosen_obj.getService("Qty")
                iaoqty = chosen_obj.getIAO("Qty")
                treatedAimpWQ = chosen_obj.getService("WQ")
                iaowq = chosen_obj.getIAO("WQ")
                treatedDemREC = chosen_obj.getService("Rec")

                return chosen_deg, chosen_obj, treatedAimpQTY, treatedAimpWQ, treatedDemREC, iaoqty, iaowq
            else:
                return 0, 0, 0, 0, 0, 0, 0
    
    def createCDF(self, score_matrix):
        """Creates a cumulative distribution for an input list of values by normalizing
        these first and subsequently summing probabilities.
        """

        pdf = []
        cdf = []
        for i in range(len(score_matrix)):
            if sum(score_matrix) == 0:
                pdf.append(1.0/float(len(score_matrix)))
            else:
                pdf.append(score_matrix[i]/sum(score_matrix))
        cumu_p = 0
        for i in range(len(pdf)):
            cumu_p += pdf[i]
            cdf.append(cumu_p)
        cdf[len(cdf)-1] = 1.0   #Adjust for rounding errors
        return cdf
    
    def samplefromCDF(self, selection_cdf):
        """Samples one sample from a cumulative distribution function and returns
        the index. Sampling is uniform, probabilities are determined by the CDF"""
        p_sample = random.random()
        for i in range(len(selection_cdf)):
            if p_sample <= selection_cdf[i]:
                return i
        return (len(selection_cdf)-1)
            
    ####################################
    #--- TRANSFER OF DATA TO OUTPUT ---#
    ####################################
    def writeStrategyView(self, id, basinID, basinBlockIDs, strategydata):
        """Writes the output view of the selected WSUD strategy and saves it to the 
        self.wsudAttr View.
        """
        strat_object = strategydata[0]
        strat_score = strategydata[1]

        for i in range(len(basinBlockIDs)):
            currentID = basinBlockIDs[i]
            #currentAttList = self.getBlockUUID(currentID, city)
            currentAttList = self.activesim.getAssetWithName("BlockID"+str(currentID))
            centreX = currentAttList.getAttribute("CentreX")
            centreY = currentAttList.getAttribute("CentreY")
            #Grab the strategy objects
            inblock_strat = strat_object.getIndividualTechStrat(currentID, "b")
            
            if inblock_strat == None:
                inblock_systems = [0,0,0,0,0,0,0]
                inblock_degs = [0,0,0,0,0,0,0]
                inblock_lotcount = [0,0,0,0,0,0,0]
            else:
                inblock_systems = inblock_strat.getTechnologies()
                inblock_degs = [0,0,0,0,0,0,0]
                inblock_lotcount = inblock_strat.getQuantity("all")
                
                for j in range(len(inblock_systems)):
                    if inblock_systems[j] != 0:
                        inblock_degs[j] = inblock_systems[j].getDesignIncrement()
                        
            offsets_matrix = [[centreX+float(self.block_size)/16.0, centreY+float(self.block_size)/4.0],
                              [centreX+float(self.block_size)/12.0, centreY+float(self.block_size)/4.0],
                              [centreX+float(self.block_size)/8.0, centreY+float(self.block_size)/4.0],
                              [centreX+float(self.block_size)/4.0, centreY+float(self.block_size)/4.0],
                              [centreX+float(self.block_size)/3.0, centreY+float(self.block_size)/4.0],
                              [centreX+float(self.block_size)/4.0, centreY-float(self.block_size)/8.0],
                              [centreX-float(self.block_size)/8.0, centreY-float(self.block_size)/4.0],
                              [centreX-float(self.block_size)/4.0, centreY-float(self.block_size)/8.0]]
                                #[Res, HDR, LI, HI, COM, ORC, Street, Neigh, Subbas]
            blockscale_names = ["L_RES", "L_HDR", "L_LI", "L_HI", "L_COM", "S", "N"]
            
            for j in range(len(blockscale_names)):
                if inblock_strat == None or inblock_systems[j] == 0:
                    continue
                current_wsud = inblock_systems[j]
                scale = blockscale_names[j]
                coordinates = offsets_matrix[j]
                goalqty = inblock_lotcount[j]
                
                loc = ubdata.UBComponent()
                #loc = city.addNode(coordinates[0], coordinates[1], 0, self.wsudAttr)
                loc.addAttribute("StrategyID", id)
                loc.addAttribute("MCAscore", strat_score)
                loc.addAttribute("posX", coordinates[0])
                loc.addAttribute("posY", coordinates[1])
                loc.addAttribute("BasinID", basinID)
                loc.addAttribute("Location", currentID)
                loc.addAttribute("Scale", scale)
                loc.addAttribute("Type", current_wsud.getType())
                loc.addAttribute("Qty", 0)      #Currently none available
                loc.addAttribute("GoalQty", goalqty)  #lot scale mainly - number of lots to build
                loc.addAttribute("SysArea", current_wsud.getSize())
                loc.addAttribute("StoreVol", current_wsud.getRecycledStorageVolume())
                loc.addAttribute("StoreType", current_wsud.getRecycledStorageType())
                loc.addAttribute("IntegStore", current_wsud.isStoreIntegrated())
                loc.addAttribute("Status", 0)   #0 = not built, 1 = built
                loc.addAttribute("Year", 9999)
                loc.addAttribute("EAFact", current_wsud.getAreaFactor())
                loc.addAttribute("SvWQ_ImpT", current_wsud.getService("WQ"))
                loc.addAttribute("SvQty_ImpT", current_wsud.getService("Qty"))
                loc.addAttribute("SvRec_Supp", current_wsud.getService("Rec"))
                loc.addAttribute("CurImpTWQ", 0)  #New systems don't treat anything yet, not implemented
                loc.addAttribute("CurImpTQty", 0)    #New systems don't treat anything yet, not implemented
                loc.addAttribute("CurSupply", 0)    #New systems don't supply yet
                loc.addAttribute("SupplyRel", float(self.targets_reliability * self.ration_harvest))
                loc.addAttribute("Upgrades", 0) #Done in the retrofit/implementation part
                #city.addComponent(loc, self.wsudAttr)

                #Transfer the key system specs
                if current_wsud.getType() in ["BF", "IS", "WSUR"]:
                    loc.addAttribute("WDepth", eval("self."+str(current_wsud.getType())+"spec_EDD"))
                elif current_wsud.getType() in ["PB"]:
                    loc.addAttribute("WDepth", float(eval("self."+str(current_wsud.getType())+"spec_MD")))
                elif current_wsud.getType() in ["RT"]:
                    loc.addAttribute("WDepth", float(eval("self." + str(current_wsud.getType()) + "_maxdepth")))

                if current_wsud.getType() in ["BF", "IS"]:
                    loc.addAttribute("FDepth", eval("self."+str(current_wsud.getType())+"spec_FD"))
                if current_wsud.getType() in ["BF", "SW", "IS", "WSUR", "PB"]:
                    loc.addAttribute("Exfil", eval("self."+str(current_wsud.getType())+"exfil"))
                else:
                    loc.addAttribute("Exfil", 0)

                # Transfer storage properties to outputs
                if current_wsud.isStoreIntegrated() == 0 and current_wsud.getRecycledStorageType() in ["RT"]:  # Tank storages
                    loc.addAttribute("ST_Depth", eval("self." + str(current_wsud.getRecycledStorageType() + "_maxdepth")))
                    loc.addAttribute("ST_Dead", eval("self." + str(current_wsud.getRecycledStorageType() + "_mindead")))
                elif current_wsud.isStoreIntegrated() == 0 and current_wsud.getRecycledStorageType() in ["PB"]:  # Pond storages
                    loc.addAttribute("ST_Depth", eval("self." + str(current_wsud.getRecycledStorageType() + "spec_MD")))
                    loc.addAttribute("ST_Dead", 0.2)  # Currently assume standard PPD as dead storage for the pond
                elif current_wsud.isStoreIntegrated():
                    loc.addAttribute("ST_Depth", loc.getAttribute("WDepth"))
                    loc.addAttribute("ST_Dead", 0.2)
                else:
                    loc.addAttribute("ST_Depth", 0.0)
                    loc.addAttribute("ST_Dead", 0.0)

                sysID = len(self.activesim.getAssetsWithIdentifier("SysID"))+1
                self.activesim.addAsset("SysID"+str(sysID), loc)

            outblock_strat = strat_object.getIndividualTechStrat(currentID, "s")
            if outblock_strat != None:
                scale = "B"
                coordinates = offsets_matrix[7]
                
                #loc = Component()
                loc = ubdata.UBComponent()
                #loc = city.addNode(coordinates[0], coordinates[1], 0, self.wsudAttr)
                loc.addAttribute("StrategyID", id)
                loc.addAttribute("MCAscore", strat_score)
                loc.addAttribute("posX", coordinates[0])
                loc.addAttribute("posY", coordinates[1])
                loc.addAttribute("BasinID", basinID)
                loc.addAttribute("Location", currentID)
                loc.addAttribute("Scale", scale)
                loc.addAttribute("Type", outblock_strat.getType())
                loc.addAttribute("Qty", 0)      #currently none available
                loc.addAttribute("GoalQty", 1)  #lot scale mainly - number of lots to build
                loc.addAttribute("SysArea", outblock_strat.getSize())
                loc.addAttribute("StoreVol", outblock_strat.getRecycledStorageVolume())
                loc.addAttribute("StoreType", outblock_strat.getRecycledStorageType())
                loc.addAttribute("IntegStore", outblock_strat.isStoreIntegrated())
                loc.addAttribute("Status", 0)
                loc.addAttribute("Year", 9999)
                loc.addAttribute("EAFact", outblock_strat.getAreaFactor())
                loc.addAttribute("SvWQ_ImpT", outblock_strat.getService("WQ"))
                loc.addAttribute("SvQty_ImpT", outblock_strat.getService("Qty"))
                loc.addAttribute("SvRec_Supp", outblock_strat.getService("Rec"))
                loc.addAttribute("CurImpTWQ", 0)  #New systems don't treat anything yet, not implemented
                loc.addAttribute("CurImpTQty", 0)    #New systems don't treat anything yet, not implemented
                loc.addAttribute("CurSupply", 0)    #New systems don't supply yet
                loc.addAttribute("SupplyRel", float(self.targets_reliability * self.ration_harvest))
                loc.addAttribute("Upgrades", 0)
                #city.addComponent(loc, self.wsudAttr)

                #Transfer the key system specs
                if outblock_strat.getType() in ["BF", "IS", "WSUR"]:
                    loc.addAttribute("WDepth", eval("self."+str(outblock_strat.getType())+"spec_EDD"))
                elif outblock_strat.getType() in ["PB"]:
                    loc.addAttribute("WDepth", float(eval("self."+str(outblock_strat.getType())+"spec_MD")))
                elif outblock_strat.getType() in ["RT"]:
                    loc.addAttribute("WDepth", float(eval("self." + str(outblock_strat.getType()) + "_maxdepth")))

                if outblock_strat.getType() in ["BF", "IS"]:
                    loc.addAttribute("FDepth", eval("self."+str(outblock_strat.getType())+"spec_FD"))
                if outblock_strat.getType() in ["BF", "SW", "IS", "WSUR", "PB"]:
                    loc.addAttribute("Exfil", eval("self."+str(outblock_strat.getType())+"exfil"))
                else:
                    loc.addAttribute("Exfil", 0)

                # Transfer storage properties to outputs
                if outblock_strat.isStoreIntegrated() == 0 and outblock_strat.getRecycledStorageType() in ["RT"]:  # Tank storages
                    loc.addAttribute("ST_Depth", eval("self." + str(outblock_strat.getRecycledStorageType()+"_maxdepth")))
                    loc.addAttribute("ST_Dead",  eval("self." + str(outblock_strat.getRecycledStorageType()+"_mindead")))
                elif outblock_strat.isStoreIntegrated() == 0 and outblock_strat.getRecycledStorageType() in ["PB"]:  # Pond storages
                    loc.addAttribute("ST_Depth", eval("self." + str(outblock_strat.getRecycledStorageType()+"spec_MD")))
                    loc.addAttribute("ST_Dead", 0.2)  # Currently assume standard PPD as dead storage for the pond
                elif outblock_strat.isStoreIntegrated():
                    loc.addAttribute("ST_Depth", loc.getAttribute("WDepth"))
                    loc.addAttribute("ST_Dead", 0.2)
                else:
                    loc.addAttribute("ST_Depth", 0.0)
                    loc.addAttribute("ST_Dead", 0.0)

                sysID = len(self.activesim.getAssetsWithIdentifier("SysID"))+1
                self.activesim.addAsset("SysID"+str(sysID), loc)
        return True
    
    def transferExistingSystemsToOutput(self, stratID, score, basinID):
        """Writes all existing systems to the new output view under a new strategyID as they
        will accompany all newly planned systems under a future alternative"""
        #existSys = city.getUUIDsOfComponentsInView(self.sysAttr)
        existSys = self.activesim.getAssetsWithIdentifier("SysPrevID")
        for curSys in existSys:
            if curSys == None:
                continue
            if int(curSys.getAttribute("BasinID")) != int(basinID):
                continue        #If the system is not in the current basin, don't transfer it yet.

            loc = ubdata.UBComponent()   #Create a new placeholder for a component object, save it to self.wsudAttr View
            loc.addAttribute("StrategyID", stratID)
            loc.addAttribute("MCAscore", score)
            loc.addAttribute("posX", curSys.getAttribute("posX"))
            loc.addAttribute("posY", curSys.getAttribute("posY"))
            loc.addAttribute("BasinID", int(curSys.getAttribute("BasinID")))
            loc.addAttribute("Location", int(curSys.getAttribute("Location")))
            loc.addAttribute("Scale", curSys.getAttribute("Scale"))
            loc.addAttribute("Type", curSys.getAttribute("Type"))
            loc.addAttribute("Qty", curSys.getAttribute("Qty"))      #currently none available
            loc.addAttribute("GoalQty", curSys.getAttribute("GoalQty"))  #lot scale mainly - number of lots to build
            loc.addAttribute("SysArea", curSys.getAttribute("SysArea"))
            loc.addAttribute("StoreVol", curSys.getAttribute("StoreVol"))
            loc.addAttribute("StoreType", curSys.getAttribute("StoreType"))
            loc.addAttribute("IntegStore", curSys.getAttribute("IntegStore"))
            loc.addAttribute("Status", int(curSys.getAttribute("Status")))
            loc.addAttribute("Year", int(curSys.getAttribute("Year")))
            loc.addAttribute("EAFact", curSys.getAttribute("EAFact"))
            loc.addAttribute("SvWQ_ImpT", curSys.getAttribute("SvWQ_ImpT"))
            loc.addAttribute("SvQty_ImpT", curSys.getAttribute("SvQty_ImpT"))
            loc.addAttribute("SvRec_Supp", curSys.getAttribute("SvRec_Supp"))
            loc.addAttribute("CurImpTWQ", curSys.getAttribute("CurImpTWQ"))  #New systems don't treat anything yet, not implemented
            loc.addAttribute("CurImpTQty", curSys.getAttribute("CurImpTQty"))    #New systems don't treat anything yet, not implemented
            loc.addAttribute("CurSupply", curSys.getAttribute("CurSupply"))    #New systems don't supply yet
            loc.addAttribute("SupplyRel", curSys.getAttribute("SupplyRel"))
            loc.addAttribute("Upgrades", int(curSys.getAttribute("Upgrades")))
            loc.addAttribute("WDepth", curSys.getAttribute("WDepth"))
            loc.addAttribute("FDepth", curSys.getAttribute("FDepth"))
            loc.addAttribute("Exfil", curSys.getAttribute("Exfil"))
            loc.addAttribute("ST_Depth", curSys.getAttribute("ST_Depth"))
            loc.addAttribute("ST_Dead", curSys.getAttribute("ST_Dead"))
            sysID = len(self.activesim.getAssetsWithIdentifier("SysID"))+1
            self.activesim.addAsset("SysID"+str(sysID), loc)
        return True
    
    
    def debugPlanning(self, basin_strategies_matrix, basinID):
        print "NOW DEBUGGING PLANNING", self.temp_dir+"/MCRSum-"+str(self.tabindex)+"-BasinID"+str(basinID)+".csv"
        f = open(self.temp_dir+"/MCRSum-"+str(self.tabindex)+"-BasinID"+str(basinID)+".csv", 'w')
        for i in range(len(basin_strategies_matrix)):
            cbs = basin_strategies_matrix[i]
            f.write(str(cbs[0])+","+str(cbs[1])+","+str(cbs[2])+","+str(cbs[3])+"\n")
        f.close()
        return True
            