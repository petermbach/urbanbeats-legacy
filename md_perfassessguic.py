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
        self.ui.perf_MUSIC.setChecked(self.module.getParameter("perf_MUSIC"))
        self.ui.perf_Economics.setChecked(self.module.getParameter("perf_Economics"))
        self.ui.perf_Microclimate.setChecked(self.module.getParameter("perf_Microclimate"))
        self.ui.perf_EPANET.setChecked(self.module.getParameter("perf_EPANET"))
        self.ui.perf_CD3.setChecked(self.module.getParameter("perf_CD3"))

        self.ed_MUSIC()

        #self.ed_Economics()
        #self.ed_Microclimate()
        #self.ed_EPANET()
        #self.ed_CD3()

        QtCore.QObject.connect(self.ui.perf_MUSIC, QtCore.SIGNAL("clicked()"), self.ed_MUSIC)
        # QtCore.QObject.connect(self.ui.perf_Economics, QtCore.SIGNAL("clicked()"), self.ed_Economics)
        # QtCore.QObject.connect(self.ui.perf_Microclimate, QtCore.SIGNAL("clicked()"), self.ed_Microclimate)
        # QtCore.QObject.connect(self.ui.perf_EPANET, QtCore.SIGNAL("clicked()"), self.ed_EPANET)
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

        #----------------------------------------------------------------------#
        #-------- INTEGRATED WATER CYCLE MODEL  -------------------------------#
        #----------------------------------------------------------------------#


        QtCore.QObject.connect(self.ui.buttonBox, QtCore.SIGNAL("accepted()"), self.save_values)

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
        return True


    def ed_CD3(self):
        return True


    #Save values function
    def save_values(self):
        #----------------------------------------------------------------------#
        #-------- SELECT ANALYSES ---------------------------------------------#
        #----------------------------------------------------------------------#
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

        #----------------------------------------------------------------------#
        #-------- INTEGRATED WATER CYCLE MODEL  -------------------------------#
        #----------------------------------------------------------------------#
