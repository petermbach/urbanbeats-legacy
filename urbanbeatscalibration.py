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

#Still to Do:
    #- Future: Option for customising excel .csv file based on headers e.g. if calibration data all contained in one file
    #  which column should be used?
    #- Future: more plotting Options for data



import os
from PyQt4 import QtCore, QtGui
from urbanbeatscalibrationgui import Ui_CalibrationGUI_Dialog
import urbanbeatscalibrationscripts as ubcal
import ubhighcharts

class CalibrationGUILaunch(QtGui.QDialog):
    def __init__(self, activesim, tabindex, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_CalibrationGUI_Dialog()
        self.ui.setupUi(self)
        self.activesim = activesim
        self.ubeatsdir = activesim.getGlobalOptionsRoot()       #Current directory of the file
        self.calibrationhistory = self.activesim.getCalibrationHistory()
        self.tabindex = tabindex
        self.activeCalibrationData = []
        self.activeCalibrationValue = None
        self.modelled_data = None

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

        QtCore.QObject.connect(self.ui.set_eval_nash, QtCore.SIGNAL("clicked()"), self.updateGUI)
        QtCore.QObject.connect(self.ui.set_eval_rmse, QtCore.SIGNAL("clicked()"), self.updateGUI)
        QtCore.QObject.connect(self.ui.set_eval_error, QtCore.SIGNAL("clicked()"), self.updateGUI)

        QtCore.QObject.connect(self.ui.set_totvalue_box, QtCore.SIGNAL("editingFinished()"), self.updateSingleValue)
        QtCore.QObject.connect(self.ui.plottype_combo, QtCore.SIGNAL("currentIndexChanged(int)"), self.updateGUI)


        #Load calibration data
        QtCore.QObject.connect(self.ui.set_data_load, QtCore.SIGNAL("clicked()"), self.openFileDialog_calibdata)
        QtCore.QObject.connect(self.ui.set_data_reset, QtCore.SIGNAL("clicked()"), self.resetCalibrationData)
        QtCore.QObject.connect(self.ui.set_gen_button, QtCore.SIGNAL("clicked()"), self.generate_calibdata)

        #Save state of calibration data
        QtCore.QObject.connect(self.ui.closeButton, QtCore.SIGNAL("clicked()"), self.saveHistory)
        QtCore.QObject.connect(self.ui.out_export, QtCore.SIGNAL("clicked()"), self.exportCalibrationResults)

        #Definition of GUI States: used in UpdateGUI to determine what to do.
        self.moddata = False
        self.obsdata = False
        self.criterionselect = False


    def updateSingleValue(self):
        self.calibrationhistory[self.getCalibrationKeyword()] = self.ui.set_totvalue_box.text()
        self.obsdata = 1
        self.updateGUI()
        return True

    def resetCalibrationData(self):
        #Reset Table
        self.calibrationhistory[self.getCalibrationKeyword()] = None
        self.ui.set_data_table.setRowCount(0)
        self.obsdata = False
        self.updateGUI()
        return True

    def getCalibrationKeyword(self):
        keys = self.calibrationhistory.keys()
        kwindex = self.ui.set_param_combo.currentIndex() + int(self.ui.set_typetotal_radio.isChecked())*5 - 1
        return keys[kwindex]

    def generate_calibdata(self):
        allassetdata = self.activesim.retrieveAssetsFromCollection("pc", self.tabindex)
        assetdata = self.activesim.getAssetsWithIdentifier("BlockID", assetcol=allassetdata)

        if self.ui.set_gen_combo.currentIndex() == 0:
            #Melbourne Water guide
            calibdata = self.generateImpAreaFromMWGuide(assetdata)
            self.updateCalibrationDataTable(calibdata)
            self.calibrationhistory[self.getCalibrationKeyword()] = None    #Set to None because this data changes every time
            self.obsdata = True
        else:
            pass

        self.updateGUI()


    def generateImpAreaFromMWGuide(self, assetdata):
        map_attr = self.activesim.getAssetWithName("MapAttributes")
        block_size = map_attr.getAttribute("BlockSize")
        #print "Block Size", block_size

        nonreslucmatrix = ["COM", "LI", "HI", "ORC", "CIV", "SVU", "TR", "RD", "PG", "REF", "UND", "NA"]
        dataset = {}
        rawdata = []
        f = open(self.ubeatsdir+"/ancillary/mw_mmg.cfg", 'r')
        for lines in f:
            rawdata.append(lines.split(','))
        f.close()

        for lines in range(len(rawdata)):
            dataset[str(rawdata[lines][0])] = rawdata[lines][1:]
        #print "Calibration MW", dataset

        #Calculate impervious area for non-residential land uses
        calibdata = [[],[]]
        curindex = 0
        for i in range(len(assetdata)):
            asset = assetdata[i]
            if asset.getAttribute("Status") == 0:
                continue

            calibdata[0].append(int(asset.getAttribute("BlockID")))
            print "BlockID", calibdata[0][curindex]
            calibdata[1].append(0)

            #Non-Residential Land uses
            for luc in nonreslucmatrix:
                calibdata[1][curindex] += asset.getAttribute("pLU_"+luc) * float(dataset[luc][2])

            #Residential
            lotarea = float(asset.getAttribute("ResLotArea"))
            if lotarea == 0:
                pass
            if lotarea < 350.0:
                calibdata[1][curindex] += asset.getAttribute("pLU_RES") * float(dataset["RES-350"][2])
            elif lotarea < 500.0:
                calibdata[1][curindex] += asset.getAttribute("pLU_RES") * float(dataset["RES-500"][2])
            elif lotarea < 800.0:
                calibdata[1][curindex] += asset.getAttribute("pLU_RES") * float(dataset["RES-800"][2])
            else:
                calibdata[1][curindex] += asset.getAttribute("pLU_RES") * float(dataset["RES-4000"][2])

            if asset.getAttribute("HDRFlats") != 0:
                calibdata[1][curindex] += asset.getAttribute("pLU_RES") * float(dataset["HDR"][2])

            #HDR
            calibdata[1][curindex] = calibdata[1][curindex] * asset.getAttribute("Active") * float(block_size) * float(block_size)
            curindex += 1
        return calibdata


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
            mod = self.retrieveModelData(["ResAllots"])
        elif self.ui.set_param_combo.currentIndex() == 3:       #Res Dwelling Count
            mod = self.retrieveModelData(["ResHouses", "HDRFlats"])
        elif self.ui.set_param_combo.currentIndex() == 4:       #Res Roof Area
            mod = self.retrieveModelData(["ResRoof", "HDRRoofA"])
        elif self.ui.set_param_combo.currentIndex() == 5:       #Total Water Demand
            mod = self.retrieveModelData(["Blk_WD"])

        if self.ui.set_typetotal_radio.isChecked():
            mod = sum(mod[1])

        self.modelled_data = mod
        self.moddata = True

        #Update calibration data table
        if self.calibrationhistory[self.getCalibrationKeyword()] == None:
            self.ui.set_totvalue_box.clear()
            self.ui.set_data_table.setRowCount(0)
            self.obsdata = False
            return True

        if self.ui.set_typeblock_radio.isChecked():
            calibdata = ubcal.readCalibrationData(str(self.calibrationhistory[self.getCalibrationKeyword()]))
            self.updateCalibrationDataTable(calibdata)
            self.obsdata = True
        else:
            self.ui.set_totvalue_box.setText(str(self.calibrationhistory[self.getCalibrationKeyword()]))
            self.obsdata = True

        self.updateGUI()


    def updateCalibrationDataTable(self, calibdata):
        self.ui.set_data_table.setRowCount(0)

        for i in range(len(calibdata[0])):
            #Update Table in GUI
            rowPosition = self.ui.set_data_table.rowCount()
            self.ui.set_data_table.insertRow(rowPosition)
            blocknum = calibdata[0][i]
            datavalue = calibdata[1][i]
            self.ui.set_data_table.setItem(rowPosition, 0, QtGui.QTableWidgetItem(str(blocknum)))
            self.ui.set_data_table.setItem(rowPosition, 1, QtGui.QTableWidgetItem(str(datavalue)))
        self.obsdata = True


    def retrieveModelData(self, attributes):
        """Retrieve data from the current model run"""
        allassetdata = self.activesim.retrieveAssetsFromCollection("pc", self.tabindex)
        assetdata = self.activesim.getAssetsWithIdentifier("BlockID", assetcol=allassetdata)
        mod = [[],[]]
        curindex = 0
        for i in range(len(assetdata)):
            if assetdata[i].getAttribute("Status") == 0:
                continue
            mod[0].append(int(assetdata[i].getAttribute("BlockID")))
            mod[1].append(0)
            for att in attributes:
                if att == "ResRoof":
                    mod[1][curindex] += float(assetdata[i].getAttribute(att)*assetdata[i].getAttribute("ResHouses"))
                else:
                    mod[1][curindex] += float(assetdata[i].getAttribute(att))
            curindex += 1
        return mod


    def openFileDialog_calibdata(self):
        fname = QtGui.QFileDialog.getOpenFileName(self, "Choose Calibration Data File...", os.curdir, "Calibration Data (*.csv *.txt)")
        if fname:
            self.calibrationhistory[self.getCalibrationKeyword()] = fname
            calibdata = ubcal.readCalibrationData(fname)
            self.updateCalibrationDataTable(calibdata)

        self.updateGUI()
        return True


    def readTableData(self):
        "Grabs all the data in the observed data table when requested"
        blockColl = {}
        for i in range(self.ui.set_data_table.rowCount()):
            print self.ui.set_data_table.item(i, 0).text(), self.ui.set_data_table.item(i, 1).text()
            blockColl[int(self.ui.set_data_table.item(i, 0).text())] = float(self.ui.set_data_table.item(i, 1).text())
        return blockColl


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
        #Plot Data
        if self.obsdata and self.moddata:
            if self.ui.set_typeblock_radio.isChecked():
                observed = self.readTableData()
                modelled = self.modelled_data

                observedvalues = []
                modelledvalues = []
                for i in observed.keys():
                    if i not in modelled[0]:
                        continue
                    observedvalues.append(round(float(observed[i]),2))
                    modelledvalues.append(round(float(modelled[1][modelled[0].index(i)]),2))

                if self.ui.plottype_combo.currentIndex() == 0:
                    #PLOT SCATTER MODELLED VS OBSERVED
                    self.plotCalibrationScatter(observedvalues, modelledvalues)
                elif self.ui.plottype_combo.currentIndex() == 1:
                    #PLOT RESIDUALS (Obs - Mod)
                    pass
                elif self.ui.plottype_combo.currentIndex() == 2:
                    #PLOT ERROR AS HISTOGRAM
                    pass

            else:
                observed = float(self.ui.set_totvalue_box.text())
                modelled = self.modelled_data

                if self.ui.plottype_combo.currentIndex() == 0:
                    #PLOT HISTOGRAM MODELLED VS OBSERVED
                    self.plotCalibrationHistogram(observed, modelled)
                elif self.ui.plottype_combo.currentIndex() == 1:
                    #PLOT RESIDUALS (Obs - Mod)
                    pass
                elif self.ui.plottype_combo.currentIndex() == 2:
                    #PLOT ERROR AS HISTOGRAM
                    pass

        else:
            self.ui.calibrationView.setHtml("")


        #Update Results Browser
        if self.moddata and self.obsdata:
            summaryline = ""
            summaryline += "Summary of Calibration: \n"
            summaryline += "---------------------------\n"

            if self.ui.set_typeblock_radio.isChecked():
                #1.1 General Reporting Stuff, data stats
                summaryline += "Observed Data Points: "+str(len(observedvalues))+"\n"
                summaryline += "Modelled Data Points: "+str(len(modelled[0]))+"\n"
                summaryline += "Data Points not compared: "+str(abs(len(modelled[0])-len(observedvalues)))+"\n\n"

                #1.2 Goodness of Fit Criterion
                if self.ui.set_eval_nash.isChecked():
                    nashE = ubcal.calculateNashE(observedvalues, modelledvalues)
                    summaryline += "Nash-Sutcliffe E = "+str(round(nashE,2))+"\n"
                else:
                    summaryline += "Nash-Sufcliffe E = (not calculated) \n"
                if self.ui.set_eval_rmse.isChecked():
                    rmse = ubcal.calculateRMSE(observedvalues, modelledvalues)
                    summaryline += "RMSE = "+str(round(rmse,2))+"\n"
                else:
                    summaryline += "RMSE = (not calculated) \n"
                if self.ui.set_eval_error.isChecked():
                    avgerr, minerr, maxerr, e10, e30, e50 = ubcal.calculateRelativeError(observedvalues, modelledvalues)
                    summaryline += "Average Relative Error = "+str(round(avgerr,1))+"%\n"
                    summaryline += "Min. Relative Error = "+str(round(minerr,1))+"%\n"
                    summaryline += "Max Relative Error = "+str(round(maxerr,1))+"%\n\n"
                    summaryline += "Data Points with < 10% Error = "+str(round(e10,0))+"\n"
                    summaryline += "Data Points with < 30% Error = "+str(round(e30,0))+"\n"
                    summaryline += "Data Points with < 50% Error = "+str(round(e50,0))+"\n"
                else:
                    summaryline += "Relative Error = (not calculated) \n"
            else:
                summaryline += "Observed Data: Using Total Value \n"
                summaryline += "Modelled Data: Using Total Value \n\n"

                if self.ui.set_eval_error.isChecked():
                    if observed == 0:
                        err = 100.0
                    else:
                        err = (observed - modelled)/observed * 100.0
                    summaryline += "Relative Error = "+str(abs(round(err,1)))+"%\n"
                else:
                    summaryline += "Relative Error = (not calculated)"

            self.ui.out_box.setPlainText(summaryline)

        else:
            self.ui.out_box.clear()
            self.ui.out_box.setPlainText("Results:\n")

        return True


    def plotCalibrationResidualHistogram(self, obs, mod):
        pass

    def plotErrorHistogram(self, obs, mod):
        pass



    def plotCalibrationHistogram(self, obs, mod):
        title = str(self.ui.set_param_combo.currentText()) + " "+self.ui.set_totvalue_units.text()[7:]
        categories = [""]
        xlabel = ""
        units = self.ui.set_totvalue_units.text()[7:]
        labelformat = [-45, 'right', 13, 'Verdana, sans-serif']
        data = {"Observed": [obs],
                "Modelled": [mod]}
        self.htmlscript = ubhighcharts.column_basic(self.ubeatsdir, title, categories, xlabel, labelformat,  units, data)
        self.ui.calibrationView.setHtml(self.htmlscript)

        print self.htmlscript
        return True


    def plotCalibrationScatter(self, obs, mod):
        """Plots a scatter plot showing the correlation of two of the selected attributes at the Block Level
        :return:
        """
        x_name = "Observed Data"
        y_name = "Modelled Data"
        title = str(self.ui.set_param_combo.currentText()) + " " +self.ui.set_totvalue_units.text()[7:]

        x_values = obs
        y_values = mod
        datadict = {x_name+" vs. "+y_name : []}
        for i in range(len(x_values)):
            datadict[x_name+" vs. "+y_name].append([x_values[i], y_values[i]])

        self.htmlscript = ubhighcharts.scatter_plot(self.ubeatsdir, title, x_name, y_name, 3, "", "", datadict)
        self.ui.calibrationView.setHtml(self.htmlscript)


    def exportCalibrationResults(self):
        """Writes calibration results to an output report file that can be used to
        make plots in Excel or other programs"""

        if self.moddata or self.obsdata:
            f = open("CalibrationResults.txt", 'w')
        else:
            QtGui.QMessageBox.warning(self, "No data to export", "There is currently no data to export!", QtGui.QMessageBox.Ok)
            return True

        #Export the Results Box
        f.write(self.ui.out_box.toPlainText())

        #Exports the Observed and Modelled Data if Available
        f.write("\n\n")
        f.write("BlockID, Observed, Modelled \n")
        if self.obsdata and self.moddata:
            if self.ui.set_typeblock_radio.isChecked():
                observed = self.readTableData()
                modelled = self.modelled_data

                for i in observed.keys():
                    if i not in modelled[0]:
                        continue
                    f.write(str(i)+","+str(round(float(observed[i]),2))+","+str(round(float(modelled[1][modelled[0].index(i)]),2))+"\n")

        #Export the Parameter Set Data if Requested
        #Urban Form only, unless Water Demands

        f.close()
        QtGui.QMessageBox.warning(self, "Export Complete", "Results for current calibration successfully \n exported to project path!", QtGui.QMessageBox.Ok)

