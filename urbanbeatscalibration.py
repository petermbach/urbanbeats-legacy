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

        self.activeCalibrationData = []
        self.activeCalibrationValue = None

        #Setup GUI
        self.ui.set_param_combo.setCurrentIndex(0)
        self.ui.set_typetotal_radio.setChecked(1)
        self.enabledisableAllGUIs(0)

        QtCore.QObject.connect(self.ui.set_param_combo, QtCore.SIGNAL("currentIndexChanged(int)"), self.changeGUI)
        QtCore.QObject.connect(self.ui.set_param_combo, QtCore.SIGNAL("currentIndexChanged(int)"), self.setupCalibration)
        QtCore.QObject.connect(self.ui.set_typeblock_radio, QtCore.SIGNAL("clicked()"), self.enabledisableGUIs)
        QtCore.QObject.connect(self.ui.set_typeblock_radio, QtCore.SIGNAL("clicked()"), self.setupCalibration)
        QtCore.QObject.connect(self.ui.set_typetotal_radio, QtCore.SIGNAL("clicked()"), self.enabledisableGUIs)
        QtCore.QObject.connect(self.ui.set_typetotal_radio, QtCore.SIGNAL("clicked()"), self.setupCalibration)

        QtCore.QObject.connect(self.ui.set_totvalue_box, QtCore.SIGNAL("editingFinished()"), self.updateSingleValue)

        #Load calibration data
        QtCore.QObject.connect(self.ui.set_data_load, QtCore.SIGNAL("clicked()"), self.openFileDialog_calibdata)
        QtCore.QObject.connect(self.ui.set_data_reset, QtCore.SIGNAL("clicked()"), self.resetCalibrationData)
        QtCore.QObject.connect(self.ui.set_gen_button, QtCore.SIGNAL("clicked()"), self.generate_calibdata)

        #Save state of calibration data
        QtCore.QObject.connect(self.ui.closeButton, QtCore.SIGNAL("clicked()"), self.saveHistory)
        QtCore.QObject.connect(self.ui.out_export, QtCore.SIGNAL("clicked()"), self.exportCalibrationResults)

    def updateSingleValue(self):
        self.calibrationhistory[self.getCalibrationKeyword()] = self.ui.set_totvalue_box.text()
        return True

    def resetCalibrationData(self):
        #Reset Table
        self.calibrationhistory[self.getCalibrationKeyword()] = None
        self.ui.set_data_table.setRowCount(0)
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
        """Sets up the calibration by retrieving modelled data and updates the calibration data table"""
        #Change Units regardless of single value or block-based comparison used

        units = ["", "units: [sqm]", "units: []", "units: []", "units: [sqm]", "units: [kL/yr]"]
        self.ui.set_totvalue_units.setText(units[self.ui.set_param_combo.currentIndex()])

        #Retrieve Model Data    mod = [[Blk ID], [Data]]
        if self.ui.set_param_combo.currentIndex() == 0:
            pass
        elif self.ui.set_param_combo.currentIndex() == 1:       #Blk_TIA
            mod = self.retrieveModelData(["Blk_TIA"])
        elif self.ui.set_param_combo.currentIndex() == 2:       #Res Allotments
            mod = self.retrieveModelData([""])
        elif self.ui.set_param_combo.currentIndex() == 3:       #Res Dwelling Count
            mod = self.retrieveModelData([""])
        elif self.ui.set_param_combo.currentIndex() == 4:       #Res Roof Area
            mod = self.retrieveModelData([""])
        elif self.ui.set_param_combo.currentIndex() == 5:       #Total Water Demand
            mod = self.retrieveModelData(["Blk_WD"])

        if self.ui.set_typetotal_radio.isChecked():
            pass
            #mod = sum(mod[1])

        #Update calibration data table
        if self.calibrationhistory[self.getCalibrationKeyword()] == None:
            self.ui.set_totvalue_box.clear()
            self.ui.set_data_table.setRowCount(0)
            return True

        if self.ui.set_typeblock_radio.isChecked():
            calibdata = ubcal.readCalibrationData(str(self.calibrationhistory[self.getCalibrationKeyword()]))
            self.updateCalibrationDataTable(calibdata)
        else:
            self.ui.set_totvalue_box.setText(str(self.calibrationhistory[self.getCalibrationKeyword()]))


    def updateCalibrationDataTable(self, calibdata):
        self.ui.set_data_table.setRowCount(0)

        for i in range(len(calibdata)):
            #Update Table in GUI
            rowPosition = self.ui.set_data_table.rowCount()
            self.ui.set_data_table.insertRow(rowPosition)
            blocknum = calibdata[i][0]
            datavalue = calibdata[i][1]
            self.ui.set_data_table.setItem(rowPosition, 0, QtGui.QTableWidgetItem(str(blocknum)))
            self.ui.set_data_table.setItem(rowPosition, 1, QtGui.QTableWidgetItem(str(datavalue)))


    def retrieveModelData(self, attributes):
        pass

    def openFileDialog_calibdata(self):
        fname = QtGui.QFileDialog.getOpenFileName(self, "Choose Calibration Data File...", os.curdir, "Calibration Data (*.csv *.txt)")
        if fname:
            self.calibrationhistory[self.getCalibrationKeyword()] = fname
            calibdata = ubcal.readCalibrationData(fname)
            self.updateCalibrationDataTable(calibdata)

        self.updateGUI()
        return True


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

    def saveHistory(self):
        """Is called upon GUI closure"""
        self.activesim.setCalibrationHistory(self.calibrationhistory)

    def updateGUI(self):
        """Updates the Calibration User Interface depending on the current state of
        data entered into the viewer. If Modelled and Observed data is available,
        program will plot the results. If at least one of the Performance criteria
        has been selected, the model calculate this as well.
        """
        #Display Results as a text report
            #1.1 General Reporting Stuff, data stats


            #1.2 Goodness of Fit Criterion



        #Plot Data
            #1a  - Plot scatter if based on block-by-block



            #1b - Plot Histogram if only a single value




        pass

    def exportCalibrationResults(self):
        """Writes calibration results to an output report file that can be used to
        make plots in Excel or other programs"""
        pass

