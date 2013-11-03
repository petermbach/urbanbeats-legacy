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

from md_delinblocksgui import Ui_DelinBlocksDialog
from PyQt4 import QtGui, QtCore

class DelinBlocksGUILaunch(QtGui.QDialog):
    def __init__(self, activesim, parent = None):
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_DelinBlocksDialog()
        self.ui.setupUi(self)
        self.module = activesim.getModuleDelinblocks()
        
        self.cities = ["Adelaide", "Brisbane", "Cairns", "Canberra", "Copenhagen", "Innsbruck", "Kuala Lumpur", "London", "Melbourne", "Munich", "Perth", "Singapore", "Sydney", "Vienna"]
        
        #Set all default parameters contained in the module file into the GUI's fields
        
        #----------------------------------------------------------------------#
        #-------- GENERAL SIMULATION INPUTS------------------------------------#
        #----------------------------------------------------------------------#
        self.ui.blocksize_in.setValue(int(self.module.getParameter("BlockSize")))
        
        if self.module.getParameter("blocksize_auto") == 1:
            self.ui.blocksize_auto.setChecked(1)
            self.ui.blocksize_in.setEnabled(0)
        else:
            self.ui.blocksize_auto.setChecked(0)
            self.ui.blocksize_in.setEnabled(1)
        
        QtCore.QObject.connect(self.ui.blocksize_auto, QtCore.SIGNAL("clicked()"), self.block_auto_size)
        
        #----------------------------------------------------------------------#
        #-------- PROCESSING INPUT DATA ---------------------------------------#
        #----------------------------------------------------------------------#        
        if self.module.getParameter("popdatatype") == "C":
            self.ui.popdata_totradio.setChecked(True)
        elif self.module.getParameter("popdatatype") == "D":
            self.ui.popdata_densradio.setChecked(True)

        if self.module.getParameter("soildatatype") == "C":
            self.ui.soildata_classify.setChecked(True)
            self.ui.soildata_unitscombo.setEnabled(False)
        elif self.module.getParameter("soildatatype") == "I":
            self.ui.soildata_infil.setChecked(True)
            self.ui.soildata_unitscombo.setEnabled(True)
        
        if self.module.getParameter("soildataunits") == "hrs":
            self.ui.soildata_unitscombo.setCurrentIndex(0)
        elif self.module.getParameter("soildataunits") == "sec":
            self.ui.soildata_unitscombo.setCurrentIndex(1)
        
        QtCore.QObject.connect(self.ui.soildata_classify, QtCore.SIGNAL("clicked()"), self.soildata_modify)
        QtCore.QObject.connect(self.ui.soildata_infil, QtCore.SIGNAL("clicked()"), self.soildata_modify)
        
        if self.module.getParameter("elevdatadatum") == "S":
            self.ui.elev_sealevel.setChecked(True)
            self.ui.elev_referencebox.setEnabled(False)
        elif self.module.getParameter("elevdatadatum") == "C":
            self.ui.elev_custom.setChecked(True)
            self.ui.elev_referencebox.setEnabled(True)
            
        QtCore.QObject.connect(self.ui.elev_sealevel, QtCore.SIGNAL("clicked()"), self.elevCustomDatum_modify)
        QtCore.QObject.connect(self.ui.elev_custom, QtCore.SIGNAL("clicked()"), self.elevCustomDatum_modify)
        
        self.ui.elev_referencebox.setText(str(self.module.getParameter("elevdatacustomref")))
        
        self.ui.planmap_check.setChecked(int(self.module.getParameter("include_plan_map")))
        self.ui.localmap_check.setChecked(int(self.module.getParameter("include_local_map")))
        
        if self.module.getParameter("include_employment") == True:
            self.ui.employment_check.setChecked(True)
            self.ui.jobdata_totradio.setEnabled(True)
            self.ui.jobdata_densradio.setEnabled(True)
        else:
            self.ui.employment_check.setChecked(False)
            self.ui.jobdata_totradio.setEnabled(False)
            self.ui.jobdata_densradio.setEnabled(False)        
        
        if self.module.getParameter("jobdatatype") == "C":
            self.ui.jobdata_totradio.setChecked(True)
        elif self.module.getParameter("jobdatatype") == "D":
            self.ui.jobdata_densradio.setChecked(True)
        
        QtCore.QObject.connect(self.ui.employment_check, QtCore.SIGNAL("clicked()"), self.employment_modify)
        
        self.ui.rivers_check.setChecked(int(self.module.getParameter("include_rivers")))
        self.ui.lakes_check.setChecked(int(self.module.getParameter("include_lakes")))
        
        if self.module.getParameter("include_groundwater") == True:
            self.ui.groundwater_check.setChecked(True)
            self.ui.groundwater_datumcombo.setEnabled(True)
        else:
            self.ui.groundwater_check.setChecked(False)
            self.ui.groundwater_datumcombo.setEnabled(False)
        
        if self.module.getParameter("groundwater_datum") == "Sea":
            self.ui.groundwater_datumcombo.setCurrentIndex(0)
        elif self.module.getParameter("groundwater_datum") == "Surf":
            self.ui.groundwater_datumcombo.setCurrentIndex(1)
        
        QtCore.QObject.connect(self.ui.groundwater_check, QtCore.SIGNAL("clicked()"), self.groundwaterDatum_modify)
        
        #self.ui.roadnet_check.setChecked(int(self.module.getParameter("include_road_net")))     #Future version
        #self.ui.sewermains_check.setChecked(int(self.module.getParameter("include_sewer_net")))
        #self.ui.supplymains_check.setChecked(int(self.module.getParameter("include_supply_net")))
        
        #conditions for what user inputs from main module are
        if self.module.getParameter("include_soc_par1") == True:
            self.ui.soc_par1_check.setChecked(1)
            self.ui.soc_par1_box.setText(self.module.getParameter("social_par1_name"))
            self.ui.socpar1binary_radio.setEnabled(1)
            self.ui.socpar1prop_radio.setEnabled(1)
        else:
            self.ui.soc_par1_check.setChecked(0)
            self.ui.soc_par1_box.setEnabled(0)
            self.ui.soc_par1_box.setText(self.module.getParameter("social_par1_name"))
            self.ui.socpar1binary_radio.setEnabled(0)
            self.ui.socpar1prop_radio.setEnabled(0)
        
        if self.module.getParameter("socpar1_type") == "B":
            self.ui.socpar1binary_radio.setChecked(True)
        elif self.module.getParameter("socpar1_type") == "P":
            self.ui.socpar1prop_radio.setChecked(True)
            
        if self.module.getParameter("include_soc_par2") == True:
            self.ui.soc_par2_check.setChecked(1)
            self.ui.soc_par2_box.setText(self.module.getParameter("social_par2_name"))
            self.ui.socpar2binary_radio.setEnabled(1)
            self.ui.socpar2prop_radio.setEnabled(1)
        else:
            self.ui.soc_par2_check.setChecked(0)
            self.ui.soc_par2_box.setEnabled(0)
            self.ui.soc_par2_box.setText(self.module.getParameter("social_par2_name"))
            self.ui.socpar2binary_radio.setEnabled(0)
            self.ui.socpar2prop_radio.setEnabled(0)
        
        if self.module.getParameter("socpar2_type") == "B":
            self.ui.socpar2binary_radio.setChecked(True)
        elif self.module.getParameter("socpar2_type") == "P":
            self.ui.socpar2prop_radio.setChecked(True)
        
        self.ui.spatialpatches_check.setChecked(int(self.module.getParameter("patchdelin")))
        self.ui.spatialstats_check.setChecked(int(self.module.getParameter("spatialmetrics")))
        
        QtCore.QObject.connect(self.ui.soc_par1_check, QtCore.SIGNAL("clicked()"), self.social_par1_modify)
        QtCore.QObject.connect(self.ui.soc_par2_check, QtCore.SIGNAL("clicked()"), self.social_par2_modify)
        
        #----------------------------------------------------------------------#
        #-------- MAP CONNECTIVITY INPUTS -------------------------------------#
        #----------------------------------------------------------------------#
        if self.module.getParameter("Neighbourhood") == "N":
            self.ui.radioVNeum.setChecked(True)
        if self.module.getParameter("Neighbourhood") == "M":
            self.ui.radioMoore.setChecked(True)
            self.ui.neighb_vnfp_check.setEnabled(0)
            self.ui.neighb_vnpd_check.setEnabled(0)
        
        self.ui.neighb_vnfp_check.setChecked(int(self.module.getParameter("vn4FlowPaths")))
        self.ui.neighb_vnpd_check.setChecked(int(self.module.getParameter("vn4Patches")))
        
        QtCore.QObject.connect(self.ui.radioVNeum, QtCore.SIGNAL("clicked()"), self.vnOptions_modify)
        QtCore.QObject.connect(self.ui.radioMoore, QtCore.SIGNAL("clicked()"), self.vnOptions_modify)
        
        #Flowpath COMBO BOX
        if self.module.getParameter("flow_method") == "DI":
            self.ui.flowpath_combo.setCurrentIndex(0)
        elif self.module.getParameter("flow_method") == "D8":
            self.ui.flowpath_combo.setCurrentIndex(1)
        
        if self.module.getParameter("demsmooth_choose") == True:
            self.ui.demsmooth_check.setChecked(1)
        else:
            self.ui.demsmooth_check.setChecked(0)
            self.ui.demsmooth_spin.setEnabled(0)
            
        self.ui.demsmooth_spin.setValue(int(self.module.getParameter("demsmooth_passes")))
        
        QtCore.QObject.connect(self.ui.demsmooth_check, QtCore.SIGNAL("clicked()"), self.demsmooth_modify)
        
        #----------------------------------------------------------------------#
        #-------- REGIONAL GEOGRAPHY INPUTS -----------------------------------#
        #----------------------------------------------------------------------#    
        
        if self.module.getParameter("locationOption") == "S":
            self.ui.cbdknown_radio.setChecked(True)
            self.ui.cbd_combo.setEnabled(1)
            self.ui.cbdlong_box.setEnabled(0)
            self.ui.cbdlat_box.setEnabled(0)
        if self.module.getParameter("locationOption") == "C":
            self.ui.cbdmanual_radio.setChecked(True)
            self.ui.cbd_combo.setEnabled(0)
            self.ui.cbdlong_box.setEnabled(1)
            self.ui.cbdlat_box.setEnabled(1)
        
        if self.module.getParameter("considerCBD") == True:
            self.ui.considergeo_check.setChecked(1)
            self.ui.cbdknown_radio.setEnabled(1)
            self.ui.cbdmanual_radio.setEnabled(1)
            self.ui.cbdmark_check.setEnabled(1)
            self.cbdupdate()
        else:
            self.ui.considergeo_check.setChecked(0)
            self.ui.cbdknown_radio.setEnabled(0)
            self.ui.cbdmanual_radio.setEnabled(0)
            self.ui.cbdmark_check.setEnabled(0)
            self.ui.cbd_combo.setEnabled(0)
            self.ui.cbdlong_box.setEnabled(0)
            self.ui.cbdlat_box.setEnabled(0)
        
        try:
            citiesindex = self.cities.index(self.module.getParameter("locationCity"))
        except:
            citiesindex = 0
        self.ui.cbd_combo.setCurrentIndex(citiesindex)
        
        self.ui.cbdlong_box.setText(str(self.module.getParameter("locationLong")))
        self.ui.cbdlat_box.setText(str(self.module.getParameter("locationLat")))
        self.ui.cbdmark_check.setChecked(int(self.module.getParameter("marklocation")))
        
        QtCore.QObject.connect(self.ui.considergeo_check, QtCore.SIGNAL("clicked()"), self.geoupdate)
        QtCore.QObject.connect(self.ui.cbdknown_radio, QtCore.SIGNAL("clicked()"), self.cbdupdate)
        QtCore.QObject.connect(self.ui.cbdmanual_radio, QtCore.SIGNAL("clicked()"), self.cbdupdate)
        
        #QTCORE CONNECTS, REAL TIME GUI CHANGE COMMANDS
        QtCore.QObject.connect(self.ui.buttonBox, QtCore.SIGNAL("accepted()"), self.save_values)
        
    #====================================================================================================
    #Enable-Disable functions for social parameters based on QtCore.QObject.connect() lines
    
    def block_auto_size(self):
        if self.ui.blocksize_auto.isChecked() == 1:
            self.ui.blocksize_in.setEnabled(0)
        else:
            self.ui.blocksize_in.setEnabled(1)
    
    def soildata_modify(self):
        if self.ui.soildata_infil.isChecked() == 1:
            self.ui.soildata_unitscombo.setEnabled(True)
        else:
            self.ui.soildata_unitscombo.setEnabled(False)
    
    def elevCustomDatum_modify(self):
        if self.ui.elev_sealevel.isChecked() == 1:
            self.ui.elev_referencebox.setEnabled(False)
        elif self.ui.elev_custom.isChecked() == 1:
            self.ui.elev_referencebox.setEnabled(True)
    
    def employment_modify(self):
        if self.ui.employment_check.isChecked() == 1:
            self.ui.jobdata_totradio.setEnabled(True)
            self.ui.jobdata_densradio.setEnabled(True)
        else:
            self.ui.jobdata_totradio.setEnabled(False)
            self.ui.jobdata_densradio.setEnabled(False)
    
    def groundwaterDatum_modify(self):
        if self.ui.groundwater_check.isChecked() == 1:
            self.ui.groundwater_datumcombo.setEnabled(True)
        else:
            self.ui.groundwater_datumcombo.setEnabled(False)
    
    def social_par1_modify(self):
        if self.ui.soc_par1_check.isChecked() == 1:
            self.ui.soc_par1_box.setEnabled(1)
            self.ui.socpar1binary_radio.setEnabled(1)
            self.ui.socpar1prop_radio.setEnabled(1)
        else:
            self.ui.soc_par1_box.setEnabled(0)
            self.ui.socpar1binary_radio.setEnabled(0)
            self.ui.socpar1prop_radio.setEnabled(0)
    
    def social_par2_modify(self):
        if self.ui.soc_par2_check.isChecked() == 1:
            self.ui.soc_par2_box.setEnabled(1)
            self.ui.socpar2binary_radio.setEnabled(1)
            self.ui.socpar2prop_radio.setEnabled(1)
        else:
            self.ui.soc_par2_box.setEnabled(0)
            self.ui.socpar2binary_radio.setEnabled(0)
            self.ui.socpar2prop_radio.setEnabled(0)
            
    def demsmooth_modify(self):
        if self.ui.demsmooth_check.isChecked() == 1:
            self.ui.demsmooth_spin.setEnabled(1)
        else:
            self.ui.demsmooth_spin.setEnabled(0)
    
    def vnOptions_modify(self):
        if self.ui.radioVNeum.isChecked() == 1:
            self.ui.neighb_vnfp_check.setEnabled(1)
            self.ui.neighb_vnpd_check.setEnabled(1)
        else:
            self.ui.neighb_vnfp_check.setEnabled(0)
            self.ui.neighb_vnpd_check.setEnabled(0)
    
    def geoupdate(self):
        if self.ui.considergeo_check.isChecked() == 1:
            self.ui.cbdknown_radio.setEnabled(1)
            self.ui.cbdmanual_radio.setEnabled(1)
            self.ui.cbdmark_check.setEnabled(1)
            self.cbdupdate()
        else:
            self.ui.considergeo_check.setChecked(0)
            self.ui.cbdknown_radio.setEnabled(0)
            self.ui.cbdmanual_radio.setEnabled(0)
            self.ui.cbdmark_check.setEnabled(0)
            self.ui.cbd_combo.setEnabled(0)
            self.ui.cbdlong_box.setEnabled(0)
            self.ui.cbdlat_box.setEnabled(0)
            
    def cbdupdate(self):
        if self.ui.cbdknown_radio.isChecked() == 1:
            self.ui.cbd_combo.setEnabled(1)
            self.ui.cbdlong_box.setEnabled(0)
            self.ui.cbdlat_box.setEnabled(0)
        elif self.ui.cbdmanual_radio.isChecked() == 1:
            self.ui.cbd_combo.setEnabled(0)
            self.ui.cbdlong_box.setEnabled(1)
            self.ui.cbdlat_box.setEnabled(1)
    
    #====================================================================================================
    
    #Save values function
    def save_values(self):
        #----------------------------------------------------------------------#
        #-------- GENERAL SIMULATION INPUTS------------------------------------#
        #----------------------------------------------------------------------#
        self.module.setParameter("BlockSize", self.ui.blocksize_in.value())
        self.module.setParameter("blocksize_auto", int(int(self.ui.blocksize_auto.isChecked())))
        
        #----------------------------------------------------------------------#
        #-------- PROCESSING INPUT DATA ---------------------------------------#
        #----------------------------------------------------------------------#
        if self.ui.popdata_totradio.isChecked() == True:
            popdatatype = "C"
        if self.ui.popdata_densradio.isChecked() == True:
            popdatatype = "D"
        self.module.setParameter("popdatatype", popdatatype)
        
        if self.ui.soildata_classify.isChecked() == True:
            soildatatype = "C"
        if self.ui.soildata_infil.isChecked() == True:
            soildatatype = "I"
        self.module.setParameter("soildatatype", soildatatype)
        
        soilunits = ["hrs", "sec"]
        self.module.setParameter("soildataunits", soilunits[self.ui.soildata_unitscombo.currentIndex()])
        
        if self.ui.elev_sealevel.isChecked() == True:
            elevdatadatum = "S"
        if self.ui.elev_custom.isChecked() == True:
            elevdatadatum = "C"
        self.module.setParameter("elevdatadatum", elevdatadatum)
        
        self.module.setParameter("elevdatacustomref", float(self.ui.elev_referencebox.text()))
        
        self.module.setParameter("include_plan_map", int(self.ui.planmap_check.isChecked()))
        self.module.setParameter("include_local_map", int(self.ui.localmap_check.isChecked()))
        
        self.module.setParameter("include_employment", int(self.ui.employment_check.isChecked()))
        
        if self.ui.jobdata_totradio.isChecked() == True:
            jobdatatype = "C"
        elif self.ui.jobdata_densradio.isChecked() == True:
            jobdatatype = "D"
        self.module.setParameter("jobdatatype", jobdatatype)
        
        self.module.setParameter("include_rivers", int(self.ui.rivers_check.isChecked()))
        self.module.setParameter("include_lakes", int(self.ui.lakes_check.isChecked()))
        
        self.module.setParameter("include_groundwater", int(self.ui.groundwater_check.isChecked()))
        
        gwoptions = ["Sea", "Surf"]
        self.module.setParameter("groundwater_datum", gwoptions[self.ui.groundwater_datumcombo.currentIndex()])
        
        #self.module.setParameter("include_road_net", int(self.ui.roadnet_check.isChecked()))
        
        if self.ui.soc_par1_check.isChecked() == 1:
            include_soc_par1 = 1
            
            social_par1_name = str(self.ui.soc_par1_box.text())
            self.module.setParameter("social_par1_name", social_par1_name)
            
            if self.ui.socpar1binary_radio.isChecked() == True:
                socpar1_type = "B"
            if self.ui.socpar1prop_radio.isChecked() == True:
                socpar1_type = "P"
            self.module.setParameter("socpar1_type", socpar1_type)
            
        else:
            include_soc_par1 = 0
            
        self.module.setParameter("include_soc_par1", include_soc_par1)
        
        if self.ui.soc_par2_check.isChecked() == 1:
            include_soc_par2 = 1
            
            social_par2_name = str(self.ui.soc_par2_box.text())
            self.module.setParameter("social_par2_name", social_par2_name)
            
            if self.ui.socpar2binary_radio.isChecked() == True:
                socpar2_type = "B"
            if self.ui.socpar2prop_radio.isChecked() == True:
                socpar2_type = "P"
            self.module.setParameter("socpar2_type", socpar2_type)
            
        else:
            include_soc_par2 = 0
            
        self.module.setParameter("include_soc_par2", include_soc_par2)
        
        self.module.setParameter("patchdelin", int(self.ui.spatialpatches_check.isChecked()))
        self.module.setParameter("spatialmetrics", int(self.ui.spatialstats_check.isChecked()))
        
        #----------------------------------------------------------------------#
        #-------- MAP CONNECTIVITY PARAMETERS----------------------------------#
        #----------------------------------------------------------------------#
        if self.ui.radioMoore.isChecked() == True:
            neighbourhood = "M"
        if self.ui.radioVNeum.isChecked() == True:
            neighbourhood = "N"
        self.module.setParameter("Neighbourhood", neighbourhood)
        
        self.module.setParameter("vn4FlowPaths", int(self.ui.neighb_vnfp_check.isChecked()))
        self.module.setParameter("vn4Patches", int(self.ui.neighb_vnpd_check.isChecked()))
        
        #Combo Box
        flow_path_matrix = ["DI","D8"]
        flow_pathindex = self.ui.flowpath_combo.currentIndex()
        flow_method = flow_path_matrix[flow_pathindex]
        self.module.setParameter("flow_method", flow_method)
        
        self.module.setParameter("demsmooth_choose", int(self.ui.demsmooth_check.isChecked()))
        self.module.setParameter("demsmooth_passes", self.ui.demsmooth_spin.value())
        
        #----------------------------------------------------------------------#
        #-------- REGIONAL GEOGRAPHY INPUTS -----------------------------------#
        #----------------------------------------------------------------------#
        self.module.setParameter("considerCBD", int(self.ui.considergeo_check.isChecked()))
        self.module.setParameter("marklocation", int(self.ui.cbdmark_check.isChecked()))

        if self.ui.cbdknown_radio.isChecked() == True:
            locationOption = "S"        #Selection
        elif self.ui.cbdmanual_radio.isChecked() == True:
            locationOption = "C"        #Coordinates
        self.module.setParameter("locationOption", str(locationOption))
        
        cityname = self.cities[self.ui.cbd_combo.currentIndex()]
        self.module.setParameter("locationCity", str(cityname))        
        
        self.module.setParameter("locationLong", float(self.ui.cbdlong_box.text()))
        self.module.setParameter("locationLat", float(self.ui.cbdlat_box.text()))

        self.emit(QtCore.SIGNAL("updatedDetails"))