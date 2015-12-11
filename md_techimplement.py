# -*- coding: utf-8 -*-
"""
@file
@author Peter M Bach <peterbach@gmail.com>
@version 1.0
@section LICENSE

This file is part of UrbanBEATS
Copyright (C) 2013 Peter M Bach

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
"""

from md_techimplementguic import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *
#from pydynamind import *
import math
import urbanbeatsdatatypes as ubdata    #UBCORE
from urbanbeatsmodule import *      #UBCORE
import numpy as np

class Techimplement(UBModule):
    """Loads the Blocks and Patches Shapefile and transfers all relevant information into
    a suitable data management structure for use in urbplanbb and other modules
    Inputs: Either project path or exact filename
    - Obtain file directly from a filename or from an ongoing simulation? - Boolean
    Filename: specify path
    Ongoing simulation: specify project path (it is likely the program will load a text file with information on how to grab the shapefile)
    Outputs: Vector Data containing block attributes (these are used in later modules as a comparison with the newly entered data)
    Log of Updates made at each version:
    
    v1.00 (June 2013):
        - full update of module features
        - compatbility with new v1.00 modules
    
    v0.80 (July 2012):
        - First created.

    @ingroup UrbanBEATS
    @author Peter M Bach
    """
    
    def __init__(self, activesim, tabindex):
        UBModule.__init__(self)
        self.cycletype = "ic"       #UBCORE: contains either planning or implementation (so it knows what to do and whether to skip)
        self.tabindex = tabindex        #UBCORE: the simulation period (knowing what iteration this module is being run at)
        self.activesim = activesim      #UBCORE

        #IMPLEMENTATION RULES TAB
        self.createParameter("dynamic_rule", STRING,"")
        self.dynamic_rule = "B" #B = Block-based, P = Parcel-based
        
        #Block-based Rules
        self.createParameter("block_based_thresh", DOUBLE, "")
        self.createParameter("bb_lot_rule", STRING, "")
        self.createParameter("bb_street_zone", BOOL, "")
        self.createParameter("bb_neigh_zone", BOOL, "")
        self.block_based_thresh = 30    #Threshold for implementation, % exceeded
        self.bb_lot_rule = "AMAP"       #AMAP = as many as possible, STRICT = strictly abide by %
        self.bb_street_zone = 1         #implement even if area hasn't been zoned yet
        self.bb_neigh_zone = 1          #implement even if neigh area hasn't been zoned yet
        
        self.createParameter("pb_lot_rule", STRING,"")
        self.createParameter("pb_street_rule", STRING,"")
        self.createParameter("pb_neigh_rule", STRING,"")
        self.createParameter("pb_neigh_zone_ignore",BOOL,"")
        self.pb_lot_rule = "G" #G = gradual, I = immediate, D = delayed
        self.pb_street_rule = "G"
        self.pb_neigh_rule = "G"
        self.pb_neigh_zone_ignore = 0
        
        self.createParameter("prec_rule", STRING,"")
        self.createParameter("prec_zone_ignore", BOOL,"")
        self.createParameter("prec_dev_threshold", BOOL,"")
        self.createParameter("prec_dev_percent", DOUBLE,"")
        self.prec_rule = "G"
        self.prec_zone_ignore = 0
        self.prec_dev_threshold = 0
        self.prec_dev_percent = 50
        
        #DRIVERS TAB - NOT ACTIVE YET, BUT PARAMETER LIST IS DEFINED FOR NOW
        self.createParameter("driver_people", BOOL,"")
        self.createParameter("driver_legal", BOOL,"")
        self.createParameter("driver_establish", BOOL,"")
        self.driver_people = 0
        self.driver_legal = 0
        self.driver_establish = 0
    
        ### ADVANCED PARAMETERS ######
        self.createParameter("currentyear", DOUBLE, "")
        self.createParameter("startyear", DOUBLE, "")
        self.currentyear = 1960
        self.startyear = 1960
        
        self.scale_matrix = ["L", "S", "N", "P"]

        
    def run(self):
        currentyear = self.currentyear  #Tracking years in the dynamic simulation
        startyear = self.startyear

        #Get global map attributes
        #strvec = city.getUUIDsOfComponentsInView(self.mapattributes)
        #map_attr = city.getComponent(strvec[0])
        map_attr = self.activesim.getAssetWithName("MapAttributes")

        #Find out how many systems are in the list of systems to be implemented
        #strvec = city.getUUIDsOfComponentsInView(self.sysGlobal)
        #totsystems = city.getComponent(strvec[0]).getAttribute("TotalSystems")
        totsystems = self.activesim.getAssetWithName("SysPrevGlobal").getAttribute("TotalSystems")

        self.notify("Total Systems in map: "+str(totsystems))
        
        #Get block number, etc.
        blocks_num = map_attr.getAttribute("NumBlocks") #number of blocks to loop through
        blocks_size = map_attr.getAttribute("BlockSize") #size of block

        #Get all systems for current block, also do a double-check on system location
        blockXY = self.getBlockXYcentres(blocks_num)
        sysList = {}
        for i in range(int(blocks_num)):
            sysList[i+1] = []   #Initialize the vector
        #sysuuids = city.getUUIDsOfComponentsInView(self.sysAttr)
        sysuuids = self.activesim.getAssetsWithIdentifier("SysPrevID")
        for curSys in sysuuids:
            location = int(curSys.getAttribute("Location"))
            if location == 0:
                posX = curSys.getAttribute("posX")
                posY = curSys.getAttribute("posY")
                location = self.determineSystemBlockLocation(posX, posY, blockXY, blocks_size)
            if self.skipIfStatusZero(location):
                continue        #If system is not within simulation bounds i.e. active blocks, skip
            else:
                sysList[int(location)].append(curSys)  #Append the UUID for the current matrix
                
        #self.notify(sysList)
        
        #Begin looping across blocks
        for i in range(int(blocks_num)):
            currentID = i + 1
            currentAttList = self.activesim.getAssetWithName("BlockID"+str(currentID))

            #-----------------------------------------------------------------#
            # DETERMINE WHETHER TO IMPLEMENT IN CURRENT BLOCK AT ALL #
            #-----------------------------------------------------------------#
            ### QUIT CONDITION #1 - BLOCK STATUS = 0 ###
            if self.skipIfStatusZero(currentID):
                continue

            ### QUIT CONDITION #2 - NO SYSTEMS PLANNED FOR BLOCK AT ALL ###
            #print sysList
            syscount = len(sysList[currentID])
            if syscount == 0:
                continue

            masterplanAttList = self.activesim.getAssetWithName("PrevID"+str(currentID))

            ### QUIT CONDITION #3 - DYNAMIC-MODE = Block-based and DEVELOPMENT < Threshold ###
            if self.dynamic_rule == "B":
                block_skip = self.skipIfBelowBlockThreshold(currentID, float(self.block_based_thresh/100))
                #use block_skip to determine whether to skip the next few steps
 
            self.notify("BlockID"+str(currentID)+" has systems to be implemented")
            
            #LOOP ACROSS SYSTEMS IN THE sysList and implement them if necessary
            for sys in sysList[currentID]:
                if sys.getAttribute("Scale") in ["L_RES"]:
                    qty, curImpT, year = self.implementLotSystem(currentAttList, masterplanAttList, sys)
                    if qty != 0 or year != self.currentyear:
                        self.writeSystemAttributesToOutput(sys, year, qty, curImpT, currentAttList, blocks_size)
                    
                elif sys.getAttribute("Scale") in ["L_COM", "L_HDR", "L_LI", "L_HI"]:
                    qty, curImpT, year = self.implementLotSystem(currentAttList, masterplanAttList, sys)
                    if qty != 0 or year != self.currentyear:
                        self.writeSystemAttributesToOutput(sys, year, qty, curImpT, currentAttList, blocks_size)
                    
                elif sys.getAttribute("Scale") in ["S", "N"]:
                    curImpT, year = self.implementStreetNeighSystem(currentAttList, masterplanAttList, sys)
                    if curImpT != 0 or year != self.currentyear:
                        self.writeSystemAttributesToOutput(sys, year, 1, curImpT, currentAttList, blocks_size)
                    
                elif sys.getAttribute("Scale") in ["B"]:
                    curImpT, year = self.implementBasinSystem(currentAttList, masterplanAttList, sys)
                    if curImpT != 0 or year != self.currentyear:
                        self.writeSystemAttributesToOutput(sys, year, 1, curImpT, currentAttList, blocks_size)
            
            #BLOCK FOR LOOP END (Repeat for next BlockID)
            
        self.notify("End of Implementation Module")

    ########################################################
    #TECHIMPLEMENT FUNCTIONS                               #
    ########################################################
    def skipIfStatusZero(self, ID):
        """Determines if the current BlockID's status is 1 or 0, if 0 transfers all its data
        to the output vector and returns true. If main function receives true"""
        if self.activesim.getAssetWithName("BlockID"+str(ID)).getAttribute("Status")==0:
            self.notify("BlockID"+str(ID)+" is not active in simulation")
            return True
        else:
            return False
    
    def getBlockXYcentres(self, blocks_num):
        """Scans the array of Blocks and creates an XY vector of block coordinates"""
        blockXY = {}
        for i in range(int(blocks_num)):
            currentID = i+1
            currentAttList = self.activesim.getAssetWithName("BlockID"+str(currentID))
            #currentAttList = self.getBlockUUID(currentID, city)
            cX = currentAttList.getAttribute("CentreX")
            cY = currentAttList.getAttribute("CentreY")
            blockXY[currentID] = [cX, cY]
        return blockXY

    def determineSystemBlockLocation(self, posX, posY, blockXY, block_size):
        """Returns the BlockID, where the system is located. If no BlockID was found,
        returns 0"""
        for i in blockXY.keys():    #Loop across blockIDs
            xmin = blockXY[i][0] - block_size/2     #Xmin is centre minus half the block size
            xmax = xmin + block_size        #max is min + block size
            ymin = blockXY[i][1] - block_size/2    
            ymax = ymin + block_size
            if posX > xmin and posX < xmax:
                if posY > ymin and posY < ymax:
                    return int(i)        #Found the BlockID
        return 0
    
    def skipIfBelowBlockThreshold(self, ID, threshold):
        undevland = self.activesim.getAssetWithName("BlockID"+str(ID)).getAttribute("pLU_UND")
        undevprev = self.activesim.getAssetWithName("PrevID"+str(ID)).getAttribute("pLU_UND")
        #undevland = self.getBlockUUID(ID, city).getAttribute("pLU_UND")
        #undevprev = self.getPrevBlockUUID(ID, city).getAttribute("pLU_UND") #This is the final value
        devtot = 1 - undevprev  #Developed = Masterplan, i.e. once 1-%UND has been developed
        if ((1-undevland)/devtot) < threshold:
            #If the developmed land (according to masterplan) has reached a threshold for development, implement
            return True
        else:
            return False        #Otherwise skip
    
    def writeSystemAttributesToOutput(self, sys, year, qty, currentImpT, currentAttList, block_size):
        """Writes the attributes to module output of the systems implemented"""
        centreX = currentAttList.getAttribute("CentreX")
        centreY = currentAttList.getAttribute("CentreY") 
        currentID = int(currentAttList.getAttribute("BlockID"))
        
        offsets_matrix = [[centreX+float(block_size)/16.0, centreY+float(block_size)/4.0],
                          [centreX+float(block_size)/12.0, centreY+float(block_size)/4.0],
                          [centreX+float(block_size)/8.0, centreY+float(block_size)/4.0],
                          [centreX+float(block_size)/4.0, centreY+float(block_size)/4.0],
                          [centreX+float(block_size)/3.0, centreY+float(block_size)/4.0],
                          [centreX+float(block_size)/4.0, centreY-float(block_size)/8.0],
                          [centreX-float(block_size)/8.0, centreY-float(block_size)/4.0],
                          [centreX-float(block_size)/4.0, centreY-float(block_size)/8.0]]
        blockscale_names = ["L_RES", "L_HDR", "L_LI", "L_HI", "L_COM", "S", "N", "B"]
        
        coordinates = offsets_matrix[blockscale_names.index(sys.getAttribute("Scale"))]
        
        #WRITE THE ATTRIBUTES
        sysAttr = ubdata.UBComponent()
        sysAttr.addAttribute("StrategyID", int(sys.getAttribute("StrategyID")))
        sysAttr.addAttribute("posX", coordinates[0])
        sysAttr.addAttribute("posY", coordinates[1])
        sysAttr.addAttribute("BasinID", int(sys.getAttribute("BasinID")))
        sysAttr.addAttribute("Location", currentID)
        sysAttr.addAttribute("Scale", sys.getAttribute("Scale"))
        sysAttr.addAttribute("Type", sys.getAttribute("Type"))
        sysAttr.addAttribute("Qty", qty)      #Currently none available
        sysAttr.addAttribute("GoalQty", sys.getAttribute("GoalQty"))  #lot scale mainly - number of lots to build
        sysAttr.addAttribute("SysArea", sys.getAttribute("SysArea"))
        sysAttr.addAttribute("Status", 1)   #0 = not built, 1 = built
        sysAttr.addAttribute("Year", int(year))
        sysAttr.addAttribute("EAFact", sys.getAttribute("EAFact"))
        sysAttr.addAttribute("ImpT", sys.getAttribute("ImpT"))
        sysAttr.addAttribute("CurImpT", currentImpT)
        sysAttr.addAttribute("Upgrades", sys.getAttribute("Upgrades")) #Done in the retrofit/implementation part
        sysAttr.addAttribute("WDepth", sys.getAttribute("WDepth")) #Done in the retrofit/implementation part
        sysAttr.addAttribute("FDepth", sys.getAttribute("FDepth")) #Done in the retrofit/implementation part
        sysAttr.addAttribute("Exfil", sys.getAttribute("Exfil")) #Done in the retrofit/implementation part
        #city.addComponent(sysAttr, self.techimplAttr)
        sysID = len(self.activesim.getAssetsWithIdentifier("SysID"))+1
        self.activesim.addAsset("SysID"+str(sysID), sysAttr)
        return True
    
    def implementLotSystem(self, currentAttList, masterAttList, sys):
        """Performs the checks to determine whether a residential lot system can be
        implemented in the current block using current Block data and masterplan
        data."""
        #GoalQty for different land uses:
            #-RES - allotments or houses
            #-HDR - always 1, it's a yes/no implementation
            #-LI - always implemented in all estates, but can only be done if they're built
            #-HI - same as LI
            #-COM - same as LI
        #print sys.getAttribute("Scale")
        if sys.getAttribute("Scale") == "L_RES":
            unitEIA = currentAttList.getAttribute("ResLotEIA")
            if sys.getAttribute("Type") in ["BF", "IS"]:    #Pick the correct units to use
                units = currentAttList.getAttribute("ResAllots")        #Allotments
                masterUnits = masterAttList.getAttribute("ResAllots")
            elif sys.getAttribute("Type") in ["RT"]:
                units = currentAttList.getAttribute("ResHouses")        #Houses
                masterUnits = masterAttList.getAttribute("ResHouses")
        elif sys.getAttribute("Scale") == "L_LI":
            unitEIA = currentAttList.getAttribute("LIAeEIA")
            units = currentAttList.getAttribute("LIestates")
            masterUnits = masterAttList.getAttribute("LIestates")
        elif sys.getAttribute("Scale") == "L_HI":
            unitEIA = currentAttList.getAttribute("HIAeEIA")
            units = currentAttList.getAttribute("HIestates")
            masterUnits = masterAttList.getAttribute("HIestates")
        elif sys.getAttribute("Scale") == "L_COM":
            unitEIA = currentAttList.getAttribute("COMAeEIA")
            units = currentAttList.getAttribute("COMestates")
            masterUnits = masterAttList.getAttribute("COMestates")
        elif sys.getAttribute("Scale") == "L_HDR":
            unitEIA = currentAttList.getAttribute("HDR_EIA")
            units = currentAttList.getAttribute("HasFlats")             #Simple yes/no
            masterUnits = masterAttList.getAttribute("HasFlats")
        #print masterUnits
        if units == 0:
            self.notify("Current Block has no units for that particular land use to implement on")
            return 0,0,0
        
        goallots = sys.getAttribute("GoalQty")      #Saved from Techplacement
        if goallots == 0:
            return 0,0,0    #No implementation specified, not even going to try
        
        if int(sys.getAttribute("Year")) == 9999:       #System not even built yet
            if self.bb_lot_rule == "AMAP":
                #As many as possible, the smaller of what the goal is or how many allotments have been built
                lotqty = min(goallots, units)      #The smaller of the two
                year = int(self.currentyear)
            elif self.bb_lot_rule == "STRICT":
                #Maintain ratio as development is built
                lotqty = min(goallots, (goallots/masterUnits) * units)   #Envisioned ratio x current number of units
                year = int(self.currentyear)
                
        elif int(sys.getAttribute("Year")) != 9999:     #Code is duplicated in case of future algorithms
            remainingQty = max(goallots - sys.getAttribute("Qty"),0)
            if remainingQty > 0 and self.bb_lot_rule == "AMAP":
                lotqty = min(goallots, units)
                year = int(self.currentyear)
                
            elif remainingQty > 0 and self.bb_lot_rule == "STRICT":
                lotqty = min(goallots, (goallots/masterUnits) * units)   #New systems
                year = int(self.currentyear)
                
            elif remainingQty <= 0:
                lotqty = goallots
                year = int(sys.getAttribute("Year"))
        
        #SPACE FOR FUTURE DECISION VARIABLES
        currentImpT = lotqty * sys.getAttribute("ImpT")
        return lotqty, currentImpT, year
    
    
    def implementStreetNeighSystem(self, currentAttList, masterAttList, sys):
        """Performs the checks to determine whether a street or neighbourhood-scale
        system can be implemented in the current block using current Block data and
        masterplan data."""
        
        if int(sys.getAttribute("Status")) == 1:    #Only for S and N systems
            #Transfer attributes as is
            curImpT = sys.getAttribute("CurImpT")
            year = int(sys.getAttribute("Year"))
            return curImpT, year
        #If status == 0, then buildyear is also 9999
        
        #CRITERIA 1 - Check available space
        if sys.getAttribute("Scale") == "S":
            avl_space = currentAttList.getAttribute("avSt_RES")
        elif sys.getAttribute("Scale") == "N":
            if sys.getAttribute("Type") in ["BF", "WSUR", "PB", "IS"]:
                avl_space = currentAttList.getAttribute("PG_av") + \
                    currentAttList.getAttribute("REF_av")
        
        sysarea = sys.getAttribute("SysArea")
        if sys.getAttribute("Scale") == "S":
            if self.bb_street_zone == 0 and avl_space < sysarea:
                return 0,0
        elif sys.getAttribute("Scale") == "N":
            if self.bb_neigh_zone == 0 and avl_space < sysarea:
                return 0,0
        
        #CRITERIA X - Future Criteria for deciding on implementation
        
        #CRITERIA 2 - Check development Status
        if sys.getAttribute("Scale") == "S":
            devarea = currentAttList.getAttribute("ResLotEIA") * \
                currentAttList.getAttribute("ResAllots")
            masterplan = currentAttList.getAttribute("ResLotEIA") * \
                currentAttList.getAttribute("ResAllots")
            if devarea/masterplan < float(self.block_based_thresh/100):
                return 0,0
            else:
                year = self.currentyear
                curImpT = sys.getAttribute("ImpT")
                return curImpT, year
        elif sys.getAttribute("Scale") == "N":
            #Develop. Have already checked the block threshold for the Neighbourhood
            year = self.currentyear
            curImpT = sys.getAttribute("ImpT")
            return curImpT, year
        return 0,0
    
    def implementBasinSystem(self, currentAttList, masterAttList, sys):
        """Performs the checks to determine whether a sub-basin scale technology can be
        implemented in the current Block using current Block data and masterplan data"""
        if int(sys.getAttribute("Status")) == 1:    #Only for S and N systems
            #Transfer attributes as is
            curImpT = sys.getAttribute("CurImpT")
            year = int(sys.getAttribute("Year"))
            self.notify("This system already is implemented")
            return curImpT, year
        #If status == 0, then buildyear is also 9999
        
        #CRITERIA 1 - Check available space
        if sys.getAttribute("Type") in ["BF", "WSUR", "PB", "IS"]:
            avl_space = currentAttList.getAttribute("PG_av") + \
                currentAttList.getAttribute("REF_av")
        
        sysarea = sys.getAttribute("SysArea")
        if self.prec_zone_ignore == 0 and avl_space < sysarea:
            return 0,0
        
        #CRITERIA X - Future space for further criteria
        
        #CRITERIA 2 - Check development status of upstream area
        curUD, mastUD = self.retrieveUndevelopedAreas(currentAttList, masterAttList, "upstream")
        if self.prec_dev_threshold == True: 
            if (1-curUD)/(1-mastUD) < float(self.prec_dev_percent/100):
                #self.notify("Upstream area not developed enough, skipping..."
                return 0,0
        
        #If the models makes it to this point, then the system is implemented
        year = self.currentyear
        curImpT = sys.getAttribute("ImpT")
        return curImpT, year

    def retrieveUndevelopedAreas(self, currentAttList, prevAttList, direction):
        """Retrieves the proportion of undeveloped area in all upstream blocks including
        the current block being implemented with WSUD. Returns current and masterplan
        proportions."""
        if direction == "upstream":
            attname = "UpstrIDs"
        elif direction == "downstream":
            attname = "DownstrIDs"
        
        streamstring = currentAttList.getAttribute(attname)
        streamIDs = streamstring.split(',')
        streamIDs.remove('')
        
        for i in range(len(streamIDs)):
            streamIDs[i] = int(streamIDs[i])
        if len(streamIDs) == 0:
            return 0
        
        undevarea = currentAttList.getAttribute("pLU_UND") * \
            currentAttList.getAttribute("Active") 
        mastplanundev = prevAttList.getAttribute("pLU_UND") * \
            prevAttList.getAttribute("pLU_UND")
        activetrack = currentAttList.getAttribute("Active")
        
        for i in range(len(streamIDs)):
            self.notify(streamIDs[i])
            blockattr = self.activesim.getAssetWithName("BlockID"+str(streamIDs[i]))
            mastattr = self.activesim.getAssetWithName("PrevID"+str(streamIDs[i]))
            #blockattr = self.getBlockUUID(streamIDs[i], city)
            #mastattr = self.getPrevBlockUUID(streamIDs[i], city)
            undevarea += blockattr.getAttribute("pLU_UND") * \
                blockattr.getAttribute("Active")
            mastplanundev += mastattr.getAttribute("pLU_UND") * \
                mastattr.getAttribute("Active")
            activetrack += blockattr.getAttribute("Active")
        
        undevarea = undevarea/activetrack
        mastplanundev = mastplanundev/activetrack
        return undevarea, mastplanundev
        