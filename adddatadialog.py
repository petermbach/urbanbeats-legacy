# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adddatadialog.ui'
#
# Created: Sun Jul 09 22:22:45 2017
#      by: PyQt4 UI code generator 4.11.3
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

class Ui_AddDataDialog(object):
    def setupUi(self, AddDataDialog):
        AddDataDialog.setObjectName(_fromUtf8("AddDataDialog"))
        AddDataDialog.resize(320, 222)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../../../../ubeatsicon.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AddDataDialog.setWindowIcon(icon)
        self.verticalLayout = QtGui.QVBoxLayout(AddDataDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.dbtitle_widget = QtGui.QWidget(AddDataDialog)
        self.dbtitle_widget.setMinimumSize(QtCore.QSize(0, 50))
        self.dbtitle_widget.setMaximumSize(QtCore.QSize(16777215, 50))
        self.dbtitle_widget.setObjectName(_fromUtf8("dbtitle_widget"))
        self.line = QtGui.QFrame(self.dbtitle_widget)
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
        self.dbtitle = QtGui.QLabel(self.dbtitle_widget)
        self.dbtitle.setGeometry(QtCore.QRect(50, 5, 241, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.dbtitle.setFont(font)
        self.dbtitle.setObjectName(_fromUtf8("dbtitle"))
        self.bpmlogo = QtGui.QLabel(self.dbtitle_widget)
        self.bpmlogo.setGeometry(QtCore.QRect(0, 0, 50, 50))
        self.bpmlogo.setMaximumSize(QtCore.QSize(50, 50))
        self.bpmlogo.setText(_fromUtf8(""))
        self.bpmlogo.setPixmap(QtGui.QPixmap(_fromUtf8(":/images/images/D4W-logoBPM.png")))
        self.bpmlogo.setObjectName(_fromUtf8("bpmlogo"))
        self.dbsubtitle = QtGui.QLabel(self.dbtitle_widget)
        self.dbsubtitle.setGeometry(QtCore.QRect(50, 25, 561, 16))
        self.dbsubtitle.setObjectName(_fromUtf8("dbsubtitle"))
        self.verticalLayout.addWidget(self.dbtitle_widget)
        self.maindb_widget = QtGui.QWidget(AddDataDialog)
        self.maindb_widget.setObjectName(_fromUtf8("maindb_widget"))
        self.adddatabrowse = QtGui.QToolButton(self.maindb_widget)
        self.adddatabrowse.setGeometry(QtCore.QRect(230, 20, 61, 20))
        self.adddatabrowse.setObjectName(_fromUtf8("adddatabrowse"))
        self.databox = QtGui.QLineEdit(self.maindb_widget)
        self.databox.setGeometry(QtCore.QRect(60, 20, 161, 20))
        self.databox.setReadOnly(False)
        self.databox.setObjectName(_fromUtf8("databox"))
        self.datafile_lbl = QtGui.QLabel(self.maindb_widget)
        self.datafile_lbl.setGeometry(QtCore.QRect(10, 20, 61, 16))
        self.datafile_lbl.setObjectName(_fromUtf8("datafile_lbl"))
        self.datatype_lbl = QtGui.QLabel(self.maindb_widget)
        self.datatype_lbl.setGeometry(QtCore.QRect(10, 60, 91, 16))
        self.datatype_lbl.setObjectName(_fromUtf8("datatype_lbl"))
        self.datatypecombo = QtGui.QComboBox(self.maindb_widget)
        self.datatypecombo.setGeometry(QtCore.QRect(100, 60, 191, 20))
        self.datatypecombo.setObjectName(_fromUtf8("datatypecombo"))
        self.datatypecombo.addItem(_fromUtf8(""))
        self.datatypecombo.addItem(_fromUtf8(""))
        self.datatypecombo.addItem(_fromUtf8(""))
        self.datatypecombo.addItem(_fromUtf8(""))
        self.datatypecombo.addItem(_fromUtf8(""))
        self.datatypecombo.addItem(_fromUtf8(""))
        self.datatypecombo.addItem(_fromUtf8(""))
        self.datatypecombo.addItem(_fromUtf8(""))
        self.datatypecombo.addItem(_fromUtf8(""))
        self.datatypecombo.addItem(_fromUtf8(""))
        self.datatypecombo.addItem(_fromUtf8(""))
        self.datatypecombo.addItem(_fromUtf8(""))
        self.datatypecombo.addItem(_fromUtf8(""))
        self.datatypecombo.addItem(_fromUtf8(""))
        self.datatypecombo.addItem(_fromUtf8(""))
        self.datatypecombo.addItem(_fromUtf8(""))
        self.datatypecombo.addItem(_fromUtf8(""))
        self.verticalLayout.addWidget(self.maindb_widget)
        self.footwidget = QtGui.QWidget(AddDataDialog)
        self.footwidget.setMinimumSize(QtCore.QSize(0, 38))
        self.footwidget.setMaximumSize(QtCore.QSize(16777215, 38))
        self.footwidget.setObjectName(_fromUtf8("footwidget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.footwidget)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.multi_adddata = QtGui.QToolButton(self.footwidget)
        self.multi_adddata.setMinimumSize(QtCore.QSize(75, 20))
        self.multi_adddata.setObjectName(_fromUtf8("multi_adddata"))
        self.horizontalLayout_2.addWidget(self.multi_adddata)
        self.multi_cleardata = QtGui.QToolButton(self.footwidget)
        self.multi_cleardata.setMinimumSize(QtCore.QSize(75, 0))
        self.multi_cleardata.setObjectName(_fromUtf8("multi_cleardata"))
        self.horizontalLayout_2.addWidget(self.multi_cleardata)
        self.done_button = QtGui.QPushButton(self.footwidget)
        self.done_button.setObjectName(_fromUtf8("done_button"))
        self.horizontalLayout_2.addWidget(self.done_button)
        self.verticalLayout.addWidget(self.footwidget)

        self.retranslateUi(AddDataDialog)
        self.datatypecombo.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(AddDataDialog)

    def retranslateUi(self, AddDataDialog):
        AddDataDialog.setWindowTitle(_translate("AddDataDialog", "Add Data...", None))
        self.dbtitle.setText(_translate("AddDataDialog", "Add Data", None))
        self.dbsubtitle.setText(_translate("AddDataDialog", "Add GIS or Climate Data to the Project", None))
        self.adddatabrowse.setText(_translate("AddDataDialog", "Browse...", None))
        self.datafile_lbl.setWhatsThis(_translate("AddDataDialog", "Rainfall time series, obtain data from weather station or climate authority of your city. Time series should be in rainfall depth and have units millimetres.", None))
        self.datafile_lbl.setText(_translate("AddDataDialog", "Data File:", None))
        self.datatype_lbl.setWhatsThis(_translate("AddDataDialog", "Rainfall time series, obtain data from weather station or climate authority of your city. Time series should be in rainfall depth and have units millimetres.", None))
        self.datatype_lbl.setText(_translate("AddDataDialog", "Select Data Type:", None))
        self.datatypecombo.setItemText(0, _translate("AddDataDialog", "<undefined>", None))
        self.datatypecombo.setItemText(1, _translate("AddDataDialog", "Elevation Map", None))
        self.datatypecombo.setItemText(2, _translate("AddDataDialog", "Soil Map", None))
        self.datatypecombo.setItemText(3, _translate("AddDataDialog", "Land Use Map", None))
        self.datatypecombo.setItemText(4, _translate("AddDataDialog", "Population Map", None))
        self.datatypecombo.setItemText(5, _translate("AddDataDialog", "Employment Map", None))
        self.datatypecombo.setItemText(6, _translate("AddDataDialog", "Planning Overlay Map", None))
        self.datatypecombo.setItemText(7, _translate("AddDataDialog", "Locality Map", None))
        self.datatypecombo.setItemText(8, _translate("AddDataDialog", "Groundwater Map", None))
        self.datatypecombo.setItemText(9, _translate("AddDataDialog", "Rivers Map", None))
        self.datatypecombo.setItemText(10, _translate("AddDataDialog", "Lakes Map", None))
        self.datatypecombo.setItemText(11, _translate("AddDataDialog", "Socio-Economic Data Map", None))
        self.datatypecombo.setItemText(12, _translate("AddDataDialog", "Existing WSUD Systems", None))
        self.datatypecombo.setItemText(13, _translate("AddDataDialog", "Existing Network Infrastructure", None))
        self.datatypecombo.setItemText(14, _translate("AddDataDialog", "Rainfall Time Series", None))
        self.datatypecombo.setItemText(15, _translate("AddDataDialog", "Evapotranspiration Time Series", None))
        self.datatypecombo.setItemText(16, _translate("AddDataDialog", "Solar Radiation Time Series", None))
        self.multi_adddata.setText(_translate("AddDataDialog", "Add Data", None))
        self.multi_cleardata.setText(_translate("AddDataDialog", "Clear", None))
        self.done_button.setText(_translate("AddDataDialog", "Done", None))

import guitoolbaricons_rc
