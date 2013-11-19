# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'narrativegui.ui'
#
# Created: Tue Nov 19 10:50:44 2013
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_NarrativeDialog(object):
    def setupUi(self, NarrativeDialog):
        NarrativeDialog.setObjectName(_fromUtf8("NarrativeDialog"))
        NarrativeDialog.resize(480, 352)
        NarrativeDialog.setWindowTitle(QtGui.QApplication.translate("NarrativeDialog", "Narrative for Current Tab", None, QtGui.QApplication.UnicodeUTF8))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../../../../ubeatsicon.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        NarrativeDialog.setWindowIcon(icon)
        self.verticalLayout = QtGui.QVBoxLayout(NarrativeDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.title_widget = QtGui.QWidget(NarrativeDialog)
        self.title_widget.setMinimumSize(QtCore.QSize(0, 50))
        self.title_widget.setMaximumSize(QtCore.QSize(16777215, 50))
        self.title_widget.setObjectName(_fromUtf8("title_widget"))
        self.bpmlogo = QtGui.QLabel(self.title_widget)
        self.bpmlogo.setGeometry(QtCore.QRect(0, 0, 50, 50))
        self.bpmlogo.setMaximumSize(QtCore.QSize(50, 50))
        self.bpmlogo.setText(_fromUtf8(""))
        self.bpmlogo.setPixmap(QtGui.QPixmap(_fromUtf8(":/images/images/D4W-logoBPM.png")))
        self.bpmlogo.setObjectName(_fromUtf8("bpmlogo"))
        self.dbtitle = QtGui.QLabel(self.title_widget)
        self.dbtitle.setGeometry(QtCore.QRect(50, 5, 331, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.dbtitle.setFont(font)
        self.dbtitle.setText(QtGui.QApplication.translate("NarrativeDialog", "Narrative Description for Current Tab", None, QtGui.QApplication.UnicodeUTF8))
        self.dbtitle.setObjectName(_fromUtf8("dbtitle"))
        self.dbsubtitle = QtGui.QLabel(self.title_widget)
        self.dbsubtitle.setGeometry(QtCore.QRect(50, 25, 441, 20))
        self.dbsubtitle.setText(QtGui.QApplication.translate("NarrativeDialog", "Add information about case study to provide context to the simulation results", None, QtGui.QApplication.UnicodeUTF8))
        self.dbsubtitle.setObjectName(_fromUtf8("dbsubtitle"))
        self.verticalLayout.addWidget(self.title_widget)
        self.widget = QtGui.QWidget(NarrativeDialog)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.heading_widget = QtGui.QWidget(self.widget)
        self.heading_widget.setObjectName(_fromUtf8("heading_widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.heading_widget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.heading_lbl = QtGui.QLabel(self.heading_widget)
        self.heading_lbl.setMinimumSize(QtCore.QSize(70, 0))
        self.heading_lbl.setMaximumSize(QtCore.QSize(70, 16777215))
        self.heading_lbl.setWhatsThis(QtGui.QApplication.translate("NarrativeDialog", "Width of the square cell in the city grid in metres", None, QtGui.QApplication.UnicodeUTF8))
        self.heading_lbl.setText(QtGui.QApplication.translate("NarrativeDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Heading</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.heading_lbl.setObjectName(_fromUtf8("heading_lbl"))
        self.horizontalLayout.addWidget(self.heading_lbl)
        self.heading_box = QtGui.QLineEdit(self.heading_widget)
        self.heading_box.setObjectName(_fromUtf8("heading_box"))
        self.horizontalLayout.addWidget(self.heading_box)
        self.year_lbl = QtGui.QLabel(self.heading_widget)
        self.year_lbl.setMinimumSize(QtCore.QSize(50, 0))
        self.year_lbl.setMaximumSize(QtCore.QSize(50, 16777215))
        self.year_lbl.setWhatsThis(QtGui.QApplication.translate("NarrativeDialog", "Width of the square cell in the city grid in metres", None, QtGui.QApplication.UnicodeUTF8))
        self.year_lbl.setText(QtGui.QApplication.translate("NarrativeDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Year</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.year_lbl.setObjectName(_fromUtf8("year_lbl"))
        self.horizontalLayout.addWidget(self.year_lbl)
        self.year_spin = QtGui.QSpinBox(self.heading_widget)
        self.year_spin.setMinimumSize(QtCore.QSize(50, 0))
        self.year_spin.setMinimum(1900)
        self.year_spin.setMaximum(3000)
        self.year_spin.setObjectName(_fromUtf8("year_spin"))
        self.horizontalLayout.addWidget(self.year_spin)
        self.verticalLayout_2.addWidget(self.heading_widget)
        self.narrative_box = QtGui.QPlainTextEdit(self.widget)
        self.narrative_box.setPlainText(QtGui.QApplication.translate("NarrativeDialog", "insert narrative description here...", None, QtGui.QApplication.UnicodeUTF8))
        self.narrative_box.setObjectName(_fromUtf8("narrative_box"))
        self.verticalLayout_2.addWidget(self.narrative_box)
        self.verticalLayout.addWidget(self.widget)
        self.widget_4 = QtGui.QWidget(NarrativeDialog)
        self.widget_4.setMinimumSize(QtCore.QSize(0, 38))
        self.widget_4.setMaximumSize(QtCore.QSize(16777215, 38))
        self.widget_4.setObjectName(_fromUtf8("widget_4"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.remarks = QtGui.QLabel(self.widget_4)
        self.remarks.setText(QtGui.QApplication.translate("NarrativeDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-style:italic;\">UrbanBEATS.current_narrative</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.remarks.setObjectName(_fromUtf8("remarks"))
        self.horizontalLayout_2.addWidget(self.remarks)
        self.buttonBox = QtGui.QDialogButtonBox(self.widget_4)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.horizontalLayout_2.addWidget(self.buttonBox)
        self.verticalLayout.addWidget(self.widget_4)

        self.retranslateUi(NarrativeDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), NarrativeDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), NarrativeDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(NarrativeDialog)

    def retranslateUi(self, NarrativeDialog):
        pass

import guitoolbaricons_rc
import guitoolbaricons_rc
import guitoolbaricons_rc
import guitoolbaricons_rc
import guitoolbaricons_rc
import guitoolbaricons_rc
