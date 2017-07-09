# -*- coding: utf-8 -*-
"""
@file
@author  Peter M Bach <peterbach@gmail.com>
@version 0.5
@section LICENSE

This file is part of UrbanBEATS
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

import urbanbeatscore as ubc
import urbanbeatsfiles as ubfiles
import urbanbeatsdialogs as ubdialogs
import urbanbeatsresults as ubresults
import urbanbeatssummaries as ubsum
import ubscripts

from urbanbeatsmaingui import Ui_urbanbeatsMain
from startscreen import Ui_StartDialog
import sys, time, os, random
import webbrowser, subprocess
from PyQt4 import QtGui, QtCore, QtWebKit

import md_delinblocksguic
import md_urbplanbbguic
import md_techplacementguic
import md_techimplementguic
import md_perfassessguic
import urbanbeatscalibration

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent = None):
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_urbanbeatsMain()
        self.ui.setupUi(self)
        self.ui.ubeatsConsole.appendPlainText("=====================================")
        self.ui.ubeatsConsole.appendPlainText("UrbanBEATS OUTPUT CONSOLE")
        self.ui.ubeatsConsole.appendPlainText("===================================== \n")
        self.printc("Started UrbanBEATS")
        #Disable all simulation options first until we have a project open
        self.enabledisable_sim_guis(0)

        self.consoleobserver = ConsoleObserver()
        #self.progressobserver = ProgressObserver()

        self.__dtype_names = ["Elevation", "Soil", "Land Use", "Population",  "Employment", "Planning", "Locality", "Groundwater", "Rivers", "Lakes", "Social Parameters", "Existing WSUD", "Existing Network", "Rainfall", "Evapotranspiration", "Solar Radiation"]
        
        #ATTRIBUTES
        self.__activeSimulationObject = None
        self.__activeprojectpath = "C:\\"
        self.__global_options = {"numstrats":5,
                                 "city": "Melbourne",
                                 "mapstyle": "Style1",
                                 "tileserverURL": "",
                                 "gearth_path": "",
                                 "defaultmodeller": "",
                                 "decisiontype": "H",
                                 "iterations": 1000,
                                 "defaultaffil":"",
                                 "gearth_auto": 0 ,
                                 "default_path":1,
                                 "temp_dir": ""}
        
        ###########################################
        ### GUI Signals & Slots                 ###
        ###########################################
        #File Menu
        self.connect(self.ui.actionNew, QtCore.SIGNAL("triggered()"), self.beginNewProjectDialog)
        self.connect(self.ui.actionOpen, QtCore.SIGNAL("triggered()"), self.openExistingProject)
        self.connect(self.ui.actionSave, QtCore.SIGNAL("triggered()"), self.saveProject)
        self.connect(self.ui.actionSave_As, QtCore.SIGNAL("triggered()"), self.saveProjectAs)
        #self.connect(self.ui.actionImportProject, QtCore.SIGNAL("triggered()"), self.importProject)
        #self.connect(self.ui.actionExportProject, QtCore.SIGNAL("triggered()"), self.exportProject)
        #Quit function already implemented        
        #----------------------------------------------------------------------------------------------<<<
        
        #Edit Menu
        #cut, copy, paste
        self.connect(self.ui.actionEdit_Project_Info, QtCore.SIGNAL("triggered()"), self.editProjectInfo)
        self.connect(self.ui.actionPreferences, QtCore.SIGNAL("triggered()"), self.editPreferences)
        #----------------------------------------------------------------------------------------------<<<        
        
        #View Menu
        self.connect(self.ui.actionProject_Description, QtCore.SIGNAL("triggered()"), self.viewProjectInfo)
        self.connect(self.ui.actionSimulation_Results, QtCore.SIGNAL("triggered()"), self.showResultsBrowseDialog)
        #----------------------------------------------------------------------------------------------<<<
        
        #Data Menu
        self.connect(self.ui.actionAddData, QtCore.SIGNAL("triggered()"), self.showAddDataDialog)
        self.connect(self.ui.actionImport_UDA, QtCore.SIGNAL("triggered()"), lambda filetype="uda": self.importDataArchive(filetype))
        self.connect(self.ui.actionImport_UDAfromUBS, QtCore.SIGNAL("triggered()"), lambda filetype="ubs": self.importDataArchive(filetype))
        self.connect(self.ui.actionExportDataArchive, QtCore.SIGNAL("triggered()"), self.exportDataArchive)
        self.connect(self.ui.addDataButton, QtCore.SIGNAL("clicked()"), self.showAddDataDialog)
        self.connect(self.ui.removeDataButton, QtCore.SIGNAL("clicked()"), self.removeDataEntry)
        self.connect(self.ui.collex_button, QtCore.SIGNAL("clicked()"), self.collexTreeWidget)        
        self.connect(self.ui.actionElevation_Data, QtCore.SIGNAL("triggered()"), lambda dtype="Elevation": self.directAddData(dtype))
        self.connect(self.ui.actionSoil_Data, QtCore.SIGNAL("triggered()"), lambda dtype="Soil": self.directAddData(dtype))
        self.connect(self.ui.actionLand_Use, QtCore.SIGNAL("triggered()"), lambda dtype="Land Use": self.directAddData(dtype))
        self.connect(self.ui.actionPopulation, QtCore.SIGNAL("triggered()"), lambda dtype="Population": self.directAddData(dtype))
        self.connect(self.ui.actionPlanning, QtCore.SIGNAL("triggered()"), lambda dtype="Planning": self.directAddData(dtype))
        self.connect(self.ui.actionLocality_Map, QtCore.SIGNAL("triggered()"), lambda dtype="Locality": self.directAddData(dtype))
        self.connect(self.ui.actionSocial_Data, QtCore.SIGNAL("triggered()"), lambda dtype="Social": self.directAddData(dtype))
        self.connect(self.ui.actionRainfall, QtCore.SIGNAL("triggered()"), lambda dtype="Rainfall": self.directAddData(dtype))        
        self.connect(self.ui.actionEvapotranspiration, QtCore.SIGNAL("triggered()"), lambda dtype="Evapotranspiration": self.directAddData(dtype))
        self.connect(self.ui.actionSolar_Radiation, QtCore.SIGNAL("triggered()"), lambda dtype="Solar Radiation": self.directAddData(dtype))        
        self.connect(self.ui.actionReset_Project_Databank, QtCore.SIGNAL("triggered()"), lambda asc=1: self.resetDatabank(asc))
        self.connect(self.ui.actionCross_check_GIS_Extents, QtCore.SIGNAL("triggered()"), self.crosscheckGIS)
        self.connect(self.ui.actionView_Active_Simulation_Data, QtCore.SIGNAL("triggered()"), self.viewSimData)
        #----------------------------------------------------------------------------------------------<<<

        #Reporting Buttons
        self.connect(self.ui.out_textrep_select, QtCore.SIGNAL("clicked()"), self.showReportingOptionsDialog)        
        self.connect(self.ui.out_gis_maps, QtCore.SIGNAL("clicked()"), self.showGISOptionsDialog)
        self.connect(self.ui.out_gis_customize, QtCore.SIGNAL("clicked()"), self.showGISAdvancedDialog)
        self.connect(self.ui.out_resultsbrowse, QtCore.SIGNAL("clicked()"), self.showResultsBrowseDialog)
        self.connect(self.ui.out_projectfolder, QtCore.SIGNAL("clicked()"), self.openActiveProjectFolder)        
        
        #Simulation Menu
        self.connect(self.ui.pc_narrative, QtCore.SIGNAL("clicked()"), self.callNarrativeGui)
        self.connect(self.ui.actionSet_Spatial_Delineation, QtCore.SIGNAL("triggered()"), self.callDelinblocksGui)
        self.connect(self.ui.pc_delinblocks, QtCore.SIGNAL("clicked()"), self.callDelinblocksGui)
        self.connect(self.ui.actionDefine_Urban_Planning_Rules, QtCore.SIGNAL("triggered()"), self.callUrbplanbbGui)
        self.connect(self.ui.pc_urbplanbb, QtCore.SIGNAL("clicked()"), self.callUrbplanbbGui)
        self.connect(self.ui.actionCustomize_Technologies, QtCore.SIGNAL("triggered()"), self.callTechplacementGui)
        self.connect(self.ui.pc_techplacement, QtCore.SIGNAL("clicked()"), self.callTechplacementGui)
        self.connect(self.ui.actionTechnology_Implementation, QtCore.SIGNAL("triggered()"), self.callTechimplementGui)
        self.connect(self.ui.ic_techimplement, QtCore.SIGNAL("clicked()"), self.callTechimplementGui)
        self.connect(self.ui.actionPerformance_Assessment, QtCore.SIGNAL("triggered()"), self.callPrepareperfGui)
        self.connect(self.ui.pa_assess, QtCore.SIGNAL("clicked()"), self.callPrepareperfGui)
        self.connect(self.ui.actionVerify_Simulation_Setup, QtCore.SIGNAL("triggered()"), self.verifySimulation)
        self.connect(self.ui.resetSimButton, QtCore.SIGNAL("clicked()"), self.resetSimulationAssets)
        self.connect(self.ui.actionReset_Simulation, QtCore.SIGNAL("triggered()"), self.resetSimulationAssets)
        self.connect(self.ui.actionRun_Simulation, QtCore.SIGNAL("triggered()"), self.checks_before_run)
        self.connect(self.ui.runButton, QtCore.SIGNAL("clicked()"), self.checks_before_run)
        self.connect(self.ui.pc_dataset, QtCore.SIGNAL("clicked()"), lambda curstate="pc": self.customize_dataset(curstate))
        self.connect(self.ui.ic_dataset, QtCore.SIGNAL("clicked()"), lambda curstate="ic": self.customize_dataset(curstate))
        self.connect(self.ui.pa_dataset, QtCore.SIGNAL("clicked()"), lambda curstate="pa": self.customize_dataset(curstate))
        self.connect(self.ui.revise_check, QtCore.SIGNAL("clicked()"), self.updateSimulationRevisionPlan)
        #----------------------------------------------------------------------------------------------<<<
                        
        #Advanced Menu
        #most advanced parameters disabled for now
        self.connect(self.ui.actionOutput_Options, QtCore.SIGNAL("triggered()"), self.editOutputOptions)
        self.connect(self.ui.actionModel_Calibration_Viewer, QtCore.SIGNAL("triggered()"), self.callCalibrationGui)
        #----------------------------------------------------------------------------------------------<<<
                
        #Window Menu
        #Minimize function already implemented        
        #----------------------------------------------------------------------------------------------<<<
        
        #Help Menu
        self.connect(self.ui.actionAbout, QtCore.SIGNAL("triggered()"), self.showAboutDialog)
        self.connect(self.ui.actionUrbanBEATS_Wiki, QtCore.SIGNAL("triggered()"), self.showHelp)        
        self.connect(self.ui.actionLike_on_Facebook, QtCore.SIGNAL("triggered()"), self.likeOnFacebook)
        #Like on Google+
        #Tweet        
        #----------------------------------------------------------------------------------------------<<<

        self.connect(self.ui.simconfig_tabs, QtCore.SIGNAL("currentChanged(int)"), self.updateSummaryBox)

        self.connect(self.consoleobserver, QtCore.SIGNAL("updateConsole"), self.printc)

        #self.connect(self.progressbarobserver, QtCore.SIGNAL("updateProgress"), self.updateProgressBar)

        #Module Checkboxes and Performance Rerun button
        self.connect(self.ui.md_techplacement_check, QtCore.SIGNAL("clicked()"), self.enabledisable_sim_modules)
        self.connect(self.ui.md_techimplement_check, QtCore.SIGNAL("clicked()"), self.enabledisable_sim_modules)
        self.connect(self.ui.md_perfassess_check, QtCore.SIGNAL("clicked()"), self.enabledisable_sim_modules)
        self.connect(self.ui.rerun_perfassess, QtCore.SIGNAL("clicked()"), self.run_simulation_perfonly)
        #----------------------------------------------------------------------------------------------<<<

    def createNewProjectInstance(self):
        newsimulation = ubc.UrbanBeatsSim(UBEATSROOT)
        newsimulation.registerObserver(self.consoleobserver)
        return newsimulation
    
    ################################
    ## Getters and Setters        ##
    ################################
    def setActiveSimulationObject(self, simobjectfromcore):
        self.__activeSimulationObject = simobjectfromcore
        return True

    def getActiveSimulationObject(self):
        return self.__activeSimulationObject
    
    def setActiveProjectPath(self, pathname):
        self.__activeprojectpath = pathname
        return True
    
    def getActiveProjectPath(self):
        return self.__activeprojectpath
        
    def printc(self, textmessage):
        if "PROGRESSUPDATE" in str(textmessage):
            progress = textmessage.split('||')
            self.updateProgressBar(int(progress[1]))
        else:
            self.ui.ubeatsConsole.appendPlainText(str(time.asctime())+" | "+str(textmessage))
        return True

    def setOptionsFromConfig(self, root_directory):
        """Sets current program options based on the .cfg file in the root folder"""
        self.__global_options = ubfiles.readGlobalOptionsConfig(root_directory)
        return True

    def getConfigOptions(self, name):
        if name == "all":
            return self.__global_options
        else:
            return self.__global_options[name]

    def setConfigOptions(self, name, value):
        self.__global_options[name] = type(self.__global_options[name])(value)

    def updateConfigFromOptions(self):
        """Updates the configuration of the program and its simulations by overwriting the config file"""
        ubfiles.updateCFGFromOptions(self.__global_options, UBEATSROOT)
        return True

    def resetConfigFile(self):
        ubfiles.resetGlobalOptions(UBEATSROOT)
        self.setOptionsFromConfig(UBEATSROOT)
        return True

    ################################
    ## GUI Preparation Functions  ##
    ################################
    
    def enabledisable_sim_guis(self, setstate):        
        self.ui.pc_dataset.setEnabled(setstate)
        self.ui.pc_narrative.setEnabled(setstate)
        self.ui.pc_delinblocks.setEnabled(setstate)
        self.ui.pc_delinblocks_help.setEnabled(setstate)
        self.ui.pc_urbplanbb.setEnabled(setstate)
        self.ui.pc_urbplanbb_help.setEnabled(setstate)
        self.ui.pc_techplacement.setEnabled(setstate)
        self.ui.pc_techplacement_help.setEnabled(setstate)
        self.ui.ic_dataset.setEnabled(setstate)
        self.ui.ic_techimplement.setEnabled(setstate)
        self.ui.ic_techimplement_help.setEnabled(setstate)
        self.ui.pa_dataset.setEnabled(setstate)  
        self.ui.pa_assess.setEnabled(setstate)
        self.ui.pa_assess_help.setEnabled(setstate)
        self.ui.md_techplacement_check.setEnabled(setstate)
        self.ui.md_techimplement_check.setEnabled(setstate)
        self.ui.md_perfassess_check.setEnabled(setstate)
        self.ui.rerun_perfassess.setEnabled(setstate)

        self.ui.out_textrep_select.setEnabled(setstate)        
        self.ui.out_gis_maps.setEnabled(setstate)
        self.ui.out_gis_customize.setEnabled(setstate)
        self.ui.out_resultsbrowse.setEnabled(setstate)
        self.ui.out_projectfolder.setEnabled(setstate)
        
        self.ui.actionAddData.setEnabled(setstate)
        self.ui.actionElevation_Data.setEnabled(setstate)
        self.ui.actionSoil_Data.setEnabled(setstate)
        self.ui.actionLand_Use.setEnabled(setstate)
        self.ui.actionPopulation.setEnabled(setstate)
        self.ui.actionPlanning.setEnabled(setstate)
        self.ui.actionLocality_Map.setEnabled(setstate)
        self.ui.actionSocial_Data.setEnabled(setstate)
        self.ui.actionRainfall.setEnabled(setstate)
        self.ui.actionEvapotranspiration.setEnabled(setstate)
        self.ui.actionSolar_Radiation.setEnabled(setstate)
        self.ui.addDataButton.setEnabled(setstate)
        self.ui.removeDataButton.setEnabled(setstate)
        self.ui.collex_button.setEnabled(setstate)
        self.ui.resetSimButton.setEnabled(setstate)
        self.ui.runButton.setEnabled(setstate)     
        self.ui.actionSet_Spatial_Delineation.setEnabled(setstate)
        self.ui.actionDefine_Urban_Planning_Rules.setEnabled(setstate)
        self.ui.actionCustomize_Technologies.setEnabled(setstate)
        self.ui.actionTechnology_Implementation.setEnabled(setstate)
        self.ui.actionPlanning_Cycle.setEnabled(setstate)
        self.ui.actionImplementation_Cycle.setEnabled(setstate)

    def disable_select_guis(self, state):
        if state == "all":
            self.ui.md_techplacement_check.setChecked(1)
            self.ui.md_techimplement_check.setChecked(1)
            self.ui.md_perfassess_check.setChecked(1)
            self.getActiveSimulationObject().changeModuleStatus("techplacement", 1)
            self.getActiveSimulationObject().changeModuleStatus("techimplement", 1)
            self.getActiveSimulationObject().changeModuleStatus("perfassess", 1)
        elif state == "basic":
            self.ui.pc_techplacement.setEnabled(0)
            self.ui.pc_techplacement_help.setEnabled(0)
            self.ui.md_techplacement_check.setEnabled(0)
            self.ui.md_techplacement_check.setChecked(0)
            self.ui.ic_dataset.setEnabled(0)
            self.ui.ic_techimplement.setEnabled(0)
            self.ui.ic_techimplement_help.setEnabled(0)
            self.ui.md_techimplement_check.setEnabled(0)
            self.ui.md_techimplement_check.setChecked(0)
            self.ui.pa_dataset.setEnabled(0)
            self.ui.pa_assess.setEnabled(0)
            self.ui.pa_assess_help.setEnabled(0)
            self.ui.md_perfassess_check.setEnabled(0)
            self.ui.md_perfassess_check.setChecked(0)
            self.ui.rerun_perfassess.setEnabled(0)
            self.ui.actionCustomize_Technologies.setEnabled(0)
            self.ui.actionTechnology_Implementation.setEnabled(0)
            self.ui.actionPlanning_Cycle.setEnabled(0)
            self.ui.actionImplementation_Cycle.setEnabled(0)
            self.getActiveSimulationObject().changeModuleStatus("techplacement", 0)
            self.getActiveSimulationObject().changeModuleStatus("techimplement", 0)
            self.getActiveSimulationObject().changeModuleStatus("perfassess", 0)
        elif state == "techplan":
            self.ui.ic_dataset.setEnabled(0)
            self.ui.md_techplacement_check.setChecked(1)
            self.ui.ic_techimplement.setEnabled(0)
            self.ui.ic_techimplement_help.setEnabled(0)
            self.ui.md_techimplement_check.setEnabled(0)
            self.ui.md_techimplement_check.setChecked(0)
            self.ui.pa_dataset.setEnabled(0)
            self.ui.pa_assess.setEnabled(0)
            self.ui.pa_assess_help.setEnabled(0)
            self.ui.rerun_perfassess.setEnabled(0)
            self.ui.md_perfassess_check.setEnabled(0)
            self.ui.md_perfassess_check.setChecked(0)
            self.ui.actionTechnology_Implementation.setEnabled(0)
            self.ui.actionPlanning_Cycle.setEnabled(0)
            self.ui.actionImplementation_Cycle.setEnabled(0)
            self.getActiveSimulationObject().changeModuleStatus("techplacement", 1)
            self.getActiveSimulationObject().changeModuleStatus("techimplement", 0)
            self.getActiveSimulationObject().changeModuleStatus("perfassess", 0)
        elif state == "techimpl":
            self.ui.md_techplacement_check.setChecked(1)
            self.ui.md_techimplement_check.setChecked(1)
            self.ui.pa_dataset.setEnabled(0)
            self.ui.pa_assess.setEnabled(0)
            self.ui.pa_assess_help.setEnabled(0)
            self.ui.md_perfassess_check.setEnabled(0)
            self.ui.md_perfassess_check.setChecked(0)
            self.ui.rerun_perfassess.setEnabled(0)
            self.ui.actionPlanning_Cycle.setEnabled(0)
            self.ui.actionImplementation_Cycle.setEnabled(0)
            self.getActiveSimulationObject().changeModuleStatus("techplacement", 1)
            self.getActiveSimulationObject().changeModuleStatus("techimplement", 1)
            self.getActiveSimulationObject().changeModuleStatus("perfassess", 0)
        elif state == "perfonly":
            self.ui.md_techplacement_check.setChecked(1)
            self.ui.md_perfassess_check.setChecked(1)
            self.ui.ic_dataset.setEnabled(0)
            self.ui.ic_techimplement.setEnabled(0)
            self.ui.ic_techimplement_help.setEnabled(0)
            self.ui.md_techimplement_check.setEnabled(0)
            self.ui.md_techimplement_check.setChecked(0)
            self.ui.pa_dataset.setEnabled(0)
            self.ui.actionTechnology_Implementation.setEnabled(0)
            self.ui.actionImplementation_Cycle.setEnabled(0)
            self.getActiveSimulationObject().changeModuleStatus("techplacement", 1)
            self.getActiveSimulationObject().changeModuleStatus("techimplement", 0)
            self.getActiveSimulationObject().changeModuleStatus("perfassess", 1)

    def enabledisable_sim_modules(self):
        """Response to clicking a module's checkbox, this function enables or disables access to the parameter screen of
        a particular module. This allows more light-weight simulations to be done.
        """
        if self.ui.md_techplacement_check.isChecked() == 0:
            #Case 1 - Techplacement disabled -- > everything else disabled, return
            self.ui.pc_techplacement.setEnabled(0)
            self.ui.md_techimplement_check.setEnabled(0)
            self.ui.ic_techimplement.setEnabled(0)
            self.ui.ic_dataset.setEnabled(0)
            self.ui.md_perfassess_check.setEnabled(0)
            self.ui.pa_assess.setEnabled(0)
            self.ui.pa_dataset.setEnabled(0)
            self.ui.rerun_perfassess.setEnabled(0)
            self.getActiveSimulationObject().changeModuleStatus("techplacement", 0)
            self.getActiveSimulationObject().changeModuleStatus("techimplement", 0)
            self.getActiveSimulationObject().changeModuleStatus("perfassess", 0)
            return True
        else:
            #Case 2 - Techplacement enabled --> check others
            self.ui.pc_techplacement.setEnabled(1)
            self.getActiveSimulationObject().changeModuleStatus("techplacement", 1)

        #Check existence of Techimplement, then whether box is checked
        print "checking implement"
        if self.getActiveSimulationObject().getLengthOfModulesVector("techimplement") != 0:
            self.ui.md_techimplement_check.setEnabled(1)
            if self.ui.md_techimplement_check.isChecked() == 0:
                self.ui.ic_techimplement.setEnabled(0)
                self.getActiveSimulationObject().changeModuleStatus("techimplement", 0)
            else:
                self.ui.ic_techimplement.setEnabled(1)
                self.ui.ic_dataset.setEnabled(1)
                self.getActiveSimulationObject().changeModuleStatus("techimplement", 1)
        else:
            self.ui.md_techimplement_check.setEnabled(0)
            self.ui.ic_techimplement.setEnabled(0)
            self.ui.ic_dataset.setEnabled(0)
            self.getActiveSimulationObject().changeModuleStatus("techimplement", 0)

        #Check existence of PerfAssess, then whether box is checked
        print "checking perfassess"
        if self.getActiveSimulationObject().getLengthOfModulesVector("perf_assess") != 0:
            self.ui.md_perfassess_check.setEnabled(1)
            if self.ui.md_perfassess_check.isChecked() == 0:
                self.ui.pa_assess.setEnabled(0)
                self.ui.rerun_perfassess.setEnabled(0)
                self.getActiveSimulationObject().changeModuleStatus("perfassess", 0)
            else:
                self.ui.pa_assess.setEnabled(1)
                self.ui.rerun_perfassess.setEnabled(1)
                self.ui.pa_dataset.setEnabled(1)
                self.getActiveSimulationObject().changeModuleStatus("perfassess", 1)
        else:
            self.ui.pa_assess.setEnabled(0)
            self.ui.md_perfassess_check.setEnabled(0)
            self.ui.rerun_perfassess.setEnabled(0)
            self.ui.pa_dataset.setEnabled(0)
            self.getActiveSimulationObject().changeModuleStatus("perfassess", 0)

    def resetConfigInterface(self):
        n = self.ui.simconfig_tabs.count()
        self.ui.summaryBox0.setHtml("")
        for i in range(n):
            if i == 0:
                continue
            sumbox = self.ui.simconfig_tabs.findChild(QtWebKit.QWebView, "summaryBox"+str(i))
            if sumbox != None:
                sumbox.setParent(None)
                sumbox.deleteLater()
            self.ui.simconfig_tabs.removeTab(1)
        return True
        
    def setupNewProject(self):
        """Resets several GUIs, and the active simulation object,
        Creates the instance of the active simulation object and sets it as active."""
        self.setActiveSimulationObject(None)        
        self.enabledisable_sim_guis(1)
        self.resetDatabank(1)
        self.resetConfigInterface()        
        newsimulation = self.createNewProjectInstance()
        self.setActiveSimulationObject(newsimulation)
        return True        

    def processSetupParameters(self):
        activeSim = self.getActiveSimulationObject()        
        self.printc("Initiated New Project: ")
        activeSim.setActiveProjectPath(self.getActiveProjectPath())
        self.printc(str(activeSim.getActiveProjectPath()))
        return True
    
    def addSimulationDetailTabs(self):
        activesimulation = self.getActiveSimulationObject()        
        self.printc(activesimulation.getParameter("simtype"))        
        tabnames = []        
        if activesimulation.getParameter("simtype") == "S":
            snapshots = activesimulation.getParameter("static_snapshots")
            for i in range(snapshots-1):
                tabnames.append("Snap"+str(int(i+1)))
        elif activesimulation.getParameter("simtype") == "D":
            if activesimulation.getParameter("dyn_irregulardt") == 0:
                breaks = activesimulation.getParameter("dyn_breaks")
                for i in range(breaks-1):
                    tabnames.append("Milestone"+str(int(i+1)))
                tabnames.append("End Year"+str(activesimulation.getParameter("dyn_totyears") + activesimulation.getParameter("dyn_startyear")))
            else:
                yearlabels = ubscripts.convertYearList(activesimulation.getParameter("dyn_irregularyears"), "MOD")
                for i in range(len(yearlabels)-1):
                    if i == 0:
                        continue
                    tabnames.append("Milestone "+str(i))
                tabnames.append("End Year"+str(yearlabels[len(yearlabels)-1]))
        else:
            pass    #no benchmark for now
            
        for i in range(len(tabnames)):
            self.simtab = QtGui.QWidget()
            self.simtab.setObjectName(_fromUtf8(str(tabnames[i])+"_data"))
            self.verticalLayout = QtGui.QVBoxLayout(self.simtab)
            self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"+str(tabnames[i])))            
            self.simtab_summarybox = QtWebKit.QWebView(self.simtab)
            self.simtab_summarybox.setObjectName("summaryBox"+str(i+1))
            self.verticalLayout.addWidget(self.simtab_summarybox)
            self.ui.simconfig_tabs.addTab(self.simtab, _fromUtf8(str(tabnames[i])))
            self.revise_check = QtGui.QCheckBox(self.simtab)
            #some condition to determine whether to enable or disable the checkbox            
            self.revise_check.setEnabled(True)
            self.revise_check.setText("Do not Revise Water Management Plan for this instance")
            self.revise_check.setObjectName(_fromUtf8("revise_check_"+str(tabnames[i])))
            self.verticalLayout.addWidget(self.revise_check)
        self.updateSummaryBox(self.ui.simconfig_tabs.currentIndex())
        return True

    ################################
    ## Functions for Signal/Slots ##
    ################################
    #File Menu                
    def beginNewProjectDialog(self):
        self.ui.simconfig_tabs.setCurrentIndex(0)
        self.ui.databrowseTree.clear()
        self.enabledisable_sim_guis(0)
        self.resetConfigInterface()
        self.setupNewProject()          

        newprojectdialog = ubdialogs.NewProjectSetup(self.getActiveSimulationObject(), 'create')
        self.connect(newprojectdialog, QtCore.SIGNAL("rejected()"), lambda setstate=0: self.enabledisable_sim_guis(setstate) )
        self.connect(newprojectdialog, QtCore.SIGNAL("newProjectSetupComplete"), self.initializeNewProjectCore)
        self.connect(newprojectdialog, QtCore.SIGNAL("newProjectSetupComplete"), self.initializeNewProject)
        self.connect(newprojectdialog, QtCore.SIGNAL("newProjectDirectory"), self.setNewProjectDirectory)
        newprojectdialog.exec_()
        return True

    def initializeNewProjectCore(self):
        activesim = self.getActiveSimulationObject()
        activesim.initializeSimulationCore()
        return True

    def initializeNewProject(self):
        """Called once activesim has been completely informed with all project info parameters.
        This is done using initializeNewProjectCore() for new projects and in ubfiles.LoadProject for existing."""
        activesim = self.getActiveSimulationObject()
        self.updateNewProject()
        if activesim.getParameter("simtype") == "S":
            if activesim.getParameter("sf_perfinclude") == 1 and activesim.getParameter("sf_techimplinclude") == 1:
                self.disable_select_guis("all")
            elif activesim.getParameter("sf_perfinclude") == 1 and activesim.getParameter("sf_techimplinclude") == 0:
                self.disable_select_guis("perfonly")
            elif activesim.getParameter("sf_techimplinclude") == 1:
                self.disable_select_guis("techimpl")
            elif activesim.getParameter("sf_techplaninclude") == 1:
                self.disable_select_guis("techplan")
            else:
                self.disable_select_guis("basic")
        elif activesim.getParameter("simtype") == "D":
            if activesim.getParameter("df_perfinclude") == 1:
                self.disable_select_guis("all")
            elif activesim.getParameter("df_perfinclude") == 0:
                self.disable_select_guis("techimpl")

    def updateSimulationRevisionPlan(self):
        """Signals to the module that in that particular tab, no revision is to be made to the masterplan regardless of
        what the user sets.
        """
        curtab = self.ui.simconfig_tabs.currentIndex()
        activesim = self.getActiveSimulationObject()
        try:
            #Try to obtain the technology placement module for that tab
            tp_module = activesim.getModuleTechplacement(curtab)
            if self.ui.revise_check.isChecked():    #If checked, do not revise
                tp_module.setParameter("Revise", 0)
            else:
                tp_module.setParameter("Revise", 1)
        except IndexError:
            pass

    def updateNewProject(self):
        self.processSetupParameters()
        self.addSimulationDetailTabs()
        return True
    
    def setNewProjectDirectory(self, pathname):
        self.printc("New Project Directory: "+str(pathname))
        self.setActiveProjectPath(pathname)
        try:
            os.chdir(str(pathname))
        except WindowsError:
            pass
        return True        
        
    def openExistingProject(self):
        self.ui.simconfig_tabs.setCurrentIndex(0)
        self.ui.databrowseTree.clear()
        self.enabledisable_sim_guis(0)
        self.resetConfigInterface()
        self.setupNewProject()                          

        fname = QtGui.QFileDialog.getOpenFileName(self, "Load Existing UrbanBEATS Project...", os.curdir, "UrbanBEATS (*.ubs)")
        if fname:
            activesim = self.getActiveSimulationObject()
            projectpath = ubfiles.getSimFileProjectPath(fname)

            #Check for the correct project path and prompt if doesn't exist
            if os.path.exists(projectpath):
                pass #All ok
            else:
                prompt_msg = "The directory "+str(projectpath)+" does not exist! Set a new directory?"
                reply = QtGui.QMessageBox.question(self, 'Project Path Location',
                                 prompt_msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.Cancel)
                if reply == QtGui.QMessageBox.Yes:
                    #Commands to select new directory
                    projectpath = QtGui.QFileDialog.getExistingDirectory(self, "Select Project Location")
                    if projectpath:
                        pass #All ok
                    else:
                        prompt_msg = "Invalid Path, Project not loaded!"
                        QtGui.QMessageBox.information(self, 'Load Project', prompt_msg, QtGui.QMessageBox.Ok)
                        self.ui.simconfig_tabs.setCurrentIndex(0)
                        self.ui.databrowseTree.clear()
                        self.enabledisable_sim_guis(0)
                        self.resetConfigInterface()
                        return False
                elif reply == QtGui.QMessageBox.Cancel:
                    prompt_msg = "Project not loaded!"
                    QtGui.QMessageBox.information(self, 'Load Project', prompt_msg, QtGui.QMessageBox.Ok)
                    #Commands to quit load operation
                    self.ui.simconfig_tabs.setCurrentIndex(0)
                    self.ui.databrowseTree.clear()
                    self.enabledisable_sim_guis(0)
                    self.resetConfigInterface()
                    return False

            mapmiss = ubfiles.loadSimFile(activesim, fname, projectpath)
            self.setActiveProjectPath(activesim.getActiveProjectPath())
            self.setupTreeWidgetFromDict()
            self.initializeNewProject()
            self.printc("Simulation Core Initialised")
            if mapmiss:
                self.raiseUBErrorMessage("Some input maps could not be loaded. Please locate these before starting the simulation!")
        else:
            self.enabledisable_sim_guis(0)

        #Call a function to update entire gui on everything
        return True

    def saveProject(self):
        activesim = self.getActiveSimulationObject()
        fname = str(activesim.getFullFileName())
        if fname == "":
            fname = QtGui.QFileDialog.getSaveFileName(self, "Save Current UrbanBEATS Project...", os.curdir, "UrbanBEATS (*.ubs)")
            if fname:
                ubfiles.saveSimFile(activesim, fname)
                activesim.setFullFileName(fname)
        else:
            ubfiles.saveSimFile(activesim, fname)    
        return True

    def saveProjectAs(self):
        activesim = self.getActiveSimulationObject()        
        fname = QtGui.QFileDialog.getSaveFileName(self, "Save Current UrbanBEATS Project As...", os.curdir, "UrbanBEATS (*.ubs)")
        if fname:
            ubfiles.saveSimFile(activesim, fname)
            activesim.setFullFileName(fname)
        
    #Edit Menu
    #cut, copy, paste
    def editProjectInfo(self):
        projectdialog = ubdialogs.NewProjectSetup(self.getActiveSimulationObject(), 'update')
        projectdialog.exec_()
        return True
    
    def editPreferences(self):
        preferencesdialog = ubdialogs.PreferencesDialogLaunch(self)
        self.connect(preferencesdialog, QtCore.SIGNAL("update_cfg"), self.updateConfigFromOptions)
        self.connect(preferencesdialog, QtCore.SIGNAL("resetOptions"), self.resetConfigFile)
        preferencesdialog.exec_()
        return True
    
    #View Menu
    def viewProjectInfo(self):
        projectdialog = ubdialogs.NewProjectSetup(self.getActiveSimulationObject(), 'view')
        projectdialog.exec_()
        return True        
    
    #Data Menu
    def showAddDataDialog(self):
        adddatadialog = ubdialogs.AddDataLaunch()
        self.connect(adddatadialog, QtCore.SIGNAL("added_data"), self.updateTreeWidget)
        self.connect(adddatadialog, QtCore.SIGNAL("added_data"), self.updateDataArchive)
        adddatadialog.exec_()
        return True

    def exportDataArchive(self):
        activesim = self.getActiveSimulationObject()
        fname = str(QtGui.QFileDialog.getSaveFileName(self, "Export Data Archive As...", os.curdir, "Data Archive (*.uda)"))
        if fname:
            ubfiles.exportDataArchiveFile(activesim, fname)
        return True

    def importDataArchive(self, filetype):
        activesim = self.getActiveSimulationObject()
        if filetype == "ubs":
            fileconstrain = "UrbanBEATS (*.ubs)"
        elif filetype == "uda":
            fileconstrain = "Data Archive (*.uda)"
        else:
            fileconstrain = ""
        fname = str(QtGui.QFileDialog.getOpenFileName(self, "Import Data Archive...", os.curdir, fileconstrain))
        if fname:
            mapmiss = ubfiles.importDataArchiveFile(activesim, fname, filetype)
            self.ui.databrowseTree.clear()
            self.resetDatabank(0)
            self.setupTreeWidgetFromDict()
            if mapmiss:
                self.raiseUBErrorMessage("Some input maps could not be loaded!")
        return True

    def directAddData(self, dtype):
        fname = QtGui.QFileDialog.getOpenFileName(self, "Locate "+str(dtype)+" Data File...", os.curdir, "")
        if fname:        
            newdata = QtGui.QTreeWidgetItem()
            newdata.setText(0, os.path.basename(fname))
            #determine index
            final_index = self.__dtype_names.index(dtype)
            if final_index in [7, 8, 9]:
                final_index = 7
            checkchild = self.ui.databrowseTree.topLevelItem(final_index).child(0)
            if self.ui.databrowseTree.topLevelItem(final_index).childCount() != 0 and checkchild.text(0) == "<none>":
                self.ui.databrowseTree.topLevelItem(final_index).removeChild(checkchild)
            self.ui.databrowseTree.topLevelItem(final_index).addChild(newdata)
            self.updateDataArchive(fname, final_index, True)
        return True
    
    def updateTreeWidget(self, fname, typeindex, datastate):
        newdata = QtGui.QTreeWidgetItem()
        newdata.setText(0, os.path.basename(str(fname)))
        typeindex -= 1  #decrement by 1 because of the <undefined> row in the add data dialog        
        if typeindex == -1:
            self.printc("ERROR: PLEASE DEFINE DATA TYPE!")
            return True
        #determine index
        if typeindex in [0, 1, 2]:
            treeindex = typeindex
        elif typeindex in [3, 4]:       #if a demographic input
            treeindex = 3
        elif typeindex in [5, 6, 7]:
            treeindex = typeindex - 1
        elif typeindex in [8, 9]:       #if a natural water body?
            treeindex = 7
        elif typeindex in [10, 11]:
            treeindex = typeindex - 2
        elif typeindex in [12, 13, 14]: #if climate data?
            treeindex = 10
        checkchild = self.ui.databrowseTree.topLevelItem(treeindex).child(0)
        if self.ui.databrowseTree.topLevelItem(treeindex).childCount() != 0 and checkchild.text(0) == "<none>":
            self.ui.databrowseTree.topLevelItem(treeindex).removeChild(checkchild)
        self.ui.databrowseTree.topLevelItem(treeindex).addChild(newdata)
        return True

    def setupTreeWidgetFromDict(self):
        dataarchive = self.getActiveSimulationObject().showDataArchive()
        for key in dataarchive:
            dtype_index = self.__dtype_names.index(key)
            for i in dataarchive[key]:
                self.updateTreeWidget(i, dtype_index+1, True)
    
    def collexTreeWidget(self):
        """Expands/Collapses the entire Active Project Data Collection Browser's Hierarchy
                - if all the widgets are expanded, it will collapse the entire hierarchy
                - if at least one of the parents are expanded, it will expand the entire hierarchy
        """
        tlitems = self.ui.databrowseTree.topLevelItemCount()
        collapse = False
        for i in range(tlitems):
            if self.ui.databrowseTree.topLevelItem(i).isExpanded() == False and collapse == False:
                collapse = True
        if collapse:    #expand all if Collapse == True because even one single category was collapsed
            for i in range(tlitems):
                self.ui.databrowseTree.topLevelItem(i).setExpanded(True)
            #Change the name of the button
            self.ui.collex_button.setText("Collapse All")
        else:
            for i in range(tlitems):
                self.ui.databrowseTree.topLevelItem(i).setExpanded(False)
            self.ui.collex_button.setText("Expand All")
        return True
            
    def updateDataArchive(self, fname, typeindex, useraction):
        activeSim = self.getActiveSimulationObject()
        if useraction == True:
            typeindex -= 1  #decrement by 1 because of the <undefined> row in the add data dialog 
            if typeindex == -1:
                return True
            dataname = self.__dtype_names[typeindex]
            activeSim.addDataToArchive(dataname, str(fname))
        elif useraction == False:
            dataname = self.__dtype_names[typeindex]
            activeSim.removeDataFromArchive(dataname, fname)            
        self.printc(activeSim.showDataArchive())
        return True        
        
    def removeDataEntry(self):
        try:        
            cur_item = self.ui.databrowseTree.currentItem()        
            cur_parent = cur_item.parent()
            if cur_parent != 0:
                cur_parent.removeChild(cur_item)
                if cur_item.text(0) != "<none>":
                    if cur_parent.text(0) == "Climate":
                        dtype_name = "Rainfall"             #this only gives you the first of three possible climate data groups
                    elif cur_parent.text(0) == "Natural Water Bodies":
                        dtype_name = "Rivers"
                    elif cur_parent.text(0) == "Demographic":
                        dtype_name = "Population"
                    else:
                        dtype_name = str(cur_parent.text(0))
                    self.updateDataArchive(cur_item.text(0), self.__dtype_names.index(dtype_name), False)
            if cur_parent.childCount() == 0:
                none_child = QtGui.QTreeWidgetItem()
                none_child.setText(0, "<none>")
                cur_parent.addChild(none_child)
        except AttributeError as e:
            self.printc(str(e))
            self.printc("Cannot remove this!")
        return True
        
    def resetDatabank(self, activesimclear):
        self.ui.databrowseTree.clear()        
        elevation = QtGui.QTreeWidgetItem()
        elevation.setText(0, "Elevation")       
        soil = QtGui.QTreeWidgetItem()
        soil.setText(0, "Soil")
        landuse = QtGui.QTreeWidgetItem()
        landuse.setText(0, "Land Use")
        demographic = QtGui.QTreeWidgetItem()
        demographic.setText(0, "Demographic")
        plannermap = QtGui.QTreeWidgetItem()
        plannermap.setText(0, "Planning")
        locality = QtGui.QTreeWidgetItem()
        locality.setText(0, "Locality")
        groundwater = QtGui.QTreeWidgetItem()
        groundwater.setText(0, "Groundwater")
        naturalwater = QtGui.QTreeWidgetItem()
        naturalwater.setText(0, "Natural Water Bodies")
        social = QtGui.QTreeWidgetItem()
        social.setText(0, "Social Parameters")        
        wsud = QtGui.QTreeWidgetItem()
        wsud.setText(0, "Existing WSUD")
        network = QtGui.QTreeWidgetItem()
        network.setText(0, "Existing Network Infrastructure")
        climate = QtGui.QTreeWidgetItem()
        climate.setText(0, "Climate")                
        toplevitems = [elevation, soil, landuse, demographic, plannermap, locality, groundwater, naturalwater, social, wsud, network, climate]
        none_elev = QtGui.QTreeWidgetItem()
        none_elev.setText(0, "<none>")
        none_soil = QtGui.QTreeWidgetItem()
        none_soil.setText(0, "<none>")
        none_land = QtGui.QTreeWidgetItem()
        none_land.setText(0, "<none>")
        none_dem = QtGui.QTreeWidgetItem()
        none_dem.setText(0, "<none>")
        none_plan = QtGui.QTreeWidgetItem()
        none_plan.setText(0, "<none>")
        none_loc = QtGui.QTreeWidgetItem()
        none_loc.setText(0, "<none>")
        none_gw = QtGui.QTreeWidgetItem()
        none_gw.setText(0, "<none>")
        none_natural = QtGui.QTreeWidgetItem()
        none_natural.setText(0, "<none>")
        none_soc = QtGui.QTreeWidgetItem()
        none_soc.setText(0, "<none>")
        none_wsud = QtGui.QTreeWidgetItem()
        none_wsud.setText(0, "<none>")
        none_clim = QtGui.QTreeWidgetItem()
        none_clim.setText(0, "<none>")
        none_list = [none_elev, none_soil, none_land, none_dem, none_plan, none_loc, none_gw, none_natural, none_soc, none_wsud, none_clim]
        self.ui.databrowseTree.addTopLevelItems(toplevitems)     
        for i in range(len(none_list)):
            self.ui.databrowseTree.topLevelItem(i).addChild(none_list[i])
        if activesimclear:
            activeSim = self.getActiveSimulationObject()
            if activeSim:
                activeSim.resetDataArchive()
        return True
    
    def crosscheckGIS(self):
        #to do
        pass
    
    def viewSimData(self):
        #will show the files from the databank that were selected for the current simulation
        #calls a GUI
        pass
    
    def updateSummaryBox(self, index):
        active_simulation = self.getActiveSimulationObject()        
        currentTabName = self.ui.simconfig_tabs.tabText(index) #self.ui.simconfig_tabs.currentIndex())
        sumhtml = """
        <!DOCTYPE HTML>
        <html>
            <body>
            <h4>Summary of Inputs for Case: """+str(currentTabName)+"""</h4>
            <hr />
            <div id="mainsummary", style="font-family:Arial; font-size:10pt">
            """+ubsum.getSummaryStringNarrative(active_simulation, index)+"""
            """+ubsum.getSummaryStringDelinBlocks(active_simulation)+"""

            """+ubsum.getSummaryStringUrbplanbb(active_simulation, index)+"""
            </div>
            </body>
        </html>
        """
        sum_box = self.ui.simconfig_tabs.findChild(QtWebKit.QWebView, "summaryBox"+str(index))
        sum_box.setHtml(sumhtml)
        return True
    
    #Simulation Menu
    def callNarrativeGui(self):
        tabindex = self.ui.simconfig_tabs.currentIndex()
        narrativeguic = ubdialogs.NarrativesGuiLaunch(self.getActiveSimulationObject(), tabindex)
        self.connect(narrativeguic, QtCore.SIGNAL("updatedDetails"), lambda tabindex=tabindex: self.updateSummaryBox(tabindex))
        narrativeguic.exec_()

    def callCalibrationGui(self):
        tabindex = self.ui.simconfig_tabs.currentIndex()
        calibrationguic = urbanbeatscalibration.CalibrationGUILaunch(self.getActiveSimulationObject(), tabindex)
        calibrationguic.exec_()

    def callDelinblocksGui(self):
        tabindex = self.ui.simconfig_tabs.currentIndex()
        delinblocksguic = md_delinblocksguic.DelinBlocksGUILaunch(self.getActiveSimulationObject())
        self.connect(delinblocksguic, QtCore.SIGNAL("updatedDetails"), lambda tabindex=tabindex: self.updateSummaryBox(tabindex))
        delinblocksguic.exec_()
        
    def callUrbplanbbGui(self):
        if self.__activeSimulationObject.getLengthOfModulesVector("urbplanbb") == 1:
            tabindex = 0
        else:
            tabindex = self.ui.simconfig_tabs.currentIndex()
        urbplanbbguic = md_urbplanbbguic.UrbplanbbGUILaunch(self.getActiveSimulationObject(), tabindex)
        urbplanbbguic.exec_()
    
    def callTechplacementGui(self):
        if self.__activeSimulationObject.getLengthOfModulesVector("techplacement") == 1:
           tabindex = 0
        else:
           tabindex = self.ui.simconfig_tabs.currentIndex()
        techplacementguic = md_techplacementguic.TechplacementGUILaunch(self.getActiveSimulationObject(), tabindex)
        techplacementguic.exec_()

    def callTechimplementGui(self):
        if self.__activeSimulationObject.getLengthOfModulesVector("techimplement") == 1:
           tabindex = 0
        else:
           tabindex = self.ui.simconfig_tabs.currentIndex()
        techimplementguic = md_techimplementguic.TechimplementGUILaunch(self.getActiveSimulationObject(), tabindex)
        techimplementguic.exec_()

    def callPrepareperfGui(self):
        if self.__activeSimulationObject.getLengthOfModulesVector("perf_assess") == 1:
            tabindex = 0
        else:
            tabindex = self.ui.simconfig_tabs.currentIndex()
        perfassessguic = md_perfassessguic.PerfAssessGUILaunch(self.getActiveSimulationObject(), tabindex)
        perfassessguic.exec_()

    def customize_dataset(self, curstate):
        tabindex = self.ui.simconfig_tabs.currentIndex()       
        customdatadialog = ubdialogs.DataSelectGUILaunch(self.getActiveSimulationObject(), curstate, tabindex)
        customdatadialog.exec_()
        
        return True
    
    def verifySimulation(self):
        #to do
        pass
    
    #Advanced Menu
    def editOutputOptions(self):
        #to do
        pass
    
    #Window Menu
    #no functions as of yet
    
    #Help Menu
    def showAboutDialog(self):
        aboutdialog = ubdialogs.AboutDialogLaunch()
        aboutdialog.exec_()
    
    def showHelp(self):
        webbrowser.open("http://urbanbeatsmodel.com/w/index.php/Main_Page")
        return True
        #functions for social networks
    
    def likeOnFacebook(self):
        webbrowser.open("http://www.facebook.com/plugins/like.php?href=http%3A%2F%2Fwww.urbanbeatsmodel.com&send=false&layout=standard&width=450&show_faces=true&action=like&colorscheme=light&font&height=1000")
        return True
        
    #Output Reporting Functions
    def showReportingOptionsDialog(self):
        reportingoptionsdialog = ubdialogs.ReportOptionsDialogLaunch(self.getActiveSimulationObject())
        reportingoptionsdialog.exec_()

    def showGISOptionsDialog(self):
        gisoptionsdialog = ubdialogs.GISOptionsDialogLaunch(self.getActiveSimulationObject())
        gisoptionsdialog.exec_()    
    
    def showGISAdvancedDialog(self):
        gisoptionsdialog = ubdialogs.GISAdvancedDialogLaunch(self.getActiveSimulationObject())
        gisoptionsdialog.exec_()     
    
    def showResultsBrowseDialog(self):
        resultsbrowsedialog = ubresults.ResultsBrowseDialogLaunch(self.getActiveSimulationObject())
        resultsbrowsedialog.exec_()
    
    def openActiveProjectFolder(self):
        #doesn't work yet...        
        self.printc("Opening Project Directory: "+str(self.getActiveProjectPath()))
        path = str(self.getActiveProjectPath())
        subprocess.Popen(r'explorer "'+path+'"')
        pass

    def resetSimulationPartial(self):
        """Only reintializes the thread, but does not reset the assets"""
        active_simulation = self.getActiveSimulationObject()
        if active_simulation.getSimulationStatus() != 0:
            active_simulation.changeSimulationStatus("perfonly")
        active_simulation.reinitializeThread()
        active_simulation.updateSimulationCompletion(False)
        self.printc("----> Partial Reset Performed!")
        self.printc("")
        return True

    def resetSimulationAssets(self):
        """Sets the reference to all Block Assets in the Model to Null causing garbage
        collection of all existing simulation assets (Blocks, Networks, Points, etc.). This
        frees up memory for the next simulation.
        """
        active_simulation = self.getActiveSimulationObject()
        active_simulation.reinitializeThread()
        active_simulation.resetAssets()
        active_simulation.resetAssetCollection()
        active_simulation.updateSimulationCompletion(False)
        active_simulation.changeSimulationStatus("fullreset")
        self.printc("----> Complete Simulation Assets Reset Performed!")
        self.printc("")
        return True

    def updateProgressBar(self, value):
        """Updates the progress bar of the Main GUI when the simulation is started/stopped/reset"""
        self.ui.progressBar.setValue(value)
        return True

    def closeEvent(self, event):
        quit_msg = "Would you like to save your work before quitting?"
        reply = QtGui.QMessageBox.question(self, 'Close Program?',
                         quit_msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No, QtGui.QMessageBox.Cancel)
        if reply == QtGui.QMessageBox.Yes:
            self.saveProject()
            event.accept()
        elif reply == QtGui.QMessageBox.No:
            event.accept()
        else:
            event.ignore()

    def raiseUBErrorMessage(self, message):
        QtGui.QMessageBox.warning(self, 'Error', message, QtGui.QMessageBox.Ok)

    #RUN SIMULATION
    def checks_before_run(self):
        active_simulation = self.getActiveSimulationObject()
        tabs = active_simulation.getNumberOfTabs()
        minmaptypes = ["Elevation", "Soil", "Land Use", "Population"]
        all_clear = 1
        #Check all maps
            # (1) Have the maps all been allocated and (2) are they of the right type?
        for t in range(tabs):
            maps = active_simulation.getCycleDataSet("pc", t)
            print "Length of Map Set ", len(maps), maps
            if len(maps) < 4:
                self.raiseUBErrorMessage(str(self.ui.simconfig_tabs.tabText(t))+"'s Planning Cycle does not have enough maps allocated!")
                all_clear = 0
                return

            for cat in minmaptypes:
                if cat not in maps.keys():
                    self.raiseUBErrorMessage(str(self.ui.simconfig_tabs.tabText(t))+"'s Planning Cycle is missing information about "+str(cat)+"!")
                    all_clear = 0
                    return

        if active_simulation.getLengthOfModulesVector("techimplement") > 0:
            for t in range(tabs):
                maps = active_simulation.getCycleDataSet("ic", t)
                if len(maps) < 4:
                    self.raiseUBErrorMessage(str(self.ui.simconfig_tabs.tabText(t))+"'s Implementation Cycle does not have enough maps allocated!")
                    all_clear = 0
                    return

                for cat in minmaptypes:
                    if cat not in maps.keys():
                        self.raiseUBErrorMessage(str(self.ui.simconfig_tabs.tabText(t))+"'s Implementation Cycle is missing information about "+str(cat)+"!")
                        all_clear = 0
                        return

        #Check some input information
            # (1) Check the MCA Scoring Matrix Path
        if active_simulation.getLengthOfModulesVector("techplacement") > 0:
            for t in range(tabs):
                if os.path.isfile(active_simulation.getModuleTechplacement(t).getParameter("scoringmatrix_path")):
                    pass
                else:
                    self.raiseUBErrorMessage("The MCA Scoring Matrix File in "+str(self.ui.simconfig_tabs.tabText(t))+" does not exist. Please locate a valid file!")
                    all_clear = 0
                    return

        return self.run_simulation()

    def run_simulation(self):
        try:
            active_simulation = self.getActiveSimulationObject()
            self.updateProgressBar(0)
            active_simulation.start()
        except RuntimeError as e:
            self.printc(e)
            self.printc("Please reset simulation before starting a new run!")
        return True

    def run_simulation_perfonly(self):
        """Runs only the performance assessment instead of going through the whole assessment cycle. This saves users time
        with certain post-planning analyses.
        """
        active_simulation = self.getActiveSimulationObject()
        self.resetSimulationPartial()
        try:
            self.updateProgressBar(0)
            active_simulation.start()
        except RuntimeError as e:
            self.printc(e)
            self.printc("Something went wrong!")
        return True


class ConsoleObserver(QtCore.QObject):
    def updateObserver(self, textmessage):
        self.emit(QtCore.SIGNAL("updateConsole"), textmessage)

class StartScreenLaunch(QtGui.QDialog):
    def __init__(self, parent = None):
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_StartDialog()
        self.ui.setupUi(self)
        
        self.connect(self.ui.NewProjectButton, QtCore.SIGNAL("clicked()"), self.startupNewProjectWindow)
        self.connect(self.ui.OpenProjectButton, QtCore.SIGNAL("clicked()"), self.startupOpenProject)
        self.connect(self.ui.VisitWebsiteButton, QtCore.SIGNAL("clicked()"), self.launchUbeatsWebsite)
        self.connect(self.ui.QuitButton, QtCore.SIGNAL("clicked()"), self.startupQuit)

    def startupNewProjectWindow(self):
        self.accept()
        self.emit(QtCore.SIGNAL("startupNew"))
        
    def startupOpenProject(self):
        self.accept()
        self.emit(QtCore.SIGNAL("startupOpen"))
    
    def launchUbeatsWebsite(self):
        webbrowser.open("http://urbanbeatsmodel.com")
        
    def startupQuit(self):
        self.accept()
        sys.exit()


if __name__ == "__main__":

    UBEATSROOT = os.path.dirname(sys.argv[0])           #Obtains the program's root directory
    UBEATSROOT = UBEATSROOT.encode('string-escape')     #To avoid weird bugs e.g. if someone's folder path
                                                        #contains escape characters e.g. \testing or \newSoftware

    random.seed()
    #Someone is launching this directly
    #Create the QApplication
    app = QtGui.QApplication(sys.argv)

    splash_matrix = ["river", "city", "forest", "fountain"]
    #Splash Screen
    splash_pix = QtGui.QPixmap("splash"+splash_matrix[random.randint(0,3)]+"800.png")
    splash = QtGui.QSplashScreen(splash_pix, QtCore.Qt.WindowStaysOnTopHint)
    splash.setMask(splash_pix.mask())
    splash.show()
    app.processEvents()

    # Simulate something that takes time
    time.sleep(2)

    #Main Window
    main_window = MainWindow()
    main_window.showMaximized()
    splash.finish(main_window)
    #Enter the main loop

    start_screen = StartScreenLaunch()
    main_window.setOptionsFromConfig(UBEATSROOT)
    QtCore.QObject.connect(start_screen, QtCore.SIGNAL("startupOpen"), main_window.openExistingProject)
    QtCore.QObject.connect(start_screen, QtCore.SIGNAL("startupNew"), main_window.beginNewProjectDialog) 
    start_screen.exec_()    
    
    sys.exit(app.exec_())    
