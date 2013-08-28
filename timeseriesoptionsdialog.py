# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'timeseriesoptionsdialog.ui'
#
# Created: Wed Apr 03 16:40:35 2013
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_TimeSeriesDialog(object):
    def setupUi(self, TimeSeriesDialog):
        TimeSeriesDialog.setObjectName(_fromUtf8("TimeSeriesDialog"))
        TimeSeriesDialog.resize(480, 350)
        TimeSeriesDialog.setWindowTitle(QtGui.QApplication.translate("TimeSeriesDialog", "Preferences", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalLayout = QtGui.QVBoxLayout(TimeSeriesDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.title_widget = QtGui.QWidget(TimeSeriesDialog)
        self.title_widget.setMinimumSize(QtCore.QSize(0, 50))
        self.title_widget.setMaximumSize(QtCore.QSize(16777215, 50))
        self.title_widget.setObjectName(_fromUtf8("title_widget"))
        self.dbsubtitle = QtGui.QLabel(self.title_widget)
        self.dbsubtitle.setGeometry(QtCore.QRect(55, 25, 561, 16))
        self.dbsubtitle.setText(QtGui.QApplication.translate("TimeSeriesDialog", "Configure how UrbanBEATS should export time-series data", None, QtGui.QApplication.UnicodeUTF8))
        self.dbsubtitle.setObjectName(_fromUtf8("dbsubtitle"))
        self.dbtitle = QtGui.QLabel(self.title_widget)
        self.dbtitle.setGeometry(QtCore.QRect(55, 5, 331, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.dbtitle.setFont(font)
        self.dbtitle.setText(QtGui.QApplication.translate("TimeSeriesDialog", "Time-Series Data Export Options", None, QtGui.QApplication.UnicodeUTF8))
        self.dbtitle.setObjectName(_fromUtf8("dbtitle"))
        self.header_img = QtGui.QLabel(self.title_widget)
        self.header_img.setGeometry(QtCore.QRect(0, 0, 50, 50))
        self.header_img.setMinimumSize(QtCore.QSize(50, 50))
        self.header_img.setMaximumSize(QtCore.QSize(50, 50))
        self.header_img.setText(_fromUtf8(""))
        self.header_img.setPixmap(QtGui.QPixmap(_fromUtf8(":/images/timeseries.png")))
        self.header_img.setObjectName(_fromUtf8("header_img"))
        self.verticalLayout.addWidget(self.title_widget)
        self.main_options_widget = QtGui.QWidget(TimeSeriesDialog)
        self.main_options_widget.setObjectName(_fromUtf8("main_options_widget"))
        self.nopref_lbl_2 = QtGui.QLabel(self.main_options_widget)
        self.nopref_lbl_2.setGeometry(QtCore.QRect(160, 190, 181, 16))
        self.nopref_lbl_2.setText(_fromUtf8(""))
        self.nopref_lbl_2.setTextFormat(QtCore.Qt.AutoText)
        self.nopref_lbl_2.setPixmap(QtGui.QPixmap(_fromUtf8(":/guitoolbaricons/custom-reports-icon.png")))
        self.nopref_lbl_2.setObjectName(_fromUtf8("nopref_lbl_2"))
        self.mapfilename_lbl = QtGui.QLabel(self.main_options_widget)
        self.mapfilename_lbl.setGeometry(QtCore.QRect(170, 110, 181, 16))
        self.mapfilename_lbl.setText(QtGui.QApplication.translate("TimeSeriesDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">coming soon...</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.mapfilename_lbl.setObjectName(_fromUtf8("mapfilename_lbl"))
        self.verticalLayout.addWidget(self.main_options_widget)
        self.widget_4 = QtGui.QWidget(TimeSeriesDialog)
        self.widget_4.setMinimumSize(QtCore.QSize(0, 38))
        self.widget_4.setMaximumSize(QtCore.QSize(16777215, 38))
        self.widget_4.setObjectName(_fromUtf8("widget_4"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.remarks = QtGui.QLabel(self.widget_4)
        self.remarks.setText(QtGui.QApplication.translate("TimeSeriesDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-style:italic;\">UrbanBEATS.timeseriesexport</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.remarks.setObjectName(_fromUtf8("remarks"))
        self.horizontalLayout_2.addWidget(self.remarks)
        self.buttonBox = QtGui.QDialogButtonBox(self.widget_4)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.horizontalLayout_2.addWidget(self.buttonBox)
        self.verticalLayout.addWidget(self.widget_4)

        self.retranslateUi(TimeSeriesDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), TimeSeriesDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), TimeSeriesDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(TimeSeriesDialog)

    def retranslateUi(self, TimeSeriesDialog):
        pass

import guitoolbaricons_rc
import guitoolbaricons_rc
import guitoolbaricons_rc
import guitoolbaricons_rc
import guitoolbaricons_rc
