# -*- coding: utf-8 -*-
"""
@file
@author  Peter M Bach <peterbach@gmail.com>
@version 1.0
@section LICENSE

This file is part of VIBe2
Copyright (C) 2016 Peter M Bach

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
import os
from PyQt4 import QtCore, QtGui
from urbanbeatscalibrationgui import Ui_CalibrationGUI_Dialog
import urbanbeatscalibrationscripts as ubcal


class CalibrationGUILaunch(QtGui.QDialog):
    def __init__(self, activesim, tabindex, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_CalibrationGUI_Dialog()
        self.ui.setupUi(self)
        self.activesim = activesim
        self.calibrationhistory = self.activesim.getCalibrationHistory()

        #Setup GUI
        self.ui.set_param_combo.setCurrentIndex(0)
        self.ui.set_typetotal_radio.setChecked(1)
        self.enabledisableAllGUIs(0)

        QtCore.QObject.connect(self.ui.set_param_combo, QtCore.SIGNAL("currentIndexChanged(int)"), self.changeGUI)
        QtCore.QObject.connect(self.ui.set_param_combo, QtCore.SIGNAL("currentIndexChanged(int)"), self.setupCalibration)
        QtCore.QObject.connect(self.ui.set_typeblock_radio, QtCore.SIGNAL("clicked()"), self.enabledisableGUIs)
        QtCore.QObject.connect(self.ui.set_typetotal_radio, QtCore.SIGNAL("clicked()"), self.enabledisableGUIs)

        #Load calibration data
        QtCore.QObject.connect(self.ui.set_data_load, QtCore.SIGNAL("clicked()"), self.openFileDialog_calibdata)
        QtCore.QObject.connect(self.ui.set_data_reset, QtCore.SIGNAL("clicked()"), self.resetCalibrationData)
        QtCore.QObject.connect(self.ui.set_gen_button, QtCore.SIGNAL("clicked()"), self.generate_calibdata)

        #Do stuff with GUI



        QtCore.QObject.connect(self.ui.closeButton, QtCore.SIGNAL("clicked()"), self.saveHistory)

    def resetCalibrationData(self):
        #Reset Table
        self.calibrationhistory[self.getCalibrationKeyword()] = None
        self.updateGUI()
        return True

    def getCalibrationKeyword(self):
        keys = self.calibrationhistory.keys()
        kwindex = self.ui.set_param_combo.currentIndex() + int(self.ui.set_typetotal_radio.isChecked())*5 - 1
        return keys[kwindex]

    def generate_calibdata(self):
        if self.ui.set_gen_combo.currentIndex() == 0:
            pass
            #Melbourne Water guide
        else:
            pass

    def setupCalibration(self):
        pass

    def retrieveModelData(self):
        pass

    def openFileDialog_calibdata(self):
        fname = QtGui.QFileDialog.getOpenFileName(self, "Choose Calibration Data File...", os.curdir, "Calibration Data (*.csv *.txt)")
        if fname:
            self.calibrationhistory[self.getCalibrationKeyword()] = fname
            calibdata = ubcal.readCalibrationData(fname)

            for i in range(len(calibdata)):
                #Update Table in GUI
                blocknum = QtGui.QTableWidgetItem()
                blocknum.setData(calibdata[i][0])
                datavalue = QtGui.QTableWidgetItem()
                datavalue.setData(calibdata[i][1])
                self.ui.set_data_table.insertRow()
                self.ui.set_data_table.setItem(i, 0, blocknum)
                self.ui.set_data_table.setItem(i, 1, datavalue)

            #self.ui.set_data_table --->

        self.updateGUI()
        return True

    def updateDataTable(self):
        pass

    def changeGUI(self, currentindex):
        if currentindex == 0:
            self.enabledisableAllGUIs(0)
        elif currentindex != 0:
            self.enabledisableAllGUIs(1)
            self.enabledisableGUIs()

    def enabledisableAllGUIs(self, status):
        self.ui.set_typetotal_radio.setEnabled(status)
        self.ui.set_typeblock_radio.setEnabled(status)

        self.ui.set_data_table.setEnabled(status)
        self.ui.set_data_load.setEnabled(status)
        self.ui.set_data_reset.setEnabled(status)
        self.ui.set_gen_combo.setEnabled(status)
        self.ui.set_gen_button.setEnabled(status)
        self.ui.set_eval_nash.setEnabled(status)
        self.ui.set_eval_rmse.setEnabled(status)

        self.ui.set_totvalue_box.setEnabled(status)
        self.ui.set_totvalue_units.setEnabled(status)
        self.ui.set_eval_error.setEnabled(status)

    def enabledisableGUIs(self):
        if self.ui.set_typetotal_radio.isChecked():
            self.ui.set_data_table.setEnabled(0)
            self.ui.set_data_load.setEnabled(0)
            self.ui.set_data_reset.setEnabled(0)
            self.ui.set_gen_combo.setEnabled(0)
            self.ui.set_gen_button.setEnabled(0)
            self.ui.set_eval_nash.setEnabled(0)
            self.ui.set_eval_rmse.setEnabled(0)

            self.ui.set_totvalue_box.setEnabled(1)
            self.ui.set_totvalue_units.setEnabled(1)
            self.ui.set_eval_error.setEnabled(1)

        if self.ui.set_typeblock_radio.isChecked():
            self.ui.set_data_table.setEnabled(1)
            self.ui.set_data_load.setEnabled(1)
            self.ui.set_data_reset.setEnabled(1)
            self.ui.set_gen_combo.setEnabled(1)
            self.ui.set_gen_button.setEnabled(1)
            self.ui.set_eval_nash.setEnabled(1)
            self.ui.set_eval_rmse.setEnabled(1)
            self.ui.set_eval_error.setEnabled(1)

            self.ui.set_totvalue_box.setEnabled(0)
            self.ui.set_totvalue_units.setEnabled(0)

            self.checkGenerateGUI()

    def checkGenerateGUI(self):
        if self.ui.set_param_combo.currentIndex() == 1:
            self.ui.set_gen_button.setEnabled(1)
            self.ui.set_gen_combo.setEnabled(1)
        else:
            self.ui.set_gen_button.setEnabled(0)
            self.ui.set_gen_combo.setEnabled(0)

    def updateGUI(self):
        #Calibration scripts to update the GUI

        pass




    def saveHistory(self):
        """Is called upon GUI closure"""
        self.activesim.setCalibrationHistory(self.calibrationhistory)
