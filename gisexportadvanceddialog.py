# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gisexportadvanceddialog.ui'
#
# Created: Wed Apr 03 16:32:56 2013
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_GISAdvancedDialog(object):
    def setupUi(self, GISAdvancedDialog):
        GISAdvancedDialog.setObjectName(_fromUtf8("GISAdvancedDialog"))
        GISAdvancedDialog.resize(480, 370)
        GISAdvancedDialog.setWindowTitle(QtGui.QApplication.translate("GISAdvancedDialog", "Preferences", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalLayout = QtGui.QVBoxLayout(GISAdvancedDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.widget = QtGui.QWidget(GISAdvancedDialog)
        self.widget.setMinimumSize(QtCore.QSize(0, 50))
        self.widget.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.header_img = QtGui.QLabel(self.widget)
        self.header_img.setGeometry(QtCore.QRect(5, 0, 50, 50))
        self.header_img.setMinimumSize(QtCore.QSize(50, 50))
        self.header_img.setMaximumSize(QtCore.QSize(50, 50))
        self.header_img.setText(_fromUtf8(""))
        self.header_img.setPixmap(QtGui.QPixmap(_fromUtf8(":/images/Layers-icon-50px.png")))
        self.header_img.setObjectName(_fromUtf8("header_img"))
        self.dbtitle = QtGui.QLabel(self.widget)
        self.dbtitle.setGeometry(QtCore.QRect(60, 5, 381, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.dbtitle.setFont(font)
        self.dbtitle.setText(QtGui.QApplication.translate("GISAdvancedDialog", "Advanced Options for Spatial Data Export", None, QtGui.QApplication.UnicodeUTF8))
        self.dbtitle.setObjectName(_fromUtf8("dbtitle"))
        self.dbsubtitle = QtGui.QLabel(self.widget)
        self.dbsubtitle.setGeometry(QtCore.QRect(60, 25, 371, 16))
        self.dbsubtitle.setText(QtGui.QApplication.translate("GISAdvancedDialog", "Select Additional Options for exporting spatial data from UrbanBEATS", None, QtGui.QApplication.UnicodeUTF8))
        self.dbsubtitle.setObjectName(_fromUtf8("dbsubtitle"))
        self.verticalLayout.addWidget(self.widget)
        self.main_options_widget = QtGui.QWidget(GISAdvancedDialog)
        self.main_options_widget.setObjectName(_fromUtf8("main_options_widget"))
        self.project_title = QtGui.QLabel(self.main_options_widget)
        self.project_title.setGeometry(QtCore.QRect(10, 10, 271, 16))
        self.project_title.setText(QtGui.QApplication.translate("GISAdvancedDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Shapefile Projection &amp; Additional Formats</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.project_title.setObjectName(_fromUtf8("project_title"))
        self.nopref_lbl_2 = QtGui.QLabel(self.main_options_widget)
        self.nopref_lbl_2.setGeometry(QtCore.QRect(160, 190, 181, 16))
        self.nopref_lbl_2.setText(_fromUtf8(""))
        self.nopref_lbl_2.setTextFormat(QtCore.Qt.AutoText)
        self.nopref_lbl_2.setPixmap(QtGui.QPixmap(_fromUtf8(":/guitoolbaricons/custom-reports-icon.png")))
        self.nopref_lbl_2.setObjectName(_fromUtf8("nopref_lbl_2"))
        self.offset_title = QtGui.QLabel(self.main_options_widget)
        self.offset_title.setGeometry(QtCore.QRect(10, 125, 181, 16))
        self.offset_title.setText(QtGui.QApplication.translate("GISAdvancedDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Offset Exported Map:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.offset_title.setObjectName(_fromUtf8("offset_title"))
        self.project_lbl1 = QtGui.QLabel(self.main_options_widget)
        self.project_lbl1.setGeometry(QtCore.QRect(20, 37, 181, 16))
        self.project_lbl1.setText(QtGui.QApplication.translate("GISAdvancedDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Select Projection:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.project_lbl1.setObjectName(_fromUtf8("project_lbl1"))
        self.projectionCustombox = QtGui.QLineEdit(self.main_options_widget)
        self.projectionCustombox.setGeometry(QtCore.QRect(120, 70, 241, 20))
        self.projectionCustombox.setObjectName(_fromUtf8("projectionCustombox"))
        self.projectionCombo = QtGui.QComboBox(self.main_options_widget)
        self.projectionCombo.setGeometry(QtCore.QRect(120, 40, 231, 16))
        self.projectionCombo.setObjectName(_fromUtf8("projectionCombo"))
        self.projectionCombo.addItem(_fromUtf8(""))
        self.projectionCombo.setItemText(0, QtGui.QApplication.translate("GISAdvancedDialog", "WGS_1984_UTM_Zone 54 S", None, QtGui.QApplication.UnicodeUTF8))
        self.projectionCombo.addItem(_fromUtf8(""))
        self.projectionCombo.setItemText(1, QtGui.QApplication.translate("GISAdvancedDialog", "WGS_1984_UTM_Zone_55 S", None, QtGui.QApplication.UnicodeUTF8))
        self.projectionCombo.addItem(_fromUtf8(""))
        self.projectionCombo.setItemText(2, QtGui.QApplication.translate("GISAdvancedDialog", "WGS_1984_UTM_Zone_56 S", None, QtGui.QApplication.UnicodeUTF8))
        self.projectionCheck = QtGui.QCheckBox(self.main_options_widget)
        self.projectionCheck.setGeometry(QtCore.QRect(360, 40, 91, 17))
        self.projectionCheck.setText(QtGui.QApplication.translate("GISAdvancedDialog", "User-defined", None, QtGui.QApplication.UnicodeUTF8))
        self.projectionCheck.setObjectName(_fromUtf8("projectionCheck"))
        self.projection_lbl3 = QtGui.QLabel(self.main_options_widget)
        self.projection_lbl3.setGeometry(QtCore.QRect(370, 70, 91, 16))
        self.projection_lbl3.setText(QtGui.QApplication.translate("GISAdvancedDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">(proj4 format)</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.projection_lbl3.setObjectName(_fromUtf8("projection_lbl3"))
        self.offsetx_box = QtGui.QLineEdit(self.main_options_widget)
        self.offsetx_box.setGeometry(QtCore.QRect(150, 195, 131, 20))
        self.offsetx_box.setObjectName(_fromUtf8("offsetx_box"))
        self.offsetfrominput_radio = QtGui.QRadioButton(self.main_options_widget)
        self.offsetfrominput_radio.setGeometry(QtCore.QRect(30, 150, 311, 17))
        self.offsetfrominput_radio.setText(QtGui.QApplication.translate("GISAdvancedDialog", "Use input data to align maps", None, QtGui.QApplication.UnicodeUTF8))
        self.offsetfrominput_radio.setObjectName(_fromUtf8("offsetfrominput_radio"))
        self.offsetcustom_radio = QtGui.QRadioButton(self.main_options_widget)
        self.offsetcustom_radio.setGeometry(QtCore.QRect(30, 170, 311, 17))
        self.offsetcustom_radio.setText(QtGui.QApplication.translate("GISAdvancedDialog", "Use custom offsets (from global origin 0,0)", None, QtGui.QApplication.UnicodeUTF8))
        self.offsetcustom_radio.setObjectName(_fromUtf8("offsetcustom_radio"))
        self.offsetx_lbl = QtGui.QLabel(self.main_options_widget)
        self.offsetx_lbl.setGeometry(QtCore.QRect(70, 195, 71, 16))
        self.offsetx_lbl.setText(QtGui.QApplication.translate("GISAdvancedDialog", "x-Offset [m]:", None, QtGui.QApplication.UnicodeUTF8))
        self.offsetx_lbl.setObjectName(_fromUtf8("offsetx_lbl"))
        self.offsety_lbl = QtGui.QLabel(self.main_options_widget)
        self.offsety_lbl.setGeometry(QtCore.QRect(70, 220, 71, 16))
        self.offsety_lbl.setText(QtGui.QApplication.translate("GISAdvancedDialog", "y-Offset [m]:", None, QtGui.QApplication.UnicodeUTF8))
        self.offsety_lbl.setObjectName(_fromUtf8("offsety_lbl"))
        self.offsety_box = QtGui.QLineEdit(self.main_options_widget)
        self.offsety_box.setGeometry(QtCore.QRect(150, 220, 131, 20))
        self.offsety_box.setText(_fromUtf8(""))
        self.offsety_box.setObjectName(_fromUtf8("offsety_box"))
        self.projection_lbl2 = QtGui.QLabel(self.main_options_widget)
        self.projection_lbl2.setGeometry(QtCore.QRect(20, 70, 181, 16))
        self.projection_lbl2.setText(QtGui.QApplication.translate("GISAdvancedDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Specify Projection:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.projection_lbl2.setObjectName(_fromUtf8("projection_lbl2"))
        self.kmlboolcheck = QtGui.QCheckBox(self.main_options_widget)
        self.kmlboolcheck.setGeometry(QtCore.QRect(30, 100, 191, 17))
        self.kmlboolcheck.setText(QtGui.QApplication.translate("GISAdvancedDialog", "Export KML Maps (Google Earth)", None, QtGui.QApplication.UnicodeUTF8))
        self.kmlboolcheck.setObjectName(_fromUtf8("kmlboolcheck"))
        self.verticalLayout.addWidget(self.main_options_widget)
        self.widget_4 = QtGui.QWidget(GISAdvancedDialog)
        self.widget_4.setMinimumSize(QtCore.QSize(0, 38))
        self.widget_4.setMaximumSize(QtCore.QSize(16777215, 38))
        self.widget_4.setObjectName(_fromUtf8("widget_4"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.remarks = QtGui.QLabel(self.widget_4)
        self.remarks.setText(QtGui.QApplication.translate("GISAdvancedDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-style:italic;\">UrbanBEATS.spatialexportadvanced</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.remarks.setObjectName(_fromUtf8("remarks"))
        self.horizontalLayout_2.addWidget(self.remarks)
        self.buttonBox = QtGui.QDialogButtonBox(self.widget_4)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.horizontalLayout_2.addWidget(self.buttonBox)
        self.verticalLayout.addWidget(self.widget_4)

        self.retranslateUi(GISAdvancedDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), GISAdvancedDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), GISAdvancedDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(GISAdvancedDialog)

    def retranslateUi(self, GISAdvancedDialog):
        pass

import guitoolbaricons_rc
import guitoolbaricons_rc
import guitoolbaricons_rc
import guitoolbaricons_rc
import guitoolbaricons_rc
