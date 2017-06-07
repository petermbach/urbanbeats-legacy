# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'md_delinblocksgui.ui'
#
# Created: Wed Jun 07 14:37:24 2017
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

class Ui_DelinBlocksDialog(object):
    def setupUi(self, DelinBlocksDialog):
        DelinBlocksDialog.setObjectName(_fromUtf8("DelinBlocksDialog"))
        DelinBlocksDialog.resize(683, 371)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/general/ublogo33.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DelinBlocksDialog.setWindowIcon(icon)
        self.verticalLayout = QtGui.QVBoxLayout(DelinBlocksDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.title_frame_2 = QtGui.QWidget(DelinBlocksDialog)
        self.title_frame_2.setMinimumSize(QtCore.QSize(0, 50))
        self.title_frame_2.setMaximumSize(QtCore.QSize(16777215, 50))
        self.title_frame_2.setObjectName(_fromUtf8("title_frame_2"))
        self.dbtitle_2 = QtGui.QLabel(self.title_frame_2)
        self.dbtitle_2.setGeometry(QtCore.QRect(51, 4, 441, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.dbtitle_2.setFont(font)
        self.dbtitle_2.setObjectName(_fromUtf8("dbtitle_2"))
        self.line_2 = QtGui.QFrame(self.title_frame_2)
        self.line_2.setGeometry(QtCore.QRect(51, 39, 573, 20))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_2.sizePolicy().hasHeightForWidth())
        self.line_2.setSizePolicy(sizePolicy)
        self.line_2.setMinimumSize(QtCore.QSize(573, 0))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.bpmlogo_2 = QtGui.QLabel(self.title_frame_2)
        self.bpmlogo_2.setGeometry(QtCore.QRect(1, -1, 50, 50))
        self.bpmlogo_2.setMaximumSize(QtCore.QSize(50, 50))
        self.bpmlogo_2.setText(_fromUtf8(""))
        self.bpmlogo_2.setPixmap(QtGui.QPixmap(_fromUtf8(":/images/images/D4W-logoBPM.png")))
        self.bpmlogo_2.setObjectName(_fromUtf8("bpmlogo_2"))
        self.dbsubtitle_2 = QtGui.QLabel(self.title_frame_2)
        self.dbsubtitle_2.setGeometry(QtCore.QRect(51, 24, 561, 16))
        self.dbsubtitle_2.setObjectName(_fromUtf8("dbsubtitle_2"))
        self.verticalLayout.addWidget(self.title_frame_2)
        self.widget = QtGui.QWidget(DelinBlocksDialog)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.scrollArea = QtGui.QScrollArea(self.widget)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 471, 1146))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.gensim_widget = QtGui.QWidget(self.scrollAreaWidgetContents)
        self.gensim_widget.setMinimumSize(QtCore.QSize(0, 60))
        self.gensim_widget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.gensim_widget.setObjectName(_fromUtf8("gensim_widget"))
        self.blocksize_lbl = QtGui.QLabel(self.gensim_widget)
        self.blocksize_lbl.setGeometry(QtCore.QRect(20, 29, 101, 16))
        self.blocksize_lbl.setObjectName(_fromUtf8("blocksize_lbl"))
        self.optionsgs_lbl = QtGui.QLabel(self.gensim_widget)
        self.optionsgs_lbl.setGeometry(QtCore.QRect(10, 5, 391, 16))
        self.optionsgs_lbl.setObjectName(_fromUtf8("optionsgs_lbl"))
        self.blocksize_in = QtGui.QSpinBox(self.gensim_widget)
        self.blocksize_in.setGeometry(QtCore.QRect(150, 30, 61, 16))
        self.blocksize_in.setMinimum(200)
        self.blocksize_in.setMaximum(5000)
        self.blocksize_in.setSingleStep(50)
        self.blocksize_in.setProperty("value", 500)
        self.blocksize_in.setObjectName(_fromUtf8("blocksize_in"))
        self.blocksize_auto = QtGui.QCheckBox(self.gensim_widget)
        self.blocksize_auto.setGeometry(QtCore.QRect(230, 30, 171, 17))
        self.blocksize_auto.setObjectName(_fromUtf8("blocksize_auto"))
        self.verticalLayout_3.addWidget(self.gensim_widget)
        self.inputdata_widget = QtGui.QWidget(self.scrollAreaWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inputdata_widget.sizePolicy().hasHeightForWidth())
        self.inputdata_widget.setSizePolicy(sizePolicy)
        self.inputdata_widget.setMinimumSize(QtCore.QSize(0, 540))
        self.inputdata_widget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.inputdata_widget.setObjectName(_fromUtf8("inputdata_widget"))
        self.soc_par1_box = QtGui.QLineEdit(self.inputdata_widget)
        self.soc_par1_box.setGeometry(QtCore.QRect(260, 400, 161, 20))
        self.soc_par1_box.setText(_fromUtf8(""))
        self.soc_par1_box.setObjectName(_fromUtf8("soc_par1_box"))
        self.soc_par1_check = QtGui.QCheckBox(self.inputdata_widget)
        self.soc_par1_check.setGeometry(QtCore.QRect(30, 400, 221, 17))
        self.soc_par1_check.setObjectName(_fromUtf8("soc_par1_check"))
        self.soc_par2_check = QtGui.QCheckBox(self.inputdata_widget)
        self.soc_par2_check.setGeometry(QtCore.QRect(30, 450, 221, 17))
        self.soc_par2_check.setObjectName(_fromUtf8("soc_par2_check"))
        self.soc_par2_box = QtGui.QLineEdit(self.inputdata_widget)
        self.soc_par2_box.setGeometry(QtCore.QRect(260, 450, 161, 20))
        self.soc_par2_box.setText(_fromUtf8(""))
        self.soc_par2_box.setObjectName(_fromUtf8("soc_par2_box"))
        self.optionsadin_lbl = QtGui.QLabel(self.inputdata_widget)
        self.optionsadin_lbl.setGeometry(QtCore.QRect(10, 5, 141, 16))
        self.optionsadin_lbl.setObjectName(_fromUtf8("optionsadin_lbl"))
        self.planmap_check = QtGui.QCheckBox(self.inputdata_widget)
        self.planmap_check.setGeometry(QtCore.QRect(30, 170, 141, 17))
        self.planmap_check.setObjectName(_fromUtf8("planmap_check"))
        self.localmap_check = QtGui.QCheckBox(self.inputdata_widget)
        self.localmap_check.setGeometry(QtCore.QRect(30, 190, 151, 17))
        self.localmap_check.setObjectName(_fromUtf8("localmap_check"))
        self.addinputs_lbl = QtGui.QLabel(self.inputdata_widget)
        self.addinputs_lbl.setGeometry(QtCore.QRect(15, 150, 411, 16))
        self.addinputs_lbl.setObjectName(_fromUtf8("addinputs_lbl"))
        self.roadnet_check = QtGui.QCheckBox(self.inputdata_widget)
        self.roadnet_check.setEnabled(False)
        self.roadnet_check.setGeometry(QtCore.QRect(190, 350, 131, 17))
        self.roadnet_check.setObjectName(_fromUtf8("roadnet_check"))
        self.soc_params_lbl = QtGui.QLabel(self.inputdata_widget)
        self.soc_params_lbl.setGeometry(QtCore.QRect(15, 375, 421, 16))
        self.soc_params_lbl.setObjectName(_fromUtf8("soc_params_lbl"))
        self.popdata_lbl = QtGui.QLabel(self.inputdata_widget)
        self.popdata_lbl.setGeometry(QtCore.QRect(15, 30, 161, 16))
        self.popdata_lbl.setObjectName(_fromUtf8("popdata_lbl"))
        self.spatialanalysis_lbl = QtGui.QLabel(self.inputdata_widget)
        self.spatialanalysis_lbl.setGeometry(QtCore.QRect(15, 500, 171, 16))
        self.spatialanalysis_lbl.setObjectName(_fromUtf8("spatialanalysis_lbl"))
        self.spatialpatches_check = QtGui.QCheckBox(self.inputdata_widget)
        self.spatialpatches_check.setGeometry(QtCore.QRect(30, 520, 191, 17))
        self.spatialpatches_check.setObjectName(_fromUtf8("spatialpatches_check"))
        self.spatialstats_check = QtGui.QCheckBox(self.inputdata_widget)
        self.spatialstats_check.setGeometry(QtCore.QRect(210, 520, 191, 17))
        self.spatialstats_check.setObjectName(_fromUtf8("spatialstats_check"))
        self.socpar1_customize = QtGui.QWidget(self.inputdata_widget)
        self.socpar1_customize.setGeometry(QtCore.QRect(50, 425, 341, 16))
        self.socpar1_customize.setObjectName(_fromUtf8("socpar1_customize"))
        self.socpar1binary_radio = QtGui.QRadioButton(self.socpar1_customize)
        self.socpar1binary_radio.setGeometry(QtCore.QRect(140, 0, 91, 17))
        self.socpar1binary_radio.setObjectName(_fromUtf8("socpar1binary_radio"))
        self.socpar1prop_radio = QtGui.QRadioButton(self.socpar1_customize)
        self.socpar1prop_radio.setGeometry(QtCore.QRect(240, 0, 91, 17))
        self.socpar1prop_radio.setObjectName(_fromUtf8("socpar1prop_radio"))
        self.socpar1format_lbl = QtGui.QLabel(self.socpar1_customize)
        self.socpar1format_lbl.setGeometry(QtCore.QRect(20, 0, 91, 16))
        self.socpar1format_lbl.setObjectName(_fromUtf8("socpar1format_lbl"))
        self.socpar2_customize = QtGui.QWidget(self.inputdata_widget)
        self.socpar2_customize.setGeometry(QtCore.QRect(50, 475, 341, 16))
        self.socpar2_customize.setObjectName(_fromUtf8("socpar2_customize"))
        self.socpar2binary_radio = QtGui.QRadioButton(self.socpar2_customize)
        self.socpar2binary_radio.setGeometry(QtCore.QRect(140, 0, 91, 17))
        self.socpar2binary_radio.setObjectName(_fromUtf8("socpar2binary_radio"))
        self.socpar2prop_radio = QtGui.QRadioButton(self.socpar2_customize)
        self.socpar2prop_radio.setGeometry(QtCore.QRect(240, 0, 91, 17))
        self.socpar2prop_radio.setObjectName(_fromUtf8("socpar2prop_radio"))
        self.socpar2format_lbl = QtGui.QLabel(self.socpar2_customize)
        self.socpar2format_lbl.setGeometry(QtCore.QRect(20, 0, 91, 16))
        self.socpar2format_lbl.setObjectName(_fromUtf8("socpar2format_lbl"))
        self.rivers_check = QtGui.QCheckBox(self.inputdata_widget)
        self.rivers_check.setGeometry(QtCore.QRect(30, 255, 141, 17))
        self.rivers_check.setObjectName(_fromUtf8("rivers_check"))
        self.lakes_check = QtGui.QCheckBox(self.inputdata_widget)
        self.lakes_check.setGeometry(QtCore.QRect(30, 275, 151, 17))
        self.lakes_check.setObjectName(_fromUtf8("lakes_check"))
        self.employment_check = QtGui.QCheckBox(self.inputdata_widget)
        self.employment_check.setGeometry(QtCore.QRect(30, 210, 141, 17))
        self.employment_check.setObjectName(_fromUtf8("employment_check"))
        self.addinputs_lbl_2 = QtGui.QLabel(self.inputdata_widget)
        self.addinputs_lbl_2.setGeometry(QtCore.QRect(15, 235, 361, 16))
        self.addinputs_lbl_2.setObjectName(_fromUtf8("addinputs_lbl_2"))
        self.drainage_check = QtGui.QCheckBox(self.inputdata_widget)
        self.drainage_check.setEnabled(True)
        self.drainage_check.setGeometry(QtCore.QRect(30, 350, 151, 17))
        self.drainage_check.setObjectName(_fromUtf8("drainage_check"))
        self.groundwater_check = QtGui.QCheckBox(self.inputdata_widget)
        self.groundwater_check.setGeometry(QtCore.QRect(30, 295, 151, 17))
        self.groundwater_check.setObjectName(_fromUtf8("groundwater_check"))
        self.soildata_lbl = QtGui.QLabel(self.inputdata_widget)
        self.soildata_lbl.setGeometry(QtCore.QRect(15, 55, 161, 16))
        self.soildata_lbl.setObjectName(_fromUtf8("soildata_lbl"))
        self.pop_options_widget = QtGui.QWidget(self.inputdata_widget)
        self.pop_options_widget.setGeometry(QtCore.QRect(180, 30, 251, 20))
        self.pop_options_widget.setObjectName(_fromUtf8("pop_options_widget"))
        self.popdata_densradio = QtGui.QRadioButton(self.pop_options_widget)
        self.popdata_densradio.setGeometry(QtCore.QRect(130, 0, 111, 17))
        self.popdata_densradio.setWhatsThis(_fromUtf8(""))
        self.popdata_densradio.setObjectName(_fromUtf8("popdata_densradio"))
        self.popdata_totradio = QtGui.QRadioButton(self.pop_options_widget)
        self.popdata_totradio.setGeometry(QtCore.QRect(20, 0, 101, 17))
        self.popdata_totradio.setObjectName(_fromUtf8("popdata_totradio"))
        self.soil_options_widget = QtGui.QWidget(self.inputdata_widget)
        self.soil_options_widget.setGeometry(QtCore.QRect(180, 55, 251, 41))
        self.soil_options_widget.setObjectName(_fromUtf8("soil_options_widget"))
        self.soildata_infil = QtGui.QRadioButton(self.soil_options_widget)
        self.soildata_infil.setGeometry(QtCore.QRect(130, 0, 111, 17))
        self.soildata_infil.setObjectName(_fromUtf8("soildata_infil"))
        self.soildata_classify = QtGui.QRadioButton(self.soil_options_widget)
        self.soildata_classify.setGeometry(QtCore.QRect(20, 0, 101, 17))
        self.soildata_classify.setObjectName(_fromUtf8("soildata_classify"))
        self.soildata_unitscombo = QtGui.QComboBox(self.soil_options_widget)
        self.soildata_unitscombo.setGeometry(QtCore.QRect(170, 20, 61, 16))
        self.soildata_unitscombo.setObjectName(_fromUtf8("soildata_unitscombo"))
        self.soildata_unitscombo.addItem(_fromUtf8(""))
        self.soildata_unitscombo.addItem(_fromUtf8(""))
        self.soildataunits_lbl = QtGui.QLabel(self.soil_options_widget)
        self.soildataunits_lbl.setGeometry(QtCore.QRect(130, 20, 31, 20))
        self.soildataunits_lbl.setObjectName(_fromUtf8("soildataunits_lbl"))
        self.groundwater_datumlbl = QtGui.QLabel(self.inputdata_widget)
        self.groundwater_datumlbl.setGeometry(QtCore.QRect(190, 295, 81, 20))
        self.groundwater_datumlbl.setObjectName(_fromUtf8("groundwater_datumlbl"))
        self.addinputs_lbl_3 = QtGui.QLabel(self.inputdata_widget)
        self.addinputs_lbl_3.setGeometry(QtCore.QRect(15, 325, 361, 16))
        self.addinputs_lbl_3.setObjectName(_fromUtf8("addinputs_lbl_3"))
        self.elevdata_lbl = QtGui.QLabel(self.inputdata_widget)
        self.elevdata_lbl.setGeometry(QtCore.QRect(15, 100, 161, 16))
        self.elevdata_lbl.setObjectName(_fromUtf8("elevdata_lbl"))
        self.elev_options_widget = QtGui.QWidget(self.inputdata_widget)
        self.elev_options_widget.setGeometry(QtCore.QRect(180, 100, 251, 41))
        self.elev_options_widget.setObjectName(_fromUtf8("elev_options_widget"))
        self.elev_custom = QtGui.QRadioButton(self.elev_options_widget)
        self.elev_custom.setGeometry(QtCore.QRect(20, 20, 71, 17))
        self.elev_custom.setWhatsThis(_fromUtf8(""))
        self.elev_custom.setObjectName(_fromUtf8("elev_custom"))
        self.elev_sealevel = QtGui.QRadioButton(self.elev_options_widget)
        self.elev_sealevel.setGeometry(QtCore.QRect(20, 0, 101, 17))
        self.elev_sealevel.setObjectName(_fromUtf8("elev_sealevel"))
        self.elev_referencebox = QtGui.QLineEdit(self.elev_options_widget)
        self.elev_referencebox.setGeometry(QtCore.QRect(90, 20, 51, 16))
        self.elev_referencebox.setObjectName(_fromUtf8("elev_referencebox"))
        self.elev_referencelbl = QtGui.QLabel(self.elev_options_widget)
        self.elev_referencelbl.setGeometry(QtCore.QRect(150, 20, 91, 16))
        self.elev_referencelbl.setObjectName(_fromUtf8("elev_referencelbl"))
        self.groundwater_datumcombo = QtGui.QComboBox(self.inputdata_widget)
        self.groundwater_datumcombo.setGeometry(QtCore.QRect(280, 295, 121, 16))
        self.groundwater_datumcombo.setObjectName(_fromUtf8("groundwater_datumcombo"))
        self.groundwater_datumcombo.addItem(_fromUtf8(""))
        self.groundwater_datumcombo.addItem(_fromUtf8(""))
        self.job_options_widget = QtGui.QWidget(self.inputdata_widget)
        self.job_options_widget.setGeometry(QtCore.QRect(180, 210, 251, 20))
        self.job_options_widget.setObjectName(_fromUtf8("job_options_widget"))
        self.jobdata_densradio = QtGui.QRadioButton(self.job_options_widget)
        self.jobdata_densradio.setGeometry(QtCore.QRect(130, 0, 111, 17))
        self.jobdata_densradio.setObjectName(_fromUtf8("jobdata_densradio"))
        self.jobdata_totradio = QtGui.QRadioButton(self.job_options_widget)
        self.jobdata_totradio.setGeometry(QtCore.QRect(20, 0, 101, 17))
        self.jobdata_totradio.setObjectName(_fromUtf8("jobdata_totradio"))
        self.verticalLayout_3.addWidget(self.inputdata_widget)
        self.connectivity_widget = QtGui.QWidget(self.scrollAreaWidgetContents)
        self.connectivity_widget.setMinimumSize(QtCore.QSize(0, 300))
        self.connectivity_widget.setObjectName(_fromUtf8("connectivity_widget"))
        self.radioVNeum = QtGui.QRadioButton(self.connectivity_widget)
        self.radioVNeum.setGeometry(QtCore.QRect(80, 110, 101, 16))
        self.radioVNeum.setWhatsThis(_fromUtf8(""))
        self.radioVNeum.setChecked(False)
        self.radioVNeum.setObjectName(_fromUtf8("radioVNeum"))
        self.img_Moore = QtGui.QLabel(self.connectivity_widget)
        self.img_Moore.setGeometry(QtCore.QRect(30, 55, 41, 41))
        self.img_Moore.setText(_fromUtf8(""))
        self.img_Moore.setPixmap(QtGui.QPixmap(_fromUtf8(":/images/images/D4W-MooreNH.png")))
        self.img_Moore.setObjectName(_fromUtf8("img_Moore"))
        self.neighb_lbl = QtGui.QLabel(self.connectivity_widget)
        self.neighb_lbl.setGeometry(QtCore.QRect(20, 30, 231, 16))
        self.neighb_lbl.setObjectName(_fromUtf8("neighb_lbl"))
        self.img_vNeum = QtGui.QLabel(self.connectivity_widget)
        self.img_vNeum.setGeometry(QtCore.QRect(30, 100, 41, 41))
        self.img_vNeum.setText(_fromUtf8(""))
        self.img_vNeum.setPixmap(QtGui.QPixmap(_fromUtf8(":/images/images/D4W-vNeumann.png")))
        self.img_vNeum.setObjectName(_fromUtf8("img_vNeum"))
        self.radioMoore = QtGui.QRadioButton(self.connectivity_widget)
        self.radioMoore.setEnabled(True)
        self.radioMoore.setGeometry(QtCore.QRect(80, 65, 82, 16))
        self.radioMoore.setWhatsThis(_fromUtf8(""))
        self.radioMoore.setCheckable(True)
        self.radioMoore.setObjectName(_fromUtf8("radioMoore"))
        self.optionsmc_lbl = QtGui.QLabel(self.connectivity_widget)
        self.optionsmc_lbl.setGeometry(QtCore.QRect(10, 5, 231, 16))
        self.optionsmc_lbl.setObjectName(_fromUtf8("optionsmc_lbl"))
        self.flowpath_lbl = QtGui.QLabel(self.connectivity_widget)
        self.flowpath_lbl.setGeometry(QtCore.QRect(20, 150, 131, 16))
        self.flowpath_lbl.setObjectName(_fromUtf8("flowpath_lbl"))
        self.flowpath_combo = QtGui.QComboBox(self.connectivity_widget)
        self.flowpath_combo.setGeometry(QtCore.QRect(30, 175, 271, 22))
        self.flowpath_combo.setObjectName(_fromUtf8("flowpath_combo"))
        self.flowpath_combo.addItem(_fromUtf8(""))
        self.flowpath_combo.addItem(_fromUtf8(""))
        self.demsmooth_check = QtGui.QCheckBox(self.connectivity_widget)
        self.demsmooth_check.setGeometry(QtCore.QRect(30, 210, 161, 17))
        self.demsmooth_check.setObjectName(_fromUtf8("demsmooth_check"))
        self.demsmooth_spin = QtGui.QSpinBox(self.connectivity_widget)
        self.demsmooth_spin.setGeometry(QtCore.QRect(190, 210, 31, 20))
        self.demsmooth_spin.setMinimum(1)
        self.demsmooth_spin.setMaximum(2)
        self.demsmooth_spin.setObjectName(_fromUtf8("demsmooth_spin"))
        self.neighb_vnfp_check = QtGui.QCheckBox(self.connectivity_widget)
        self.neighb_vnfp_check.setGeometry(QtCore.QRect(210, 100, 191, 17))
        self.neighb_vnfp_check.setObjectName(_fromUtf8("neighb_vnfp_check"))
        self.neighb_vnpd_check = QtGui.QCheckBox(self.connectivity_widget)
        self.neighb_vnpd_check.setGeometry(QtCore.QRect(210, 120, 191, 17))
        self.neighb_vnpd_check.setObjectName(_fromUtf8("neighb_vnpd_check"))
        self.neighb_lbl2 = QtGui.QLabel(self.connectivity_widget)
        self.neighb_lbl2.setGeometry(QtCore.QRect(180, 80, 221, 16))
        self.neighb_lbl2.setObjectName(_fromUtf8("neighb_lbl2"))
        self.use_river = QtGui.QCheckBox(self.connectivity_widget)
        self.use_river.setGeometry(QtCore.QRect(30, 240, 361, 17))
        self.use_river.setObjectName(_fromUtf8("use_river"))
        self.use_drainage = QtGui.QCheckBox(self.connectivity_widget)
        self.use_drainage.setGeometry(QtCore.QRect(30, 270, 361, 17))
        self.use_drainage.setObjectName(_fromUtf8("use_drainage"))
        self.verticalLayout_3.addWidget(self.connectivity_widget)
        self.regiongeography_widget = QtGui.QWidget(self.scrollAreaWidgetContents)
        self.regiongeography_widget.setMinimumSize(QtCore.QSize(0, 210))
        self.regiongeography_widget.setObjectName(_fromUtf8("regiongeography_widget"))
        self.cbdoption_lbl = QtGui.QLabel(self.regiongeography_widget)
        self.cbdoption_lbl.setGeometry(QtCore.QRect(20, 60, 231, 16))
        self.cbdoption_lbl.setObjectName(_fromUtf8("cbdoption_lbl"))
        self.optionsmc_lbl_2 = QtGui.QLabel(self.regiongeography_widget)
        self.optionsmc_lbl_2.setGeometry(QtCore.QRect(10, 5, 231, 16))
        self.optionsmc_lbl_2.setObjectName(_fromUtf8("optionsmc_lbl_2"))
        self.cbd_combo = QtGui.QComboBox(self.regiongeography_widget)
        self.cbd_combo.setGeometry(QtCore.QRect(220, 85, 181, 16))
        self.cbd_combo.setObjectName(_fromUtf8("cbd_combo"))
        self.cbd_combo.addItem(_fromUtf8(""))
        self.cbd_combo.addItem(_fromUtf8(""))
        self.cbd_combo.addItem(_fromUtf8(""))
        self.cbd_combo.addItem(_fromUtf8(""))
        self.cbd_combo.addItem(_fromUtf8(""))
        self.cbd_combo.addItem(_fromUtf8(""))
        self.cbd_combo.addItem(_fromUtf8(""))
        self.cbd_combo.addItem(_fromUtf8(""))
        self.cbd_combo.addItem(_fromUtf8(""))
        self.cbd_combo.addItem(_fromUtf8(""))
        self.cbd_combo.addItem(_fromUtf8(""))
        self.cbd_combo.addItem(_fromUtf8(""))
        self.cbd_combo.addItem(_fromUtf8(""))
        self.cbd_combo.addItem(_fromUtf8(""))
        self.considergeo_check = QtGui.QCheckBox(self.regiongeography_widget)
        self.considergeo_check.setGeometry(QtCore.QRect(20, 30, 361, 17))
        self.considergeo_check.setWhatsThis(_fromUtf8(""))
        self.considergeo_check.setObjectName(_fromUtf8("considergeo_check"))
        self.cbdknown_radio = QtGui.QRadioButton(self.regiongeography_widget)
        self.cbdknown_radio.setGeometry(QtCore.QRect(20, 85, 211, 17))
        self.cbdknown_radio.setObjectName(_fromUtf8("cbdknown_radio"))
        self.cbdmanual_radio = QtGui.QRadioButton(self.regiongeography_widget)
        self.cbdmanual_radio.setGeometry(QtCore.QRect(20, 110, 211, 17))
        self.cbdmanual_radio.setObjectName(_fromUtf8("cbdmanual_radio"))
        self.cbdlong_box = QtGui.QLineEdit(self.regiongeography_widget)
        self.cbdlong_box.setGeometry(QtCore.QRect(220, 130, 113, 20))
        self.cbdlong_box.setObjectName(_fromUtf8("cbdlong_box"))
        self.cbdlat_box = QtGui.QLineEdit(self.regiongeography_widget)
        self.cbdlat_box.setGeometry(QtCore.QRect(220, 155, 113, 20))
        self.cbdlat_box.setObjectName(_fromUtf8("cbdlat_box"))
        self.cbdlong_lbl = QtGui.QLabel(self.regiongeography_widget)
        self.cbdlong_lbl.setGeometry(QtCore.QRect(160, 130, 61, 16))
        self.cbdlong_lbl.setObjectName(_fromUtf8("cbdlong_lbl"))
        self.cbdlat_lbl = QtGui.QLabel(self.regiongeography_widget)
        self.cbdlat_lbl.setGeometry(QtCore.QRect(160, 155, 61, 16))
        self.cbdlat_lbl.setObjectName(_fromUtf8("cbdlat_lbl"))
        self.cbdmark_check = QtGui.QCheckBox(self.regiongeography_widget)
        self.cbdmark_check.setGeometry(QtCore.QRect(20, 180, 181, 20))
        self.cbdmark_check.setObjectName(_fromUtf8("cbdmark_check"))
        self.verticalLayout_3.addWidget(self.regiongeography_widget)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout.addWidget(self.scrollArea)
        self.widget_2 = QtGui.QWidget(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setMinimumSize(QtCore.QSize(151, 0))
        self.widget_2.setMaximumSize(QtCore.QSize(151, 16777215))
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.img_blocks = QtGui.QLabel(self.widget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.img_blocks.sizePolicy().hasHeightForWidth())
        self.img_blocks.setSizePolicy(sizePolicy)
        self.img_blocks.setMinimumSize(QtCore.QSize(0, 90))
        self.img_blocks.setMaximumSize(QtCore.QSize(16777215, 90))
        self.img_blocks.setText(_fromUtf8(""))
        self.img_blocks.setPixmap(QtGui.QPixmap(_fromUtf8(":/images/images/D4W-BBcells.png")))
        self.img_blocks.setObjectName(_fromUtf8("img_blocks"))
        self.verticalLayout_2.addWidget(self.img_blocks)
        self.descr_blocks = QtGui.QTextBrowser(self.widget_2)
        self.descr_blocks.setObjectName(_fromUtf8("descr_blocks"))
        self.verticalLayout_2.addWidget(self.descr_blocks)
        self.horizontalLayout.addWidget(self.widget_2)
        self.verticalLayout.addWidget(self.widget)
        self.widget_4 = QtGui.QWidget(DelinBlocksDialog)
        self.widget_4.setMinimumSize(QtCore.QSize(0, 38))
        self.widget_4.setMaximumSize(QtCore.QSize(16777215, 38))
        self.widget_4.setObjectName(_fromUtf8("widget_4"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.remarks = QtGui.QLabel(self.widget_4)
        self.remarks.setObjectName(_fromUtf8("remarks"))
        self.horizontalLayout_2.addWidget(self.remarks)
        self.remarks2 = QtGui.QLabel(self.widget_4)
        self.remarks2.setObjectName(_fromUtf8("remarks2"))
        self.horizontalLayout_2.addWidget(self.remarks2)
        self.buttonBox = QtGui.QDialogButtonBox(self.widget_4)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.horizontalLayout_2.addWidget(self.buttonBox)
        self.helpButton = QtGui.QPushButton(self.widget_4)
        self.helpButton.setEnabled(True)
        self.helpButton.setObjectName(_fromUtf8("helpButton"))
        self.horizontalLayout_2.addWidget(self.helpButton)
        self.verticalLayout.addWidget(self.widget_4)

        self.retranslateUi(DelinBlocksDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), DelinBlocksDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), DelinBlocksDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(DelinBlocksDialog)
        DelinBlocksDialog.setTabOrder(self.scrollArea, self.buttonBox)
        DelinBlocksDialog.setTabOrder(self.buttonBox, self.helpButton)
        DelinBlocksDialog.setTabOrder(self.helpButton, self.descr_blocks)
        DelinBlocksDialog.setTabOrder(self.descr_blocks, self.blocksize_in)
        DelinBlocksDialog.setTabOrder(self.blocksize_in, self.blocksize_auto)
        DelinBlocksDialog.setTabOrder(self.blocksize_auto, self.popdata_totradio)
        DelinBlocksDialog.setTabOrder(self.popdata_totradio, self.popdata_densradio)
        DelinBlocksDialog.setTabOrder(self.popdata_densradio, self.soildata_classify)
        DelinBlocksDialog.setTabOrder(self.soildata_classify, self.soildata_infil)
        DelinBlocksDialog.setTabOrder(self.soildata_infil, self.soildata_unitscombo)
        DelinBlocksDialog.setTabOrder(self.soildata_unitscombo, self.elev_sealevel)
        DelinBlocksDialog.setTabOrder(self.elev_sealevel, self.elev_custom)
        DelinBlocksDialog.setTabOrder(self.elev_custom, self.elev_referencebox)
        DelinBlocksDialog.setTabOrder(self.elev_referencebox, self.planmap_check)
        DelinBlocksDialog.setTabOrder(self.planmap_check, self.localmap_check)
        DelinBlocksDialog.setTabOrder(self.localmap_check, self.employment_check)
        DelinBlocksDialog.setTabOrder(self.employment_check, self.jobdata_totradio)
        DelinBlocksDialog.setTabOrder(self.jobdata_totradio, self.jobdata_densradio)
        DelinBlocksDialog.setTabOrder(self.jobdata_densradio, self.rivers_check)
        DelinBlocksDialog.setTabOrder(self.rivers_check, self.lakes_check)
        DelinBlocksDialog.setTabOrder(self.lakes_check, self.groundwater_check)
        DelinBlocksDialog.setTabOrder(self.groundwater_check, self.groundwater_datumcombo)
        DelinBlocksDialog.setTabOrder(self.groundwater_datumcombo, self.roadnet_check)
        DelinBlocksDialog.setTabOrder(self.roadnet_check, self.drainage_check)
        DelinBlocksDialog.setTabOrder(self.drainage_check, self.soc_par1_check)
        DelinBlocksDialog.setTabOrder(self.soc_par1_check, self.soc_par1_box)
        DelinBlocksDialog.setTabOrder(self.soc_par1_box, self.socpar1binary_radio)
        DelinBlocksDialog.setTabOrder(self.socpar1binary_radio, self.socpar1prop_radio)
        DelinBlocksDialog.setTabOrder(self.socpar1prop_radio, self.soc_par2_check)
        DelinBlocksDialog.setTabOrder(self.soc_par2_check, self.soc_par2_box)
        DelinBlocksDialog.setTabOrder(self.soc_par2_box, self.socpar2binary_radio)
        DelinBlocksDialog.setTabOrder(self.socpar2binary_radio, self.socpar2prop_radio)
        DelinBlocksDialog.setTabOrder(self.socpar2prop_radio, self.spatialpatches_check)
        DelinBlocksDialog.setTabOrder(self.spatialpatches_check, self.spatialstats_check)
        DelinBlocksDialog.setTabOrder(self.spatialstats_check, self.radioMoore)
        DelinBlocksDialog.setTabOrder(self.radioMoore, self.radioVNeum)
        DelinBlocksDialog.setTabOrder(self.radioVNeum, self.neighb_vnfp_check)
        DelinBlocksDialog.setTabOrder(self.neighb_vnfp_check, self.neighb_vnpd_check)
        DelinBlocksDialog.setTabOrder(self.neighb_vnpd_check, self.flowpath_combo)
        DelinBlocksDialog.setTabOrder(self.flowpath_combo, self.demsmooth_check)
        DelinBlocksDialog.setTabOrder(self.demsmooth_check, self.demsmooth_spin)
        DelinBlocksDialog.setTabOrder(self.demsmooth_spin, self.considergeo_check)
        DelinBlocksDialog.setTabOrder(self.considergeo_check, self.cbdknown_radio)
        DelinBlocksDialog.setTabOrder(self.cbdknown_radio, self.cbd_combo)
        DelinBlocksDialog.setTabOrder(self.cbd_combo, self.cbdmanual_radio)
        DelinBlocksDialog.setTabOrder(self.cbdmanual_radio, self.cbdlong_box)
        DelinBlocksDialog.setTabOrder(self.cbdlong_box, self.cbdlat_box)
        DelinBlocksDialog.setTabOrder(self.cbdlat_box, self.cbdmark_check)

    def retranslateUi(self, DelinBlocksDialog):
        DelinBlocksDialog.setWindowTitle(_translate("DelinBlocksDialog", "Spatial Delineation Module", None))
        self.dbtitle_2.setText(_translate("DelinBlocksDialog", "Spatial Delineation of Building Blocks", None))
        self.dbsubtitle_2.setText(_translate("DelinBlocksDialog", "Processes Input Data and creates the grid of cells that represents a discretised version of the case study region.", None))
        self.blocksize_lbl.setWhatsThis(_translate("DelinBlocksDialog", "Width of the square cell in the city grid in metres", None))
        self.blocksize_lbl.setText(_translate("DelinBlocksDialog", "Block Size [m]", None))
        self.optionsgs_lbl.setWhatsThis(_translate("DelinBlocksDialog", "Width of the square cell in the city grid in metres", None))
        self.optionsgs_lbl.setText(_translate("DelinBlocksDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">General Simulation</span></p></body></html>", None))
        self.blocksize_in.setToolTip(_translate("DelinBlocksDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Width of the square cell in the city grid in metres</span></p></body></html>", None))
        self.blocksize_auto.setToolTip(_translate("DelinBlocksDialog", "An automatic algorithm that determines a suitable block size based on the map for computational efficiency.", None))
        self.blocksize_auto.setText(_translate("DelinBlocksDialog", "Auto-determine Block Size", None))
        self.soc_par1_check.setToolTip(_translate("DelinBlocksDialog", "Include a social parameter in the modelling? Define it here and set its purpose in the Technologies Planning Dialog Window.", None))
        self.soc_par1_check.setWhatsThis(_translate("DelinBlocksDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Check this box if you would like to experiment with social parameters. DAnCE4Water-BPM (when used as standalone) allows for a maximum of two socio-economic parameters to be specified. Input must be in the form of probabilities (between 0 and 1).</span></p></body></html>", None))
        self.soc_par1_check.setText(_translate("DelinBlocksDialog", "Include Social Parameter 1 - Name:", None))
        self.soc_par2_check.setToolTip(_translate("DelinBlocksDialog", "Include a second social parameter in the modelling? Define it here and set its purpose in the Technologies Planning Dialog Window.", None))
        self.soc_par2_check.setWhatsThis(_translate("DelinBlocksDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Check this box if you would like to experiment with social parameters. DAnCE4Water-BPM (when used as standalone) allows for a maximum of two socio-economic parameters to be specified. Input must be in the form of probabilities (between 0 and 1).</span></p></body></html>", None))
        self.soc_par2_check.setText(_translate("DelinBlocksDialog", "Include Social Parameter 2 - Name:", None))
        self.optionsadin_lbl.setWhatsThis(_translate("DelinBlocksDialog", "Width of the square cell in the city grid in metres", None))
        self.optionsadin_lbl.setText(_translate("DelinBlocksDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Processing of Input Data</span></p></body></html>", None))
        self.planmap_check.setToolTip(_translate("DelinBlocksDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">An additional sub-classification to support the land use map. See user guide for more details...</span></p></body></html>", None))
        self.planmap_check.setWhatsThis(_translate("DelinBlocksDialog", "A raster layer that is aligned the basic inputs zoning and population map. The planner\'s map contains typology-ratios for all land zones, specified according to the user\'s urban planning snapshot for the region in question. Refer to user guide for more information on how to create this map.", None))
        self.planmap_check.setText(_translate("DelinBlocksDialog", "Planner\'s Map", None))
        self.localmap_check.setToolTip(_translate("DelinBlocksDialog", "A map of locations of key urban facilities, which may have significant influence on the urban water cycle and water management options. See user guide for more details...", None))
        self.localmap_check.setWhatsThis(_translate("DelinBlocksDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">A raster layer that contains information on the location of the central business district and/or activity centres for the region.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">1-2 are urban centres</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">1 = CBD</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">2 = Activity Centre</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">3-7 are water-related point landmarks</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">3 = WWTP</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">4 = DWTP</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">5 = Outfall/Outlet</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"></p></body></html>", None))
        self.localmap_check.setText(_translate("DelinBlocksDialog", "Locality Map", None))
        self.addinputs_lbl.setText(_translate("DelinBlocksDialog", "Additional Planning and Geographic Information:", None))
        self.roadnet_check.setWhatsThis(_translate("DelinBlocksDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">A network maps of all road networks (polylines) in the region</span></p></body></html>", None))
        self.roadnet_check.setText(_translate("DelinBlocksDialog", "Road Networks", None))
        self.soc_params_lbl.setWhatsThis(_translate("DelinBlocksDialog", "Societal and demographic information can be used in the model to influence the planning of urban water infrastructure based on societal preferences. Up to two maps can be added to the model and data can take one of two forms:\n"
"- Binary: Yes/No format, which is treated as an absolute criteria\n"
"- Proportions: A value from 0 to 1, which is treated as a likelihood", None))
        self.soc_params_lbl.setText(_translate("DelinBlocksDialog", "Include Societal/Demographic Information", None))
        self.popdata_lbl.setWhatsThis(_translate("DelinBlocksDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Format of the population data input map.</span></p></body></html>", None))
        self.popdata_lbl.setText(_translate("DelinBlocksDialog", "Population Data Format:", None))
        self.spatialanalysis_lbl.setWhatsThis(_translate("DelinBlocksDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Additional analysis of the input data, which can be used for various other purposes. Two options are available:</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Patch delineation:</span> looks into the clustering of land uses within the urban environment</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Spatial Indices:</span> calculates a set of common spatial indices (e.g. richness, diversity, dominance) for further interpretation of land use distribution.</p></body></html>", None))
        self.spatialanalysis_lbl.setText(_translate("DelinBlocksDialog", "Spatial Analysis of Inputs", None))
        self.spatialpatches_check.setToolTip(_translate("DelinBlocksDialog", "Conduct a patch delineation? This will produce a patch map, which can be exported.", None))
        self.spatialpatches_check.setWhatsThis(_translate("DelinBlocksDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Runs a patch delineation algorithm across all building blocks to determine the clustering of land use mixes therein. This algorithm takes longer for larger blocks.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Information resulting from this is subsequently used in later parts of the model to determine urban form as well as technological opportunities. This allows more accurate assessment of technological opportunities, but is more computationally intensive.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">A map of patches will be created as an output if the option is checked among the list of desired outputs.</span></p></body></html>", None))
        self.spatialpatches_check.setText(_translate("DelinBlocksDialog", "Conduct Patch Delineation", None))
        self.spatialstats_check.setToolTip(_translate("DelinBlocksDialog", "Calculate a set of spatial indices for additional interpretation? Information is written into the blocks map.", None))
        self.spatialstats_check.setWhatsThis(_translate("DelinBlocksDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Calculates a basic set of spatial indices to describe the nature of land use mix in each building block. These include:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- Shannon Diversity Index</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- Shannon Dominance Index</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- Shannon Evenness Index</span></p></body></html>", None))
        self.spatialstats_check.setText(_translate("DelinBlocksDialog", "Calculate Set of Spatial Indices", None))
        self.socpar1binary_radio.setToolTip(_translate("DelinBlocksDialog", "Data is in the format of 0 or 1 where 0 denotes NO and 1 denotes YES. The model will treat this data as an absolute criteria.", None))
        self.socpar1binary_radio.setText(_translate("DelinBlocksDialog", "Binary Yes/No", None))
        self.socpar1prop_radio.setToolTip(_translate("DelinBlocksDialog", "Data values range between 0 and 1 representing the likelihood of societal preference for or against water infrastructure. The model will use this values as a probability of implementation.", None))
        self.socpar1prop_radio.setText(_translate("DelinBlocksDialog", "Proportions", None))
        self.socpar1format_lbl.setText(_translate("DelinBlocksDialog", "Select Format:", None))
        self.socpar2binary_radio.setToolTip(_translate("DelinBlocksDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Data is in the format of 0 or 1 where 0 denotes NO and 1 denotes YES. The model will treat this data as an absolute criteria.</span></p></body></html>", None))
        self.socpar2binary_radio.setText(_translate("DelinBlocksDialog", "Binary Yes/No", None))
        self.socpar2prop_radio.setToolTip(_translate("DelinBlocksDialog", "Data values range between 0 and 1 representing the likelihood of societal preference for or against water infrastructure. The model will use this values as a probability of implementation.", None))
        self.socpar2prop_radio.setText(_translate("DelinBlocksDialog", "Proportions", None))
        self.socpar2format_lbl.setText(_translate("DelinBlocksDialog", "Select Format:", None))
        self.rivers_check.setToolTip(_translate("DelinBlocksDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">A shapefile input of relevant river alignment (centreline). Recommended only for larger case studies (&gt;60sqkm) or where necessary.</span></p></body></html>", None))
        self.rivers_check.setWhatsThis(_translate("DelinBlocksDialog", "A raster layer that is aligned the basic inputs zoning and population map. The planner\'s map contains typology-ratios for all land zones, specified according to the user\'s urban planning snapshot for the region in question. Refer to user guide for more information on how to create this map.", None))
        self.rivers_check.setText(_translate("DelinBlocksDialog", "Rivers", None))
        self.lakes_check.setToolTip(_translate("DelinBlocksDialog", "A polygonal map of large water bodies in the region, which may have significance to the case study.", None))
        self.lakes_check.setWhatsThis(_translate("DelinBlocksDialog", "A raster layer that is aligned the basic inputs zoning and population map. The planner\'s map contains typology-ratios for all land zones, specified according to the user\'s urban planning snapshot for the region in question. Refer to user guide for more information on how to create this map.", None))
        self.lakes_check.setText(_translate("DelinBlocksDialog", "Lakes", None))
        self.employment_check.setToolTip(_translate("DelinBlocksDialog", "A map of employment in the region, which can be expressed as either total number of jobs or job density.", None))
        self.employment_check.setWhatsThis(_translate("DelinBlocksDialog", "A raster layer that is aligned the basic inputs zoning and population map. The planner\'s map contains typology-ratios for all land zones, specified according to the user\'s urban planning snapshot for the region in question. Refer to user guide for more information on how to create this map.", None))
        self.employment_check.setText(_translate("DelinBlocksDialog", "Employment Map", None))
        self.addinputs_lbl_2.setText(_translate("DelinBlocksDialog", "Information on Natural Features:", None))
        self.drainage_check.setWhatsThis(_translate("DelinBlocksDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">A network maps of all road networks (polylines) in the region</span></p></body></html>", None))
        self.drainage_check.setText(_translate("DelinBlocksDialog", "Stormwater Drainage", None))
        self.groundwater_check.setToolTip(_translate("DelinBlocksDialog", "A map of groundwater levels within the case study region. Levels need to be referenced relative to a datum.", None))
        self.groundwater_check.setWhatsThis(_translate("DelinBlocksDialog", "A raster layer that is aligned the basic inputs zoning and population map. The planner\'s map contains typology-ratios for all land zones, specified according to the user\'s urban planning snapshot for the region in question. Refer to user guide for more information on how to create this map.", None))
        self.groundwater_check.setText(_translate("DelinBlocksDialog", "Groundwater Table", None))
        self.soildata_lbl.setWhatsThis(_translate("DelinBlocksDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Format of the input soil map, can be one of two options:</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Classification</span> = categorical data where each raster cell represents a particular soil type. The different classes include 1 = x, 2 = x, 3 = x, 4 = x, 5 = x</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Infiltration Rate</span> = directly specified infiltration rates. If this option is checked, select the appropriate units from the dropdown menu below.</p></body></html>", None))
        self.soildata_lbl.setText(_translate("DelinBlocksDialog", "Soil Data Format:", None))
        self.popdata_densradio.setToolTip(_translate("DelinBlocksDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Input data given as a population density [people/ ha]</span></p></body></html>", None))
        self.popdata_densradio.setText(_translate("DelinBlocksDialog", "Population Density", None))
        self.popdata_totradio.setToolTip(_translate("DelinBlocksDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Input data given as a total population [no. of people]</span></p></body></html>", None))
        self.popdata_totradio.setWhatsThis(_translate("DelinBlocksDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"></p></body></html>", None))
        self.popdata_totradio.setText(_translate("DelinBlocksDialog", "Total Population", None))
        self.soildata_infil.setToolTip(_translate("DelinBlocksDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Infiltration rate of soil, select appropriate units as either [mm/hr] or [m/sec]</span></p></body></html>", None))
        self.soildata_infil.setWhatsThis(_translate("DelinBlocksDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"></p></body></html>", None))
        self.soildata_infil.setText(_translate("DelinBlocksDialog", "Infiltration Rates", None))
        self.soildata_classify.setToolTip(_translate("DelinBlocksDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Classification of soil as one of five categories:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">1 - sand</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">2 - sandy clay</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">3 - medium clay</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">4 - heavy clay</span></p></body></html>", None))
        self.soildata_classify.setWhatsThis(_translate("DelinBlocksDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"></p></body></html>", None))
        self.soildata_classify.setText(_translate("DelinBlocksDialog", "Classification", None))
        self.soildata_unitscombo.setItemText(0, _translate("DelinBlocksDialog", "mm/hr", None))
        self.soildata_unitscombo.setItemText(1, _translate("DelinBlocksDialog", "m/sec", None))
        self.soildataunits_lbl.setText(_translate("DelinBlocksDialog", "Units:", None))
        self.groundwater_datumlbl.setWhatsThis(_translate("DelinBlocksDialog", "Sea Level - all groundwater depths are relative to sea level datum\n"
"Natural surface - measured from the natural surface of the elevation data in that region.", None))
        self.groundwater_datumlbl.setText(_translate("DelinBlocksDialog", "Choose Datum:", None))
        self.addinputs_lbl_3.setWhatsThis(_translate("DelinBlocksDialog", "Coming Soon...", None))
        self.addinputs_lbl_3.setText(_translate("DelinBlocksDialog", "Network Infrastructure:", None))
        self.elevdata_lbl.setWhatsThis(_translate("DelinBlocksDialog", "Datum of the elevation data, i.e. the point from which the measurements are based. This can either be sea level or a custom datum set as metres above sea level.", None))
        self.elevdata_lbl.setText(_translate("DelinBlocksDialog", "Elevation Reference Point:", None))
        self.elev_custom.setText(_translate("DelinBlocksDialog", "Custom", None))
        self.elev_sealevel.setWhatsThis(_translate("DelinBlocksDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"></p></body></html>", None))
        self.elev_sealevel.setText(_translate("DelinBlocksDialog", "Sea Level", None))
        self.elev_referencelbl.setText(_translate("DelinBlocksDialog", "m above sea level", None))
        self.groundwater_datumcombo.setItemText(0, _translate("DelinBlocksDialog", "Sea Level", None))
        self.groundwater_datumcombo.setItemText(1, _translate("DelinBlocksDialog", "Natural Surface", None))
        self.jobdata_densradio.setToolTip(_translate("DelinBlocksDialog", "Density of employment [jobs/ha]", None))
        self.jobdata_densradio.setWhatsThis(_translate("DelinBlocksDialog", "Input data given as a population density [people/ ha]", None))
        self.jobdata_densradio.setText(_translate("DelinBlocksDialog", "Job Density [/ha]", None))
        self.jobdata_totradio.setToolTip(_translate("DelinBlocksDialog", "Total number of employed people in the raster cell.", None))
        self.jobdata_totradio.setWhatsThis(_translate("DelinBlocksDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Input data given as a total population [no. of people]</span></p></body></html>", None))
        self.jobdata_totradio.setText(_translate("DelinBlocksDialog", "Total Jobs", None))
        self.radioVNeum.setToolTip(_translate("DelinBlocksDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Von Neumann, four cardinal directions on either side of the central block.</span></p></body></html>", None))
        self.radioVNeum.setText(_translate("DelinBlocksDialog", "Von Neumann", None))
        self.neighb_lbl.setWhatsThis(_translate("DelinBlocksDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">How many blocks to consider when determining drainage fluxes (the greater the number, the greater the computational burden).</span></p></body></html>", None))
        self.neighb_lbl.setText(_translate("DelinBlocksDialog", "Select Neighbourhood (default: Moore):", None))
        self.radioMoore.setToolTip(_translate("DelinBlocksDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Moore, all eight neighbours around the central block.</span></p></body></html>", None))
        self.radioMoore.setText(_translate("DelinBlocksDialog", "Moore", None))
        self.optionsmc_lbl.setWhatsThis(_translate("DelinBlocksDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">How many blocks to consider when determining drainage fluxes (the greater the number, the greater the computational burden).</span></p></body></html>", None))
        self.optionsmc_lbl.setText(_translate("DelinBlocksDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Local Extents &amp; Map Connectivity</span></p></body></html>", None))
        self.flowpath_lbl.setWhatsThis(_translate("DelinBlocksDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Method of finding flow direction in the digital elevation model or in this case the grid of blocks. Refer to publications for further information.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">D-infinity</span><span style=\" font-size:8pt;\"> - Tarboton, 1997. A new method for the determination of flow directions and upslope areas in grid digital elevation models. Water Resources Research v33.2, 309-319</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">(This method is adapted here as more probabilistic. Whilst D-infinity usually finds two flow paths, UrbanBEATS will randomly choose one of the two dominant flow directions).</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">D8</span><span style=\" font-size:8pt;\"> - O\'Callaghan &amp; Mark, 1984. The Extraction of Drainage Networks from Digital Elevation Data. Computer Vision, Graphics and Image Processing v28, 323-344</span></p></body></html>", None))
        self.flowpath_lbl.setText(_translate("DelinBlocksDialog", "Flow Path Method:", None))
        self.flowpath_combo.setItemText(0, _translate("DelinBlocksDialog", "Adapted version of D-infinity (Tarboton, 1997)", None))
        self.flowpath_combo.setItemText(1, _translate("DelinBlocksDialog", "D8 (O\'Callaghan & Mark, 1984)", None))
        self.demsmooth_check.setToolTip(_translate("DelinBlocksDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Check if you want to avoid localised ponds forming in the region. If this is of particular interest because the DEM\'s accuracy has been assured and the purpose of the simulation is to assess these problem spots, then leave this box unchecked.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Correction proceeds as follows:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- If cell cannot transfer water downhill, but there is an adjacent cell with identical elevation within tolerance limit, it will transfer the water into this.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- If tolerance limit is not met, cell\'s water is routed directly to catchment outlet.</span></p></body></html>", None))
        self.demsmooth_check.setWhatsThis(_translate("DelinBlocksDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Applies a weighted average smoothing filter over the DEM layer. </span></p></body></html>", None))
        self.demsmooth_check.setText(_translate("DelinBlocksDialog", "DEM Smoothing (no. passes)", None))
        self.demsmooth_spin.setToolTip(_translate("DelinBlocksDialog", "Select the number of times the smoothing algorithm should be applied. A higher number will lead to a much smoother map, but can result in possible issues with finding flow paths.", None))
        self.neighb_vnfp_check.setToolTip(_translate("DelinBlocksDialog", "Delineation of flow directions across the map of blocks.", None))
        self.neighb_vnfp_check.setWhatsThis(_translate("DelinBlocksDialog", "Check if you want to avoid localised ponds forming in the region. If this is of particular interest because the DEM\'s accuracy has been assured and the purpose of the simulation is to assess these problem spots, then leave this box unchecked.\n"
"\n"
"Correction proceeds as follows:\n"
"- If cell cannot transfer water downhill, but there is an adjacent cell with identical elevation within tolerance limit, it will transfer the water into this.\n"
"- If tolerance limit is not met, cell\'s water is routed directly to catchment outlet.", None))
        self.neighb_vnfp_check.setText(_translate("DelinBlocksDialog", "Flow Path Delineation", None))
        self.neighb_vnpd_check.setToolTip(_translate("DelinBlocksDialog", "Averaging of certain attributes for a single block based on its neighbours.", None))
        self.neighb_vnpd_check.setWhatsThis(_translate("DelinBlocksDialog", "Check if you want to avoid localised ponds forming in the region. If this is of particular interest because the DEM\'s accuracy has been assured and the purpose of the simulation is to assess these problem spots, then leave this box unchecked.\n"
"\n"
"Correction proceeds as follows:\n"
"- If cell cannot transfer water downhill, but there is an adjacent cell with identical elevation within tolerance limit, it will transfer the water into this.\n"
"- If tolerance limit is not met, cell\'s water is routed directly to catchment outlet.", None))
        self.neighb_vnpd_check.setText(_translate("DelinBlocksDialog", "Spatial Averaging Operations", None))
        self.neighb_lbl2.setWhatsThis(_translate("DelinBlocksDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">If the Von Neumann neighbourhood is selected, choose which processes this neighbourhood should apply to. All processes not assigned the Von Neumann neighbourhood will default to using the Moore Neighbourhood.</span></p></body></html>", None))
        self.neighb_lbl2.setText(_translate("DelinBlocksDialog", "Apply Von Neumann Neighbourhood to: ", None))
        self.use_river.setToolTip(_translate("DelinBlocksDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Check if you want to avoid localised ponds forming in the region. If this is of particular interest because the DEM\'s accuracy has been assured and the purpose of the simulation is to assess these problem spots, then leave this box unchecked.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Correction proceeds as follows:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- If cell cannot transfer water downhill, but there is an adjacent cell with identical elevation within tolerance limit, it will transfer the water into this.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- If tolerance limit is not met, cell\'s water is routed directly to catchment outlet.</span></p></body></html>", None))
        self.use_river.setWhatsThis(_translate("DelinBlocksDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Applies a weighted average smoothing filter over the DEM layer. </span></p></body></html>", None))
        self.use_river.setText(_translate("DelinBlocksDialog", "Use natural features as guide points for flow paths?", None))
        self.use_drainage.setToolTip(_translate("DelinBlocksDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Check if you want to avoid localised ponds forming in the region. If this is of particular interest because the DEM\'s accuracy has been assured and the purpose of the simulation is to assess these problem spots, then leave this box unchecked.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Correction proceeds as follows:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- If cell cannot transfer water downhill, but there is an adjacent cell with identical elevation within tolerance limit, it will transfer the water into this.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- If tolerance limit is not met, cell\'s water is routed directly to catchment outlet.</span></p></body></html>", None))
        self.use_drainage.setWhatsThis(_translate("DelinBlocksDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Applies a weighted average smoothing filter over the DEM layer. </span></p></body></html>", None))
        self.use_drainage.setText(_translate("DelinBlocksDialog", "Use built drainage infrastructure as guide points for flow paths?", None))
        self.cbdoption_lbl.setWhatsThis(_translate("DelinBlocksDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"></p></body></html>", None))
        self.cbdoption_lbl.setText(_translate("DelinBlocksDialog", "Select an option for determining CBD Location:", None))
        self.optionsmc_lbl_2.setWhatsThis(_translate("DelinBlocksDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">How many blocks to consider when determining drainage fluxes (the greater the number, the greater the computational burden).</span></p></body></html>", None))
        self.optionsmc_lbl_2.setText(_translate("DelinBlocksDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Regional Geography</span></p></body></html>", None))
        self.cbd_combo.setItemText(0, _translate("DelinBlocksDialog", "Adelaide, Australia", None))
        self.cbd_combo.setItemText(1, _translate("DelinBlocksDialog", "Brisbane, Australia", None))
        self.cbd_combo.setItemText(2, _translate("DelinBlocksDialog", "Cairns, Australia", None))
        self.cbd_combo.setItemText(3, _translate("DelinBlocksDialog", "Canberra, Australia", None))
        self.cbd_combo.setItemText(4, _translate("DelinBlocksDialog", "Copenhagen, Denmark", None))
        self.cbd_combo.setItemText(5, _translate("DelinBlocksDialog", "Innsbruck, Austria", None))
        self.cbd_combo.setItemText(6, _translate("DelinBlocksDialog", "Kuala Lumpur, Malaysia", None))
        self.cbd_combo.setItemText(7, _translate("DelinBlocksDialog", "London, UK", None))
        self.cbd_combo.setItemText(8, _translate("DelinBlocksDialog", "Melbourne, Australia", None))
        self.cbd_combo.setItemText(9, _translate("DelinBlocksDialog", "Munich, Germany", None))
        self.cbd_combo.setItemText(10, _translate("DelinBlocksDialog", "Perth, Australia", None))
        self.cbd_combo.setItemText(11, _translate("DelinBlocksDialog", "Singapore, Singapore", None))
        self.cbd_combo.setItemText(12, _translate("DelinBlocksDialog", "Sydney, Australia", None))
        self.cbd_combo.setItemText(13, _translate("DelinBlocksDialog", "Vienna, Austria", None))
        self.considergeo_check.setToolTip(_translate("DelinBlocksDialog", "Checking this box will have the model to calculate distance from CBD (based on a selected city using its central point of reference).", None))
        self.considergeo_check.setText(_translate("DelinBlocksDialog", "Consider location of nearest Central Business District in Simulation", None))
        self.cbdknown_radio.setToolTip(_translate("DelinBlocksDialog", "Choose the nearest city if your case study is within its metropolitan region.", None))
        self.cbdknown_radio.setText(_translate("DelinBlocksDialog", "Select from a list of known locations", None))
        self.cbdmanual_radio.setToolTip(_translate("DelinBlocksDialog", "Enter the coordinates of your city\'s CBD manually. Use decimal degrees.", None))
        self.cbdmanual_radio.setText(_translate("DelinBlocksDialog", "Manually enter coordinates of CBD", None))
        self.cbdlong_box.setToolTip(_translate("DelinBlocksDialog", "Units of decimal degrees", None))
        self.cbdlat_box.setToolTip(_translate("DelinBlocksDialog", "Units of decimal degrees.", None))
        self.cbdlong_lbl.setWhatsThis(_translate("DelinBlocksDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">How many blocks to consider when determining drainage fluxes (the greater the number, the greater the computational burden).</span></p></body></html>", None))
        self.cbdlong_lbl.setText(_translate("DelinBlocksDialog", "Longitude", None))
        self.cbdlat_lbl.setWhatsThis(_translate("DelinBlocksDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">How many blocks to consider when determining drainage fluxes (the greater the number, the greater the computational burden).</span></p></body></html>", None))
        self.cbdlat_lbl.setText(_translate("DelinBlocksDialog", "Latitude", None))
        self.cbdmark_check.setToolTip(_translate("DelinBlocksDialog", "Checking this box will produce a CBD point on the \"block centres\" output map.", None))
        self.cbdmark_check.setWhatsThis(_translate("DelinBlocksDialog", "Check if you want to avoid localised ponds forming in the region. If this is of particular interest because the DEM\'s accuracy has been assured and the purpose of the simulation is to assess these problem spots, then leave this box unchecked.\n"
"\n"
"Correction proceeds as follows:\n"
"- If cell cannot transfer water downhill, but there is an adjacent cell with identical elevation within tolerance limit, it will transfer the water into this.\n"
"- If tolerance limit is not met, cell\'s water is routed directly to catchment outlet.", None))
        self.cbdmark_check.setText(_translate("DelinBlocksDialog", "Mark this location on output map", None))
        self.descr_blocks.setHtml(_translate("DelinBlocksDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Set basic simulation parameters for creating the block map of input region. Define additional inputs and specify neighbourhood and DEM analysis rules.</span></p></body></html>", None))
        self.remarks.setText(_translate("DelinBlocksDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-style:italic;\">UrbanBEATS Version 1.0</span></p></body></html>", None))
        self.remarks2.setText(_translate("DelinBlocksDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-style:italic;\">- (C) 2014 Peter M. Bach</span></p></body></html>", None))
        self.helpButton.setWhatsThis(_translate("DelinBlocksDialog", "You do not need help right now! :)", None))
        self.helpButton.setText(_translate("DelinBlocksDialog", "Help", None))

import guitoolbaricons_rc
