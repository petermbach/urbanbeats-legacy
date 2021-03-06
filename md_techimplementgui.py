# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'md_techimplementgui.ui'
#
# Created: Fri Aug 01 09:33:01 2014
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_TechImplement_Dialog(object):
    def setupUi(self, TechImplement_Dialog):
        TechImplement_Dialog.setObjectName(_fromUtf8("TechImplement_Dialog"))
        TechImplement_Dialog.resize(771, 598)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TechImplement_Dialog.sizePolicy().hasHeightForWidth())
        TechImplement_Dialog.setSizePolicy(sizePolicy)
        TechImplement_Dialog.setWindowTitle(QtGui.QApplication.translate("TechImplement_Dialog", "Technology Implementation", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalLayout = QtGui.QVBoxLayout(TechImplement_Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.techimplement_title = QtGui.QFrame(TechImplement_Dialog)
        self.techimplement_title.setMinimumSize(QtCore.QSize(0, 50))
        self.techimplement_title.setMaximumSize(QtCore.QSize(16777215, 50))
        self.techimplement_title.setFrameShape(QtGui.QFrame.StyledPanel)
        self.techimplement_title.setFrameShadow(QtGui.QFrame.Raised)
        self.techimplement_title.setObjectName(_fromUtf8("techimplement_title"))
        self.tech_heading = QtGui.QLabel(self.techimplement_title)
        self.tech_heading.setGeometry(QtCore.QRect(50, 5, 451, 21))
        self.tech_heading.setText(QtGui.QApplication.translate("TechImplement_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Decentralised Technology Implementation</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.tech_heading.setObjectName(_fromUtf8("tech_heading"))
        self.tech_subheading = QtGui.QLabel(self.techimplement_title)
        self.tech_subheading.setGeometry(QtCore.QRect(50, 25, 531, 16))
        self.tech_subheading.setText(QtGui.QApplication.translate("TechImplement_Dialog", "Set Rules for implementing technology configurations found from the input masterplan", None, QtGui.QApplication.UnicodeUTF8))
        self.tech_subheading.setObjectName(_fromUtf8("tech_subheading"))
        self.label = QtGui.QLabel(self.techimplement_title)
        self.label.setGeometry(QtCore.QRect(0, 0, 50, 50))
        self.label.setMinimumSize(QtCore.QSize(50, 50))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8(":/general/ublogo50.png")))
        self.label.setObjectName(_fromUtf8("label"))
        self.line = QtGui.QFrame(self.techimplement_title)
        self.line.setGeometry(QtCore.QRect(50, 49, 703, 3))
        self.line.setMinimumSize(QtCore.QSize(703, 0))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout.addWidget(self.techimplement_title)
        self.techimplement_input = QtGui.QTabWidget(TechImplement_Dialog)
        self.techimplement_input.setObjectName(_fromUtf8("techimplement_input"))
        self.DesignCriteria = QtGui.QWidget()
        self.DesignCriteria.setObjectName(_fromUtf8("DesignCriteria"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.DesignCriteria)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.techimplement_widget = QtGui.QWidget(self.DesignCriteria)
        self.techimplement_widget.setObjectName(_fromUtf8("techimplement_widget"))
        self.gridLayout_22 = QtGui.QGridLayout(self.techimplement_widget)
        self.gridLayout_22.setMargin(0)
        self.gridLayout_22.setObjectName(_fromUtf8("gridLayout_22"))
        self.techimplement_inputs = QtGui.QScrollArea(self.techimplement_widget)
        self.techimplement_inputs.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.techimplement_inputs.setWidgetResizable(True)
        self.techimplement_inputs.setObjectName(_fromUtf8("techimplement_inputs"))
        self.design_crit_inputs_widget = QtGui.QWidget()
        self.design_crit_inputs_widget.setGeometry(QtCore.QRect(0, 0, 465, 448))
        self.design_crit_inputs_widget.setObjectName(_fromUtf8("design_crit_inputs_widget"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.design_crit_inputs_widget)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.blockimplement_title = QtGui.QLabel(self.design_crit_inputs_widget)
        self.blockimplement_title.setMinimumSize(QtCore.QSize(0, 16))
        self.blockimplement_title.setMaximumSize(QtCore.QSize(16777215, 16))
        self.blockimplement_title.setWhatsThis(QtGui.QApplication.translate("TechImplement_Dialog", "Select what design goals to consider and what priority they take over each other. Highest priority (1) and Lowest priority (3) influence technology\'s chance of being implemented. Note that equal priority can be set as well, in which case no one design rationale is more important than the other.", None, QtGui.QApplication.UnicodeUTF8))
        self.blockimplement_title.setText(QtGui.QApplication.translate("TechImplement_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Lot, Street, Neighbourhood Implementation</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.blockimplement_title.setObjectName(_fromUtf8("blockimplement_title"))
        self.verticalLayout_5.addWidget(self.blockimplement_title)
        self.blockimplement_widget = QtGui.QWidget(self.design_crit_inputs_widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.blockimplement_widget.sizePolicy().hasHeightForWidth())
        self.blockimplement_widget.setSizePolicy(sizePolicy)
        self.blockimplement_widget.setMinimumSize(QtCore.QSize(0, 280))
        self.blockimplement_widget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.blockimplement_widget.setObjectName(_fromUtf8("blockimplement_widget"))
        self.implement_dynamics_lbl = QtGui.QLabel(self.blockimplement_widget)
        self.implement_dynamics_lbl.setGeometry(QtCore.QRect(20, 10, 221, 16))
        self.implement_dynamics_lbl.setWhatsThis(QtGui.QApplication.translate("TechImplement_Dialog", "Determines how the model decides when systems are to be implemented. There are two possible modes: Block-based development and Parcel-based development.\n"
"\n"
"Block-based Development: If a Block", None, QtGui.QApplication.UnicodeUTF8))
        self.implement_dynamics_lbl.setText(QtGui.QApplication.translate("TechImplement_Dialog", "Choose Type of Implementation Dynamics:", None, QtGui.QApplication.UnicodeUTF8))
        self.implement_dynamics_lbl.setObjectName(_fromUtf8("implement_dynamics_lbl"))
        self.implementdynamics_combo = QtGui.QComboBox(self.blockimplement_widget)
        self.implementdynamics_combo.setGeometry(QtCore.QRect(240, 10, 181, 16))
        self.implementdynamics_combo.setObjectName(_fromUtf8("implementdynamics_combo"))
        self.implementdynamics_combo.addItem(_fromUtf8(""))
        self.implementdynamics_combo.setItemText(0, QtGui.QApplication.translate("TechImplement_Dialog", "Block-based Development", None, QtGui.QApplication.UnicodeUTF8))
        self.implementdynamics_combo.addItem(_fromUtf8(""))
        self.implementdynamics_combo.setItemText(1, QtGui.QApplication.translate("TechImplement_Dialog", "Parcel-based Development", None, QtGui.QApplication.UnicodeUTF8))
        self.implementdynamic_stack = QtGui.QStackedWidget(self.blockimplement_widget)
        self.implementdynamic_stack.setGeometry(QtCore.QRect(10, 40, 421, 231))
        self.implementdynamic_stack.setObjectName(_fromUtf8("implementdynamic_stack"))
        self.block_based = QtGui.QWidget()
        self.block_based.setObjectName(_fromUtf8("block_based"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.block_based)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.block_based_group = QtGui.QGroupBox(self.block_based)
        self.block_based_group.setTitle(QtGui.QApplication.translate("TechImplement_Dialog", "Block-based Development", None, QtGui.QApplication.UnicodeUTF8))
        self.block_based_group.setObjectName(_fromUtf8("block_based_group"))
        self.block_based_lbl1 = QtGui.QLabel(self.block_based_group)
        self.block_based_lbl1.setGeometry(QtCore.QRect(30, 25, 281, 16))
        self.block_based_lbl1.setText(QtGui.QApplication.translate("TechImplement_Dialog", "Implement if development exceeds % of Total Block Area", None, QtGui.QApplication.UnicodeUTF8))
        self.block_based_lbl1.setObjectName(_fromUtf8("block_based_lbl1"))
        self.block_dev_threshold = QtGui.QSpinBox(self.block_based_group)
        self.block_dev_threshold.setGeometry(QtCore.QRect(320, 25, 51, 16))
        self.block_dev_threshold.setSuffix(QtGui.QApplication.translate("TechImplement_Dialog", "%", None, QtGui.QApplication.UnicodeUTF8))
        self.block_dev_threshold.setProperty("value", 50)
        self.block_dev_threshold.setObjectName(_fromUtf8("block_dev_threshold"))
        self.block_based_lbl2 = QtGui.QLabel(self.block_based_group)
        self.block_based_lbl2.setGeometry(QtCore.QRect(10, 50, 131, 16))
        self.block_based_lbl2.setText(QtGui.QApplication.translate("TechImplement_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-style:italic;\">Lot Scale</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.block_based_lbl2.setObjectName(_fromUtf8("block_based_lbl2"))
        self.block_based_lbl3 = QtGui.QLabel(self.block_based_group)
        self.block_based_lbl3.setGeometry(QtCore.QRect(10, 100, 131, 16))
        self.block_based_lbl3.setText(QtGui.QApplication.translate("TechImplement_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-style:italic;\">Street Scale</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.block_based_lbl3.setObjectName(_fromUtf8("block_based_lbl3"))
        self.block_based_lbl4 = QtGui.QLabel(self.block_based_group)
        self.block_based_lbl4.setGeometry(QtCore.QRect(10, 150, 131, 16))
        self.block_based_lbl4.setText(QtGui.QApplication.translate("TechImplement_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-style:italic;\">Neighbourhood Scale</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.block_based_lbl4.setObjectName(_fromUtf8("block_based_lbl4"))
        self.neigh_forceimplement_check = QtGui.QCheckBox(self.block_based_group)
        self.neigh_forceimplement_check.setGeometry(QtCore.QRect(30, 175, 331, 17))
        self.neigh_forceimplement_check.setText(QtGui.QApplication.translate("TechImplement_Dialog", "Implement even if allocated area has not yet been zoned", None, QtGui.QApplication.UnicodeUTF8))
        self.neigh_forceimplement_check.setObjectName(_fromUtf8("neigh_forceimplement_check"))
        self.lot_amap_radio = QtGui.QRadioButton(self.block_based_group)
        self.lot_amap_radio.setGeometry(QtCore.QRect(30, 75, 151, 17))
        self.lot_amap_radio.setText(QtGui.QApplication.translate("TechImplement_Dialog", "As many units as possible", None, QtGui.QApplication.UnicodeUTF8))
        self.lot_amap_radio.setObjectName(_fromUtf8("lot_amap_radio"))
        self.lot_strict_radio = QtGui.QRadioButton(self.block_based_group)
        self.lot_strict_radio.setGeometry(QtCore.QRect(220, 75, 161, 17))
        self.lot_strict_radio.setText(QtGui.QApplication.translate("TechImplement_Dialog", "Strictly maintain % houses", None, QtGui.QApplication.UnicodeUTF8))
        self.lot_strict_radio.setObjectName(_fromUtf8("lot_strict_radio"))
        self.street_forceimplement_check = QtGui.QCheckBox(self.block_based_group)
        self.street_forceimplement_check.setGeometry(QtCore.QRect(30, 125, 331, 17))
        self.street_forceimplement_check.setText(QtGui.QApplication.translate("TechImplement_Dialog", "Implement even if allocated area has not yet been zoned", None, QtGui.QApplication.UnicodeUTF8))
        self.street_forceimplement_check.setObjectName(_fromUtf8("street_forceimplement_check"))
        self.horizontalLayout_2.addWidget(self.block_based_group)
        self.implementdynamic_stack.addWidget(self.block_based)
        self.parcel_based = QtGui.QWidget()
        self.parcel_based.setObjectName(_fromUtf8("parcel_based"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.parcel_based)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.parcel_based_group = QtGui.QGroupBox(self.parcel_based)
        self.parcel_based_group.setTitle(QtGui.QApplication.translate("TechImplement_Dialog", "Parcel-based Development", None, QtGui.QApplication.UnicodeUTF8))
        self.parcel_based_group.setObjectName(_fromUtf8("parcel_based_group"))
        self.parcel_based_lbl5 = QtGui.QLabel(self.parcel_based_group)
        self.parcel_based_lbl5.setGeometry(QtCore.QRect(10, 130, 131, 16))
        self.parcel_based_lbl5.setText(QtGui.QApplication.translate("TechImplement_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-style:italic;\">Neighbourhood Scale</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.parcel_based_lbl5.setObjectName(_fromUtf8("parcel_based_lbl5"))
        self.parcel_based_lbl1 = QtGui.QLabel(self.parcel_based_group)
        self.parcel_based_lbl1.setGeometry(QtCore.QRect(10, 30, 131, 16))
        self.parcel_based_lbl1.setText(QtGui.QApplication.translate("TechImplement_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-style:italic;\">Lot Scale</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.parcel_based_lbl1.setObjectName(_fromUtf8("parcel_based_lbl1"))
        self.parcel_based_lbl4 = QtGui.QLabel(self.parcel_based_group)
        self.parcel_based_lbl4.setGeometry(QtCore.QRect(20, 100, 131, 16))
        self.parcel_based_lbl4.setText(QtGui.QApplication.translate("TechImplement_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Implementation dynamic:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.parcel_based_lbl4.setObjectName(_fromUtf8("parcel_based_lbl4"))
        self.parcel_based_lbl6 = QtGui.QLabel(self.parcel_based_group)
        self.parcel_based_lbl6.setGeometry(QtCore.QRect(20, 150, 141, 16))
        self.parcel_based_lbl6.setText(QtGui.QApplication.translate("TechImplement_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Implementation dynamic:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.parcel_based_lbl6.setObjectName(_fromUtf8("parcel_based_lbl6"))
        self.parcel_based_lbl3 = QtGui.QLabel(self.parcel_based_group)
        self.parcel_based_lbl3.setGeometry(QtCore.QRect(10, 80, 131, 16))
        self.parcel_based_lbl3.setText(QtGui.QApplication.translate("TechImplement_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-style:italic;\">Street Scale</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.parcel_based_lbl3.setObjectName(_fromUtf8("parcel_based_lbl3"))
        self.parcel_based_lbl2 = QtGui.QLabel(self.parcel_based_group)
        self.parcel_based_lbl2.setGeometry(QtCore.QRect(20, 50, 141, 16))
        self.parcel_based_lbl2.setText(QtGui.QApplication.translate("TechImplement_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Implementation dynamic:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.parcel_based_lbl2.setObjectName(_fromUtf8("parcel_based_lbl2"))
        self.parcel_rule_neigh = QtGui.QComboBox(self.parcel_based_group)
        self.parcel_rule_neigh.setGeometry(QtCore.QRect(180, 150, 211, 16))
        self.parcel_rule_neigh.setObjectName(_fromUtf8("parcel_rule_neigh"))
        self.parcel_rule_neigh.addItem(_fromUtf8(""))
        self.parcel_rule_neigh.setItemText(0, QtGui.QApplication.translate("TechImplement_Dialog", "Gradual (maintaining level of service)", None, QtGui.QApplication.UnicodeUTF8))
        self.parcel_rule_neigh.addItem(_fromUtf8(""))
        self.parcel_rule_neigh.setItemText(1, QtGui.QApplication.translate("TechImplement_Dialog", "Immediate (all at once where possible)", None, QtGui.QApplication.UnicodeUTF8))
        self.parcel_rule_neigh.addItem(_fromUtf8(""))
        self.parcel_rule_neigh.setItemText(2, QtGui.QApplication.translate("TechImplement_Dialog", "Delayed (slowed implementation)", None, QtGui.QApplication.UnicodeUTF8))
        self.parcel_rule_street = QtGui.QComboBox(self.parcel_based_group)
        self.parcel_rule_street.setGeometry(QtCore.QRect(180, 100, 211, 16))
        self.parcel_rule_street.setObjectName(_fromUtf8("parcel_rule_street"))
        self.parcel_rule_street.addItem(_fromUtf8(""))
        self.parcel_rule_street.setItemText(0, QtGui.QApplication.translate("TechImplement_Dialog", "Gradual (maintaining level of service)", None, QtGui.QApplication.UnicodeUTF8))
        self.parcel_rule_street.addItem(_fromUtf8(""))
        self.parcel_rule_street.setItemText(1, QtGui.QApplication.translate("TechImplement_Dialog", "Immediate (all at once where possible)", None, QtGui.QApplication.UnicodeUTF8))
        self.parcel_rule_street.addItem(_fromUtf8(""))
        self.parcel_rule_street.setItemText(2, QtGui.QApplication.translate("TechImplement_Dialog", "Delayed (slowed implementation)", None, QtGui.QApplication.UnicodeUTF8))
        self.parcel_rule_neigh_check = QtGui.QCheckBox(self.parcel_based_group)
        self.parcel_rule_neigh_check.setGeometry(QtCore.QRect(20, 180, 331, 17))
        self.parcel_rule_neigh_check.setText(QtGui.QApplication.translate("TechImplement_Dialog", "Implement even if allocated area has not yet been zoned", None, QtGui.QApplication.UnicodeUTF8))
        self.parcel_rule_neigh_check.setObjectName(_fromUtf8("parcel_rule_neigh_check"))
        self.parcel_rule_lot = QtGui.QComboBox(self.parcel_based_group)
        self.parcel_rule_lot.setGeometry(QtCore.QRect(180, 50, 211, 16))
        self.parcel_rule_lot.setObjectName(_fromUtf8("parcel_rule_lot"))
        self.parcel_rule_lot.addItem(_fromUtf8(""))
        self.parcel_rule_lot.setItemText(0, QtGui.QApplication.translate("TechImplement_Dialog", "Gradual (maintaining level of service)", None, QtGui.QApplication.UnicodeUTF8))
        self.parcel_rule_lot.addItem(_fromUtf8(""))
        self.parcel_rule_lot.setItemText(1, QtGui.QApplication.translate("TechImplement_Dialog", "Immediate (all at once where possible)", None, QtGui.QApplication.UnicodeUTF8))
        self.parcel_rule_lot.addItem(_fromUtf8(""))
        self.parcel_rule_lot.setItemText(2, QtGui.QApplication.translate("TechImplement_Dialog", "Delayed (slowed implementation)", None, QtGui.QApplication.UnicodeUTF8))
        self.horizontalLayout_3.addWidget(self.parcel_based_group)
        self.implementdynamic_stack.addWidget(self.parcel_based)
        self.verticalLayout_5.addWidget(self.blockimplement_widget)
        self.prec_impl_title = QtGui.QLabel(self.design_crit_inputs_widget)
        self.prec_impl_title.setMinimumSize(QtCore.QSize(0, 16))
        self.prec_impl_title.setMaximumSize(QtCore.QSize(16777215, 16))
        self.prec_impl_title.setText(QtGui.QApplication.translate("TechImplement_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Precinct-scale Implementation</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.prec_impl_title.setObjectName(_fromUtf8("prec_impl_title"))
        self.verticalLayout_5.addWidget(self.prec_impl_title)
        self.precinct_implement_widget = QtGui.QWidget(self.design_crit_inputs_widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(190)
        sizePolicy.setHeightForWidth(self.precinct_implement_widget.sizePolicy().hasHeightForWidth())
        self.precinct_implement_widget.setSizePolicy(sizePolicy)
        self.precinct_implement_widget.setMinimumSize(QtCore.QSize(0, 100))
        self.precinct_implement_widget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.precinct_implement_widget.setObjectName(_fromUtf8("precinct_implement_widget"))
        self.prec_impl_lbl = QtGui.QLabel(self.precinct_implement_widget)
        self.prec_impl_lbl.setGeometry(QtCore.QRect(20, 10, 171, 16))
        self.prec_impl_lbl.setText(QtGui.QApplication.translate("TechImplement_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Choose implementation dynamic:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.prec_impl_lbl.setObjectName(_fromUtf8("prec_impl_lbl"))
        self.prec_impl_rule = QtGui.QComboBox(self.precinct_implement_widget)
        self.prec_impl_rule.setGeometry(QtCore.QRect(210, 10, 211, 16))
        self.prec_impl_rule.setObjectName(_fromUtf8("prec_impl_rule"))
        self.prec_impl_rule.addItem(_fromUtf8(""))
        self.prec_impl_rule.setItemText(0, QtGui.QApplication.translate("TechImplement_Dialog", "Gradual (maintaining level of service)", None, QtGui.QApplication.UnicodeUTF8))
        self.prec_impl_rule.addItem(_fromUtf8(""))
        self.prec_impl_rule.setItemText(1, QtGui.QApplication.translate("TechImplement_Dialog", "Immediate (all at once where possible)", None, QtGui.QApplication.UnicodeUTF8))
        self.prec_impl_rule.addItem(_fromUtf8(""))
        self.prec_impl_rule.setItemText(2, QtGui.QApplication.translate("TechImplement_Dialog", "Delayed (slowed implementation)", None, QtGui.QApplication.UnicodeUTF8))
        self.prec_impl_force_check = QtGui.QCheckBox(self.precinct_implement_widget)
        self.prec_impl_force_check.setGeometry(QtCore.QRect(20, 40, 331, 17))
        self.prec_impl_force_check.setText(QtGui.QApplication.translate("TechImplement_Dialog", "Implement even if allocated area has not yet been zoned", None, QtGui.QApplication.UnicodeUTF8))
        self.prec_impl_force_check.setObjectName(_fromUtf8("prec_impl_force_check"))
        self.prec_impl_thresh_check = QtGui.QCheckBox(self.precinct_implement_widget)
        self.prec_impl_thresh_check.setGeometry(QtCore.QRect(20, 70, 321, 17))
        self.prec_impl_thresh_check.setText(QtGui.QApplication.translate("TechImplement_Dialog", "Allow implementation if upstream development > % threshold", None, QtGui.QApplication.UnicodeUTF8))
        self.prec_impl_thresh_check.setObjectName(_fromUtf8("prec_impl_thresh_check"))
        self.prec_impl_thresh_spin = QtGui.QSpinBox(self.precinct_implement_widget)
        self.prec_impl_thresh_spin.setGeometry(QtCore.QRect(350, 70, 61, 16))
        self.prec_impl_thresh_spin.setSuffix(QtGui.QApplication.translate("TechImplement_Dialog", "%", None, QtGui.QApplication.UnicodeUTF8))
        self.prec_impl_thresh_spin.setMaximum(100)
        self.prec_impl_thresh_spin.setObjectName(_fromUtf8("prec_impl_thresh_spin"))
        self.verticalLayout_5.addWidget(self.precinct_implement_widget)
        self.techimplement_inputs.setWidget(self.design_crit_inputs_widget)
        self.gridLayout_22.addWidget(self.techimplement_inputs, 0, 0, 2, 2)
        self.horizontalLayout_4.addWidget(self.techimplement_widget)
        self.implement_sidebar = QtGui.QFrame(self.DesignCriteria)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.implement_sidebar.sizePolicy().hasHeightForWidth())
        self.implement_sidebar.setSizePolicy(sizePolicy)
        self.implement_sidebar.setMinimumSize(QtCore.QSize(221, 0))
        self.implement_sidebar.setMaximumSize(QtCore.QSize(221, 16777215))
        self.implement_sidebar.setFrameShape(QtGui.QFrame.StyledPanel)
        self.implement_sidebar.setFrameShadow(QtGui.QFrame.Raised)
        self.implement_sidebar.setObjectName(_fromUtf8("implement_sidebar"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.implement_sidebar)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.implement_sidebar_img = QtGui.QLabel(self.implement_sidebar)
        self.implement_sidebar_img.setMinimumSize(QtCore.QSize(0, 145))
        self.implement_sidebar_img.setText(_fromUtf8(""))
        self.implement_sidebar_img.setPixmap(QtGui.QPixmap(_fromUtf8(":/techplacement/D4W-wsudimplement.png")))
        self.implement_sidebar_img.setObjectName(_fromUtf8("implement_sidebar_img"))
        self.verticalLayout_3.addWidget(self.implement_sidebar_img)
        self.implement_sidebar_descr = QtGui.QTextBrowser(self.implement_sidebar)
        self.implement_sidebar_descr.setHtml(QtGui.QApplication.translate("TechImplement_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Adust dynamics settings for technology implementation. Set different rules for various scales and determine driving forces behind system implementation.</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.implement_sidebar_descr.setObjectName(_fromUtf8("implement_sidebar_descr"))
        self.verticalLayout_3.addWidget(self.implement_sidebar_descr)
        self.horizontalLayout_4.addWidget(self.implement_sidebar)
        self.techimplement_input.addTab(self.DesignCriteria, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.tab)
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.techimplement_widget_2 = QtGui.QWidget(self.tab)
        self.techimplement_widget_2.setObjectName(_fromUtf8("techimplement_widget_2"))
        self.gridLayout_23 = QtGui.QGridLayout(self.techimplement_widget_2)
        self.gridLayout_23.setMargin(0)
        self.gridLayout_23.setObjectName(_fromUtf8("gridLayout_23"))
        self.techimplement_inputs_2 = QtGui.QScrollArea(self.techimplement_widget_2)
        self.techimplement_inputs_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.techimplement_inputs_2.setWidgetResizable(True)
        self.techimplement_inputs_2.setObjectName(_fromUtf8("techimplement_inputs_2"))
        self.design_crit_inputs_widget_2 = QtGui.QWidget()
        self.design_crit_inputs_widget_2.setGeometry(QtCore.QRect(0, 0, 465, 416))
        self.design_crit_inputs_widget_2.setObjectName(_fromUtf8("design_crit_inputs_widget_2"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.design_crit_inputs_widget_2)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.driver_title_3 = QtGui.QLabel(self.design_crit_inputs_widget_2)
        self.driver_title_3.setMinimumSize(QtCore.QSize(0, 16))
        self.driver_title_3.setMaximumSize(QtCore.QSize(16777215, 16))
        self.driver_title_3.setWhatsThis(QtGui.QApplication.translate("TechImplement_Dialog", "Select what design goals to consider and what priority they take over each other. Highest priority (1) and Lowest priority (3) influence technology\'s chance of being implemented. Note that equal priority can be set as well, in which case no one design rationale is more important than the other.", None, QtGui.QApplication.UnicodeUTF8))
        self.driver_title_3.setText(QtGui.QApplication.translate("TechImplement_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Drivers for Implementation</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.driver_title_3.setObjectName(_fromUtf8("driver_title_3"))
        self.verticalLayout_6.addWidget(self.driver_title_3)
        self.impl_drivers_widget = QtGui.QWidget(self.design_crit_inputs_widget_2)
        self.impl_drivers_widget.setMinimumSize(QtCore.QSize(0, 140))
        self.impl_drivers_widget.setObjectName(_fromUtf8("impl_drivers_widget"))
        self.impl_drivers_lbl1 = QtGui.QLabel(self.impl_drivers_widget)
        self.impl_drivers_lbl1.setGeometry(QtCore.QRect(10, 10, 411, 16))
        self.impl_drivers_lbl1.setText(QtGui.QApplication.translate("TechImplement_Dialog", "Select and customize which drivers will determine if implementation takes place", None, QtGui.QApplication.UnicodeUTF8))
        self.impl_drivers_lbl1.setObjectName(_fromUtf8("impl_drivers_lbl1"))
        self.peoplepref_check = QtGui.QCheckBox(self.impl_drivers_widget)
        self.peoplepref_check.setEnabled(False)
        self.peoplepref_check.setGeometry(QtCore.QRect(30, 40, 131, 17))
        self.peoplepref_check.setText(QtGui.QApplication.translate("TechImplement_Dialog", "People preferences", None, QtGui.QApplication.UnicodeUTF8))
        self.peoplepref_check.setObjectName(_fromUtf8("peoplepref_check"))
        self.legal_check = QtGui.QCheckBox(self.impl_drivers_widget)
        self.legal_check.setEnabled(False)
        self.legal_check.setGeometry(QtCore.QRect(30, 70, 131, 17))
        self.legal_check.setText(QtGui.QApplication.translate("TechImplement_Dialog", "Legal provisions", None, QtGui.QApplication.UnicodeUTF8))
        self.legal_check.setObjectName(_fromUtf8("legal_check"))
        self.establish_check = QtGui.QCheckBox(self.impl_drivers_widget)
        self.establish_check.setEnabled(False)
        self.establish_check.setGeometry(QtCore.QRect(30, 100, 201, 17))
        self.establish_check.setText(QtGui.QApplication.translate("TechImplement_Dialog", "System Establishment Requirements", None, QtGui.QApplication.UnicodeUTF8))
        self.establish_check.setObjectName(_fromUtf8("establish_check"))
        self.verticalLayout_6.addWidget(self.impl_drivers_widget)
        self.techimplement_inputs_2.setWidget(self.design_crit_inputs_widget_2)
        self.gridLayout_23.addWidget(self.techimplement_inputs_2, 0, 0, 2, 2)
        self.horizontalLayout_7.addWidget(self.techimplement_widget_2)
        self.implement_sidebar_2 = QtGui.QFrame(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.implement_sidebar_2.sizePolicy().hasHeightForWidth())
        self.implement_sidebar_2.setSizePolicy(sizePolicy)
        self.implement_sidebar_2.setMinimumSize(QtCore.QSize(221, 0))
        self.implement_sidebar_2.setMaximumSize(QtCore.QSize(221, 16777215))
        self.implement_sidebar_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.implement_sidebar_2.setFrameShadow(QtGui.QFrame.Raised)
        self.implement_sidebar_2.setObjectName(_fromUtf8("implement_sidebar_2"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.implement_sidebar_2)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.implement_sidebar_img_2 = QtGui.QLabel(self.implement_sidebar_2)
        self.implement_sidebar_img_2.setMinimumSize(QtCore.QSize(0, 145))
        self.implement_sidebar_img_2.setText(_fromUtf8(""))
        self.implement_sidebar_img_2.setPixmap(QtGui.QPixmap(_fromUtf8(":/techplacement/D4W-wsudimplement.png")))
        self.implement_sidebar_img_2.setObjectName(_fromUtf8("implement_sidebar_img_2"))
        self.verticalLayout_4.addWidget(self.implement_sidebar_img_2)
        self.implement_sidebar_descr_2 = QtGui.QTextBrowser(self.implement_sidebar_2)
        self.implement_sidebar_descr_2.setHtml(QtGui.QApplication.translate("TechImplement_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Set additional rules for the model to consider before making a Yes/No decision on implementing planned technologies in each block.</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.implement_sidebar_descr_2.setObjectName(_fromUtf8("implement_sidebar_descr_2"))
        self.verticalLayout_4.addWidget(self.implement_sidebar_descr_2)
        self.horizontalLayout_7.addWidget(self.implement_sidebar_2)
        self.techimplement_input.addTab(self.tab, _fromUtf8(""))
        self.verticalLayout.addWidget(self.techimplement_input)
        self.techimplement_footer = QtGui.QWidget(TechImplement_Dialog)
        self.techimplement_footer.setMaximumSize(QtCore.QSize(16777215, 38))
        self.techimplement_footer.setObjectName(_fromUtf8("techimplement_footer"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.techimplement_footer)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.remarks = QtGui.QLabel(self.techimplement_footer)
        self.remarks.setText(QtGui.QApplication.translate("TechImplement_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-style:italic;\">UrbanBEATS v1.0 - (C) 2013 Peter M. Bach </span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.remarks.setObjectName(_fromUtf8("remarks"))
        self.horizontalLayout.addWidget(self.remarks)
        self.buttonBox = QtGui.QDialogButtonBox(self.techimplement_footer)
        self.buttonBox.setMaximumSize(QtCore.QSize(16777215, 23))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.horizontalLayout.addWidget(self.buttonBox)
        self.helpButton = QtGui.QPushButton(self.techimplement_footer)
        self.helpButton.setWhatsThis(QtGui.QApplication.translate("TechImplement_Dialog", "Are you serious?", None, QtGui.QApplication.UnicodeUTF8))
        self.helpButton.setText(QtGui.QApplication.translate("TechImplement_Dialog", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.helpButton.setObjectName(_fromUtf8("helpButton"))
        self.horizontalLayout.addWidget(self.helpButton)
        self.verticalLayout.addWidget(self.techimplement_footer)

        self.retranslateUi(TechImplement_Dialog)
        self.techimplement_input.setCurrentIndex(0)
        self.implementdynamic_stack.setCurrentIndex(0)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), TechImplement_Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), TechImplement_Dialog.reject)
        QtCore.QObject.connect(self.implementdynamics_combo, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(int)")), self.implementdynamic_stack.setCurrentIndex)
        QtCore.QMetaObject.connectSlotsByName(TechImplement_Dialog)

    def retranslateUi(self, TechImplement_Dialog):
        self.techimplement_input.setTabText(self.techimplement_input.indexOf(self.DesignCriteria), QtGui.QApplication.translate("TechImplement_Dialog", "Implementation Rules", None, QtGui.QApplication.UnicodeUTF8))
        self.techimplement_input.setTabText(self.techimplement_input.indexOf(self.tab), QtGui.QApplication.translate("TechImplement_Dialog", "Drivers for Implementation", None, QtGui.QApplication.UnicodeUTF8))

import dialogimg_rc
import dialogimg_rc
