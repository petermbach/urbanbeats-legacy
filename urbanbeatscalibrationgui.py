# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'urbanbeatscalibrationgui.ui'
#
# Created: Thu Mar 10 11:49:34 2016
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_CalibrationGUI_Dialog(object):
    def setupUi(self, CalibrationGUI_Dialog):
        CalibrationGUI_Dialog.setObjectName(_fromUtf8("CalibrationGUI_Dialog"))
        CalibrationGUI_Dialog.resize(1095, 686)
        CalibrationGUI_Dialog.setMinimumSize(QtCore.QSize(1024, 680))
        self.verticalLayout = QtGui.QVBoxLayout(CalibrationGUI_Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.title_widget = QtGui.QWidget(CalibrationGUI_Dialog)
        self.title_widget.setMinimumSize(QtCore.QSize(0, 50))
        self.title_widget.setMaximumSize(QtCore.QSize(16777215, 50))
        self.title_widget.setObjectName(_fromUtf8("title_widget"))
        self.line = QtGui.QFrame(self.title_widget)
        self.line.setGeometry(QtCore.QRect(50, 40, 1031, 20))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setMinimumSize(QtCore.QSize(573, 0))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.windowtitle = QtGui.QLabel(self.title_widget)
        self.windowtitle.setGeometry(QtCore.QRect(50, 5, 241, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.windowtitle.setFont(font)
        self.windowtitle.setObjectName(_fromUtf8("windowtitle"))
        self.windowLogo = QtGui.QLabel(self.title_widget)
        self.windowLogo.setGeometry(QtCore.QRect(0, 0, 50, 50))
        self.windowLogo.setMaximumSize(QtCore.QSize(50, 50))
        self.windowLogo.setText(_fromUtf8(""))
        self.windowLogo.setPixmap(QtGui.QPixmap(_fromUtf8(":/guitoolbaricons/outputs.png")))
        self.windowLogo.setObjectName(_fromUtf8("windowLogo"))
        self.windowsubtitle = QtGui.QLabel(self.title_widget)
        self.windowsubtitle.setGeometry(QtCore.QRect(50, 25, 561, 16))
        self.windowsubtitle.setObjectName(_fromUtf8("windowsubtitle"))
        self.verticalLayout.addWidget(self.title_widget)
        self.main_widget = QtGui.QWidget(CalibrationGUI_Dialog)
        self.main_widget.setObjectName(_fromUtf8("main_widget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.main_widget)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.calibrationSettings = QtGui.QWidget(self.main_widget)
        self.calibrationSettings.setMinimumSize(QtCore.QSize(250, 0))
        self.calibrationSettings.setMaximumSize(QtCore.QSize(200, 16777215))
        self.calibrationSettings.setObjectName(_fromUtf8("calibrationSettings"))
        self.set_param_combo = QtGui.QComboBox(self.calibrationSettings)
        self.set_param_combo.setGeometry(QtCore.QRect(10, 50, 231, 22))
        self.set_param_combo.setObjectName(_fromUtf8("set_param_combo"))
        self.set_param_combo.addItem(_fromUtf8(""))
        self.set_param_combo.addItem(_fromUtf8(""))
        self.set_param_combo.addItem(_fromUtf8(""))
        self.set_param_combo.addItem(_fromUtf8(""))
        self.set_param_combo.addItem(_fromUtf8(""))
        self.set_param_combo.addItem(_fromUtf8(""))
        self.set_param_lbl = QtGui.QLabel(self.calibrationSettings)
        self.set_param_lbl.setGeometry(QtCore.QRect(10, 30, 191, 16))
        self.set_param_lbl.setObjectName(_fromUtf8("set_param_lbl"))
        self.set_totvalue_box = QtGui.QLineEdit(self.calibrationSettings)
        self.set_totvalue_box.setGeometry(QtCore.QRect(20, 165, 121, 20))
        self.set_totvalue_box.setObjectName(_fromUtf8("set_totvalue_box"))
        self.set_data_table = QtGui.QTableWidget(self.calibrationSettings)
        self.set_data_table.setGeometry(QtCore.QRect(10, 220, 231, 141))
        self.set_data_table.setGridStyle(QtCore.Qt.SolidLine)
        self.set_data_table.setObjectName(_fromUtf8("set_data_table"))
        self.set_data_table.setColumnCount(2)
        self.set_data_table.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.set_data_table.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.set_data_table.setHorizontalHeaderItem(1, item)
        self.set_data_table.horizontalHeader().setVisible(True)
        self.set_data_table.verticalHeader().setVisible(False)
        self.set_type_lbl = QtGui.QLabel(self.calibrationSettings)
        self.set_type_lbl.setGeometry(QtCore.QRect(10, 85, 191, 16))
        self.set_type_lbl.setObjectName(_fromUtf8("set_type_lbl"))
        self.set_totvalue_units = QtGui.QLabel(self.calibrationSettings)
        self.set_totvalue_units.setGeometry(QtCore.QRect(150, 165, 91, 20))
        self.set_totvalue_units.setObjectName(_fromUtf8("set_totvalue_units"))
        self.set_typetotal_radio = QtGui.QRadioButton(self.calibrationSettings)
        self.set_typetotal_radio.setGeometry(QtCore.QRect(30, 110, 91, 17))
        self.set_typetotal_radio.setObjectName(_fromUtf8("set_typetotal_radio"))
        self.set_totvalue_lbl = QtGui.QLabel(self.calibrationSettings)
        self.set_totvalue_lbl.setGeometry(QtCore.QRect(10, 140, 191, 16))
        self.set_totvalue_lbl.setObjectName(_fromUtf8("set_totvalue_lbl"))
        self.set_typeblock_radio = QtGui.QRadioButton(self.calibrationSettings)
        self.set_typeblock_radio.setGeometry(QtCore.QRect(130, 110, 91, 17))
        self.set_typeblock_radio.setObjectName(_fromUtf8("set_typeblock_radio"))
        self.set_data_lbl = QtGui.QLabel(self.calibrationSettings)
        self.set_data_lbl.setGeometry(QtCore.QRect(10, 195, 191, 16))
        self.set_data_lbl.setObjectName(_fromUtf8("set_data_lbl"))
        self.set_data_reset = QtGui.QPushButton(self.calibrationSettings)
        self.set_data_reset.setGeometry(QtCore.QRect(129, 370, 111, 23))
        self.set_data_reset.setObjectName(_fromUtf8("set_data_reset"))
        self.set_data_load = QtGui.QPushButton(self.calibrationSettings)
        self.set_data_load.setGeometry(QtCore.QRect(10, 370, 111, 23))
        self.set_data_load.setObjectName(_fromUtf8("set_data_load"))
        self.set_eval_lbl = QtGui.QLabel(self.calibrationSettings)
        self.set_eval_lbl.setGeometry(QtCore.QRect(10, 460, 191, 16))
        self.set_eval_lbl.setObjectName(_fromUtf8("set_eval_lbl"))
        self.set_eval_nash = QtGui.QCheckBox(self.calibrationSettings)
        self.set_eval_nash.setGeometry(QtCore.QRect(20, 485, 161, 17))
        self.set_eval_nash.setObjectName(_fromUtf8("set_eval_nash"))
        self.set_eval_rmse = QtGui.QCheckBox(self.calibrationSettings)
        self.set_eval_rmse.setGeometry(QtCore.QRect(20, 505, 161, 17))
        self.set_eval_rmse.setObjectName(_fromUtf8("set_eval_rmse"))
        self.set_eval_error = QtGui.QCheckBox(self.calibrationSettings)
        self.set_eval_error.setGeometry(QtCore.QRect(20, 525, 161, 17))
        self.set_eval_error.setObjectName(_fromUtf8("set_eval_error"))
        self.set_gen_button = QtGui.QPushButton(self.calibrationSettings)
        self.set_gen_button.setGeometry(QtCore.QRect(170, 425, 71, 23))
        self.set_gen_button.setObjectName(_fromUtf8("set_gen_button"))
        self.set_gen_lbl = QtGui.QLabel(self.calibrationSettings)
        self.set_gen_lbl.setGeometry(QtCore.QRect(10, 400, 191, 16))
        self.set_gen_lbl.setObjectName(_fromUtf8("set_gen_lbl"))
        self.set_gen_combo = QtGui.QComboBox(self.calibrationSettings)
        self.set_gen_combo.setGeometry(QtCore.QRect(10, 425, 151, 22))
        self.set_gen_combo.setObjectName(_fromUtf8("set_gen_combo"))
        self.set_gen_combo.addItem(_fromUtf8(""))
        self.calibset_title = QtGui.QLabel(self.calibrationSettings)
        self.calibset_title.setGeometry(QtCore.QRect(9, 9, 191, 16))
        self.calibset_title.setObjectName(_fromUtf8("calibset_title"))
        self.horizontalLayout_2.addWidget(self.calibrationSettings)
        self.calibrationResults = QtGui.QWidget(self.main_widget)
        self.calibrationResults.setMinimumSize(QtCore.QSize(250, 0))
        self.calibrationResults.setObjectName(_fromUtf8("calibrationResults"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.calibrationResults)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.caliboutput_title = QtGui.QLabel(self.calibrationResults)
        self.caliboutput_title.setObjectName(_fromUtf8("caliboutput_title"))
        self.verticalLayout_2.addWidget(self.caliboutput_title)
        self.out_box = QtGui.QPlainTextEdit(self.calibrationResults)
        self.out_box.setObjectName(_fromUtf8("out_box"))
        self.verticalLayout_2.addWidget(self.out_box)
        self.report_includeparams_check = QtGui.QCheckBox(self.calibrationResults)
        self.report_includeparams_check.setObjectName(_fromUtf8("report_includeparams_check"))
        self.verticalLayout_2.addWidget(self.report_includeparams_check)
        self.out_export = QtGui.QPushButton(self.calibrationResults)
        self.out_export.setObjectName(_fromUtf8("out_export"))
        self.verticalLayout_2.addWidget(self.out_export)
        self.horizontalLayout_2.addWidget(self.calibrationResults)
        self.calibrationView = QtWebKit.QWebView(self.main_widget)
        self.calibrationView.setMinimumSize(QtCore.QSize(550, 0))
        self.calibrationView.setMaximumSize(QtCore.QSize(500, 16777215))
        self.calibrationView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.calibrationView.setObjectName(_fromUtf8("calibrationView"))
        self.horizontalLayout_2.addWidget(self.calibrationView)
        self.verticalLayout.addWidget(self.main_widget)
        self.footer = QtGui.QWidget(CalibrationGUI_Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.footer.sizePolicy().hasHeightForWidth())
        self.footer.setSizePolicy(sizePolicy)
        self.footer.setMinimumSize(QtCore.QSize(0, 38))
        self.footer.setMaximumSize(QtCore.QSize(16777215, 38))
        self.footer.setObjectName(_fromUtf8("footer"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.footer)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.remarks = QtGui.QLabel(self.footer)
        self.remarks.setMinimumSize(QtCore.QSize(900, 0))
        self.remarks.setObjectName(_fromUtf8("remarks"))
        self.horizontalLayout.addWidget(self.remarks)
        self.closeButton = QtGui.QPushButton(self.footer)
        self.closeButton.setMinimumSize(QtCore.QSize(82, 20))
        self.closeButton.setMaximumSize(QtCore.QSize(82, 20))
        self.closeButton.setWhatsThis(_fromUtf8(""))
        self.closeButton.setObjectName(_fromUtf8("closeButton"))
        self.horizontalLayout.addWidget(self.closeButton)
        self.verticalLayout.addWidget(self.footer)

        self.retranslateUi(CalibrationGUI_Dialog)
        QtCore.QObject.connect(self.closeButton, QtCore.SIGNAL(_fromUtf8("clicked()")), CalibrationGUI_Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(CalibrationGUI_Dialog)

    def retranslateUi(self, CalibrationGUI_Dialog):
        CalibrationGUI_Dialog.setWindowTitle(_translate("CalibrationGUI_Dialog", "UrbanBEATS Results Explorer", None))
        self.windowtitle.setText(_translate("CalibrationGUI_Dialog", "Model Calibration Viewer", None))
        self.windowsubtitle.setText(_translate("CalibrationGUI_Dialog", "Load or generate a real and/or hypothetical data set to calibrate UrbanBEATS\' outputs against.", None))
        self.set_param_combo.setItemText(0, _translate("CalibrationGUI_Dialog", "<select parameter to calibrate>", None))
        self.set_param_combo.setItemText(1, _translate("CalibrationGUI_Dialog", "Impervious Area", None))
        self.set_param_combo.setItemText(2, _translate("CalibrationGUI_Dialog", "Residential Allotment Count", None))
        self.set_param_combo.setItemText(3, _translate("CalibrationGUI_Dialog", "Residential House Count", None))
        self.set_param_combo.setItemText(4, _translate("CalibrationGUI_Dialog", "Total Residential Roof Area", None))
        self.set_param_combo.setItemText(5, _translate("CalibrationGUI_Dialog", "Water Demand", None))
        self.set_param_lbl.setText(_translate("CalibrationGUI_Dialog", "Select Parameter to Calibrate:", None))
        self.set_data_table.setSortingEnabled(False)
        item = self.set_data_table.horizontalHeaderItem(0)
        item.setText(_translate("CalibrationGUI_Dialog", "BlockID", None))
        item = self.set_data_table.horizontalHeaderItem(1)
        item.setText(_translate("CalibrationGUI_Dialog", "Observed", None))
        self.set_type_lbl.setText(_translate("CalibrationGUI_Dialog", "Type of Calibration:", None))
        self.set_totvalue_units.setText(_translate("CalibrationGUI_Dialog", "units: [%]", None))
        self.set_typetotal_radio.setText(_translate("CalibrationGUI_Dialog", "Total Value", None))
        self.set_totvalue_lbl.setText(_translate("CalibrationGUI_Dialog", "Enter Total Value:", None))
        self.set_typeblock_radio.setText(_translate("CalibrationGUI_Dialog", "Block-by-block", None))
        self.set_data_lbl.setText(_translate("CalibrationGUI_Dialog", "...or Enter Calibration Data:", None))
        self.set_data_reset.setText(_translate("CalibrationGUI_Dialog", "Reset", None))
        self.set_data_load.setText(_translate("CalibrationGUI_Dialog", "Load...", None))
        self.set_eval_lbl.setText(_translate("CalibrationGUI_Dialog", "Select Evaluation Criteria:", None))
        self.set_eval_nash.setText(_translate("CalibrationGUI_Dialog", "Nash-Sutcliffe Coefficient", None))
        self.set_eval_rmse.setText(_translate("CalibrationGUI_Dialog", "Root Mean Squared Error", None))
        self.set_eval_error.setText(_translate("CalibrationGUI_Dialog", "Relative Error", None))
        self.set_gen_button.setText(_translate("CalibrationGUI_Dialog", "Generate", None))
        self.set_gen_lbl.setText(_translate("CalibrationGUI_Dialog", "...or Generate a Calibration Data Set:", None))
        self.set_gen_combo.setItemText(0, _translate("CalibrationGUI_Dialog", "MW MUSIC Guide", None))
        self.calibset_title.setText(_translate("CalibrationGUI_Dialog", "<html><head/><body><p><span style=\" font-weight:600; font-style:italic;\">Calibration Settings</span></p></body></html>", None))
        self.caliboutput_title.setText(_translate("CalibrationGUI_Dialog", "<html><head/><body><p><span style=\" font-weight:600; font-style:italic;\">Calibration Outputs</span></p></body></html>", None))
        self.out_box.setPlainText(_translate("CalibrationGUI_Dialog", "Results:", None))
        self.report_includeparams_check.setText(_translate("CalibrationGUI_Dialog", "Include Parameters in Report", None))
        self.out_export.setText(_translate("CalibrationGUI_Dialog", "Export Report...", None))
        self.remarks.setText(_translate("CalibrationGUI_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\">UrbanBEATS v1.0 - (C) 2016 Peter M. Bach </span></p></body></html>", None))
        self.closeButton.setText(_translate("CalibrationGUI_Dialog", "Close", None))

from PyQt4 import QtWebKit
import guitoolbaricons_rc