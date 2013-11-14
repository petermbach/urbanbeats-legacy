# -*- coding: utf-8 -*-
"""
@file
@author  Peter M Bach <peterbach@gmail.com>
@version 0.5
@section LICENSE

This file is part of VIBe2
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

#------ IMPORTS --------------
#Regular imports
import threading, gc, os

#Dependencies
import urbanbeatsdatatypes as ubdata

#Modules
import md_delinblocks, md_urbplanbb, md_techplacement, md_techimplement#, md_perfassess
import md_getpreviousblocks, md_getsystems, md_writeMUSICsim


emptyBlockPath = os.path.dirname(__file__)+str("/ancillary/emptyblockmap.shp")
emptySysPath = os.path.dirname(__file__)+str("/ancillary/emptysystemsmap.shp")

# ------ CLASS DEFINITION -------
class UrbanBeatsSim(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        #Simulation object of UrbanBEATS, contains the full details of one simulation

        #Observer, Status and Filename
        self.__observers = []         #Observers of the current simulation
        self.__simulation_has_completed = 0
        self.__filename= ""                 #Filename of the simulation
        self.__tabs = 1
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

        self.__basename_archive = {}        #Contains the basename vs. full path name translations

        self.__narratives = []  #N narratives based on the number of snapshots or timelines or the single benchmark operation
                                #Will take the form: [heading, narrative] and added to the array

        #MODULES
        self.__delinblocks = []
        self.__urbplanbb = []
        self.__techplacement = []
        self.__techimplement = []
        self.__perfassess = []

        self.__getprevBlocks = []   #md_getpreviousblocks module, is initialize and parameters automatically set based on project details ["pc", "ic"]
        self.__getSystems = []      #md_getsystems module, parameters set based on cycle data set and whether dynamic simulation ["pc", "ic"]
        self.__musicexport = []     #md_writeMUSICsim

        #DATA SETS
        self.__data_geographic_pc = []      #contains the geographic data set for different snapshots/milestones for planning
        self.__data_geographic_ic = []      #contains geographic data set for different snapshots/milestones for implementation
        self.__data_climate = []            #contains climate data set for different snapshots/milestones

        self.__assets = {}            #The Database of the simulation file, which contains ALL the vector information
        self.__assetscollection = {"pc":[], "ic":[]}    #Holds ALL assets for the entire simulation

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

        self.__delinblocks.append(md_delinblocks.Delinblocks(self, 0))         #ONLY ONE DELINBLOCKS NEEDED
        self.__urbplanbb.append(md_urbplanbb.Urbplanbb(self, 0))         #Add the first one, then check if more needed
        self.__getprevBlocks.append(md_getpreviousblocks.GetPreviousBlocks(self, 0))  #planning cycle modules

        if self.__projectinfo["sf_ubpconstant"] == 0: #if urbplanning rules are NOT to be constant...
            for i in range(int(paramlength-1)):     #add additional urbplan objects
                self.__urbplanbb.append(md_urbplanbb.Urbplanbb(self, i+1))

        if self.__projectinfo["sf_techplaninclude"] == 1:     #If techplan is included
            self.__musicexport.append(md_writeMUSICsim.WriteResults2MUSIC(self, 0))
            self.__techplacement.append(md_techplacement.Techplacement(self, 0))
            self.__getSystems.append(md_getsystems.GetSystems(self, 0))
            if self.__projectinfo["sf_techplanconstant"] == 0:
                for i in range(int(paramlength-1)):
                    self.__techplacement.append(md_techplacement.Techplacement(self, i+1))

        if self.__projectinfo["sf_techimplinclude"] == 1:     #If techimplement is included
            self.__getSystems.append(md_getsystems.GetSystems(self, 0))
            self.__techimplement.append(md_techimplement.Techimplement(self, 0))
            self.__getprevBlocks.append(md_getpreviousblocks.GetPreviousBlocks(self, 0))
            if self.__projectinfo["sf_techimplconstant"] == 0:
                for i in range(int(paramlength-1)):
                    self.__techimplement.append(md_techimplement.Techimplement(self, i+1))

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

        self.__tabs = int(paramlength)
        #FINISHED INITIALIZATION
        self.updateObservers(str(self.getAllCycleDataSets("pc")))
        self.updateObservers(str(self.printAllModules()))

    def initializeParameterSetsDynamic(self):
        paramlength = self.__projectinfo["dyn_breaks"] +1       #n breaks + baseline

        self.__delinblocks.append(md_delinblocks.Delinblocks(self, 0))         #ONLY ONE DELINBLOCKS NEEDED
        self.__urbplanbb.append(md_urbplanbb.Urbplanbb(self, 0))         #Add the first one, then check if more needed
        self.__getprevBlocks.append(md_getpreviousblocks.GetPreviousBlocks(self, 0))  #planning cycle modules

        if self.__projectinfo["df_ubpconstant"] == 0: #if NOT same urbanplanning rules
            for i in range(int(paramlength-1)):
                self.__urbplanbb.append(md_urbplanbb.Urbplanbb(self, i+1))

        self.__getSystems.append(md_getsystems.GetSystems(self, 0))
        self.__techplacement.append(md_techplacement.Techplacement(self, 0))
        if self.__projectinfo["df_techplaceconstant"] == 0:
            for i in range(int(paramlength-1)):
                self.__techplacement.append(md_techplacement.Techplacement(self, i+1))

        self.__techimplement.append(md_techimplement.Techimplement(self, 0))
        self.__getprevBlocks.append(md_getpreviousblocks.GetPreviousBlocks(self, 0))
        self.__getSystems.append(md_getsystems.GetSystems(self, 0))
        if self.__projectinfo["df_techimplconstant"] == 0:
            for i in range(int(paramlength-1)):
                self.__techimplement.append(md_techimplement.Techimplement(self, i+1))

        #if self.__projectinfo["df_perfinclude"] != 0:
        #    self.__perfassess.append(md_perfassess.PerformanceAssess(self, "pc", 0))
        #    if self.__projectinfo["df_perfconstant"] == 0:
        #        for i in range(int(paramlength-1)):
        #            self.__perfassess.append(md_perfassess.PerformanceAssess(self, "pc", i+1))

        self.__narratives = []
        for i in range(int(paramlength)):
            self.__narratives.append(["Header"+str(i), "insert current narrative here..."])

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

        self.__tabs = int(paramlength)
        #End of Initialization
        self.updateObservers(str(self.getAllCycleDataSets("pc")))
        self.updateObservers(str(self.printAllModules()))

    def initalizeParameterSetBenchmark(self):
        self.__delinblocks.append(md_delinblocks.Delinblocks(self, 0))         #ONLY ONE DELINBLOCKS NEEDED
        self.__urbplanbb.append(md_urbplanbb.Urbplanbb(self, 0))
#        self.__params_techplacement.append(TechplacementParameterSet("baseline"))
#        self.__params_techimplement.append(TechimplementParameterSet("baseline"))
#        self.__params_perfassess.append(PerformanceParameterSet("baseline"))
        return True

    ### ---------- DATA ARCHIVE & DATA SET MANIPULATION --------------------------
    def addDataToArchive(self, datatype, fname):
        #print datatype
        self.__data_archive_fnames[datatype].append(str(fname))
        self.__basename_archive[os.path.basename(str(fname))] = str(fname)
        print fname
        print os.path.basename(fname)
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
            fpath = self.__basename_archive[fname]
            self.__data_archive_fnames[datatype].remove(str(fpath))
            self.__basename_archive.pop(str(fname))
        except KeyError:
            print "Something wrong"
            return True

    def resetDataArchive(self):
        for key in self.__data_archive_fnames:
            self.__data_archive_fnames[key] = []
        self.__basename_archive = {}
        return True

    def showDataArchive(self):
        return self.__data_archive_fnames

    def setCycleDataSet(self, curstate, tabindex, dataset, fnameoption):
        if fnameoption == "B":  #Basename in the arrays? Refer to dictionary
            datasetfull = {}
            for dt in dataset.keys():
                datasetfull[dt] = self.__basename_archive[dataset[dt]]
        else:
            datasetfull = dataset
        if curstate == "pc":
            if len(self.__data_geographic_pc) > 1:
                self.__data_geographic_pc[tabindex] = datasetfull
            else:
                self.__data_geographic_pc[0] = datasetfull
        elif curstate == "ic":
            if len(self.__data_geographic_ic) > 1:
                self.__data_geographic_ic[tabindex] = datasetfull
            else:
                self.__data_geographic_ic[0] = datasetfull
        elif curstate == "pa":
            if len(self.__data_climate) > 1:
                self.__data_climate[tabindex] = datasetfull
            else:
                self.__data_climate[0] = datasetfull
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

    def removeAssetByName(self, name):
        """Remove an asset from the collection based on the name"""
        try:
            del self.__assets[name]
        except KeyError:
            return True

    def resetAssets(self):
        """Erases all assets, leaves an empty dictionary, carried out when resetting the simulation"""
        self.__assets = {}
        gc.collect()
        return True

    def resetAssetCollection(self):
        """Resets the asset collection completely"""
        self.__assetscollection = {"pc": [], "ic": []}
        gc.collect()
        self.updateObservers("PROGRESSUPDATE||0")
        return True

    def returnAllAssets(self):
        """Returns the dictionary containing all assets from the simulation"""
        return self.__assets

    def debugAssets(self, assetid, attname):
        """Returns the attribute value denoted by attname of all assets that have the identifier assetid"""
        assets = self.getAssetsWithIdentifier(assetid)
        print assets
        for i in assets:
            print i.getAttribute("BlockID"), i.getAttribute(attname)

    def retrieveAssetsFromCollection(self, cycle, tabindex):
        """To be used only once the simulation has completed, returns assets
        from a particular cycle and snapshot/time period to be used in plotting results
        """
        try:
            return self.__assetscollection[cycle][tabindex]
        except KeyError:
            return 0

    def transferCurrentAssetsToCollection(self, cycle):
        """Transfers the current Assets in self.__assets to the asset collection
        to be used later in viewing results, etc."""
        self.__assetscollection[cycle].append(self.__assets)
        return True

    def exportGIS(self, tabindex, curcycle):
        """Calls the Shapefile Export function from urbanbeatsdatatypes"""
        ubdata.exportGISShapeFile(self, tabindex, curcycle)
        return True

    def run(self):
        self.updateObservers("Starting Simulation")

        if len(self.__techimplement) == 0:
            progressincrement = 1.0/float(self.__tabs)   #1 divided by number of tabs e.g. 4 tabs, each tab will be 25% of progress bar
        else:
            progressincrement = 1.0/(float(self.__tabs * 2.0))  #if there is implementation, one progress increment is twice as short

        incrementcount = 0.0
        for tab in range(self.__tabs):
            #Current iteration index = tab's value
            self.updateObservers("Tab No. "+str(tab+1))
            #-------------------- BASIC SIMULATION STRUCTURE BEGINS HERE -----------------
            #----------------------------------------#
            #PLANNING CYCLE START                    #
            #----------------------------------------#
            self.resetAssets()  #Reset the asset vector
            #(1) Set files for previous systems and blocks
            if tab == 0:
                self.__getprevBlocks[0].setParameter("block_path_name", emptyBlockPath)
                self.__getprevBlocks[0].setParameter("patchesavailable", 0)
                self.__getprevBlocks[0].setParameter("patch_path_name", emptyBlockPath)
                self.__getprevBlocks[0].setParameter("patchesavailable", 0)
            else:
                self.__getprevBlocks[0].setParameter("block_path_name", emptyBlockPath) #PREVIOUS SIMULATION
                self.__getprevBlocks[0].setParameter("patchesavailable", 0)
                self.__getprevBlocks[0].setParameter("patch_path_name", emptyBlockPath)
                self.__getprevBlocks[0].setParameter("patchesavailable", 0)
                #Set previous simulation files name+tab-1
                pass

            #(2) Delinblocks
            self.updateObservers("PROGRESSUPDATE||"+str(int(10.0*progressincrement+incrementcount)))
            delinblocks = self.getModuleDelinblocks()
            delinblocks.setParameter("curcycle", "pc")
            delinblocks.setParameter("tabindex", tab)
            delinblocks.attach(self.__observers)   #Register the observer
            delinblocks.run()
            delinblocks.detach(self.__observers)   #Deregister the observer after run completion
            self.updateObservers("PROGRESSUPDATE||"+str(int(20.0*progressincrement+incrementcount)))

            #(3) Urbplanbb
            getPrevBlocks = self.__getprevBlocks[0]
            getPrevBlocks.attach(self.__observers)
            getPrevBlocks.run()
            getPrevBlocks.detach(self.__observers)
            self.updateObservers("PROGRESSUPDATE||"+str(int(30.0*progressincrement+incrementcount)))

            urbplanbb = self.getModuleUrbplanbb(tab)
            urbplanbb.attach(self.__observers)  #Register the observer
            urbplanbb.run()
            urbplanbb.detach(self.__observers)
            self.updateObservers("PROGRESSUPDATE||"+str(int(50.0*progressincrement+incrementcount)))

            #(4) Techplacement
            if len(self.__techplacement) > 0:
                if tab == 0:
                    self.__getSystems[0].setParameter("ubeats_file", 1)
                    self.__getSystems[0].setParameter("path_name", emptySysPath)
                else:
                    pass

                getSystems = self.__getSystems[0]
                getSystems.attach(self.__observers)
                getSystems.run()
                getSystems.detach(self.__observers)
                self.updateObservers("PROGRESSUPDATE||"+str(int(60.0*progressincrement+incrementcount)))

                techplacement = self.getModuleTechplacement(tab)
                techplacement.attach(self.__observers)
                techplacement.run()
                techplacement.detach(self.__observers)

                musicExport = self.__musicexport[0]
                musicExport.setParameter("pathname", str(self.getActiveProjectPath))
                musicExport.setParameter("filename", "MUSICSim")
                musicExport.setParameter("masterplanmodel", 1)
                musicExport.setParameter("currentyear", tab)
                musicExport.attach(self.__observers)
                musicExport.run()
                musicExport.detach(self.__observers)

            self.updateObservers("PROGRESSUPDATE||"+str(int(80.0*progressincrement+incrementcount)))

            #(5) Export
            self.updateObservers("PROGRESSUPDATE||"+str(int(90.0*progressincrement+incrementcount)))
            self.transferCurrentAssetsToCollection("pc")
            self.exportGIS(tab, "pc")
            self.updateObservers("PROGRESSUPDATE||"+str(int(100.0*progressincrement+incrementcount)))
            incrementcount += 100.0*progressincrement

            #----------------------------------------#
            #IMPLEMENTATION CYCLE START (IF SELECTED)#
            #----------------------------------------#
            if len(self.getModuleTechimplement(9999)) == 0:
                continue    #Skip the loop, otherwise implement stuff
            self.resetAssets()  #Reset the asset vector
            incrementcount += 1

            #(1) Set parameters for modules that load previous blocks and systems
            #self.__getprevBlocks[0].setParameter("block_path_name", emptyBlockPath)
            #self.__getprevBlocks[0].setParameter("patchesavailable", 0)
            #self.__getprevBlocks[0].setParameter("patch_path_name", emptyBlockPath)
            #self.__getprevBlocks[0].setParameter("patchesavailable", 0)

            #(2) Delinblocks
            self.updateObservers("PROGRESSUPDATE||"+str(int(10*progressincrement+incrementcount)))
            delinblocks = self.getModuleDelinblocks()
            delinblocks.setParameter("curcycle", "ic")
            delinblocks.setParameter("tabindex", tab)
            delinblocks.attach(self.__observers)   #Register the observer
            delinblocks.run()
            delinblocks.detach(self.__observers)   #Deregister the observer after run completion
            self.updateObservers("PROGRESSUPDATE||"+str(int(30*progressincrement+incrementcount)))

            #(3) Urbplanbb
            #getPrevBlocks = self.__getprevBlocks[0]
            #getPrevBlocks.attach(self.__observers)
            #getPrevBlocks.run()
            #getPrevBlocks.detach(self.__observers)
            self.updateObservers("PROGRESSUPDATE||"+str(int(30.0*progressincrement+incrementcount)))

            self.updateObservers("PROGRESSUPDATE||"+str(int(40*progressincrement+incrementcount)))

            self.updateObservers("PROGRESSUPDATE||"+str(int(60*progressincrement+incrementcount)))

            #(4) Techimplement
            #self.__getSystems[0].setParameter("ubeats_file", 1)
            #self.__getSystems[0].setParameter("path_name", emptySysPath)
            self.updateObservers("PROGRESSUPDATE||"+str(int(70*progressincrement+incrementcount)))



            self.updateObservers("PROGRESSUPDATE||"+str(int(90*progressincrement+incrementcount)))

            #(5) Export
            #musicExport = self.__getModuleWrite2MUSIC[0]
            #musicExport.setParameter("curcycle", "ic")
            #musicExport.setParameter("tabindex", tab)
            #musicExport.attach(self.__observers)
            #musicExport.run()
            #musicExport.detach(self.__observers)
            self.updateObservers("PROGRESSUPDATE||"+str(int(90.0*progressincrement+incrementcount)))

            self.transferCurrentAssetsToCollection("ic")
            self.exportGIS(tab, "ic")
            self.updateObservers("PROGRESSUPDATE||"+str(int(100*progressincrement+incrementcount)))
            incrementcount += 100.0*progressincrement

        #----------------- BASIC SIMULATION STRUCTURE ENS HERE ------------------
        self.updateObservers("End of Simulation")
        self.updateObservers("PROGRESSUPDATE||100")
        #END OF SIMULATION
