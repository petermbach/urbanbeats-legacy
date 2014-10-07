# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'md_perfassessgui.ui'
#
# Created: Tue Oct 07 11:08:31 2014
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Perfconfig_Dialog(object):
    def setupUi(self, Perfconfig_Dialog):
        Perfconfig_Dialog.setObjectName(_fromUtf8("Perfconfig_Dialog"))
        Perfconfig_Dialog.resize(670, 460)
        Perfconfig_Dialog.setWindowTitle(QtGui.QApplication.translate("Perfconfig_Dialog", "Performance Assessment Settings", None, QtGui.QApplication.UnicodeUTF8))
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
        self.prepPA_subheading.setText(QtGui.QApplication.translate("Perfconfig_Dialog", "Configure settings performance assessment of the Urban Water System", None, QtGui.QApplication.UnicodeUTF8))
        self.prepPA_subheading.setObjectName(_fromUtf8("prepPA_subheading"))
        self.prepPA_heading = QtGui.QLabel(self.title_frame)
        self.prepPA_heading.setGeometry(QtCore.QRect(50, 5, 451, 21))
        self.prepPA_heading.setText(QtGui.QApplication.translate("Perfconfig_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Performance Assessment</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
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
        self.scrollAreaWidgetContents_9.setGeometry(QtCore.QRect(0, 0, 463, 278))
        self.scrollAreaWidgetContents_9.setObjectName(_fromUtf8("scrollAreaWidgetContents_9"))
        self.verticalLayout_14 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents_9)
        self.verticalLayout_14.setObjectName(_fromUtf8("verticalLayout_14"))
        self.musicsimconfig_lbl_2 = QtGui.QLabel(self.scrollAreaWidgetContents_9)
        self.musicsimconfig_lbl_2.setMinimumSize(QtCore.QSize(445, 16))
        self.musicsimconfig_lbl_2.setMaximumSize(QtCore.QSize(16777215, 16))
        self.musicsimconfig_lbl_2.setText(QtGui.QApplication.translate("Perfconfig_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Select which Analyses to conduct</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.musicsimconfig_lbl_2.setObjectName(_fromUtf8("musicsimconfig_lbl_2"))
        self.verticalLayout_14.addWidget(self.musicsimconfig_lbl_2)
        self.simulationconfig_widget_3 = QtGui.QWidget(self.scrollAreaWidgetContents_9)
        self.simulationconfig_widget_3.setMinimumSize(QtCore.QSize(0, 100))
        self.simulationconfig_widget_3.setObjectName(_fromUtf8("simulationconfig_widget_3"))
        self.perf_MUSIC = QtGui.QCheckBox(self.simulationconfig_widget_3)
        self.perf_MUSIC.setGeometry(QtCore.QRect(60, 20, 361, 17))
        self.perf_MUSIC.setText(QtGui.QApplication.translate("Perfconfig_Dialog", "MUSIC Model Creation, Simulation and Assessment", None, QtGui.QApplication.UnicodeUTF8))
        self.perf_MUSIC.setObjectName(_fromUtf8("perf_MUSIC"))
        self.perf_Economics = QtGui.QCheckBox(self.simulationconfig_widget_3)
        self.perf_Economics.setGeometry(QtCore.QRect(60, 60, 361, 17))
        self.perf_Economics.setText(QtGui.QApplication.translate("Perfconfig_Dialog", "Economic Analysis", None, QtGui.QApplication.UnicodeUTF8))
        self.perf_Economics.setObjectName(_fromUtf8("perf_Economics"))
        self.perf_Microclimate = QtGui.QCheckBox(self.simulationconfig_widget_3)
        self.perf_Microclimate.setGeometry(QtCore.QRect(60, 100, 361, 17))
        self.perf_Microclimate.setText(QtGui.QApplication.translate("Perfconfig_Dialog", "Microclimate Analysis", None, QtGui.QApplication.UnicodeUTF8))
        self.perf_Microclimate.setObjectName(_fromUtf8("perf_Microclimate"))
        self.perf_EPANET = QtGui.QCheckBox(self.simulationconfig_widget_3)
        self.perf_EPANET.setEnabled(False)
        self.perf_EPANET.setGeometry(QtCore.QRect(60, 140, 291, 17))
        self.perf_EPANET.setText(QtGui.QApplication.translate("Perfconfig_Dialog", "Integrated Water Supply Systems Analysis", None, QtGui.QApplication.UnicodeUTF8))
        self.perf_EPANET.setObjectName(_fromUtf8("perf_EPANET"))
        self.perf_CD3 = QtGui.QCheckBox(self.simulationconfig_widget_3)
        self.perf_CD3.setEnabled(False)
        self.perf_CD3.setGeometry(QtCore.QRect(60, 180, 291, 17))
        self.perf_CD3.setText(QtGui.QApplication.translate("Perfconfig_Dialog", "Integrated Urban Water Cycle Modelling", None, QtGui.QApplication.UnicodeUTF8))
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
        self.verticalLayout_14.addWidget(self.simulationconfig_widget_3)
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
        self.general_descr_3.setHtml(QtGui.QApplication.translate("Perfconfig_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Setup performance assessment for planning outputs.</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
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
        self.scrollAreaWidgetContents_7.setGeometry(QtCore.QRect(0, 0, 463, 436))
        self.scrollAreaWidgetContents_7.setObjectName(_fromUtf8("scrollAreaWidgetContents_7"))
        self.verticalLayout_12 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents_7)
        self.verticalLayout_12.setObjectName(_fromUtf8("verticalLayout_12"))
        self.musicsimconfig_lbl = QtGui.QLabel(self.scrollAreaWidgetContents_7)
        self.musicsimconfig_lbl.setMinimumSize(QtCore.QSize(445, 16))
        self.musicsimconfig_lbl.setMaximumSize(QtCore.QSize(16777215, 16))
        self.musicsimconfig_lbl.setText(QtGui.QApplication.translate("Perfconfig_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Setup MUSIC Simulation</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.musicsimconfig_lbl.setObjectName(_fromUtf8("musicsimconfig_lbl"))
        self.verticalLayout_12.addWidget(self.musicsimconfig_lbl)
        self.simulationconfig_widget = QtGui.QWidget(self.scrollAreaWidgetContents_7)
        self.simulationconfig_widget.setMinimumSize(QtCore.QSize(0, 100))
        self.simulationconfig_widget.setObjectName(_fromUtf8("simulationconfig_widget"))
        self.musicsplit_check = QtGui.QCheckBox(self.simulationconfig_widget)
        self.musicsplit_check.setGeometry(QtCore.QRect(10, 70, 381, 17))
        self.musicsplit_check.setText(QtGui.QApplication.translate("Perfconfig_Dialog", "Write a separate simulation file for each basin", None, QtGui.QApplication.UnicodeUTF8))
        self.musicsplit_check.setObjectName(_fromUtf8("musicsplit_check"))
        self.music_browse_pathbox = QtGui.QLineEdit(self.simulationconfig_widget)
        self.music_browse_pathbox.setGeometry(QtCore.QRect(130, 40, 201, 20))
        self.music_browse_pathbox.setObjectName(_fromUtf8("music_browse_pathbox"))
        self.music_browse_lbl = QtGui.QLabel(self.simulationconfig_widget)
        self.music_browse_lbl.setGeometry(QtCore.QRect(10, 40, 111, 20))
        self.music_browse_lbl.setText(QtGui.QApplication.translate("Perfconfig_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">.mlb Climate file Path:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.music_browse_lbl.setObjectName(_fromUtf8("music_browse_lbl"))
        self.music_browse_button = QtGui.QToolButton(self.simulationconfig_widget)
        self.music_browse_button.setGeometry(QtCore.QRect(340, 40, 61, 19))
        self.music_browse_button.setText(QtGui.QApplication.translate("Perfconfig_Dialog", "Browse...", None, QtGui.QApplication.UnicodeUTF8))
        self.music_browse_button.setObjectName(_fromUtf8("music_browse_button"))
        self.music_version = QtGui.QLabel(self.simulationconfig_widget)
        self.music_version.setGeometry(QtCore.QRect(10, 10, 121, 20))
        self.music_version.setText(QtGui.QApplication.translate("Perfconfig_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Select MUSIC Version:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.music_version.setObjectName(_fromUtf8("music_version"))
        self.music_version_combo = QtGui.QComboBox(self.simulationconfig_widget)
        self.music_version_combo.setGeometry(QtCore.QRect(130, 10, 201, 21))
        self.music_version_combo.setObjectName(_fromUtf8("music_version_combo"))
        self.music_version_combo.addItem(_fromUtf8(""))
        self.music_version_combo.setItemText(0, QtGui.QApplication.translate("Perfconfig_Dialog", "eWater MUSIC Version 5", None, QtGui.QApplication.UnicodeUTF8))
        self.music_version_combo.addItem(_fromUtf8(""))
        self.music_version_combo.setItemText(1, QtGui.QApplication.translate("Perfconfig_Dialog", "eWater MUSIC Version 6", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalLayout_12.addWidget(self.simulationconfig_widget)
        self.musicwsudsetup_lbl = QtGui.QLabel(self.scrollAreaWidgetContents_7)
        self.musicwsudsetup_lbl.setMinimumSize(QtCore.QSize(445, 16))
        self.musicwsudsetup_lbl.setMaximumSize(QtCore.QSize(16777215, 16))
        self.musicwsudsetup_lbl.setText(QtGui.QApplication.translate("Perfconfig_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">WSUD Parameter Setup</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.musicwsudsetup_lbl.setObjectName(_fromUtf8("musicwsudsetup_lbl"))
        self.verticalLayout_12.addWidget(self.musicwsudsetup_lbl)
        self.simulationconfig_widget_2 = QtGui.QWidget(self.scrollAreaWidgetContents_7)
        self.simulationconfig_widget_2.setMinimumSize(QtCore.QSize(0, 90))
        self.simulationconfig_widget_2.setObjectName(_fromUtf8("simulationconfig_widget_2"))
        self.musicBF_params = QtGui.QLabel(self.simulationconfig_widget_2)
        self.musicBF_params.setGeometry(QtCore.QRect(10, 5, 151, 20))
        self.musicBF_params.setText(QtGui.QApplication.translate("Perfconfig_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Bioretention Parameters:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.musicBF_params.setObjectName(_fromUtf8("musicBF_params"))
        self.musicBF_TN_box = QtGui.QLineEdit(self.simulationconfig_widget_2)
        self.musicBF_TN_box.setGeometry(QtCore.QRect(270, 30, 61, 20))
        self.musicBF_TN_box.setObjectName(_fromUtf8("musicBF_TN_box"))
        self.musicBF_TN_lbl = QtGui.QLabel(self.simulationconfig_widget_2)
        self.musicBF_TN_lbl.setGeometry(QtCore.QRect(30, 30, 181, 20))
        self.musicBF_TN_lbl.setText(QtGui.QApplication.translate("Perfconfig_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">TN Content of Filter Media [mg/kg]</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.musicBF_TN_lbl.setObjectName(_fromUtf8("musicBF_TN_lbl"))
        self.musicBF_ortho_lbl = QtGui.QLabel(self.simulationconfig_widget_2)
        self.musicBF_ortho_lbl.setGeometry(QtCore.QRect(30, 55, 241, 20))
        self.musicBF_ortho_lbl.setText(QtGui.QApplication.translate("Perfconfig_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Orthophosphate Content of Filter Media [mg/kg]</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.musicBF_ortho_lbl.setObjectName(_fromUtf8("musicBF_ortho_lbl"))
        self.musicBF_ortho_box = QtGui.QLineEdit(self.simulationconfig_widget_2)
        self.musicBF_ortho_box.setGeometry(QtCore.QRect(270, 55, 61, 20))
        self.musicBF_ortho_box.setObjectName(_fromUtf8("musicBF_ortho_box"))
        self.verticalLayout_12.addWidget(self.simulationconfig_widget_2)
        self.musicwsudsetup_lbl_2 = QtGui.QLabel(self.scrollAreaWidgetContents_7)
        self.musicwsudsetup_lbl_2.setMinimumSize(QtCore.QSize(445, 16))
        self.musicwsudsetup_lbl_2.setMaximumSize(QtCore.QSize(16777215, 16))
        self.musicwsudsetup_lbl_2.setText(QtGui.QApplication.translate("Perfconfig_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Auto-Run Simulations</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
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
        self.musicpath_lbl.setText(QtGui.QApplication.translate("Perfconfig_Dialog", "Path to MUSIC.exe:", None, QtGui.QApplication.UnicodeUTF8))
        self.musicpath_lbl.setObjectName(_fromUtf8("musicpath_lbl"))
        self.musicpath_browse = QtGui.QPushButton(self.simulationconfig_widget_4)
        self.musicpath_browse.setEnabled(False)
        self.musicpath_browse.setGeometry(QtCore.QRect(270, 40, 61, 23))
        self.musicpath_browse.setText(QtGui.QApplication.translate("Perfconfig_Dialog", "Browse...", None, QtGui.QApplication.UnicodeUTF8))
        self.musicpath_browse.setObjectName(_fromUtf8("musicpath_browse"))
        self.musicflux_check = QtGui.QCheckBox(self.simulationconfig_widget_4)
        self.musicflux_check.setEnabled(False)
        self.musicflux_check.setGeometry(QtCore.QRect(30, 120, 211, 18))
        self.musicflux_check.setText(QtGui.QApplication.translate("Perfconfig_Dialog", "Flow and Pollution Time Series", None, QtGui.QApplication.UnicodeUTF8))
        self.musicflux_check.setObjectName(_fromUtf8("musicflux_check"))
        self.musicexport_lbl = QtGui.QLabel(self.simulationconfig_widget_4)
        self.musicexport_lbl.setGeometry(QtCore.QRect(10, 70, 141, 16))
        self.musicexport_lbl.setText(QtGui.QApplication.translate("Perfconfig_Dialog", "Select Results to Export:", None, QtGui.QApplication.UnicodeUTF8))
        self.musicexport_lbl.setObjectName(_fromUtf8("musicexport_lbl"))
        self.musictte_check = QtGui.QCheckBox(self.simulationconfig_widget_4)
        self.musictte_check.setEnabled(False)
        self.musictte_check.setGeometry(QtCore.QRect(30, 95, 221, 18))
        self.musictte_check.setText(QtGui.QApplication.translate("Perfconfig_Dialog", "Treatment Train Effectiveness", None, QtGui.QApplication.UnicodeUTF8))
        self.musictte_check.setObjectName(_fromUtf8("musictte_check"))
        self.musicauto_check = QtGui.QCheckBox(self.simulationconfig_widget_4)
        self.musicauto_check.setEnabled(False)
        self.musicauto_check.setGeometry(QtCore.QRect(10, 10, 311, 18))
        self.musicauto_check.setText(QtGui.QApplication.translate("Perfconfig_Dialog", "AutoRun MUSIC Simulation Files", None, QtGui.QApplication.UnicodeUTF8))
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
        self.general_descr.setHtml(QtGui.QApplication.translate("Perfconfig_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Setup performance assessment for planning outputs.</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
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
        self.lcc_title.setText(QtGui.QApplication.translate("Perfconfig_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Life Cycle Costing</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.lcc_title.setObjectName(_fromUtf8("lcc_title"))
        self.verticalLayout_21.addWidget(self.lcc_title)
        self.lcc_widget = QtGui.QWidget(self.scrollAreaWidgetContents_11)
        self.lcc_widget.setMinimumSize(QtCore.QSize(0, 100))
        self.lcc_widget.setObjectName(_fromUtf8("lcc_widget"))
        self.comingsoon_4 = QtGui.QLabel(self.lcc_widget)
        self.comingsoon_4.setGeometry(QtCore.QRect(100, 30, 111, 20))
        self.comingsoon_4.setText(QtGui.QApplication.translate("Perfconfig_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-style:italic;\">coming soon...</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.comingsoon_4.setObjectName(_fromUtf8("comingsoon_4"))
        self.verticalLayout_21.addWidget(self.lcc_widget)
        self.market_title = QtGui.QLabel(self.scrollAreaWidgetContents_11)
        self.market_title.setMinimumSize(QtCore.QSize(445, 16))
        self.market_title.setMaximumSize(QtCore.QSize(16777215, 16))
        self.market_title.setText(QtGui.QApplication.translate("Perfconfig_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Cost Allocations</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.market_title.setObjectName(_fromUtf8("market_title"))
        self.verticalLayout_21.addWidget(self.market_title)
        self.market_widget = QtGui.QWidget(self.scrollAreaWidgetContents_11)
        self.market_widget.setMinimumSize(QtCore.QSize(0, 100))
        self.market_widget.setObjectName(_fromUtf8("market_widget"))
        self.comingsoon_5 = QtGui.QLabel(self.market_widget)
        self.comingsoon_5.setGeometry(QtCore.QRect(90, 40, 111, 20))
        self.comingsoon_5.setText(QtGui.QApplication.translate("Perfconfig_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-style:italic;\">coming soon...</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
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
        self.general_descr_5.setHtml(QtGui.QApplication.translate("Perfconfig_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Undertake life cycle costing of the WSUD options and assess the financial implications.</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
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
        self.lcov_title.setText(QtGui.QApplication.translate("Perfconfig_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Land Cover Analysis</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.lcov_title.setObjectName(_fromUtf8("lcov_title"))
        self.verticalLayout_13.addWidget(self.lcov_title)
        self.lcov_widget = QtGui.QWidget(self.scrollAreaWidgetContents_8)
        self.lcov_widget.setMinimumSize(QtCore.QSize(0, 100))
        self.lcov_widget.setObjectName(_fromUtf8("lcov_widget"))
        self.comingsoon_3 = QtGui.QLabel(self.lcov_widget)
        self.comingsoon_3.setGeometry(QtCore.QRect(70, 40, 111, 20))
        self.comingsoon_3.setText(QtGui.QApplication.translate("Perfconfig_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-style:italic;\">coming soon...</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.comingsoon_3.setObjectName(_fromUtf8("comingsoon_3"))
        self.verticalLayout_13.addWidget(self.lcov_widget)
        self.lst_title = QtGui.QLabel(self.scrollAreaWidgetContents_8)
        self.lst_title.setMinimumSize(QtCore.QSize(445, 16))
        self.lst_title.setMaximumSize(QtCore.QSize(16777215, 16))
        self.lst_title.setText(QtGui.QApplication.translate("Perfconfig_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Land Surface Temperatures</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.lst_title.setObjectName(_fromUtf8("lst_title"))
        self.verticalLayout_13.addWidget(self.lst_title)
        self.lst_widget = QtGui.QWidget(self.scrollAreaWidgetContents_8)
        self.lst_widget.setMinimumSize(QtCore.QSize(0, 100))
        self.lst_widget.setObjectName(_fromUtf8("lst_widget"))
        self.comingsoon_2 = QtGui.QLabel(self.lst_widget)
        self.comingsoon_2.setGeometry(QtCore.QRect(70, 30, 111, 20))
        self.comingsoon_2.setText(QtGui.QApplication.translate("Perfconfig_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-style:italic;\">coming soon...</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.comingsoon_2.setObjectName(_fromUtf8("comingsoon_2"))
        self.verticalLayout_13.addWidget(self.lst_widget)
        self.lstat_title = QtGui.QLabel(self.scrollAreaWidgetContents_8)
        self.lstat_title.setMinimumSize(QtCore.QSize(445, 16))
        self.lstat_title.setMaximumSize(QtCore.QSize(16777215, 16))
        self.lstat_title.setText(QtGui.QApplication.translate("Perfconfig_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Land Surface to Air Temperature Relationship</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.lstat_title.setObjectName(_fromUtf8("lstat_title"))
        self.verticalLayout_13.addWidget(self.lstat_title)
        self.lstat_widget = QtGui.QWidget(self.scrollAreaWidgetContents_8)
        self.lstat_widget.setMinimumSize(QtCore.QSize(0, 100))
        self.lstat_widget.setObjectName(_fromUtf8("lstat_widget"))
        self.comingsoon_1 = QtGui.QLabel(self.lstat_widget)
        self.comingsoon_1.setGeometry(QtCore.QRect(70, 30, 111, 20))
        self.comingsoon_1.setText(QtGui.QApplication.translate("Perfconfig_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-style:italic;\">coming soon...</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
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
        self.general_descr_2.setHtml(QtGui.QApplication.translate("Perfconfig_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Conduct a simple microclimate analysis of the modelled development. Produces an air temperature distribution map.</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
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
        self.scrollAreaWidgetContents_10.setGeometry(QtCore.QRect(0, 0, 463, 340))
        self.scrollAreaWidgetContents_10.setObjectName(_fromUtf8("scrollAreaWidgetContents_10"))
        self.verticalLayout_19 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents_10)
        self.verticalLayout_19.setObjectName(_fromUtf8("verticalLayout_19"))
        self.simulationconfig_lbl_8 = QtGui.QLabel(self.scrollAreaWidgetContents_10)
        self.simulationconfig_lbl_8.setEnabled(False)
        self.simulationconfig_lbl_8.setMinimumSize(QtCore.QSize(445, 16))
        self.simulationconfig_lbl_8.setMaximumSize(QtCore.QSize(16777215, 16))
        self.simulationconfig_lbl_8.setText(QtGui.QApplication.translate("Perfconfig_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Water Demand Downscaling</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.simulationconfig_lbl_8.setObjectName(_fromUtf8("simulationconfig_lbl_8"))
        self.verticalLayout_19.addWidget(self.simulationconfig_lbl_8)
        self.outputconfig_widget_8 = QtGui.QWidget(self.scrollAreaWidgetContents_10)
        self.outputconfig_widget_8.setMinimumSize(QtCore.QSize(0, 300))
        self.outputconfig_widget_8.setObjectName(_fromUtf8("outputconfig_widget_8"))
        self.dagg_dp_noonlbl = QtGui.QLabel(self.outputconfig_widget_8)
        self.dagg_dp_noonlbl.setEnabled(False)
        self.dagg_dp_noonlbl.setGeometry(QtCore.QRect(165, 240, 41, 16))
        self.dagg_dp_noonlbl.setToolTip(QtGui.QApplication.translate("Perfconfig_Dialog", "12pm to 6pm", None, QtGui.QApplication.UnicodeUTF8))
        self.dagg_dp_noonlbl.setWhatsThis(QtGui.QApplication.translate("Perfconfig_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Select the minimum water quality requirement to source from when meeting demand.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">PO = Potable Water</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">NP = Non-potable Water</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">RW = Rainwater</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">SW = Stormwater</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">GW = Greywater</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.dagg_dp_noonlbl.setText(QtGui.QApplication.translate("Perfconfig_Dialog", "Noon", None, QtGui.QApplication.UnicodeUTF8))
        self.dagg_dp_noonlbl.setObjectName(_fromUtf8("dagg_dp_noonlbl"))
        self.dagg_sds_vol_lbl = QtGui.QLabel(self.outputconfig_widget_8)
        self.dagg_sds_vol_lbl.setEnabled(False)
        self.dagg_sds_vol_lbl.setGeometry(QtCore.QRect(75, 75, 151, 16))
        self.dagg_sds_vol_lbl.setWhatsThis(QtGui.QApplication.translate("Perfconfig_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Select the minimum water quality requirement to source from when meeting demand.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">PO = Potable Water</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">NP = Non-potable Water</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">RW = Rainwater</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">SW = Stormwater</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">GW = Greywater</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.dagg_sds_vol_lbl.setText(QtGui.QApplication.translate("Perfconfig_Dialog", "Volume used during day time:", None, QtGui.QApplication.UnicodeUTF8))
        self.dagg_sds_vol_lbl.setObjectName(_fromUtf8("dagg_sds_vol_lbl"))
        self.dagg_dp_nightlbl = QtGui.QLabel(self.outputconfig_widget_8)
        self.dagg_dp_nightlbl.setEnabled(False)
        self.dagg_dp_nightlbl.setGeometry(QtCore.QRect(365, 240, 41, 16))
        self.dagg_dp_nightlbl.setToolTip(QtGui.QApplication.translate("Perfconfig_Dialog", "12am to 6am", None, QtGui.QApplication.UnicodeUTF8))
        self.dagg_dp_nightlbl.setWhatsThis(QtGui.QApplication.translate("Perfconfig_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Select the minimum water quality requirement to source from when meeting demand.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">PO = Potable Water</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">NP = Non-potable Water</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">RW = Rainwater</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">SW = Stormwater</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">GW = Greywater</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.dagg_dp_nightlbl.setText(QtGui.QApplication.translate("Perfconfig_Dialog", "Night", None, QtGui.QApplication.UnicodeUTF8))
        self.dagg_dp_nightlbl.setObjectName(_fromUtf8("dagg_dp_nightlbl"))
        self.dagg_dp_eveninglbl = QtGui.QLabel(self.outputconfig_widget_8)
        self.dagg_dp_eveninglbl.setEnabled(False)
        self.dagg_dp_eveninglbl.setGeometry(QtCore.QRect(260, 240, 41, 16))
        self.dagg_dp_eveninglbl.setToolTip(QtGui.QApplication.translate("Perfconfig_Dialog", "6pm to 12am", None, QtGui.QApplication.UnicodeUTF8))
        self.dagg_dp_eveninglbl.setWhatsThis(QtGui.QApplication.translate("Perfconfig_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Select the minimum water quality requirement to source from when meeting demand.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">PO = Potable Water</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">NP = Non-potable Water</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">RW = Rainwater</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">SW = Stormwater</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">GW = Greywater</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.dagg_dp_eveninglbl.setText(QtGui.QApplication.translate("Perfconfig_Dialog", "Evening", None, QtGui.QApplication.UnicodeUTF8))
        self.dagg_dp_eveninglbl.setObjectName(_fromUtf8("dagg_dp_eveninglbl"))
        self.dagg_sds_vol_spin = QtGui.QSpinBox(self.outputconfig_widget_8)
        self.dagg_sds_vol_spin.setEnabled(False)
        self.dagg_sds_vol_spin.setGeometry(QtCore.QRect(225, 75, 51, 16))
        self.dagg_sds_vol_spin.setSuffix(QtGui.QApplication.translate("Perfconfig_Dialog", "%", None, QtGui.QApplication.UnicodeUTF8))
        self.dagg_sds_vol_spin.setPrefix(_fromUtf8(""))
        self.dagg_sds_vol_spin.setMaximum(100)
        self.dagg_sds_vol_spin.setObjectName(_fromUtf8("dagg_sds_vol_spin"))
        self.dagg_dp_eveningspin = QtGui.QDoubleSpinBox(self.outputconfig_widget_8)
        self.dagg_dp_eveningspin.setEnabled(False)
        self.dagg_dp_eveningspin.setGeometry(QtCore.QRect(256, 220, 51, 16))
        self.dagg_dp_eveningspin.setObjectName(_fromUtf8("dagg_dp_eveningspin"))
        self.dagg_dp_noonpic = QtGui.QLabel(self.outputconfig_widget_8)
        self.dagg_dp_noonpic.setGeometry(QtCore.QRect(155, 175, 41, 41))
        self.dagg_dp_noonpic.setToolTip(QtGui.QApplication.translate("Perfconfig_Dialog", "approx. 6am to 12pm", None, QtGui.QApplication.UnicodeUTF8))
        self.dagg_dp_noonpic.setWhatsThis(QtGui.QApplication.translate("Perfconfig_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Select the minimum water quality requirement to source from when meeting demand.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">PO = Potable Water</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">NP = Non-potable Water</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">RW = Rainwater</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">SW = Stormwater</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">GW = Greywater</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.dagg_dp_noonpic.setText(_fromUtf8(""))
        self.dagg_dp_noonpic.setPixmap(QtGui.QPixmap(_fromUtf8("noon-small.png")))
        self.dagg_dp_noonpic.setObjectName(_fromUtf8("dagg_dp_noonpic"))
        self.dagg_sds_vol_lbl2 = QtGui.QLabel(self.outputconfig_widget_8)
        self.dagg_sds_vol_lbl2.setEnabled(False)
        self.dagg_sds_vol_lbl2.setGeometry(QtCore.QRect(285, 75, 111, 16))
        self.dagg_sds_vol_lbl2.setWhatsThis(QtGui.QApplication.translate("Perfconfig_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Select the minimum water quality requirement to source from when meeting demand.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">PO = Potable Water</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">NP = Non-potable Water</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">RW = Rainwater</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">SW = Stormwater</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">GW = Greywater</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.dagg_sds_vol_lbl2.setText(QtGui.QApplication.translate("Perfconfig_Dialog", "of Total Daily Demand", None, QtGui.QApplication.UnicodeUTF8))
        self.dagg_sds_vol_lbl2.setObjectName(_fromUtf8("dagg_sds_vol_lbl2"))
        self.dagg_dp_morningspin = QtGui.QDoubleSpinBox(self.outputconfig_widget_8)
        self.dagg_dp_morningspin.setEnabled(False)
        self.dagg_dp_morningspin.setGeometry(QtCore.QRect(56, 220, 51, 16))
        self.dagg_dp_morningspin.setObjectName(_fromUtf8("dagg_dp_morningspin"))
        self.dagg_sds_radio = QtGui.QRadioButton(self.outputconfig_widget_8)
        self.dagg_sds_radio.setEnabled(False)
        self.dagg_sds_radio.setGeometry(QtCore.QRect(25, 30, 151, 17))
        self.dagg_sds_radio.setText(QtGui.QApplication.translate("Perfconfig_Dialog", "Simple Linear Downscaling", None, QtGui.QApplication.UnicodeUTF8))
        self.dagg_sds_radio.setObjectName(_fromUtf8("dagg_sds_radio"))
        self.dagg_method_lbl = QtGui.QLabel(self.outputconfig_widget_8)
        self.dagg_method_lbl.setEnabled(False)
        self.dagg_method_lbl.setGeometry(QtCore.QRect(15, 10, 151, 16))
        self.dagg_method_lbl.setWhatsThis(QtGui.QApplication.translate("Perfconfig_Dialog", "Based on Aquacycle\'s calibration parameter. If soil moisture drops below this value, irrigation will occur to refill the soil moisture store. Specify as a proportion (e.g. 0.5 for 50%)", None, QtGui.QApplication.UnicodeUTF8))
        self.dagg_method_lbl.setText(QtGui.QApplication.translate("Perfconfig_Dialog", "Select preferred method", None, QtGui.QApplication.UnicodeUTF8))
        self.dagg_method_lbl.setObjectName(_fromUtf8("dagg_method_lbl"))
        self.dagg_dp_nightspin = QtGui.QDoubleSpinBox(self.outputconfig_widget_8)
        self.dagg_dp_nightspin.setEnabled(False)
        self.dagg_dp_nightspin.setGeometry(QtCore.QRect(356, 220, 51, 16))
        self.dagg_dp_nightspin.setObjectName(_fromUtf8("dagg_dp_nightspin"))
        self.dagg_dp_predef_check = QtGui.QCheckBox(self.outputconfig_widget_8)
        self.dagg_dp_predef_check.setEnabled(False)
        self.dagg_dp_predef_check.setGeometry(QtCore.QRect(55, 120, 101, 17))
        self.dagg_dp_predef_check.setText(QtGui.QApplication.translate("Perfconfig_Dialog", "Pre-defined", None, QtGui.QApplication.UnicodeUTF8))
        self.dagg_dp_predef_check.setObjectName(_fromUtf8("dagg_dp_predef_check"))
        self.dagg_dp_radio = QtGui.QRadioButton(self.outputconfig_widget_8)
        self.dagg_dp_radio.setEnabled(False)
        self.dagg_dp_radio.setGeometry(QtCore.QRect(25, 100, 151, 17))
        self.dagg_dp_radio.setText(QtGui.QApplication.translate("Perfconfig_Dialog", "Diurnal Pattern", None, QtGui.QApplication.UnicodeUTF8))
        self.dagg_dp_radio.setObjectName(_fromUtf8("dagg_dp_radio"))
        self.dagg_dp_morningpic = QtGui.QLabel(self.outputconfig_widget_8)
        self.dagg_dp_morningpic.setEnabled(True)
        self.dagg_dp_morningpic.setGeometry(QtCore.QRect(55, 175, 41, 41))
        self.dagg_dp_morningpic.setToolTip(QtGui.QApplication.translate("Perfconfig_Dialog", "approx. 6am to 12pm", None, QtGui.QApplication.UnicodeUTF8))
        self.dagg_dp_morningpic.setWhatsThis(QtGui.QApplication.translate("Perfconfig_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Select the minimum water quality requirement to source from when meeting demand.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">PO = Potable Water</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">NP = Non-potable Water</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">RW = Rainwater</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">SW = Stormwater</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">GW = Greywater</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.dagg_dp_morningpic.setText(_fromUtf8(""))
        self.dagg_dp_morningpic.setPixmap(QtGui.QPixmap(_fromUtf8("morning-small.png")))
        self.dagg_dp_morningpic.setObjectName(_fromUtf8("dagg_dp_morningpic"))
        self.dagg_dp_noonspin = QtGui.QDoubleSpinBox(self.outputconfig_widget_8)
        self.dagg_dp_noonspin.setEnabled(False)
        self.dagg_dp_noonspin.setGeometry(QtCore.QRect(156, 220, 51, 16))
        self.dagg_dp_noonspin.setObjectName(_fromUtf8("dagg_dp_noonspin"))
        self.dagg_dp_pdbox = QtGui.QComboBox(self.outputconfig_widget_8)
        self.dagg_dp_pdbox.setEnabled(False)
        self.dagg_dp_pdbox.setGeometry(QtCore.QRect(165, 120, 181, 16))
        self.dagg_dp_pdbox.setObjectName(_fromUtf8("dagg_dp_pdbox"))
        self.dagg_dp_pdbox.addItem(_fromUtf8(""))
        self.dagg_dp_pdbox.setItemText(0, QtGui.QApplication.translate("Perfconfig_Dialog", "Gujer et al.", None, QtGui.QApplication.UnicodeUTF8))
        self.dagg_dp_pdbox.addItem(_fromUtf8(""))
        self.dagg_dp_pdbox.setItemText(1, QtGui.QApplication.translate("Perfconfig_Dialog", "Melbourne Water Guide", None, QtGui.QApplication.UnicodeUTF8))
        self.dagg_dp_nightpic = QtGui.QLabel(self.outputconfig_widget_8)
        self.dagg_dp_nightpic.setGeometry(QtCore.QRect(355, 175, 41, 41))
        self.dagg_dp_nightpic.setToolTip(QtGui.QApplication.translate("Perfconfig_Dialog", "approx. 6am to 12pm", None, QtGui.QApplication.UnicodeUTF8))
        self.dagg_dp_nightpic.setWhatsThis(QtGui.QApplication.translate("Perfconfig_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Select the minimum water quality requirement to source from when meeting demand.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">PO = Potable Water</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">NP = Non-potable Water</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">RW = Rainwater</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">SW = Stormwater</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">GW = Greywater</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.dagg_dp_nightpic.setText(_fromUtf8(""))
        self.dagg_dp_nightpic.setPixmap(QtGui.QPixmap(_fromUtf8("night-small.png")))
        self.dagg_dp_nightpic.setObjectName(_fromUtf8("dagg_dp_nightpic"))
        self.dagg_dp_custom_check = QtGui.QCheckBox(self.outputconfig_widget_8)
        self.dagg_dp_custom_check.setEnabled(False)
        self.dagg_dp_custom_check.setGeometry(QtCore.QRect(55, 150, 101, 17))
        self.dagg_dp_custom_check.setText(QtGui.QApplication.translate("Perfconfig_Dialog", "Custom Factors", None, QtGui.QApplication.UnicodeUTF8))
        self.dagg_dp_custom_check.setObjectName(_fromUtf8("dagg_dp_custom_check"))
        self.dagg_sds_subp_check = QtGui.QCheckBox(self.outputconfig_widget_8)
        self.dagg_sds_subp_check.setEnabled(False)
        self.dagg_sds_subp_check.setGeometry(QtCore.QRect(55, 50, 361, 17))
        self.dagg_sds_subp_check.setText(QtGui.QApplication.translate("Perfconfig_Dialog", "Sub-proportion daily demand into day and nighttime volumes", None, QtGui.QApplication.UnicodeUTF8))
        self.dagg_sds_subp_check.setObjectName(_fromUtf8("dagg_sds_subp_check"))
        self.dagg_dp_eveningpic = QtGui.QLabel(self.outputconfig_widget_8)
        self.dagg_dp_eveningpic.setGeometry(QtCore.QRect(255, 175, 41, 41))
        self.dagg_dp_eveningpic.setToolTip(QtGui.QApplication.translate("Perfconfig_Dialog", "approx. 6am to 12pm", None, QtGui.QApplication.UnicodeUTF8))
        self.dagg_dp_eveningpic.setWhatsThis(QtGui.QApplication.translate("Perfconfig_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Select the minimum water quality requirement to source from when meeting demand.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">PO = Potable Water</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">NP = Non-potable Water</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">RW = Rainwater</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">SW = Stormwater</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">GW = Greywater</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.dagg_dp_eveningpic.setText(_fromUtf8(""))
        self.dagg_dp_eveningpic.setPixmap(QtGui.QPixmap(_fromUtf8("evening-small.png")))
        self.dagg_dp_eveningpic.setObjectName(_fromUtf8("dagg_dp_eveningpic"))
        self.dagg_dp_morninglbl = QtGui.QLabel(self.outputconfig_widget_8)
        self.dagg_dp_morninglbl.setEnabled(False)
        self.dagg_dp_morninglbl.setGeometry(QtCore.QRect(60, 240, 41, 16))
        self.dagg_dp_morninglbl.setToolTip(QtGui.QApplication.translate("Perfconfig_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">6am to 12pm</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.dagg_dp_morninglbl.setWhatsThis(QtGui.QApplication.translate("Perfconfig_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Select the minimum water quality requirement to source from when meeting demand.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">PO = Potable Water</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">NP = Non-potable Water</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">RW = Rainwater</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">SW = Stormwater</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">GW = Greywater</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.dagg_dp_morninglbl.setText(QtGui.QApplication.translate("Perfconfig_Dialog", "Morning", None, QtGui.QApplication.UnicodeUTF8))
        self.dagg_dp_morninglbl.setObjectName(_fromUtf8("dagg_dp_morninglbl"))
        self.verticalLayout_19.addWidget(self.outputconfig_widget_8)
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
        self.general_descr_4.setHtml(QtGui.QApplication.translate("Perfconfig_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Link a water supply network model to UrbanBEATS to assess the impact of the current options on the resulting water distribution network.</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
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
        self.simulationconfig_lbl_4.setText(QtGui.QApplication.translate("Perfconfig_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Urban Hydrology</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.simulationconfig_lbl_4.setObjectName(_fromUtf8("simulationconfig_lbl_4"))
        self.verticalLayout_25.addWidget(self.simulationconfig_lbl_4)
        self.outputconfig_widget_4 = QtGui.QWidget(self.scrollAreaWidgetContents_12)
        self.outputconfig_widget_4.setMinimumSize(QtCore.QSize(0, 100))
        self.outputconfig_widget_4.setObjectName(_fromUtf8("outputconfig_widget_4"))
        self.comingsoon_6 = QtGui.QLabel(self.outputconfig_widget_4)
        self.comingsoon_6.setEnabled(False)
        self.comingsoon_6.setGeometry(QtCore.QRect(40, 30, 111, 20))
        self.comingsoon_6.setText(QtGui.QApplication.translate("Perfconfig_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-style:italic;\">coming soon...</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
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
        self.general_descr_6.setHtml(QtGui.QApplication.translate("Perfconfig_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Conduct a full long-term integrated water quantity and mass balance simulation of the current option(s).</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
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
        self.remarks.setText(QtGui.QApplication.translate("Perfconfig_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-style:italic;\">UrbanBEATS v1.0 - (C) 2013 Peter M. Bach </span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.remarks.setObjectName(_fromUtf8("remarks"))
        self.horizontalLayout_7.addWidget(self.remarks)
        self.buttonBox = QtGui.QDialogButtonBox(self.footer_widget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.horizontalLayout_7.addWidget(self.buttonBox)
        self.pushButton = QtGui.QPushButton(self.footer_widget)
        self.pushButton.setWhatsThis(QtGui.QApplication.translate("Perfconfig_Dialog", "Help? What\'s that? Does it taste good? :)", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Perfconfig_Dialog", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout_7.addWidget(self.pushButton)
        self.verticalLayout.addWidget(self.footer_widget)

        self.retranslateUi(Perfconfig_Dialog)
        self.main_input_widget.setCurrentIndex(0)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Perfconfig_Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Perfconfig_Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Perfconfig_Dialog)

    def retranslateUi(self, Perfconfig_Dialog):
        self.main_input_widget.setTabText(self.main_input_widget.indexOf(self.tab_2), QtGui.QApplication.translate("Perfconfig_Dialog", "Select Analyses", None, QtGui.QApplication.UnicodeUTF8))
        self.main_input_widget.setTabText(self.main_input_widget.indexOf(self.generaltab), QtGui.QApplication.translate("Perfconfig_Dialog", "MUSIC Simulation", None, QtGui.QApplication.UnicodeUTF8))
        self.main_input_widget.setTabText(self.main_input_widget.indexOf(self.tab_4), QtGui.QApplication.translate("Perfconfig_Dialog", "Economics", None, QtGui.QApplication.UnicodeUTF8))
        self.main_input_widget.setTabText(self.main_input_widget.indexOf(self.tab), QtGui.QApplication.translate("Perfconfig_Dialog", "Microclimate", None, QtGui.QApplication.UnicodeUTF8))
        self.main_input_widget.setTabText(self.main_input_widget.indexOf(self.tab_3), QtGui.QApplication.translate("Perfconfig_Dialog", "Water Supply", None, QtGui.QApplication.UnicodeUTF8))
        self.main_input_widget.setTabText(self.main_input_widget.indexOf(self.tab_5), QtGui.QApplication.translate("Perfconfig_Dialog", "Integrated Cycle", None, QtGui.QApplication.UnicodeUTF8))

import guitoolbaricons_rc
