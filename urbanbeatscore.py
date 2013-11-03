# -*- coding: utf-8 -*-
"""
@file
@author  Peter M Bach <peterbach@gmail.com>
@version 0.5
@section LICENSE

This file is part of VIBe2
Copyright (C) 2011  Peter M Bach

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

#------ IMPORTS --------------
#Regular imports
import threading, gc

#Dependencies
import urbanbeatsdatatypes as ubdata

#Modules
import md_delinblocks, md_urbplanbb, md_techplacement, md_techimplement#, md_perfassess

# ------ CLASS DEFINITION -------
class UrbanBeatsSim(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        #Simulation object of UrbanBEATS, contains the full details of one simulation

        #Observer, Status and Filename
        self.__observers = []         #Observers of the current simulation
        self.__simulation_has_completed = 0
        self.__filename= ""                 #Filename of the simulation

        ### ---------- Project information, Narrative Information and Simulation Details ------------
        self.__projectinfo = {
                "name" : "<enter name>",
                "date" : "",
                "region" : "<none specified>",
                "state" : "<none>",
                "country" : "<none specified>",
                "modeller" : "<none specified>",
                "affiliation" : "<none specified>",
                "otherpersons" : "<none specified>",
                "synopsis" : "<none specified>",
                "simtype" : "S",
                "static_snapshots" : int(2),
                "sf_ubpconstant": int(0),
                "sf_techplaninclude":int(0),
                "sf_techplanconstant":int(0),
                "sf_techimplinclude":int(0),
                "sf_techimplconstant":int(0),
                "sf_perfinclude":int(0),
                "sd_samedata":'E',
                "sd_sameclimate":int(0),
                "dyn_totyears" : int(50),
                "dyn_startyear" : int(1960),
                "dyn_breaks" : int(5),
                "dyn_irregulardt" : int(0),
                "df_ubpconstant":int(0),
                "df_techplaceconstant":int(0),
                "df_techimplconstant":int(0),
                "df_perfinclude":int(0),
                "df_perfconstant":int(0),
                "dd_samemaster":int(0),
                "dd_sameclimate":int(0),
                "projectpath" : "<none>",
                "projectpathsavedata" : int(0)   }

        self.__projectpath = "C:\\hello\\you\\"

        self.__data_archive_fnames = {
                "Elevation" : [],
                "Soil" : [],
                "Land Use" : [],
                "Population" : [],
                "Employment" : [],
                "Planning" : [],
                "Locality" : [],
                "Groundwater" : [],
                "Rivers" : [],
                "Lakes" : [],
                "Social Parameters" : [],
                "Existing Systems" : [],
                "Rainfall" : [],
                "Evapotranspiration" : [],
                "Solar Radiation" : []                }       #will contain the full library of data for the simulation

        self.__narratives = []  #N narratives based on the number of snapshots or timelines or the single benchmark operation
                                #Will take the form: [heading, narrative] and added to the array

        #MODULES
        self.__delinblocks = []
        self.__urbplanbb = []
        self.__techplacement = []
        self.__techimplement = []
        self.__perfassess = []

        #DATA SETS
        self.__data_geographic_pc = []      #contains the geographic data set for different snapshots/milestones for planning
        self.__data_geographic_ic = []      #contains geographic data set for different snapshots/milestones for implementation
        self.__data_climate = []            #contains climate data set for different snapshots/milestones

        self.__assets = {}            #The Database of the simulation file, which contains ALL the vector information

        #Outputs and File Export Options
        self.__gis_options = {
                "Filename": "unnamed",
                "BuildingBlocks" : int(1),
                "PatchData" : int(0),
                "Flowpaths": int(0),
                "PlannedWSUD" : int(0),
                "ImplementedWSUD" : int(0),
                "CentrePoints" : int(0),
                "Projection": "+proj=utm +zone=55 +south +ellps=WGS84 +datum=WGS84 +units=m +no_defs +towgs84=0,0,0",
                "ProjUser" : int(0),
                "Proj4" : "",
                "Offset" : "I",
                "OffsetCustX" : float(0.0),
                "OffsetCustY" : float(0.0),
                "GoogleEarth" : int(0),
                "Localities" : int(0)   }

        self.__optionsinfo = {}       #contains all the reporting options and other options

    ### --------- UTILITY FUNCTIONS -----------------------------
    def registerObserver(self, observerobj):
        """Registers an object as an observer into the simulation's observer array"""
        self.__observers.append(observerobj)

    def updateObservers(self, message):
        for observer in self.__observers:
            observer.updateObserver(message)

    def updateSimulationCompletion(self, caseupdate):
        self.__simulation_has_completed = int(caseupdate)
        return True
        
    def checkIfSimulationComplete(self):
        return bool(self.__simulation_has_completed)

    def reinitializeThread(self):
        threading.Thread.__init__(self)     #Reinitialize so that the thread can be restarted

    ### ---------- SIMULATION FILE MANIPULATION --------------------
    def getFullFileName(self):
        return self.__filename
    
    def setFullFileName(self, fname):
        self.__filename = fname
        return True

    ### ----------------- INITIALIZATION FUNCTIONS ---------------------
    def initializeSimulationCore(self):
        if self.__projectinfo["simtype"] == "S":
            self.initializeParameterSetsStatic()
        elif self.__projectinfo["simtype"] == "D":
            self.initializeParameterSetsDynamic()
        elif self.__projectinfo["simtype"] == "B":
            self.initializeParameterSetBenchmark()
        return True

    def initializeParameterSetsStatic(self):
        paramlength = self.__projectinfo["static_snapshots"]

        self.__delinblocks.append(md_delinblocks.Delinblocks(self, "pc", 0))         #ONLY ONE DELINBLOCKS NEEDED
        self.__urbplanbb.append(md_urbplanbb.Urbplanbb(self, "pc", 0))         #Add the first one, then check if more needed

        if self.__projectinfo["sf_ubpconstant"] == 0: #if urbplanning rules are NOT to be constant...
            for i in range(int(paramlength-1)):     #add additional urbplan objects
                self.__urbplanbb.append(md_urbplanbb.Urbplanbb(self, "pc", i+1))

        if self.__projectinfo["sf_techplaninclude"] == 1:     #If techplan is included
            self.__techplacement.append(md_techplacement.Techplacement(self, "pc", 0))
            if self.__projectinfo["sf_techplanconstant"] == 0:
                for i in range(int(paramlength-1)):
                    self.__techplacement.append(md_techplacement.Techplacement(self, "pc", i+1))

        if self.__projectinfo["sf_techimplinclude"] == 1:     #If techimplement is included
            self.__techimplement.append(md_techimplement.Techimplement(self, "ic", 0))
            if self.__projectinfo["sf_techimplconstant"] == 0:
                for i in range(int(paramlength-1)):
                    self.__techimplement.append(md_techimplement.Techimplement(self, "ic", i+1))

        #if self.__projectinfo["sf_perfinclude"] == 1:
        #    self.__perf_assess.append(md_perfassess.PerformanceAssess(self, "pc", 0))
        #    #No varying allowed in a static simulation as we are assuming that we're simulating the same catchment

        self.__narratives = []
        for i in range(int(paramlength)):
            self.__narratives.append(["Header"+str(i), "insert current narrative here..."])

        if self.__projectinfo["sf_techimplinclude"] == 1:
            if self.__projectinfo["sd_samedata"] == 'M':   #No change in MASTERPLAN        STATICDATAOPTIONS[0] = 0 --> MASTERPLAN CHANGES
                for i in range(int(paramlength)):                          #STATICDATAOPTIONS[0] = 1 --> MASTERPLAN CONSTANT
                    self.__data_geographic_ic.append({}) #so change the implementation environment data ever cycle
            else:
                self.__data_geographic_ic.append({})

            if self.__projectinfo["sf_techimplinclude"] == 1 and self.__projectinfo["sd_samedata"] == 'E': #No change in implementation environment
                for i in range(int(paramlength)):
                    self.__data_geographic_pc.append({}) #so change the masterplan data every cycle
            else:
                self.__data_geographic_pc.append({})
        else:
            for i in range(int(paramlength)):
                self.__data_geographic_pc.append({})    #else by default just add the required number of placeholders to planning cycle data

        if self.__projectinfo["sf_perfinclude"] == 1:
            if self.__projectinfo["sd_sameclimate"] == 0:   #Change in climate every snapshot
                for i in range(int(paramlength)):                       #STATICDATAOPTIONS[1] = 0 --> CLIMATE CHANGES
                    self.__data_climate.append({})                      #STATICDATAOPTIONS[1] = 1 --> CLIMATE CONSTANT
            else:
                self.__data_climate.append({})
        else:
            pass    #array stays empty

    def initializeParameterSetsDynamic(self):
        paramlength = self.__projectinfo["dyn_breaks"] +1       #n breaks + baseline

        self.__delinblocks.append(md_delinblocks.Delinblocks(self, "pc", 0))         #ONLY ONE DELINBLOCKS NEEDED
        self.__urbplanbb.append(md_urbplanbb.Urbplanbb(self, "pc",0))         #Add the first one, then check if more needed

        if self.__projectinfo["df_ubpconstant"] == 0: #if NOT same urbanplanning rules
            for i in range(int(paramlength-1)):
                self.__urbplanbb.append(md_urbplanbb.Urbplanbb(self, "pc", i+1))

        #self.__techplacement.append(md_techplacement.Techplacement(self, "pc", 0))
        #if self.__projectinfo["df_techplaceconstant"] == 0:
        #    for i in range(int(paramlength-1)):
        #        self.__techplacement.append(md_techplacement.Techplacement(self, "pc", i+1))
        #
        #self.__techimplement.append(md_techimplement.Techimplement(self, "ic", 0))
        #if self.__projectinfo["df_techimplconstant"] == 0:
        #    for i in range(int(paramlength-1)):
        #        self.__techimplement.append(md_techimplement.Techimplement(self, "ic", i+1))
        #
        #if self.__projectinfo["df_perfinclude"] != 0:
        #    self.__perfassess.append(md_perfassess.PerformanceAssess(self, "pc", 0))
        #    if self.__projectinfo["df_perfconstant"] == 0:
        #        for i in range(int(paramlength-1)):
        #            self.__perfassess.append(md_perfassess.PerformanceAssess(self, "pc", i+1))

        if self.__projectinfo["dd_samemaster"] == 0:                     #If masterplan should change
            for i in range(int(paramlength)):
                self.__data_geographic_pc.append({})
        else:
            self.__data_geographic_pc.append({})

        for i in range(int(paramlength)):
            self.__data_geographic_ic.append({})

        if self.__projectinfo["df_perfinclude"] == 1:
            if self.__projectinfo["dd_sameclimate"] == 0:                     #if climate data should change
                for i in range(int(paramlength)):
                    self.__data_climate.append({})
            else:
                self.__data_climate.append({})
        else:
            pass        #Leave climate data array blank with len = 0

    def initalizeParameterSetBenchmark(self):
        self.__delinblocks.append(md_delinblocks.Delinblocks(self, "pc", 0))         #ONLY ONE DELINBLOCKS NEEDED
        self.__urbplanbb.append(md_urbplanbb.Urbplanbb(self, "pc", 0))
#        self.__params_techplacement.append(TechplacementParameterSet("baseline"))
#        self.__params_techimplement.append(TechimplementParameterSet("baseline"))
#        self.__params_perfassess.append(PerformanceParameterSet("baseline"))
        return True

    ### ---------- DATA ARCHIVE & DATA SET MANIPULATION --------------------------
    def addDataToArchive(self, datatype, fname):
        #print datatype
        self.__data_archive_fnames[datatype].append(str(fname))
        return True

    def removeDataFromArchive(self, datatype, fname):
        if datatype == "Rainfall":
            if fname in self.__data_archive_fnames["Evapotranspiration"]:
                datatype = "Evapotranspiration"
            elif fname in self.__data_archive_fnames["Solar Radiation"]:
                datatype = "Solar Radiation"
        if datatype == "Rivers":
            if fname in self.__data_archive_fnames["Lakes"]:
                datatype = "Lakes"
        if datatype == "Population":
            if fname in self.__data_archive_fnames["Employment"]:
                datatype = "Employment"
        try:
            self.__data_archive_fnames[datatype].remove(str(fname))
        except KeyError:
            return True

    def resetDataArchive(self):
        for key in self.__data_archive_fnames:
            self.__data_archive_fnames[key] = []
        return True

    def showDataArchive(self):
        return self.__data_archive_fnames

    def setCycleDataSet(self,curstate, tabindex, dataset):
        if curstate == "pc":
            if len(self.__data_geographic_pc) > 1:
                self.__data_geographic_pc[tabindex] = dataset
            else:
                self.__data_geographic_pc[0] = dataset
        elif curstate == "ic":
            if len(self.__data_geographic_ic) > 1:
                self.__data_geographic_ic[tabindex] = dataset
            else:
                self.__data_geographic_ic[0] = dataset
        elif curstate == "pa":
            if len(self.__data_climate) > 1:
                self.__data_climate[tabindex] = dataset
            else:
                self.__data_climate[0] = dataset
        return True

    def getCycleDataSet(self, curstate, tabindex):
        if curstate == "pc":
            if len(self.__data_geographic_pc) > 1:
                return self.__data_geographic_pc[tabindex]
            else:
                return self.__data_geographic_pc[0]

        if curstate == "ic":
            if len(self.__data_geographic_ic) > 1:
                return self.__data_geographic_ic[tabindex]
            else:
                return self.__data_geographic_ic[0]
        
        if curstate == "pa":
            if len(self.__data_climate) > 1:
                return self.__data_climate[tabindex]
            else:
                return self.__data_climate[0]
        return True
        
    def getAllCycleDataSets(self, curstate):
        if curstate == "pc":
            return self.__data_geographic_pc
        elif curstate == "ic":
            return self.__data_geographic_ic
        elif curstate == "pa":
            return self.__data_climate
        else:
            return 0

    def printAllDataSets(self):
        return [self.__data_geographic_pc, self.__data_geographic_ic, self.__data_climate]

    ### -------------- PARAMETER MANIPULATION ---------------------------
    def setParameter(self, name, value):
        self.__projectinfo[name] = value
        return True
    
    def getParameter(self, name):
        try:
            return self.__projectinfo[name]
        except KeyError:
            return None

    def setNarrative(self, tabindex, narrative):
        if tabindex == 9999:
            self.__narratives = narrative
        else:
            self.__narratives[tabindex] = narrative

    def getNarrative(self, tabindex):
        try:
            return self.__narratives[tabindex]
        except IndexError:
            return ["none", "none"]

    def getAllNarratives(self):
        return self.__narratives

    def getProjectDetails(self):
        return self.__projectinfo

    def getGISExportDetails(self):
        return self.__gis_options

    def setGISExportDetails(self, name, value):
        if name in self.__gis_options:  #if the key exists, set the 
            self.__gis_options[name] = value
        return True

    def getActiveProjectPath(self):
        return self.__projectpath        
    
    def setActiveProjectPath(self, pathname):
        self.__projectpath = pathname
        return True

    ### --------------- MODULES -------------------------------
    def getLengthOfModulesVector(self, modulevector):
        if modulevector == "urbplanbb":
            vec_length = len(self.__urbplanbb)
        elif modulevector == "techplacement":
            vec_length = len(self.__techplacement)
        elif modulevector == "techimplement":
            vec_length = len(self.__techimplement)
        elif modulevector == "perf_assess":
            vec_length = len(self.__perf_assess)
        return vec_length
    
    def getModuleDelinblocks(self):
        return self.__delinblocks[0]

    def getModuleUrbplanbb(self, index):
        if index == 9999:
            return self.__urbplanbb
        else:
            if len(self.__urbplanbb) == 1:
                return self.__urbplanbb[0]
            return self.__urbplanbb[index]

    def getModuleTechplacement(self, index):
        if index == 9999:
            return self.__techplacement
        else:
            if len(self.__techplacement) == 1:
                return self.__techplacement[0]
            return self.__techplacement[index]

    def getModuleTechimplement(self, index):
        if index == 9999:
            return self.__techimplement
        else:
            if len(self.__techimplement) == 1:
                return self.__techimplement[0]
            return self.__techimplement[index]

    def getModulePerfAssess(self, index):
        if index == 9999:
            return self.__perfassess
        else:
            if len(self.__perfassess) == 1:
                return self.__perfassess[0]
            return self.__perfassess[index]

    def printAllModules(self):
        return [self.__delinblocks, self.__urbplanbb, self.__techplacement, self.__techimplement, self.__perfassess]

    ### ----------- SIMULATION DATA TYPE MANIPULATION ------------------------
    def addAsset(self, name, asset):
        """Adds a new asset to the asset dictionary with the key 'name'"""
        self.__assets[name] = asset
        return True

    def getAssetWithName(self, name):
        """Returns the Asset Object with the key 'name' from the asset collection"""
        return self.__assets[name]

    def getAssetsWithIdentifier(self, idstring):
        """Scans the complete Asset List and returns all assets with the idstring contained
        in their name (e.g. BlockID contained in the name "BlockID1", "BlockID2", etc.)
        """
        assetcollection = []
        for i in self.__assets:
            if idstring in i:
                assetcollection.append(self.__assets[i])
        return assetcollection

    def resetAssets(self):
        """Erases all assets, leaves an empty dictionary, carried out when resetting the simulation"""
        self.__assets = {}
        gc.collect()
        self.updateObservers("PROGRESSUPDATE||0")
        return True

    def returnAllAssets(self):
        """Returns the dictionary containing all assets from the simulation"""
        return self.__assets

    def exportGIS(self):
        """Calls the Shapefile Export function from urbanbeatsdatatypes"""
        ubdata.exportGISShapeFile(self)
        return True

    def run(self):
        self.updateObservers("Starting Simulation")

        #-------------------- BASIC SIMULATION STRUCTURE BEGINS HERE -----------------

        self.updateObservers("PROGRESSUPDATE||10")
        delinblocks = self.getModuleDelinblocks()
        delinblocks.attach(self.__observers)   #Register the observer
        delinblocks.run()
        delinblocks.detach(self.__observers)   #Deregister the observer after run completion
        self.updateObservers("PROGRESSUPDATE||30")

        urbplanbb = self.getModuleUrbplanbb(0)
        urbplanbb.attach(self.__observers)  #Register the observer
        urbplanbb.run()
        urbplanbb.detach(self.__observers)
        self.updateObservers("PROGRESSUPDATE||70")

        self.exportGIS()
        self.updateObservers("PROGRESSUPDATE||90")
        #self.exportGIS()

        #----------------- BASIC SIMULATION STRUCTURE ENS HERE ------------------
        self.updateObservers("End of Simulation")
        self.updateObservers("PROGRESSUPDATE||100")
        #END OF SIMULATION
