# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'selectdatadialog.ui'
#
# Created: Tue Jan 15 12:03:36 2013
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_SelectData(object):
    def setupUi(self, SelectData):
        SelectData.setObjectName(_fromUtf8("SelectData"))
        SelectData.resize(825, 425)
        SelectData.setWindowTitle(QtGui.QApplication.translate("SelectData", "Select Data for Current Simulation Cycle", None, QtGui.QApplication.UnicodeUTF8))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/images/ubeatsicon.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SelectData.setWindowIcon(icon)
        self.verticalLayout = QtGui.QVBoxLayout(SelectData)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.dbtitle_widget = QtGui.QWidget(SelectData)
        self.dbtitle_widget.setMinimumSize(QtCore.QSize(0, 50))
        self.dbtitle_widget.setMaximumSize(QtCore.QSize(16777215, 50))
        self.dbtitle_widget.setObjectName(_fromUtf8("dbtitle_widget"))
        self.bpmlogo = QtGui.QLabel(self.dbtitle_widget)
        self.bpmlogo.setGeometry(QtCore.QRect(0, 0, 50, 50))
        self.bpmlogo.setMaximumSize(QtCore.QSize(50, 50))
        self.bpmlogo.setText(_fromUtf8(""))
        self.bpmlogo.setPixmap(QtGui.QPixmap(_fromUtf8(":/images/images/D4W-logoBPM.png")))
        self.bpmlogo.setObjectName(_fromUtf8("bpmlogo"))
        self.dbsubtitle = QtGui.QLabel(self.dbtitle_widget)
        self.dbsubtitle.setGeometry(QtCore.QRect(50, 25, 561, 16))
        self.dbsubtitle.setText(QtGui.QApplication.translate("SelectData", "Create a complete data set for current simulation cycle", None, QtGui.QApplication.UnicodeUTF8))
        self.dbsubtitle.setObjectName(_fromUtf8("dbsubtitle"))
        self.line = QtGui.QFrame(self.dbtitle_widget)
        self.line.setGeometry(QtCore.QRect(50, 40, 751, 20))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setMinimumSize(QtCore.QSize(573, 0))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.dbtitle = QtGui.QLabel(self.dbtitle_widget)
        self.dbtitle.setGeometry(QtCore.QRect(50, 5, 441, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.dbtitle.setFont(font)
        self.dbtitle.setText(QtGui.QApplication.translate("SelectData", "Select Data for Simulation", None, QtGui.QApplication.UnicodeUTF8))
        self.dbtitle.setObjectName(_fromUtf8("dbtitle"))
        self.verticalLayout.addWidget(self.dbtitle_widget)
        self.widget = QtGui.QWidget(SelectData)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.databrowse = QtGui.QTreeWidget(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.databrowse.sizePolicy().hasHeightForWidth())
        self.databrowse.setSizePolicy(sizePolicy)
        self.databrowse.setMinimumSize(QtCore.QSize(275, 0))
        self.databrowse.setDragDropMode(QtGui.QAbstractItemView.DragOnly)
        self.databrowse.setObjectName(_fromUtf8("databrowse"))
        self.databrowse.headerItem().setText(0, QtGui.QApplication.translate("SelectData", "Data Browser", None, QtGui.QApplication.UnicodeUTF8))
        self.horizontalLayout.addWidget(self.databrowse)
        self.buttonwidget = QtGui.QWidget(self.widget)
        self.buttonwidget.setObjectName(_fromUtf8("buttonwidget"))
        self.addData = QtGui.QPushButton(self.buttonwidget)
        self.addData.setGeometry(QtCore.QRect(10, 50, 81, 23))
        self.addData.setText(QtGui.QApplication.translate("SelectData", "Add >>>", None, QtGui.QApplication.UnicodeUTF8))
        self.addData.setObjectName(_fromUtf8("addData"))
        self.removeData = QtGui.QPushButton(self.buttonwidget)
        self.removeData.setGeometry(QtCore.QRect(10, 220, 81, 23))
        self.removeData.setText(QtGui.QApplication.translate("SelectData", "<< Remove", None, QtGui.QApplication.UnicodeUTF8))
        self.removeData.setObjectName(_fromUtf8("removeData"))
        self.resetData = QtGui.QPushButton(self.buttonwidget)
        self.resetData.setGeometry(QtCore.QRect(10, 250, 81, 23))
        self.resetData.setText(QtGui.QApplication.translate("SelectData", "Reset", None, QtGui.QApplication.UnicodeUTF8))
        self.resetData.setObjectName(_fromUtf8("resetData"))
        self.horizontalLayout.addWidget(self.buttonwidget)
        self.activedatabrowser = QtGui.QTreeWidget(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.activedatabrowser.sizePolicy().hasHeightForWidth())
        self.activedatabrowser.setSizePolicy(sizePolicy)
        self.activedatabrowser.setMinimumSize(QtCore.QSize(400, 0))
        self.activedatabrowser.setDragDropMode(QtGui.QAbstractItemView.DropOnly)
        self.activedatabrowser.setAlternatingRowColors(True)
        self.activedatabrowser.setObjectName(_fromUtf8("activedatabrowser"))
        self.activedatabrowser.headerItem().setText(0, QtGui.QApplication.translate("SelectData", "Active Data", None, QtGui.QApplication.UnicodeUTF8))
        self.activedatabrowser.headerItem().setText(1, QtGui.QApplication.translate("SelectData", "Type of Data", None, QtGui.QApplication.UnicodeUTF8))
        self.activedatabrowser.header().setDefaultSectionSize(200)
        self.activedatabrowser.header().setMinimumSectionSize(100)
        self.activedatabrowser.header().setSortIndicatorShown(True)
        self.horizontalLayout.addWidget(self.activedatabrowser)
        self.verticalLayout.addWidget(self.widget)
        self.buttonBox = QtGui.QDialogButtonBox(SelectData)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(SelectData)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), SelectData.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), SelectData.reject)
        QtCore.QMetaObject.connectSlotsByName(SelectData)

    def retranslateUi(self, SelectData):
        pass

import guitoolbaricons_rc
import guitoolbaricons_rc
import guitoolbaricons_rc
import guitoolbaricons_rc
