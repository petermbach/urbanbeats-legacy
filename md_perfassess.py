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
import scipy.spatial as sps
from osgeo import ogr, osr
import pymusic, ubmusicwrite, ubepanet
import urbanbeatsdatatypes as ubdata

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

        #MUSIC TAB
        self.createParameter("musicversion", STRING, "Active MUSIC Version for file writing")
        self.createParameter("musicclimatefile", STRING, "Path to the .mlb climate file")
        self.createParameter("musicseparatebasin", BOOL, "Write separate .msf files per basin?")
        self.musicversion = 'Version 6'
        self.musicclimatefile = ""
        self.musicseparatebasin = 1

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

        self.createParameter("bf_tncontent", DOUBLE, "TN content of Bioretention filter media")
        self.createParameter("bf_orthophosphate", DOUBLE, "Orthophosphate content of filter media")
        self.bf_tncontent = 800.0
        self.bf_orthophosphate = 50.0

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

        #MICROCLIMATE TAB

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
        #self.createParameter("cp_kitchen", )
        self.cp_kitchen = [1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0]
        #self.createParameter("cp_shower", )
        self.cp_shower = [1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0]
        #self.createParameter("cp_toilet", )
        self.cp_toilet = [1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0]
        #self.createParameter("cp_laundry", )
        self.cp_laundry = [1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0]
        #self.createParameter("cp_irrigation", )
        self.cp_irrigation = [1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0]
        #self.createParameter("cp_com", )
        self.cp_com = [1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0]
        #self.createParameter("cp_ind", )
        self.cp_ind = [1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0]
        #self.createParameter("cp_publicirri", )
        self.cp_publicirri = [1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0]

        #EPANET integration variables
        self.createParameter("epanetintmethod", STRING, "")
        self.createParameter("epanet_scanradius", DOUBLE, "")
        self.createParameter("epanet_excludezeros", BOOL, "")
        self.createParameter("epanet_exportshp", BOOL, "")
        self.createParameter("epanet_inpfname", STRING, "")
        self.createParameter("runBaseInp", BOOL, "")
        self.createParameter("epanet_simtype", STRING, "")

        #VD = voronoi diagram, DT = delaunay triangulation, RS = radial scan, NN = nearest neighbour
        self.epanetintmethod = "VD"
        self.epanet_scanradius = 0.5  #only for radial scan method
        self.epanet_excludezeros = 1    #exclude all nodes with zero demand?
        self.epanet_exportshp = 1   #export a visual illustration of the spatial integration between blocks and network
        self.epanet_inpfname = ""   #input filename
        self.runBaseInp = 0         #run the base simulation? will rebuild the .inp file
        #STS = static sim, 24H = 24-hour, EPS = extended period sim (72hrs), LTS = long-term sim
        self.epanet_simtype = "STS"

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


        # ----------------------------------------------------------------------------


    def run(self):
        self.notify("Now Running Performance Assessment")

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
        map_attr = self.activesim.getAssetWithName("MapAttributes")     #fetches global map attributes
        blocks_num = map_attr.getAttribute("NumBlocks")
        blocks_size = map_attr.getAttribute("BlockSize")
        totalbasins = map_attr.getAttribute("TotalBasins")
        strats = map_attr.getAttribute("OutputStrats")

        if self.masterplanmodel:    #differentiate between planning and implementation models
            filesuffix = "PC"
        else:
            filesuffix = "IC"
            strats = 1

        self.notify("Total Basins: "+str(totalbasins))
        self.notify("Total Strategies: "+str(strats))

        #Define MUSIC Version
        if self.musicversion == "Version 6":
            pymusic.setMUSICversion(6)
        elif self.musicversion == "Version 5":
            pymusic.setMUSICversion(5)

        #Begin Writing MUSIC Files
        for s in range(int(strats)):
            currentStratID = s+1

            if self.musicseparatebasin:     #Determine if to write separate files or one single file
                musicbasins = totalbasins
            else:
                musicbasins = 1

            for b in range(int(musicbasins)):
                if self.musicseparatebasin:
                    systemlist = self.getWSUDSystemsForStratID(currentStratID, b+1)
                    basinblockIDs = self.getBlocksIDsForBasinID(b+1)
                    ufile = ubmusicwrite.createMUSICmsf(self.musicfilepathname,
                                                   self.musicfilename+"-ID"+str(currentStratID)+"-"+str(int(b+1))+"-"+str(self.currentyear)+filesuffix)
                else:
                    systemlist = self.getWSUDSystemsForStratID(currentStratID, 9999)
                    basinblockIDs = self.getBlocksIDsForBasinID(9999)
                    ufile = ubmusicwrite.createMUSICmsf(self.musicfilepathname,
                                                   self.musicfilename+"-ID"+str(currentStratID)+"-"+str(self.currentyear)+filesuffix)

                ubmusicwrite.writeMUSICheader(ufile, self.musicclimatefile)

                scalar = 10
                ncount = 1
                musicnodedb = {}       #contains the database of nodes for each Block

                for i in basinblockIDs:
                    currentID = i
                    currentAttList = self.activesim.getAssetWithName("BlockID"+str(currentID))
                    musicnodedb["BlockID"+str(currentID)] = {}
                    blocksystems = self.getBlockSystems(currentID, systemlist)
                    #self.notify(str(blocksystems))

                    blockX = currentAttList.getAttribute("CentreX")
                    blockY = currentAttList.getAttribute("CentreY")

                    #(1) WRITE CATCHMENT NODES - maximum possibility of 7 Nodes (Lot x 6, non-lot x 1)
                    #       Lot: RES, HDR, COM, LI, HI, ORC
                    #       Street/Neigh: x 1
                    if self.include_pervious:
                        catchment_parameter_list = [1, self.musicRR_soil, self.musicRR_field, 80,200, 1, 10, self.musicRR_rcr, self.musicRR_bfr, self.musicRR_dsr]
                        total_catch_area = (blocks_size * blocks_size) * currentAttList.getAttribute("Active") / 10000      #[ha]
                        total_catch_imparea = currentAttList.getAttribute("Blk_EIA")/10000
                        total_catch_EIF = (total_catch_imparea / total_catch_area)
                    else:
                        catchment_parameter_list = [1,120,30,80,200,1,10,25,5,0]
                        total_catch_area = currentAttList.getAttribute("Blk_EIA")/10000      #[ha]
                        total_catch_imparea = total_catch_area
                        total_catch_EIF = 1     #100% impervious

                    catchnodecount = self.determineBlockCatchmentNodeCount(blocksystems)
                    lotcount = catchnodecount - 1   #one less
                    lotareas, loteifs = self.determineCatchmentLotAreas(currentAttList, blocksystems)

                    nonlotarea = total_catch_area - sum(lotareas.values())
                    if self.include_pervious:
                        total_lot_imparea = 0.0
                        for j in lotareas.keys():
                            total_lot_imparea += lotareas[j] * loteifs[j]/100
                        nonlotimparea = total_catch_imparea - total_lot_imparea
                        if nonlotarea == 0:
                            nonloteia = 0.0
                        else:
                            nonloteia = nonlotimparea / nonlotarea
                    else:
                        nonlotarea = total_catch_imparea - sum(lotareas.values())
                        nonloteia = 100

                    if nonlotarea == 0:
                        self.notify("ISSUE: NONLOT AREA ZERO ON BLOCK: "+str(currentID))
                    ncount_list = []

                    lotoffset = 0
                    if catchnodecount > 1:
                        for j in lotareas.keys():       #Loop over lot catchments
                            if lotareas[j] == 0:
                                continue
                            ncount_list.append(ncount)
                            ubmusicwrite.writeMUSICcatchmentnode(ufile, currentID, j, ncount, (blockX-blocks_size/4+(lotoffset*blocks_size/12))*scalar, (blockY+blocks_size/4+(lotoffset*blocks_size/12))*scalar, lotareas[j], loteifs[j], catchment_parameter_list)
                            lotoffset += 1
                            musicnodedb["BlockID"+str(currentID)]["C_"+j] = ncount
                            ncount += 1

                        #Write Street/Neigh Catchment Node
                        ncount_list.append(ncount)
                        ubmusicwrite.writeMUSICcatchmentnode(ufile, currentID, "", ncount, (blockX-blocks_size/4)*scalar, (blockY)*scalar, nonlotarea, nonloteia, catchment_parameter_list)
                        musicnodedb["BlockID"+str(currentID)]["C_R"] = ncount
                        ncount += 1
                    else:
                        ncount_list.append(0)
                        ncount_list.append(ncount)
                        ubmusicwrite.writeMUSICcatchmentnode(ufile, currentID, "", ncount, (blockX-blocks_size/4)*scalar, (blockY)*scalar, total_catch_area, total_catch_EIF, catchment_parameter_list)
                        musicnodedb["BlockID"+str(currentID)]["C_R"] = ncount
                        ncount += 1

                    #(2) WRITE TREATMENT NODES
                    lotoffset = -1
                    for sys in blocksystems.keys():
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
                        offsets = self.getSystemOffsetXY(curSys, blocks_size)
                        sysKexfil = curSys.getAttribute("Exfil")
                        parameter_list = eval("self.prepareParameters"+str(curSys.getAttribute("Type"))+"(curSys, sysKexfil)")
                        eval("ubmusicwrite.writeMUSICnode"+str(systype)+"(ufile, currentID, scale, ncount, (blockX+offsets[0]+(addOffset*blocks_size/12))*scalar, (blockY+offsets[1]+(addOffset*blocks_size/12))*scalar, parameter_list)")
                        musicnodedb["BlockID"+str(currentID)]["S_"+scale] = ncount
                        ncount += 1

                    #(3) WRITE BLOCK JUNCTION
                    ncount_list.append(ncount)
                    offsets = self.getSystemOffsetXY("J", blocks_size)
                    if int(currentAttList.getAttribute("Outlet")) == 1:
                        self.notify("GOT AN OUTLET at BlockID"+str(currentID))
                        basinID = int(currentAttList.getAttribute("BasinID"))
                        jname = "OUT_Bas"+str(basinID)+"-BlkID"+str(currentID)
                        #self.notify(str(jname))
                    else:
                        jname = "Block"+str(currentID)+"J"
                    ubmusicwrite.writeMUSICjunction(ufile, jname, ncount, (blockX+offsets[0])*scalar, (blockY+offsets[1])*scalar)
                    musicnodedb["BlockID"+str(currentID)]["J"] = ncount
                    ncount += 1

                    #(4) WRITE ALL LINKS WITHIN BLOCK
                    nodelinks = self.getInBlockNodeLinks(musicnodedb["BlockID"+str(currentID)])
                    routeparams = ["Not Routed", 30, 0.25]
                    for link in range(len(nodelinks)):
                        ubmusicwrite.writeMUSIClink(ufile, nodelinks[link][0], nodelinks[link][1], routeparams)

                #(5) WRITE ALL LINKS BETWEEN BLOCKS
                for i in basinblockIDs:
                    currentID = i
                    currentAttList = self.activesim.getAssetWithName("BlockID"+str(currentID))
                    downID = int(currentAttList.getAttribute("downID"))
                    #Determine routing parameters
                    if self.include_route:
                        if self.musicRR_muskk_auto:
                            #Work out Muskingum k approximation based on block size and 1m/s flow
                            musk_K = max(int(float(blocks_size)/60.0), 3)
                        else:
                            musk_K = self.musicRR_muskk
                        routeparams = ["Routed", musk_K, self.musicRR_musktheta]
                    else:
                        routeparams = ["Not Routed", 30, 0.25]  #Defaults

                    if downID == -1 or downID == 0:
                        downID = int(currentAttList.getAttribute("drainID"))
                    if downID == -1 or downID == 0:
                        continue
                    if int(currentAttList.getAttribute("Outlet")) == 1:
                        continue
                    else:
                        #print musicnodedb
                        nodelink = self.getDownstreamNodeLink(musicnodedb["BlockID"+str(currentID)], musicnodedb["BlockID"+str(downID)])
                        ubmusicwrite.writeMUSIClink(ufile, nodelink[0], nodelink[1], routeparams)

                ubmusicwrite.writeMUSICfooter(ufile)
        return True

    def runEconomicAnalysis(self):
        """Conducts an economic analysis of the life cycle costs and a number of other factors based
        on the planned options
        """
        pass

        return True

    def runMicroclimateAnalysis(self):
        """ Undertakes land cover analysis followed by applying land surface and air temperature
        relationships to understand local microclimate of the current modelled urban environment.
        """
        pass

        return True

    def runWaterSupply(self):
        """ Conducts integration with EPANET and water supply modelling. Coming Soon. Subject of
        future research
        """
        map_attr = self.activesim.getAssetWithName("MapAttributes")     #fetches global map attributes
        blocks_num = map_attr.getAttribute("NumBlocks")
        blocks_size = map_attr.getAttribute("BlockSize")
        totalbasins = map_attr.getAttribute("TotalBasins")
        strats = map_attr.getAttribute("OutputStrats")

        if self.masterplanmodel:    #differentiate between planning and implementation models
            filesuffix = "PC"
        else:
            filesuffix = "IC"
            strats = 1

        self.notify("Total Basins: "+str(totalbasins))
        self.notify("Total Strategies: "+str(strats))

        #(1) - Demand Downscaling Data
        enduses = ["kitchen", "shower", "toilet", "laundry", "irrigation", "com", "ind", "publicirri"]
        for i in enduses:
            if eval("self."+i+"pat") == "SDD":
                map_attr.addAttribute("wdp_"+i, self.sdd)

            elif eval("self."+i+"pat") == "CDP":
                map_attr.addAttribute("wdp_"+i, self.cdp)
            elif eval("self."+i+"pat") == "OHT":
                map_attr.addAttribute("wdp_"+i, self.oht)
            elif eval("self."+i+"pat") == "AHC":
                map_attr.addAttribute("wdp_"+i, self.ahc)
            else:
                map_attr.addAttribute("wdp_"+i, eval("self.cp_"+i))

        #(2) - EPANET Link
        #Check for valid EPANET file, if not valid, do not run
        self.notify("Performing EPANET Link...")
        if not os.path.isfile(self.epanet_inpfname):
            self.notify("Warning, no valid EPANET simulation file found, skipping assessment")
            return True

        base_inpfile = ubepanet.readInpFile(self.epanet_inpfname)   #Load file data
        node_list = ubepanet.getDataFromInpFile(base_inpfile, "[COORDINATES]", "array")   #Get the nodes
        node_props = ubepanet.getDataFromInpFile(base_inpfile, "[JUNCTIONS]", "dict")       #Get the list of Junctinos
        print node_list
        print node_props
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
                        "PPubIrr": self.createPatternString(map_attr.getAttribute("wdp_publicirri"))}

            dem_list = self.adjustEPANETdemands(rev_node_list, nbrelation)
            print dem_list

        #Use the node block list to work out the new demands and rewrite the EPANET file
        if self.runBaseInp:
            self.rewriteEPANETbase(base_inpfile)

        self.writeUB_EPANETfile(base_inpfile, node_list, opt_list, times_list,
                                node_props, dem_list, pat_list)

        #Run the EPANET Simulations
        self.runEPANETsim()
        return True

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
            nbfilter = [nbrelation.keys()[j] for j in range(len(nbrelation.keys())) if str(i) in nbrelation.keys()[j]]
            if len(nbfilter) == 0:
                new_node_data[i] = nodedata
                node_dem.addAttribute("NodeID_"+str(i), [nodedata[1], nodedata[1]])
                continue

            #for all others grab block demand data and tally up
            nodedemand = self.calculateWeightedNodeDemand(nbrelation, nbfilter, "Blk_WD")
            # nodedemand = 0
            # for j in range(len(nbfilter)):
            #     bID = nbrelation[nbfilter[j]][1]
            #     bdata = self.activesim.getAssetWithName("BlockID"+str(bID))
            #     prop = nbrelation[nbfilter[j]][4]
            #     nodedemand += float(bdata.getAttribute("Blk_WD") * cf * prop)

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
                        "Blk_com", "Blk_ind","Blk_publicirri"]
        pattern_names = ["PKitch", "PShower", "PToilet", "PLaundry", "PGarden",
                         "PCom", "PInd", "PPubIrr"]

        new_demand_data = []

        for i in rev_node_list:
            curID = i[0]
            print curID
            nbfilter = [nbrelation.keys()[j] for j in range(len(nbrelation.keys())) if str(curID) in nbrelation.keys()[j]]
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
                        "Blk_com", "Blk_ind", "Blk_publicirri"]:
            cf = float(1000.0/(24.0*3600.0))     #kL/day into L/sec

        nodedemand = 0
        for j in range(len(nbfilter)):
            bID = nbrelation[nbfilter[j]][1]
            bdata = self.activesim.getAssetWithName("BlockID"+str(bID))
            prop = nbrelation[nbfilter[j]][4]
            nodedemand += float(bdata.getAttribute(enduse) * cf * prop)
        return nodedemand

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
                print area

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

    def rewriteEPANETbase(self, basedata):
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
                    f.write(str(nID)+"\t"+str(nIDd[0])+"\t"+str(nIDd[1])+"\t"+str(nIDd[2])+"\t"+"\n")
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
        loteifs = {"L_RES":100, "L_HDR":100,"L_LI":100,"L_HI":100,"L_COM":100,"L_ORC":100}

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
                                - junction to basin sys                 - remain catchment to junction if no sys"""
        nodelinks = []
        linkmap = {"C_L_RES": ["S_L_RES"], "C_L_HDR":["S_L_HDR"], "C_L_LI": ["S_L_LI"],
                   "C_L_HI": ["S_L_HI"], "C_L_COM": ["S_L_COM"], "C_L_ORC": ["S_L_ORC"],
                   "C_R": ["S_S", "S_N", "J"], "J": ["S_B", 0],
                   "S_L_RES": ["S_S", "S_N", "J"], "S_L_HDR": ["S_N", "J"], "S_L_LI": ["S_N", "J"],
                   "S_L_HI": ["S_N", "J"], "S_L_COM": ["S_N", "J"], "S_L_ORC": ["S_N", "J"],
                   "S_S": ["S_N", "J"], "S_N": ["J"], "S_B" : [0]}      #gives the order in which links can be arranged
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
        #Case 2: Basin to Junction
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
            parameter_list = [sysarea, sysedd, sysarea*0.2, current_soilK, 1000.0*numpy.sqrt(((0.895*sysarea*sysedd)/(72*3600*0.6*0.25*numpy.pi*numpy.sqrt(2*9.81*sysedd)))), 72.0]
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

        return parameter_list

    def prepareParametersPB(self, curSys, current_soilK):
        """Function to setup the parameter list vector for Ponds & Basins"""
        #parameter_list = [surface area, mean depth, permanent pool, exfil, eq pipe diam, det time]
        sysqty = self.getSystemQuantity(curSys)
        sysarea = self.getEffectiveSystemArea(curSys)*sysqty
        sysedd = float(curSys.getAttribute("WDepth"))      #The mean depth
        parameter_list = [sysarea, sysedd, sysarea*0.2, current_soilK, 1000*numpy.sqrt(((0.895*sysarea*sysedd)/(72*3600*0.6*0.25*numpy.pi*numpy.sqrt(2*9.81*sysedd)))), 72.0]
        return parameter_list

    def prepareParametersSW(self, curSys, current_soilK):
        """Function to setup the parameter list vector for swales"""
        #parameter_list = [length, bedslope, Wbase, Wtop, depth, veg.height, exfilrate]
        sysqty = self.getSystemQuantity(curSys)
        sysarea = self.getEffectiveSystemArea(curSys)*sysqty
        parameter_list = [sysarea/4, 5, 2, 6, float(1.0/3.0),0.05, current_soilK]
        return parameter_list

    def prepareParametersRT(self, curSys, current_soilK):
        """Function to setup the parameter list vectr for raintanks"""
        #>>>FUTURE
        parameter_list = []
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