# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'md_perfassessgui.ui'
#
# Created: Mon Apr 20 10:00:38 2015
#      by: PyQt4 UI code generator 4.9.6
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

class Ui_Perfconfig_Dialog(object):
    def setupUi(self, Perfconfig_Dialog):
        Perfconfig_Dialog.setObjectName(_fromUtf8("Perfconfig_Dialog"))
        Perfconfig_Dialog.resize(670, 460)
        self.verticalLayout = QtGui.QVBoxLayout(Perfconfig_Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.title_frame = QtGui.QFrame(Perfconfig_Dialog)
        self.title_frame.setMinimumSize(QtCore.QSize(0, 50))
        self.title_frame.setMaximumSize(QtCore.QSize(16777215, 50))
        self.title_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.title_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.title_frame.setObjectName(_fromUtf8("title_frame"))
        self.prepPA_subheading = QtGui.QLabel(self.title_frame)
        self.prepPA_subheading.setGeometry(QtCore.QRect(50, 25, 741, 16))
        self.prepPA_subheading.setObjectName(_fromUtf8("prepPA_subheading"))
        self.prepPA_heading = QtGui.QLabel(self.title_frame)
        self.prepPA_heading.setGeometry(QtCore.QRect(50, 5, 451, 21))
        self.prepPA_heading.setObjectName(_fromUtf8("prepPA_heading"))
        self.label = QtGui.QLabel(self.title_frame)
        self.label.setGeometry(QtCore.QRect(0, 0, 50, 50))
        self.label.setMinimumSize(QtCore.QSize(50, 50))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8(":/images/images/D4W-logoBPM.png")))
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.title_frame)
        self.main_input_widget = QtGui.QTabWidget(Perfconfig_Dialog)
        self.main_input_widget.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_input_widget.sizePolicy().hasHeightForWidth())
        self.main_input_widget.setSizePolicy(sizePolicy)
        self.main_input_widget.setObjectName(_fromUtf8("main_input_widget"))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.tab_2)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.general_params_3 = QtGui.QWidget(self.tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.general_params_3.sizePolicy().hasHeightForWidth())
        self.general_params_3.setSizePolicy(sizePolicy)
        self.general_params_3.setMinimumSize(QtCore.QSize(0, 0))
        self.general_params_3.setObjectName(_fromUtf8("general_params_3"))
        self.verticalLayout_17 = QtGui.QVBoxLayout(self.general_params_3)
        self.verticalLayout_17.setMargin(0)
        self.verticalLayout_17.setObjectName(_fromUtf8("verticalLayout_17"))
        self.scrollArea_9 = QtGui.QScrollArea(self.general_params_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea_9.sizePolicy().hasHeightForWidth())
        self.scrollArea_9.setSizePolicy(sizePolicy)
        self.scrollArea_9.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea_9.setWidgetResizable(True)
        self.scrollArea_9.setObjectName(_fromUtf8("scrollArea_9"))
        self.scrollAreaWidgetContents_9 = QtGui.QWidget()
        self.scrollAreaWidgetContents_9.setGeometry(QtCore.QRect(0, 0, 463, 383))
        self.scrollAreaWidgetContents_9.setObjectName(_fromUtf8("scrollAreaWidgetContents_9"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents_9)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.musicsimconfig_lbl_3 = QtGui.QLabel(self.scrollAreaWidgetContents_9)
        self.musicsimconfig_lbl_3.setMinimumSize(QtCore.QSize(445, 16))
        self.musicsimconfig_lbl_3.setMaximumSize(QtCore.QSize(16777215, 16))
        self.musicsimconfig_lbl_3.setObjectName(_fromUtf8("musicsimconfig_lbl_3"))
        self.verticalLayout_2.addWidget(self.musicsimconfig_lbl_3)
        self.widget = QtGui.QWidget(self.scrollAreaWidgetContents_9)
        self.widget.setMinimumSize(QtCore.QSize(0, 85))
        self.widget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.select_pc = QtGui.QRadioButton(self.widget)
        self.select_pc.setGeometry(QtCore.QRect(60, 10, 351, 21))
        self.select_pc.setObjectName(_fromUtf8("select_pc"))
        self.pushButton_2 = QtGui.QPushButton(self.widget)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 5, 31, 31))
        self.pushButton_2.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/images/cycle_planning_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_2.setFlat(True)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(self.widget)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 45, 31, 31))
        self.pushButton_3.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/images/cycle_implement_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon1)
        self.pushButton_3.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_3.setFlat(True)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.select_ic = QtGui.QRadioButton(self.widget)
        self.select_ic.setGeometry(QtCore.QRect(60, 50, 351, 21))
        self.select_ic.setObjectName(_fromUtf8("select_ic"))
        self.verticalLayout_2.addWidget(self.widget)
        self.musicsimconfig_lbl_2 = QtGui.QLabel(self.scrollAreaWidgetContents_9)
        self.musicsimconfig_lbl_2.setMinimumSize(QtCore.QSize(445, 16))
        self.musicsimconfig_lbl_2.setMaximumSize(QtCore.QSize(16777215, 16))
        self.musicsimconfig_lbl_2.setObjectName(_fromUtf8("musicsimconfig_lbl_2"))
        self.verticalLayout_2.addWidget(self.musicsimconfig_lbl_2)
        self.simulationconfig_widget_3 = QtGui.QWidget(self.scrollAreaWidgetContents_9)
        self.simulationconfig_widget_3.setMinimumSize(QtCore.QSize(0, 230))
        self.simulationconfig_widget_3.setObjectName(_fromUtf8("simulationconfig_widget_3"))
        self.perf_MUSIC = QtGui.QCheckBox(self.simulationconfig_widget_3)
        self.perf_MUSIC.setGeometry(QtCore.QRect(60, 20, 361, 17))
        self.perf_MUSIC.setObjectName(_fromUtf8("perf_MUSIC"))
        self.perf_Economics = QtGui.QCheckBox(self.simulationconfig_widget_3)
        self.perf_Economics.setGeometry(QtCore.QRect(60, 60, 361, 17))
        self.perf_Economics.setObjectName(_fromUtf8("perf_Economics"))
        self.perf_Microclimate = QtGui.QCheckBox(self.simulationconfig_widget_3)
        self.perf_Microclimate.setGeometry(QtCore.QRect(60, 100, 361, 17))
        self.perf_Microclimate.setObjectName(_fromUtf8("perf_Microclimate"))
        self.perf_EPANET = QtGui.QCheckBox(self.simulationconfig_widget_3)
        self.perf_EPANET.setEnabled(True)
        self.perf_EPANET.setGeometry(QtCore.QRect(60, 140, 291, 17))
        self.perf_EPANET.setObjectName(_fromUtf8("perf_EPANET"))
        self.perf_CD3 = QtGui.QCheckBox(self.simulationconfig_widget_3)
        self.perf_CD3.setEnabled(False)
        self.perf_CD3.setGeometry(QtCore.QRect(60, 180, 291, 17))
        self.perf_CD3.setObjectName(_fromUtf8("perf_CD3"))
        self.label_2 = QtGui.QLabel(self.simulationconfig_widget_3)
        self.label_2.setGeometry(QtCore.QRect(15, 95, 31, 31))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8(":/guitoolbaricons/thermo.png")))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.simulationconfig_widget_3)
        self.label_3.setGeometry(QtCore.QRect(15, 55, 31, 31))
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setPixmap(QtGui.QPixmap(_fromUtf8(":/guitoolbaricons/outputs.png")))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.simulationconfig_widget_3)
        self.label_4.setGeometry(QtCore.QRect(15, 15, 31, 31))
        self.label_4.setText(_fromUtf8(""))
        self.label_4.setPixmap(QtGui.QPixmap(_fromUtf8(":/guitoolbaricons/climatedata.png")))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.simulationconfig_widget_3)
        self.label_5.setGeometry(QtCore.QRect(15, 135, 31, 31))
        self.label_5.setText(_fromUtf8(""))
        self.label_5.setPixmap(QtGui.QPixmap(_fromUtf8(":/guitoolbaricons/disperse.png")))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.simulationconfig_widget_3)
        self.label_6.setGeometry(QtCore.QRect(15, 175, 31, 31))
        self.label_6.setText(_fromUtf8(""))
        self.label_6.setPixmap(QtGui.QPixmap(_fromUtf8(":/guitoolbaricons/world.png")))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout_2.addWidget(self.simulationconfig_widget_3)
        self.scrollArea_9.setWidget(self.scrollAreaWidgetContents_9)
        self.verticalLayout_17.addWidget(self.scrollArea_9)
        self.horizontalLayout_2.addWidget(self.general_params_3)
        self.general_sidebar_3 = QtGui.QWidget(self.tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.general_sidebar_3.sizePolicy().hasHeightForWidth())
        self.general_sidebar_3.setSizePolicy(sizePolicy)
        self.general_sidebar_3.setMinimumSize(QtCore.QSize(0, 0))
        self.general_sidebar_3.setMaximumSize(QtCore.QSize(122, 16777215))
        self.general_sidebar_3.setObjectName(_fromUtf8("general_sidebar_3"))
        self.verticalLayout_10 = QtGui.QVBoxLayout(self.general_sidebar_3)
        self.verticalLayout_10.setMargin(0)
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.general_img_3 = QtGui.QLabel(self.general_sidebar_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.general_img_3.sizePolicy().hasHeightForWidth())
        self.general_img_3.setSizePolicy(sizePolicy)
        self.general_img_3.setMinimumSize(QtCore.QSize(0, 0))
        self.general_img_3.setMaximumSize(QtCore.QSize(104, 145))
        self.general_img_3.setText(_fromUtf8(""))
        self.general_img_3.setPixmap(QtGui.QPixmap(_fromUtf8(":/images/images/D4W_ppa_general.png")))
        self.general_img_3.setObjectName(_fromUtf8("general_img_3"))
        self.verticalLayout_10.addWidget(self.general_img_3)
        self.general_descr_3 = QtGui.QTextBrowser(self.general_sidebar_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.general_descr_3.sizePolicy().hasHeightForWidth())
        self.general_descr_3.setSizePolicy(sizePolicy)
        self.general_descr_3.setMinimumSize(QtCore.QSize(104, 0))
        self.general_descr_3.setMaximumSize(QtCore.QSize(104, 16777215))
        self.general_descr_3.setObjectName(_fromUtf8("general_descr_3"))
        self.verticalLayout_10.addWidget(self.general_descr_3)
        self.horizontalLayout_2.addWidget(self.general_sidebar_3)
        self.main_input_widget.addTab(self.tab_2, _fromUtf8(""))
        self.generaltab = QtGui.QWidget()
        self.generaltab.setObjectName(_fromUtf8("generaltab"))
        self.horizontalLayout_9 = QtGui.QHBoxLayout(self.generaltab)
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.general_params = QtGui.QWidget(self.generaltab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.general_params.sizePolicy().hasHeightForWidth())
        self.general_params.setSizePolicy(sizePolicy)
        self.general_params.setMinimumSize(QtCore.QSize(0, 0))
        self.general_params.setObjectName(_fromUtf8("general_params"))
        self.verticalLayout_15 = QtGui.QVBoxLayout(self.general_params)
        self.verticalLayout_15.setMargin(0)
        self.verticalLayout_15.setObjectName(_fromUtf8("verticalLayout_15"))
        self.scrollArea_7 = QtGui.QScrollArea(self.general_params)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea_7.sizePolicy().hasHeightForWidth())
        self.scrollArea_7.setSizePolicy(sizePolicy)
        self.scrollArea_7.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea_7.setWidgetResizable(True)
        self.scrollArea_7.setObjectName(_fromUtf8("scrollArea_7"))
        self.scrollAreaWidgetContents_7 = QtGui.QWidget()
        self.scrollAreaWidgetContents_7.setGeometry(QtCore.QRect(0, 0, 463, 764))
        self.scrollAreaWidgetContents_7.setObjectName(_fromUtf8("scrollAreaWidgetContents_7"))
        self.verticalLayout_12 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents_7)
        self.verticalLayout_12.setObjectName(_fromUtf8("verticalLayout_12"))
        self.musicsimconfig_lbl = QtGui.QLabel(self.scrollAreaWidgetContents_7)
        self.musicsimconfig_lbl.setMinimumSize(QtCore.QSize(445, 16))
        self.musicsimconfig_lbl.setMaximumSize(QtCore.QSize(16777215, 16))
        self.musicsimconfig_lbl.setObjectName(_fromUtf8("musicsimconfig_lbl"))
        self.verticalLayout_12.addWidget(self.musicsimconfig_lbl)
        self.simulationconfig_widget = QtGui.QWidget(self.scrollAreaWidgetContents_7)
        self.simulationconfig_widget.setMinimumSize(QtCore.QSize(0, 100))
        self.simulationconfig_widget.setObjectName(_fromUtf8("simulationconfig_widget"))
        self.musicsplit_check = QtGui.QCheckBox(self.simulationconfig_widget)
        self.musicsplit_check.setGeometry(QtCore.QRect(10, 70, 381, 17))
        self.musicsplit_check.setObjectName(_fromUtf8("musicsplit_check"))
        self.music_browse_pathbox = QtGui.QLineEdit(self.simulationconfig_widget)
        self.music_browse_pathbox.setGeometry(QtCore.QRect(130, 40, 201, 20))
        self.music_browse_pathbox.setObjectName(_fromUtf8("music_browse_pathbox"))
        self.music_browse_lbl = QtGui.QLabel(self.simulationconfig_widget)
        self.music_browse_lbl.setGeometry(QtCore.QRect(10, 40, 111, 20))
        self.music_browse_lbl.setObjectName(_fromUtf8("music_browse_lbl"))
        self.music_browse_button = QtGui.QToolButton(self.simulationconfig_widget)
        self.music_browse_button.setGeometry(QtCore.QRect(340, 40, 61, 19))
        self.music_browse_button.setObjectName(_fromUtf8("music_browse_button"))
        self.music_version = QtGui.QLabel(self.simulationconfig_widget)
        self.music_version.setGeometry(QtCore.QRect(10, 10, 121, 20))
        self.music_version.setObjectName(_fromUtf8("music_version"))
        self.music_version_combo = QtGui.QComboBox(self.simulationconfig_widget)
        self.music_version_combo.setGeometry(QtCore.QRect(130, 10, 201, 21))
        self.music_version_combo.setObjectName(_fromUtf8("music_version_combo"))
        self.music_version_combo.addItem(_fromUtf8(""))
        self.music_version_combo.addItem(_fromUtf8(""))
        self.verticalLayout_12.addWidget(self.simulationconfig_widget)
        self.musiccatchment_lbl = QtGui.QLabel(self.scrollAreaWidgetContents_7)
        self.musiccatchment_lbl.setMinimumSize(QtCore.QSize(445, 16))
        self.musiccatchment_lbl.setMaximumSize(QtCore.QSize(16777215, 16))
        self.musiccatchment_lbl.setObjectName(_fromUtf8("musiccatchment_lbl"))
        self.verticalLayout_12.addWidget(self.musiccatchment_lbl)
        self.musiccatchment_widget = QtGui.QWidget(self.scrollAreaWidgetContents_7)
        self.musiccatchment_widget.setMinimumSize(QtCore.QSize(0, 300))
        self.musiccatchment_widget.setObjectName(_fromUtf8("musiccatchment_widget"))
        self.rnr_params_lbl = QtGui.QLabel(self.musiccatchment_widget)
        self.rnr_params_lbl.setGeometry(QtCore.QRect(30, 35, 151, 20))
        self.rnr_params_lbl.setObjectName(_fromUtf8("rnr_params_lbl"))
        self.musicRR_soil_box = QtGui.QLineEdit(self.musiccatchment_widget)
        self.musicRR_soil_box.setGeometry(QtCore.QRect(270, 60, 61, 20))
        self.musicRR_soil_box.setObjectName(_fromUtf8("musicRR_soil_box"))
        self.musicRR_soil_lbl = QtGui.QLabel(self.musiccatchment_widget)
        self.musicRR_soil_lbl.setGeometry(QtCore.QRect(50, 60, 141, 20))
        self.musicRR_soil_lbl.setObjectName(_fromUtf8("musicRR_soil_lbl"))
        self.musicRR_field_lbl = QtGui.QLabel(self.musiccatchment_widget)
        self.musicRR_field_lbl.setGeometry(QtCore.QRect(50, 85, 161, 20))
        self.musicRR_field_lbl.setObjectName(_fromUtf8("musicRR_field_lbl"))
        self.musicRR_field_box = QtGui.QLineEdit(self.musiccatchment_widget)
        self.musicRR_field_box.setGeometry(QtCore.QRect(270, 85, 61, 20))
        self.musicRR_field_box.setObjectName(_fromUtf8("musicRR_field_box"))
        self.include_pervious = QtGui.QCheckBox(self.musiccatchment_widget)
        self.include_pervious.setGeometry(QtCore.QRect(10, 10, 411, 17))
        self.include_pervious.setObjectName(_fromUtf8("include_pervious"))
        self.musicRR_bfr_lbl = QtGui.QLabel(self.musiccatchment_widget)
        self.musicRR_bfr_lbl.setGeometry(QtCore.QRect(50, 110, 161, 20))
        self.musicRR_bfr_lbl.setObjectName(_fromUtf8("musicRR_bfr_lbl"))
        self.musicRR_rcr_lbl = QtGui.QLabel(self.musiccatchment_widget)
        self.musicRR_rcr_lbl.setGeometry(QtCore.QRect(50, 135, 161, 20))
        self.musicRR_rcr_lbl.setObjectName(_fromUtf8("musicRR_rcr_lbl"))
        self.musicRR_dsr_lbl = QtGui.QLabel(self.musiccatchment_widget)
        self.musicRR_dsr_lbl.setGeometry(QtCore.QRect(50, 160, 161, 20))
        self.musicRR_dsr_lbl.setObjectName(_fromUtf8("musicRR_dsr_lbl"))
        self.musicRR_bfr_spin = QtGui.QDoubleSpinBox(self.musiccatchment_widget)
        self.musicRR_bfr_spin.setGeometry(QtCore.QRect(270, 110, 62, 16))
        self.musicRR_bfr_spin.setDecimals(1)
        self.musicRR_bfr_spin.setMaximum(100.0)
        self.musicRR_bfr_spin.setProperty("value", 5.0)
        self.musicRR_bfr_spin.setObjectName(_fromUtf8("musicRR_bfr_spin"))
        self.musicRR_rcr_spin = QtGui.QDoubleSpinBox(self.musiccatchment_widget)
        self.musicRR_rcr_spin.setGeometry(QtCore.QRect(270, 135, 62, 16))
        self.musicRR_rcr_spin.setDecimals(1)
        self.musicRR_rcr_spin.setObjectName(_fromUtf8("musicRR_rcr_spin"))
        self.musicRR_dsr_spin = QtGui.QDoubleSpinBox(self.musiccatchment_widget)
        self.musicRR_dsr_spin.setGeometry(QtCore.QRect(270, 160, 62, 16))
        self.musicRR_dsr_spin.setDecimals(1)
        self.musicRR_dsr_spin.setObjectName(_fromUtf8("musicRR_dsr_spin"))
        self.include_route = QtGui.QCheckBox(self.musiccatchment_widget)
        self.include_route.setGeometry(QtCore.QRect(10, 190, 411, 17))
        self.include_route.setObjectName(_fromUtf8("include_route"))
        self.musicRR_musk_lbl1 = QtGui.QLabel(self.musiccatchment_widget)
        self.musicRR_musk_lbl1.setGeometry(QtCore.QRect(50, 210, 191, 20))
        self.musicRR_musk_lbl1.setObjectName(_fromUtf8("musicRR_musk_lbl1"))
        self.musicRR_muskk_auto = QtGui.QRadioButton(self.musiccatchment_widget)
        self.musicRR_muskk_auto.setGeometry(QtCore.QRect(80, 230, 141, 17))
        self.musicRR_muskk_auto.setObjectName(_fromUtf8("musicRR_muskk_auto"))
        self.musicRR_muskk_custom = QtGui.QRadioButton(self.musiccatchment_widget)
        self.musicRR_muskk_custom.setGeometry(QtCore.QRect(80, 250, 91, 17))
        self.musicRR_muskk_custom.setObjectName(_fromUtf8("musicRR_muskk_custom"))
        self.musicRR_musktheta_lbl = QtGui.QLabel(self.musiccatchment_widget)
        self.musicRR_musktheta_lbl.setGeometry(QtCore.QRect(50, 270, 191, 20))
        self.musicRR_musktheta_lbl.setObjectName(_fromUtf8("musicRR_musktheta_lbl"))
        self.musicRR_musk_lbl2 = QtGui.QLabel(self.musiccatchment_widget)
        self.musicRR_musk_lbl2.setGeometry(QtCore.QRect(340, 250, 81, 20))
        self.musicRR_musk_lbl2.setObjectName(_fromUtf8("musicRR_musk_lbl2"))
        self.musicRR_muskk_spin = QtGui.QSpinBox(self.musiccatchment_widget)
        self.musicRR_muskk_spin.setGeometry(QtCore.QRect(270, 250, 61, 16))
        self.musicRR_muskk_spin.setMinimum(3)
        self.musicRR_muskk_spin.setMaximum(500)
        self.musicRR_muskk_spin.setObjectName(_fromUtf8("musicRR_muskk_spin"))
        self.musicRR_musktheta_spin = QtGui.QDoubleSpinBox(self.musiccatchment_widget)
        self.musicRR_musktheta_spin.setGeometry(QtCore.QRect(270, 270, 62, 16))
        self.musicRR_musktheta_spin.setMinimum(0.1)
        self.musicRR_musktheta_spin.setMaximum(0.49)
        self.musicRR_musktheta_spin.setSingleStep(0.01)
        self.musicRR_musktheta_spin.setObjectName(_fromUtf8("musicRR_musktheta_spin"))
        self.verticalLayout_12.addWidget(self.musiccatchment_widget)
        self.musicwsudsetup_lbl = QtGui.QLabel(self.scrollAreaWidgetContents_7)
        self.musicwsudsetup_lbl.setMinimumSize(QtCore.QSize(445, 16))
        self.musicwsudsetup_lbl.setMaximumSize(QtCore.QSize(16777215, 16))
        self.musicwsudsetup_lbl.setObjectName(_fromUtf8("musicwsudsetup_lbl"))
        self.verticalLayout_12.addWidget(self.musicwsudsetup_lbl)
        self.simulationconfig_widget_2 = QtGui.QWidget(self.scrollAreaWidgetContents_7)
        self.simulationconfig_widget_2.setMinimumSize(QtCore.QSize(0, 90))
        self.simulationconfig_widget_2.setObjectName(_fromUtf8("simulationconfig_widget_2"))
        self.musicBF_params = QtGui.QLabel(self.simulationconfig_widget_2)
        self.musicBF_params.setGeometry(QtCore.QRect(10, 5, 151, 20))
        self.musicBF_params.setObjectName(_fromUtf8("musicBF_params"))
        self.musicBF_TN_box = QtGui.QLineEdit(self.simulationconfig_widget_2)
        self.musicBF_TN_box.setGeometry(QtCore.QRect(270, 30, 61, 20))
        self.musicBF_TN_box.setObjectName(_fromUtf8("musicBF_TN_box"))
        self.musicBF_TN_lbl = QtGui.QLabel(self.simulationconfig_widget_2)
        self.musicBF_TN_lbl.setGeometry(QtCore.QRect(30, 30, 181, 20))
        self.musicBF_TN_lbl.setObjectName(_fromUtf8("musicBF_TN_lbl"))
        self.musicBF_ortho_lbl = QtGui.QLabel(self.simulationconfig_widget_2)
        self.musicBF_ortho_lbl.setGeometry(QtCore.QRect(30, 55, 241, 20))
        self.musicBF_ortho_lbl.setObjectName(_fromUtf8("musicBF_ortho_lbl"))
        self.musicBF_ortho_box = QtGui.QLineEdit(self.simulationconfig_widget_2)
        self.musicBF_ortho_box.setGeometry(QtCore.QRect(270, 55, 61, 20))
        self.musicBF_ortho_box.setObjectName(_fromUtf8("musicBF_ortho_box"))
        self.verticalLayout_12.addWidget(self.simulationconfig_widget_2)
        self.musicwsudsetup_lbl_2 = QtGui.QLabel(self.scrollAreaWidgetContents_7)
        self.musicwsudsetup_lbl_2.setMinimumSize(QtCore.QSize(445, 16))
        self.musicwsudsetup_lbl_2.setMaximumSize(QtCore.QSize(16777215, 16))
        self.musicwsudsetup_lbl_2.setObjectName(_fromUtf8("musicwsudsetup_lbl_2"))
        self.verticalLayout_12.addWidget(self.musicwsudsetup_lbl_2)
        self.simulationconfig_widget_4 = QtGui.QWidget(self.scrollAreaWidgetContents_7)
        self.simulationconfig_widget_4.setMinimumSize(QtCore.QSize(0, 150))
        self.simulationconfig_widget_4.setObjectName(_fromUtf8("simulationconfig_widget_4"))
        self.musicpath_box = QtGui.QLineEdit(self.simulationconfig_widget_4)
        self.musicpath_box.setEnabled(False)
        self.musicpath_box.setGeometry(QtCore.QRect(120, 40, 141, 20))
        self.musicpath_box.setObjectName(_fromUtf8("musicpath_box"))
        self.musicpath_lbl = QtGui.QLabel(self.simulationconfig_widget_4)
        self.musicpath_lbl.setGeometry(QtCore.QRect(10, 40, 111, 16))
        self.musicpath_lbl.setObjectName(_fromUtf8("musicpath_lbl"))
        self.musicpath_browse = QtGui.QPushButton(self.simulationconfig_widget_4)
        self.musicpath_browse.setEnabled(False)
        self.musicpath_browse.setGeometry(QtCore.QRect(270, 40, 61, 23))
        self.musicpath_browse.setObjectName(_fromUtf8("musicpath_browse"))
        self.musicflux_check = QtGui.QCheckBox(self.simulationconfig_widget_4)
        self.musicflux_check.setEnabled(False)
        self.musicflux_check.setGeometry(QtCore.QRect(30, 120, 211, 18))
        self.musicflux_check.setObjectName(_fromUtf8("musicflux_check"))
        self.musicexport_lbl = QtGui.QLabel(self.simulationconfig_widget_4)
        self.musicexport_lbl.setGeometry(QtCore.QRect(10, 70, 141, 16))
        self.musicexport_lbl.setObjectName(_fromUtf8("musicexport_lbl"))
        self.musictte_check = QtGui.QCheckBox(self.simulationconfig_widget_4)
        self.musictte_check.setEnabled(False)
        self.musictte_check.setGeometry(QtCore.QRect(30, 95, 221, 18))
        self.musictte_check.setObjectName(_fromUtf8("musictte_check"))
        self.musicauto_check = QtGui.QCheckBox(self.simulationconfig_widget_4)
        self.musicauto_check.setEnabled(False)
        self.musicauto_check.setGeometry(QtCore.QRect(10, 10, 311, 18))
        self.musicauto_check.setObjectName(_fromUtf8("musicauto_check"))
        self.verticalLayout_12.addWidget(self.simulationconfig_widget_4)
        self.scrollArea_7.setWidget(self.scrollAreaWidgetContents_7)
        self.verticalLayout_15.addWidget(self.scrollArea_7)
        self.horizontalLayout_9.addWidget(self.general_params)
        self.general_sidebar = QtGui.QWidget(self.generaltab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.general_sidebar.sizePolicy().hasHeightForWidth())
        self.general_sidebar.setSizePolicy(sizePolicy)
        self.general_sidebar.setMinimumSize(QtCore.QSize(0, 0))
        self.general_sidebar.setMaximumSize(QtCore.QSize(122, 16777215))
        self.general_sidebar.setObjectName(_fromUtf8("general_sidebar"))
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.general_sidebar)
        self.verticalLayout_8.setMargin(0)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.general_img = QtGui.QLabel(self.general_sidebar)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.general_img.sizePolicy().hasHeightForWidth())
        self.general_img.setSizePolicy(sizePolicy)
        self.general_img.setMinimumSize(QtCore.QSize(0, 0))
        self.general_img.setMaximumSize(QtCore.QSize(104, 145))
        self.general_img.setText(_fromUtf8(""))
        self.general_img.setPixmap(QtGui.QPixmap(_fromUtf8(":/images/images/D4W_ppa_hydrology.png")))
        self.general_img.setObjectName(_fromUtf8("general_img"))
        self.verticalLayout_8.addWidget(self.general_img)
        self.general_descr = QtGui.QTextBrowser(self.general_sidebar)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.general_descr.sizePolicy().hasHeightForWidth())
        self.general_descr.setSizePolicy(sizePolicy)
        self.general_descr.setMinimumSize(QtCore.QSize(104, 0))
        self.general_descr.setMaximumSize(QtCore.QSize(104, 16777215))
        self.general_descr.setObjectName(_fromUtf8("general_descr"))
        self.verticalLayout_8.addWidget(self.general_descr)
        self.horizontalLayout_9.addWidget(self.general_sidebar)
        self.main_input_widget.addTab(self.generaltab, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.tab_4)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.general_params_5 = QtGui.QWidget(self.tab_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.general_params_5.sizePolicy().hasHeightForWidth())
        self.general_params_5.setSizePolicy(sizePolicy)
        self.general_params_5.setMinimumSize(QtCore.QSize(0, 0))
        self.general_params_5.setObjectName(_fromUtf8("general_params_5"))
        self.verticalLayout_20 = QtGui.QVBoxLayout(self.general_params_5)
        self.verticalLayout_20.setMargin(0)
        self.verticalLayout_20.setObjectName(_fromUtf8("verticalLayout_20"))
        self.scrollArea_11 = QtGui.QScrollArea(self.general_params_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea_11.sizePolicy().hasHeightForWidth())
        self.scrollArea_11.setSizePolicy(sizePolicy)
        self.scrollArea_11.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea_11.setWidgetResizable(True)
        self.scrollArea_11.setObjectName(_fromUtf8("scrollArea_11"))
        self.scrollAreaWidgetContents_11 = QtGui.QWidget()
        self.scrollAreaWidgetContents_11.setGeometry(QtCore.QRect(0, 0, 463, 278))
        self.scrollAreaWidgetContents_11.setObjectName(_fromUtf8("scrollAreaWidgetContents_11"))
        self.verticalLayout_21 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents_11)
        self.verticalLayout_21.setObjectName(_fromUtf8("verticalLayout_21"))
        self.lcc_title = QtGui.QLabel(self.scrollAreaWidgetContents_11)
        self.lcc_title.setMinimumSize(QtCore.QSize(445, 16))
        self.lcc_title.setMaximumSize(QtCore.QSize(16777215, 16))
        self.lcc_title.setObjectName(_fromUtf8("lcc_title"))
        self.verticalLayout_21.addWidget(self.lcc_title)
        self.lcc_widget = QtGui.QWidget(self.scrollAreaWidgetContents_11)
        self.lcc_widget.setMinimumSize(QtCore.QSize(0, 100))
        self.lcc_widget.setObjectName(_fromUtf8("lcc_widget"))
        self.comingsoon_4 = QtGui.QLabel(self.lcc_widget)
        self.comingsoon_4.setGeometry(QtCore.QRect(100, 30, 111, 20))
        self.comingsoon_4.setObjectName(_fromUtf8("comingsoon_4"))
        self.verticalLayout_21.addWidget(self.lcc_widget)
        self.market_title = QtGui.QLabel(self.scrollAreaWidgetContents_11)
        self.market_title.setMinimumSize(QtCore.QSize(445, 16))
        self.market_title.setMaximumSize(QtCore.QSize(16777215, 16))
        self.market_title.setObjectName(_fromUtf8("market_title"))
        self.verticalLayout_21.addWidget(self.market_title)
        self.market_widget = QtGui.QWidget(self.scrollAreaWidgetContents_11)
        self.market_widget.setMinimumSize(QtCore.QSize(0, 100))
        self.market_widget.setObjectName(_fromUtf8("market_widget"))
        self.comingsoon_5 = QtGui.QLabel(self.market_widget)
        self.comingsoon_5.setGeometry(QtCore.QRect(90, 40, 111, 20))
        self.comingsoon_5.setObjectName(_fromUtf8("comingsoon_5"))
        self.verticalLayout_21.addWidget(self.market_widget)
        self.scrollArea_11.setWidget(self.scrollAreaWidgetContents_11)
        self.verticalLayout_20.addWidget(self.scrollArea_11)
        self.horizontalLayout_4.addWidget(self.general_params_5)
        self.general_sidebar_5 = QtGui.QWidget(self.tab_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.general_sidebar_5.sizePolicy().hasHeightForWidth())
        self.general_sidebar_5.setSizePolicy(sizePolicy)
        self.general_sidebar_5.setMinimumSize(QtCore.QSize(0, 0))
        self.general_sidebar_5.setMaximumSize(QtCore.QSize(122, 16777215))
        self.general_sidebar_5.setObjectName(_fromUtf8("general_sidebar_5"))
        self.verticalLayout_22 = QtGui.QVBoxLayout(self.general_sidebar_5)
        self.verticalLayout_22.setMargin(0)
        self.verticalLayout_22.setObjectName(_fromUtf8("verticalLayout_22"))
        self.general_img_5 = QtGui.QLabel(self.general_sidebar_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.general_img_5.sizePolicy().hasHeightForWidth())
        self.general_img_5.setSizePolicy(sizePolicy)
        self.general_img_5.setMinimumSize(QtCore.QSize(0, 0))
        self.general_img_5.setMaximumSize(QtCore.QSize(104, 145))
        self.general_img_5.setText(_fromUtf8(""))
        self.general_img_5.setPixmap(QtGui.QPixmap(_fromUtf8(":/images/images/D4W_ppa_economics.png")))
        self.general_img_5.setObjectName(_fromUtf8("general_img_5"))
        self.verticalLayout_22.addWidget(self.general_img_5)
        self.general_descr_5 = QtGui.QTextBrowser(self.general_sidebar_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.general_descr_5.sizePolicy().hasHeightForWidth())
        self.general_descr_5.setSizePolicy(sizePolicy)
        self.general_descr_5.setMinimumSize(QtCore.QSize(104, 0))
        self.general_descr_5.setMaximumSize(QtCore.QSize(104, 16777215))
        self.general_descr_5.setObjectName(_fromUtf8("general_descr_5"))
        self.verticalLayout_22.addWidget(self.general_descr_5)
        self.horizontalLayout_4.addWidget(self.general_sidebar_5)
        self.main_input_widget.addTab(self.tab_4, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.tab)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.general_params_2 = QtGui.QWidget(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.general_params_2.sizePolicy().hasHeightForWidth())
        self.general_params_2.setSizePolicy(sizePolicy)
        self.general_params_2.setMinimumSize(QtCore.QSize(0, 0))
        self.general_params_2.setObjectName(_fromUtf8("general_params_2"))
        self.verticalLayout_16 = QtGui.QVBoxLayout(self.general_params_2)
        self.verticalLayout_16.setMargin(0)
        self.verticalLayout_16.setObjectName(_fromUtf8("verticalLayout_16"))
        self.scrollArea_8 = QtGui.QScrollArea(self.general_params_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea_8.sizePolicy().hasHeightForWidth())
        self.scrollArea_8.setSizePolicy(sizePolicy)
        self.scrollArea_8.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea_8.setWidgetResizable(True)
        self.scrollArea_8.setObjectName(_fromUtf8("scrollArea_8"))
        self.scrollAreaWidgetContents_8 = QtGui.QWidget()
        self.scrollAreaWidgetContents_8.setGeometry(QtCore.QRect(0, 0, 463, 396))
        self.scrollAreaWidgetContents_8.setObjectName(_fromUtf8("scrollAreaWidgetContents_8"))
        self.verticalLayout_13 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents_8)
        self.verticalLayout_13.setObjectName(_fromUtf8("verticalLayout_13"))
        self.lcov_title = QtGui.QLabel(self.scrollAreaWidgetContents_8)
        self.lcov_title.setMinimumSize(QtCore.QSize(445, 16))
        self.lcov_title.setMaximumSize(QtCore.QSize(16777215, 16))
        self.lcov_title.setObjectName(_fromUtf8("lcov_title"))
        self.verticalLayout_13.addWidget(self.lcov_title)
        self.lcov_widget = QtGui.QWidget(self.scrollAreaWidgetContents_8)
        self.lcov_widget.setMinimumSize(QtCore.QSize(0, 100))
        self.lcov_widget.setObjectName(_fromUtf8("lcov_widget"))
        self.comingsoon_3 = QtGui.QLabel(self.lcov_widget)
        self.comingsoon_3.setGeometry(QtCore.QRect(70, 40, 111, 20))
        self.comingsoon_3.setObjectName(_fromUtf8("comingsoon_3"))
        self.verticalLayout_13.addWidget(self.lcov_widget)
        self.lst_title = QtGui.QLabel(self.scrollAreaWidgetContents_8)
        self.lst_title.setMinimumSize(QtCore.QSize(445, 16))
        self.lst_title.setMaximumSize(QtCore.QSize(16777215, 16))
        self.lst_title.setObjectName(_fromUtf8("lst_title"))
        self.verticalLayout_13.addWidget(self.lst_title)
        self.lst_widget = QtGui.QWidget(self.scrollAreaWidgetContents_8)
        self.lst_widget.setMinimumSize(QtCore.QSize(0, 100))
        self.lst_widget.setObjectName(_fromUtf8("lst_widget"))
        self.comingsoon_2 = QtGui.QLabel(self.lst_widget)
        self.comingsoon_2.setGeometry(QtCore.QRect(70, 30, 111, 20))
        self.comingsoon_2.setObjectName(_fromUtf8("comingsoon_2"))
        self.verticalLayout_13.addWidget(self.lst_widget)
        self.lstat_title = QtGui.QLabel(self.scrollAreaWidgetContents_8)
        self.lstat_title.setMinimumSize(QtCore.QSize(445, 16))
        self.lstat_title.setMaximumSize(QtCore.QSize(16777215, 16))
        self.lstat_title.setObjectName(_fromUtf8("lstat_title"))
        self.verticalLayout_13.addWidget(self.lstat_title)
        self.lstat_widget = QtGui.QWidget(self.scrollAreaWidgetContents_8)
        self.lstat_widget.setMinimumSize(QtCore.QSize(0, 100))
        self.lstat_widget.setObjectName(_fromUtf8("lstat_widget"))
        self.comingsoon_1 = QtGui.QLabel(self.lstat_widget)
        self.comingsoon_1.setGeometry(QtCore.QRect(70, 30, 111, 20))
        self.comingsoon_1.setObjectName(_fromUtf8("comingsoon_1"))
        self.verticalLayout_13.addWidget(self.lstat_widget)
        self.scrollArea_8.setWidget(self.scrollAreaWidgetContents_8)
        self.verticalLayout_16.addWidget(self.scrollArea_8)
        self.horizontalLayout.addWidget(self.general_params_2)
        self.general_sidebar_2 = QtGui.QWidget(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.general_sidebar_2.sizePolicy().hasHeightForWidth())
        self.general_sidebar_2.setSizePolicy(sizePolicy)
        self.general_sidebar_2.setMinimumSize(QtCore.QSize(0, 0))
        self.general_sidebar_2.setMaximumSize(QtCore.QSize(122, 16777215))
        self.general_sidebar_2.setObjectName(_fromUtf8("general_sidebar_2"))
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.general_sidebar_2)
        self.verticalLayout_9.setMargin(0)
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.general_img_2 = QtGui.QLabel(self.general_sidebar_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.general_img_2.sizePolicy().hasHeightForWidth())
        self.general_img_2.setSizePolicy(sizePolicy)
        self.general_img_2.setMinimumSize(QtCore.QSize(0, 0))
        self.general_img_2.setMaximumSize(QtCore.QSize(104, 145))
        self.general_img_2.setText(_fromUtf8(""))
        self.general_img_2.setPixmap(QtGui.QPixmap(_fromUtf8(":/images/images/D4W_ppa_energy.png")))
        self.general_img_2.setObjectName(_fromUtf8("general_img_2"))
        self.verticalLayout_9.addWidget(self.general_img_2)
        self.general_descr_2 = QtGui.QTextBrowser(self.general_sidebar_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.general_descr_2.sizePolicy().hasHeightForWidth())
        self.general_descr_2.setSizePolicy(sizePolicy)
        self.general_descr_2.setMinimumSize(QtCore.QSize(104, 0))
        self.general_descr_2.setMaximumSize(QtCore.QSize(104, 16777215))
        self.general_descr_2.setObjectName(_fromUtf8("general_descr_2"))
        self.verticalLayout_9.addWidget(self.general_descr_2)
        self.horizontalLayout.addWidget(self.general_sidebar_2)
        self.main_input_widget.addTab(self.tab, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.tab_3)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.general_params_4 = QtGui.QWidget(self.tab_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.general_params_4.sizePolicy().hasHeightForWidth())
        self.general_params_4.setSizePolicy(sizePolicy)
        self.general_params_4.setMinimumSize(QtCore.QSize(0, 0))
        self.general_params_4.setObjectName(_fromUtf8("general_params_4"))
        self.verticalLayout_18 = QtGui.QVBoxLayout(self.general_params_4)
        self.verticalLayout_18.setMargin(0)
        self.verticalLayout_18.setObjectName(_fromUtf8("verticalLayout_18"))
        self.scrollArea_10 = QtGui.QScrollArea(self.general_params_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea_10.sizePolicy().hasHeightForWidth())
        self.scrollArea_10.setSizePolicy(sizePolicy)
        self.scrollArea_10.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea_10.setWidgetResizable(True)
        self.scrollArea_10.setObjectName(_fromUtf8("scrollArea_10"))
        self.scrollAreaWidgetContents_10 = QtGui.QWidget()
        self.scrollAreaWidgetContents_10.setGeometry(QtCore.QRect(0, 0, 463, 896))
        self.scrollAreaWidgetContents_10.setObjectName(_fromUtf8("scrollAreaWidgetContents_10"))
        self.verticalLayout_19 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents_10)
        self.verticalLayout_19.setObjectName(_fromUtf8("verticalLayout_19"))
        self.demand_down_title = QtGui.QLabel(self.scrollAreaWidgetContents_10)
        self.demand_down_title.setEnabled(True)
        self.demand_down_title.setMinimumSize(QtCore.QSize(445, 16))
        self.demand_down_title.setMaximumSize(QtCore.QSize(16777215, 16))
        self.demand_down_title.setObjectName(_fromUtf8("demand_down_title"))
        self.verticalLayout_19.addWidget(self.demand_down_title)
        self.dp_config_widget = QtGui.QWidget(self.scrollAreaWidgetContents_10)
        self.dp_config_widget.setMinimumSize(QtCore.QSize(0, 400))
        self.dp_config_widget.setObjectName(_fromUtf8("dp_config_widget"))
        self.dagg_dp_noonpic_2 = QtGui.QLabel(self.dp_config_widget)
        self.dagg_dp_noonpic_2.setGeometry(QtCore.QRect(155, 175, 41, 41))
        self.dagg_dp_noonpic_2.setText(_fromUtf8(""))
        self.dagg_dp_noonpic_2.setPixmap(QtGui.QPixmap(_fromUtf8("noon-small.png")))
        self.dagg_dp_noonpic_2.setObjectName(_fromUtf8("dagg_dp_noonpic_2"))
        self.dagg_dp_morningpic_2 = QtGui.QLabel(self.dp_config_widget)
        self.dagg_dp_morningpic_2.setEnabled(True)
        self.dagg_dp_morningpic_2.setGeometry(QtCore.QRect(55, 175, 41, 41))
        self.dagg_dp_morningpic_2.setText(_fromUtf8(""))
        self.dagg_dp_morningpic_2.setPixmap(QtGui.QPixmap(_fromUtf8("morning-small.png")))
        self.dagg_dp_morningpic_2.setObjectName(_fromUtf8("dagg_dp_morningpic_2"))
        self.dagg_dp_nightpic_2 = QtGui.QLabel(self.dp_config_widget)
        self.dagg_dp_nightpic_2.setGeometry(QtCore.QRect(355, 175, 41, 41))
        self.dagg_dp_nightpic_2.setText(_fromUtf8(""))
        self.dagg_dp_nightpic_2.setPixmap(QtGui.QPixmap(_fromUtf8("night-small.png")))
        self.dagg_dp_nightpic_2.setObjectName(_fromUtf8("dagg_dp_nightpic_2"))
        self.dp_kitchen_combo = QtGui.QComboBox(self.dp_config_widget)
        self.dp_kitchen_combo.setGeometry(QtCore.QRect(110, 40, 191, 16))
        self.dp_kitchen_combo.setObjectName(_fromUtf8("dp_kitchen_combo"))
        self.dp_kitchen_combo.addItem(_fromUtf8(""))
        self.dp_kitchen_combo.addItem(_fromUtf8(""))
        self.dp_kitchen_combo.addItem(_fromUtf8(""))
        self.dp_kitchen_combo.addItem(_fromUtf8(""))
        self.demand_res_lbl = QtGui.QLabel(self.dp_config_widget)
        self.demand_res_lbl.setGeometry(QtCore.QRect(10, 10, 261, 16))
        self.demand_res_lbl.setObjectName(_fromUtf8("demand_res_lbl"))
        self.dp_kitchen_lbl = QtGui.QLabel(self.dp_config_widget)
        self.dp_kitchen_lbl.setGeometry(QtCore.QRect(30, 40, 46, 13))
        self.dp_kitchen_lbl.setObjectName(_fromUtf8("dp_kitchen_lbl"))
        self.dp_shower_lbl = QtGui.QLabel(self.dp_config_widget)
        self.dp_shower_lbl.setGeometry(QtCore.QRect(30, 70, 46, 13))
        self.dp_shower_lbl.setObjectName(_fromUtf8("dp_shower_lbl"))
        self.dp_toilet_lbl = QtGui.QLabel(self.dp_config_widget)
        self.dp_toilet_lbl.setGeometry(QtCore.QRect(30, 100, 46, 13))
        self.dp_toilet_lbl.setObjectName(_fromUtf8("dp_toilet_lbl"))
        self.dp_laundry_lbl = QtGui.QLabel(self.dp_config_widget)
        self.dp_laundry_lbl.setGeometry(QtCore.QRect(30, 130, 46, 13))
        self.dp_laundry_lbl.setObjectName(_fromUtf8("dp_laundry_lbl"))
        self.dp_shower_combo = QtGui.QComboBox(self.dp_config_widget)
        self.dp_shower_combo.setGeometry(QtCore.QRect(110, 70, 191, 16))
        self.dp_shower_combo.setObjectName(_fromUtf8("dp_shower_combo"))
        self.dp_shower_combo.addItem(_fromUtf8(""))
        self.dp_shower_combo.addItem(_fromUtf8(""))
        self.dp_shower_combo.addItem(_fromUtf8(""))
        self.dp_shower_combo.addItem(_fromUtf8(""))
        self.dp_toilet_combo = QtGui.QComboBox(self.dp_config_widget)
        self.dp_toilet_combo.setGeometry(QtCore.QRect(110, 100, 191, 16))
        self.dp_toilet_combo.setObjectName(_fromUtf8("dp_toilet_combo"))
        self.dp_toilet_combo.addItem(_fromUtf8(""))
        self.dp_toilet_combo.addItem(_fromUtf8(""))
        self.dp_toilet_combo.addItem(_fromUtf8(""))
        self.dp_toilet_combo.addItem(_fromUtf8(""))
        self.dp_laundry_combo = QtGui.QComboBox(self.dp_config_widget)
        self.dp_laundry_combo.setGeometry(QtCore.QRect(110, 130, 191, 16))
        self.dp_laundry_combo.setObjectName(_fromUtf8("dp_laundry_combo"))
        self.dp_laundry_combo.addItem(_fromUtf8(""))
        self.dp_laundry_combo.addItem(_fromUtf8(""))
        self.dp_laundry_combo.addItem(_fromUtf8(""))
        self.dp_laundry_combo.addItem(_fromUtf8(""))
        self.dp_irrigate_lbl = QtGui.QLabel(self.dp_config_widget)
        self.dp_irrigate_lbl.setGeometry(QtCore.QRect(30, 160, 46, 13))
        self.dp_irrigate_lbl.setObjectName(_fromUtf8("dp_irrigate_lbl"))
        self.dp_irrigate_combo = QtGui.QComboBox(self.dp_config_widget)
        self.dp_irrigate_combo.setGeometry(QtCore.QRect(110, 160, 191, 16))
        self.dp_irrigate_combo.setObjectName(_fromUtf8("dp_irrigate_combo"))
        self.dp_irrigate_combo.addItem(_fromUtf8(""))
        self.dp_irrigate_combo.addItem(_fromUtf8(""))
        self.dp_irrigate_combo.addItem(_fromUtf8(""))
        self.dp_irrigate_combo.addItem(_fromUtf8(""))
        self.demand_nonres_lbl = QtGui.QLabel(self.dp_config_widget)
        self.demand_nonres_lbl.setGeometry(QtCore.QRect(10, 190, 261, 16))
        self.demand_nonres_lbl.setObjectName(_fromUtf8("demand_nonres_lbl"))
        self.dp_com_combo = QtGui.QComboBox(self.dp_config_widget)
        self.dp_com_combo.setGeometry(QtCore.QRect(110, 220, 191, 16))
        self.dp_com_combo.setObjectName(_fromUtf8("dp_com_combo"))
        self.dp_com_combo.addItem(_fromUtf8(""))
        self.dp_com_combo.addItem(_fromUtf8(""))
        self.dp_com_combo.addItem(_fromUtf8(""))
        self.dp_com_combo.addItem(_fromUtf8(""))
        self.dp_com_lbl = QtGui.QLabel(self.dp_config_widget)
        self.dp_com_lbl.setGeometry(QtCore.QRect(30, 220, 61, 16))
        self.dp_com_lbl.setObjectName(_fromUtf8("dp_com_lbl"))
        self.dp_ind_combo = QtGui.QComboBox(self.dp_config_widget)
        self.dp_ind_combo.setGeometry(QtCore.QRect(110, 250, 191, 16))
        self.dp_ind_combo.setObjectName(_fromUtf8("dp_ind_combo"))
        self.dp_ind_combo.addItem(_fromUtf8(""))
        self.dp_ind_combo.addItem(_fromUtf8(""))
        self.dp_ind_combo.addItem(_fromUtf8(""))
        self.dp_ind_combo.addItem(_fromUtf8(""))
        self.dp_ind_lbl = QtGui.QLabel(self.dp_config_widget)
        self.dp_ind_lbl.setGeometry(QtCore.QRect(30, 250, 46, 13))
        self.dp_ind_lbl.setObjectName(_fromUtf8("dp_ind_lbl"))
        self.dp_kitchen_custom = QtGui.QPushButton(self.dp_config_widget)
        self.dp_kitchen_custom.setGeometry(QtCore.QRect(320, 38, 81, 21))
        self.dp_kitchen_custom.setObjectName(_fromUtf8("dp_kitchen_custom"))
        self.dp_shower_custom = QtGui.QPushButton(self.dp_config_widget)
        self.dp_shower_custom.setGeometry(QtCore.QRect(320, 67, 81, 21))
        self.dp_shower_custom.setObjectName(_fromUtf8("dp_shower_custom"))
        self.dp_toilet_custom = QtGui.QPushButton(self.dp_config_widget)
        self.dp_toilet_custom.setGeometry(QtCore.QRect(320, 97, 81, 21))
        self.dp_toilet_custom.setObjectName(_fromUtf8("dp_toilet_custom"))
        self.dp_laundry_custom = QtGui.QPushButton(self.dp_config_widget)
        self.dp_laundry_custom.setGeometry(QtCore.QRect(320, 127, 81, 21))
        self.dp_laundry_custom.setObjectName(_fromUtf8("dp_laundry_custom"))
        self.dp_irrigate_custom = QtGui.QPushButton(self.dp_config_widget)
        self.dp_irrigate_custom.setGeometry(QtCore.QRect(320, 157, 81, 21))
        self.dp_irrigate_custom.setObjectName(_fromUtf8("dp_irrigate_custom"))
        self.dp_com_custom = QtGui.QPushButton(self.dp_config_widget)
        self.dp_com_custom.setGeometry(QtCore.QRect(320, 217, 81, 21))
        self.dp_com_custom.setObjectName(_fromUtf8("dp_com_custom"))
        self.dp_ind_custom = QtGui.QPushButton(self.dp_config_widget)
        self.dp_ind_custom.setGeometry(QtCore.QRect(320, 247, 81, 21))
        self.dp_ind_custom.setObjectName(_fromUtf8("dp_ind_custom"))
        self.dp_pubirr_combo = QtGui.QComboBox(self.dp_config_widget)
        self.dp_pubirr_combo.setGeometry(QtCore.QRect(110, 280, 191, 16))
        self.dp_pubirr_combo.setObjectName(_fromUtf8("dp_pubirr_combo"))
        self.dp_pubirr_combo.addItem(_fromUtf8(""))
        self.dp_pubirr_combo.addItem(_fromUtf8(""))
        self.dp_pubirr_combo.addItem(_fromUtf8(""))
        self.dp_pubirr_combo.addItem(_fromUtf8(""))
        self.dp_pubirr_lbl = QtGui.QLabel(self.dp_config_widget)
        self.dp_pubirr_lbl.setGeometry(QtCore.QRect(30, 280, 46, 13))
        self.dp_pubirr_lbl.setObjectName(_fromUtf8("dp_pubirr_lbl"))
        self.dp_pubirr_custom = QtGui.QPushButton(self.dp_config_widget)
        self.dp_pubirr_custom.setGeometry(QtCore.QRect(320, 277, 81, 21))
        self.dp_pubirr_custom.setObjectName(_fromUtf8("dp_pubirr_custom"))
        self.eps_title = QtGui.QLabel(self.dp_config_widget)
        self.eps_title.setGeometry(QtCore.QRect(10, 310, 261, 16))
        self.eps_title.setObjectName(_fromUtf8("eps_title"))
        self.altwater_title = QtGui.QLabel(self.dp_config_widget)
        self.altwater_title.setGeometry(QtCore.QRect(10, 360, 261, 16))
        self.altwater_title.setObjectName(_fromUtf8("altwater_title"))
        self.verticalLayout_19.addWidget(self.dp_config_widget)
        self.ws_network_title = QtGui.QLabel(self.scrollAreaWidgetContents_10)
        self.ws_network_title.setEnabled(True)
        self.ws_network_title.setMinimumSize(QtCore.QSize(445, 16))
        self.ws_network_title.setMaximumSize(QtCore.QSize(16777215, 16))
        self.ws_network_title.setObjectName(_fromUtf8("ws_network_title"))
        self.verticalLayout_19.addWidget(self.ws_network_title)
        self.wsnetwork_config_widget = QtGui.QWidget(self.scrollAreaWidgetContents_10)
        self.wsnetwork_config_widget.setMinimumSize(QtCore.QSize(0, 200))
        self.wsnetwork_config_widget.setObjectName(_fromUtf8("wsnetwork_config_widget"))
        self.dagg_dp_noonpic_3 = QtGui.QLabel(self.wsnetwork_config_widget)
        self.dagg_dp_noonpic_3.setGeometry(QtCore.QRect(155, 175, 41, 41))
        self.dagg_dp_noonpic_3.setText(_fromUtf8(""))
        self.dagg_dp_noonpic_3.setPixmap(QtGui.QPixmap(_fromUtf8("noon-small.png")))
        self.dagg_dp_noonpic_3.setObjectName(_fromUtf8("dagg_dp_noonpic_3"))
        self.dagg_dp_morningpic_3 = QtGui.QLabel(self.wsnetwork_config_widget)
        self.dagg_dp_morningpic_3.setEnabled(True)
        self.dagg_dp_morningpic_3.setGeometry(QtCore.QRect(55, 175, 41, 41))
        self.dagg_dp_morningpic_3.setText(_fromUtf8(""))
        self.dagg_dp_morningpic_3.setPixmap(QtGui.QPixmap(_fromUtf8("morning-small.png")))
        self.dagg_dp_morningpic_3.setObjectName(_fromUtf8("dagg_dp_morningpic_3"))
        self.dagg_dp_nightpic_3 = QtGui.QLabel(self.wsnetwork_config_widget)
        self.dagg_dp_nightpic_3.setGeometry(QtCore.QRect(355, 175, 41, 41))
        self.dagg_dp_nightpic_3.setText(_fromUtf8(""))
        self.dagg_dp_nightpic_3.setPixmap(QtGui.QPixmap(_fromUtf8("night-small.png")))
        self.dagg_dp_nightpic_3.setObjectName(_fromUtf8("dagg_dp_nightpic_3"))
        self.dagg_dp_eveningpic_3 = QtGui.QLabel(self.wsnetwork_config_widget)
        self.dagg_dp_eveningpic_3.setGeometry(QtCore.QRect(255, 175, 41, 41))
        self.dagg_dp_eveningpic_3.setText(_fromUtf8(""))
        self.dagg_dp_eveningpic_3.setPixmap(QtGui.QPixmap(_fromUtf8("evening-small.png")))
        self.dagg_dp_eveningpic_3.setObjectName(_fromUtf8("dagg_dp_eveningpic_3"))
        self.verticalLayout_19.addWidget(self.wsnetwork_config_widget)
        self.ws_network_title_2 = QtGui.QLabel(self.scrollAreaWidgetContents_10)
        self.ws_network_title_2.setEnabled(True)
        self.ws_network_title_2.setMinimumSize(QtCore.QSize(445, 16))
        self.ws_network_title_2.setMaximumSize(QtCore.QSize(16777215, 16))
        self.ws_network_title_2.setObjectName(_fromUtf8("ws_network_title_2"))
        self.verticalLayout_19.addWidget(self.ws_network_title_2)
        self.wsnetwork_config_widget_2 = QtGui.QWidget(self.scrollAreaWidgetContents_10)
        self.wsnetwork_config_widget_2.setMinimumSize(QtCore.QSize(0, 200))
        self.wsnetwork_config_widget_2.setObjectName(_fromUtf8("wsnetwork_config_widget_2"))
        self.dagg_dp_noonpic_4 = QtGui.QLabel(self.wsnetwork_config_widget_2)
        self.dagg_dp_noonpic_4.setGeometry(QtCore.QRect(155, 175, 41, 41))
        self.dagg_dp_noonpic_4.setText(_fromUtf8(""))
        self.dagg_dp_noonpic_4.setPixmap(QtGui.QPixmap(_fromUtf8("noon-small.png")))
        self.dagg_dp_noonpic_4.setObjectName(_fromUtf8("dagg_dp_noonpic_4"))
        self.dagg_dp_morningpic_4 = QtGui.QLabel(self.wsnetwork_config_widget_2)
        self.dagg_dp_morningpic_4.setEnabled(True)
        self.dagg_dp_morningpic_4.setGeometry(QtCore.QRect(55, 175, 41, 41))
        self.dagg_dp_morningpic_4.setText(_fromUtf8(""))
        self.dagg_dp_morningpic_4.setPixmap(QtGui.QPixmap(_fromUtf8("morning-small.png")))
        self.dagg_dp_morningpic_4.setObjectName(_fromUtf8("dagg_dp_morningpic_4"))
        self.dagg_dp_nightpic_4 = QtGui.QLabel(self.wsnetwork_config_widget_2)
        self.dagg_dp_nightpic_4.setGeometry(QtCore.QRect(355, 175, 41, 41))
        self.dagg_dp_nightpic_4.setText(_fromUtf8(""))
        self.dagg_dp_nightpic_4.setPixmap(QtGui.QPixmap(_fromUtf8("night-small.png")))
        self.dagg_dp_nightpic_4.setObjectName(_fromUtf8("dagg_dp_nightpic_4"))
        self.dagg_dp_eveningpic_4 = QtGui.QLabel(self.wsnetwork_config_widget_2)
        self.dagg_dp_eveningpic_4.setGeometry(QtCore.QRect(255, 175, 41, 41))
        self.dagg_dp_eveningpic_4.setText(_fromUtf8(""))
        self.dagg_dp_eveningpic_4.setPixmap(QtGui.QPixmap(_fromUtf8("evening-small.png")))
        self.dagg_dp_eveningpic_4.setObjectName(_fromUtf8("dagg_dp_eveningpic_4"))
        self.verticalLayout_19.addWidget(self.wsnetwork_config_widget_2)
        self.scrollArea_10.setWidget(self.scrollAreaWidgetContents_10)
        self.verticalLayout_18.addWidget(self.scrollArea_10)
        self.horizontalLayout_3.addWidget(self.general_params_4)
        self.general_sidebar_4 = QtGui.QWidget(self.tab_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.general_sidebar_4.sizePolicy().hasHeightForWidth())
        self.general_sidebar_4.setSizePolicy(sizePolicy)
        self.general_sidebar_4.setMinimumSize(QtCore.QSize(0, 0))
        self.general_sidebar_4.setMaximumSize(QtCore.QSize(122, 16777215))
        self.general_sidebar_4.setObjectName(_fromUtf8("general_sidebar_4"))
        self.verticalLayout_11 = QtGui.QVBoxLayout(self.general_sidebar_4)
        self.verticalLayout_11.setMargin(0)
        self.verticalLayout_11.setObjectName(_fromUtf8("verticalLayout_11"))
        self.general_img_4 = QtGui.QLabel(self.general_sidebar_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.general_img_4.sizePolicy().hasHeightForWidth())
        self.general_img_4.setSizePolicy(sizePolicy)
        self.general_img_4.setMinimumSize(QtCore.QSize(0, 0))
        self.general_img_4.setMaximumSize(QtCore.QSize(104, 145))
        self.general_img_4.setText(_fromUtf8(""))
        self.general_img_4.setPixmap(QtGui.QPixmap(_fromUtf8(":/images/images/D4W_ppa_demand.png")))
        self.general_img_4.setObjectName(_fromUtf8("general_img_4"))
        self.verticalLayout_11.addWidget(self.general_img_4)
        self.general_descr_4 = QtGui.QTextBrowser(self.general_sidebar_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.general_descr_4.sizePolicy().hasHeightForWidth())
        self.general_descr_4.setSizePolicy(sizePolicy)
        self.general_descr_4.setMinimumSize(QtCore.QSize(104, 0))
        self.general_descr_4.setMaximumSize(QtCore.QSize(104, 16777215))
        self.general_descr_4.setObjectName(_fromUtf8("general_descr_4"))
        self.verticalLayout_11.addWidget(self.general_descr_4)
        self.horizontalLayout_3.addWidget(self.general_sidebar_4)
        self.main_input_widget.addTab(self.tab_3, _fromUtf8(""))
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName(_fromUtf8("tab_5"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.tab_5)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.general_params_6 = QtGui.QWidget(self.tab_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.general_params_6.sizePolicy().hasHeightForWidth())
        self.general_params_6.setSizePolicy(sizePolicy)
        self.general_params_6.setMinimumSize(QtCore.QSize(0, 0))
        self.general_params_6.setObjectName(_fromUtf8("general_params_6"))
        self.verticalLayout_24 = QtGui.QVBoxLayout(self.general_params_6)
        self.verticalLayout_24.setMargin(0)
        self.verticalLayout_24.setObjectName(_fromUtf8("verticalLayout_24"))
        self.scrollArea_12 = QtGui.QScrollArea(self.general_params_6)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea_12.sizePolicy().hasHeightForWidth())
        self.scrollArea_12.setSizePolicy(sizePolicy)
        self.scrollArea_12.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea_12.setWidgetResizable(True)
        self.scrollArea_12.setObjectName(_fromUtf8("scrollArea_12"))
        self.scrollAreaWidgetContents_12 = QtGui.QWidget()
        self.scrollAreaWidgetContents_12.setGeometry(QtCore.QRect(0, 0, 463, 278))
        self.scrollAreaWidgetContents_12.setObjectName(_fromUtf8("scrollAreaWidgetContents_12"))
        self.verticalLayout_25 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents_12)
        self.verticalLayout_25.setObjectName(_fromUtf8("verticalLayout_25"))
        self.simulationconfig_lbl_4 = QtGui.QLabel(self.scrollAreaWidgetContents_12)
        self.simulationconfig_lbl_4.setEnabled(False)
        self.simulationconfig_lbl_4.setMinimumSize(QtCore.QSize(445, 16))
        self.simulationconfig_lbl_4.setMaximumSize(QtCore.QSize(16777215, 16))
        self.simulationconfig_lbl_4.setObjectName(_fromUtf8("simulationconfig_lbl_4"))
        self.verticalLayout_25.addWidget(self.simulationconfig_lbl_4)
        self.outputconfig_widget_4 = QtGui.QWidget(self.scrollAreaWidgetContents_12)
        self.outputconfig_widget_4.setMinimumSize(QtCore.QSize(0, 100))
        self.outputconfig_widget_4.setObjectName(_fromUtf8("outputconfig_widget_4"))
        self.comingsoon_6 = QtGui.QLabel(self.outputconfig_widget_4)
        self.comingsoon_6.setEnabled(False)
        self.comingsoon_6.setGeometry(QtCore.QRect(40, 30, 111, 20))
        self.comingsoon_6.setObjectName(_fromUtf8("comingsoon_6"))
        self.verticalLayout_25.addWidget(self.outputconfig_widget_4)
        self.scrollArea_12.setWidget(self.scrollAreaWidgetContents_12)
        self.verticalLayout_24.addWidget(self.scrollArea_12)
        self.horizontalLayout_5.addWidget(self.general_params_6)
        self.general_sidebar_6 = QtGui.QWidget(self.tab_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.general_sidebar_6.sizePolicy().hasHeightForWidth())
        self.general_sidebar_6.setSizePolicy(sizePolicy)
        self.general_sidebar_6.setMinimumSize(QtCore.QSize(0, 0))
        self.general_sidebar_6.setMaximumSize(QtCore.QSize(122, 16777215))
        self.general_sidebar_6.setObjectName(_fromUtf8("general_sidebar_6"))
        self.verticalLayout_23 = QtGui.QVBoxLayout(self.general_sidebar_6)
        self.verticalLayout_23.setMargin(0)
        self.verticalLayout_23.setObjectName(_fromUtf8("verticalLayout_23"))
        self.general_img_6 = QtGui.QLabel(self.general_sidebar_6)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.general_img_6.sizePolicy().hasHeightForWidth())
        self.general_img_6.setSizePolicy(sizePolicy)
        self.general_img_6.setMinimumSize(QtCore.QSize(0, 0))
        self.general_img_6.setMaximumSize(QtCore.QSize(104, 145))
        self.general_img_6.setText(_fromUtf8(""))
        self.general_img_6.setPixmap(QtGui.QPixmap(_fromUtf8(":/images/images/D4W_ppa_pollution.png")))
        self.general_img_6.setObjectName(_fromUtf8("general_img_6"))
        self.verticalLayout_23.addWidget(self.general_img_6)
        self.general_descr_6 = QtGui.QTextBrowser(self.general_sidebar_6)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.general_descr_6.sizePolicy().hasHeightForWidth())
        self.general_descr_6.setSizePolicy(sizePolicy)
        self.general_descr_6.setMinimumSize(QtCore.QSize(104, 0))
        self.general_descr_6.setMaximumSize(QtCore.QSize(104, 16777215))
        self.general_descr_6.setObjectName(_fromUtf8("general_descr_6"))
        self.verticalLayout_23.addWidget(self.general_descr_6)
        self.horizontalLayout_5.addWidget(self.general_sidebar_6)
        self.main_input_widget.addTab(self.tab_5, _fromUtf8(""))
        self.verticalLayout.addWidget(self.main_input_widget)
        self.footer_widget = QtGui.QWidget(Perfconfig_Dialog)
        self.footer_widget.setMinimumSize(QtCore.QSize(0, 38))
        self.footer_widget.setMaximumSize(QtCore.QSize(16777215, 38))
        self.footer_widget.setObjectName(_fromUtf8("footer_widget"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.footer_widget)
        self.horizontalLayout_7.setMargin(0)
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.remarks = QtGui.QLabel(self.footer_widget)
        self.remarks.setObjectName(_fromUtf8("remarks"))
        self.horizontalLayout_7.addWidget(self.remarks)
        self.buttonBox = QtGui.QDialogButtonBox(self.footer_widget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.horizontalLayout_7.addWidget(self.buttonBox)
        self.pushButton = QtGui.QPushButton(self.footer_widget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout_7.addWidget(self.pushButton)
        self.verticalLayout.addWidget(self.footer_widget)

        self.retranslateUi(Perfconfig_Dialog)
        self.main_input_widget.setCurrentIndex(0)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Perfconfig_Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Perfconfig_Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Perfconfig_Dialog)

    def retranslateUi(self, Perfconfig_Dialog):
        Perfconfig_Dialog.setWindowTitle(_translate("Perfconfig_Dialog", "Performance Assessment Settings", None))
        self.prepPA_subheading.setText(_translate("Perfconfig_Dialog", "Configure settings performance assessment of the Urban Water System", None))
        self.prepPA_heading.setText(_translate("Perfconfig_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Performance Assessment</span></p></body></html>", None))
        self.musicsimconfig_lbl_3.setText(_translate("Perfconfig_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Select Simulation Cycle to use for Performance Assessment</span></p></body></html>", None))
        self.select_pc.setText(_translate("Perfconfig_Dialog", "Planning Cycle Performance Assessment", None))
        self.select_ic.setText(_translate("Perfconfig_Dialog", "Implementation Cycle Performance Assessment", None))
        self.musicsimconfig_lbl_2.setText(_translate("Perfconfig_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Select which Analyses to conduct</span></p></body></html>", None))
        self.perf_MUSIC.setText(_translate("Perfconfig_Dialog", "MUSIC Model Creation, Simulation and Assessment", None))
        self.perf_Economics.setText(_translate("Perfconfig_Dialog", "Economic Life Cycle Costing Analysis", None))
        self.perf_Microclimate.setText(_translate("Perfconfig_Dialog", "Microclimate Analysis", None))
        self.perf_EPANET.setText(_translate("Perfconfig_Dialog", "Integrated Water Supply Systems Analysis", None))
        self.perf_CD3.setText(_translate("Perfconfig_Dialog", "Integrated Urban Water Cycle Modelling", None))
        self.general_descr_3.setHtml(_translate("Perfconfig_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Setup performance assessment for planning outputs.</span></p></body></html>", None))
        self.main_input_widget.setTabText(self.main_input_widget.indexOf(self.tab_2), _translate("Perfconfig_Dialog", "Select Analyses", None))
        self.musicsimconfig_lbl.setText(_translate("Perfconfig_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Setup MUSIC Simulation</span></p></body></html>", None))
        self.musicsplit_check.setText(_translate("Perfconfig_Dialog", "Write a separate simulation file for each basin", None))
        self.music_browse_lbl.setText(_translate("Perfconfig_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">.mlb Climate file Path:</span></p></body></html>", None))
        self.music_browse_button.setText(_translate("Perfconfig_Dialog", "Browse...", None))
        self.music_version.setText(_translate("Perfconfig_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Select MUSIC Version:</span></p></body></html>", None))
        self.music_version_combo.setItemText(0, _translate("Perfconfig_Dialog", "eWater MUSIC Version 5", None))
        self.music_version_combo.setItemText(1, _translate("Perfconfig_Dialog", "eWater MUSIC Version 6", None))
        self.musiccatchment_lbl.setText(_translate("Perfconfig_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Catchment Hydrology Setup</span></p></body></html>", None))
        self.rnr_params_lbl.setText(_translate("Perfconfig_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Rainfall-Runoff Parameters</span></p></body></html>", None))
        self.musicRR_soil_lbl.setText(_translate("Perfconfig_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Soil Storage Capacity [mm]</span></p></body></html>", None))
        self.musicRR_field_lbl.setText(_translate("Perfconfig_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Field Capacity [mm]</span></p></body></html>", None))
        self.include_pervious.setText(_translate("Perfconfig_Dialog", "Include Pervious Areas in Catchment Simulation?", None))
        self.musicRR_bfr_lbl.setText(_translate("Perfconfig_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Daily Baseflow Rate</span></p></body></html>", None))
        self.musicRR_rcr_lbl.setText(_translate("Perfconfig_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Daily Recharge Rate</span></p></body></html>", None))
        self.musicRR_dsr_lbl.setText(_translate("Perfconfig_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Daily Deep Seepage Rate</span></p></body></html>", None))
        self.musicRR_bfr_spin.setSuffix(_translate("Perfconfig_Dialog", "%", None))
        self.musicRR_rcr_spin.setSuffix(_translate("Perfconfig_Dialog", "%", None))
        self.musicRR_dsr_spin.setSuffix(_translate("Perfconfig_Dialog", "%", None))
        self.include_route.setText(_translate("Perfconfig_Dialog", "Including Runoff Routing Across Catchment?", None))
        self.musicRR_musk_lbl1.setText(_translate("Perfconfig_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Muskingum-Cunge K [min]</span></p></body></html>", None))
        self.musicRR_muskk_auto.setText(_translate("Perfconfig_Dialog", "Determine automatically", None))
        self.musicRR_muskk_custom.setText(_translate("Perfconfig_Dialog", "Specify value", None))
        self.musicRR_musktheta_lbl.setText(_translate("Perfconfig_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Muskingum-Cunge Theta (0.1 - 0.49)</span></p></body></html>", None))
        self.musicRR_musk_lbl2.setText(_translate("Perfconfig_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">mins</span></p></body></html>", None))
        self.musicwsudsetup_lbl.setText(_translate("Perfconfig_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">WSUD Parameter Setup</span></p></body></html>", None))
        self.musicBF_params.setText(_translate("Perfconfig_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Bioretention Parameters:</span></p></body></html>", None))
        self.musicBF_TN_lbl.setText(_translate("Perfconfig_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">TN Content of Filter Media [mg/kg]</span></p></body></html>", None))
        self.musicBF_ortho_lbl.setText(_translate("Perfconfig_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Orthophosphate Content of Filter Media [mg/kg]</span></p></body></html>", None))
        self.musicwsudsetup_lbl_2.setText(_translate("Perfconfig_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Auto-Run Simulations</span></p></body></html>", None))
        self.musicpath_lbl.setText(_translate("Perfconfig_Dialog", "Path to MUSIC.exe:", None))
        self.musicpath_browse.setText(_translate("Perfconfig_Dialog", "Browse...", None))
        self.musicflux_check.setText(_translate("Perfconfig_Dialog", "Flow and Pollution Time Series", None))
        self.musicexport_lbl.setText(_translate("Perfconfig_Dialog", "Select Results to Export:", None))
        self.musictte_check.setText(_translate("Perfconfig_Dialog", "Treatment Train Effectiveness", None))
        self.musicauto_check.setText(_translate("Perfconfig_Dialog", "AutoRun MUSIC Simulation Files", None))
        self.general_descr.setHtml(_translate("Perfconfig_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Setup performance assessment for planning outputs.</span></p></body></html>", None))
        self.main_input_widget.setTabText(self.main_input_widget.indexOf(self.generaltab), _translate("Perfconfig_Dialog", "MUSIC Simulation", None))
        self.lcc_title.setText(_translate("Perfconfig_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Life Cycle Costing</span></p></body></html>", None))
        self.comingsoon_4.setText(_translate("Perfconfig_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-style:italic;\">coming soon...</span></p></body></html>", None))
        self.market_title.setText(_translate("Perfconfig_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Cost Allocations</span></p></body></html>", None))
        self.comingsoon_5.setText(_translate("Perfconfig_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-style:italic;\">coming soon...</span></p></body></html>", None))
        self.general_descr_5.setHtml(_translate("Perfconfig_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Undertake life cycle costing of the WSUD options and assess the financial implications.</span></p></body></html>", None))
        self.main_input_widget.setTabText(self.main_input_widget.indexOf(self.tab_4), _translate("Perfconfig_Dialog", "Economics", None))
        self.lcov_title.setText(_translate("Perfconfig_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Land Cover Analysis</span></p></body></html>", None))
        self.comingsoon_3.setText(_translate("Perfconfig_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-style:italic;\">coming soon...</span></p></body></html>", None))
        self.lst_title.setText(_translate("Perfconfig_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Land Surface Temperatures</span></p></body></html>", None))
        self.comingsoon_2.setText(_translate("Perfconfig_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-style:italic;\">coming soon...</span></p></body></html>", None))
        self.lstat_title.setText(_translate("Perfconfig_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Land Surface to Air Temperature Relationship</span></p></body></html>", None))
        self.comingsoon_1.setText(_translate("Perfconfig_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-style:italic;\">coming soon...</span></p></body></html>", None))
        self.general_descr_2.setHtml(_translate("Perfconfig_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Conduct a simple microclimate analysis of the modelled development. Produces an air temperature distribution map.</span></p></body></html>", None))
        self.main_input_widget.setTabText(self.main_input_widget.indexOf(self.tab), _translate("Perfconfig_Dialog", "Microclimate", None))
        self.demand_down_title.setText(_translate("Perfconfig_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Water Demand Downscaling</span></p></body></html>", None))
        self.dagg_dp_noonpic_2.setToolTip(_translate("Perfconfig_Dialog", "approx. 6am to 12pm", None))
        self.dagg_dp_noonpic_2.setWhatsThis(_translate("Perfconfig_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Select the minimum water quality requirement to source from when meeting demand.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">PO = Potable Water</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">NP = Non-potable Water</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">RW = Rainwater</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">SW = Stormwater</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">GW = Greywater</span></p></body></html>", None))
        self.dagg_dp_morningpic_2.setToolTip(_translate("Perfconfig_Dialog", "approx. 6am to 12pm", None))
        self.dagg_dp_morningpic_2.setWhatsThis(_translate("Perfconfig_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Select the minimum water quality requirement to source from when meeting demand.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">PO = Potable Water</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">NP = Non-potable Water</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">RW = Rainwater</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">SW = Stormwater</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">GW = Greywater</span></p></body></html>", None))
        self.dagg_dp_nightpic_2.setToolTip(_translate("Perfconfig_Dialog", "approx. 6am to 12pm", None))
        self.dagg_dp_nightpic_2.setWhatsThis(_translate("Perfconfig_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Select the minimum water quality requirement to source from when meeting demand.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">PO = Potable Water</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">NP = Non-potable Water</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">RW = Rainwater</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">SW = Stormwater</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">GW = Greywater</span></p></body></html>", None))
        self.dp_kitchen_combo.setItemText(0, _translate("Perfconfig_Dialog", "Standard 24h Diurnal Patttern", None))
        self.dp_kitchen_combo.setItemText(1, _translate("Perfconfig_Dialog", "Constant Hourly Pattern", None))
        self.dp_kitchen_combo.setItemText(2, _translate("Perfconfig_Dialog", "After-hours Constant 6pm-6am", None))
        self.dp_kitchen_combo.setItemText(3, _translate("Perfconfig_Dialog", "User-defined...", None))
        self.demand_res_lbl.setText(_translate("Perfconfig_Dialog", "<html><head/><body><p><span style=\" font-weight:600; font-style:italic;\">Configure Residential Demand Patterns:</span></p></body></html>", None))
        self.dp_kitchen_lbl.setText(_translate("Perfconfig_Dialog", "Kitchen", None))
        self.dp_shower_lbl.setText(_translate("Perfconfig_Dialog", "Shower", None))
        self.dp_toilet_lbl.setText(_translate("Perfconfig_Dialog", "Toilet", None))
        self.dp_laundry_lbl.setText(_translate("Perfconfig_Dialog", "Laundry", None))
        self.dp_shower_combo.setItemText(0, _translate("Perfconfig_Dialog", "Standard 24h Diurnal Patttern", None))
        self.dp_shower_combo.setItemText(1, _translate("Perfconfig_Dialog", "Constant Hourly Pattern", None))
        self.dp_shower_combo.setItemText(2, _translate("Perfconfig_Dialog", "After-hours Constant 6pm-6am", None))
        self.dp_shower_combo.setItemText(3, _translate("Perfconfig_Dialog", "User-defined...", None))
        self.dp_toilet_combo.setItemText(0, _translate("Perfconfig_Dialog", "Standard 24h Diurnal Patttern", None))
        self.dp_toilet_combo.setItemText(1, _translate("Perfconfig_Dialog", "Constant Hourly Pattern", None))
        self.dp_toilet_combo.setItemText(2, _translate("Perfconfig_Dialog", "After-hours Constant 6pm-6am", None))
        self.dp_toilet_combo.setItemText(3, _translate("Perfconfig_Dialog", "User-defined...", None))
        self.dp_laundry_combo.setItemText(0, _translate("Perfconfig_Dialog", "Standard 24h Diurnal Patttern", None))
        self.dp_laundry_combo.setItemText(1, _translate("Perfconfig_Dialog", "Constant Hourly Pattern", None))
        self.dp_laundry_combo.setItemText(2, _translate("Perfconfig_Dialog", "After-hours Constant 6pm-6am", None))
        self.dp_laundry_combo.setItemText(3, _translate("Perfconfig_Dialog", "User-defined...", None))
        self.dp_irrigate_lbl.setText(_translate("Perfconfig_Dialog", "Irrigation", None))
        self.dp_irrigate_combo.setItemText(0, _translate("Perfconfig_Dialog", "Standard 24h Diurnal Patttern", None))
        self.dp_irrigate_combo.setItemText(1, _translate("Perfconfig_Dialog", "Constant Hourly Pattern", None))
        self.dp_irrigate_combo.setItemText(2, _translate("Perfconfig_Dialog", "After-hours Constant 6pm-6am", None))
        self.dp_irrigate_combo.setItemText(3, _translate("Perfconfig_Dialog", "User-defined...", None))
        self.demand_nonres_lbl.setText(_translate("Perfconfig_Dialog", "<html><head/><body><p><span style=\" font-weight:600; font-style:italic;\">Configure Non-Residential Demand Patterns:</span></p></body></html>", None))
        self.dp_com_combo.setItemText(0, _translate("Perfconfig_Dialog", "Standard 24h Diurnal Patttern", None))
        self.dp_com_combo.setItemText(1, _translate("Perfconfig_Dialog", "Constant Hourly Pattern", None))
        self.dp_com_combo.setItemText(2, _translate("Perfconfig_Dialog", "After-hours Constant 6pm-6am", None))
        self.dp_com_combo.setItemText(3, _translate("Perfconfig_Dialog", "User-defined...", None))
        self.dp_com_lbl.setText(_translate("Perfconfig_Dialog", "Commercial", None))
        self.dp_ind_combo.setItemText(0, _translate("Perfconfig_Dialog", "Standard 24h Diurnal Patttern", None))
        self.dp_ind_combo.setItemText(1, _translate("Perfconfig_Dialog", "Constant Hourly Pattern", None))
        self.dp_ind_combo.setItemText(2, _translate("Perfconfig_Dialog", "After-hours Constant 6pm-6am", None))
        self.dp_ind_combo.setItemText(3, _translate("Perfconfig_Dialog", "User-defined...", None))
        self.dp_ind_lbl.setText(_translate("Perfconfig_Dialog", "Industrial", None))
        self.dp_kitchen_custom.setText(_translate("Perfconfig_Dialog", "Custom...", None))
        self.dp_shower_custom.setText(_translate("Perfconfig_Dialog", "Custom...", None))
        self.dp_toilet_custom.setText(_translate("Perfconfig_Dialog", "Custom...", None))
        self.dp_laundry_custom.setText(_translate("Perfconfig_Dialog", "Custom...", None))
        self.dp_irrigate_custom.setText(_translate("Perfconfig_Dialog", "Custom...", None))
        self.dp_com_custom.setText(_translate("Perfconfig_Dialog", "Custom...", None))
        self.dp_ind_custom.setText(_translate("Perfconfig_Dialog", "Custom...", None))
        self.dp_pubirr_combo.setItemText(0, _translate("Perfconfig_Dialog", "Standard 24h Diurnal Patttern", None))
        self.dp_pubirr_combo.setItemText(1, _translate("Perfconfig_Dialog", "Constant Hourly Pattern", None))
        self.dp_pubirr_combo.setItemText(2, _translate("Perfconfig_Dialog", "After-hours Constant 6pm-6am", None))
        self.dp_pubirr_combo.setItemText(3, _translate("Perfconfig_Dialog", "User-defined...", None))
        self.dp_pubirr_lbl.setText(_translate("Perfconfig_Dialog", "Irrigation", None))
        self.dp_pubirr_custom.setText(_translate("Perfconfig_Dialog", "Custom...", None))
        self.eps_title.setText(_translate("Perfconfig_Dialog", "<html><head/><body><p><span style=\" font-weight:600; font-style:italic;\">Weekly, Monthly &amp; Seasonal Settings</span></p></body></html>", None))
        self.altwater_title.setText(_translate("Perfconfig_Dialog", "<html><head/><body><p><span style=\" font-weight:600; font-style:italic;\">Rules for Alternative Water Sources</span></p></body></html>", None))
        self.ws_network_title.setText(_translate("Perfconfig_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Network Data &amp; Hydraulics</span></p></body></html>", None))
        self.dagg_dp_noonpic_3.setToolTip(_translate("Perfconfig_Dialog", "approx. 6am to 12pm", None))
        self.dagg_dp_noonpic_3.setWhatsThis(_translate("Perfconfig_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Select the minimum water quality requirement to source from when meeting demand.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">PO = Potable Water</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">NP = Non-potable Water</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">RW = Rainwater</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">SW = Stormwater</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">GW = Greywater</span></p></body></html>", None))
        self.dagg_dp_morningpic_3.setToolTip(_translate("Perfconfig_Dialog", "approx. 6am to 12pm", None))
        self.dagg_dp_morningpic_3.setWhatsThis(_translate("Perfconfig_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Select the minimum water quality requirement to source from when meeting demand.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">PO = Potable Water</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">NP = Non-potable Water</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">RW = Rainwater</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">SW = Stormwater</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">GW = Greywater</span></p></body></html>", None))
        self.dagg_dp_nightpic_3.setToolTip(_translate("Perfconfig_Dialog", "approx. 6am to 12pm", None))
        self.dagg_dp_nightpic_3.setWhatsThis(_translate("Perfconfig_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Select the minimum water quality requirement to source from when meeting demand.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">PO = Potable Water</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">NP = Non-potable Water</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">RW = Rainwater</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">SW = Stormwater</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">GW = Greywater</span></p></body></html>", None))
        self.dagg_dp_eveningpic_3.setToolTip(_translate("Perfconfig_Dialog", "approx. 6am to 12pm", None))
        self.dagg_dp_eveningpic_3.setWhatsThis(_translate("Perfconfig_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Select the minimum water quality requirement to source from when meeting demand.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">PO = Potable Water</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">NP = Non-potable Water</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">RW = Rainwater</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">SW = Stormwater</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">GW = Greywater</span></p></body></html>", None))
        self.ws_network_title_2.setText(_translate("Perfconfig_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">EPANET Simulation Management</span></p></body></html>", None))
        self.dagg_dp_noonpic_4.setToolTip(_translate("Perfconfig_Dialog", "approx. 6am to 12pm", None))
        self.dagg_dp_noonpic_4.setWhatsThis(_translate("Perfconfig_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Select the minimum water quality requirement to source from when meeting demand.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">PO = Potable Water</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">NP = Non-potable Water</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">RW = Rainwater</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">SW = Stormwater</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">GW = Greywater</span></p></body></html>", None))
        self.dagg_dp_morningpic_4.setToolTip(_translate("Perfconfig_Dialog", "approx. 6am to 12pm", None))
        self.dagg_dp_morningpic_4.setWhatsThis(_translate("Perfconfig_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Select the minimum water quality requirement to source from when meeting demand.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">PO = Potable Water</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">NP = Non-potable Water</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">RW = Rainwater</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">SW = Stormwater</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">GW = Greywater</span></p></body></html>", None))
        self.dagg_dp_nightpic_4.setToolTip(_translate("Perfconfig_Dialog", "approx. 6am to 12pm", None))
        self.dagg_dp_nightpic_4.setWhatsThis(_translate("Perfconfig_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Select the minimum water quality requirement to source from when meeting demand.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">PO = Potable Water</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">NP = Non-potable Water</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">RW = Rainwater</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">SW = Stormwater</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">GW = Greywater</span></p></body></html>", None))
        self.dagg_dp_eveningpic_4.setToolTip(_translate("Perfconfig_Dialog", "approx. 6am to 12pm", None))
        self.dagg_dp_eveningpic_4.setWhatsThis(_translate("Perfconfig_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Select the minimum water quality requirement to source from when meeting demand.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">PO = Potable Water</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">NP = Non-potable Water</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">RW = Rainwater</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">SW = Stormwater</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">GW = Greywater</span></p></body></html>", None))
        self.general_descr_4.setHtml(_translate("Perfconfig_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Link a water supply network model to UrbanBEATS to assess the impact of the current options on the resulting water distribution network.</span></p></body></html>", None))
        self.main_input_widget.setTabText(self.main_input_widget.indexOf(self.tab_3), _translate("Perfconfig_Dialog", "Water Supply", None))
        self.simulationconfig_lbl_4.setText(_translate("Perfconfig_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Urban Hydrology</span></p></body></html>", None))
        self.comingsoon_6.setText(_translate("Perfconfig_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-style:italic;\">coming soon...</span></p></body></html>", None))
        self.general_descr_6.setHtml(_translate("Perfconfig_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Conduct a full long-term integrated water quantity and mass balance simulation of the current option(s).</span></p></body></html>", None))
        self.main_input_widget.setTabText(self.main_input_widget.indexOf(self.tab_5), _translate("Perfconfig_Dialog", "Integrated Cycle", None))
        self.remarks.setText(_translate("Perfconfig_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-style:italic;\">UrbanBEATS v1.0 - (C) 2013 Peter M. Bach </span></p></body></html>", None))
        self.pushButton.setWhatsThis(_translate("Perfconfig_Dialog", "Help? What\'s that? Does it taste good? :)", None))
        self.pushButton.setText(_translate("Perfconfig_Dialog", "Help", None))

import guitoolbaricons_rc
