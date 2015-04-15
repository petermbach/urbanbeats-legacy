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

import sys, random, numpy, math
import pymusic, ubmusicwrite

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

    def __init__(self, activesim, tabindex, cycletype):      #UBCORE
        UBModule.__init__(self)      #UBCORE
        self.cycletype = cycletype       #UBCORE: contains either planning or implementation (so it knows what to do and whether to skip)
        self.tabindex = tabindex        #UBCORE: the simulation period (knowing what iteration this module is being run at)
        self.activesim = activesim      #UBCORE

        #PARAMETER LIST START
        #-----------------------------------------------------------------------
        #SELECT ANALYSES TAB
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
        #                       AHC - after-hours constant, UDP - user-defined pattern
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

        self.ssd = [0.3,0.3,0.3,0.3,0.5,1.0,1.5,1.5,1.3,1.0,1.0,1.5,1.5,1.2,1.0,1.0,1.0,1.3,1.3,0.8,0.8,0.5,0.5,0.5]
        self.cdp = [1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0]
        self.ahc = [2.0,2.0,2.0,2.0,2.0,2.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,2.0,2.0,2.0,2.0,2.0,2.0]

        #Custom pattern variables if needed
        self.cp_kitchen = [1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0]
        self.cp_shower = [1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0]
        self.cp_toilet = [1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0]
        self.cp_laundry = [1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0]
        self.cp_irrigation = [1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0]
        self.cp_com = [1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0]
        self.cp_ind = [1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0]
        self.cp_publicirri = [1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0]

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
                        total_catch_area = (blocks_size * blocks_size) / 10000      #[ha]
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

        #Part 1 - Demand Downscaling Data





        return True

    def runIWCM(self):
        """ Creates a simulation file and calls the CityDrain3 Modelling Platform to undertake
        detailed performance assessment of the integrated urban water cycle from a quantity and
        quality perspective.
        """
        pass

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