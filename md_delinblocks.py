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
from md_delinblocksguic import *        #UBCORE
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import PyQt4
import math, time
import random as rand
import ubpatchdelin as ubpat
import ubconvertcoord as ubcc
import ubvectormapload as ubvmap
import urbanbeatsdatatypes as ubdata    #UBCORE
from urbanbeatsmodule import *      #UBCORE

class Delinblocks(UBModule):      #UBCORE
    """Processes information from either UrbanSim or four input biophysical rasters
    and an optional two social-economic rasters and creates a preliminary grid of
    building blocks. 
	
	A coarser resolution grid of the input raster is output
	- block
            contains N number of cells depending on user-specified resolution
            and input raster size, note that all four layers need to match up
            in size, this can be prepared in GIS software.
        - inputs:
            BlockSize = size of cell, model assumes square cells, specify size
                in metres [m]
	- code is split into two possible options based on whether the data is derived
            from UrbanSim or not.
    
    Log of Updates made at each version:
    
    v1.0 update (October 2012) - Post Dynamind Conversion:
        - Full revision and restructuring of parameter list for module, addition of new Regional Geography Parameters
        - Commenting out of UrbanSim Algorithms in the modules. These are not part of UrbanBEATS, but DAnCE4Water
        - Modularisation of entire module, patches, vector map loading and other features extracted as separated files
        - Implementation of all remaining features as indicated in the GUI (e.g. D-infinity, DEM smoothing, CBD info, loading of vector maps)
        - delinbasins.py code from previous versions has been integrated into this module, improved upon
            now runs 10 times faster
        - Most of the drawing algorithms are in their own separate functions, a lot of sub-procedures have been made their own functions
    
    v0.75 update (October 2011):
        - Added neighbourhood --> block searches all 8 neighbours to get IDs
        - Added terrain delineation --> D8 method only with edge drawing
        - Added additional inputs (planning map, locality map and road network map)
        - Cleaned up code a bit with extra headings and better differentiation between
          UrbanSim Forks and other code
        - Updated GUI with new inputs
        - Does Moore/vonNeumann differentiation now in block flow directions
        - Can account for sinks, but only within existing neighbourhood.
        - Writes attributes to the extracted drainage network
        - Receives and processes Planner's Map, mapping it onto the relevant land uses
        - Implemented calculation of four diversity metrics: richness, Shannon's Diversity, Dominance and Evenness
        Future work:
            - add processing of locality map
            - add processing of natural sink map
            - add processing of road network map
            - Make code more modular, perhaps splitting terrain delineation with rest
            - Implement hexagonal blocks
    
    v0.5 update (August 2011):
        - implemented UrbanSim forks, labelled in the code at five locations
        - implemented additional raster inputs: social parameters 1 and 2 with naming
          treats these as probabilities and returns the average probability for the area
        - processes either the land use, population rasters OR UrbanSim data
        - updated GUI for delinblocks to include UrbanSim and social parameter inputs
        
    v0.5 first (July 2011):
        - implemented block delineation algorithm for basic parameters
        - looks for von Neplan_mapumann neighbourhood and returns Block IDs, writes to Shp file output
        - draws the grid of blocks
        - designed GUI for delinblocks
	
	@ingroup UrbanBEATS
        @author Peter M Bach
        """
    
    def __init__(self, activesim, tabindex):      #UBCORE
        UBModule.__init__(self)      #UBCORE
        self.cycletype = "pc"       #UBCORE: contains either planning or implementation (so it knows what to do and whether to skip)
        self.tabindex = tabindex        #UBCORE: the simulation period (knowing what iteration this module is being run at)
        self.activesim = activesim      #UBCORE
       
        #PARAMETER LIST START
        #-----------------------------------------------------------------------
        
        #General Simulation Parameters
        self.createParameter("BlockSize", DOUBLE, "Block Size")
        self.createParameter("blocksize_auto", BOOL, "Autosize Blocks?")
        self.BlockSize = float(500)                    #size of the blocks (in m)
        self.blocksize_auto = 0             #should the size be chosen automatically?

        self.createParameter("popdatatype", STRING, "Population Data Format")         #DYNAMIND
        self.createParameter("soildatatype", STRING, "Soil Data Format")
        self.createParameter("soildataunits", STRING, "Units for Soil Data")
        self.createParameter("elevdatadatum", STRING, "Datum for Elevation Data")
        self.createParameter("elevdatacustomref", DOUBLE, "Custom Reference Elevation")
        self.createParameter("include_plan_map", BOOL ,"Include Planner's Map?")
        self.createParameter("include_local_map", BOOL,"Include Locality Map?")
        self.createParameter("include_employment", BOOL, "Include Employment Map?")
        self.createParameter("jobdatatype", STRING, "Job Data Format")
        self.createParameter("include_rivers", BOOL, "Include Rivers Map?")
        self.createParameter("include_lakes", BOOL, "Include Lakes Map?")
        self.createParameter("include_groundwater", BOOL, "Include Groundwater Map?")
        self.createParameter("groundwater_datum", STRING, "Groundwater Datum?")
        self.createParameter("include_drainage_net", BOOL, "")
        #self.createParameter("include_road_net", BOOL,"")
        self.createParameter("include_soc_par1", BOOL,"Include Social Parameters Map?")
        self.createParameter("include_soc_par2", BOOL,"Include a Second Social Parameters Map?")
        self.createParameter("social_par1_name", STRING,"Social Parameter 1 Name")
        self.createParameter("social_par2_name", STRING,"Social Parameter 2 Name")
        self.createParameter("socpar1_type", STRING, "Data format for Social Parameter 1")
        self.createParameter("socpar2_type", STRING, "Data format for Social Parameter 2")
        self.createParameter("patchdelin", BOOL, "Delineate Patches?")
        self.createParameter("spatialmetrics", BOOL, "Calculate Spatial Metrics?")

        self.popdatatype = "D"                  #population data type: D = density, C = count
        self.soildatatype = "C"                 #I = infiltration rates, C = classification
        self.soildataunits = "hrs"              #sec = m/s, hrs = mm/hr
        self.elevdatadatum = "S"                #S = sea level, C = custom
        self.elevdatacustomref = float(0.0)              #reference above sea level for custom elevation
        self.include_plan_map = 0           #planner's map displaying typology distributions
        self.include_local_map = 0          #locality map displaying location of centres
        self.include_employment = 0         #include employment data for industrial land uses?
        self.jobdatatype = "D"                  #employment data type: D = density, C = count
        self.include_rivers = 0             #include river systems
        self.include_lakes = 0              #include lake systems
        self.include_groundwater = 0        #include groundwater table
        self.groundwater_datum = "Sea"          #"Sea" = Sea level, "Surf" = Surface level

        self.include_drainage_net = False       # include water supply mains
        #self.include_road_net = False          #road network map not working yet
        #self.include_sewer_net = False        #include sewer mains
        
        self.include_soc_par1 = 0            #include a social parameter in the simulation?
        self.include_soc_par2 = 0            #include a social parameter in the simulation?
        self.social_par1_name = "unnamed1"      #name of social parameter1
        self.social_par2_name = "unnamed2"      #name of social parameter2
        self.socpar1_type = "B"                 #B = Binary, P = Proportionate
        self.socpar2_type = "B"
        
        self.patchdelin = 0                  #perform patch delineation? All subsequent algorithms will need to consider this
        self.spatialmetrics = 0              #perform calculation of spatial metrics? Just an additional feature
        
        #Local Extents and Map Connectivity
        self.createParameter("Neighbourhood", STRING,"Type of Neighbourhood")
        self.createParameter("vn4FlowPaths", BOOL,"Use vonNeumann Neighbourhood for Flow Paths?")
        self.createParameter("vn4Patches", BOOL,"Use vonNeumann Neighbourhood for Patches?")
        self.createParameter("flow_method", STRING,"Selected Flowpath Method")
        self.createParameter("demsmooth_choose", BOOL,"Smoothen DEM?")
        self.createParameter("demsmooth_passes", DOUBLE,"Number of Smoothing Passes for DEM")
        self.createParameter("use_river", BOOL, "Use river network data to determine flow paths?")
        self.createParameter("use_drainage", BOOL, "Use drainage network data to determine flow paths?")
        
        self.Neighbourhood = "M"                #three options: M = Moore, N = von Neumann
        self.vn4FlowPaths = 0
        self.vn4Patches = 0
        self.flow_method = "D8"                 #three options: DI = D-infinity (Tarboton), D8 = D8 (O'Callaghan & Mark) and MS = Divergent (Freeman)
        self.demsmooth_choose = 0
        self.demsmooth_passes = float(1)
        self.use_river = 0
        self.use_drainage = 0


        #Regional Geography
        self.createParameter("considerCBD", BOOL, "Consider CBD Location?")
        self.createParameter("locationOption", STRING, "Location Method")
        self.createParameter("locationCity", STRING, "City Name")
        self.createParameter("locationLong", DOUBLE, "CBD Longitude")
        self.createParameter("locationLat", DOUBLE, "CBD Latitude")
        self.createParameter("marklocation", BOOL, "Mark Location on Output Map?")
        
        self.considerCBD = 0
        self.locationOption = "S"       #method for setting location option: S = selection, C = coordinates
        self.locationCity = "Melbourne" #index of the combobox, it returns the city name in a different vector
        self.locationLong = float(0.0)           #longitude of the location
        self.locationLat = float(0.0)            #latitude of the location
        self.marklocation = 0       #should this CBD location be marked on the map as a point? If yes, it will be saved to the Block Centre Points
        
        #Hidden Inputs
        #self.createParameter("LocalityFilename", STRING, "")
        #self.createParameter("RiversFilename", STRING, "")
        #self.createParameter("LakesFilename", STRING, "")
        #self.createParameter("obtain_flowbasins", STRING, "")           #changed internally depending on cycle to skip flowpath delineation
        #self.LocalityFilename = "C:/UrbanBEATSv1CaseStudies/LocalityMap_UTM.shp"
        #self.RiversFilename = "C:/UrbanBEATSv1CaseStudies/Rivers_UTM.shp"
        #self.LakesFilename = "C:/UrbanBEATSv1CaseStudies/Lakes.shp"
        #self.obtain_flowbasins = "D"                                    #F = file, D = delineate
        
        #self.createParameter("xllcorner", DOUBLE, "")
        #self.createParameter("yllcorner", DOUBLE, "")
        #self.xllcorner = float(313420.7405)    #Yarra Estuary Limits
        #self.yllcorner = float(5807211.478)    #spatial extents of the input map

        self.xllcorner = float(0)    #Obtained from the loaded raster data (elevation) upon run-time
        self.yllcorner = float(0)    #spatial extents of the input map
        
        #-----------------------------------------------------------------------
        #END OF INPUT PARAMETER LIST

        self.elevation = 0            #<-- BASE INPUTS
        self.soil = 0
        self.landuse = 0
        self.population = 0
        self.plan_map = 0               #<-- ADDITIONAL INPUTS
        self.employment = 0          #rivers, lakes and localities are read externally
        self.groundwater = 0        #see HIDDEN PARAMETERS
        self.socpar1 = 0
        self.socpar2 = 0

        self.CBDcoordinates = {
                    "Adelaide" : [280780.0759095973, 6132244.023877329],
                    "Brisbane" : [502317.812981302, 6961397.420122750],
                    "Cairns" : [369106.391411321, 8128447.001515380],
                    "Canberra" : [693122.206993260, 6090719.284280210],
                    "Copenhagen" : [347093.425724650, 6172710.918933620],
                    "Innsbruck" : [681848.057202314, 5237885.440371720],
                    "Kuala Lumpur" : [799755.394164082, 348044.713410070],
                    "London" : [699324.171955045, 5710156.274752980],
                    "Melbourne" : [321467.336657357, 5813188.082041830],
                    "Munich" : [691723.398045385, 5334697.280393150],
                    "Perth" : [392423.697319843, 6466441.091644930],
                    "Singapore" : [372162.693079949, 141518.167286989],
                    "Sydney" : [334154.239302794, 6251091.03554923],
                    "Vienna" : [602067.456062062, 5340352.522405760]    }
        self.soildictionary = [180, 36, 3.6, 0.36]    #mm/hr - 1=sand, 2=sandy clay, 3=medium clay, 4=heavy clay

    def loadRaster(self, dataset, dtype):       #UBCORE FUNCTION
        self.notify("Loading "+str(dtype))
        rasterload = ubdata.importRasterData(dataset[str(dtype)])
        self.notify("Load "+str(dtype)+" "+dataset[str(dtype)]+" Complete")
        return rasterload
    
    def run(self):
        self.notify("StartDelinBlocks!")        #UBCORE
        rand.seed()


        cs = self.BlockSize             #set blocksize to a local variable with a short name cs = cell size
                
        if self.Neighbourhood == "N":           #Set neighbourhood Type
            neighbourhood_type = 4              #von Neumann = 4 neighbours
        else: 
            neighbourhood_type = 8              #Moore = 8 neighbours
        
        self.notify(self.BlockSize)        #UBCORE
        
        ## Retrieve the raster data UBCORE VERSION ###############################################################################
        ## 4 BASIC INPUTS ###
        cycledataset = self.activesim.getCycleDataSet(self.cycletype, self.tabindex)
        self.notify(str(cycledataset))
        elevationraster = self.loadRaster(cycledataset, "Elevation")   #ELEVATION AND SOIL DATA ARE NOT URBANSIM DEPENDENT!
        self.xllcorner = elevationraster.getExtents()[0] 
        self.yllcorner = elevationraster.getExtents()[1]    #spatial extents of the input map
        
        soilraster = self.loadRaster(cycledataset, "Soil")
        landuseraster = self.loadRaster(cycledataset, "Land Use")
        population = self.loadRaster(cycledataset, "Population")        
        
        ### 7 ADDITIONAL INPUTS ###
        #(1) - Planner's Map
        if self.include_plan_map: plan_map = self.loadRaster(cycledataset, "Planning")        
        else: plan_map = 0
       
        #(2) - Locality Map
        if self.include_local_map: localitymap = ubvmap.runLocalityImport(cycledataset["Locality"])
        else: localitymap = 0
        
        #(3) - Employment Map
        if self.include_employment: employment = self.loadRaster(cycledataset, "Employment")
        else: employment = 0
        
        #(4) - Rivers Map
        if self.include_rivers or self.use_river:
            riverpoints = ubvmap.runRiverImport(float(cs/4), cycledataset["Rivers"])
        else:
            riverpoints = 0
        
        #(5) - Lakes Map
        if self.include_lakes: lakepoints = ubvmap.runLakesImport(cycledataset["Lakes"])
        else: lakepoints = 0
        
        #(6) - Groundwater Map
        if self.include_groundwater: groundwater = self.loadRaster(cycledataset, "Groundwater")
        else: groundwater = 0
        
        #(7) - Social Parameters
        if self.include_soc_par1: socpar1 = self.loadRaster(cycledataset, "Social Parameters")
        else: socpar1 = 0
        #print "Socpar1", socpar1
        if self.include_soc_par2: socpar2 = self.loadRaster(cycledataset, "Social Parameters")
        else: socpar2 = 0
        #print "Socpar2", socpar2

        #(8) - Network Infrastructure
        if self.include_drainage_net or self.use_drainage:
            print "Loading Drainage network"
            drainagepoints = ubvmap.runRiverImport(float(cs/4), cycledataset["Existing Network"])
            print drainagepoints
            print len(drainagepoints)
        else:
            drainagepoints = 0

        #road_net, supply_net and sewer_net = coming in future versions

        ################################### END OF DATA RETRIEVAL UBCORE VERSION ##############################################
        
        inputres = landuseraster.getCellSize()                                #input data resolution [m]
        width =  elevationraster.getDimensions()[0] * elevationraster.getCellSize()     #UBCORE
        height =  elevationraster.getDimensions()[1] * elevationraster.getCellSize()   #UBCORE 

        xllcorner, yllcorner = landuseraster.getExtents()       #UBCORE
        #self.notify(elevationraster.getDimensions()[0])         #UBCORE
        #self.notify(str(width)+","+str(height))                 #UBCORE

        #####################################################################################                
        
        ### AUTO SIZE BLOCKS ###
        if self.blocksize_auto == True:
            cs = self.autosizeBlocks(width, height)
        else:
            cs = self.BlockSize                                                 #BlockSize stored locally [m]
        cellsinblock = int(cs/inputres)                                         #tells us how many smaller cells are in one length of block  
        
        #UBCORE ---------------->
        #self.notify("Width "+str(width))
        #self.notify("Height "+str(height))
        #self.notify("Block Size: "+str(cs))
        #self.notify("Cells in Block: "+str(cellsinblock))
        #------------------> UBCORE 
        
        #Note that the simulation area needs to have a larger width and larger height than the data input area!
        whfactor = 1 - (1/(cs*2))               #factor replaces the rounding function and speeds up computation
        widthnew = int(width/cs+whfactor)       #width of the simulation area (divide total width by block size and round) [#Blocks]
        heightnew = int(height/cs+whfactor)      #height of the simulation area (multiply block size with this to get actual length) [#Blocks]
        numblocks = widthnew * heightnew        #number of blocks based on how many blocks wide x how many blocks tall [#Blocks]
        
        ### MAP ATTRIBUTES - The Global Attributes List - write present information across to this component
        map_attr = ubdata.UBComponent()         #UBCORE
        map_attr.addAttribute("NumBlocks", numblocks)                   #Number of blocks in the grid
        map_attr.addAttribute("WidthBlocks", widthnew)                  #Width of simulation area in # of blocks
        map_attr.addAttribute("HeightBlocks", heightnew)                #Height of simulation area in # of blocks
        map_attr.addAttribute("BlockSize", cs)                          #Size of block [m]
        map_attr.addAttribute("InputReso", inputres)                    #Resolution of the input data [m]
        map_attr.addAttribute("xllcorner", xllcorner)
        map_attr.addAttribute("yllcorner", yllcorner)
        map_attr.addAttribute("Neigh_Type", neighbourhood_type) 
        map_attr.addAttribute("ConsiderCBD", self.considerCBD)
        map_attr.addAttribute("include_plan_map", self.include_plan_map)
        map_attr.addAttribute("include_local_map", self.include_local_map)
        map_attr.addAttribute("include_employment", self.include_employment)
        map_attr.addAttribute("include_rivers", self.include_rivers)
        map_attr.addAttribute("include_lakes", self.include_lakes)
        map_attr.addAttribute("include_groundwater", self.include_groundwater)
        map_attr.addAttribute("include_soc_par1", self.include_soc_par1)
        map_attr.addAttribute("include_soc_par2", self.include_soc_par2)
        map_attr.addAttribute("patchdelin", self.patchdelin)
        map_attr.addAttribute("spatialmetrics", self.spatialmetrics)
        map_attr.addAttribute("considerCBD", self.considerCBD)

        #Look up long and lat of CBD if need to be considered
        if self.considerCBD:
            #Grab CBD coordinates, convert to UTM if necessary
            cityeasting, citynorthing = self.getCBDcoordinates()        #EASTING = X, NORTHING = Y
            #delinblocks works at Global (0,0) then exports it and offsets the map. Hidden parameters xll and yllcorner deal with real extents
                                                                #to realign it with the original data
            map_attr.addAttribute("CBDLocationLong", cityeasting)
            map_attr.addAttribute("CBDLocationLat", citynorthing)
            
            #Use HIDDEN PARAMETERS FOR NOW
            
            #See if marklocation can be added
            #UBCORE ------------------>            
            if self.marklocation:
                city_pts = ubdata.UBVector([(cityeasting-self.xllcorner, citynorthing-self.yllcorner,0)])
                city_pts.addAttribute("BlockID", -1)     #-1 for CBD
                city_pts.addAttribute("AvgElev", -1)     #-1 for CBD
                city_pts.addAttribute("Type", "CBD")     #-1 for CBD
                self.activesim.addAsset("CPCityCentre", city_pts)
            #------------------> UBCORE 

        self.activesim.addAsset("MapAttributes", map_attr)                 #UBCORE: save Mapattribuets as an asset of the current simulation
        
        x_adj = 0               #these track the position of the 'draw cursor', these offset the cursor
        y_adj = 0               #can be used to offset the drawing completely from (0,0)
        
        ########################################################################
        ### DRAW BLOCKS AND ASSIGN INFO                                      ###
        ######################################################################## 
        blockIDcount = 1     #counts through Block ID, initialize this variable here
        for y in range(heightnew):              #outer loop scans through rows
            for x in range(widthnew):           #inner loop scans through columns

                self.notify("CURRENT BLOCK ID: "+str(blockIDcount))     #UBCORE)

                block_attr = self.createBlockFace(x, y, cs, x_adj, y_adj, blockIDcount)         #UBCORE
                
                xcentre = x*cs+0.5*cs       #Centre point               
                ycentre = y*cs+0.5*cs   
                       
                x_start = x*cellsinblock    #Bottom-left-hand corner (grid-numbering)
                y_start = y*cellsinblock
                
                xorigin = (x+x_adj)*cs
                yorigin = (y+y_adj)*cs
                
                block_attr.addAttribute("CentreX", xcentre)
                block_attr.addAttribute("CentreY", ycentre)
                block_attr.addAttribute("LocateX", x+1)
                block_attr.addAttribute("LocateY", y+1)
                block_attr.addAttribute("OriginX", xorigin)
                block_attr.addAttribute("OriginY", yorigin)
                offset = [(x+x_adj)*cs, (y+y_adj)*cs]
                
                ####################################################
                ### 1.1 DETERMINE BLOCK NEIGHBOURHOOD            ###
                ####################################################
                blockNHD = self.findNeighbourhood(blockIDcount, x, y, numblocks, widthnew, heightnew)
                block_attr.addAttribute("Nhd_N", blockNHD[0])             #North neighbour Block ID
                block_attr.addAttribute("Nhd_S", blockNHD[1])             #South neighbour Block ID
                block_attr.addAttribute("Nhd_W", blockNHD[2])             #West neighbour Block ID
                block_attr.addAttribute("Nhd_E", blockNHD[3])             #East neighbour Block ID
                block_attr.addAttribute("Nhd_NE", blockNHD[4])            #Northeast neighbour Block ID
                block_attr.addAttribute("Nhd_NW", blockNHD[5])            #Northwest neighbour Block ID
                block_attr.addAttribute("Nhd_SE", blockNHD[6])            #Southeast neighbour Block ID
                block_attr.addAttribute("Nhd_SW", blockNHD[7])            #Southwest neighbour Block ID
               
                
                ####################################################
                ### 1.2 CALCULATE DISTANCE FROM CBD IF NECESSARY ###
                ####################################################
                if self.considerCBD:
                    currenteasting = xcentre + self.xllcorner
                    currentnorthing = ycentre + self.yllcorner
                    
                    #Calculate distance and angle
                    dist = math.sqrt(math.pow((cityeasting-currenteasting),2)+math.pow((citynorthing-currentnorthing),2))
                    theta = math.degrees(math.atan2((currentnorthing - citynorthing),(currenteasting - cityeasting)))

                    block_attr.addAttribute("CBDdist", dist)
                    block_attr.addAttribute("CBDdir", theta)
                
                
                ####################################################
                ### 1.3 RETRIEVE EXACT VALUES FROM INPUT DATA    ###
                ####################################################
                datasources = [landuseraster, population, elevationraster, soilraster, plan_map, employment, groundwater, socpar1, socpar2]
                datamatrices = self.retrieveData(datasources, [x_start, y_start], cellsinblock)
                
                lucdatamatrix = datamatrices[0]         #holds land use data from input 
                popdatamatrix = datamatrices[1]         #holds population data from input 
                elevdatamatrix = datamatrices[2]        #holds elevation data from input
                soildatamatrix = datamatrices[3]        #holds soil data from input
                
                planmapmatrix = datamatrices[4]
                employmentmatrix = datamatrices[5]
                groundwatermatrix = datamatrices[6]
                                
                socpar1matrix = datamatrices[7]
                socpar2matrix = datamatrices[8]
                
                #Determine frequency of land class occurrences
                landclassprop, activity = self.frequencyLUC(lucdatamatrix)
                
                if activity == 0:
                    blockstatus = 0
                else:
                    blockstatus = 1
                block_attr.addAttribute("Status", blockstatus)
                block_attr.addAttribute("Active", activity)
                
                
                ####################################################
                ### 2.1 CALCULATE SPATIAL METRICS                ###
                ####################################################
                #Using land class frequencies
                if self.spatialmetrics:
                    richness = self.calcRichness(landclassprop)
                    shdiv, shdom, sheven = self.calcShannonMetrics(landclassprop, richness)
                    block_attr.addAttribute("Rich", richness)
                    block_attr.addAttribute("ShDiv", shdiv)
                    block_attr.addAttribute("ShDom", shdom)
                    block_attr.addAttribute("ShEven", sheven)                    
                
              
                ####################################################
                ### 2.2 CONDUCT TALLYING UP OF DATA FOR BLOCK    ###
                ####################################################
                #Land use classes
                block_attr.addAttribute("pLU_RES", landclassprop[0])           #Land use proportions in block (multiply with block area to get Area
                block_attr.addAttribute("pLU_COM", landclassprop[1])           #RES = Residential      RD = Road
                block_attr.addAttribute("pLU_ORC", landclassprop[2])           #COM = Commercial       TR = Transport facility
                block_attr.addAttribute("pLU_LI", landclassprop[3])            #ORC = Offices & Res    PG = Parks & Gardens
                block_attr.addAttribute("pLU_HI", landclassprop[4])            #LI = Light Industry    REF = Reserves & Floodways
                block_attr.addAttribute("pLU_CIV", landclassprop[5])           #HI = Heavy Industry    UND = Undeveloped
                block_attr.addAttribute("pLU_SVU", landclassprop[6])           #CIV = Civic Facilities NA = Unclassified
                block_attr.addAttribute("pLU_RD", landclassprop[7])            #SVU = Services & Utility
                block_attr.addAttribute("pLU_TR", landclassprop[8])
                block_attr.addAttribute("pLU_PG", landclassprop[9])
                block_attr.addAttribute("pLU_REF", landclassprop[10])
                block_attr.addAttribute("pLU_UND", landclassprop[11])
                block_attr.addAttribute("pLU_NA", landclassprop[12])                
                
                #Averages & Counts for Soil, Elevation, Population and additional inputs
                raster_sum_soil, total_n_soil = 0, 0
                raster_sum_elev, total_n_elev = 0, 0
                pop_sum_total = 0
                soc_par1, total_n_soc_par1 = 0, 0       #to tally up an average in case
                soc_par2, total_n_soc_par2 = 0, 0       #to tally up an average in case    
                job_sum_total = 0
                
                plan_map_sums = [0,0,0,0]       #4 categories of planner's map dependent on RES, COM, LI, HI
                plan_map_counts = [0,0,0,0]
                
                elevlist = []
                
                for a in range(cellsinblock):        #Loop across all cells in the block
                    for b in range(cellsinblock):
                        if soildatamatrix[a][b] != -9999:
                            raster_sum_soil += soildatamatrix[a][b]
                            total_n_soil += 1
                        if elevdatamatrix[a][b] != -9999:
                            total_n_elev += 1
                            elevlist.append(elevdatamatrix[a][b])
                            if self.elevdatadatum == "S":
                                raster_sum_elev += elevdatamatrix[a][b]
                            elif self.elevdatadatum == "C":
                                raster_sum_elev += elevdatamatrix[a][b] + self.elevdatacustomref #bring it back to sea level
                            
                        if popdatamatrix[a][b] != -9999:
                            if self.popdatatype == "C":                         #If population data is a count
                                pop_sum_total += popdatamatrix[a][b]
                            else:                                               #Else population data is a density [pax/ha]
                                pop_sum_total += popdatamatrix[a][b] * (inputres*inputres)/10000
                        
                        #PLANNER'S MAP
                        if self.include_plan_map:
                            lucplanindex = [1, 2, 4, 5]     #numbers are LUC categories that planner's map deals with
                            if lucdatamatrix[a][b] in lucplanindex:
                                lucindex = lucplanindex.index(lucdatamatrix[a][b])
                                if len(planmapmatrix) != 0 and planmapmatrix[a][b] != -9999:
                                    plan_map_sums[lucindex] += planmapmatrix[a][b]
                                    plan_map_counts[lucindex] += 1
                                    
                        #EMPLOYMENT - Like Population
                        if self.include_employment:
                            if employmentmatrix[a][b] != -9999:
                                if self.jobdatatype == "C":
                                    job_sum_total += employmentmatrix[a][b]
                                else:
                                    job_sum_total += employmentmatrix[a][b] * (inputres*inputres)/10000
                            
                        #GROUNDWATER TABLE - Like Elevation, but scaled based on correct datum
                        if self.include_groundwater:
                            gwdepthcumu = 0
                            gwcount = 0
                            if groundwatermatrix[a][b] != -9999:
                                gwdepthcumu += groundwatermatrix[a][b]
                                gwcount += 1
                        
                        #SOCIAL PARAMETERS - Like Population if proportion, if Binary, based on majority
                        if self.include_soc_par1:
                            if len(socpar1matrix) != 0:
                                if socpar1matrix[a][b] != -9999:
                                    soc_par1 += socpar1matrix[a][b]
                                    total_n_soc_par1 += 1
                        if self.include_soc_par2:
                            if len(socpar2matrix) != 0 :
                                if socpar2matrix[a][b] != -9999:
                                    soc_par2 += socpar2matrix[a][b]
                                    total_n_soc_par2 += 1
                               
                #Adjust the total count in case it is zero to prevent division by zero. If count = 0, then sum = 0 because nothing was found
                total_n_soil = self.adjustCount(total_n_soil)
                total_n_elev = self.adjustCount(total_n_elev)
                total_n_soc_par1 = self.adjustCount(total_n_soc_par1)
                total_n_soc_par2 = self.adjustCount(total_n_soc_par2)
                for a in range(len(plan_map_counts)):
                    plan_map_counts[a] = self.adjustCount(plan_map_counts[a])
                
                block_attr.addAttribute("Soil_k", raster_sum_soil/total_n_soil)
                block_attr.addAttribute("AvgElev", raster_sum_elev/total_n_elev)
                block_attr.addAttribute("Pop", pop_sum_total)
                
                if blockstatus == 1:
                    curblock_node = ubdata.UBVector([(xcentre,ycentre,0)])              #UBCORE
                    curblock_node.addAttribute("BlockID", blockIDcount)
                    curblock_node.addAttribute("AvgElev", raster_sum_elev/total_n_elev)
                    curblock_node.addAttribute("Type", "Block")
                    self.activesim.addAsset("BlockCPID"+str(blockIDcount), curblock_node)   #UBCORE
                
                if self.include_soc_par1:
                    block_attr.addAttribute("SocPar1", soc_par1/total_n_soc_par1)
                if self.include_soc_par2:
                    block_attr.addAttribute("SocPar2", soc_par2/total_n_soc_par2)
                if self.include_plan_map:
                    block_attr.addAttribute("PM_RES", plan_map_sums[0]/plan_map_counts[0])
                    block_attr.addAttribute("PM_COM", plan_map_sums[1]/plan_map_counts[1])
                    block_attr.addAttribute("PM_LI", plan_map_sums[2]/plan_map_counts[2])
                    block_attr.addAttribute("PM_HI", plan_map_sums[3]/plan_map_counts[3])
                if self.include_employment:
                    block_attr.addAttribute("Employ", job_sum_total)           #Total people EMPLOYED in block
                if self.include_groundwater:
                    if self.groundwater_datum == "Sea":
                        if total_n_elev == 0 or gwcount == 0:
                            gwdepth = -9999
                        else:
                            gwdepth = float(raster_sum_elev/total_n_elev) - float(gwdepthcumu/gwcount)
                    elif self.groundwater_datum == "Surf":
                        if gwcount == 0:
                            gwdepth = -9999
                        else:
                            gwdepth = float(gwdepthcumu/gwcount)
                    block_attr.addAttribute("GWDepth", gwdepth)
                    
                #Rivers, Lakes & Locality Map Data Locate for Block and Assign
                blockxmin = xorigin + self.xllcorner            #Grab the corners of the current block
                blockxmax = xorigin + self.xllcorner + cs
                blockymin = yorigin + self.yllcorner
                blockymax = yorigin + self.yllcorner + cs
                
                #RIVERS AND DRAINAGE - At least one point within Block
                hasriver = 0
                if self.include_rivers or self.use_river:
                    pointcount = 0
                    while pointcount != len(riverpoints):
                        pointset = riverpoints[pointcount]
                        pointcount += 1
                        if pointset[0] >= blockxmin and pointset[0] < blockxmax:
                            if pointset[1] >= blockymin and pointset[1] < blockymax:
                                hasriver = 1
                                pointcount = len(riverpoints)
                    block_attr.addAttribute("HasRiv", hasriver)

                hasdrainage = 0
                if self.include_drainage_net or self.use_drainage:
                    pointcount = 0
                    while pointcount != len(drainagepoints):
                        pointset = drainagepoints[pointcount]
                        pointcount += 1
                        if pointset[0] >= blockxmin and pointset[0] < blockxmax:
                            if pointset[1] >= blockymin and pointset[1] < blockymax:
                                hasdrainage = 1
                                pointcount = len(drainagepoints)
                    block_attr.addAttribute("HasDrain", hasdrainage)

                #LAKES - Centroid within Block
                haslake = 0
                lakearea = 0
                if self.include_lakes:
                    pointcount = 0
                    while pointcount != len(lakepoints):
                        pointset = lakepoints[pointcount]
                        pointcount += 1
                        if pointset[0] >= blockxmin and pointset[0] < blockxmax:
                            if pointset[1] >= blockymin and pointset[1] < blockymax:
                                haslake = 1
                                lakearea = pointset[2]
                                pointcount = len(lakepoints)
                    block_attr.addAttribute("HasLake", haslake)
                    block_attr.addAttribute("LakeAr", lakearea)
                    
                #LOCALITY MAP - Must scan each point and place in Block!
                haslocal = 0
                facilcount = 0
                if self.include_local_map:
                    for locfeature in localitymap:
                        if locfeature[1] >= blockxmin and locfeature[1] < blockxmax:
                            if locfeature[2] >= blockymin and locfeature[2] < blockymax:
                                haslocal = 1
                                facilcount += 1
                                fac_attr = ubdata.UBVector([(locfeature[1]-self.xllcorner, locfeature[2]-self.yllcorner, 0, self.blocklocality)])
                                fac_attr.addAttribute("BlockID", blockIDcount)
                                fac_attr.addAttribute("Type", locfeature[0])
                                fac_attr.addAttribute("Area", locfeature[3])
                                fac_attr.addAttribute("TIF", locfeature[4])
                                fac_attr.addAttribute("ARoof", locfeature[5])
                                fac_attr.addAttribute("AvgWD", locfeature[6])
                                self.activesim.addAsset("FacilityID"+str(facilcount))
                                localitymap.remove(locfeature)  #Remove this entry from the matrix to make it shorter for next time
                                
                    block_attr.addAttribute("HasLoc", haslocal)
                    block_attr.addAttribute("NFacil", facilcount)
                
                
                ####################################################
                ### 2.3 DELINEATE PATCHES                        ###
                ####################################################
                #Call the function using the current Block's Patch information
                if self.patchdelin:
                    patchdict = ubpat.landscapePatchDelineation(lucdatamatrix, elevdatamatrix, soildatamatrix)
                    #Draw the patches and save info to view
                    for i in range(len(patchdict)):
                        paspect = patchdict["PatchID"+str(i+1)][5]
                        pacentroid = patchdict["PatchID"+str(i+1)][4]
                        paarea = patchdict["PatchID"+str(i+1)][0]
                        paluc = patchdict["PatchID"+str(i+1)][1]
                        paelev = patchdict["PatchID"+str(i+1)][2]
                        pasoil = patchdict["PatchID"+str(i+1)][3]

                        luccheck = 1    #CHANGE THIS VARIABLE TO ZERO IF YOU DO NOT WANT THE MODEL TO CONSIDER NO-DATA PATCHES
                        if luccheck:
                            if paluc == -9999:  #if the current patch is a no-data patch, skip...
                                continue

                        self.drawPatchCentroid(pacentroid, paspect, inputres, offset, i+1, blockIDcount, paarea, paluc, paelev, pasoil)
                        
                    block_attr.addAttribute("Patches", len(patchdict))
                    #print "End Patches"
                
                ### FINISH UP THE LOOP ###
                block_attr.addAttribute("BasinID", 0)               #Assign Default value of zero, this is altered below
                
                ### INCREMENT BLOCK ID COUNT BY 1 ###
                self.activesim.addAsset("BlockID"+str(blockIDcount), block_attr)        #Add block asset to simulation storage
                blockIDcount += 1    #increase counter by one before next loop to represent next Block ID
                #END OF BLOCK LOOP
        
        ########################################################################
        ### 3.) TERRAIN & BASIN DELINEATION                                  ###
        ########################################################################
        if self.demsmooth_choose:
            for currentpass in range(int(self.demsmooth_passes)):
                self.smoothDEM(numblocks, neighbourhood_type) 
        
        #Determine whether terrain delineation already exists or whether it needs to be done
        self.delineateFlowPaths(numblocks, cs, neighbourhood_type)
        hash_table = self.createBlockHashTable(numblocks)
        totalbasins = self.delineateBasins(numblocks, hash_table)
        map_attr.addAttribute("TotalBasins", totalbasins)

    ########################################
        #RESET ALL RASTER AND VECTOR DATA VARIABLES        
        elevationraster.resetData()
        soilraster.resetData()
        landuseraster.resetData()
        population.resetData()
        if plan_map != 0: plan_map.resetData()
        if localitymap != 0: localitymap = 0
        if employment != 0: employment.resetData()
        if riverpoints != 0: riverpoints = 0
        if lakepoints != 0: lakepoints = 0
        if groundwater != 0: groundwater.resetData()
        if socpar1 != 0: socpar1.resetData()
        if socpar2 != 0: socpar2.resetData()
        self.notify("End of DelinBlocks")

    ########################################################################
    ### DELINBLOCKS SUB-FUNCTIONS                                        ###
    ########################################################################

    def autosizeBlocks(self, width, height):
        """Calculates the recommended Block Size dependent on the size of the case study
        determined by the input map dimensions. Takes width and height and returns block
        size
        
        Rules:
           - Based on experience from simulations, aims to reduce simulation times
             while providing enough accuracy.
           - Aim to simulate under 500 Blocks"""
        blocklimit = 500
        totarea = width * height
        idealblockarea = totarea / 500
        idealblocksize = math.sqrt(idealblockarea)
        print "IdBS:", idealblocksize
        
        if idealblocksize <= 200:
            blocksize = 200
        elif idealblocksize <= 500:
            blocksize = 500
        elif idealblocksize <= 1000:
            blocksize = 1000
        elif idealblocksize <= 2000:
            blocksize = 2000
        elif idealblocksize/1000 < 10:
            blocksize = (int(idealblocksize/1000)+1)*1000
        else:
            blocksize = (int(idealblocksize/10000)+1)*10000
        
        if blocksize >= 10000:
            print "WARNING: Block Size is very large, it is recommended to use a smaller case study!"    
        
        return blocksize        
    
    def createBlockFace(self, x, y, cs, x_adj, y_adj, ID):
        n1 = ((x+x_adj)*cs,(y+y_adj)*cs,0)
        n2 = ((x+x_adj+1)*cs,(y+y_adj)*cs,0)
        n3 = ((x+x_adj+1)*cs,(y+y_adj+1)*cs,0)
        n4 = ((x+x_adj)*cs,(y+y_adj+1)*cs,0)
        
        #Definte the UrbanBEATS Asset        
        block_attr = ubdata.UBVector([n1, n2, n3, n4, n1])        
        block_attr.addAttribute("BlockID", int(ID))
        
        return block_attr
    
    def getCBDcoordinates(self):
        if self.locationOption == "S":
            #look up city and grab coordinates
            coordinates = self.CBDcoordinates[self.locationCity]
            return coordinates[0], coordinates[1]   #easting, northing
        elif self.locationOption == "C":
            longitude = self.locationLong
            latitude = self.locationLat
            coordinates = ubcc.convertGeographic2UTM(longitude, latitude)
            return coordinates[0], coordinates[1]   #easting, northing

    
    def retrieveData(self, datasources, startextents, cellsinblock):
        """Scans the original data range and retrieves all the data values contained
        therein:
                   - datasources: the Views containing the rasters
                   - startextents: [xstart, ystart] coordinates
                   - cellsinblock: how many cells are in one block (defines extents)
        """
        #Base Inputs
        lucdatamatrix = []
        popdatamatrix = []
        elevdatamatrix = []
        soildatamatrix = []
        
        #Additional Inputs
        planmapmatrix = []
        employmentmatrix = []
        groundwatermatrix = []
        socpar1matrix = []
        socpar2matrix = []
        
        
        x_start = startextents[0]
        y_start = startextents[1]
        
        for i in range(cellsinblock):
            lucdatamatrix.append([])
            popdatamatrix.append([])
            elevdatamatrix.append([])
            soildatamatrix.append([])
            planmapmatrix.append([])
            employmentmatrix.append([])
            groundwatermatrix.append([])
            socpar1matrix.append([])
            socpar2matrix.append([])
            
            for j in range(cellsinblock):
                lucdatamatrix[i].append(datasources[0].getValue(x_start+i, y_start+j))
                popdatamatrix[i].append(datasources[1].getValue(x_start+i, y_start+j))
                elevdatamatrix[i].append(datasources[2].getValue(x_start+i, y_start+j))
                
                if self.soildatatype == "C":
                    if datasources[3].getValue(x_start+i, y_start+j) != -9999:
                        soildatamatrix[i].append(self.soildictionary[int(datasources[3].getValue(x_start+i, y_start+j))-1])        #look up mm/hr value
                    else:
                        soildatamatrix[i].append(-9999)
                elif self.soildataunits == "hrs":
                    soildatamatrix[i].append(datasources[3].getValue(x_start+i, y_start+j))     #keep as mm/hr
                elif self.soildataunits == "sec":
                    soildatamatrix[i].append((datasources[3].getValue(x_start+i, y_start+j))*1000*60*60)        #convert to mm/hr
                
                if datasources[4] != 0: planmapmatrix[i].append(datasources[4].getValue(x_start+i, y_start+j))
                if datasources[5] != 0: employmentmatrix[i].append(datasources[5].getValue(x_start+i, y_start+j))
                if datasources[6] != 0: groundwatermatrix[i].append(datasources[6].getValue(x_start+i, y_start+j))
                if datasources[7] != 0: socpar1matrix[i].append(datasources[7].getValue(x_start+i, y_start+j))
                if datasources[8] != 0: socpar2matrix[i].append(datasources[8].getValue(x_start+i, y_start+j))
                
        datamatrices = [lucdatamatrix, popdatamatrix, elevdatamatrix, soildatamatrix, planmapmatrix, employmentmatrix, groundwatermatrix, socpar1matrix, socpar2matrix]
        return datamatrices


    def frequencyLUC(self, lucdatamatrix):
        #Determine size of matrix
        matsize = len(lucdatamatrix)
        #'RES', 'COM', 'ORC', 'LI', 'HI', 'CIV', 'SVU', 'RD', 'TR', 'PG', 'REF', 'UND', 'NA'
        lucprop = [0,0,0,0,0,0,0,0,0,0,0,0,0]
        total_n_luc = 0
        for i in range(matsize):
            for j in range(matsize):
                landclass = lucdatamatrix[i][j]
                if landclass == -9999:
                    pass
                else:
                    lucprop[int(landclass-1)] += 1
                    total_n_luc += 1
        
        #Convert frequency to proportion
        if total_n_luc == 0:
            return [0,0,0,0,0,0,0,0,0,0,0,0,0], 0
        for i in range(len(lucprop)):
            lucprop[i] = float(lucprop[i])/total_n_luc
        activity = float(total_n_luc) / float((matsize * matsize))
        return lucprop, activity
    
    
    def calcRichness(self, landclassprop):
        richness = 0
        for i in landclassprop:
            if i != 0:
                richness += 1
        return richness


    def calcShannonMetrics(self, landclassprop, richness):
        if richness == 0:
            return 0,0,0
        
        #Shannon Diversity Index (Shannon, 1948) - measures diversity in categorical data, the information entropy of
        #the distribution: H = -sum(pi ln(pi))
        shandiv = 0
        for sdiv in landclassprop:
            if sdiv != 0:
                shandiv += sdiv*math.log(sdiv)
        shandiv = -1 * shandiv
        
        #Shannon Dominance Index: The degree to which a single class dominates in the area, 0 = evenness
        shandom = math.log(richness) - shandiv
        
        #Shannon Evenness Index: Similar to dominance, the level of evenness among the land classes
        if richness == 1:
            shaneven = 1
        else:
            shaneven = shandiv/math.log(richness)
            
        return shandiv, shandom, shaneven
    
    
    def findNeighbourhood(self, ID, x, y, numblocks, widthnew, heightnew):
        """NEIGHBOURHOODs - Search for all 8 neighbours. """
        neighbour_assign = 0
        #check neighbour IDs
        #check for corner pieces
        if ID - 1 == 0:                            #bottom left
            neighbour_assign = 1
            N_neighbour = ID + widthnew 
            S_neighbour = 0
            W_neighbour = 0
            E_neighbour = ID + 1
            NE_neighbour = N_neighbour + 1
            NW_neighbour = 0
            SE_neighbour = 0
            SW_neighbour = 0
        if ID + 1 == numblocks+1:                  #top right
            neighbour_assign = 1
            N_neighbour = 0
            S_neighbour = ID - widthnew
            W_neighbour = ID - 1
            E_neighbour = 0
            NE_neighbour = 0
            NW_neighbour = 0
            SE_neighbour = 0
            SW_neighbour = S_neighbour - 1
        if ID - widthnew == 0:                     #bottom right
            neighbour_assign = 1
            N_neighbour = ID + widthnew
            S_neighbour = 0
            W_neighbour = ID - 1
            E_neighbour = 0
            NE_neighbour = 0
            NW_neighbour = N_neighbour - 1
            SE_neighbour = 0
            SW_neighbour = 0
        if ID + widthnew == numblocks+1:           #top left
            neighbour_assign = 1
            N_neighbour = 0
            S_neighbour = ID - widthnew
            W_neighbour = 0
            E_neighbour = ID + 1
            NE_neighbour = 0
            NW_neighbour = 0
            SE_neighbour = S_neighbour + 1
            SW_neighbour = 0
        
        #check for edge piece
        if neighbour_assign == 1:
            pass
        else:
            if float(ID)/widthnew == y+1:                  #East edge
                neighbour_assign = 1
                N_neighbour = ID + widthnew
                S_neighbour = ID - widthnew
                W_neighbour = ID - 1
                E_neighbour = 0
                NE_neighbour = 0
                NW_neighbour = N_neighbour - 1
                SE_neighbour = 0
                SW_neighbour = S_neighbour - 1
            if float(ID-1)/widthnew == y:                  #West edge
                neighbour_assign = 1
                N_neighbour = ID + widthnew
                S_neighbour = ID - widthnew
                W_neighbour = 0
                E_neighbour = ID + 1
                NE_neighbour = N_neighbour + 1
                NW_neighbour = 0
                SE_neighbour = S_neighbour + 1
                SW_neighbour = 0
            if ID - widthnew < 0:                          #South edge
                neighbour_assign = 1
                N_neighbour = ID + widthnew
                S_neighbour = 0
                W_neighbour = ID - 1
                E_neighbour = ID + 1
                NE_neighbour = N_neighbour + 1
                NW_neighbour = N_neighbour - 1
                SE_neighbour = 0
                SW_neighbour = 0
            if ID + widthnew > numblocks+1:                #North edge
                neighbour_assign = 1
                N_neighbour = 0
                S_neighbour = ID - widthnew
                W_neighbour = ID - 1
                E_neighbour = ID + 1
                NE_neighbour = 0
                NW_neighbour = 0
                SE_neighbour = S_neighbour + 1
                SW_neighbour = S_neighbour - 1
        
        #if there is still no neighbours assigned then assume standard cross
        if neighbour_assign == 1:
            pass
        else:
            neighbour_assign = 1
            N_neighbour = ID + widthnew
            S_neighbour = ID - widthnew
            W_neighbour = ID - 1
            E_neighbour = ID + 1
            NE_neighbour = N_neighbour + 1
            NW_neighbour = N_neighbour - 1
            SE_neighbour = S_neighbour + 1
            SW_neighbour = S_neighbour - 1
        
        blockNHD = [N_neighbour, S_neighbour, W_neighbour, E_neighbour, NE_neighbour, NW_neighbour, SE_neighbour, SW_neighbour]    
        return blockNHD                
    
    
    def adjustCount(self, total_count):
        if total_count == 0:
            total_count = 1
        else:
            pass
        return total_count


    def drawPatchCentroid(self, nodes, aspect, scalar, offset, PaID, ID, area, LUC, elev, soil):        #UBCORE VERSION ----------------->
        rs = scalar #rs = raster size
        plist = (nodes[0]*rs+offset[0], nodes[1]*rs+offset[1], 0)       #Nodes = [x, y], Offset = [x, y], RS = scaling factor

        patch_attr = ubdata.UBVector([plist])
        patch_attr.addAttribute("PatchID", PaID)              #ID of Patch in Block ID
        patch_attr.addAttribute("LandUse", LUC)              #Land use of the patch
        patch_attr.addAttribute("Area", area*rs*rs)                 #Area of the patch
        patch_attr.addAttribute("AvgElev", elev)              #Average elevation of the patch
        patch_attr.addAttribute("SoilK", soil)
        patch_attr.addAttribute("BlockID", ID)              #Block ID that patch belongs to
        patch_attr.addAttribute("AspRatio", aspect)     #Aspect ratio of the patch
        
        self.activesim.addAsset("B"+str(ID)+"PatchID"+str(PaID), patch_attr)
        return True

    
    def smoothDEM(self, numblocks, nhd_type):
        new_elevs = []
        for i in range(int(numblocks)):
            nhd_count = 1
            currentID = i+1
            currentAttList = self.activesim.getAssetWithName("BlockID"+str(currentID))
            if currentAttList.getAttribute("Status") == 0:
                new_elevs.append(0)
                continue
            
            new_elev = currentAttList.getAttribute("AvgElev")
            
            neighbourhood = self.getBlockNeighbourhood(currentAttList)
            neighbourhoodZ = self.getNeighbourhoodZ(neighbourhood)
            
            if nhd_type == 4:
                #only vonNeumann cells
                for k in range(len(neighbourhoodZ)-4):
                    if k == 99999:
                        continue
                    new_elev += k
                    nhd_count += 1
            else:
                for k in neighbourhoodZ:                #Scan all neighbour cells
                    if k == 99999:                      #if the value is 99999, it means the cell isn't active
                        continue
                    new_elev += k
                    nhd_count += 1
                    
                new_elevs.append(new_elev/nhd_count)    #calculate average, add to the new matrix
        
        for i in range(int(numblocks)):     #write all new elevations to replace the existing value
            currentID = i+1
            currentAttList = self.activesim.getAssetWithName(currentID)
            currentAttList.setAttribute("AvgElev", new_elevs[i])
        return True


    def getBlockNeighbourhood(self, currentAttList):
        """Returns the Moore neighbouhoord for the Block (8 neighbours in all cardinal
        directions, the order is North, South, West, Est, followed by NE, NW, SE, SW"""
        ID_N = int(round(currentAttList.getAttribute("Nhd_N")))
        ID_S = int(round(currentAttList.getAttribute("Nhd_S")))
        ID_W = int(round(currentAttList.getAttribute("Nhd_W")))
        ID_E = int(round(currentAttList.getAttribute("Nhd_E")))
        ID_NE = int(round(currentAttList.getAttribute("Nhd_NE")))
        ID_NW = int(round(currentAttList.getAttribute("Nhd_NW")))
        ID_SE = int(round(currentAttList.getAttribute("Nhd_SE")))
        ID_SW = int(round(currentAttList.getAttribute("Nhd_SW")))
        current_neighb = [ID_N, ID_S, ID_W, ID_E, ID_NE, ID_NW, ID_SE, ID_SW]
        return current_neighb

    
    def getNeighbourhoodZ(self, nhdIDs):
        current_neighbdZ = []

        #scan for river and drainage data
        rivbool = []
        drainbool = []
        if self.use_river or self.use_drainage:
            for i in nhdIDs:
                if i == 0:
                    rivbool.append(0)       #rivbool = [0,0,0,1,0,0] contains a list of booleans, if the sum is greater
                    drainbool.append(0)     #than 0 then at least one neighbour has the water feature
                else:
                    rivbool.append(self.activesim.getAssetWithName("BlockID"+str(i)).getAttribute("HasRiver"))
                    drainbool.append(self.activesim.getAssetWithName("BlockID"+str(i)).getAttribute("HasDrain"))

        for i in nhdIDs:       #scan all 8 neighbours, determine elevation
            if i == 0:          #if the Neighbourhood ID == 0
                current_neighbdZ.append(99999)
                continue
            curface = self.activesim.getAssetWithName("BlockID"+str(i))
            if int(round(curface.getAttribute("Status"))) == 0:
                current_neighbdZ.append(99999) #works based on Sea Level, so nothing can really be higher than Everest :)
                continue
            if self.use_river and sum(rivbool) > 0:
                if curface.getAttribute("HasRiver") == 1:
                    current_neighbdZ.append(curface.getAttribute("AvgElev"))
                    continue
                else:
                    current_neighbdZ.append(99999)
                continue
            if self.use_drainage and sum(drainbool) > 0:
                if curface.getAttribute("HasDrain") == 1:
                    current_neighbdZ.append(curface.getAttribute("AvgElev"))
                else:
                    current_neighbdZ.append(99999)
                continue

            current_neighbdZ.append(curface.getAttribute("AvgElev"))

        return current_neighbdZ


    def findDownstreamD8(self, currentZ, neighboursZ, neighbourhood_type):
        if neighbourhood_type == 4:
            neighboursZ[4] = 999999
            neighboursZ[5] = 999999
            neighboursZ[6] = 999999
            neighboursZ[7] = 999999
        for i in range(len(neighboursZ)):            #D8 is simply the largest drop
            neighboursZ[i] = currentZ - neighboursZ[i]
        max_Zdrop = max(neighboursZ)
        if max_Zdrop <= 0:
            direction = -9999  #-9999 means that the current block is a sink
        else:
            direction = neighboursZ.index(max_Zdrop)
        return direction, max_Zdrop


    def findDownstreamDinf(self, currentZ, blocksize, neighboursZ, neighbourhood_type):
        """D-infinity method adapted to only direct water in one direction based on the steepest
        slope of the 8 triangular facets surrounding a Block's neighbourhood and a probabilistic
        choice weighted by the proportioning of flow. This is the stochastic option of flowpath
        delineation for UrbanBEATS and ONLY works with Moore neighbourhood"""

        facetdict = {}      #Stores all the information about the 8 facets
        facetdict["e1"] = ["E","N","N","W","W","S","S","E"]
        facetdict["e2"] = ["NE","NE","NW","NW","SW","SW","SE","SE"]
        facetdict["ac"] = [0,1,1,2,2,3,3,4]
        facetdict["af"] = [1,-1,1,-1,1,-1,1,-1]
        cardin = { "E":0, "NE":1, "N":2, "NW":3, "W":4, "SW":5, "S":6, "SE":7 }
        
        e0 = currentZ               #CONSTANT PARAMETERS (because of constant block grid and centre point)
        d1 = blocksize
        d2 = d1
        facetangles = [0, math.pi/4, math.pi/2, 3*math.pi/4, math.pi, 5*math.pi/4, 3*math.pi/2, 7*math.pi/4]
        
        #Re-sort the neighbours matrix based on polar angle
        sortedneighb = [neighboursZ[3],neighboursZ[4],neighboursZ[0],neighboursZ[5],neighboursZ[2],neighboursZ[7],neighboursZ[1],neighboursZ[6]]
        rmatrix = []
        smatrix = []

        for i in range(len(sortedneighb)):  #Calculate slopes of all 8 facets
            currentfacet = i
            
            e1 = sortedneighb[cardin[facetdict["e1"][currentfacet]]]        #e1 elevation:  (1) get cardinal direction from dictionary, 
                                                                            #               (2) get the index from cardin and 
            e2 = sortedneighb[cardin[facetdict["e2"][currentfacet]]]        #               (3) get the value from neighbz
            
            ac = facetdict["ac"][currentfacet]
            af = facetdict["af"][currentfacet]
            
            s1 = (e0 - e1)/d1
            s2 = (e1 - e2)/d2
            r = math.atan(s2/s1)
            s = math.sqrt(math.pow(s1,2) + math.pow(s2, 2))
            
            if r < 0:
                r = 0
                s = s1
            elif r > math.atan(d2/d1):
                r = math.atan(d2/d1)
                s = (e0 - e2)/math.sqrt(math.pow(d1, 2) + math.pow(d2, 2))
            
            rmatrix.append(r)
            smatrix.append(s)
        
        #Find the maximum slope and get the angle
        rmax = max(rmatrix)
        rg = af*rmax + ac*math.pi/2.0
        
        #Find the facet
        for i in range(len(facetangles)):
            if rg > facetangles[i]:
                continue
            else:
                facet = i-1
                theta1 = facetangles[i-1]
                theta2 = facetangles[i]
        #Adjust angles based on rg to get proportions
        alpha1 = rg - theta1
        alpha2 = theta2 - rg
        p1 = alpha1/(alpha1 + alpha2)
        p2 = alpha2/(alpha2 + alpha1)
        
        print "Proportioned Flows:", p1, p2
        
        if rand.random() < p1:
            choice = p1
            directionfacet = int(theta1/(math.pi/4))
        else:
            choice = p2
            directionfacet = int(theta2/(math.pi/4))
            
        print "Choice:", choice
        
        direction = neighboursZ.index(sortedneighb[directionfacet-1])
        return direction, max_Zdrop
    
    
    def drawFlowPaths(self, currentID, downstreamID, currentAttList, max_Zdrop, avg_slope, typenum):    #UBCORE VERSION ------------
        f = self.activesim.getAssetWithName("BlockID"+str(int(downstreamID)))
            
        x_up = currentAttList.getAttribute("CentreX")
        y_up = currentAttList.getAttribute("CentreY")
        z_up = currentAttList.getAttribute("AvgElev")
        upNode = (x_up,y_up,z_up)
        
        x_down = f.getAttribute("CentreX")
        y_down = f.getAttribute("CentreY")
        z_down = f.getAttribute("AvgElev")
        downNode = (x_down,y_down,z_down)
        
        network_attr = ubdata.UBVector([upNode, downNode])         
        network_attr.addAttribute("BlockID", currentID)
        network_attr.addAttribute("DownID", downstreamID)
        network_attr.addAttribute("Z_up", z_up)
        network_attr.addAttribute("Z_down", z_down)
        network_attr.addAttribute("max_Zdrop", max_Zdrop)
        network_attr.addAttribute("Type", typenum)       #1 = basic downstream, -1 = unblocked sink, #0 = sink
        network_attr.addAttribute("avg_slope", avg_slope)
        self.activesim.addAsset("NetworkID"+str(currentID), network_attr)
        return True
    
    def delineateFlowPaths(self, numblocks, cs, neighbourhood_type):
        sinkIDs = []
        riverIDs = []
        lakeIDs = []

        for i in range(numblocks):
            currentID = i+1
            
            #CONDITION 1 - Block is Active in Simulation
            currentAttList = self.activesim.getAssetWithName("BlockID"+str(currentID))
            
            if currentAttList.getAttribute("Status") == 0:
                #print "BlockID"+str(currentID)+" not active in simulation"
                continue
            
            #CONDITION 2 - Block already contains a sink e.g. river/etc.
            if currentAttList.getAttribute("HasRiv") == 1 and useriver == 0:
                hasRiver = 1
                riverIDs.append(currentID)
                continue
            
            currentZ = currentAttList.getAttribute("AvgElev")
            
            #Neighbours array: [N, S, W, E, NE, NW, SE, SW], the last four are 0 if only vonNeumann Nhd used.
            neighbours = self.getBlockNeighbourhood(currentAttList)
            neighboursZ = self.getNeighbourhoodZ(neighbours)
            
            #Find Downstream Block - The Functions return the Index of the Cardinal Direction
            if self.flow_method == "D8":
                flow_direction, max_Zdrop = self.findDownstreamD8(currentZ, neighboursZ, neighbourhood_type)
            elif self.flow_method == "DI":
                flow_direction, max_Zdrop = self.findDownstreamDinf(currentZ, cs, neighboursZ, neighbourhood_type)
            
            if flow_direction == -9999:
                sinkIDs.append(currentID)
                downstreamID = -1
            else:
                downstreamID = neighbours[flow_direction]
            
            #Grab Distance/Slope between two Block IDs
            if flow_direction == -9999:
                dx = 0
            elif flow_direction <= 3:
                dx = cs
            elif flow_direction > 3:
                dx = math.sqrt(2*cs*cs)                        #diagonal
                
            if dx == 0: avg_slope = 0
            else: avg_slope = max_Zdrop/dx
            
            currentAttList.addAttribute("downID", downstreamID)
            currentAttList.addAttribute("maxdZ", max_Zdrop)
            currentAttList.addAttribute("slope", avg_slope)
            
            #DRAW NETWORKS OF PATHS THAT ARE NOT SINKS
            if downstreamID != -1 and downstreamID != 0:
                #print "To Draw"
                #print currentID
                #print downstreamID
                self.drawFlowPaths(currentID, downstreamID, currentAttList, max_Zdrop, avg_slope, 1)
            
        self.unblockSinks(sinkIDs, numblocks)
        self.connectRiverBlocks(riverIDs, numblocks)
        return True

    
    def unblockSinks(self, sinkIDs, numblocks):
        total_sinks = len(sinkIDs)
        #print "A total of: "+str(total_sinks)+" sinks found in map!"
        self.notify("A total of: "+str(total_sinks)+" sinks found in map!") #UBCORE

        #Sink unblocking algorithm for immediate neighbourhood
        for i in sinkIDs:
            currentID = i
            #print "CurrentID: ", currentID
            self.notify("CurrentID: "+str(currentID))   #UBCORE
            currentAttList = self.activesim.getAssetWithName("BlockID"+str(int(currentID)))           
            currentZ = currentAttList.getAttribute("AvgElev")    
            
            current_neighb = self.getBlockNeighbourhood(currentAttList)
            #print current_neighb
            self.notify(current_neighb)
            possible_IDdrains = []
            possible_IDdZ = []
            possibility = 0
            
            for j in current_neighb:
                if j == 0:
                    continue
                f = self.activesim.getAssetWithName("BlockID"+str(int(j)))                
                testdownID = int(round(f.getAttribute("downID")))
                if  testdownID not in [currentID, -1] and testdownID not in current_neighb and int(round(f.getAttribute("Status"))) != 0:
                    possible_IDdrains.append(j)
                    possible_IDdZ.append(f.getAttribute("AvgElev")-currentZ)
                    possibility += 1
        
            if possibility > 0:         #if algorithm found a possible pathway for sink to unblock, then get the ID and connect network
                sink_path = min(possible_IDdZ)
                sink_drainID = possible_IDdrains[possible_IDdZ.index(sink_path)]
                currentAttList.addAttribute("drainID", sink_drainID)            
                currentAttList.addAttribute("h_pond", sink_path)
                self.drawFlowPaths(currentID, sink_drainID, currentAttList, sink_path, 0, -1) 
                continue
            else:
                #IF the model reaches this point, the identified cell is either most definitely an outlet or a very troublesome sink
                currentAttList.addAttribute("drainID", -1)      #-1 in drainID = outlet or sub-outlet        
        return True


    def connectRiverBlocks(self, riverIDs, numblocks):
        #print "A total of: "+str(len(riverIDs))+" Blocks contain a river body!"
        self.notify("A total of: "+str(len(riverIDs))+" Blocks contain a river body!")
        riverbodycount = 0        
        return True
    
    
    def createBlockHashTable(self, numblocks):
        """Indexes through the list of blocks and finds the downstream blocks that each
        block flows into (0 = outlet). This hash table is required for finding basins
        within the case study area.
        """
        hash_table = [[],[]]    #COLUMN1: BLOCK ID (UP), COLUMN2: DOWNSTREAM ID (DOWN)
        for i in range(int(numblocks)):
            currentID = i+1
            currentAttList = self.activesim.getAssetWithName("BlockID"+str(currentID))
            if currentAttList.getAttribute("Status") == 0:
                #print "BlockID"+str(currentID)+" not active in simulation"
                continue
            
            hash_table[0].append(int(currentID))
            
            if currentAttList.getAttribute("downID") not in [0, -1]:
                hash_table[1].append(int(currentAttList.getAttribute("downID")))
            elif currentAttList.getAttribute("drainID") not in [0, -1]:
                hash_table[1].append(int(currentAttList.getAttribute("drainID")))
            else:
                hash_table[1].append(int(0))
        #print hash_table
        self.notify(hash_table)
        return hash_table
    
    def delineateBasins(self, numblocks, hash_table): #UBCORE VERSION ------------------------------------------------------
        basinID = 0
        for i in range(numblocks):
            currentID = i+1
            currentAttList = self.activesim.getAssetWithName("BlockID"+str(int(currentID)))
            if currentAttList.getAttribute("Status") == 0:
                #print "BlockID"+str(currentID)+" not active in simulation"
                continue
            
            if currentID not in hash_table[1]:
                currentAttList.addAttribute("UpstrIDs", "")
                if currentID in hash_table[0]:
                    if hash_table[1][hash_table[0].index(currentID)] == 0:
                        #print "Found a single block basin at Block: ", currentID
                        self.notify("Found a single block basin at Block: "+str(currentID))
                        basinID += 1   #transfer currentID to all blocks
                        currentAttList.addAttribute("BasinID", basinID)
                        currentAttList.addAttribute("DownStrIDs", "")
                        currentAttList.addAttribute("Outlet", 1)
                        continue
            else:
                upstreamIDs = [currentID]
                for id in upstreamIDs:
                    for j in range(len(hash_table[1])):
                        if id == hash_table[1][j]:
                            if hash_table[0][j] not in upstreamIDs:
                                upstreamIDs.append(hash_table[0][j])

                upstreamIDs.remove(currentID)
                #print "BlockID", currentID, "Upstream: ", upstreamIDs
                self.notify("BlockID"+str(currentID)+" Upstream: "+str(upstreamIDs))
                outputstring = ""
                for j in upstreamIDs:
                    outputstring += str(j)+","
                currentAttList.addAttribute("UpstrIDs", outputstring)

            downstreamIDs = [currentID]
            for id in downstreamIDs:
                for j in range(len(hash_table[0])):
                    if id == hash_table[0][j]:
                        if hash_table[1][j] not in downstreamIDs:
                            downstreamIDs.append(hash_table[1][j])
            downstreamIDs.remove(currentID)
            downstreamIDs.remove(0)
            self.notify("BlockID"+str(currentID)+" Downstream: "+str(downstreamIDs))
            outputstring = ""
            for j in downstreamIDs:
                outputstring += str(j)+","
            currentAttList.addAttribute("DownstrIDs", outputstring)

            #Set Basin IDs
            if hash_table[1][hash_table[0].index(currentID)] == 0:
                #print "Found a basin outlet at Block: ", currentID
                self.notify("Found a basin outlet at Block: "+str(currentID))
                basinID += 1   #transfer currentID to all blocks
                currentAttList.addAttribute("Outlet", 1)
                currentAttList.addAttribute("BasinID", basinID)
                for j in upstreamIDs:
                    upblock = self.activesim.getAssetWithName("BlockID"+str(int(j)))
                    upblock.addAttribute("BasinID", basinID)
                    upblock.addAttribute("Outlet", 0)
        
        #print "Total Basins in Case Study: ", basinID
        self.notify("Total Basins in Case Study: "+str(basinID))

        return basinID
