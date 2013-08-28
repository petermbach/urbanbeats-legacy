# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'startscreen.ui'
#
# Created: Thu Aug 09 01:17:01 2012
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_StartDialog(object):
    def setupUi(self, StartDialog):
        StartDialog.setObjectName(_fromUtf8("StartDialog"))
        StartDialog.resize(480, 640)
        StartDialog.setWindowTitle(QtGui.QApplication.translate("StartDialog", "Getting Started...", None, QtGui.QApplication.UnicodeUTF8))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../../../../ubeatsicon.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        StartDialog.setWindowIcon(icon)
        self.ubeatslogo = QtGui.QLabel(StartDialog)
        self.ubeatslogo.setGeometry(QtCore.QRect(30, 500, 128, 122))
        self.ubeatslogo.setText(_fromUtf8(""))
        self.ubeatslogo.setPixmap(QtGui.QPixmap(_fromUtf8(":/images/images/ubeatslogo128x128.png")))
        self.ubeatslogo.setObjectName(_fromUtf8("ubeatslogo"))
        self.NewProjectButton = QtGui.QPushButton(StartDialog)
        self.NewProjectButton.setGeometry(QtCore.QRect(30, 95, 81, 81))
        self.NewProjectButton.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/guitoolbaricons/text.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.NewProjectButton.setIcon(icon1)
        self.NewProjectButton.setIconSize(QtCore.QSize(32, 32))
        self.NewProjectButton.setObjectName(_fromUtf8("NewProjectButton"))
        self.OpenProjectButton = QtGui.QPushButton(StartDialog)
        self.OpenProjectButton.setGeometry(QtCore.QRect(30, 195, 81, 81))
        self.OpenProjectButton.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/guitoolbaricons/folder-open.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.OpenProjectButton.setIcon(icon2)
        self.OpenProjectButton.setIconSize(QtCore.QSize(32, 32))
        self.OpenProjectButton.setObjectName(_fromUtf8("OpenProjectButton"))
        self.VisitWebsiteButton = QtGui.QPushButton(StartDialog)
        self.VisitWebsiteButton.setGeometry(QtCore.QRect(30, 295, 81, 81))
        self.VisitWebsiteButton.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/guitoolbaricons/world.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.VisitWebsiteButton.setIcon(icon3)
        self.VisitWebsiteButton.setIconSize(QtCore.QSize(32, 32))
        self.VisitWebsiteButton.setObjectName(_fromUtf8("VisitWebsiteButton"))
        self.dbtitle = QtGui.QLabel(StartDialog)
        self.dbtitle.setGeometry(QtCore.QRect(20, 20, 441, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.dbtitle.setFont(font)
        self.dbtitle.setText(QtGui.QApplication.translate("StartDialog", "Welcome to UrbanBEATS v1.0", None, QtGui.QApplication.UnicodeUTF8))
        self.dbtitle.setObjectName(_fromUtf8("dbtitle"))
        self.label = QtGui.QLabel(StartDialog)
        self.label.setGeometry(QtCore.QRect(40, 60, 251, 16))
        self.label.setText(QtGui.QApplication.translate("StartDialog", "Please select an option below to get started: ", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.dbtitle_2 = QtGui.QLabel(StartDialog)
        self.dbtitle_2.setGeometry(QtCore.QRect(130, 105, 441, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.dbtitle_2.setFont(font)
        self.dbtitle_2.setText(QtGui.QApplication.translate("StartDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Begin a New Project</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.dbtitle_2.setObjectName(_fromUtf8("dbtitle_2"))
        self.label_2 = QtGui.QLabel(StartDialog)
        self.label_2.setGeometry(QtCore.QRect(130, 125, 321, 16))
        self.label_2.setText(QtGui.QApplication.translate("StartDialog", "Start a new project from scratch, customize simulation type, add", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(StartDialog)
        self.label_3.setGeometry(QtCore.QRect(130, 140, 321, 16))
        self.label_3.setText(QtGui.QApplication.translate("StartDialog", "data and explore your urban environment.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.dbtitle_3 = QtGui.QLabel(StartDialog)
        self.dbtitle_3.setGeometry(QtCore.QRect(130, 200, 441, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.dbtitle_3.setFont(font)
        self.dbtitle_3.setText(QtGui.QApplication.translate("StartDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Open an Existing Project</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.dbtitle_3.setObjectName(_fromUtf8("dbtitle_3"))
        self.label_4 = QtGui.QLabel(StartDialog)
        self.label_4.setGeometry(QtCore.QRect(130, 220, 321, 16))
        self.label_4.setText(QtGui.QApplication.translate("StartDialog", "Continue from where you left off in a different simulation, update", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(StartDialog)
        self.label_5.setGeometry(QtCore.QRect(130, 235, 321, 16))
        self.label_5.setText(QtGui.QApplication.translate("StartDialog", "parameters and discover new insights.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(StartDialog)
        self.label_6.setGeometry(QtCore.QRect(130, 325, 321, 16))
        self.label_6.setText(QtGui.QApplication.translate("StartDialog", "Keep yourself up to date with the latest developments. Learn", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(StartDialog)
        self.label_7.setGeometry(QtCore.QRect(130, 340, 321, 16))
        self.label_7.setText(QtGui.QApplication.translate("StartDialog", "more about the model with the online Wiki.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.dbtitle_4 = QtGui.QLabel(StartDialog)
        self.dbtitle_4.setGeometry(QtCore.QRect(130, 305, 441, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.dbtitle_4.setFont(font)
        self.dbtitle_4.setText(QtGui.QApplication.translate("StartDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Visit UrbanBEATSModel.com</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.dbtitle_4.setObjectName(_fromUtf8("dbtitle_4"))
        self.QuitButton = QtGui.QPushButton(StartDialog)
        self.QuitButton.setGeometry(QtCore.QRect(30, 395, 81, 81))
        self.QuitButton.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/guitoolbaricons/quit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.QuitButton.setIcon(icon4)
        self.QuitButton.setIconSize(QtCore.QSize(32, 32))
        self.QuitButton.setObjectName(_fromUtf8("QuitButton"))
        self.dbtitle_5 = QtGui.QLabel(StartDialog)
        self.dbtitle_5.setGeometry(QtCore.QRect(130, 405, 441, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.dbtitle_5.setFont(font)
        self.dbtitle_5.setText(QtGui.QApplication.translate("StartDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Quit Program</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.dbtitle_5.setObjectName(_fromUtf8("dbtitle_5"))
        self.label_8 = QtGui.QLabel(StartDialog)
        self.label_8.setGeometry(QtCore.QRect(130, 425, 321, 16))
        self.label_8.setText(QtGui.QApplication.translate("StartDialog", "Close the program, see you next time.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(StartDialog)
        self.label_9.setGeometry(QtCore.QRect(180, 600, 251, 16))
        self.label_9.setText(QtGui.QApplication.translate("StartDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">version 1.0, (C) 2011, 2012, Peter M. Bach</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setObjectName(_fromUtf8("label_9"))

        self.retranslateUi(StartDialog)
        QtCore.QMetaObject.connectSlotsByName(StartDialog)

    def retranslateUi(self, StartDialog):
        pass

import guitoolbaricons_rc
