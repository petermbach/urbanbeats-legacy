# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'preferencesdialog.ui'
#
# Created: Thu Aug 09 01:11:15 2012
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_PreferencesDialog(object):
    def setupUi(self, PreferencesDialog):
        PreferencesDialog.setObjectName(_fromUtf8("PreferencesDialog"))
        PreferencesDialog.resize(480, 640)
        PreferencesDialog.setWindowTitle(QtGui.QApplication.translate("PreferencesDialog", "Preferences", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalLayout = QtGui.QVBoxLayout(PreferencesDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.title_frame = QtGui.QFrame(PreferencesDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title_frame.sizePolicy().hasHeightForWidth())
        self.title_frame.setSizePolicy(sizePolicy)
        self.title_frame.setMinimumSize(QtCore.QSize(0, 50))
        self.title_frame.setMaximumSize(QtCore.QSize(16777215, 50))
        self.title_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.title_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.title_frame.setObjectName(_fromUtf8("title_frame"))
        self.dbtitle = QtGui.QLabel(self.title_frame)
        self.dbtitle.setGeometry(QtCore.QRect(55, 5, 441, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.dbtitle.setFont(font)
        self.dbtitle.setText(QtGui.QApplication.translate("PreferencesDialog", "Preferences", None, QtGui.QApplication.UnicodeUTF8))
        self.dbtitle.setObjectName(_fromUtf8("dbtitle"))
        self.dbsubtitle = QtGui.QLabel(self.title_frame)
        self.dbsubtitle.setGeometry(QtCore.QRect(55, 25, 561, 16))
        self.dbsubtitle.setText(QtGui.QApplication.translate("PreferencesDialog", "Configure the program", None, QtGui.QApplication.UnicodeUTF8))
        self.dbsubtitle.setObjectName(_fromUtf8("dbsubtitle"))
        self.line = QtGui.QFrame(self.title_frame)
        self.line.setGeometry(QtCore.QRect(50, 40, 573, 20))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setMinimumSize(QtCore.QSize(573, 0))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.preferences_cogs = QtGui.QLabel(self.title_frame)
        self.preferences_cogs.setGeometry(QtCore.QRect(0, 0, 50, 50))
        self.preferences_cogs.setMinimumSize(QtCore.QSize(50, 50))
        self.preferences_cogs.setMaximumSize(QtCore.QSize(50, 50))
        self.preferences_cogs.setText(_fromUtf8(""))
        self.preferences_cogs.setPixmap(QtGui.QPixmap(_fromUtf8(":/images/bevel-gear-icon.png")))
        self.preferences_cogs.setObjectName(_fromUtf8("preferences_cogs"))
        self.verticalLayout.addWidget(self.title_frame)
        self.main_preferences_widget = QtGui.QWidget(PreferencesDialog)
        self.main_preferences_widget.setObjectName(_fromUtf8("main_preferences_widget"))
        self.nopref_lbl = QtGui.QLabel(self.main_preferences_widget)
        self.nopref_lbl.setGeometry(QtCore.QRect(150, 120, 181, 16))
        self.nopref_lbl.setText(QtGui.QApplication.translate("PreferencesDialog", "Curently no preferences available", None, QtGui.QApplication.UnicodeUTF8))
        self.nopref_lbl.setObjectName(_fromUtf8("nopref_lbl"))
        self.verticalLayout.addWidget(self.main_preferences_widget)
        self.widget_4 = QtGui.QWidget(PreferencesDialog)
        self.widget_4.setMinimumSize(QtCore.QSize(0, 38))
        self.widget_4.setMaximumSize(QtCore.QSize(16777215, 38))
        self.widget_4.setObjectName(_fromUtf8("widget_4"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.remarks = QtGui.QLabel(self.widget_4)
        self.remarks.setText(QtGui.QApplication.translate("PreferencesDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-style:italic;\">UrbanBEATS.preferences</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.remarks.setObjectName(_fromUtf8("remarks"))
        self.horizontalLayout_2.addWidget(self.remarks)
        self.buttonBox = QtGui.QDialogButtonBox(self.widget_4)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.horizontalLayout_2.addWidget(self.buttonBox)
        self.verticalLayout.addWidget(self.widget_4)

        self.retranslateUi(PreferencesDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), PreferencesDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), PreferencesDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(PreferencesDialog)

    def retranslateUi(self, PreferencesDialog):
        pass

import guitoolbaricons_rc
