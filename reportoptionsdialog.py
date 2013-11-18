# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reportoptionsdialog.ui'
#
# Created: Mon Nov 18 10:30:52 2013
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_ReportOptionsDialog(object):
    def setupUi(self, ReportOptionsDialog):
        ReportOptionsDialog.setObjectName(_fromUtf8("ReportOptionsDialog"))
        ReportOptionsDialog.resize(480, 482)
        ReportOptionsDialog.setWindowTitle(QtGui.QApplication.translate("ReportOptionsDialog", "Preferences", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalLayout = QtGui.QVBoxLayout(ReportOptionsDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.title_widget = QtGui.QWidget(ReportOptionsDialog)
        self.title_widget.setMinimumSize(QtCore.QSize(0, 50))
        self.title_widget.setMaximumSize(QtCore.QSize(16777215, 50))
        self.title_widget.setObjectName(_fromUtf8("title_widget"))
        self.header_img = QtGui.QLabel(self.title_widget)
        self.header_img.setGeometry(QtCore.QRect(-5, 5, 50, 50))
        self.header_img.setMinimumSize(QtCore.QSize(50, 50))
        self.header_img.setMaximumSize(QtCore.QSize(50, 50))
        self.header_img.setText(_fromUtf8(""))
        self.header_img.setPixmap(QtGui.QPixmap(_fromUtf8(":/images/custom-reports-icon.png")))
        self.header_img.setObjectName(_fromUtf8("header_img"))
        self.dbtitle = QtGui.QLabel(self.title_widget)
        self.dbtitle.setGeometry(QtCore.QRect(50, 10, 271, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.dbtitle.setFont(font)
        self.dbtitle.setText(QtGui.QApplication.translate("ReportOptionsDialog", "Reporting Options", None, QtGui.QApplication.UnicodeUTF8))
        self.dbtitle.setObjectName(_fromUtf8("dbtitle"))
        self.dbsubtitle = QtGui.QLabel(self.title_widget)
        self.dbsubtitle.setGeometry(QtCore.QRect(50, 30, 321, 16))
        self.dbsubtitle.setText(QtGui.QApplication.translate("ReportOptionsDialog", "Configure how UrbanBEATS should report results", None, QtGui.QApplication.UnicodeUTF8))
        self.dbsubtitle.setObjectName(_fromUtf8("dbsubtitle"))
        self.verticalLayout.addWidget(self.title_widget)
        self.main_options_widget = QtGui.QWidget(ReportOptionsDialog)
        self.main_options_widget.setObjectName(_fromUtf8("main_options_widget"))
        self.reporttype_title = QtGui.QLabel(self.main_options_widget)
        self.reporttype_title.setGeometry(QtCore.QRect(20, 10, 181, 16))
        self.reporttype_title.setText(QtGui.QApplication.translate("ReportOptionsDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Type of Report</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.reporttype_title.setObjectName(_fromUtf8("reporttype_title"))
        self.nopref_lbl_2 = QtGui.QLabel(self.main_options_widget)
        self.nopref_lbl_2.setGeometry(QtCore.QRect(160, 190, 181, 16))
        self.nopref_lbl_2.setText(_fromUtf8(""))
        self.nopref_lbl_2.setTextFormat(QtCore.Qt.AutoText)
        self.nopref_lbl_2.setPixmap(QtGui.QPixmap(_fromUtf8(":/guitoolbaricons/custom-reports-icon.png")))
        self.nopref_lbl_2.setObjectName(_fromUtf8("nopref_lbl_2"))
        self.sectionsincl_title = QtGui.QLabel(self.main_options_widget)
        self.sectionsincl_title.setGeometry(QtCore.QRect(20, 100, 181, 16))
        self.sectionsincl_title.setText(QtGui.QApplication.translate("ReportOptionsDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Select Sections to Include:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.sectionsincl_title.setObjectName(_fromUtf8("sectionsincl_title"))
        self.radioHTML = QtGui.QRadioButton(self.main_options_widget)
        self.radioHTML.setGeometry(QtCore.QRect(50, 35, 82, 17))
        self.radioHTML.setText(QtGui.QApplication.translate("ReportOptionsDialog", "HTML Report", None, QtGui.QApplication.UnicodeUTF8))
        self.radioHTML.setObjectName(_fromUtf8("radioHTML"))
        self.radioPlainText = QtGui.QRadioButton(self.main_options_widget)
        self.radioPlainText.setGeometry(QtCore.QRect(200, 35, 131, 17))
        self.radioPlainText.setText(QtGui.QApplication.translate("ReportOptionsDialog", "Plain Text Report", None, QtGui.QApplication.UnicodeUTF8))
        self.radioPlainText.setObjectName(_fromUtf8("radioPlainText"))
        self.filename_lbl = QtGui.QLabel(self.main_options_widget)
        self.filename_lbl.setGeometry(QtCore.QRect(40, 67, 181, 16))
        self.filename_lbl.setText(QtGui.QApplication.translate("ReportOptionsDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Enter Custom Filename:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.filename_lbl.setObjectName(_fromUtf8("filename_lbl"))
        self.filename_box = QtGui.QLineEdit(self.main_options_widget)
        self.filename_box.setGeometry(QtCore.QRect(160, 65, 251, 20))
        self.filename_box.setObjectName(_fromUtf8("filename_box"))
        self.checkProjectDetails = QtGui.QCheckBox(self.main_options_widget)
        self.checkProjectDetails.setGeometry(QtCore.QRect(50, 125, 111, 17))
        self.checkProjectDetails.setText(QtGui.QApplication.translate("ReportOptionsDialog", "Project Details", None, QtGui.QApplication.UnicodeUTF8))
        self.checkProjectDetails.setObjectName(_fromUtf8("checkProjectDetails"))
        self.checkSetupDetails = QtGui.QCheckBox(self.main_options_widget)
        self.checkSetupDetails.setGeometry(QtCore.QRect(50, 150, 141, 17))
        self.checkSetupDetails.setText(QtGui.QApplication.translate("ReportOptionsDialog", "Model Setup Details", None, QtGui.QApplication.UnicodeUTF8))
        self.checkSetupDetails.setObjectName(_fromUtf8("checkSetupDetails"))
        self.checkSpatialData = QtGui.QCheckBox(self.main_options_widget)
        self.checkSpatialData.setGeometry(QtCore.QRect(50, 200, 141, 17))
        self.checkSpatialData.setText(QtGui.QApplication.translate("ReportOptionsDialog", "Output Spatial Data", None, QtGui.QApplication.UnicodeUTF8))
        self.checkSpatialData.setObjectName(_fromUtf8("checkSpatialData"))
        self.checkWaterPlan = QtGui.QCheckBox(self.main_options_widget)
        self.checkWaterPlan.setGeometry(QtCore.QRect(50, 225, 191, 17))
        self.checkWaterPlan.setText(QtGui.QApplication.translate("ReportOptionsDialog", "Output Water Management Plan", None, QtGui.QApplication.UnicodeUTF8))
        self.checkWaterPlan.setObjectName(_fromUtf8("checkWaterPlan"))
        self.checkWaterAlts = QtGui.QCheckBox(self.main_options_widget)
        self.checkWaterAlts.setGeometry(QtCore.QRect(250, 200, 191, 17))
        self.checkWaterAlts.setText(QtGui.QApplication.translate("ReportOptionsDialog", "Details of Alternative Plans", None, QtGui.QApplication.UnicodeUTF8))
        self.checkWaterAlts.setObjectName(_fromUtf8("checkWaterAlts"))
        self.checkPerformance = QtGui.QCheckBox(self.main_options_widget)
        self.checkPerformance.setGeometry(QtCore.QRect(250, 225, 191, 17))
        self.checkPerformance.setText(QtGui.QApplication.translate("ReportOptionsDialog", "System Performance", None, QtGui.QApplication.UnicodeUTF8))
        self.checkPerformance.setObjectName(_fromUtf8("checkPerformance"))
        self.checkSpatialStats = QtGui.QCheckBox(self.main_options_widget)
        self.checkSpatialStats.setGeometry(QtCore.QRect(250, 175, 191, 17))
        self.checkSpatialStats.setText(QtGui.QApplication.translate("ReportOptionsDialog", "Statistics on Spatial Data", None, QtGui.QApplication.UnicodeUTF8))
        self.checkSpatialStats.setObjectName(_fromUtf8("checkSpatialStats"))
        self.checkDataDetails = QtGui.QCheckBox(self.main_options_widget)
        self.checkDataDetails.setGeometry(QtCore.QRect(50, 175, 141, 17))
        self.checkDataDetails.setText(QtGui.QApplication.translate("ReportOptionsDialog", "Input Data Details", None, QtGui.QApplication.UnicodeUTF8))
        self.checkDataDetails.setObjectName(_fromUtf8("checkDataDetails"))
        self.checkImplement = QtGui.QCheckBox(self.main_options_widget)
        self.checkImplement.setGeometry(QtCore.QRect(50, 250, 191, 17))
        self.checkImplement.setText(QtGui.QApplication.translate("ReportOptionsDialog", "Plan Implementation Details", None, QtGui.QApplication.UnicodeUTF8))
        self.checkImplement.setObjectName(_fromUtf8("checkImplement"))
        self.additionalreport_title = QtGui.QLabel(self.main_options_widget)
        self.additionalreport_title.setGeometry(QtCore.QRect(20, 280, 181, 16))
        self.additionalreport_title.setText(QtGui.QApplication.translate("ReportOptionsDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Additional Outputs:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.additionalreport_title.setObjectName(_fromUtf8("additionalreport_title"))
        self.exportSimLog = QtGui.QCheckBox(self.main_options_widget)
        self.exportSimLog.setGeometry(QtCore.QRect(50, 305, 151, 17))
        self.exportSimLog.setText(QtGui.QApplication.translate("ReportOptionsDialog", "Export Simulation Log", None, QtGui.QApplication.UnicodeUTF8))
        self.exportSimLog.setObjectName(_fromUtf8("exportSimLog"))
        self.exportBlocksCSV = QtGui.QCheckBox(self.main_options_widget)
        self.exportBlocksCSV.setGeometry(QtCore.QRect(50, 330, 261, 17))
        self.exportBlocksCSV.setText(QtGui.QApplication.translate("ReportOptionsDialog", "Export Blocks Attributes Table", None, QtGui.QApplication.UnicodeUTF8))
        self.exportBlocksCSV.setObjectName(_fromUtf8("exportBlocksCSV"))
        self.verticalLayout.addWidget(self.main_options_widget)
        self.widget_4 = QtGui.QWidget(ReportOptionsDialog)
        self.widget_4.setMinimumSize(QtCore.QSize(0, 38))
        self.widget_4.setMaximumSize(QtCore.QSize(16777215, 38))
        self.widget_4.setObjectName(_fromUtf8("widget_4"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.remarks = QtGui.QLabel(self.widget_4)
        self.remarks.setText(QtGui.QApplication.translate("ReportOptionsDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-style:italic;\">UrbanBEATS v1.0 - (C) 2013 Peter M. Bach</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.remarks.setObjectName(_fromUtf8("remarks"))
        self.horizontalLayout_2.addWidget(self.remarks)
        self.buttonBox = QtGui.QDialogButtonBox(self.widget_4)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.horizontalLayout_2.addWidget(self.buttonBox)
        self.verticalLayout.addWidget(self.widget_4)

        self.retranslateUi(ReportOptionsDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), ReportOptionsDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), ReportOptionsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ReportOptionsDialog)

    def retranslateUi(self, ReportOptionsDialog):
        pass

import guitoolbaricons_rc
import guitoolbaricons_rc
import guitoolbaricons_rc
import dialogimg_rc
import guitoolbaricons_rc
