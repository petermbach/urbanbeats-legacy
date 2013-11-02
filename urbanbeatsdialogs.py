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

import sys, os
from urbanbeatscore import *
from PyQt4 import QtGui, QtCore

from newprojectdialog import Ui_NewProjectDialog
from aboutdialog import Ui_AboutDialog
from adddatadialog import Ui_AddDataDialog
from preferencesdialog import Ui_PreferencesDialog
from gisexportoptionsdialog import Ui_GISExportDialog
from gisexportadvanceddialog import Ui_GISAdvancedDialog
from reportoptionsdialog import Ui_ReportOptionsDialog
from selectdatadialog import Ui_SelectData
from narrativegui import Ui_NarrativeDialog

class NewProjectSetup(QtGui.QDialog):
    def __init__(self, msim, readwrite, parent = None):
        self.module = UrbanBeatsSim        
        self.module = msim        
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_NewProjectDialog()
        self.ui.setupUi(self)

        #prepare GUI depending on read/write
        if readwrite == 'create':
            self.ui.projectpath_box.setEnabled(1)
            self.ui.projectpath_check.setEnabled(1)
            self.ui.projectpath_button.setEnabled(1)
            self.ui.simtype_combo.setEnabled(1)
            self.ui.snapshots_spin.setEnabled(1)
            self.ui.dynamicperiod_spin.setEnabled(1)
            self.ui.dynamicstart_spin.setEnabled(1)
            self.ui.dynamicbreaks_spin.setEnabled(1)
            self.ui.dynamicinterval_check.setEnabled(1)
        else:
            self.ui.projectpath_box.setEnabled(0)
            self.ui.projectpath_check.setEnabled(0)
            self.ui.projectpath_button.setEnabled(0)
            self.ui.simtype_combo.setEnabled(0)
            self.ui.snapshots_spin.setEnabled(0)
            self.ui.dynamicperiod_spin.setEnabled(0)
            self.ui.dynamicstart_spin.setEnabled(0)
            self.ui.dynamicbreaks_spin.setEnabled(0)
            self.ui.dynamicinterval_check.setEnabled(0)
            if readwrite == 'view':
                #pass (update in future)
                pass
        
        #Connect Core with GUI
        self.ui.name_box.setText(self.module.getParameter("name"))
        self.ui.city_box.setText(self.module.getParameter("region"))
        self.ui.state_box.setText(self.module.getParameter("state"))
        self.ui.country_box.setText(self.module.getParameter("country"))
        self.ui.modellername_box.setText(self.module.getParameter("modeller"))
        self.ui.affiliation_box.setText(self.module.getParameter("affiliation"))
        self.ui.othermodellers_box.setText(self.module.getParameter("otherpersons"))
        self.ui.synopsis_box.setPlainText(self.module.getParameter("synopsis"))
        
        self.ui.projectpath_box.setText(self.module.getParameter("projectpath"))
        
        if self.module.getParameter("projectpathsavedata") == 1:
            self.ui.projectpath_check.setChecked(1)
        else:
            self.ui.projectpath_check.setChecked(0)
        
        if self.module.getParameter("simtype") == "S":
            self.ui.simtype_combo.setCurrentIndex(0)
        elif self.module.getParameter("simtype") == "D":
            self.ui.simtype_combo.setCurrentIndex(1)
        elif self.module.getParameter("simtype") == "B":
            self.ui.simtype_combo.setCurrentIndex(2)
        
        self.ui.snapshots_spin.setValue(self.module.getParameter("static_snapshots"))

        staticsimfeatures = self.module.getParameter("staticsimfeatures")
        self.ui.static_ubpconstant.setChecked(bool(staticsimfeatures[0]))
        self.ui.static_techplaninclude.setChecked(bool(staticsimfeatures[1]))
        self.ui.static_techplanconstant.setChecked(bool(staticsimfeatures[2]))
        self.ui.static_techimplinclude.setChecked(bool(staticsimfeatures[3]))
        self.ui.static_techimplconstant.setChecked(bool(staticsimfeatures[4]))
        self.ui.static_perfinclude.setChecked(bool(staticsimfeatures[5]))
        
         #  "staticdataoptions" : [0,0]
        staticdataoptions = self.module.getParameter("staticdataoptions")
        if staticdataoptions[0] == 1:
            self.ui.radioMasterplan.setChecked(1)
        elif staticdataoptions[0] == 0:
            self.ui.radioEnvironment.setChecked(1)
        
        self.ui.static_climateconstant.setChecked(bool(staticdataoptions[1]))
        
        self.ui.dynamicperiod_spin.setValue(self.module.getParameter("dyn_totyears"))
        self.ui.dynamicstart_spin.setValue(self.module.getParameter("dyn_startyear"))
        self.ui.dynamicbreaks_spin.setValue(self.module.getParameter("dyn_breaks"))
        
        if self.module.getParameter("dyn_irregulardt") == 1:
            self.ui.dynamicinterval_check.setChecked(1)
        else:
            self.ui.dynamicinterval_check.setChecked(0)
            
        dynsimfeatures = self.module.getParameter("dynsimfeatures")
        self.ui.dyn_ubpconstant.setChecked(bool(dynsimfeatures[0]))
        self.ui.dyn_techplanconstant.setChecked(bool(dynsimfeatures[1]))
        self.ui.dyn_techimplconstant.setChecked(bool(dynsimfeatures[2]))
        self.ui.dyn_perfinclude.setChecked(bool(dynsimfeatures[3]))
        self.ui.dyn_perfconstant.setChecked(bool(dynsimfeatures[4]))        
        
         #       "dyndatafeatures" : [0,0]
        dyndatafeatures = self.module.getParameter("dyndatafeatures")
        self.ui.dyn_masterplanconstant.setChecked(bool(dyndatafeatures[0]))
        self.ui.dyn_climateconstant.setChecked(bool(dyndatafeatures[1]))
                        
        #Connect GUI Elements        
        self.connect(self.ui.projectpath_button, QtCore.SIGNAL("clicked()"), self.setProjectPath)
        self.connect(self.ui.buttonBox, QtCore.SIGNAL("accepted()"), self.save_values)
        
    def setProjectPath(self):
        pathname = QtGui.QFileDialog.getExistingDirectory(self, "Select Project Location")        
        if pathname:
            self.ui.projectpath_box.setText(pathname)
            self.emit(QtCore.SIGNAL("newProjectDirectory"), pathname)
        
    def save_values(self):
        #compile parameter list             
        self.module.setParameter("name", str(self.ui.name_box.text()))
        self.module.setParameter("date", 0)
        self.module.setParameter("region", str(self.ui.city_box.text()))
        self.module.setParameter("state", str(self.ui.state_box.text()))
        self.module.setParameter("country", str(self.ui.country_box.text()))
        self.module.setParameter("modeller", str(self.ui.modellername_box.text()))
        self.module.setParameter("affilitation", str(self.ui.affiliation_box.text()))
        self.module.setParameter("otherpersons", str(self.ui.othermodellers_box.text()))
        self.module.setParameter("synopsis", str(self.ui.synopsis_box.toPlainText()))
        
        self.module.setParameter("projectpath", str(self.ui.projectpath_box.text()))
        self.module.setParameter("projectpathsavedata", int(self.ui.projectpath_check.isChecked()))

        simtype_matrix = ["S", "D", "B"]
        simtype = simtype_matrix[self.ui.simtype_combo.currentIndex()]
        self.module.setParameter("simtype", simtype)
        
        self.module.setParameter("static_snapshots", self.ui.snapshots_spin.value())                        

        static_parameters = [int(self.ui.static_ubpconstant.isChecked()), int(self.ui.static_techplaninclude.isChecked()), \
                                int(self.ui.static_techplanconstant.isChecked()), int(self.ui.static_techimplinclude.isChecked()), \
                                int(self.ui.static_techimplconstant.isChecked()), int(self.ui.static_perfinclude.isChecked())]
        self.module.setParameter("staticsimfeatures", static_parameters)
                
        staticdataoptions = [int(self.ui.radioMasterplan.isChecked()), int(self.ui.static_climateconstant.isChecked())]
        self.module.setParameter("staticdataoptions", staticdataoptions)

        self.module.setParameter("dyn_totyears", self.ui.dynamicperiod_spin.value())
        self.module.setParameter("dyn_startyear", self.ui.dynamicstart_spin.value())
        self.module.setParameter("dyn_breaks", self.ui.dynamicbreaks_spin.value())
        self.module.setParameter("dyn_irregulardt", int(self.ui.dynamicinterval_check.isChecked()))
        
        dyn_simfeatures = [int(self.ui.dyn_ubpconstant.isChecked()), int(self.ui.dyn_techplanconstant.isChecked()), \
                            int(self.ui.dyn_techimplconstant.isChecked()), int(self.ui.dyn_perfinclude.isChecked()), \
                            int(self.ui.dyn_perfconstant.isChecked())]
        self.module.setParameter("dynsimfeatures", dyn_simfeatures)
        
        dyn_datafeatures = [int(self.ui.dyn_masterplanconstant.isChecked()), int(self.ui.dyn_climateconstant.isChecked())]
        self.module.setParameter("dyndatafeatures", dyn_datafeatures)
        
        self.emit(QtCore.SIGNAL("newProjectSetupComplete"))

class NarrativesGuiLaunch(QtGui.QDialog):
    def __init__(self, activesim, tabindex, parent = None):
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_NarrativeDialog()
        self.ui.setupUi(self)

        self.module = UrbanBeatsSim
        self.module = activesim

        self.tabindex = tabindex

        self.ui.heading_box.setText(self.module.getNarrative(self.tabindex)[0])
        self.ui.narrative_box.setPlainText(self.module.getNarrative(self.tabindex)[1])

        self.connect(self.ui.buttonBox, QtCore.SIGNAL("accepted()"), self.save_values)

    def save_values(self):
        narrative = []
        narrative.append(self.ui.heading_box.text())
        narrative.append(self.ui.narrative_box.toPlainText())
        self.module.setNarrative(self.tabindex, narrative)
        self.emit(QtCore.SIGNAL("updatedDetails"))

class AboutDialogLaunch(QtGui.QDialog):
    def __init__(self, parent = None):
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_AboutDialog()
        self.ui.setupUi(self)


class PreferencesDialogLaunch(QtGui.QDialog):
    def __init__(self, parent = None):
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_PreferencesDialog()
        self.ui.setupUi(self)


class AddDataLaunch(QtGui.QDialog):
    def __init__(self, parent = None):
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_AddDataDialog()
        self.ui.setupUi(self)   
        
        self.connect(self.ui.adddatabrowse, QtCore.SIGNAL("clicked()"), self.loaddata)
        self.connect(self.ui.buttonBox, QtCore.SIGNAL("accepted()"), self.save_values)
        
    def loaddata(self):
        fname = QtGui.QFileDialog.getOpenFileName(self, "Locate Simulation Data File...", os.curdir, "")
        if fname: 
            self.ui.databox.setText(fname)
    
    def save_values(self):
        type_index = self.ui.datatypecombo.currentIndex()
        if self.ui.databox.text() == "":
            pass
        else:
            self.emit(QtCore.SIGNAL("added_data"), self.ui.databox.text(), type_index, True)
   

class ReportOptionsDialogLaunch(QtGui.QDialog):
    def __init__(self, parent = None):
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_ReportOptionsDialog()
        self.ui.setupUi(self)
        

class GISOptionsDialogLaunch(QtGui.QDialog):
    def __init__(self, activesim, parent = None):
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_GISExportDialog()
        self.ui.setupUi(self)
        self.parameters = activesim.getGISExportDetails()
        self.module = activesim        
        
        self.ui.filename_box.setText(self.parameters["Filename"])
        self.ui.mapBlocks.setChecked(bool(self.parameters["BuildingBlocks"]))
        self.ui.mapPatches.setChecked(bool(self.parameters["PatchData"]))        
        self.ui.mapFlowpaths.setChecked(bool(self.parameters["Flowpaths"]))
        self.ui.mapWSUDplan.setChecked(bool(self.parameters["PlannedWSUD"]))
        self.ui.mapWSUDimplement.setChecked(bool(self.parameters["ImplementedWSUD"]))        
        self.ui.mapCentrepoints.setChecked(bool(self.parameters["CentrePoints"]))
        self.ui.mapLocalities.setChecked(bool(self.parameters["Localities"]))

        self.connect(self.ui.buttonBox, QtCore.SIGNAL("accepted()"), self.save_values)        
        
    def save_values(self):
        self.module.setGISExportDetails("Filename", self.ui.filename_box.text())
        self.module.setGISExportDetails("BuildingBlocks", int(self.ui.mapBlocks.isChecked()))
        self.module.setGISExportDetails("PatchData", int(self.ui.mapPatches.isChecked()))
        self.module.setGISExportDetails("Flowpaths", int(self.ui.mapFlowpaths.isChecked()))
        self.module.setGISExportDetails("CentrePoints", int(self.ui.mapCentrepoints.isChecked()))
        self.module.setGISExportDetails("PlannedWSUD", int(self.ui.mapWSUDplan.isChecked()))
        self.module.setGISExportDetails("ImplementedWSUD", int(self.ui.mapWSUDimplement.isChecked()))
        self.module.setGISExportDetails("Localities", int(self.ui.mapLocalities.isChecked()))
        return True        
        

class GISAdvancedDialogLaunch(QtGui.QDialog):
    def __init__(self, activesim, parent = None):
        self.projindex = ["+proj=utm +zone=54 +south +ellps=WGS84 +datum=WGS84 +units=m +no_defs +towgs84=0,0,0", \
                            "+proj=utm +zone=55 +south +ellps=WGS84 +datum=WGS84 +units=m +no_defs +towgs84=0,0,0", \
                            "+proj=utm +zone=56 +south +ellps=WGS84 +datum=WGS84 +units=m +no_defs +towgs84=0,0,0"]        
                            
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_GISAdvancedDialog()
        self.ui.setupUi(self)
        self.module = activesim
        self.parameters = activesim.getGISExportDetails()
        
        #PROJECTION COMBO BOX
        self.ui.projectionCombo.setCurrentIndex(self.projindex.index(self.parameters["Projection"]))        
        
        if self.parameters["ProjUser"] == 1:
            self.ui.projectionCheck.setChecked(1)
            self.ui.projectionCustombox.setEnabled(1)
        else:
            self.ui.projectionCheck.setChecked(0)
            self.ui.projectionCustombox.setEnabled(0)
                            
        self.ui.projectionCustombox.setText(str(self.parameters["Proj4"]))
        self.ui.kmlboolcheck.setChecked(bool(self.parameters["GoogleEarth"]))
        
        if self.parameters["Offset"] == "I":
            self.ui.offsetfrominput_radio.setChecked(1)
            self.ui.offsetx_box.setEnabled(0)
            self.ui.offsety_box.setEnabled(0)
        elif self.parameters["Offset"] == "C":
            self.ui.offsetcustom_radio.setChecked(1)
            self.ui.offsetx_box.setEnabled(1)
            self.ui.offsety_box.setEnabled(1)
            
        self.ui.offsetx_box.setText(str(self.parameters["OffsetCustX"]))
        self.ui.offsety_box.setText(str(self.parameters["OffsetCustY"]))
        
        self.connect(self.ui.projectionCheck, QtCore.SIGNAL("clicked()"), self.enabledisableCustomProj)
        self.connect(self.ui.offsetfrominput_radio, QtCore.SIGNAL("clicked()"), self.enabledisableOffsets)
        self.connect(self.ui.offsetcustom_radio, QtCore.SIGNAL("clicked()"), self.enabledisableOffsets)
        self.connect(self.ui.buttonBox, QtCore.SIGNAL("accepted()"), self.save_values)
        
    def enabledisableOffsets(self):
        if self.ui.offsetfrominput_radio.isChecked() == 1:
            self.ui.offsetx_box.setEnabled(0)
            self.ui.offsety_box.setEnabled(0)
        elif self.ui.offsetcustom_radio.isChecked() == 1:
            self.ui.offsetx_box.setEnabled(1)
            self.ui.offsety_box.setEnabled(1)
    
    def enabledisableCustomProj(self):
        if self.ui.projectionCheck.isChecked() == 1:
            self.ui.projectionCustombox.setEnabled(1)
            self.ui.projectionCombo.setEnabled(0)
        else:
            self.ui.projectionCustombox.setEnabled(0)
            self.ui.projectionCombo.setEnabled(1)
        
    def save_values(self):
        self.module.setGISExportDetails("Projection", str(self.projindex[self.ui.projectionCombo.currentIndex()]))
        self.module.setGISExportDetails("ProjUser", int(self.ui.projectionCheck.isChecked()))
        self.module.setGISExportDetails("Proj4", str(self.ui.projectionCustombox.text()))
        self.module.setGISExportDetails("GoogleEarth", int(self.ui.kmlboolcheck.isChecked()))
        
        if self.ui.offsetfrominput_radio.isChecked() == 1:
            self.module.setGISExportDetails("Offset", "I")
        elif self.ui.offsetcustom_radio.isChecked() == 1:
            self.module.setGISExportDetails("Offset", "C")
        
        self.module.setGISExportDetails("OffsetCustX", float(self.ui.offsetx_box.text()))
        self.module.setGISExportDetails("OffsetCustY", float(self.ui.offsety_box.text()))
        
        return True

class DataSelectGUILaunch(QtGui.QDialog):
    def __init__(self, activesim, curstate, tabindex, parent = None):
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_SelectData()
        self.ui.setupUi(self)
        self.module = activesim
        self.__dtype_names = ["Elevation", "Soil", "Land Use", "Population",  "Employment", "Planning", "Locality", "Groundwater", "Rivers", "Lakes", "Social Parameters", "Existing Systems", "Rainfall", "Evapotranspiration", "Solar Radiation"]        
        self.__curstate = curstate
        self.__tabindex = tabindex
        self.__activedataitems = {}        
        
        #Reset the interface
        self.ui.databrowse.clear()
        self.ui.activedatabrowser.clear()
        
        #Add the parent tabs into 'databrowse'
        if curstate in ["pc", "ic"]:        
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
            wsud.setText(0, "Existing Systems")
            customtoplevitems = [elevation, soil, landuse, demographic, plannermap, locality, groundwater, naturalwater, social, wsud]
        elif curstate in ["pa"]:
            climate = QtGui.QTreeWidgetItem()
            climate.setText(0, "Climate")                
            customtoplevitems = [climate]
        self.ui.databrowse.addTopLevelItems(customtoplevitems)     
        
        #Add the files from the core simulation object
        dataarchive = self.module.showDataArchive()
        
        for i in customtoplevitems:
            label = i.text(0)
            if label == "Demographic":  #exception 1
                altlabels = ["Population", "Employment"]
                for alts in altlabels:                
                    if len(dataarchive[alts]) != 0:
                        for j in range(len(dataarchive[alts])):
                            fname = dataarchive[alts][j]
                            fchild = QtGui.QTreeWidgetItem()
                            fchild.setText(0, fname)
                            fchild.setText(1, alts)
                            i.addChild(fchild)
                continue
                
            if label == "Natural Water Bodies": #exception 2
                altlabels = ["Rivers", "Lakes"]
                for alts in altlabels:                
                    if len(dataarchive[alts]) != 0:
                        for j in range(len(dataarchive[alts])):
                            fname = dataarchive[alts][j]
                            fchild = QtGui.QTreeWidgetItem()
                            fchild.setText(0, fname)
                            fchild.setText(1, alts)
                            i.addChild(fchild)
                continue
                            
            if label == "Climate":  #exception 3
                altlabels = ["Rainfall", "Evapotranspiration", "Solar Radiation"]
                for alts in altlabels:                
                    if len(dataarchive[alts]) != 0:
                        for j in range(len(dataarchive[alts])):
                            fname = dataarchive[alts][j]
                            fchild = QtGui.QTreeWidgetItem()
                            fchild.setText(0, fname)
                            fchild.setText(1, alts)
                            i.addChild(fchild)
                continue                            
                            
            if len(dataarchive[str(label)]) == 0:
                continue
            else:
                for j in range(len(dataarchive[str(label)])):
                    fname = dataarchive[str(label)][j]
                    fchild = QtGui.QTreeWidgetItem()
                    fchild.setText(0, fname)
                    fchild.setText(1, str(label))
                    i.addChild(fchild)
        
        for i in customtoplevitems:
            i.setExpanded(1)
        
        self.__activedataitems = self.module.getCycleDataSet(curstate, tabindex)
        for key in self.__activedataitems:
            activebrowseitem = QtGui.QTreeWidgetItem()
            activebrowseitem.setText(1, key)
            activebrowseitem.setText(0, self.__activedataitems[key])
            self.ui.activedatabrowser.addTopLevelItem(activebrowseitem)
        
        #Signal/Slots
        self.connect(self.ui.addData, QtCore.SIGNAL("clicked()"), self.addSelectedData)
        self.connect(self.ui.removeData, QtCore.SIGNAL("clicked()"), self.removeSelectedData)
        self.connect(self.ui.resetData, QtCore.SIGNAL("clicked()"), self.resetDataSet)
        self.connect(self.ui.buttonBox, QtCore.SIGNAL("accepted()"), self.save_values)
        
    def addSelectedData(self):        
        try:        
            cur_item = self.ui.databrowse.currentItem()
            cur_parent = cur_item.parent()
            if cur_parent != 0: #IF THE SELECTED ITEM HAS A PARENT, THEN IT IS A CHILD AND CAN BE ADDED
                cur_copy = QtGui.QTreeWidgetItem()
                cur_copy.setText(0, cur_item.text(0))
                cur_copy.setText(1, cur_item.text(1))
                self.ui.activedatabrowser.addTopLevelItem(cur_copy)
        except AttributeError:
            pass        
        return True
        
    def removeSelectedData(self):
        cur_item = self.ui.activedatabrowser.currentItem()
        index = self.ui.activedatabrowser.indexOfTopLevelItem(cur_item)
        self.ui.activedatabrowser.takeTopLevelItem(index)
        return True
        
    def resetDataSet(self):
        self.ui.activedatabrowser.clear()        
        return True
        
    def updateActiveDataItems(self):
        tlitms = []
        for i in range(self.ui.activedatabrowser.topLevelItemCount()):
            tlitms.append(self.ui.activedatabrowser.topLevelItem(i))
        self.__activedataitems = {}
        for i in tlitms:
            self.__activedataitems[str(i.text(1))] = str(i.text(0))
        return True
        
    def save_values(self):
        self.updateActiveDataItems()
        self.module.setCycleDataSet(self.__curstate, self.__tabindex, self.__activedataitems)
        return True























        







        
        