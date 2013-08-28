# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'aboutdialog.ui'
#
# Created: Thu Aug 09 01:19:43 2012
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_AboutDialog(object):
    def setupUi(self, AboutDialog):
        AboutDialog.setObjectName(_fromUtf8("AboutDialog"))
        AboutDialog.resize(320, 240)
        AboutDialog.setWindowTitle(QtGui.QApplication.translate("AboutDialog", "About UrbanBEATS", None, QtGui.QApplication.UnicodeUTF8))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../../../../ubeatsicon.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AboutDialog.setWindowIcon(icon)
        self.buttonBox = QtGui.QDialogButtonBox(AboutDialog)
        self.buttonBox.setGeometry(QtCore.QRect(230, 170, 81, 61))
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.ubeatslogo = QtGui.QLabel(AboutDialog)
        self.ubeatslogo.setGeometry(QtCore.QRect(20, 20, 128, 122))
        self.ubeatslogo.setText(_fromUtf8(""))
        self.ubeatslogo.setPixmap(QtGui.QPixmap(_fromUtf8(":/images/images/ubeatslogo128x128.png")))
        self.ubeatslogo.setObjectName(_fromUtf8("ubeatslogo"))
        self.simconfig_lbl = QtGui.QLabel(AboutDialog)
        self.simconfig_lbl.setGeometry(QtCore.QRect(80, 140, 91, 20))
        self.simconfig_lbl.setText(QtGui.QApplication.translate("AboutDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">version 1.0</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.simconfig_lbl.setObjectName(_fromUtf8("simconfig_lbl"))
        self.simconfig_lbl_2 = QtGui.QLabel(AboutDialog)
        self.simconfig_lbl_2.setGeometry(QtCore.QRect(30, 170, 171, 20))
        self.simconfig_lbl_2.setText(QtGui.QApplication.translate("AboutDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Author: Peter M. Bach</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.simconfig_lbl_2.setObjectName(_fromUtf8("simconfig_lbl_2"))
        self.simconfig_lbl_3 = QtGui.QLabel(AboutDialog)
        self.simconfig_lbl_3.setGeometry(QtCore.QRect(30, 190, 151, 20))
        self.simconfig_lbl_3.setText(QtGui.QApplication.translate("AboutDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"www.urbanbeatsmodel.com\"><span style=\" text-decoration: underline; color:#0000ff;\">www.urbanbeatsmodel.com</span></a></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.simconfig_lbl_3.setObjectName(_fromUtf8("simconfig_lbl_3"))
        self.simconfig_lbl_4 = QtGui.QLabel(AboutDialog)
        self.simconfig_lbl_4.setGeometry(QtCore.QRect(30, 210, 171, 20))
        self.simconfig_lbl_4.setText(QtGui.QApplication.translate("AboutDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">(C) 2011, 2012 Peter M. Bach</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.simconfig_lbl_4.setObjectName(_fromUtf8("simconfig_lbl_4"))

        self.retranslateUi(AboutDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), AboutDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), AboutDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(AboutDialog)

    def retranslateUi(self, AboutDialog):
        pass

import guitoolbaricons_rc
