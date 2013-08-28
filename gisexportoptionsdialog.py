# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gisexportoptionsdialog.ui'
#
# Created: Wed Apr 03 16:34:45 2013
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_GISExportDialog(object):
    def setupUi(self, GISExportDialog):
        GISExportDialog.setObjectName(_fromUtf8("GISExportDialog"))
        GISExportDialog.resize(480, 350)
        GISExportDialog.setWindowTitle(QtGui.QApplication.translate("GISExportDialog", "Preferences", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalLayout = QtGui.QVBoxLayout(GISExportDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.title_widget = QtGui.QWidget(GISExportDialog)
        self.title_widget.setMinimumSize(QtCore.QSize(0, 50))
        self.title_widget.setMaximumSize(QtCore.QSize(16777215, 50))
        self.title_widget.setObjectName(_fromUtf8("title_widget"))
        self.dbtitle = QtGui.QLabel(self.title_widget)
        self.dbtitle.setGeometry(QtCore.QRect(60, 5, 291, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.dbtitle.setFont(font)
        self.dbtitle.setText(QtGui.QApplication.translate("GISExportDialog", "Spatial Data Export Options", None, QtGui.QApplication.UnicodeUTF8))
        self.dbtitle.setObjectName(_fromUtf8("dbtitle"))
        self.header_img = QtGui.QLabel(self.title_widget)
        self.header_img.setGeometry(QtCore.QRect(5, 0, 50, 50))
        self.header_img.setMinimumSize(QtCore.QSize(50, 50))
        self.header_img.setMaximumSize(QtCore.QSize(50, 50))
        self.header_img.setText(_fromUtf8(""))
        self.header_img.setPixmap(QtGui.QPixmap(_fromUtf8(":/images/Layers-icon-50px.png")))
        self.header_img.setObjectName(_fromUtf8("header_img"))
        self.dbsubtitle = QtGui.QLabel(self.title_widget)
        self.dbsubtitle.setGeometry(QtCore.QRect(60, 25, 281, 16))
        self.dbsubtitle.setText(QtGui.QApplication.translate("GISExportDialog", "Configure how UrbanBEATS should export spatial data", None, QtGui.QApplication.UnicodeUTF8))
        self.dbsubtitle.setObjectName(_fromUtf8("dbsubtitle"))
        self.verticalLayout.addWidget(self.title_widget)
        self.main_options_widget = QtGui.QWidget(GISExportDialog)
        self.main_options_widget.setObjectName(_fromUtf8("main_options_widget"))
        self.mapfilename_title = QtGui.QLabel(self.main_options_widget)
        self.mapfilename_title.setGeometry(QtCore.QRect(20, 10, 181, 16))
        self.mapfilename_title.setText(QtGui.QApplication.translate("GISExportDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Map Filenames</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.mapfilename_title.setObjectName(_fromUtf8("mapfilename_title"))
        self.nopref_lbl_2 = QtGui.QLabel(self.main_options_widget)
        self.nopref_lbl_2.setGeometry(QtCore.QRect(160, 190, 181, 16))
        self.nopref_lbl_2.setText(_fromUtf8(""))
        self.nopref_lbl_2.setTextFormat(QtCore.Qt.AutoText)
        self.nopref_lbl_2.setPixmap(QtGui.QPixmap(_fromUtf8(":/guitoolbaricons/custom-reports-icon.png")))
        self.nopref_lbl_2.setObjectName(_fromUtf8("nopref_lbl_2"))
        self.selectmaps_title = QtGui.QLabel(self.main_options_widget)
        self.selectmaps_title.setGeometry(QtCore.QRect(20, 70, 181, 16))
        self.selectmaps_title.setText(QtGui.QApplication.translate("GISExportDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Select Maps to Export:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.selectmaps_title.setObjectName(_fromUtf8("selectmaps_title"))
        self.mapfilename_lbl = QtGui.QLabel(self.main_options_widget)
        self.mapfilename_lbl.setGeometry(QtCore.QRect(40, 37, 181, 16))
        self.mapfilename_lbl.setText(QtGui.QApplication.translate("GISExportDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Enter Custom Filename:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.mapfilename_lbl.setObjectName(_fromUtf8("mapfilename_lbl"))
        self.filename_box = QtGui.QLineEdit(self.main_options_widget)
        self.filename_box.setGeometry(QtCore.QRect(160, 35, 251, 20))
        self.filename_box.setObjectName(_fromUtf8("filename_box"))
        self.mapBlocks = QtGui.QCheckBox(self.main_options_widget)
        self.mapBlocks.setGeometry(QtCore.QRect(50, 95, 121, 17))
        self.mapBlocks.setText(QtGui.QApplication.translate("GISExportDialog", "Building Blocks", None, QtGui.QApplication.UnicodeUTF8))
        self.mapBlocks.setObjectName(_fromUtf8("mapBlocks"))
        self.mapPatches = QtGui.QCheckBox(self.main_options_widget)
        self.mapPatches.setGeometry(QtCore.QRect(50, 120, 141, 17))
        self.mapPatches.setText(QtGui.QApplication.translate("GISExportDialog", "Patch Data", None, QtGui.QApplication.UnicodeUTF8))
        self.mapPatches.setObjectName(_fromUtf8("mapPatches"))
        self.mapWSUDplan = QtGui.QCheckBox(self.main_options_widget)
        self.mapWSUDplan.setGeometry(QtCore.QRect(160, 95, 141, 17))
        self.mapWSUDplan.setText(QtGui.QApplication.translate("GISExportDialog", "Planned WSUD", None, QtGui.QApplication.UnicodeUTF8))
        self.mapWSUDplan.setObjectName(_fromUtf8("mapWSUDplan"))
        self.mapWSUDimplement = QtGui.QCheckBox(self.main_options_widget)
        self.mapWSUDimplement.setGeometry(QtCore.QRect(160, 120, 191, 17))
        self.mapWSUDimplement.setText(QtGui.QApplication.translate("GISExportDialog", "Implemented WSUD", None, QtGui.QApplication.UnicodeUTF8))
        self.mapWSUDimplement.setObjectName(_fromUtf8("mapWSUDimplement"))
        self.mapFlowpaths = QtGui.QCheckBox(self.main_options_widget)
        self.mapFlowpaths.setGeometry(QtCore.QRect(50, 145, 141, 17))
        self.mapFlowpaths.setText(QtGui.QApplication.translate("GISExportDialog", "Flowpaths", None, QtGui.QApplication.UnicodeUTF8))
        self.mapFlowpaths.setObjectName(_fromUtf8("mapFlowpaths"))
        self.mapsBasins = QtGui.QCheckBox(self.main_options_widget)
        self.mapsBasins.setEnabled(False)
        self.mapsBasins.setGeometry(QtCore.QRect(160, 145, 191, 17))
        self.mapsBasins.setText(QtGui.QApplication.translate("GISExportDialog", "Basin Map", None, QtGui.QApplication.UnicodeUTF8))
        self.mapsBasins.setObjectName(_fromUtf8("mapsBasins"))
        self.additionalexport_title = QtGui.QLabel(self.main_options_widget)
        self.additionalexport_title.setGeometry(QtCore.QRect(20, 175, 181, 16))
        self.additionalexport_title.setText(QtGui.QApplication.translate("GISExportDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Additional Outputs:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.additionalexport_title.setObjectName(_fromUtf8("additionalexport_title"))
        self.mapCentrepoints = QtGui.QCheckBox(self.main_options_widget)
        self.mapCentrepoints.setGeometry(QtCore.QRect(50, 200, 201, 17))
        self.mapCentrepoints.setText(QtGui.QApplication.translate("GISExportDialog", "Centre Points for each Building Block", None, QtGui.QApplication.UnicodeUTF8))
        self.mapCentrepoints.setObjectName(_fromUtf8("mapCentrepoints"))
        self.mapLocalities = QtGui.QCheckBox(self.main_options_widget)
        self.mapLocalities.setGeometry(QtCore.QRect(310, 95, 81, 17))
        self.mapLocalities.setText(QtGui.QApplication.translate("GISExportDialog", "Localities", None, QtGui.QApplication.UnicodeUTF8))
        self.mapLocalities.setObjectName(_fromUtf8("mapLocalities"))
        self.verticalLayout.addWidget(self.main_options_widget)
        self.widget_4 = QtGui.QWidget(GISExportDialog)
        self.widget_4.setMinimumSize(QtCore.QSize(0, 38))
        self.widget_4.setMaximumSize(QtCore.QSize(16777215, 38))
        self.widget_4.setObjectName(_fromUtf8("widget_4"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.remarks = QtGui.QLabel(self.widget_4)
        self.remarks.setText(QtGui.QApplication.translate("GISExportDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-style:italic;\">UrbanBEATS.spatialexport</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.remarks.setObjectName(_fromUtf8("remarks"))
        self.horizontalLayout_2.addWidget(self.remarks)
        self.buttonBox = QtGui.QDialogButtonBox(self.widget_4)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.horizontalLayout_2.addWidget(self.buttonBox)
        self.verticalLayout.addWidget(self.widget_4)

        self.retranslateUi(GISExportDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), GISExportDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), GISExportDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(GISExportDialog)

    def retranslateUi(self, GISExportDialog):
        pass

import guitoolbaricons_rc
import guitoolbaricons_rc
import guitoolbaricons_rc
import guitoolbaricons_rc
import guitoolbaricons_rc
