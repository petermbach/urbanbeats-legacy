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

from md_perfassessgui import Ui_Perfconfig_Dialog
from md_perf_custompattern import Ui_CustomPatternDialog
from PyQt4 import QtGui, QtCore
import os

class PerfAssessGUILaunch(QtGui.QDialog):
    def __init__(self, activesim, tabindex, parent = None):
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_Perfconfig_Dialog()
        self.ui.setupUi(self)
        self.module = activesim.getModulePerfAssess(tabindex)

        #Set all default parameters contained in the module file into the GUI's fields

        #----------------------------------------------------------------------#
        #-------- SELECT ANALYSES ---------------------------------------------#
        #----------------------------------------------------------------------#
        if self.module.getParameter("cycletype") == "pc":
            self.ui.select_pc.setChecked(1)
        else:
            self.ui.select_ic.setChecked(1)

        self.ui.perf_MUSIC.setChecked(self.module.getParameter("perf_MUSIC"))
        self.ui.perf_Economics.setChecked(self.module.getParameter("perf_Economics"))
        self.ui.perf_Microclimate.setChecked(self.module.getParameter("perf_Microclimate"))
        self.ui.perf_EPANET.setChecked(self.module.getParameter("perf_EPANET"))
        self.ui.perf_CD3.setChecked(self.module.getParameter("perf_CD3"))

        self.ed_MUSIC()
        #self.ed_Economics()
        #self.ed_Microclimate()
        self.ed_EPANET()
        #self.ed_CD3()

        QtCore.QObject.connect(self.ui.perf_MUSIC, QtCore.SIGNAL("clicked()"), self.ed_MUSIC)
        # QtCore.QObject.connect(self.ui.perf_Economics, QtCore.SIGNAL("clicked()"), self.ed_Economics)
        # QtCore.QObject.connect(self.ui.perf_Microclimate, QtCore.SIGNAL("clicked()"), self.ed_Microclimate)
        QtCore.QObject.connect(self.ui.perf_EPANET, QtCore.SIGNAL("clicked()"), self.ed_EPANET)
        # QtCore.QObject.connect(self.ui.perf_CD3, QtCore.SIGNAL("clicked()"), self.ed_CD3)

        #----------------------------------------------------------------------#
        #-------- MUSIC -------------------------------------------------------#
        #----------------------------------------------------------------------#
        self.versioncombo = ["Version 5", "Version 6"]
        self.ui.music_version_combo.setCurrentIndex(self.versioncombo.index(self.module.getParameter("musicversion")))

        self.ui.music_browse_pathbox.setText(self.module.getParameter("musicclimatefile"))
        QtCore.QObject.connect(self.ui.music_browse_button, QtCore.SIGNAL("clicked()"), self.perf_MUSIC_climatefile)

        self.ui.musicsplit_check.setChecked(self.module.getParameter("musicseparatebasin"))

        self.ui.include_pervious.setChecked(self.module.getParameter("include_pervious"))
        self.ui.musicRR_soil_box.setText(str(self.module.getParameter("musicRR_soil")))
        self.ui.musicRR_field_box.setText(str(self.module.getParameter("musicRR_field")))
        self.ui.musicRR_bfr_spin.setValue(self.module.getParameter("musicRR_bfr"))
        self.ui.musicRR_rcr_spin.setValue(self.module.getParameter("musicRR_rcr"))
        self.ui.musicRR_dsr_spin.setValue(self.module.getParameter("musicRR_dsr"))

        self.ui.include_route.setChecked(self.module.getParameter("include_route"))
        if self.module.getParameter("musicRR_muskk_auto") == 1:
            self.ui.musicRR_muskk_auto.setChecked(1)
        else:
            self.ui.musicRR_muskk_custom.setChecked(1)
        self.ui.musicRR_muskk_spin.setValue(self.module.getParameter("musicRR_muskk"))
        self.ui.musicRR_musktheta_spin.setValue(self.module.getParameter("musicRR_musktheta"))

        self.ui.musicBF_TN_box.setText(str(self.module.getParameter("bf_tncontent")))
        self.ui.musicBF_ortho_box.setText(str(self.module.getParameter("bf_orthophosphate")))

        self.ui.musicauto_check.setChecked(self.module.getParameter("musicautorun"))
        QtCore.QObject.connect(self.ui.musicauto_check, QtCore.SIGNAL("clicked()"), self.ed_MUSIC)

        self.ui.musicpath_box.setText(self.module.getParameter(str("musicpath")))
        QtCore.QObject.connect(self.ui.musicpath_browse, QtCore.SIGNAL("clicked()"), self.perf_MUSIC_pathbrowse)

        self.ui.musictte_check.setChecked(self.module.getParameter("musicTTE"))
        self.ui.musicflux_check.setChecked(self.module.getParameter("musicFlux"))

        self.connect(self.ui.include_pervious, QtCore.SIGNAL("clicked()"), self.ed_catchment)
        self.connect(self.ui.include_route, QtCore.SIGNAL("clicked()"), self.ed_route)
        self.ed_catchment()
        self.ed_route()

        #----------------------------------------------------------------------#
        #-------- ECONOMICS ---------------------------------------------------#
        #----------------------------------------------------------------------#

        #----------------------------------------------------------------------#
        #-------- MICROCLIMATE ------------------------------------------------#
        #----------------------------------------------------------------------#

        #----------------------------------------------------------------------#
        #-------- EPANET ------------------------------------------------------#
        #----------------------------------------------------------------------#
        self.patterncomboindex = ["SDD", "CDP", "OHT", "AHC", "UDP"]

        self.ui.dp_kitchen_combo.setCurrentIndex(self.patterncomboindex.index(self.module.getParameter("kitchenpat")))
        self.ui.dp_shower_combo.setCurrentIndex(self.patterncomboindex.index(self.module.getParameter("showerpat")))
        self.ui.dp_toilet_combo.setCurrentIndex(self.patterncomboindex.index(self.module.getParameter("toiletpat")))
        self.ui.dp_laundry_combo.setCurrentIndex(self.patterncomboindex.index(self.module.getParameter("laundrypat")))
        self.ui.dp_irrigate_combo.setCurrentIndex(self.patterncomboindex.index(self.module.getParameter("irrigationpat")))
        self.ui.dp_com_combo.setCurrentIndex(self.patterncomboindex.index(self.module.getParameter("compat")))
        self.ui.dp_ind_combo.setCurrentIndex(self.patterncomboindex.index(self.module.getParameter("indpat")))
        self.ui.dp_pubirr_combo.setCurrentIndex(self.patterncomboindex.index(self.module.getParameter("publicirripat")))

        self.ui.dp_kitchen_custom.setEnabled(self.ui.dp_kitchen_combo.currentIndex()==4)
        self.ui.dp_shower_custom.setEnabled(self.ui.dp_shower_combo.currentIndex()==4)
        self.ui.dp_toilet_custom.setEnabled(self.ui.dp_toilet_combo.currentIndex()==4)
        self.ui.dp_laundry_custom.setEnabled(self.ui.dp_laundry_combo.currentIndex()==4)
        self.ui.dp_irrigate_custom.setEnabled(self.ui.dp_irrigate_combo.currentIndex()==4)
        self.ui.dp_com_custom.setEnabled(self.ui.dp_com_combo.currentIndex()==4)
        self.ui.dp_ind_custom.setEnabled(self.ui.dp_ind_combo.currentIndex()==4)
        self.ui.dp_pubirr_custom.setEnabled(self.ui.dp_pubirr_combo.currentIndex()==4)

        QtCore.QObject.connect(self.ui.dp_kitchen_combo, QtCore.SIGNAL("currentIndexChanged(int)"), self.dp_combo_customise)
        QtCore.QObject.connect(self.ui.dp_shower_combo, QtCore.SIGNAL("currentIndexChanged(int)"), self.dp_combo_customise)
        QtCore.QObject.connect(self.ui.dp_toilet_combo, QtCore.SIGNAL("currentIndexChanged(int)"), self.dp_combo_customise)
        QtCore.QObject.connect(self.ui.dp_laundry_combo, QtCore.SIGNAL("currentIndexChanged(int)"), self.dp_combo_customise)
        QtCore.QObject.connect(self.ui.dp_irrigate_combo, QtCore.SIGNAL("currentIndexChanged(int)"), self.dp_combo_customise)
        QtCore.QObject.connect(self.ui.dp_com_combo, QtCore.SIGNAL("currentIndexChanged(int)"), self.dp_combo_customise)
        QtCore.QObject.connect(self.ui.dp_ind_combo, QtCore.SIGNAL("currentIndexChanged(int)"), self.dp_combo_customise)
        QtCore.QObject.connect(self.ui.dp_pubirr_combo, QtCore.SIGNAL("currentIndexChanged(int)"), self.dp_combo_customise)

        QtCore.QObject.connect(self.ui.dp_kitchen_custom, QtCore.SIGNAL("clicked()"),lambda enduse="kitchen": self.callPatternGui(enduse))
        QtCore.QObject.connect(self.ui.dp_shower_custom, QtCore.SIGNAL("clicked()"), lambda enduse="shower": self.callPatternGui(enduse))
        QtCore.QObject.connect(self.ui.dp_toilet_custom, QtCore.SIGNAL("clicked()"), lambda enduse="toilet": self.callPatternGui(enduse))
        QtCore.QObject.connect(self.ui.dp_laundry_custom, QtCore.SIGNAL("clicked()"), lambda enduse="laundry": self.callPatternGui(enduse))
        QtCore.QObject.connect(self.ui.dp_irrigate_custom, QtCore.SIGNAL("clicked()"), lambda enduse="irrigation": self.callPatternGui(enduse))
        QtCore.QObject.connect(self.ui.dp_com_custom, QtCore.SIGNAL("clicked()"), lambda enduse="com": self.callPatternGui(enduse))
        QtCore.QObject.connect(self.ui.dp_ind_custom, QtCore.SIGNAL("clicked()"), lambda enduse="ind": self.callPatternGui(enduse))
        QtCore.QObject.connect(self.ui.dp_pubirr_custom, QtCore.SIGNAL("clicked()"), lambda enduse="publicirri": self.callPatternGui(enduse))

        if self.module.getParameter("epanetintmethod") == "NN":
            self.ui.epanet_intnn.setChecked(1)
        elif self.module.getParameter("epanetintmethod") == "RS":
            self.ui.epanet_intrscan.setChecked(1)
        elif self.module.getParameter("epanetintmethod") == "DT":
            self.ui.epanet_intdelaunay.setChecked(1)
        elif self.module.getParameter("epanetintmethod") == "VD":
            self.ui.epanet_intvoronoi.setChecked(1)

        self.ui.epanet_scanradius.setEnabled(self.ui.epanet_intrscan.isChecked())
        self.ui.epanet_scanradius.setValue(float(self.module.getParameter("epanet_scanradius")))

        self.ui.epanet_ignorezero.setChecked(self.module.getParameter("epanet_excludezeros"))
        self.ui.epanet_exportvisual.setChecked(self.module.getParameter("epanet_exportshp"))

        self.ui.epanet_line.setText(str(self.module.getParameter("epanet_inpfname")))
        self.ui.epanet_basesim_check.setChecked(int(self.module.getParameter("runBaseInp")))

        self.epanet_simtypes = ["STS", "24H", "EPS", "LTS"]
        self.ui.epanet_simtypecombo.setCurrentIndex(self.epanet_simtypes.index(self.module.getParameter("epanet_simtype")))

        QtCore.QObject.connect(self.ui.epanet_intnn, QtCore.SIGNAL("clicked()"), self.rscan_boxchange)
        QtCore.QObject.connect(self.ui.epanet_intrscan, QtCore.SIGNAL("clicked()"), self.rscan_boxchange)
        QtCore.QObject.connect(self.ui.epanet_intdelaunay, QtCore.SIGNAL("clicked()"), self.rscan_boxchange)
        QtCore.QObject.connect(self.ui.epanet_intvoronoi, QtCore.SIGNAL("clicked()"), self.rscan_boxchange)
        QtCore.QObject.connect(self.ui.epanet_browse, QtCore.SIGNAL("clicked()"), self.getEpanetInpName)

        self.hleq = ["D-W", "H-W", "C-M"]
        self.ui.epanetsim_hl_combo.setCurrentIndex(self.hleq.index(self.module.getParameter("epanetsim_hl")))
        self.ui.epanetsim_hlc_box.setText(str(self.module.getParameter("epanetsim_hlc")))
        self.ui.epanetsim_hts_box.setText(str(self.module.getParameter("epanetsim_hts")))
        self.ui.epanetsim_qts_box.setText(str(self.module.getParameter("epanetsim_qts")))
        self.ui.epanetsim_hlc_check.setChecked(int(self.module.getParameter("epanetsim_hlc_reassign")))
        self.ui.epanetsim_visc_box.setText(str(self.module.getParameter("epanetsim_visc")))
        self.ui.epanetsim_specg_box.setText(str(self.module.getParameter("epanetsim_specg")))
        self.ui.epanetsim_emit_box.setText(str(self.module.getParameter("epanetsim_emit")))
        self.ui.epanetsim_trials_box.setText(str(self.module.getParameter("epanetsim_trials")))
        self.ui.epanetsim_acc_box.setText(str(self.module.getParameter("epanetsim_accuracy")))
        self.ui.epanetsim_demmult_box.setText(str(self.module.getParameter("epanetsim_demmult")))



        #----------------------------------------------------------------------#
        #-------- INTEGRATED WATER CYCLE MODEL  -------------------------------#
        #----------------------------------------------------------------------#


        QtCore.QObject.connect(self.ui.buttonBox, QtCore.SIGNAL("accepted()"), self.save_values)

    def rscan_boxchange(self):
        self.ui.epanet_scanradius.setEnabled(self.ui.epanet_intrscan.isChecked())
        return True

    def getEpanetInpName(self):
        fname = QtGui.QFileDialog.getOpenFileName(self, "Locate EPANET .inp File...", os.curdir, str("EPANET File (*.inp)"))
        if fname:
            self.ui.epanet_line.setText(fname)
        return True

    def callPatternGui(self, enduse):
        custompatternguic = CustomPatternGUILaunch(self.module, enduse)
        custompatternguic.exec_()
        return True

    def dp_combo_customise(self):
        self.ui.dp_kitchen_custom.setEnabled(self.ui.dp_kitchen_combo.currentIndex()==4)
        self.ui.dp_shower_custom.setEnabled(self.ui.dp_shower_combo.currentIndex()==4)
        self.ui.dp_toilet_custom.setEnabled(self.ui.dp_toilet_combo.currentIndex()==4)
        self.ui.dp_laundry_custom.setEnabled(self.ui.dp_laundry_combo.currentIndex()==4)
        self.ui.dp_irrigate_custom.setEnabled(self.ui.dp_irrigate_combo.currentIndex()==4)
        self.ui.dp_com_custom.setEnabled(self.ui.dp_com_combo.currentIndex()==4)
        self.ui.dp_ind_custom.setEnabled(self.ui.dp_ind_combo.currentIndex()==4)
        self.ui.dp_pubirr_custom.setEnabled(self.ui.dp_pubirr_combo.currentIndex()==4)

    def ed_catchment(self):
        self.ui.musicRR_soil_box.setEnabled(self.ui.include_pervious.isChecked())
        self.ui.musicRR_field_box.setEnabled(self.ui.include_pervious.isChecked())
        self.ui.musicRR_bfr_spin.setEnabled(self.ui.include_pervious.isChecked())
        self.ui.musicRR_rcr_spin.setEnabled(self.ui.include_pervious.isChecked())
        self.ui.musicRR_dsr_spin.setEnabled(self.ui.include_pervious.isChecked())

    def ed_route(self):
        self.ui.musicRR_muskk_auto.setEnabled(self.ui.include_route.isChecked())
        self.ui.musicRR_muskk_spin.setEnabled(self.ui.include_route.isChecked())
        self.ui.musicRR_muskk_custom.setEnabled(self.ui.include_route.isChecked())
        self.ui.musicRR_musktheta_spin.setEnabled(self.ui.include_route.isChecked())

    def ed_MUSIC(self):
        self.ui.music_version_combo.setEnabled(int(self.ui.perf_MUSIC.isChecked()))
        self.ui.music_browse_pathbox.setEnabled(int(self.ui.perf_MUSIC.isChecked()))
        self.ui.music_browse_button.setEnabled(int(self.ui.perf_MUSIC.isChecked()))
        self.ui.musicsplit_check.setEnabled(int(self.ui.perf_MUSIC.isChecked()))
        self.ui.musicBF_TN_box.setEnabled(int(self.ui.perf_MUSIC.isChecked()))
        self.ui.musicBF_ortho_box.setEnabled(int(self.ui.perf_MUSIC.isChecked()))
        # self.ui.musicauto_check.setEnabled(int(self.ui.perf_MUSIC.isChecked()))
        self.ui.musicpath_box.setEnabled(int(self.ui.perf_MUSIC.isChecked()))
        self.ui.musicpath_browse.setEnabled(int(self.ui.perf_MUSIC.isChecked()))
        self.ui.musictte_check.setEnabled(int(self.ui.perf_MUSIC.isChecked()))
        self.ui.musicflux_check.setEnabled(int(self.ui.perf_MUSIC.isChecked()))
        if self.ui.perf_MUSIC.isChecked():
            self.ed_MUSICautorun()

    def ed_MUSICautorun(self):
        self.ui.musicpath_box.setEnabled(int(self.ui.musicauto_check.isChecked()))
        self.ui.musicpath_browse.setEnabled(int(self.ui.musicauto_check.isChecked()))
        self.ui.musictte_check.setEnabled(int(self.ui.musicauto_check.isChecked()))
        self.ui.musicflux_check.setEnabled(int(self.ui.musicauto_check.isChecked()))

    def perf_MUSIC_climatefile(self):
        fname = QtGui.QFileDialog.getOpenFileName(self, "Locate Climate File .mlb...", os.curdir, str("Met Template (*.mlb)"))
        if fname:
            self.ui.music_browse_pathbox.setText(fname)

    def perf_MUSIC_pathbrowse(self):
        fname = QtGui.QFileDialog.getOpenFileName(self, "Locate MUSIC .exe...", os.curdir, str("Executable (*.exe)"))
        if fname:
            self.ui.musicpath_box.setText(fname)

    def ed_Economics(self):
        return True


    def ed_Microclimate(self):
        return True


    def ed_EPANET(self):
        #To write once first pass EPANET module is done
        return True


    def ed_CD3(self):
        return True


    #Save values function
    def save_values(self):
        #----------------------------------------------------------------------#
        #-------- SELECT ANALYSES ---------------------------------------------#
        #----------------------------------------------------------------------#
        if self.ui.select_pc.isChecked():
            self.module.setParameter("cycletype", "pc")
        else:
            self.module.setParameter("cycletype", "ic")

        self.module.setParameter("perf_MUSIC", int(self.ui.perf_MUSIC.isChecked()))
        self.module.setParameter("perf_Economics", int(self.ui.perf_Economics.isChecked()))
        self.module.setParameter("perf_Microclimate", int(self.ui.perf_Microclimate.isChecked()))
        self.module.setParameter("perf_EPANET", int(self.ui.perf_EPANET.isChecked()))
        self.module.setParameter("perf_CD3", int(self.ui.perf_CD3.isChecked()))

        #----------------------------------------------------------------------#
        #-------- MUSIC -------------------------------------------------------#
        #----------------------------------------------------------------------#
        self.module.setParameter("musicversion", self.versioncombo[int(self.ui.music_version_combo.currentIndex())])
        self.module.setParameter("musicclimatefile", self.ui.music_browse_pathbox.text())
        self.module.setParameter("musicseparatebasin", int(self.ui.musicsplit_check.isChecked()))
        self.module.setParameter("include_pervious", int(self.ui.include_pervious.isChecked()))
        self.module.setParameter("musicRR_soil", float(self.ui.musicRR_soil_box.text()))
        self.module.setParameter("musicRR_field", float(self.ui.musicRR_field_box.text()))
        self.module.setParameter("musicRR_bfr", self.ui.musicRR_bfr_spin.value())
        self.module.setParameter("musicRR_rcr", self.ui.musicRR_rcr_spin.value())
        self.module.setParameter("musicRR_dsr", self.ui.musicRR_dsr_spin.value())

        self.module.setParameter("include_route", int(self.ui.include_route.isChecked()))
        self.module.setParameter("musicRR_muskk", self.ui.musicRR_muskk_spin.value())
        self.module.setParameter("musicRR_musktheta", self.ui.musicRR_musktheta_spin.value())

        if self.ui.musicRR_muskk_auto.isChecked():
            self.module.setParameter("musicRR_muskk_auto", 1)
        else:
            self.module.setParameter("musicRR_muskk_auto", 0)

        self.module.setParameter("bf_tncontent", float(self.ui.musicBF_TN_box.text()))
        self.module.setParameter("bf_orthophosphate", float(self.ui.musicBF_ortho_box.text()))
        self.module.setParameter("musicautorun", int(self.ui.musicauto_check.isChecked()))
        self.module.setParameter("musicpath", self.ui.musicpath_box.text())
        self.module.setParameter("musicTTE", int(self.ui.musictte_check.isChecked()))
        self.module.setParameter("musicFlux", int(self.ui.musicflux_check.isChecked()))

        #----------------------------------------------------------------------#
        #-------- ECONOMICS ---------------------------------------------------#
        #----------------------------------------------------------------------#

        #----------------------------------------------------------------------#
        #-------- MICROCLIMATE ------------------------------------------------#
        #----------------------------------------------------------------------#

        #----------------------------------------------------------------------#
        #-------- EPANET ------------------------------------------------------#
        #----------------------------------------------------------------------#
        #Demand Downscaling
        self.module.setParameter("kitchenpat", self.patterncomboindex[self.ui.dp_kitchen_combo.currentIndex()])
        self.module.setParameter("showerpat", self.patterncomboindex[self.ui.dp_shower_combo.currentIndex()])
        self.module.setParameter("toiletpat", self.patterncomboindex[self.ui.dp_toilet_combo.currentIndex()])
        self.module.setParameter("laundrypat", self.patterncomboindex[self.ui.dp_laundry_combo.currentIndex()])
        self.module.setParameter("irrigationpat", self.patterncomboindex[self.ui.dp_irrigate_combo.currentIndex()])
        self.module.setParameter("compat", self.patterncomboindex[self.ui.dp_com_combo.currentIndex()])
        self.module.setParameter("indpat", self.patterncomboindex[self.ui.dp_ind_combo.currentIndex()])
        self.module.setParameter("publicirripat", self.patterncomboindex[self.ui.dp_pubirr_combo.currentIndex()])

        #Weekly and Seasonal Scaling

        #Network Hydraulics

        #EPANET Link
        if self.ui.epanet_intnn.isChecked():
            self.module.setParameter("epanetintmethod", "NN")
        elif self.ui.epanet_intrscan.isChecked():
            self.module.setParameter("epanetintmethod", "RS")
        elif self.ui.epanet_intdelaunay.isChecked():
            self.module.setParameter("epanetintmethod", "DT")
        elif self.ui.epanet_intvoronoi.isChecked():
            self.module.setParameter("epanetintmethod", "VD")

        self.module.setParameter("epanet_scanradius", float(self.ui.epanet_scanradius.value()))
        self.module.setParameter("epanet_excludezeros", int(self.ui.epanet_ignorezero.isChecked()))
        self.module.setParameter("epanet_exportshp", int(self.ui.epanet_exportvisual.isChecked()))
        self.module.setParameter("epanet_inpfname", str(self.ui.epanet_line.text()))
        self.module.setParameter("runBaseInp", int(self.ui.epanet_basesim_check.isChecked()))
        self.module.setParameter("epanet_simtype", self.epanet_simtypes[self.ui.epanet_simtypecombo.currentIndex()])

        self.hleq = ["D-W", "H-W", "C-M"]
        self.module.setParameter("epanetsim_hl", self.hleq[self.ui.epanetsim_hl_combo.currentIndex()])
        self.module.setParameter("epanetsim_hlc", float(self.ui.epanetsim_hlc_box.text()))
        self.module.setParameter("epanetsim_hts", self.ui.epanetsim_hts_box.text())
        self.module.setParameter("epanetsim_qts", self.ui.epanetsim_qts_box.text())
        self.module.setParameter("epanetsim_hlc_reassign", int(self.ui.epanetsim_hlc_check.isChecked()))
        self.module.setParameter("epanetsim_visc", float(self.ui.epanetsim_visc_box.text()))
        self.module.setParameter("epanetsim_specg", float(self.ui.epanetsim_specg_box.text()))
        self.module.setParameter("epanetsim_emit", float(self.ui.epanetsim_emit_box.text()))
        self.module.setParameter("epanetsim_trials", float(self.ui.epanetsim_trials_box.text()))
        self.module.setParameter("epanetsim_accuracy", float(self.ui.epanetsim_acc_box.text()))
        self.module.setParameter("epanetsim_demmult", float(self.ui.epanetsim_demmult_box.text()))

        #----------------------------------------------------------------------#
        #-------- INTEGRATED WATER CYCLE MODEL  -------------------------------#
        #----------------------------------------------------------------------#


class CustomPatternGUILaunch(QtGui.QDialog):
    def __init__(self, activesim, enduse, parent = None):
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_CustomPatternDialog()
        self.ui.setupUi(self)
        self.module = activesim
        self.enduse = enduse
        #Transfer pattern data into table

        endusekeys = {"kitchen":"Kitchen", "shower": "Shower", "toilet":"Toilet", "laundry":"Laundry",
                      "irrigation": "Garden Irrigation", "com": "Commercial", "ind":"Light & Heavy Industry",
                      "publicirri": "Public Open Space Irrigation"}

        self.ui.endusetype.setText(endusekeys[self.enduse])
        self.pattern = self.module.getCustomPattern(self.enduse)

        avgscalar = sum(self.pattern)/len(self.pattern)
        self.ui.avg_box.setText(str(round(avgscalar,3)))

        for i in range(24):
            self.ui.tableWidget.item(i,0).setText(str(self.pattern[i]))

        QtCore.QObject.connect(self.ui.tableWidget, QtCore.SIGNAL("itemChanged(QTableWidgetItem *)"), self.recalcAvg)
        QtCore.QObject.connect(self.ui.button_Box, QtCore.SIGNAL("accepted()"), self.save_values)

    def recalcAvg(self):
        subpattern = []
        for i in range(24):
            subpattern.append(float(self.ui.tableWidget.item(i,0).text()))
        try:
            avgscalar = sum(subpattern)/len(subpattern)
            self.ui.avg_box.setText(str(round(avgscalar,3)))
        except:
            self.ui.avg_box.setText("ERROR")

    def save_values(self):
        for i in range(24):
            self.pattern[i] = float(self.ui.tableWidget.item(i,0).text())

        self.module.changeCustomPattern(self.enduse, self.pattern)
        return True