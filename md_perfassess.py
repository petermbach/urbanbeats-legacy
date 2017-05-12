# -*- coding: utf-8 -*-
"""
@file
@author  Peter M Bach <peterbach@gmail.com>
@version 1.0
@section LICENSE

This file is part of UrbanBEATS (www.urbanbeatsmodel.com)
Copyright (C) 2011, 2012, 2013  Peter M Bach

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
from md_perfassessguic import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import PyQt4

import sys, random, numpy, math, os, scipy, Polygon
import dateutil.parser as dtparse
import scipy.spatial as sps
from osgeo import ogr, osr
import pymusic, ubmusicwrite, ubepanet
import urbanbeatsdatatypes as ubdata
import ubseriesread as ubseries
import md_perf_waterbalance as ubwaterbal
import ubeconomics as ubecon

from urbanbeatsmodule import *

class PerformanceAssess(UBModule):      #UBCORE
    """Performs performance assessment actions on the output set of blocks and WSUD options
    performance assessment is quite modular.

    v1.0: Initial build of revised concept of Performance Assessment
        - Three key features: MUSIC simulation file creation, economics, microclimate
        - MUSIC interface quite simplistic, but allows linkage with WSC Toolkit

	@ingroup UrbanBEATS
        @author Peter M Bach
        """

    def __init__(self, activesim, tabindex):      #UBCORE
        UBModule.__init__(self)      #UBCORE
        # CORE: contains either planning or implementation (so it knows what to do and whether to skip)
        self.tabindex = tabindex        #UBCORE: the simulation period (knowing what iteration this module is being run at)
        self.activesim = activesim      #UBCORE
        self.LUCMatrix = ["RES", "COM", "ORC", "LI", "HI", "CIV", "SVU", "RD", "TR", "PG", "REF", "UND", "NA"]

        #PARAMETER LIST START
        #-----------------------------------------------------------------------
        #SELECT ANALYSES TAB
        self.createParameter("cycletype", STRING, "Use which data set?, pc or ic")
        self.cycletype = "pc"

        self.createParameter("perf_MUSIC", BOOL, "Yes/No MUSIC")
        self.createParameter("perf_Economics", BOOL, "Yes/No Economic Stuff")
        self.createParameter("perf_Microclimate", BOOL, "Yes/No Microclimate Stuff")
        self.createParameter("perf_EPANET", BOOL, "Yes/No EPANET Link")
        self.createParameter("perf_CD3", BOOL, "Yes/No Integrated Water Cycle Model")
        self.perf_MUSIC = 0
        self.perf_Economics = 0
        self.perf_Microclimate = 0
        self.perf_EPANET = 0
        self.perf_CD3 = 0

        #CLIMATE TAB
        self.createParameter("rainfile", STRING, "Rainfall filepath")
        self.createParameter("evapfile", STRING, "Evapotranspiration filepath")
        self.createParameter("analysis_dt", DOUBLE, "Analysis time step [mins]")
        self.createParameter("rainyears", DOUBLE, "Number of years of rainfall to use")
        self.rainfile = "<none>"
        self.evapfile = "<none>"
        self.analysis_dt = 6.0
        self.rainyears = 2

        self.createParameter("rainscale", BOOL, "Scale rainfall data?")
        self.createParameter("evapscale", BOOL, "Scale evapotranspiration data?")
        self.createParameter("rainscalars", LISTDOUBLE, "Monthly scaling factors for rain")
        self.createParameter("evapscalars", LISTDOUBLE, "Monthly scaling factors for evapotranspiration")
        self.rainscale = 0
        self.evapscale = 0
        self.rainscalars = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
        self.evapscalars = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]

        self.createParameter("rainscaleconstant", BOOL, "Use one single scalar?")
        self.createParameter("evapscaleconstant", BOOL, "Use a single evapo scalar?")
        self.rainscaleconstant = 0
        self.evapscaleconstant = 0


        self.defaultscalars = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]

        self.raindata = []  # Globals to contain the data time series
        self.evapdata = []
        self.solardata = []

        #MUSIC TAB
        self.createParameter("musicversion", STRING, "Active MUSIC Version for file writing")
        self.createParameter("musicclimatefile", STRING, "Path to the .mlb climate file")
        self.createParameter("musicseparatebasin", BOOL, "Write separate .msf files per basin?")
        self.musicversion = 'Version 6.1'       #2016-09-30: Version 6.1, Version 6.2
        self.musicclimatefile = ""
        self.musicseparatebasin = 1

        self.createParameter("music_concept", STRING, "The method to be used for creating the MUSIC file")
        self.music_concept = "linear"   #linear, nonlinear, both

        self.createParameter("include_pervious", BOOL, "Include pervious areas in simulation?")
        self.createParameter("musicRR_soil", DOUBLE, "MUSIC soil storage capacity")
        self.createParameter("musicRR_field", DOUBLE, "MUSIC field storage capacity")
        self.createParameter("musicRR_bfr", DOUBLE, "MUSIC daily baseflow rate")
        self.createParameter("musicRR_rcr", DOUBLE, "Daily recharge rate")
        self.createParameter("musicRR_dsr", DOUBLE, "Daily deep seepage rate")
        self.include_pervious = 1
        self.musicRR_soil = 120.0
        self.musicRR_field = 80
        self.musicRR_bfr = 5.00
        self.musicRR_rcr = 25.00
        self.musicRR_dsr = 0.00

        self.createParameter("include_route", BOOL, "Include flow routing?")
        self.createParameter("musicRR_muskk_auto", BOOL, "Auto-determine Muskingum K based on blocks?")
        self.createParameter("musicRR_muskk", DOUBLE, "Muskingum Cunge K value")
        self.createParameter("musicRR_musktheta", DOUBLE, "Muskingum Cunge theta value")
        self.include_route = 1
        self.musicRR_muskk_auto = 0
        self.musicRR_muskk = 30.0
        self.musicRR_musktheta = 0.1

        self.createParameter("musicautorun", BOOL, "Auto-run MUSIC simulation?")
        self.createParameter("musicpath", STRING, "Path to the MUSIC exe file")
        self.createParameter("musicTTE", BOOL, "Export Treatment Train Effectiveness?")
        self.createParameter("musicFlux", BOOL, "Export Flux data from MUSIC simulation?")
        self.musicautorun = 0
        self.musicpath = ''
        self.musicTTE = 0
        self.musicFlux = 0

        self.createParameter("musicfilepathname", STRING, "")
        self.createParameter("musicfilename", STRING, "")
        self.createParameter("currentyear", DOUBLE, "")
        self.createParameter("masterplanmodel", BOOL, "")
        #self.createParameter("include_secondary_links", BOOL, "")
        self.musicfilepathname = "D:\\"
        self.musicfilename = "ubeatsMUSIC"
        self.currentyear = 9999
        self.masterplanmodel = 1
        #self.include_secondary_links = 0


        #ECONOMICS TAB
        self.createParameter("assessyears", DOUBLE, "")
        self.createParameter("assessonlycapital", BOOL, "")
        self.createParameter("rateconstant", BOOL, "")
        self.createParameter("drate", DOUBLE, "")
        self.createParameter("irate", DOUBLE, "")
        self.createParameter("ratefile", STRING, "")
        self.createParameter("currency", STRING, "")
        self.createParameter("currencyconv", DOUBLE, "")
        self.createParameter("convagainst", STRING, "")
        self.createParameter("allocatecost", BOOL, "")
        self.assessyears = 50.0
        self.assessonlycapital = False
        self.rateconstant = True
        self.drate = 4.00
        self.irate = 1.55
        self.ratefile = "< no file selected >"
        self.currency = "AUD"
        self.currencyconv = 1.00
        self.convagainst = "AUD"
        self.allocatecost = False

        self.createParameter("LCCtemplate", STRING, "")
        self.createParameter("useDecom", BOOL, "")
        self.createParameter("includeMaintain", BOOL, "")
        self.createParameter("ignoreLifeSpan", BOOL, "")
        self.LCCtemplate = "MELBW"  #MELBW, MUSIC, CUSTO
        self.useDecom = True
        self.includeMaintain = True
        self.ignoreLifeSpan = False

        self.createParameter("otherecon", BOOL, "")
        self.createParameter("econ_bulkwater", BOOL, "")
        self.createParameter("econ_bulkwater_price", DOUBLE, "")
        self.createParameter("econ_wwtp", BOOL, "")
        self.createParameter("econ_wwtp_price", DOUBLE, "")
        self.createParameter("econ_nutrients", BOOL, "")
        self.createParameter("econ_nutrients_price", DOUBLE, "")
        self.createParameter("econ_landplan", BOOL, "")
        self.createParameter("econ_landplan_price", DOUBLE, "")
        self.createParameter("econ_energy", BOOL, "")
        self.createParameter("econ_energy_price", DOUBLE, "")
        self.otherecon = False
        self.econ_bulkwater = False
        self.econ_bulkwater_price = 0.00
        self.econ_wwtp = False
        self.econ_wwtp_price = 0.00
        self.econ_nutrients = False
        self.econ_nutrients_price = 0.00
        self.econ_landplan = False
        self.econ_landplan_price = 0.00
        self.econ_energy = False
        self.econ_energy_price = 0.00

        #MICROCLIMATE TAB
        self.createParameter("assesslevel", STRING, "")
        self.createParameter("assessunits", STRING, "")
        self.createParameter("interptype", STRING, "")
        self.createParameter("basecase", BOOL, "")
        self.createParameter("diffmap", BOOL, "")
        self.assesslevel = "P"      #P = patch, B = block
        self.assessunits = "LST"      #LST = land surface temp, ETC = equivalent thermal comfort index
        self.interptype = "IDW"     #IDW = inverse distance weighted, KRI = kriging
        self.basecase = 0
        self.diffmap = 0

        #Interpolation parameters

        #Land Surface Temp Parameters
        self.createParameter("as_shape", STRING, "")
        self.createParameter("co_shape", STRING, "")
        self.createParameter("dg_shape", STRING, "")
        self.createParameter("ig_shape", STRING, "")
        self.createParameter("rf_shape", STRING, "")
        self.createParameter("tr_shape", STRING, "")
        self.createParameter("wa_shape", STRING, "")
        self.createParameter("as_min", DOUBLE, "")
        self.createParameter("co_min", DOUBLE, "")
        self.createParameter("dg_min", DOUBLE, "")
        self.createParameter("ig_min", DOUBLE, "")
        self.createParameter("rf_min", DOUBLE, "")
        self.createParameter("tr_min", DOUBLE, "")
        self.createParameter("wa_min", DOUBLE, "")
        self.createParameter("as_max", DOUBLE, "")
        self.createParameter("co_max", DOUBLE, "")
        self.createParameter("dg_max", DOUBLE, "")
        self.createParameter("ig_max", DOUBLE, "")
        self.createParameter("rf_max", DOUBLE, "")
        self.createParameter("tr_max", DOUBLE, "")
        self.createParameter("wa_max", DOUBLE, "")
        self.as_shape = "C"     #B = bell-curve, C = constant, U = uniform
        self.co_shape = "C"     #B = bell-curve, C = constant, U = uniform
        self.dg_shape = "C"     #B = bell-curve, C = constant, U = uniform
        self.ig_shape = "C"     #B = bell-curve, C = constant, U = uniform
        self.rf_shape = "C"     #B = bell-curve, C = constant, U = uniform
        self.tr_shape = "C"     #B = bell-curve, C = constant, U = uniform
        self.wa_shape = "C"     #B = bell-curve, C = constant, U = uniform
        self.as_min = 55.8
        self.co_min = 47.9
        self.dg_min = 55.4
        self.ig_min = 35.9
        self.rf_min = 58.0
        self.tr_min = 37.8
        self.wa_min = 28.0
        self.as_max = 45.0
        self.co_max = 45.0
        self.dg_max = 45.0
        self.ig_max = 45.0
        self.rf_max = 45.0
        self.tr_max = 45.0
        self.wa_max = 45.0

        #WATER SUPPLY
        #Pattern names include: SDD - standard daily diurnal, CDP - constant daily pattern,
        #                       AHC - after-hours constant, OHT - office hours trapezoid
        #                       UDP - user-defined pattern
        self.createParameter("kitchenpat", STRING, "")
        self.createParameter("showerpat", STRING, "")
        self.createParameter("toiletpat", STRING, "")
        self.createParameter("laundrypat", STRING, "")
        self.createParameter("irrigationpat", STRING, "")
        self.createParameter("compat", STRING, "")
        self.createParameter("indpat", STRING, "")
        self.createParameter("publicirripat", STRING, "")
        self.kitchenpat = "SDD"
        self.showerpat = "SDD"
        self.toiletpat = "SDD"
        self.laundrypat = "SDD"
        self.irrigationpat = "SDD"
        self.compat = "UDP"
        self.indpat = "SDD"
        self.publicirripat = "SDD"

        self.sdd = [0.3,0.3,0.3,0.3,0.5,1.0,1.5,1.5,1.3,1.0,1.0,1.5,1.5,1.2,1.0,1.0,1.0,1.3,1.3,0.8,0.8,0.5,0.5,0.5]
        self.cdp = [1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0]
        self.oht = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.5,1.0,1.5,2.0,2.5,3.0,3.0,3.0,2.5,2.0,1.5,1.0,0.5,0.0,0.0,0.0,0.0]
        self.ahc = [2.0,2.0,2.0,2.0,2.0,2.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,2.0,2.0,2.0,2.0,2.0,2.0]

        #Custom pattern variables if needed
        self.createParameter("cp_kitchen", LISTDOUBLE, "")
        self.cp_kitchen = [1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0]
        self.createParameter("cp_shower",  LISTDOUBLE, "")
        self.cp_shower = [1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0]
        self.createParameter("cp_toilet",  LISTDOUBLE, "")
        self.cp_toilet = [1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0]
        self.createParameter("cp_laundry",  LISTDOUBLE, "")
        self.cp_laundry = [1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0]
        self.createParameter("cp_irrigation",  LISTDOUBLE, "")
        self.cp_irrigation = [1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0]
        self.createParameter("cp_com",  LISTDOUBLE, "")
        self.cp_com = [1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0]
        self.createParameter("cp_ind",  LISTDOUBLE, "")
        self.cp_ind = [1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0]
        self.createParameter("cp_publicirri",  LISTDOUBLE, "")
        self.cp_publicirri = [1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0]

        #Long Term Water Supply Dynamics
        self.createParameter("run_fullTSSim", BOOL, "")
        self.run_fullTSSim = 0

        self.createParameter("scalefile", STRING, "Filepath to the climate data to be used for scaling")
        self.createParameter("scaleyears", DOUBLE, "Number of years of continuous scaling data to use")
        self.createParameter("globalaverage", DOUBLE, "Global average to base the scaling upon")
        self.createParameter("globalavgauto", BOOL, "Boolean to determine whether avg. calculated from data")
        self.scalefile = "<none>"
        self.scaleyears = 2
        self.globalaverage = 0
        self.globalavgauto = 1

        self.createParameter("weekend_nres", BOOL, "Reduce weekend non-residential demand?")
        self.createParameter("weekend_nres_factor", DOUBLE, "Reduction factor for weekend non-res demand")
        self.createParameter("weekend_res", BOOL, "Increase weekend residential demand?")
        self.createParameter("weekend_res_factor", DOUBLE, "Multiplication factor to increase weekend demand")
        self.weekend_nres = 0
        self.weekend_nres_factor = 1.0
        self.weekend_res = 0
        self.weekend_res_factor = 1.0

        self.createParameter("rain_no_irrigate", BOOL, "Do not irrigate when it is raining?")
        self.createParameter("irrigate_lead", DOUBLE, "Lead time to begin irrigation again after rain")
        self.rain_no_irrigate = 0
        self.irrigate_lead = 24.0       #[hours]

        self.createParameter("init_store_levels", DOUBLE, "Initial storage % in all storages")
        self.createParameter("priority_pubirri", DOUBLE, "Priority for public irrigation supply")
        self.createParameter("priority_privirri", DOUBLE, "Priority for private outdoor supply")
        self.createParameter("priority_privin_nc", DOUBLE, "Priority for private indoor no contact supply")
        self.createParameter("priority_privin_c", DOUBLE, "Priority for private indoor contact supply")
        self.createParameter("regional_supply_rule", STRING, "Regional water supply rule")
        self.init_store_levels = 0.0
        self.priority_pubirri = 0
        self.priority_privirri = 2
        self.priority_privin_nc = 3
        self.priority_privin_c = 4
        self.regional_supply_rule = "CLOSE"   #of "EQUAL" for all surroundings evenly

        #EPANET integration variables
        self.createParameter("epanetintmethod", STRING, "")
        self.createParameter("epanet_scanradius", DOUBLE, "")
        self.createParameter("epanet_excludezeros", BOOL, "")
        self.createParameter("epanet_exportshp", BOOL, "")
        self.createParameter("epanet_inpfname", STRING, "")
        self.createParameter("runBaseInp", BOOL, "")
        self.createParameter("epanet_simtype", STRING, "")
        self.createParameter("epanet_offset", BOOL, "")
        self.createParameter("epanet_useProjectOffset", BOOL, "")
        self.createParameter("epanet_offsetX", DOUBLE, "")
        self.createParameter("epanet_offsetY", DOUBLE, "")

        #VD = voronoi diagram, DT = delaunay triangulation, RS = radial scan, NN = nearest neighbour
        self.epanetintmethod = "VD"
        self.epanet_scanradius = 0.5  #only for radial scan method
        self.epanet_excludezeros = 1    #exclude all nodes with zero demand?
        self.epanet_exportshp = 1   #export a visual illustration of the spatial integration between blocks and network
        self.epanet_inpfname = ""   #input filename
        self.runBaseInp = 0         #run the base simulation? will rebuild the .inp file
        #STS = static sim, 24H = 24-hour, EPS = extended period sim (72hrs), LTS = long-term sim
        self.epanet_simtype = "STS"
        self.epanet_offset = 0
        self.epanet_useProjectOffset = 0
        self.epanet_offsetX = 0
        self.epanet_offsetY = 0

        self.createParameter("epanetsim_hl", STRING, "")
        self.createParameter("epanetsim_hlc", DOUBLE, "")
        self.createParameter("epanetsim_hlc_reassign", BOOL, "")
        self.createParameter("epanetsim_hts", STRING, "")
        self.createParameter("epanetsim_qts", STRING, "")
        self.createParameter("epanetsim_visc", DOUBLE, "")
        self.createParameter("epanetsim_specg", DOUBLE, "")
        self.createParameter("epanetsim_emit", DOUBLE, "")
        self.createParameter("epanetsim_trials", DOUBLE, "")
        self.createParameter("epanetsim_accuracy", DOUBLE, "")
        self.createParameter("epanetsim_demmult", DOUBLE, "")
        self.epanetsim_hl = "D-W"   #D-W, H-W, C-M
        self.epanetsim_hlc = 0.01
        self.epanetsim_hlc_reassign = 1
        self.epanetsim_hts = "1:00"
        self.epanetsim_qts = "0:05"
        self.epanetsim_visc = 1.0
        self.epanetsim_specg = 1.0
        self.epanetsim_emit = 0.5
        self.epanetsim_trials = 40
        self.epanetsim_accuracy = 0.001
        self.epanetsim_demmult = 1.0

        #INTEGRATED WATER CYCLE MODEL


        #ADVANCED PARAMETERS ---------------------------------------------------------
        self.totalbasins = 0
        self.blocks_num = 0
        self.blocks_size = 0
        self.strats = 0

        # ----------------------------------------------------------------------------


    def run(self):
        self.notify("Now Running Performance Assessment")

        map_attr = self.activesim.getAssetWithName("MapAttributes")  # fetches global map attributes
        self.blocks_num = map_attr.getAttribute("NumBlocks")
        self.blocks_size = map_attr.getAttribute("BlockSize")
        self.totalbasins = map_attr.getAttribute("TotalBasins")
        self.strats = map_attr.getAttribute("OutputStrats")

        #If necessary: Load climate data and scale it according to factors
        if self.perf_EPANET or self.perf_CD3:       #Add perf_MUSIC next time
            self.raindata = ubseries.loadClimate(self.rainfile, self.analysis_dt, self.rainyears)
            self.evapdata = ubseries.loadClimate(self.evapfile, 1440, self.rainyears)   #Extract PET at daily
            #self.solardata = ubseries.loadClimate(self.solarfile, 1440, self.rainyears)    #Solar Radiation data

            if self.rainscale:
                if self.rainscaleconstant:
                    scalars = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
                    for i in range(len(scalars)):
                        scalars[i] = self.rainscalars[0]
                    self.raindata = ubseries.scaleClimateSeries(self.raindata, scalars)
                else:
                    self.raindata = ubseries.scaleClimateSeries(self.raindata, self.rainscalars)

            if self.evapscale:
                if self.evapscaleconstant:
                    scalars = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
                    for i in range(len(scalars)):
                        scalars[i] = self.evapscalars[0]
                    print "Scalars", scalars
                    self.evapdata = ubseries.scaleClimateSeries(self.evapdata, scalars)
                else:
                    self.evapdata = ubseries.scaleClimateSeries(self.evapdata, self.evapscalars)

            #SCALING FOR SOLAR RADIATION DATA?
        if self.perf_MUSIC:
            self.notify("Exporting MUSIC Simulation...")
            self.writeMUSIC()

        if self.perf_Economics:
            self.runEconomicAnalysis()

        if self.perf_Microclimate:
            self.runMicroclimateAnalysis()

        if self.perf_EPANET:
            self.runWaterSupply()

        if self.perf_CD3:
            self.runIWCM()

        return True


    def changeCustomPattern(self, enduse, patternvector):
        exec("self.cp_"+str(enduse)+" = "+str(patternvector))

    def getCustomPattern(self, enduse):
        return eval("self.cp_"+str(enduse))

    def writeMUSIC(self):
        """ Executes the export option to a MUSIC simulation file, the program uses the options
        to create a number of MUSIC files to the export directory with the given block attributes
        system options and parameters.
        """
        if self.masterplanmodel:    #differentiate between planning and implementation models
            filesuffix = "PC"
            strats = self.strats
        else:
            filesuffix = "IC"
            strats = 1

        self.notify("Total Basins: "+str(self.totalbasins))
        self.notify("Total Strategies: "+str(strats))

        #Define MUSIC Version
        if self.musicversion == "Version 6":
            pymusic.setMUSICversion(6)
        elif self.musicversion == "Version 5":
            pymusic.setMUSICversion(5)

        #Begin Writing MUSIC Files
        for s in range(int(strats)):
            currentStratID = s+1
            if self.music_concept == "nonlinear":
                self.writeMUSICnonlinear(currentStratID, filesuffix)
            elif self.music_concept == "linear":
                self.writeMUSIClinear(currentStratID, filesuffix)
            else:
                self.writeMUSICnonlinear(currentStratID, filesuffix)
                self.writeMUSIClinear(currentStratID, filesuffix)
        return True

    def writeMUSIClinear(self, currentStratID, filesuffix):
        """Writes the linear version of the MUSIC simulation file. This is where all systems drain separately and
        runoff downstream is collected cumulatively across all areas. Junctions are used primarily as a collection
        stream.

        :return: A MUSIC .msf file annotated with LI to denote that this is a linear model
        """
        concept = "LI"
        if self.musicseparatebasin:     #Determines whether to write separate files or not
            musicbasins = self.totalbasins
        else:
            musicbasins = 1

        if self.include_route:
            if self.musicRR_muskk_auto:
                # Work out Muskingum k approximation based on block size and 1m/s flow
                musk_K = max(int(float(self.blocks_size) / 60.0), 3)
            else:
                musk_K = self.musicRR_muskk
            routeparams = ["Routed", musk_K, self.musicRR_musktheta]
        else:
            routeparams = ["Not Routed", 30, 0.25]  # Defaults

        for b in range(int(musicbasins)):
            basinID = b+1
            if self.musicseparatebasin:
                systemlist = self.getWSUDSystemsForStratID(currentStratID, b + 1)
                basinblockIDs = self.getBlocksIDsForBasinID(b+1)
                ufile = ubmusicwrite.createMUSICmsf(self.musicfilepathname,
                                                    self.musicfilename + "-ID" + str(currentStratID) + concept + "-" + str(
                                                        int(b + 1)) + "-" + str(self.currentyear) + filesuffix)
            else:
                systemlist = self.getWSUDSystemsForStratID(currentStratID, 9999)
                basinblockIDs = self.getBlocksIDsForBasinID(9999)
                ufile = ubmusicwrite.createMUSICmsf(self.musicfilepathname,
                                                    self.musicfilename + "-ID" + str(currentStratID) + concept + "-" + str(
                                                        self.currentyear) + filesuffix)

            ubmusicwrite.writeMUSICheader(ufile, self.musicclimatefile, self.musicversion)

            scalar = 10
            ncount = 1
            musicnodedb = {}    #store the database of MUSIC nodes across Blocks
            blockcatchmentTracker = {}

            #LOOP 1 - Write all in-block systems with catchments and links
            for i in basinblockIDs:
                currentID = i
                currentAttList = self.activesim.getAssetWithName("BlockID" + str(currentID))
                musicnodedb["BlockID" + str(currentID)] = {}
                blockcatchmentTracker["BlockID" + str(currentID)] = currentAttList.getAttribute("Blk_EIA")
                blocksystems = self.getBlockSystems(currentID, systemlist)

                blockX = currentAttList.getAttribute("CentreX")
                blockY = currentAttList.getAttribute("CentreY")

                # WRITE NODES
                catchment_parameter_list = [1, 120, 30, 80, 200, 1, 10, 25, 5, 0]
                total_catch_EIF = 1

                scalekeys = ["L_RES", "L_HDR", "L_COM", "L_LI", "L_HI", "L_ORC", "S", "N"]
                catchxoffset = 0.25
                yoffsets = [4.0/5.0, 4.0/5.0, 4.0/5.0, 4.0/5.0, 4.0/5.0, 4.0/5.0, 3.0/5.0, 2.0/5.0]

                for s in range(len(scalekeys)):
                    if len(blocksystems[scalekeys[s]]) == 0:
                        continue
                    curwsud = blocksystems[scalekeys[s]][0]
                    nodelink = []
                    catchImp = curwsud.getAttribute("SvWQ_ImpT")*curwsud.getAttribute("GoalQty")
                    availImp = blockcatchmentTracker["BlockID" + str(currentID)]
                    treatImp = min(catchImp, availImp)
                    blockcatchmentTracker["BlockID"+str(currentID)] -= treatImp  # Subtract the treated impervious area from block imp
                    if treatImp == 0:
                        print "WARNING: Planned too many systems... re-check settings"
                        continue

                    #Write the catchment node
                    ubmusicwrite.writeMUSICcatchmentnode(ufile, currentID, scalekeys[s], ncount,
                            (blockX - self.blocks_size * catchxoffset) * scalar,
                            (blockY - self.blocks_size/ 2.0 + yoffsets[s]*self.blocks_size) * scalar,
                            treatImp/10000.0, total_catch_EIF, catchment_parameter_list, self.musicversion)

                    musicnodedb["BlockID"+str(currentID)]["C_"+scalekeys[s]] = ncount
                    nodelink.append(ncount)
                    ncount += 1

                    #Write the treatment node
                    systype = curwsud.getAttribute("Type")
                    sysKexfil = curwsud.getAttribute("Exfil")

                    parameter_list = eval("self.prepareParameters" + str(systype) + "(curwsud, sysKexfil)")
                    eval("ubmusicwrite.writeMUSICnode"+str(systype)+ "(ufile, currentID, scalekeys[s], ncount, blockX * scalar," +
                                  "(blockY - self.blocks_size/2.0 + yoffsets[s]*self.blocks_size)*scalar, parameter_list, self.musicversion)")
                    musicnodedb["BlockID"+str(currentID)]["S_"+scalekeys[s]] = ncount
                    nodelink.append(ncount)
                    ncount += 1

                    #Write the link to connect these two nodes
                    ubmusicwrite.writeMUSIClink(ufile, nodelink[0], nodelink[1], routeparams, self.musicversion)
                    technodeID = nodelink[1]
                    nodelink = [technodeID]

                    # If there is a Storage System Node that isn't integrated, write the node
                    if curwsud.getAttribute("StoreType") == "NA" or curwsud.getAttribute("IntegStore") == 1:
                        continue
                    storeType = curwsud.getAttribute("StoreType")
                    parameter_list = eval("self.prepareParameters" + str(storeType) + "Store(curwsud, sysKexfil)")
                    eval("ubmusicwrite.writeMUSICnode"+str(storeType)+ "(ufile, currentID, scalekeys[s], ncount, (blockX + (self.blocks_size/8.0)) * scalar,"+
                         "(blockY - self.blocks_size/2.0 + yoffsets[s]*self.blocks_size)*scalar, parameter_list, self.musicversion)")
                    musicnodedb["BlockID"+str(currentID)]["ST_"+scalekeys[s]] = ncount
                    nodelink.append(ncount)
                    ncount += 1

                    ubmusicwrite.writeMUSIClink(ufile, nodelink[0], nodelink[1], routeparams, self.musicversion)

            # LOOP 2 - Write all basin-scale systems
            for i in basinblockIDs:
                currentID = i
                currentAttList = self.activesim.getAssetWithName("BlockID" + str(currentID))
                blocksystems = self.getBlockSystems(currentID, systemlist)
                blockX = currentAttList.getAttribute("CentreX")
                blockY = currentAttList.getAttribute("CentreY")

                if len(blocksystems["B"]) == 0:
                    continue

                curwsud = blocksystems["B"][0]
                nodelink = []
                catchImp = curwsud.getAttribute("SvWQ_ImpT") + curwsud.getAttribute("GoalQty")

                # WRITE NODES
                catchment_parameter_list = [1, 120, 30, 80, 200, 1, 10, 25, 5, 0]
                total_catch_EIF = 1
                catchxoffset = 0.25

                # Work out how much impervious area to subtract from the other blocks
                upIDs = []
                upAreas = []
                upPs = []

                # Get Upstream Blocks and only keep those with actively untreated impervious area
                upstreamIDs = currentAttList.getAttribute("UpstrIDs").split(',')
                upstreamIDs.remove('')
                for j in range(len(upstreamIDs)):
                    upstreamIDs[j] = int(upstreamIDs[j])
                    if blockcatchmentTracker["BlockID" + str(upstreamIDs[j])] <= 0:  # If there is no area left to treat, remove
                        continue
                    upIDs.append(upstreamIDs[j])
                    upAreas.append(blockcatchmentTracker["BlockID" + str(upstreamIDs[j])])
                if catchImp > sum(upAreas):     #If the treated catchment impervious area is greater than the sum of untreated areas
                    treatedImp = sum(upAreas)
                    for j in range(len(upIDs)):
                        blockcatchmentTracker["BlockID" + str(upIDs[j])] = 0 # Set all areas to zero
                else:
                    for j in range(len(upIDs)):     #Calculate the proportions of each block relevant to the total area
                        upPs.append(upAreas[j] / sum(upAreas))   #and then check what the leftover area is
                        Atreat = min(upPs[j] * catchImp, upAreas[j])
                        Anew = max(upAreas[j] - Atreat, 0)
                        blockcatchmentTracker["BlockID" + str(upIDs[j])] = Anew

                        #Write the catchment node
                ubmusicwrite.writeMUSICcatchmentnode(ufile, currentID, "B", ncount,
                                                     (blockX + self.blocks_size * catchxoffset) * scalar,
                                                     (blockY - self.blocks_size / 2.0 + 4.0/5.0 * self.blocks_size) * scalar,
                                                     catchImp/10000.0, total_catch_EIF, catchment_parameter_list, self.musicversion)

                musicnodedb["BlockID" + str(currentID)]["C_B"] = ncount
                nodelink.append(ncount)
                ncount += 1

                # Write the treatment node
                systype = curwsud.getAttribute("Type")
                sysKexfil = curwsud.getAttribute("Exfil")
                parameter_list = eval(
                    "self.prepareParameters" + str(systype) + "(curwsud, sysKexfil)")
                eval("ubmusicwrite.writeMUSICnode" + str(
                    systype) + "(ufile, currentID, \"B\", ncount, (blockX + self.blocks_size * catchxoffset) * scalar," +
                     "(blockY - self.blocks_size/2.0 + 3.0/5.0*self.blocks_size)*scalar, parameter_list, self.musicversion)")
                musicnodedb["BlockID" + str(currentID)]["S_B"] = ncount
                nodelink.append(ncount)
                ncount += 1

                # Write the link to connect these two nodes
                ubmusicwrite.writeMUSIClink(ufile, nodelink[0], nodelink[1], routeparams, self.musicversion)
                technodeID = nodelink[1]
                nodelink = [technodeID]

                # If there is a Storage System Node that isn't integrated, write the node
                if curwsud.getAttribute("StoreType") == "NA" or curwsud.getAttribute("IntegStore") == 1:
                    continue
                storeType = curwsud.getAttribute("StoreType")
                parameter_list = eval("self.prepareParameters" + str(storeType) + "Store(curwsud, sysKexfil)")
                eval("ubmusicwrite.writeMUSICnode" + str(
                    storeType) + "(ufile, currentID, \"B\", ncount, (blockX + self.blocks_size * catchxoffset) * scalar," +
                     "(blockY - self.blocks_size/2.0 + 2.0/5.0*self.blocks_size)*scalar, parameter_list, self.musicversion)")
                musicnodedb["BlockID" + str(currentID)]["ST_B"] = ncount
                nodelink.append(ncount)
                ncount += 1

                ubmusicwrite.writeMUSIClink(ufile, nodelink[0], nodelink[1], routeparams, self.musicversion)

            # LOOP 3 - Write all remaining area catchments
            for i in basinblockIDs:
                currentID = i
                currentAttList = self.activesim.getAssetWithName("BlockID"+str(currentID))
                blockX = currentAttList.getAttribute("CentreX")
                blockY = currentAttList.getAttribute("CentreY")

                if blockcatchmentTracker["BlockID"+str(currentID)] <= 0:   #if the remaining impervious area for that
                    print "BlockID", currentID, "has no impervious area left..."
                    continue        #block is equal to zero, then skip it, no remaining catchment node needed

                catchImp = blockcatchmentTracker["BlockID"+str(currentID)]
                catchment_parameter_list = [1, 120, 30, 80, 200, 1, 10, 25, 5, 0]
                total_catch_EIF = 1
                catchxoffset = 0.25

                # Write the catchment node
                ubmusicwrite.writeMUSICcatchmentnode(ufile, currentID, "REST", ncount,
                                                     (blockX - self.blocks_size * catchxoffset) * scalar,
                                                     (blockY - self.blocks_size / 2.0 + 1.0/5.0 * self.blocks_size) * scalar,
                                                     catchImp/10000.0, total_catch_EIF, catchment_parameter_list, self.musicversion)

                musicnodedb["BlockID" + str(currentID)]["C_REST"] = ncount
                ncount += 1

            #LOOP 3.5 - Write all pervious catchment area if this is wanted
            if self.include_pervious:
                for i in basinblockIDs:
                    currentID = i
                    currentAttList = self.activesim.getAssetWithName("BlockID" + str(currentID))
                    blockX = currentAttList.getAttribute("CentreX")
                    blockY = currentAttList.getAttribute("CentreY")
                    catchment_parameter_list = [1, self.musicRR_soil, 0, self.musicRR_field, 200, 1, 10,
                                                self.musicRR_rcr, self.musicRR_bfr, self.musicRR_dsr]
                    catchxoffset = 0.25

                    pervArea = max((self.blocks_size * self.blocks_size)*currentAttList.getAttribute("Active") - currentAttList.getAttribute("Blk_EIA"),0)
                    if pervArea == 0:
                        continue

                    ubmusicwrite.writeMUSICcatchmentnode(ufile, currentID, "PERV", ncount,
                                                         (blockX - self.blocks_size * catchxoffset)*scalar,
                                                         (blockY - self.blocks_size / 2.0 + 0.8/5.0 * self.blocks_size)*scalar,
                                                         pervArea/10000.0, 0.0, catchment_parameter_list, self.musicversion)
                    musicnodedb["BlockID"+str(currentID)]["C_PERV"] = ncount
                    ncount += 1

            # LOOP 4 - Write Junction nodes
            for i in basinblockIDs:
                currentID = i
                currentAttList = self.activesim.getAssetWithName("BlockID" + str(currentID))
                blockX = currentAttList.getAttribute("CentreX")
                blockY = currentAttList.getAttribute("CentreY")

                if len(musicnodedb["BlockID"+str(currentID)]) == 0: #If there are no nodes in this block, skip the junction
                    musicnodedb["BlockID" + str(currentID)]["JUNCTION"] = -9999  # Do not create a junction
                    continue

                if int(currentAttList.getAttribute("Outlet")) == 1:
                    self.notify("GOT AN OUTLET at BlockID" + str(currentID))
                    basinID = int(currentAttList.getAttribute("BasinID"))
                    jname = "OUT_Bas" + str(basinID) + "-BlkID" + str(currentID)
                else:
                    jname = "BlockID" + str(currentID) + "J"

                ubmusicwrite.writeMUSICjunction(ufile, jname, ncount, (blockX + self.blocks_size * 0.25) * scalar,
                                                (blockY - self.blocks_size / 2.0 + self.blocks_size * 1.0 / 5.0) * scalar, self.musicversion)

                musicnodedb["BlockID" + str(currentID)]["JUNCTION"] = ncount
                ncount += 1

            # FINAL PASS - connect all nodes
            internal_keys = ["S_L_RES", "S_L_HDR", "S_L_COM", "S_L_ORC", "S_L_LI", "S_L_HI", "S_S", "S_N", "S_B", "C_REST", "C_PERV"]
            harvest_keys = ["ST_L_RES", "ST_L_HDR", "ST_L_COM", "ST_L_ORC", "ST_L_LI", "ST_L_HI", "ST_S", "ST_N", "ST_B", "ST_REST", "ST_PERV"]
            for i in basinblockIDs:
                currentID = i
                currentAttList = self.activesim.getAssetWithName("BlockID" + str(currentID))
                if musicnodedb["BlockID" + str(currentID)]["JUNCTION"] == -9999:
                    print "Junction Node with -9999 ID found"
                    print musicnodedb["BlockID" + str(currentID)]
                    continue

                #Internal Connections - all WSUD systems to the junction node and REST node with junction
                for j in range(len(internal_keys)):
                    ckey = internal_keys[j]
                    hkey = harvest_keys[j]
                    # Write the link
                    if musicnodedb["BlockID"+str(currentID)].has_key(hkey): #If the block has a storage system
                        ubmusicwrite.writeMUSIClink(ufile, musicnodedb["BlockID"+str(currentID)][hkey],
                                                    musicnodedb["BlockID"+str(currentID)]["JUNCTION"], routeparams, self.musicversion)
                    elif musicnodedb["BlockID"+str(currentID)].has_key(ckey):
                        ubmusicwrite.writeMUSIClink(ufile, musicnodedb["BlockID" + str(currentID)][ckey],
                                                    musicnodedb["BlockID" + str(currentID)]["JUNCTION"], routeparams, self.musicversion)

                #External Connection - Junction Node to Junction Node
                if int(currentAttList.getAttribute("Outlet")) == 1:
                    continue

                junction_found = 0
                downAtt = currentAttList
                while junction_found == 0:
                    downID = int(downAtt.getAttribute("downID"))
                    if downID == -1 or downID == 0:
                        downID = int(downAtt.getAttribute("drainID"))
                    if downID == -1 or downID == 0:
                        print "SHOULD NOT HAPPEN!"
                        junction_found = 1
                    else:
                        if musicnodedb["BlockID"+str(downID)]["JUNCTION"] != -9999:
                            ubmusicwrite.writeMUSIClink(ufile, musicnodedb["BlockID"+str(currentID)]["JUNCTION"],
                                                musicnodedb["BlockID"+str(downID)]["JUNCTION"], routeparams, self.musicversion)
                            junction_found = 1
                        else:
                            #Assign the downstream block as the next block to check (skip that junction but go down the chain)
                            downAtt = self.activesim.getAssetWithName("BlockID"+str(downID))

            #Write the footer for the file.
            ubmusicwrite.writeMUSICfooter(ufile)

    def writeMUSICnonlinear(self, currentStratID, filesuffix):
        """Writes the non-linear version of the MUSIC simulation file. This is where all systems drain into successive
        downstream systems. The relationship is non-linear and non-conservative meaining that all treatment systems
        will appear as oversized in the model because the overall treatment efficiency will be greater than what is
        predicted

        :return: A MUSIC .msf file annotated with NL to denote that this is a non-linear model
        """
        concept = "NL"
        if self.musicseparatebasin:  # Determine if to write separate files or one single file
            musicbasins = self.totalbasins
        else:
            musicbasins = 1

        for b in range(int(musicbasins)):
            if self.musicseparatebasin:
                systemlist = self.getWSUDSystemsForStratID(currentStratID, b + 1)
                basinblockIDs = self.getBlocksIDsForBasinID(b + 1)
                ufile = ubmusicwrite.createMUSICmsf(self.musicfilepathname,
                                                    self.musicfilename + "-ID" + str(currentStratID) + concept + "-" + str(
                                                        int(b + 1)) + "-" + str(self.currentyear) + filesuffix)
            else:
                systemlist = self.getWSUDSystemsForStratID(currentStratID, 9999)
                basinblockIDs = self.getBlocksIDsForBasinID(9999)
                ufile = ubmusicwrite.createMUSICmsf(self.musicfilepathname,
                                                    self.musicfilename + "-ID" + str(currentStratID) + concept + "-" + str(
                                                        self.currentyear) + filesuffix)

            ubmusicwrite.writeMUSICheader(ufile, self.musicclimatefile, self.musicversion)

            scalar = 10
            ncount = 1
            musicnodedb = {}  # contains the database of nodes for each Block

            for i in basinblockIDs:
                currentID = i
                currentAttList = self.activesim.getAssetWithName("BlockID" + str(currentID))
                musicnodedb["BlockID" + str(currentID)] = {}
                blocksystems = self.getBlockSystems(currentID, systemlist)
                # self.notify(str(blocksystems))

                blockX = currentAttList.getAttribute("CentreX")
                blockY = currentAttList.getAttribute("CentreY")

                # (1) WRITE CATCHMENT NODES - maximum possibility of 7 Nodes (Lot x 6, non-lot x 1)
                #       Lot: RES, HDR, COM, LI, HI, ORC
                #       Street/Neigh: x 1
                if self.include_pervious:
                    catchment_parameter_list = [1, self.musicRR_soil, self.musicRR_field, 80, 200, 1, 10,
                                                self.musicRR_rcr, self.musicRR_bfr, self.musicRR_dsr]
                    total_catch_area = (self.blocks_size * self.blocks_size) * currentAttList.getAttribute(
                        "Active") / 10000  # [ha]
                    total_catch_imparea = currentAttList.getAttribute("Blk_EIA") / 10000
                    total_catch_EIF = (total_catch_imparea / total_catch_area)
                else:
                    catchment_parameter_list = [1, 120, 30, 80, 200, 1, 10, 25, 5, 0]
                    total_catch_area = currentAttList.getAttribute("Blk_EIA") / 10000  # [ha]
                    total_catch_imparea = total_catch_area
                    total_catch_EIF = 1  # 100% impervious

                catchnodecount = self.determineBlockCatchmentNodeCount(blocksystems)
                lotcount = catchnodecount - 1  # one less
                lotareas, loteifs = self.determineCatchmentLotAreas(currentAttList, blocksystems)

                nonlotarea = total_catch_area - sum(lotareas.values())
                if self.include_pervious:
                    total_lot_imparea = 0.0
                    for j in lotareas.keys():
                        total_lot_imparea += lotareas[j] * loteifs[j]
                    nonlotimparea = total_catch_imparea - total_lot_imparea
                    if nonlotarea == 0:
                        nonloteia = 0.0
                    else:
                        nonloteia = nonlotimparea / nonlotarea
                else:
                    nonlotarea = total_catch_imparea - sum(lotareas.values())
                    nonloteia = 1

                if nonlotarea == 0:
                    self.notify("ISSUE: NONLOT AREA ZERO ON BLOCK: " + str(currentID))
                ncount_list = []

                lotoffset = 0
                if catchnodecount > 1:
                    for j in lotareas.keys():  # Loop over lot catchments
                        if lotareas[j] == 0:
                            continue
                        ncount_list.append(ncount)
                        ubmusicwrite.writeMUSICcatchmentnode(ufile, currentID, j, ncount, (
                        blockX - self.blocks_size / 4 + (lotoffset * self.blocks_size / 12)) * scalar, (
                                                             blockY + self.blocks_size / 4 + (
                                                             lotoffset * self.blocks_size / 12)) * scalar, lotareas[j],
                                                             loteifs[j], catchment_parameter_list, self.musicversion)
                        lotoffset += 1
                        musicnodedb["BlockID" + str(currentID)]["C_" + j] = ncount
                        ncount += 1

                    # Write Street/Neigh Catchment Node
                    ncount_list.append(ncount)
                    ubmusicwrite.writeMUSICcatchmentnode(ufile, currentID, "", ncount,
                                                         (blockX - self.blocks_size / 4) * scalar, (blockY) * scalar,
                                                         nonlotarea, nonloteia, catchment_parameter_list, self.musicversion)
                    musicnodedb["BlockID" + str(currentID)]["C_R"] = ncount
                    ncount += 1
                else:
                    ncount_list.append(0)
                    ncount_list.append(ncount)
                    ubmusicwrite.writeMUSICcatchmentnode(ufile, currentID, "", ncount,
                                                         (blockX - self.blocks_size / 4) * scalar, (blockY) * scalar,
                                                         total_catch_area, total_catch_EIF, catchment_parameter_list, self.musicversion)
                    musicnodedb["BlockID" + str(currentID)]["C_R"] = ncount
                    ncount += 1

                # (2) WRITE TREATMENT NODES
                lotoffset = -1
                for sys in blocksystems.keys():
                    nodelink = []   #in case there are harvesting systems
                    if len(blocksystems[sys]) == 0:
                        continue
                    curSys = blocksystems[sys][0]

                    systype = curSys.getAttribute("Type")
                    ncount_list.append(ncount)
                    scale = curSys.getAttribute("Scale")
                    if "L" in scale:
                        lotoffset += 1
                        addOffset = lotoffset
                    else:
                        addOffset = 0
                    offsets = self.getSystemOffsetXY(curSys, self.blocks_size)
                    sysKexfil = curSys.getAttribute("Exfil")

                    #Create parameter list, also accounts for integrated storage
                    parameter_list = eval(
                        "self.prepareParameters" + str(curSys.getAttribute("Type")) + "(curSys, sysKexfil)")
                    eval("ubmusicwrite.writeMUSICnode" + str(
                        systype) + "(ufile, currentID, scale, ncount, (blockX+offsets[0]+(addOffset*self.blocks_size/12))*scalar, "+
                                   "(blockY+offsets[1]+(addOffset*self.blocks_size/12))*scalar, parameter_list, self.musicversion)")
                    musicnodedb["BlockID" + str(currentID)]["S_" + scale] = ncount
                    nodelink.append(ncount)
                    ncount += 1

                    if curSys.getAttribute("StoreType") != "NA" and curSys.getAttribute("IntegStore") == 0:
                        storeType = curSys.getAttribute("StoreType")
                        parameter_list = eval("self.prepareParameters"+str(storeType)+"Store(curSys, sysKexfil)")
                        eval("ubmusicwrite.writeMUSICnode"+str(
                            storeType)+"(ufile, currentID, scale, ncount, (blockX+offsets[0]+(0.125*self.blocks_size)+(addOffset*self.blocks_size/12))*scalar,"+
                             "(blockY+offsets[1]+(addOffset*self.blocks_size/12))*scalar, parameter_list, self.musicversion)")
                        musicnodedb["BlockID"+str(currentID)]["ST_"+scale] = ncount
                        nodelink.append(ncount)
                        ncount += 1
                        ubmusicwrite.writeMUSIClink(ufile, nodelink[0], nodelink[1], routeparams, self.musicversion)   #link the two systems

                # (3) WRITE BLOCK JUNCTION
                ncount_list.append(ncount)
                offsets = self.getSystemOffsetXY("J", self.blocks_size)
                if int(currentAttList.getAttribute("Outlet")) == 1:
                    self.notify("GOT AN OUTLET at BlockID" + str(currentID))
                    basinID = int(currentAttList.getAttribute("BasinID"))
                    jname = "OUT_Bas" + str(basinID) + "-BlkID" + str(currentID)
                    # self.notify(str(jname))
                else:
                    jname = "Block" + str(currentID) + "J"
                ubmusicwrite.writeMUSICjunction(ufile, jname, ncount, (blockX + offsets[0]) * scalar,
                                                (blockY + offsets[1]) * scalar, self.musicversion)
                musicnodedb["BlockID" + str(currentID)]["J"] = ncount
                ncount += 1

                # (4) WRITE ALL LINKS WITHIN BLOCK
                nodelinks = self.getInBlockNodeLinks(musicnodedb["BlockID" + str(currentID)])
                routeparams = ["Not Routed", 30, 0.25]
                for link in range(len(nodelinks)):
                    ubmusicwrite.writeMUSIClink(ufile, nodelinks[link][0], nodelinks[link][1], routeparams, self.musicversion)

            # (5) WRITE ALL LINKS BETWEEN BLOCKS
            for i in basinblockIDs:
                currentID = i
                currentAttList = self.activesim.getAssetWithName("BlockID" + str(currentID))
                downID = int(currentAttList.getAttribute("downID"))
                # Determine routing parameters
                if self.include_route:
                    if self.musicRR_muskk_auto:
                        # Work out Muskingum k approximation based on block size and 1m/s flow
                        musk_K = max(int(float(self.blocks_size) / 60.0), 3)
                    else:
                        musk_K = self.musicRR_muskk
                    routeparams = ["Routed", musk_K, self.musicRR_musktheta]
                else:
                    routeparams = ["Not Routed", 30, 0.25]  # Defaults

                if downID == -1 or downID == 0:
                    downID = int(currentAttList.getAttribute("drainID"))
                if downID == -1 or downID == 0:
                    continue
                if int(currentAttList.getAttribute("Outlet")) == 1:
                    continue
                else:
                    # print musicnodedb
                    nodelink = self.getDownstreamNodeLink(musicnodedb["BlockID" + str(currentID)],
                                                          musicnodedb["BlockID" + str(downID)])
                    ubmusicwrite.writeMUSIClink(ufile, nodelink[0], nodelink[1], routeparams, self.musicversion)

            ubmusicwrite.writeMUSICfooter(ufile)


    def runEconomicAnalysis(self):
        """Conducts an economic analysis of the life cycle costs and a number of other factors based
        on the planned options exported from the Technology Planning Module (note that this is NOT the benchmark version)
        """

        #PREPARE drate and irate vectors using available inputs


        #Define conversion factor if any



        #GET WSUD Object
            #For each system in that object
                #--> Get system Type and Size or the most relevant parameter for the costing
                #--> Create the Spec using the LCC library
                #--> Convert to real-cost matrix by using varioous rules including
                        # - Maintenance every year?
                        # - Decommissioning at the end?
                        # - The Life Span Rule
                #--> Subject the real-cost matrix to LCC




        pass

        return True


    def runMicroclimateAnalysis(self):
        """ Undertakes land cover analysis followed by applying land surface and air temperature
        relationships to understand local microclimate of the current modelled urban environment.
        """

        #Create temperature vector for all land covers
        dist = [self.as_shape, self.co_shape, self.dg_shape, self.ig_shape, self.rf_shape, self.tr_shape, self.wa_shape]
        mins = [self.as_min, self.co_min, self.dg_min, self.ig_min, self.rf_min, self.tr_min, self.wa_min]
        maxs = [self.as_max, self.co_max, self.dg_max, self.ig_max, self.rf_max, self.tr_max, self.wa_max]

        tempdict = self.createTemperatureDictionary(dist, mins, maxs)

        #Calculate equivalent LSTs at either block or patch level
        if self.assesslevel == "R":
            self.transferTemperatureDataToPatches(tempdict)
        elif self.assesslevel == "B":
            self.transferTemperatureDataToBlocks(tempdict)
        elif self.assesslevel == "P":
            self.transferTemperatureDataToRaster(tempdict)

        #Perform Interpolation or Smoothing
        #COMING SOON!
        return True

    def transferTemperatureDataToPatches(self, tempdict):
        """ Transfers temperature data to patches for different land uses.

        :param tempdict: temperature dictionary created by createTemperatureDictionary()
        :return: void, writes LST value to patch centrepoint map
        """
        self.notify("Transferring Temperature Data To Patches")

        patcheslist = self.activesim.getAssetsWithIdentifier("PatchID")
        for i in range(len(patcheslist)):
            currentPatch = patcheslist[i]
            curA = currentPatch.getAttribute("Area")
            curLUC = self.LUCMatrix[int(currentPatch.getAttribute("LandUse"))-1]
            #print "Block ID", currentPatch.getAttribute("BlockID"), "Patch No.", currentPatch.getAttribute("PatchID"), "Land use", curLUC

            lcoverdict = self.getLandCoverProportions(currentPatch.getAttribute("BlockID"), curLUC)

            patchtemp = 0
            for i in lcoverdict.keys():
                patchtemp += float(lcoverdict[i]) * float(eval(tempdict[i]))

            currentPatch.addAttribute("LSTemp", patchtemp)
        return True

    def transferTemperatureDataToRaster(self, tempdict):
        """Transfers the temperature data to the input land use raster through the land surface cover link

        :param tempdict:
        :return:
        """
        self.notify("Creating Temperature Raster")

        cycledataset = self.activesim.getCycleDataSet(self.cycletype, self.tabindex)
        landuseraster = ubdata.importRasterData(cycledataset["Land Use"])
        cs = landuseraster.getCellSize()
        ncols, nrows = landuseraster.getDimensions()

        blockIndex = self.createBlockMapIndex()
        self.createBlockLUCTemperatures(tempdict)

        newdata = [[-9999 for i in range(ncols)] for j in range(nrows)]     #new array of cols and rows dimensions

        for row in range(nrows):
            for col in range(ncols):
                if landuseraster.getValue(col, row) == -9999:
                    newdata[row][col] = -9999
                    continue
                curLUC = self.LUCMatrix[int(landuseraster.getValue(col, row)-1)]
                curloc = [int((col)*cs/self.blocks_size)+1, int((row)*cs/self.blocks_size)+1]

                try:
                    blockID = blockIndex[curloc[0]][curloc[1]]
                except KeyError:
                    newdata[row][col] = -9999
                    continue
                celltemp = self.activesim.getAssetWithName("BlockID"+str(blockID)).getAttribute("LST_"+str(curLUC))
                newdata[row][col] = celltemp

        newdata = self.flipRasterData(newdata)

        passes = 1
        newdata = self.smoothRasterData(passes, newdata)

        # DEBUG - WRITE TO OUTPUT RASTER
        f = open(self.activesim.getActiveProjectPath() + "/LSTOutput.txt", 'w')
        f.write("ncols \t" + str(ncols) + "\n")
        f.write("nrows \t" + str(nrows) + "\n")
        f.write("xllcorner \t" + str(landuseraster.getExtents()[0]) + "\n")
        f.write("yllcorner \t" + str(landuseraster.getExtents()[1]) + "\n")
        f.write("cellsize \t" + str(cs) + "\n")
        f.write("NODATA_value \t" + str(-9999) + "\n")
        for i in range(len(newdata)):
            tempstring = ""
            for j in range(len(newdata[i])):
                tempstring += str(newdata[i][j]) + " "
            f.write(tempstring + "\n")
        f.close()

    def smoothRasterData(self, passes, dataset):
        nrows = len(dataset)
        ncols = len(dataset[0])
        finaldataset = []
        for p in range(passes):
            newraster = [[-9999 for i in range(ncols)] for j in range(nrows)]
            for r in range(nrows):
                for c in range(ncols):
                    curval = dataset[r][c]
                    if curval == -9999:
                        continue
                    newraster[r][c] = self.getAverageNeighbourValue(dataset, r, c, nrows, ncols)
            finaldataset = newraster
        return finaldataset


    def getAverageNeighbourValue(self, dataset, row, col, nrows, ncols):
        neighbourhood = []
        xyoffsets = [-1, 0, 1]  # matrix to track the offsets and neighbours
        for y in xyoffsets:
            for x in xyoffsets:
                try:
                    neighbourhood.append(dataset[row+y][col+x])
                except IndexError:
                    continue
        neighbourhood = filter(lambda x: x != -9999, neighbourhood)
        return float(sum(neighbourhood))/float(len(neighbourhood))


    def flipRasterData(self, dataset):
        flipdata = []
        currentrow = len(dataset) - 1
        while currentrow >= 0:
            row = dataset[currentrow]
            for i in range(len(row)):
                row[i] = float(row[i])
            flipdata.append(row)
            currentrow -= 1
        return flipdata


    def createBlockLUCTemperatures(self, tempdict):
        blocklist = self.activesim.getAssetsWithIdentifier("BlockID")
        for b in range(len(blocklist)):
            if blocklist[b].getAttribute("Status") == 0:
                continue
            curblock = blocklist[b]
            curID = curblock.getAttribute("BlockID")

            for luc in self.LUCMatrix:
                if curblock.getAttribute("pLU_"+luc) == 0:
                    curblock.addAttribute("LST_" + luc, -9999)
                    continue

                lcoverdict = self.getLandCoverProportions(curID, luc)
                lcoverTemp = 0
                for i in lcoverdict.keys():
                    lcoverTemp += float(lcoverdict[i]) * float(eval(tempdict[i]))

                curblock.addAttribute("LST_"+luc, lcoverTemp)

    def createBlockMapIndex(self):
        blocklist = self.activesim.getAssetsWithIdentifier("BlockID")

        blockIndex = {}
        widths = []
        heights = []

        map_attr = self.activesim.getAssetWithName("MapAttributes")
        width = map_attr.getAttribute("WidthBlocks")
        height = map_attr.getAttribute("HeightBlocks")

        # for i in range(len(blocklist)):
        #     widths.append(blocklist[i].getAttribute("LocateX"))
        #     heights.append(blocklist[i].getAttribute("LocateY"))
        # width = max(widths)
        # height = max(heights)

        for i in range(width):
            blockIndex[int(i+1)] = {}

        for i in range(len(blocklist)):
            curblock = blocklist[i]
            if curblock.getAttribute("Status") == 0:
                continue

            blockIndex[int(curblock.getAttribute("LocateX"))][int(curblock.getAttribute("LocateY"))] = curblock.getAttribute("BlockID")
            #If we query the correct X and Y, we'll get the BlockID

            #Only does this for blocks, which are active
        return blockIndex


    def transferTemperatureDataToBlocks(self, tempdict):
        """ Transfers temperature data to block Centre points for different land uses for use in
        interpolation, also writes the LST to the block map for export.

        :param tempdict: temperature dictionary obtained from createTemperatureDictionary()
        :return: void, writes LST value to block map and block centre point map
        """
        self.notify("Transferring Temperature Data To Blocks")

        map_attr = self.activesim.getAssetWithName("MapAttributes")     #fetches global map attributes
        blocks_size = map_attr.getAttribute("BlockSize")

        #Retrieve Blocks
        blocklist = self.activesim.getAssetsWithIdentifier("BlockID")

        #Loop across blocks and calculate temperatures
        for i in range(len(blocklist)):
            if blocklist[i].getAttribute("Status") == 0:
                continue
            currentAttList = blocklist[i]
            currentID = currentAttList.getAttribute("BlockID")
            blockCP = self.activesim.getAssetWithName("BlockCPID"+str(currentID))       #Note that there is also possibly a CBD centre point!

            blocktemp = 0

            for luc in self.LUCMatrix:
                pLU = currentAttList.getAttribute("pLU_"+luc)
                lcoverdict = self.getLandCoverProportions(currentID, luc)

                for j in lcoverdict.keys():
                    blocktemp += float(lcoverdict[j]) * float(eval(tempdict[j])) * pLU

            currentAttList.addAttribute("LSTemp", blocktemp)
            blockCP.addAttribute("LSTemp", blocktemp)
        return True


    def createTemperatureDictionary(self, dist, minvalues, maxvalues):
        """ Creates the reference dictionary for the land cover temperatures

        :param dist:    shape of the distribution for all proposed surface cover temperatures
        :param mins:    input vector of all minimum temperature values
        :param maxs:    input vector of all maximum temperature values
        :return: tempdict, to be called with eval() since some options have a random generation contained within them
        """
        refnames = ["AS", "CO", "DG", "IG", "RF", "TR", "WA"]
        tempdict = {}
        for i in range(len(refnames)):
            if dist[i] == "C":
                tempdict[refnames[i]] = str(minvalues[i])
            elif dist[i] == "B":
                tempdict[refnames[i]] = "min(max(random.normalvariate(("+str((minvalues[i]+maxvalues[i])/2.0)+", ("+str((minvalues[i]+maxvalues[i])/20.0)+", "+str(minvalues[i])+"), "+str(maxvalues[i])+")"
            elif dist[i] == "U":
                tempdict[refnames[i]] = "random.randrange("+str(minvalues[i])+", "+str(maxvalues[i])+")"
        return tempdict


    def getLandCoverProportions(self, blockID, landuse):
        """ Retrieves the full set of land cover proportions for different land uses for a given block ID

        :param blockID: ID of the block to look up land cover information for
        :param landuse: land use code to look up land cover information for.
        :return:
        """
        lcover = {"CO": 0.00, "AS": 0.00, "TR": 0.00, "DG": 0.00, "IG": 0.00, "RF": 0.00, "WA": 0.00}
        currentAttList = self.activesim.getAssetWithName("BlockID"+str(blockID))
        if landuse in ["RES", "COM", "ORC", "LI", "HI", "TR", "CIV"]:
            covers = ["CO", "AS", "TR", "DG", "IG", "RF"]
            if landuse == "CIV":
                landuse = "COM"
            elif landuse == "TR":
                landuse = "LI"
        elif landuse in ["PG", "REF"]:
            covers = ["CO", "AS", "TR", "DG", "IG"]
        elif landuse in ["UND", "SVU"]:
            covers = ["DG", "IG"]
        elif landuse in ["RD"]:
            covers = ["AS", "CO", "DG", "IG"]
        elif landuse in ["NA"]:
            covers = ["IG", "CO", "DG"]

        for c in covers:
            lcover[c] = currentAttList.getAttribute("LC_"+landuse+"_"+c)
        return lcover


    def runWaterSupply(self):
        """ Conducts integration with EPANET and water supply modelling. Coming Soon. Subject of
        future research
        """
        map_attr = self.activesim.getAssetWithName("MapAttributes")     #fetches global map attributes
        params = {}     #Dictionary containing all relevant data for integrated water supply balance sim

        if self.masterplanmodel:    #differentiate between planning and implementation models
            filesuffix = "PC"
            strats = self.strats
        else:
            filesuffix = "IC"
            strats = 1

        self.notify("Total Basins: "+str(self.totalbasins))
        self.notify("Total Strategies: "+str(strats))

        #(1) - Demand Downscaling Data
        enduses = ["kitchen", "shower", "toilet", "laundry", "irrigation", "com", "ind", "publicirri", "losses"]
        for i in enduses:
            if i == "losses":
                map_attr.addAttribute("wdp_losses", self.cdp)   #Constant pattern for losses
                params["losses_pat"] = self.cdp
                continue
            if eval("self."+i+"pat") == "SDD":
                map_attr.addAttribute("wdp_"+i, self.sdd)
                params[i+"_pat"] = self.sdd     #Save patterns to the parameter file
            elif eval("self."+i+"pat") == "CDP":
                map_attr.addAttribute("wdp_"+i, self.cdp)
                params[i + "_pat"] = self.cdp
            elif eval("self."+i+"pat") == "OHT":
                map_attr.addAttribute("wdp_"+i, self.oht)
                params[i + "_pat"] = self.oht
            elif eval("self."+i+"pat") == "AHC":
                map_attr.addAttribute("wdp_"+i, self.ahc)
                params[i + "_pat"] = self.ahc
            else:
                map_attr.addAttribute("wdp_"+i, eval("self.cp_"+i))
                params[i + "_pat"] = eval("self.cp_"+i)

        # (2) - Integrated Water Supply Balance Simulation
        #Check if an IWBS is needed...
        if self.epanet_simtype != "STS" and self.run_fullTSSim:            #Introduce something for simplified 24-hr sim
            self.notify("Conducting Integrated Water Supply Balance")

            #Scaling Rules for temporal file
            params["globalaverage"] = self.globalaverage
            params["globalavgauto"] = self.globalavgauto

            #Transfer temporal rule parameters
            params["weekend_res"] = self.weekend_res
            params["weekend_resfact"] = self.weekend_res_factor
            params["weekend_nres"] = self.weekend_nres
            params["weekend_nresfact"] = self.weekend_nres_factor

            #Transfer alt supply parameters
            params["init_store_levels"] = self.init_store_levels
            params["priority_pubirri"] = self.priority_pubirri
            params["priority_privirri"] = self.priority_privirri
            params["priority_privin_nc"] = self.priority_privin_nc
            params["priority_privin_c"] = self.priority_privin_c
            params["regional_supply_rule"] = self.regional_supply_rule

            #print "Params ", params

            #Grab Scaling Data Set and create a scalar array
            scalefiledata = ubseries.loadClimate(self.scalefile, 1440, self.scaleyears)
            #print scalefiledata
            if self.globalavgauto:
                scalefilefact = ubseries.convertClimateToScalars(scalefiledata, "REL", 0)
            else:
                scalefilefact = ubseries.convertClimateToScalars(scalefiledata, "REL", self.globalaverage)

            #Retrieve the basin structure and set up a dictionary to track demands each time step
            stratlist = self.getWSUDSystemsForStratID(1, 9999)  #Get ALL WSUD assets in the strategy

            block_track = {}
            block_wsud = {}
            basin_structure = {}
            for i in range(self.totalbasins):
                # Gain an Idea of the Block Progression
                curbas = i+1
                basinblockIDs = self.getBlocksIDsForBasinID(curbas)
                idflow_assets, idflow_order = self.determineBlockFlowOrder(basinblockIDs)
                basin_structure[curbas] = [idflow_order, idflow_assets]
                #print idflow_order
                for j in range(len(idflow_order)):
                    block_track[idflow_order[j]] = []
                    block_wsud[idflow_order[j]] = [None, None, None]      #[Lot, neigh, basin]

            wsudscales = ["L_RES", "N", "B"]
            for i in stratlist:
                curWSUD = i
                blockID = curWSUD.getAttribute("Location")
                scale = curWSUD.getAttribute("Scale")
                if curWSUD.getAttribute("StoreVol") > 0:
                    block_wsud[blockID][wsudscales.index(scale)] = curWSUD
            print block_wsud


            #Proceed to Do Water Balance
            #Avoid running through time series as many times as possible.

            # Debugger to only run a certain number of time steps
            debugStopper = 4    #DEBUG: how many time steps to work with
            # ---------------------------------------------------

            f = open("C:/Users/Peter Bach/Documents/Coding Projects/TimeSeriesResults.csv", 'w')
            headerstring = "Time,Rain[mm],"
            for i in block_track.keys():
                for j in enduses:
                    headerstring+= str(i)+"_"+str(j)+","
            f.write(headerstring+"\n")

            sb_labels = ["StoreInit", "Inflow", "Spill", "OtherLoss", "Demand", "Supply", "StoreFinal"]
            g = open("C:/Users/Peter Bach/Documents/Coding Projects/TimeSeriesStorages.csv", 'w')
            headerstring = "Time,Rain[mm],Evap[mm],"
            #     for j in

            scaledaytracker = 0
            scaledaytrackermax = len(scalefilefact)
            evapdaytracker = 0
            evapdaytrackermax = len(self.evapdata)
            monthtracker = 0
            irrigationtracker = 9999  # Start at a very high number

            curday = dtparse.parse(self.raindata[0][0]).day
            curmonth = dtparse.parse(self.raindata[0][0]).month
            self.notify("Current dt " + self.raindata[0][0])
            for i in range(len(self.raindata)):

                #Debugger to only run a certain number of time steps
                # if debugStopper == 0:
                #     break
                #---------------------------------------------------
                cdateTime = self.raindata[i][0]
                cdateTimeP = dtparse.parse(cdateTime)
                julianday = int(format(dtparse.parse(cdateTime), "%j")) #Julian day i.e. the continuous numbered day of the year

                if cdateTimeP.month != curmonth:
                    curmonth = cdateTimeP.month
                    self.notify("Current dt "+cdateTime)

                #Check the current day for the scaling data
                if curday != dtparse.parse(cdateTime).day:
                    scaledaytracker += 1
                    if scaledaytracker > scaledaytrackermax:
                        scaledaytracker = 0      #Reset to zero if it has reached its maximum
                    evapdaytracker += 1
                    if evapdaytracker > evapdaytrackermax:
                        evapdaytracker = 0
                    curday = dtparse.parse(cdateTime).day

                #Check if irrigation necessary
                if self.rain_no_irrigate:
                    if self.raindata[i][1] > 0:
                        irrigationtracker = 0   #Set to zero
                    else:
                        irrigationtracker += 1

                for j in range(self.totalbasins):
                    curbas = j+1
                    basblocks = basin_structure[curbas][1]
                    for k in range(len(basblocks)):
                        bWD = ubwaterbal.UB_BlockDemand(cdateTime, self.raindata[i][1], self.evapdata[evapdaytracker][1],
                                                  scalefilefact[scaledaytracker][1], params, basblocks[k])

                        if irrigationtracker < self.irrigate_lead:
                            bWD["irrigation"] = 0.0     #If the irrigationtracker is less than lead time, do not irrigate
                            bWD["publicirri"] = 0.0     #if this is switched off, the tracker is ALWAYS > lead time

                        block_track[basblocks[k].getAttribute("BlockID")] = bWD

                #print block_track

                #Write the data into a .csv for tracking
                datastring = str(cdateTime)+ "," + str(self.raindata[i][1]) + ","
                for j in block_track.keys():
                    block_use_data = block_track[j]
                    for k in enduses:
                        #print k, block_use_data
                        datastring += str(block_use_data[k]) + ","
                f.write(datastring + "\n")

                # Debugger to only run a certain number of time steps
                # debugStopper -= 1
                # ---------------------------------------------------

            f.close()
            print "FINISHED"

        #(3) - EPANET Link
        #Check for valid EPANET file, if not valid, do not run
        self.notify("Performing EPANET Link...")
        if not os.path.isfile(self.epanet_inpfname):
            self.notify("Warning, no valid EPANET simulation file found, skipping assessment")
            return True

        base_inpfile = ubepanet.readInpFile(self.epanet_inpfname)   #Load file data
        node_list = ubepanet.getDataFromInpFile(base_inpfile, "[COORDINATES]", "array")   #Get the nodes as [name, x, y]
        node_props = ubepanet.getDataFromInpFile(base_inpfile, "[JUNCTIONS]", "dict")       #Get the list of Junctinos as {"Name" : [elev, demand, etc.]}
        #print node_list
        #print node_props

        #Apply offset to entire Node List
        if self.epanet_offset:
            node_list, offx, offy = self.applyNetworkJunctionOffsets(node_list)
        else:
            offx, offy = 0, 0

        #Scan node list and create final list that follow two conditions:
        # (1) keep only nodes in the junction list,
        # (2) remove zero demand nodes if necessary
        rev_node_list = []
        for i in node_list:
            if i[0] in node_props.keys():   #(1) check if node in junction list
                if self.epanet_excludezeros and float(node_props[i[0]][1]) == 0:
                    #If the node is a Junction, check if its demand is zero, if yes, skip
                    continue
                rev_node_list.append(i) #add the current node to the revised list if it passes (1) and (2)

        self.notify("Found " + str(len(rev_node_list)) + " out of "+ str(len(node_list)) + " relevant nodes.")

        #Run the corresponding integration, which will return a dictionary of the node-block relationship
        if self.epanetintmethod == "VD":
            nbrelation = self.analyseVoronoi(rev_node_list)
        elif self.epanetintmethod == "DT":
            nbrelation = self.analyseDelaunay(rev_node_list)
        elif self.epanetintmethod == "RS":
            nbrelation = self.analyseRadialScan(rev_node_list)
        elif self.epanetintmethod == "NN":
            nbrelation = self.analyseNearestNeigh(rev_node_list)

        #[OPTIONS] & [TIMES] lists
        opt_list = ubepanet.getDataFromInpFile(base_inpfile, "[OPTIONS]", "dict")
        times_list = ubepanet.getDataFromInpFile(base_inpfile, "[TIMES]", "dict")
        #print times_list

        for a in times_list.keys():
            if len(times_list[a]) > 1:
                mergestring = ""
                for b in range(len(times_list[a])):
                    mergestring += str(times_list[a][b])
                times_list[a] = [mergestring]

        for a in opt_list.keys():
            if len(opt_list[a]) > 1:
                mergestring = ""
                for b in range(len(opt_list[a])):
                    mergestring += str(opt_list[a][b])
                opt_list[a] = [mergestring]


            #Set the Times List
        if self.epanet_simtype == "STS": #STS = static sim, 24H = 24-hour, EPS = extended period sim (72hrs), LTS = long-term sim
            times_list["Duration"] = ['0:00']
        elif self.epanet_simtype == "24H":
            times_list["Duration"] = ['24:00']
        elif self.epanet_simtype == "EPS":
            times_list["Duration"] = ['72:00']
        elif self.epanet_simtype == "LTS":
            times_list["Duration"] = ['24:00']

        times_list["Hydraulic Timestep"] = [self.epanetsim_hts]
        times_list["Quality Timestep"] = [self.epanetsim_qts]

            #Set the Options List
        opt_list["Headloss"] = [self.epanetsim_hl]
        opt_list["Specific Gravity"] = [self.epanetsim_specg]
        opt_list["Viscosity"] = [self.epanetsim_visc]
        opt_list["Trials"] = [self.epanetsim_trials]
        opt_list["Accuracy"] = [self.epanetsim_accuracy]
        opt_list["Emitter Exponent"] = [self.epanetsim_emit]
        opt_list["Demand Multiplier"] = [self.epanetsim_demmult]

        #Rewrite [JUNCTIONS] list Section of the EPANET File
        node_props = self.adjustEPANETjunctions(node_props, nbrelation)

        #Write the [PATTERN] and full demand profile depending on the type of simulation
        if self.epanet_simtype == "STS":
            pat_list = []
            dem_list = []
        else:
            #Populate Pattern List
            pat_list = {"1" : self.createPatternString(self.cdp),
                        "PKitch" : self.createPatternString(map_attr.getAttribute("wdp_kitchen")),
                        "PShower": self.createPatternString(map_attr.getAttribute("wdp_shower")),
                        "PToilet": self.createPatternString(map_attr.getAttribute("wdp_toilet")),
                        "PLaundry": self.createPatternString(map_attr.getAttribute("wdp_laundry")),
                        "PGarden": self.createPatternString(map_attr.getAttribute("wdp_irrigation")),
                        "PCom": self.createPatternString(map_attr.getAttribute("wdp_com")),
                        "PInd": self.createPatternString(map_attr.getAttribute("wdp_ind")),
                        "PPubIrr": self.createPatternString(map_attr.getAttribute("wdp_publicirri")),
                        "PLosses": self.createPatternString(map_attr.getAttribute("wdp_losses"))}

            dem_list = self.adjustEPANETdemands(rev_node_list, nbrelation)
            #print dem_list

        #Use the node block list to work out the new demands and rewrite the EPANET file
        if self.runBaseInp:
            self.rewriteEPANETbase(base_inpfile, offx, offy)


        self.writeUB_EPANETfile(base_inpfile, node_list, opt_list, times_list,
                                node_props, dem_list, pat_list)

        #Run the EPANET Simulations
        self.runEPANETsim()
        return True

    def retrieveStoragesForBlock(self, blockID):
        """Runs through the WSUD strategies and returns all systems that are 'relevant' i.e.
                - with storage for the indicated block ID
                - at the lot and neighbourhood scales
            in the block flow order specified.

        :param idorder: Array of block IDs in the order upstream to downstream
        :return: assets of relevant WSUD systems at the Lot, Neighbourhood and Basin scales
        """
        stratlist = [None, None]


        return stratlist


    def applyNetworkJunctionOffsets(self, nodelist):
        """Applies a custom offset to the entire EPANET node list coordinates. This offset allows alignment of GIS
        map with EPANET network map.

        :param nodelist: the nodelist obtained from ubEPANET
        :return: nodelist with offset coordinates
        """
        newnodelist = []

        if self.epanet_useProjectOffset:
            map_attr = self.activesim.getAssetWithName("MapAttributes")
            self.epanet_offsetX = map_attr.getAttribute("xllcorner")
            self.epanet_offsetY = map_attr.getAttribute("yllcorner")

        offx = self.epanet_offsetX
        offy = self.epanet_offsetY

        for i in range(len(nodelist)):
            newnodelist.append([nodelist[i][0], str(float(nodelist[i][1])+float(offx)), str(float(nodelist[i][2])+float(offy))])
        return newnodelist, offx, offy


    def createPatternString(self, pattern):
        """Creates a string that represents the demand pattern of a particular end use (patname)
        returns a tab-delimited string of patterns
        :param pattern: the variable containing the pattern name
        :return: patstring, the tab-delimited string
        """
        patstring = ""
        for i in range(len(pattern)):
            patstring += str(pattern[i]) + "\t"
        patstring.rstrip("\t")
        patstring += "\n"
        return patstring

    def adjustEPANETjunctions(self, node_props, nbrelation):
        """Rewrites the node properties list with the new demands depending on simulation type
        :param node_props: the Node properties list obtained by retrieving the [JUNCTIONS] data
        :param nbrelation: relationship between blocks and nodes
        :return: a revised node props dictionary that can be transferred back into the inp file under [JUNCTIONS]
        """
        self.notify("Readjusting Junction Demands...")
        new_node_data = {}
        node_dem = ubdata.UBComponent()

        for i in node_props.keys():
            nodedata = node_props[i]

            #Grab all the data for the single node id
            nbfilter = []
            for j in nbrelation.keys():
                abbr = str(i)+"-"
                relationnameLength = len(j.split("-")[0])
                if abbr in j and len(abbr) == relationnameLength+1:
                    nbfilter.append(j)

            #nbfilter = [nbrelation.keys()[j] for j in range(len(nbrelation.keys())) if str(i)+"-" in nbrelation.keys()[j]]
            if len(nbfilter) == 0:
                new_node_data[i] = nodedata
                node_dem.addAttribute("NodeID_"+str(i), [nodedata[1], nodedata[1]])
                continue
            if i == 1 or i=="1":
                print nbfilter

            #for all others grab block demand data and tally up
            nodedemand = self.calculateWeightedNodeDemand(nbrelation, nbfilter, "Blk_WD")
            # nodedemand = 0
            # for j in range(len(nbfilter)):
            #     bID = nbrelation[nbfilter[j]][1]
            #     bdata = self.activesim.getAssetWithName("BlockID"+str(bID))
            #     prop = nbrelation[nbfilter[j]][4]
            #     nodedemand += float(bdata.getAttribute("Blk_WD") * cf * prop)

            if i == 1 or i=="1":
                print nodedemand

            node_dem.addAttribute("NodeID_"+str(i), [nodedata[1], nodedemand])

            new_node_data[i] = [nodedata[0], nodedemand,';']

        self.activesim.addAsset("NodeDemands", node_dem)    #For graphing later on
        return new_node_data

    def adjustEPANETdemands(self, rev_node_list, nbrelation):
        """Calculates the individual end uses and writes them into a new data array that
        adds to [DEMANDS] in the EPANET .inp file
        :param rev_node_list: the node list that is
        :param nbrelation:
        :return:
        """
        self.notify("Layering Junction Demand Patterns...")
        enduse_atts = ["Blk_kitchen", "Blk_shower", "Blk_toilet", "Blk_laundry", "Blk_irrigation",
                        "Blk_com", "Blk_ind","Blk_publicirri", "Blk_losses"]
        pattern_names = ["PKitch", "PShower", "PToilet", "PLaundry", "PGarden",
                         "PCom", "PInd", "PPubIrr", "PLosses"]

        new_demand_data = []

        for i in rev_node_list:
            curID = i[0]
            if curID == "1" or curID == 1:
                print "BIG DEMAND NODE!!"
            #nbfilter = [nbrelation.keys()[j] for j in range(len(nbrelation.keys())) if str(curID)+"-" in nbrelation.keys()[j]]
            nbfilter = []
            abbr = curID+"-"
            for j in nbrelation.keys():
                relationnameLength = len(j.split("-")[0])
                if abbr in j and len(abbr) == relationnameLength+1:
                    nbfilter.append(j)
            if abbr == "1-":
                print nbfilter


            if len(nbfilter) == 0:
                continue
            for k in range(len(enduse_atts)):
                nodedemand = self.calculateWeightedNodeDemand(nbrelation, nbfilter, enduse_atts[k])
                if nodedemand != 0:
                    new_demand_data.append([curID, nodedemand, pattern_names[k], ";"+str(enduse_atts[k])])

        return new_demand_data


    def calculateWeightedNodeDemand(self, nbrelation, nbfilter, enduse):
        """Calculates a weighted average of a demand for a particular node based on a specified
        attribute. The function uses results from the integration method (nbrelation) to determine
        the final value.
        :param nbrelation:
        :param nbfilter:
        :return:
        """
        if enduse in ["Blk_WD"]:
            cf = float(1000.0/(365.0*24.0*3600.0)) #kL/yr into L/sec
        elif enduse in ["Blk_kitchen", "Blk_shower", "Blk_toilet", "Blk_laundry", "Blk_irrigation",
                        "Blk_com", "Blk_ind", "Blk_publicirri", "Blk_losses"]:
            cf = float(1000.0/(24.0*3600.0))     #kL/day into L/sec

        nodedemand = 0
        for j in range(len(nbfilter)):
            bID = nbrelation[nbfilter[j]][1]
            bdata = self.activesim.getAssetWithName("BlockID"+str(bID))
            prop = nbrelation[nbfilter[j]][4]
            nodedemand += float(bdata.getAttribute(enduse) * cf * prop)
        return nodedemand

    def determineBlockFlowOrder(self, idList):
        """ Orders blocks in flow direction for modelling drainage system from upstream most to
        downstream most block for a given input list.
        :param idList: List of BlockIDs that are connected to each other e.g. [319, 300, 303, 301, 282]
        :return:
        """
        blockassets = []
        for i in idList:
            blockassets.append(self.activesim.getAssetWithName("BlockID"+str(i)))

        blockOrder = []
        blockIDs = []
        for block in blockassets:
            upstreamBlocks = block.getAttribute("UpstrIDs")
            if len(upstreamBlocks) == 0:
                blockOrder.append(block)
                blockIDs.append(block.getAttribute("BlockID"))

        for i in blockOrder:
            if i.getAttribute("downID") == -1:
                downID = i.getAttribute("drainID")
            else:
                downID = i.getAttribute("downID")
            if downID == -1:
                continue
            if downID in blockIDs:
                continue
            else:
                blockOrder.append(self.activesim.getAssetWithName("BlockID"+str(downID)))
                blockIDs.append(downID)

        return blockOrder, blockIDs

    def runIWCM(self):
        """ Creates a simulation file and calls the CityDrain3 Modelling Platform to undertake
        detailed performance assessment of the integrated urban water cycle from a quantity and
        quality perspective.
        """
        pass

        return True

    ########################################################
    #EPANET Integration SUBFUNCTIONS                       #
    ########################################################
    def analyseVoronoi(self, node_list):
        self.notify("Creating and intersecting blocks with Voronoi Diagram")
        nbrelation = {}  #Node ID: [[blockID, weight],...]
        blocksize = float(self.activesim.getAssetWithName("MapAttributes").getAttribute("BlockSize"))

        #Create Numpylist
        ptList = []
        for i in range(len(node_list)):
            ptList.append([float(node_list[i][1]), float(node_list[i][2])])
        numPtList = numpy.array(ptList)        #Scipy's spatial library deals with numpy arrays

        #Run scipy.spatial Voronoi
        vor = sps.Voronoi(numPtList)    #Perform the Voronoi search

        if vor.points.shape[1] != 2: #Checks if the shape is 2D
            raise ValueError("Need a 2D input!")

        new_regions = []
        new_vertices = vor.vertices.tolist()    #Converts the ndarray to a nested python list

        #Get some geometric details so that we can set the bounds
        center = vor.points.mean(axis=0)    #Computes the mean value of all coordinates around the center axis
        radius = vor.points.ptp(axis=0).max()    #Gets the largest peak to peak value using ndarray.ptp()

        #Collect all ridges
        all_ridges = {}

        #Map each point onto each ridge
        for (pt1, pt2), (vt1,vt2) in zip(vor.ridge_points, vor.ridge_vertices):
            #zip() aggregates elements from each iterable

            #We essentially assign the vertices to pt1 and pt2 in the dictionary
            #   the mapping tells us that pt1 has vertices vt1 and vt2, which are shared
            #   with pt2 and vice versa
            all_ridges.setdefault(pt1, []).append((pt2,vt1,vt2))
            all_ridges.setdefault(pt2, []).append((pt1, vt1, vt2))

        #Deal with infinite edges, create the data of polygons
        for p1, region in enumerate(vor.point_region):
        #    print p1, region
            vert = vor.regions[region]
            if -1 not in vert:
                new_regions.append(vert)
                continue

            #If -1 is found, reconstruct a non-infinite region based on the radius
            ridges = all_ridges[p1]
            new_reg = [v for v in vert if v >= 0]    #Define a new region, add to it all non-infinite vertices

            for p2, v1, v2 in ridges:
                if v2 < 0:
                    v1, v2 = v2, v1 #if it's v2 that's -1 then swap them around
                if v1 >= 0:
                    #finite ridge: already in the region variable, skip
                    continue

                #Compute the missing endpoint of an infinite ridge
                t = vor.points[p2] - vor.points[p1]
                t /= numpy.linalg.norm(t)

                # Compute the missing endpoint of an infinite ridge
                t = vor.points[p2] - vor.points[p1] # tangent
                t /= numpy.linalg.norm(t)
                n = numpy.array([-t[1], t[0]])  # normal

                midpoint = vor.points[[p1, p2]].mean(axis=0)
                direction = numpy.sign(numpy.dot(midpoint - center, n)) * n
                far_point = vor.vertices[v2] + direction * radius

                new_reg.append(len(new_vertices))
                new_vertices.append(far_point.tolist())

            # sort region counterclockwise
            vs = numpy.asarray([new_vertices[v] for v in new_reg])
            c = vs.mean(axis=0)
            angles = numpy.arctan2(vs[:,1] - c[1], vs[:,0] - c[0])
            new_reg = numpy.array(new_reg)[numpy.argsort(angles)]

            # finish
            new_regions.append(new_reg.tolist())

        #Craete the Polygon list to do the intersection
        voronoipoly = {}        #Holds all the data of the voronoi polygons based on node ID
        counter = 0
        for reg in new_regions:
            polycoor = []
            for vindex in reg:
                polycoor.append(new_vertices[vindex])
            voronoipoly[node_list[counter][0]] = Polygon.Polygon(polycoor)
            counter += 1

        #Get block layer, transform into proper coordinate system
        block_data = self.activesim.getAssetsWithIdentifier("BlockID")
        map_data = self.activesim.getAssetWithName("MapAttributes")
        offsets = [map_data.getAttribute("xllcorner"), map_data.getAttribute("yllcorner")]

        #Create block geometry list
        blocksgeom = {}     #Holds all the data of the block polygons based on BlockID
        for i in range(len(block_data)):
            curblock = block_data[i]
            if curblock.getAttribute("Status") == 0:
                continue
            nl = curblock.getCoordinates()  #returns [(x, y, z), (x, y, z), etc.]
            blockpts = []
            for j in range(len(nl)):
                blockpts.append([nl[j][0]+offsets[0], nl[j][1]+offsets[1]])
            blocksgeom[curblock.getAttribute("BlockID")] = Polygon.Polygon(blockpts)

        #Intersect layers, calculate areas
        for i in voronoipoly.keys():
            for j in blocksgeom.keys():
                polysect = voronoipoly[i]&blocksgeom[j]
                if polysect.nPoints() == 0:
                    continue
                poly = ogr.Geometry(ogr.wkbPolygon)
                ring = ogr.Geometry(ogr.wkbLinearRing)
                for point in range(len(polysect[0])):
                    ring.AddPoint(polysect[0][point][0], polysect[0][point][1])
                ring.AddPoint(polysect[0][0][0], polysect[0][0][1])
                poly.AddGeometry(ring)
                area = poly.GetArea()
                #print area

                #Key: NodeID-BlockID, attributes [NodeID, BlockID, wkbPolygon, Area]
                nbrelation[str(i)+"-"+str(j)] = [i, j, poly, area, float(area/(blocksize*blocksize))]

        #Write the dictionary, export the intersected shapefile
        if self.epanet_exportshp:
            self.exportEPANETshape(nbrelation, "voronoi")

        return nbrelation

    def exportEPANETshape(self, nbrelation, intmethod):
        gisoptions = self.activesim.getGISExportDetails()
        fname = gisoptions["Filename"]+"_"+intmethod+"_"+str(self.tabindex)
        if gisoptions["ProjUser"] == True:
            proj = gisoptions["Proj4"]
        else:
            proj = gisoptions["Projection"]

        os.chdir(str(self.activesim.getActiveProjectPath()))

        spatialRef = osr.SpatialReference()
        spatialRef.ImportFromProj4(proj)

        drv = ogr.GetDriverByName('ESRI Shapefile')
        if os.path.exists(str(fname)+".shp"): os.remove(str(fname)+".shp")
        shapefile = drv.CreateDataSource(str(fname)+".shp")

        self.notify("Exporting Voronoi Intersect as Shapefile to file: "+str(fname))

        if intmethod in ["voronoi", "delaunay"]:
            layer = shapefile.CreateLayer('layer1', spatialRef, ogr.wkbPolygon)
        else:
            layer = shapefile.CreateLayer('layer1', spatialRef, ogr.wkbLineString)

        layerDefn = layer.GetLayerDefn()

        #Define Attributes
        fielddefmatrix = []
        fielddefmatrix.append(ogr.FieldDefn("NodeID", ogr.OFTString))
        fielddefmatrix.append(ogr.FieldDefn("BlockID", ogr.OFTInteger))

        if intmethod in ["voronoi", "delaunay"]:
            fielddefmatrix.append(ogr.FieldDefn("Area_sqm", ogr.OFTReal))
        else:
            fielddefmatrix.append(ogr.FieldDefn("Dist_m", ogr.OFTReal)) #Will figure out in future

        for field in fielddefmatrix:
            layer.CreateField(field)
            layer.GetLayerDefn()

        #Run through nbrelation and create all geometries
        for i in nbrelation.keys():
            curgeom = nbrelation[i]
            feature = ogr.Feature(layerDefn)
            feature.SetGeometry(curgeom[2])
            feature.SetFID(0)

            #Add Attributes
            feature.SetField("NodeID", str(curgeom[0]))
            feature.SetField("BlockID", int(curgeom[1]))

            if intmethod in ["voronoi", "delaunay"]:
                feature.SetField("Area_sqm", float(curgeom[3]))
            else:
                feature.SetField("Dist_m", float(curgeom[3]))   #Will figure out in future

            layer.CreateFeature(feature)

        shapefile.Destroy()


    def analyseDelaunay(self, node_list):
        nbrelation = {}  #Node ID: [[blockID, weight],...]

        return nbrelation

    def analyseNearestNeigh(self, node_list):
        nbrelation = {}  #Node ID: [[blockID, weight],...]

        return nbrelation

    def analyseRadialScan(self, node_list):
        nbrelation = {}  #Node ID: [[blockID, weight],...]

        return nbrelation

    def rewriteEPANETbase(self, basedata, offX, offY):
        print "Re-run the base input file"
        return True

    def writeUB_EPANETfile(self, basedata, node_list, opt_list, times_list, node_props, dem_list, pat_list):
        epanetpath = self.activesim.getActiveProjectPath()
        epanetfname = self.activesim.getGISExportDetails()["Filename"]+"_epanet.inp"

        f = open(epanetpath+"/"+epanetfname, 'w')
        line = 0
        while line != len(basedata):
            if "[JUNCTIONS]" in basedata[line]:
                f.write("[JUNCTION]\n")
                line += 1
                f.write(";ID \t Elev \t Demand \t Pattern \t\n")
                for nID in node_props.keys():
                    nIDd = node_props[nID]  #nodeIDdata
                    try:
                        f.write(str(nID)+"\t"+str(nIDd[0])+"\t"+str(nIDd[1])+"\t"+str(nIDd[2])+"\t"+"\n")
                    except IndexError:  #Catches an index error if no pattern has been defined for the node
                        if len(nIDd) == 2:      #If no pattern has been defined, just write elevation and demand
                            f.write(str(nID)+"\t"+str(nIDd[0])+"\t"+str(nIDd[1])+"\n")
                        else:   #If no demand has been defined, just write elevation and set demand as zero
                            f.write(str(nID)+"\t"+str(nID[0])+"\t"+str(0)+"\n")
                f.write("\n")   #empty line

                #Move the line variable forward to the next
                while basedata[line][0] != "[":
                    line += 1

            if "[PATTERNS]" in basedata[line] and self.epanet_simtype != "STS":
                f.write("[PATTERNS]\n")
                line += 1
                f.write(";ID \t Multipliers \t\n")
                for pID in pat_list.keys():
                    f.write(str(pID)+"\t"+str(pat_list[pID]))
                f.write("\n")

                #Move the line variable forward to the next
                while basedata[line][0] != "[":
                    line += 1

            if "[OPTIONS]" in basedata[line]:
                f.write("[OPTIONS]\n")
                line += 1
                for oID in opt_list.keys():
                   f.write(str(oID)+"\t"+str(opt_list[oID][0])+"\n")
                f.write("\n")

                #Move the line variable forward to the next
                while basedata[line][0] != "[":
                    line += 1

            if "[TIMES]" in basedata[line]:
                f.write("[TIMES]\n")
                line += 1
                for oID in times_list.keys():
                    f.write(str(oID)+"\t"+str(times_list[oID][0])+"\n")
                f.write("\n")

                #Move the line variable forward to the next
                while basedata[line][0] != "[":
                    line += 1

            if "[DEMANDS]" in basedata[line]:
                #write new demands matrix = [ [id, demand, pattern, comment], ...]
                f.write("[DEMANDS]\n")
                line += 1
                for dID in range(len(dem_list)):
                    demdata = dem_list[dID]
                    f.write(str(demdata[0])+"\t"+str(demdata[1])+"\t"+str(demdata[2])+"\t"+str(demdata[3])+"\n")
                f.write("\n")

                #Move the line variable forward to the next
                while basedata[line][0] != "[":
                    line += 1

            f.write(basedata[line])

            line += 1

        f.close()
        return True

    def runEPANETsim(self):
        print "Calling EPANET"
        return True

    ########################################################
    #WriteMUSICSim SUBFUNCTIONS                            #
    ########################################################
    def getWSUDSystemsForStratID(self, stratID, basinID):
        """Scans the WSUD assets and returns an array of all components within the specified
        strategy ID"""
        wsudIDs = self.activesim.getAssetsWithIdentifier("SysID")
        systemlist = []
        for curSys in wsudIDs:
            if curSys.getAttribute("StrategyID") != int(stratID):
                continue    #Not in current Strategy
            if basinID == 9999 or curSys.getAttribute("BasinID") == int(basinID):
                systemlist.append(curSys)
        return systemlist

    def getBlocksIDsForBasinID(self, basinID):
        """Retrieves all BlockIDs for a specific Basin ID if basinID == 9999, then returns all block IDs
        """
        blockIDs = self.activesim.getAssetsWithIdentifier("BlockID")
        blockIDlist = []
        for b in blockIDs:
            if b.getAttribute("Status") == 0:
                continue    #If block status is zero, continue
            if basinID == 9999 or b.getAttribute("BasinID") == int(basinID):
                blockIDlist.append(int(b.getAttribute("BlockID")))
        # print "BasinID", basinID, "BlockIDs: ", blockIDlist
        return blockIDlist

    def getBlockSystems(self, currentID, systemlist):
        """Scans the systemlist passed to the function and returns all WSUD components
        present in the currentID block in dictionary form based on scale
            - currentID: current Block ID that we want the systems for
            - systemlist: the system list created by scanning the self.wsudAttr View
            - city: city datastream
        """
        sysDict = {"L_RES":[], "L_LI":[], "L_COM":[], "L_HI":[], "L_HDR":[], "L_ORC":[], "S":[], "N":[], "B":[]}
        for curSys in systemlist:
            if int(curSys.getAttribute("Location")) != int(currentID):
                continue
            else:
                sysDict[curSys.getAttribute("Scale")].append(curSys)
        return sysDict

    def determineBlockCatchmentNodeCount(self, blocksystems):
        """Determines the number of catchment nodes to construct in the current block
        based on the system count."""
        catchcount = 1      #Regardless for street/neighbourhood
        for i in blocksystems.keys():
            #One catchment for each lot scale, one combined catchment for street/neigh
            if i in ["S", "N", "B"]:
                continue
            if len(blocksystems[i]) == 0:       #Additional only apply to lot systems
                continue
            catchcount += 1
        return catchcount

    def determineCatchmentLotAreas(self, currentAttList, blocksystems):
        """Determines the areas for each of the lots, which have a system present."""
        lotareas = {"L_RES":0, "L_HDR":0, "L_LI":0, "L_HI":0, "L_COM":0, "L_ORC":0}
        loteifs = {"L_RES":1, "L_HDR":1,"L_LI":1,"L_HI":1,"L_COM":1,"L_ORC":1}

        #Residential Areas
        if len(blocksystems["L_RES"]) != 0:
            resEIA = currentAttList.getAttribute("ResAllots") * \
                     currentAttList.getAttribute("ResLotEIA") / 10000        #[ha]
            if self.include_pervious:
                lotareas["L_RES"] = currentAttList.getAttribute("ResAllots") * \
                    currentAttList.getAttribute("ResLotArea") / 10000
                loteifs["L_RES"] = float (resEIA / lotareas["L_RES"])
            else:
                lotareas["L_RES"] = resEIA

        #High-Density Residential Areas
        if len(blocksystems["L_HDR"]) != 0:
            hdrEIA = currentAttList.getAttribute("HDR_EIA") / 10000
            if self.include_pervious:
                lotareas["L_HDR"] = currentAttList.getAttribute("HDR_TIA") + currentAttList.getAttribute("HDRGarden")
                loteifs["L_HDR"] = float( hdrEIA / lotareas["L_HDR"])
            else:
                lotareas["L_HDR"] = hdrEIA

        #Light Industrial Areas
        if len(blocksystems["L_LI"]) != 0:
            liEIA = currentAttList.getAttribute("LIAeEIA") * \
                currentAttList.getAttribute("LIestates") / 10000
            if self.include_pervious:
                lotareas["L_LI"] = (currentAttList.getAttribute("LIAeEIA") + currentAttList.getAttribute("avLt_LI")) * \
                        currentAttList.getAttribute("LIestates") / 10000
                loteifs["L_LI"] = float(liEIA / lotareas["L_LI"])
            else:
                lotareas["L_LI"] = liEIA

        #Heavy Industrial Areas
        if len(blocksystems["L_HI"]) != 0:
            hiEIA = currentAttList.getAttribute("HIAeEIA") * \
                currentAttList.getAttribute("HIestates") / 10000
            if self.include_pervious:
                lotareas["L_HI"] = (currentAttList.getAttribute("HIAeEIA") + currentAttList.getAttribute("avLt_HI")) * \
                        currentAttList.getAttribute("HIestates") / 10000
                loteifs["L_HI"] = float(hiEIA / lotareas["L_HI"])
            else:
                lotareas["L_HI"] = hiEIA

        #Commercial Areas
        if len(blocksystems["L_COM"]) != 0:
            comEIA = currentAttList.getAttribute("COMAeEIA") * \
                currentAttList.getAttribute("COMestates") / 10000
            if self.include_pervious:
                lotareas["L_COM"] = (currentAttList.getAttribute("COMAeEIA") + currentAttList.getAttribute("avLt_COM")) * \
                        currentAttList.getAttribute("COMestates") / 10000
                loteifs["L_COM"] = float(comEIA / lotareas["L_COM"])
            else:
                lotareas["L_COM"] = comEIA

        #Office/ResCom Mixed Areas
        if len(blocksystems["L_ORC"]) != 0:
            orcEIA = currentAttList.getAttribute("ORCAeEIA") * \
                currentAttList.getAttribute("ORCestates") / 10000
            if self.include_pervious:
                lotareas["L_ORC"] = (currentAttList.getAttribute("ORCAeEIA") + currentAttList.getAttribute("avLt_ORC")) * \
                        currentAttList.getAttribute("ORCestates") / 10000
                loteifs["L_ORC"] = float(orcEIA / lotareas["L_ORC"])
            else:
                lotareas["L_ORC"] = orcEIA
        return lotareas, loteifs

    def getInBlockNodeLinks(self, nodedb):
        """Returns an array of nodeIDs that are connected by a link for all within-block aspects for
        following rules:        - lot catchment to lot system           - lot RES system to street/neigh system
                                - remain catch to stree/neigh system    - lot nonRES sys to neigh system
                                - street sys to neigh sys               - neigh sys to junction
                                - junction to basin sys                 - remain catchment to junction if no sys
                                In the case of stormwater harvesting systems, all treatment goes to storage
                                and all storage goes to downstream treatment/storage
                                """
        nodelinks = []
        linkmap = {"C_L_RES": ["S_L_RES"], "C_L_HDR":["S_L_HDR"], "C_L_LI": ["S_L_LI"],
                   "C_L_HI": ["S_L_HI"], "C_L_COM": ["S_L_COM"], "C_L_ORC": ["S_L_ORC"],
                   "C_R": ["S_S", "S_N", "J"], "J": ["S_B", 0],
                   "S_L_RES": ["ST_L_RES", "S_S", "S_N", "J"], "S_L_HDR": ["ST_L_HDR", "S_N", "J"], "S_L_LI": ["ST_L_LI", "S_N", "J"],
                   "S_L_HI": ["ST_L_HI", "S_N", "J"], "S_L_COM": ["ST_L_COM", "S_N", "J"], "S_L_ORC": ["ST_L_ORC", "S_N", "J"],
                   "ST_L_RES" : ["S_S", "S_N", "ST_N", "J"], "ST_L_HDR": ["S_S", "S_N", "ST_N", "J"], "ST_L_LI": ["S_S", "S_N", "ST_N", "J"],
                   "ST_L_HI" : ["S_S", "S_N", "ST_N", "J"], "ST_L_COM": ["S_S", "S_N", "ST_N", "J"], "ST_L_ORC": ["S_S", "S_N", "ST_N", "J"],
                   "S_S": ["S_N", "ST_N", "J"], "S_N": ["ST_N", "J"], "ST_N" : ["J"], "S_B" : ["ST_B"], "ST_B" : [0]}      #gives the order in which links can be arranged
        for key in nodedb.keys():
            map = linkmap[key]
            #self.notify(str(map))
            for pos in range(len(map)):
                if map[pos] in nodedb.keys():
                    nodelinks.append([nodedb[key], nodedb[map[pos]]])   #[ID1, ID2] in an array
                    break
        #self.notify(str(nodelinks))
        return nodelinks

    def getDownstreamNodeLink(self, upNodes, downNodes):
        """Returns the nodeIDs to connect with a link between two blocks"""
        nodelink = []
        #Case 1: Junction to Junction
        if "S_B" not in upNodes.keys():
            nodelink = [upNodes["J"], downNodes["J"]]
        #Case 2: Basin Storage systems to Junction
        elif "ST_B" in upNodes.keys():
            nodelink = [upNodes["ST_B"], downNodes["J"]]
        #Case 3: No basin storage, just basin system to Junction
        else:
            nodelink = [upNodes["S_B"], downNodes["J"]]
        return nodelink

    def getSystemOffsetXY(self, curSys, blocks_size):
        """Returns the coordinate offsets for the MUSIC node depending on the system scale.
        Offsets are defined in the offsetdictionary and are based on the pre-defined positioning
        for various treatment nodes and various scales. Node that the Lot nodes have an additional
        offset defined when they are placed"""
        offsetdictionary = {"L":[0, 0.25*blocks_size], "S":[0,0],
                            "N":[0, 0.25*blocks_size*(-1)],
                            "B":[0.25*blocks_size,0.25*blocks_size*(-1)] ,
                            "J":[0.25*blocks_size, 0]}  #Used to position treatment nodes depending on their scale
        if curSys == "J":
            return offsetdictionary["J"]
        scale = curSys.getAttribute("Scale")
        if scale in ["L_RES", "L_COM", "L_LI", "L_HDR", "L_HI", "L_ORC"]:
            return offsetdictionary["L"]
        else:
            return offsetdictionary[scale]

    def prepareParametersBF(self, curSys, current_soilK):
        """Function to setup the parameter list vector for biofilters """
        #parameter_list = [EDD, surface area, filter area, unlined perimeter, satk, filterdepth, exfiltration]
        sysqty = self.getSystemQuantity(curSys)
        sysedd = float(curSys.getAttribute("WDepth"))
        sysarea = self.getEffectiveSystemArea(curSys)*sysqty
        sysfd = float(curSys.getAttribute("FDepth"))
        sysKexfil = float(curSys.getAttribute("Exfil"))
        parameter_list = [sysedd,sysarea,sysarea, (2*numpy.sqrt(sysarea/0.4)+2*sysarea/(numpy.sqrt(sysarea/0.4))), 180, sysfd, current_soilK]
        return parameter_list

    def prepareParametersIS(self, curSys, current_soilK):
        """Function to setup the parameter list vector for infiltration systems"""
        #parameter_list = [surface area, EDD, filter area, unlined perimeter, filterdepth, exfiltration]
        sysqty = self.getSystemQuantity(curSys)
        sysedd = float(curSys.getAttribute("WDepth"))
        sysarea = self.getEffectiveSystemArea(curSys)*sysqty
        sysfd = float(curSys.getAttribute("FDepth"))
        parameter_list = [sysarea,sysedd,sysarea, (2*numpy.sqrt(sysarea/0.4)+2*sysarea/(numpy.sqrt(sysarea/0.4))), sysfd, current_soilK]
        return parameter_list

    def prepareParametersWSUR(self, curSys, current_soilK):
        """Function to setup the parameter list vector for Surface Wetlands"""
        #parameter_list = [surface area, EDD, permanent pool, exfil, eq pipe diam, det time]
        sysqty = self.getSystemQuantity(curSys)
        sysarea = self.getEffectiveSystemArea(curSys)*sysqty
        sysedd = float(curSys.getAttribute("WDepth"))
        try:
            parameter_list = [sysarea, sysedd, sysarea*0.2, current_soilK, 1000.0*numpy.sqrt(((0.895*sysarea*sysedd)/(72*3600*0.6*0.25*numpy.pi*numpy.sqrt(2*9.81*sysedd))))]
        except TypeError as e:
            print e
            print "SysArea", type(sysarea)
            print "SysEdd", type(sysedd)
            print "SysQty", sysqty
            print "Soil", current_soilK
            print "Part 1", sysarea*sysedd*0.895
            print "Part 2", 72*3600*0.6*0.25*numpy.pi
            print "Part 3", numpy.sqrt(2*9.81*sysedd)
            print "Big Thing", 1000.0*numpy.sqrt(((0.895*sysarea*sysedd)/(72*3600*0.6*0.25*numpy.pi*numpy.sqrt(2*9.81*sysedd))))

        if curSys.getAttribute("IntegStore") == 1 and curSys.getAttribute("StoreVol") != 0:
            parameter_list.append(0)
            parameter_list.append(curSys.getAttribute("SvRec_Supp")/1000.0)
        else:
            parameter_list.append(1)
            parameter_list.append(-9999)
        return parameter_list

    def prepareParametersPB(self, curSys, current_soilK):
        """Function to setup the parameter list vector for Ponds & Basins"""
        #parameter_list = [surface area, mean depth, permanent pool, exfil, eq pipe diam, det time]
        sysqty = self.getSystemQuantity(curSys)
        sysarea = self.getEffectiveSystemArea(curSys)*sysqty
        sysedd = float(curSys.getAttribute("WDepth"))      #The mean depth
        parameter_list = [sysarea, sysedd, sysarea*0.2, current_soilK, 1000*numpy.sqrt(((0.895*sysarea*sysedd)/(72*3600*0.6*0.25*numpy.pi*numpy.sqrt(2*9.81*sysedd))))]

        if curSys.getAttribute("IntegStore") == 1 and curSys.getAttribute("StoreVol") != 0:
            parameter_list.append(0)    #Use stored water for irrigation or other uses? 0=Yes, 1=No
            parameter_list.append(curSys.getAttribute("SvRec_Supp")/1000.0)
        else:
            parameter_list.append(1)        #No storage reuse
            parameter_list.append(-9999)
        return parameter_list

    def prepareParametersSW(self, curSys, current_soilK):
        """Function to setup the parameter list vector for swales"""
        #parameter_list = [length, bedslope, Wbase, Wtop, depth, veg.height, exfilrate]
        sysqty = self.getSystemQuantity(curSys)
        sysarea = self.getEffectiveSystemArea(curSys)*sysqty
        parameter_list = [sysarea/4, 5, 2, 6, float(1.0/3.0),0.05, current_soilK]
        return parameter_list

    def prepareParametersRT(self, curSys, current_soilK):
        """Calls prepareParametersRTStore() since it is identical for Rainwater Tanks"""
        return self.prepareParametersRTStore(curSys, current_soilK)

    def prepareParametersRTStore(self, curSys, current_soilK):
        """Function to setup the parameter list vectr for raintanks"""
        #parameter_list = [annualdemand, numtanks, surfarea, totVol, initvol, overflowpipediam]
        numtanks = self.getSystemQuantity(curSys)
        storeVol = float(curSys.getAttribute("StoreVol")) * numtanks
        storeDepth = float(curSys.getAttribute("ST_Depth"))
        surfarea = float(storeVol / storeDepth)
        totVol = storeVol + float(surfarea*curSys.getAttribute("ST_Dead")) #store Volume + dead storage
        annualdemand = float(curSys.getAttribute("SvRec_Supp")*numtanks)/1000.0   #kL/yr --> ML/yr
        initvol = 0
        overflowpipediam = math.sqrt(math.pow(100.0/2.0,2)*numtanks)*2.0    #Rescale Raintank Diameter

        parameter_list = [annualdemand, numtanks, surfarea, totVol, initvol, overflowpipediam]
        return parameter_list

    def prepareParametersPBStore(self, curSys, current_soilK):
        """Function to setup the parameter list vector for ponds as a storage system"""
        #Parameter List = [
        sysqty = self.getSystemQuantity(curSys)
        sysvol = float(curSys.getAttribute("StoreVol"))
        storeDepth = float(curSys.getAttribute("ST_Depth"))
        surfarea = float(sysvol / storeDepth)
        ppd = float(curSys.getAttribute("ST_Dead"))
        annualdemand = float(curSys.getAttribute("SvRec_Supp"))
        parameter_list = [surfarea, storeDepth, surfarea * 0.2, current_soilK, 1000 * numpy.sqrt(
            ((0.895 * surfarea * storeDepth) / (72 * 3600 * 0.6 * 0.25 * numpy.pi * numpy.sqrt(2 * 9.81 * storeDepth)))), 0, annualdemand]
        return parameter_list

    def getEffectiveSystemArea(self, curSys):
        """Returns the effective system area of a given curSys input WSUD system
        equal to the total area divided by the effective area factor, both saved as attributes
        in the Attribue Object"""
        sysarea = float(curSys.getAttribute("SysArea"))/float(curSys.getAttribute("EAFact"))
        return sysarea

    def getSystemQuantity(self, curSys):
        """Gets the number of systems present in the plan. This is most relevant for lot-scale
        systems as these occur in multiple quantities. Systems are summed up in the MUSIC file
        as a single equivalent node for that scale."""
        if self.masterplanmodel:
            return float(int(curSys.getAttribute("GoalQty")))
        else:
            return float(int(curSys.getAttribute("Qty")))