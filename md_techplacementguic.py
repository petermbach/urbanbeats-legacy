# -*- coding: utf-8 -*-
"""
@file
@author  Peter M Bach <peterbach@gmail.com>
@version 0.5
@section LICENSE

This file is part of VIBe2
Copyright (C) 2011, 2012, 2013  Peter M Bach

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
"""
import os

from PyQt4 import QtCore, QtGui
#from pyvibe import *
#from pydynamind import *
from md_techplacementgui import Ui_TechPlace_Dialog

class TechplacementGUILaunch(QtGui.QDialog):
    def __init__(self, activesim, tabindex, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_TechPlace_Dialog()
        self.ui.setupUi(self)
        self.module = activesim.getModuleTechplacement(tabindex)
        #Assign Default Values & Connect Signal/Slots

        #######################################
        #General Strategy Tab
        #######################################

        #-------- DESIGN RATIONALE --------------------------------------------#
        self.ui.ration_runoff_check.setChecked(bool(int(self.module.getParameter("ration_runoff"))))
        self.ui.ration_pollute_check.setChecked(bool(int(self.module.getParameter("ration_pollute"))))
        self.ui.ration_harvest_check.setChecked(bool(int(self.module.getParameter("ration_harvest"))))
        self.ui.runoff_pri_spin.setValue(int(self.module.getParameter("runoff_pri")))
        self.ui.pollute_pri_spin.setValue(int(self.module.getParameter("pollute_pri")))
        self.ui.harvest_pri_spin.setValue(int(self.module.getParameter("harvest_pri")))

        #-------- MANAGEMENT TARGETS ------------------------------------------#
        self.ui.targets_runoff_spin.setValue(float(self.module.getParameter("targets_runoff")))
        self.ui.targets_TSS_spin.setValue(float(self.module.getParameter("targets_TSS")))
        self.ui.targets_TN_spin.setValue(float(self.module.getParameter("targets_TN")))
        self.ui.targets_TP_spin.setValue(float(self.module.getParameter("targets_TP")))
        self.ui.targets_reliability_spin.setValue(float(self.module.getParameter("targets_reliability")))

        #-------- SERVICE LEVELS ----------------------------------------------#
        self.ui.service_swmQty.setValue(float(self.module.getParameter("service_swmQty")))
        self.ui.service_swmWQ.setValue(float(self.module.getParameter("service_swmWQ")))
        self.ui.service_rec.setValue(float(self.module.getParameter("service_rec")))

        self.ui.service_res.setChecked(bool(int(self.module.getParameter("service_res"))))
        self.ui.service_hdr.setChecked(bool(int(self.module.getParameter("service_hdr"))))
        self.ui.service_com.setChecked(bool(int(self.module.getParameter("service_com"))))
        self.ui.service_li.setChecked(bool(int(self.module.getParameter("service_li"))))
        self.ui.service_hi.setChecked(bool(int(self.module.getParameter("service_hi"))))

        self.ui.service_redundancy.setValue(float(self.module.getParameter("service_redundancy")))

        #-------- STRATEGY SETUP ----------------------------------------------#
        if self.module.getParameter("strategy_lot_check") == 1:
            self.ui.strategy_lot_check.setChecked(1)
            self.ui.strategy_lot_rigour.setEnabled(1)
            self.ui.strategy_lot_rigour_box.setEnabled(1)
        else:
            self.ui.strategy_lot_check.setChecked(0)
            self.ui.strategy_lot_rigour.setEnabled(0)
            self.ui.strategy_lot_rigour_box.setEnabled(0)

        QtCore.QObject.connect(self.ui.strategy_lot_check, QtCore.SIGNAL("clicked()"), self.enableLotRigour)

        self.ui.strategy_lot_rigour.setValue(int(self.module.getParameter("lot_rigour")))
        self.ui.strategy_lot_rigour_box.setText(str(self.module.getParameter("lot_rigour")))
        QtCore.QObject.connect(self.ui.strategy_lot_rigour, QtCore.SIGNAL("valueChanged(int)"), self.adjustRigourLot)

        if self.module.getParameter("strategy_street_check") == 1:
            self.ui.strategy_street_check.setChecked(1)
            self.ui.strategy_street_rigour.setEnabled(1)
            self.ui.strategy_street_rigour_box.setEnabled(1)
        else:
            self.ui.strategy_street_check.setChecked(0)
            self.ui.strategy_street_rigour.setEnabled(0)
            self.ui.strategy_street_rigour_box.setEnabled(0)

        QtCore.QObject.connect(self.ui.strategy_street_check, QtCore.SIGNAL("clicked()"), self.enableStreetRigour)

        self.ui.strategy_street_rigour.setValue(int(self.module.getParameter("street_rigour")))
        self.ui.strategy_street_rigour_box.setText(str(self.module.getParameter("street_rigour")))
        QtCore.QObject.connect(self.ui.strategy_street_rigour, QtCore.SIGNAL("valueChanged(int)"), self.adjustRigourStreet)

        if self.module.getParameter("strategy_neigh_check") == 1:
            self.ui.strategy_neigh_check.setChecked(1)
            self.ui.strategy_neigh_rigour.setEnabled(1)
            self.ui.strategy_neigh_rigour_box.setEnabled(1)
        else:
            self.ui.strategy_neigh_check.setChecked(0)
            self.ui.strategy_neigh_rigour.setEnabled(0)
            self.ui.strategy_neigh_rigour_box.setEnabled(0)

        QtCore.QObject.connect(self.ui.strategy_neigh_check, QtCore.SIGNAL("clicked()"), self.enableNeighRigour)

        self.ui.strategy_neigh_rigour.setValue(int(self.module.getParameter("neigh_rigour")))
        self.ui.strategy_neigh_rigour_box.setText(str(self.module.getParameter("neigh_rigour")))
        QtCore.QObject.connect(self.ui.strategy_neigh_rigour, QtCore.SIGNAL("valueChanged(int)"), self.adjustRigourNeigh)

        if self.module.getParameter("strategy_subbas_check") == 1:
            self.ui.strategy_subbas_check.setChecked(1)
            self.ui.strategy_subbas_rigour.setEnabled(1)
            self.ui.strategy_subbas_rigour_box.setEnabled(1)
        else:
            self.ui.strategy_subbas_check.setChecked(0)
            self.ui.strategy_subbas_rigour.setEnabled(0)
            self.ui.strategy_subbas_rigour_box.setEnabled(0)

        QtCore.QObject.connect(self.ui.strategy_subbas_check, QtCore.SIGNAL("clicked()"), self.enableSubbasRigour)

        self.ui.strategy_subbas_rigour.setValue(int(self.module.getParameter("subbas_rigour")))
        self.ui.strategy_subbas_rigour_box.setText(str(self.module.getParameter("subbas_rigour")))
        QtCore.QObject.connect(self.ui.strategy_subbas_rigour, QtCore.SIGNAL("valueChanged(int)"), self.adjustRigourSubbas)

        self.ui.strategy_scalepref_slider.setValue(int(self.module.getParameter("scalepref")))

        #######################################
        #Retrofit Tab
        #######################################
        if self.module.getParameter("retrofit_scenario") == "N":
            self.ui.area_retrofit_combo.setCurrentIndex(0)
            self.ui.lot_renew_check.setEnabled(0)
            self.ui.lot_decom_check.setEnabled(0)
            self.ui.street_decom_check.setEnabled(0)
            self.ui.street_renew_check.setEnabled(0)
            self.ui.neigh_renew_check.setEnabled(0)
            self.ui.neigh_decom_check.setEnabled(0)
            self.ui.prec_renew_check.setEnabled(0)
            self.ui.prec_decom_check.setEnabled(0)
            self.ui.decom_slider.setEnabled(0)
            self.ui.decom_box.setEnabled(0)
            self.ui.renew_slider.setEnabled(0)
            self.ui.renew_box.setEnabled(0)
            self.ui.radioKeep.setEnabled(0)
            self.ui.radioDecom.setEnabled(0)
        elif self.module.getParameter("retrofit_scenario") == "R":
            self.ui.area_retrofit_combo.setCurrentIndex(1)
            self.ui.lot_renew_check.setEnabled(1)
            self.ui.lot_decom_check.setEnabled(1)
            self.ui.street_decom_check.setEnabled(1)
            self.ui.street_renew_check.setEnabled(1)
            self.ui.neigh_renew_check.setEnabled(1)
            self.ui.neigh_decom_check.setEnabled(1)
            self.ui.prec_renew_check.setEnabled(1)
            self.ui.prec_decom_check.setEnabled(1)
            self.ui.decom_slider.setEnabled(1)
            self.ui.decom_box.setEnabled(1)
            self.ui.renew_slider.setEnabled(1)
            self.ui.renew_box.setEnabled(1)
            self.ui.radioKeep.setEnabled(1)
            self.ui.radioDecom.setEnabled(1)
        elif self.module.getParameter("retrofit_scenario") == "F":
            self.ui.area_retrofit_combo.setCurrentIndex(2)
            self.ui.lot_renew_check.setEnabled(1)
            self.ui.lot_decom_check.setEnabled(1)
            self.ui.street_decom_check.setEnabled(1)
            self.ui.street_renew_check.setEnabled(1)
            self.ui.neigh_renew_check.setEnabled(1)
            self.ui.neigh_decom_check.setEnabled(1)
            self.ui.prec_renew_check.setEnabled(1)
            self.ui.prec_decom_check.setEnabled(1)
            self.ui.decom_slider.setEnabled(1)
            self.ui.decom_box.setEnabled(1)
            self.ui.renew_slider.setEnabled(1)
            self.ui.renew_box.setEnabled(1)
            self.ui.radioKeep.setEnabled(1)
            self.ui.radioDecom.setEnabled(1)

        if self.module.getParameter("renewal_cycle_def") == 1:
            self.ui.retrofit_renewal_check.setChecked(1)
        else:
            self.ui.retrofit_renewal_check.setChecked(0)

        self.ui.renewal_lot_years.setValue(float(self.module.getParameter("renewal_lot_years")))
        self.ui.renewal_lot_spin.setValue(float(self.module.getParameter("renewal_lot_perc")))
        self.ui.renewal_street_years.setValue(float(self.module.getParameter("renewal_street_years")))
        self.ui.renewal_neigh_years.setValue(float(self.module.getParameter("renewal_neigh_years")))

        if self.module.getParameter("force_street") == 1:
            self.ui.retrofit_forced_street_check.setChecked(1)
        else:
            self.ui.retrofit_forced_street_check.setChecked(0)

        if self.module.getParameter("force_neigh") == 1:
            self.ui.retrofit_forced_neigh_check.setChecked(1)
        else:
            self.ui.retrofit_forced_neigh_check.setChecked(0)

        if self.module.getParameter("force_prec") == 1:
            self.ui.retrofit_forced_prec_check.setChecked(1)
        else:
            self.ui.retrofit_forced_prec_check.setChecked(0)


        if self.module.getParameter("lot_renew") == 1:
            self.ui.lot_renew_check.setChecked(1)
        else:
            self.ui.lot_renew_check.setChecked(0)

        if self.module.getParameter("lot_decom") == 1:
            self.ui.lot_decom_check.setChecked(1)
        else:
            self.ui.lot_decom_check.setChecked(0)

        if self.module.getParameter("street_renew") == 1:
            self.ui.street_renew_check.setChecked(1)
        else:
            self.ui.street_renew_check.setChecked(0)

        if self.module.getParameter("street_decom") == 1:
            self.ui.street_decom_check.setChecked(1)
        else:
            self.ui.street_decom_check.setChecked(0)

        if self.module.getParameter("neigh_renew") == 1:
            self.ui.neigh_renew_check.setChecked(1)
        else:
            self.ui.neigh_renew_check.setChecked(0)

        if self.module.getParameter("neigh_decom") == 1:
            self.ui.neigh_decom_check.setChecked(1)
        else:
            self.ui.neigh_decom_check.setChecked(0)

        if self.module.getParameter("prec_renew") == 1:
            self.ui.prec_renew_check.setChecked(1)
        else:
            self.ui.prec_renew_check.setChecked(0)

        if self.module.getParameter("prec_decom") == 1:
            self.ui.prec_decom_check.setChecked(1)
        else:
            self.ui.prec_decom_check.setChecked(0)

        self.ui.decom_slider.setValue(int(self.module.getParameter("decom_thresh")))
        self.ui.decom_box.setText(str(self.module.getParameter("decom_thresh"))+"%")
        self.ui.renew_slider.setValue(int(self.module.getParameter("renewal_thresh")))
        self.ui.renew_box.setText(str(self.module.getParameter("renewal_thresh"))+"%")
        QtCore.QObject.connect(self.ui.decom_slider, QtCore.SIGNAL("valueChanged(int)"), self.decom_update)
        QtCore.QObject.connect(self.ui.renew_slider, QtCore.SIGNAL("valueChanged(int)"), self.renew_update)

        if self.module.getParameter("renewal_alternative") == "K":
            self.ui.radioKeep.setChecked(True)
        if self.module.getParameter("renewal_alternative") == "D":
            self.ui.radioDecom.setChecked(True)

        QtCore.QObject.connect(self.ui.area_retrofit_combo, QtCore.SIGNAL("currentIndexChanged(int)"), self.update_retrofitoptions)

        #######################################
        #Water Use and Recycling Tab
        #######################################
        #--> Water Demands
        self.ui.freq_kitchen_box.setText(str(self.module.getParameter("freq_kitchen")))
        self.ui.freq_shower_box.setText(str(self.module.getParameter("freq_shower")))
        self.ui.freq_toilet_box.setText(str(self.module.getParameter("freq_toilet")))
        self.ui.freq_laundry_box.setText(str(self.module.getParameter("freq_laundry")))
        self.ui.dur_kitchen_box.setText(str(self.module.getParameter("dur_kitchen")))
        self.ui.dur_shower_box.setText(str(self.module.getParameter("dur_shower")))
        self.ui.demandvary_kitchen_box.setValue(int(self.module.getParameter("demandvary_kitchen")))
        self.ui.demandvary_shower_box.setValue(int(self.module.getParameter("demandvary_shower")))
        self.ui.demandvary_toilet_box.setValue(int(self.module.getParameter("demandvary_toilet")))
        self.ui.demandvary_laundry_box.setValue(int(self.module.getParameter("demandvary_laundry")))
        self.ui.priv_irr_vol_box.setText(str(self.module.getParameter("priv_irr_vol")))

        #COMBO BOX
        if self.module.getParameter("ffp_kitchen") == "PO":
            self.ui.ffp_kitchen_combo.setCurrentIndex(0)
        elif self.module.getParameter("ffp_kitchen") == "NP":
            self.ui.ffp_kitchen_combo.setCurrentIndex(1)
        elif self.module.getParameter("ffp_kitchen") == "RW":
            self.ui.ffp_kitchen_combo.setCurrentIndex(2)
        elif self.module.getParameter("ffp_kitchen") == "SW":
            self.ui.ffp_kitchen_combo.setCurrentIndex(3)
        elif self.module.getParameter("ffp_kitchen") == "GW":
            self.ui.ffp_kitchen_combo.setCurrentIndex(4)

        if self.module.getParameter("ffp_shower") == "PO":
            self.ui.ffp_shower_combo.setCurrentIndex(0)
        elif self.module.getParameter("ffp_shower") == "NP":
            self.ui.ffp_shower_combo.setCurrentIndex(1)
        elif self.module.getParameter("ffp_shower") == "RW":
            self.ui.ffp_shower_combo.setCurrentIndex(2)
        elif self.module.getParameter("ffp_shower") == "SW":
            self.ui.ffp_shower_combo.setCurrentIndex(3)
        elif self.module.getParameter("ffp_shower") == "GW":
            self.ui.ffp_shower_combo.setCurrentIndex(4)

        if self.module.getParameter("ffp_toilet") == "PO":
            self.ui.ffp_toilet_combo.setCurrentIndex(0)
        elif self.module.getParameter("ffp_toilet") == "NP":
            self.ui.ffp_toilet_combo.setCurrentIndex(1)
        elif self.module.getParameter("ffp_toilet") == "RW":
            self.ui.ffp_toilet_combo.setCurrentIndex(2)
        elif self.module.getParameter("ffp_toilet") == "SW":
            self.ui.ffp_toilet_combo.setCurrentIndex(3)
        elif self.module.getParameter("ffp_toilet") == "GW":
            self.ui.ffp_toilet_combo.setCurrentIndex(4)

        if self.module.getParameter("ffp_laundry") == "PO":
            self.ui.ffp_laundry_combo.setCurrentIndex(0)
        elif self.module.getParameter("ffp_laundry") == "NP":
            self.ui.ffp_laundry_combo.setCurrentIndex(1)
        elif self.module.getParameter("ffp_laundry") == "RW":
            self.ui.ffp_laundry_combo.setCurrentIndex(2)
        elif self.module.getParameter("ffp_laundry") == "SW":
            self.ui.ffp_laundry_combo.setCurrentIndex(3)
        elif self.module.getParameter("ffp_laundry") == "GW":
            self.ui.ffp_laundry_combo.setCurrentIndex(4)

        if self.module.getParameter("ffp_garden") == "PO":
            self.ui.ffp_garden_combo.setCurrentIndex(0)
        elif self.module.getParameter("ffp_garden") == "NP":
            self.ui.ffp_garden_combo.setCurrentIndex(1)
        elif self.module.getParameter("ffp_garden") == "RW":
            self.ui.ffp_garden_combo.setCurrentIndex(2)
        elif self.module.getParameter("ffp_garden") == "SW":
            self.ui.ffp_garden_combo.setCurrentIndex(3)
        elif self.module.getParameter("ffp_garden") == "GW":
            self.ui.ffp_garden_combo.setCurrentIndex(4)

        self.ui.comdemand_box.setText(str(self.module.getParameter("com_demand")))
        self.ui.lidemand_box.setText(str(self.module.getParameter("li_demand")))
        self.ui.hidemand_box.setText(str(self.module.getParameter("hi_demand")))
        self.ui.comdemand_spin.setValue(int(self.module.getParameter("com_demandvary")))
        self.ui.lidemand_spin.setValue(int(self.module.getParameter("li_demandvary")))
        self.ui.hidemand_spin.setValue(int(self.module.getParameter("hi_demandvary")))

        demandunits = ['sqm', 'cap']
        self.ui.comdemand_units.setCurrentIndex(demandunits.index(self.module.getParameter("com_demandunits")))
        self.ui.lidemand_units.setCurrentIndex(demandunits.index(self.module.getParameter("li_demandunits")))
        self.ui.hidemand_units.setCurrentIndex(demandunits.index(self.module.getParameter("hi_demandunits")))

        self.ui.public_irr_volume.setText(str(self.module.getParameter("public_irr_vol")))
        self.ui.public_irr_nonres.setChecked(bool(int(self.module.getParameter("irrigate_nonres"))))
        self.ui.public_irr_pg.setChecked(bool(int(self.module.getParameter("irrigate_parks"))))
        self.ui.public_irr_ref.setChecked(bool(int(self.module.getParameter("irrigate_refs"))))

        #COMBO BOX
        if self.module.getParameter("public_irr_wq") == "PO":
            self.ui.public_irr_wq.setCurrentIndex(0)
        elif self.module.getParameter("public_irr_wq") == "NP":
            self.ui.public_irr_wq.setCurrentIndex(1)
        elif self.module.getParameter("public_irr_wq") == "RW":
            self.ui.public_irr_wq.setCurrentIndex(2)
        elif self.module.getParameter("public_irr_wq") == "SW":
            self.ui.public_irr_wq.setCurrentIndex(3)
        elif self.module.getParameter("public_irr_wq") == "GW":
            self.ui.public_irr_wq.setCurrentIndex(4)

        #--> Water Efficiency
        ### NOTE: Not linking Rating System Combo box, AS6400 the only available system currently

        if self.module.getParameter("WEF_loc_house") == 1:
            self.ui.WEF_loc_house_check.setChecked(1)
        else:
            self.ui.WEF_loc_house_check.setChecked(0)

        if self.module.getParameter("WEF_loc_apart") == 1:
            self.ui.WEF_loc_apart_check.setChecked(1)
        else:
            self.ui.WEF_loc_apart_check.setChecked(0)

        if self.module.getParameter("WEF_loc_nonres") == 1:
            self.ui.WEF_loc_nonres_check.setChecked(1)
        else:
            self.ui.WEF_loc_nonres_check.setChecked(0)

        if self.module.getParameter("WEF_method") == "C":
            self.ui.WEF_constant_radio.setChecked(1)
            self.ui.WEF_constant_combo.setEnabled(1)
            self.ui.WEF_distribution_combo.setEnabled(0)
            self.ui.WEF_distribution_select.setEnabled(0)
            self.ui.WEF_distribution_check.setEnabled(0)
        elif self.module.getParameter("WEF_method") == "D":
            self.ui.WEF_distribution_radio.setChecked(1)
            self.ui.WEF_constant_combo.setEnabled(0)
            self.ui.WEF_distribution_combo.setEnabled(1)
            self.ui.WEF_distribution_select.setEnabled(1)
            self.ui.WEF_distribution_check.setEnabled(1)

        QtCore.QObject.connect(self.ui.WEF_constant_radio, QtCore.SIGNAL("clicked()"), self.update_WEF_determine)
        QtCore.QObject.connect(self.ui.WEF_distribution_radio, QtCore.SIGNAL("clicked()"), self.update_WEF_determine)

        self.ui.WEF_constant_combo.setCurrentIndex(int(self.module.getParameter("WEF_c_rating"))-1)
        self.ui.WEF_distribution_combo.setCurrentIndex(int(self.module.getParameter("WEF_d_rating"))-1)

        self.WEFdist = ["LH", "LL", "NM", "UF"]
        self.ui.WEF_distribution_select.setCurrentIndex(self.WEFdist.index(self.module.getParameter("WEF_distribution")))

        self.ui.WEF_distribution_check.setChecked(bool(int(self.module.getParameter("WEF_includezero"))))

        #--> Harvesting Strategy + Additional Info
        self.ui.rec_demrange_min.setValue(int(self.module.getParameter("rec_demrange_min")))
        self.ui.rec_demrange_max.setValue(int(self.module.getParameter("rec_demrange_max")))
        self.ui.rec_ww_kitchen.setChecked(bool(int(self.module.getParameter("ww_kitchen"))))
        self.ui.rec_ww_shower.setChecked(bool(int(self.module.getParameter("ww_shower"))))
        self.ui.rec_ww_toilet.setChecked(bool(int(self.module.getParameter("ww_toilet"))))
        self.ui.rec_ww_laundry.setChecked(bool(int(self.module.getParameter("ww_laundry"))))

        if self.module.getParameter("hs_strategy") == "ud":
            self.ui.radio_hsdown.setChecked(1)
        elif self.module.getParameter("hs_strategy") == "uu":
            self.ui.radio_hsup.setChecked(1)
        elif self.module.getParameter("hs_strategy") == "ua":
            self.ui.radio_hsall.setChecked(1)

        self.sbmethod = ["Eqn", "Sim"]
        self.ui.rec_assessment_combo.setCurrentIndex(self.sbmethod.index(self.module.getParameter("sb_method")))

        self.ui.rec_rainfall_spin.setValue(int(self.module.getParameter("rain_length")))

        if self.module.getParameter("WEFstatus") == 1:
            self.ui.WEF_consider.setChecked(1)
            self.ui.WEF_rating_system_combo.setEnabled(1)
            self.ui.WEF_loc_house_check.setEnabled(1)
            self.ui.WEF_loc_apart_check.setEnabled(1)
            self.ui.WEF_constant_radio.setEnabled(1)
            self.ui.WEF_distribution_radio.setEnabled(1)
            if self.ui.WEF_constant_radio.isChecked() == 1:
                self.ui.WEF_constant_combo.setEnabled(1)
            else:
                self.ui.WEF_constant_combo.setEnabled(0)
            if self.ui.WEF_distribution_radio.isChecked() == 1:
                self.ui.WEF_distribution_combo.setEnabled(1)
                self.ui.WEF_distribution_select.setEnabled(1)
                self.ui.WEF_distribution_check.setEnabled(1)
            else:
                self.ui.WEF_distribution_combo.setEnabled(0)
                self.ui.WEF_distribution_select.setEnabled(0)
                self.ui.WEF_distribution_check.setEnabled(0)
        else:
            self.ui.WEF_consider.setChecked(0)
            self.ui.WEF_rating_system_combo.setEnabled(0)
            self.ui.WEF_loc_house_check.setEnabled(0)
            self.ui.WEF_loc_apart_check.setEnabled(0)
            self.ui.WEF_constant_radio.setEnabled(0)
            self.ui.WEF_distribution_radio.setEnabled(0)
            self.ui.WEF_constant_combo.setEnabled(0)
            self.ui.WEF_distribution_combo.setEnabled(0)
            self.ui.WEF_distribution_select.setEnabled(0)
            self.ui.WEF_distribution_check.setEnabled(0)

        QtCore.QObject.connect(self.ui.WEF_consider, QtCore.SIGNAL("clicked()"), self.WEF_consider_update)

        #######################################
        #Choose & Customize Technologies Tab
        #######################################

        #--------- Advanced Stormwater Harvesting Plant -----------------------#
        if self.module.getParameter("ASHPstatus") == 1:
            self.ui.ASHPstatus_box.setChecked(1)
        else:
            self.ui.ASHPstatus_box.setChecked(0)

        #--------- Aquaculture/LivingSystems ----------------------------------#
        if self.module.getParameter("AQstatus") == 1:
            self.ui.AQstatus_box.setChecked(1)
        else:
            self.ui.AQstatus_box.setChecked(0)

        #--------- Aquifer Storage/Recovery -----------------------------------#
        if self.module.getParameter("ASRstatus") == 1:
            self.ui.ASRstatus_box.setChecked(1)
        else:
            self.ui.ASRstatus_box.setChecked(0)

        #--------- Biofiltration/Raingardens ----------------------------------#
        if self.module.getParameter("BFstatus") == 1:
            self.ui.BFstatus_box.setChecked(1)
        else:
            self.ui.BFstatus_box.setChecked(0)

        #Available Scales
        if self.module.getParameter("BFlot") == 1:
            self.ui.BFlot_check.setChecked(1)
        else:
            self.ui.BFlot_check.setChecked(0)

        if self.module.getParameter("BFstreet") == 1:
            self.ui.BFstreet_check.setChecked(1)
        else:
            self.ui.BFstreet_check.setChecked(0)

        if self.module.getParameter("BFneigh") == 1:
            self.ui.BFneigh_check.setChecked(1)
        else:
            self.ui.BFneigh_check.setChecked(0)

        if self.module.getParameter("BFprec") == 1:
            self.ui.BFprec_check.setChecked(1)
        else:
            self.ui.BFprec_check.setChecked(0)

        #Available Applications
        if self.module.getParameter("BFflow") == 1:
            self.ui.BFflow_check.setChecked(1)
        else:
            self.ui.BFflow_check.setChecked(0)

        if self.module.getParameter("BFpollute") == 1:
            self.ui.BFpollute_check.setChecked(1)
        else:
            self.ui.BFpollute_check.setChecked(0)

        if self.module.getParameter("BFrecycle") == 1:
            self.ui.BFrecycle_check.setChecked(1)
        else:
            self.ui.BFrecycle_check.setChecked(0)

        #Design Curves
        if self.module.getParameter("BFdesignUB") == 1:
            self.ui.BFdesignUB_box.setChecked(1)
        else:
            self.ui.BFdesignUB_box.setChecked(0)

        if self.module.getParameter("BFdesignUB") == 1:
            self.ui.BFdesignUB_box.setChecked(1)
            self.ui.BFdesigncurve_browse.setEnabled(0)
            self.ui.BFdesigncurve_pathbox.setText("no file")
        else:
            self.ui.BFdesignUB_box.setChecked(0)
            self.ui.BFdesigncurve_browse.setEnabled(1)
            self.ui.BFdesigncurve_pathbox.setText(str(self.module.getParameter("BFdescur_path")))

        QtCore.QObject.connect(self.ui.BFdesigncurve_browse, QtCore.SIGNAL("clicked()"), self.openFileDialog_BF)
        QtCore.QObject.connect(self.ui.BFdesignUB_box, QtCore.SIGNAL("clicked()"), self.BFdesign_enable)

        #Design Information

        #COMBO BOXES CONTAINING EDD AND FD SPECS
        if self.module.getParameter("BFspec_EDD") == 0:
            self.ui.BFspecs_EDD_combo.setCurrentIndex(0)
        elif self.module.getParameter("BFspec_EDD") == 0.1:
            self.ui.BFspecs_EDD_combo.setCurrentIndex(1)
        elif self.module.getParameter("BFspec_EDD") == 0.2:
            self.ui.BFspecs_EDD_combo.setCurrentIndex(2)
        elif self.module.getParameter("BFspec_EDD") == 0.3:
            self.ui.BFspecs_EDD_combo.setCurrentIndex(3)
        elif self.module.getParameter("BFspec_EDD") == 0.4:
            self.ui.BFspecs_EDD_combo.setCurrentIndex(4)

        if self.module.getParameter("BFspec_FD") == 0.2:
            self.ui.BFspecs_FD_combo.setCurrentIndex(0)
        elif self.module.getParameter("BFspec_FD") == 0.4:
            self.ui.BFspecs_FD_combo.setCurrentIndex(1)
        elif self.module.getParameter("BFspec_FD") == 0.6:
            self.ui.BFspecs_FD_combo.setCurrentIndex(2)
        elif self.module.getParameter("BFspec_FD") == 0.8:
            self.ui.BFspecs_FD_combo.setCurrentIndex(3)

        if self.module.getParameter("BFexfil") == 0:
            self.ui.BFexfil_combo.setCurrentIndex(0)
        elif self.module.getParameter("BFexfil") == 0.18:
            self.ui.BFexfil_combo.setCurrentIndex(1)
        elif self.module.getParameter("BFexfil") == 0.36:
            self.ui.BFexfil_combo.setCurrentIndex(2)
        elif self.module.getParameter("BFexfil") == 1.8:
            self.ui.BFexfil_combo.setCurrentIndex(3)
        elif self.module.getParameter("BFexfil") == 3.6:
            self.ui.BFexfil_combo.setCurrentIndex(4)

        self.ui.BFminsize_box.setText(str(self.module.getParameter("BFminsize")))
        self.ui.BFmaxsize_box.setText(str(self.module.getParameter("BFmaxsize")))
        self.ui.BFavglifespin.setValue(int(self.module.getParameter("BFavglife")))

        #futher design info coming soon

        #--------- Green Roof -------------------------------------------------#
        if self.module.getParameter("GRstatus") == 1:
            self.ui.GRstatus_box.setChecked(1)
        else:
            self.ui.GRstatus_box.setChecked(0)

        #--------- Greywater Tank/Treatment -----------------------------------#
        if self.module.getParameter("GTstatus") == 1:
            self.ui.GTstatus_box.setChecked(1)
        else:
            self.ui.GTstatus_box.setChecked(0)

        #--------- Gross Pollutant Trap ---------------------------------------#
        if self.module.getParameter("GPTstatus") == 1:
            self.ui.GPTstatus_box.setChecked(1)
        else:
            self.ui.GPTstatus_box.setChecked(0)

        #--------- Infiltration System ----------------------------------------#
        if self.module.getParameter("ISstatus") == 1:
            self.ui.ISstatus_box.setChecked(1)
        else:
            self.ui.ISstatus_box.setChecked(0)

        #Available Scales
        if self.module.getParameter("ISlot") == 1:
            self.ui.ISlot_check.setChecked(1)
        else:
            self.ui.ISlot_check.setChecked(0)

        if self.module.getParameter("ISstreet") == 1:
            self.ui.ISstreet_check.setChecked(1)
        else:
            self.ui.ISstreet_check.setChecked(0)

        if self.module.getParameter("ISneigh") == 1:
            self.ui.ISneigh_check.setChecked(1)
        else:
            self.ui.ISneigh_check.setChecked(0)

        #Available Applications
        if self.module.getParameter("ISflow") == 1:
            self.ui.ISflow_check.setChecked(1)
        else:
            self.ui.ISflow_check.setChecked(0)

        if self.module.getParameter("ISpollute") == 1:
            self.ui.ISpollute_check.setChecked(1)
        else:
            self.ui.ISpollute_check.setChecked(0)

        #Design Curves
        if self.module.getParameter("ISdesignUB") == 1:
            self.ui.ISdesignUB_box.setChecked(1)
            self.ui.ISdesigncurve_browse.setEnabled(0)
            self.ui.ISdesigncurve_pathbox.setText("no file")
        else:
            self.ui.ISdesignUB_box.setChecked(0)
            self.ui.ISdesigncurve_browse.setEnabled(1)
            self.ui.ISdesigncurve_pathbox.setText(str(self.module.getParameter("ISdescur_path")))

        QtCore.QObject.connect(self.ui.ISdesigncurve_browse, QtCore.SIGNAL("clicked()"), self.openFileDialog_IS)
        QtCore.QObject.connect(self.ui.ISdesignUB_box, QtCore.SIGNAL("clicked()"), self.ISdesign_enable)

        #Design Information

        #COMBO BOXES CONTAINING EDD AND FD SPECS
        if self.module.getParameter("ISspec_EDD") == 0.1:
            self.ui.ISspecs_EDD_combo.setCurrentIndex(0)
        elif self.module.getParameter("ISspec_EDD") == 0.2:
            self.ui.ISspecs_EDD_combo.setCurrentIndex(1)
        elif self.module.getParameter("ISspec_EDD") == 0.3:
            self.ui.ISspecs_EDD_combo.setCurrentIndex(2)
        elif self.module.getParameter("ISspec_EDD") == 0.4:
            self.ui.ISspecs_EDD_combo.setCurrentIndex(3)

        if self.module.getParameter("ISspec_FD") == 0.2:
            self.ui.ISspecs_FD_combo.setCurrentIndex(0)
        elif self.module.getParameter("ISspec_FD") == 0.4:
            self.ui.ISspecs_FD_combo.setCurrentIndex(1)
        elif self.module.getParameter("ISspec_FD") == 0.6:
            self.ui.ISspecs_FD_combo.setCurrentIndex(2)
        elif self.module.getParameter("ISspec_FD") == 0.8:
            self.ui.ISspecs_FD_combo.setCurrentIndex(3)
        print self.module.getParameter("ISexfil")
        if self.module.getParameter("ISexfil") == 0.18:
            self.ui.ISexfil_combo.setCurrentIndex(0)
        elif self.module.getParameter("ISexfil") == 0.36:
            self.ui.ISexfil_combo.setCurrentIndex(1)
        elif self.module.getParameter("ISexfil") == 1.8:
            self.ui.ISexfil_combo.setCurrentIndex(2)
        elif self.module.getParameter("ISexfil") == 3.6:
            self.ui.ISexfil_combo.setCurrentIndex(3)

        self.ui.ISminsize_box.setText(str(self.module.getParameter("ISminsize")))
        self.ui.ISmaxsize_box.setText(str(self.module.getParameter("ISmaxsize")))
        self.ui.ISavglifespin.setValue(int(self.module.getParameter("ISavglife")))

        #--------- Packaged Plant ---------------------------------------------#
        if self.module.getParameter("PPLstatus") == 1:
            self.ui.PPLstatus_box.setChecked(1)
        else:
            self.ui.PPLstatus_box.setChecked(0)

        #--------- Ponds/Sedimentation Basin ----------------------------------#
        if self.module.getParameter("PBstatus") == 1:
            self.ui.PBstatus_box.setChecked(1)
        else:
            self.ui.PBstatus_box.setChecked(0)

        #Available Scales
        if self.module.getParameter("PBneigh") == 1:
            self.ui.PBneigh_check.setChecked(1)
        else:
            self.ui.PBneigh_check.setChecked(0)

        if self.module.getParameter("PBprec") == 1:
            self.ui.PBprec_check.setChecked(1)
        else:
            self.ui.PBprec_check.setChecked(0)

        #Available Applications
        if self.module.getParameter("PBflow") == 1:
            self.ui.PBflow_check.setChecked(1)
        else:
            self.ui.PBflow_check.setChecked(0)

        if self.module.getParameter("PBpollute") == 1:
            self.ui.PBpollute_check.setChecked(1)
        else:
            self.ui.PBpollute_check.setChecked(0)

        if self.module.getParameter("PBrecycle") == 1:
            self.ui.PBrecycle_check.setChecked(1)
        else:
            self.ui.PBrecycle_check.setChecked(0)

        #Design Curves
        if self.module.getParameter("PBdesignUB") == 1:
            self.ui.PBdesignUB_box.setChecked(1)
        else:
            self.ui.PBdesignUB_box.setChecked(0)

        if self.module.getParameter("PBdesignUB") == 1:
            self.ui.PBdesignUB_box.setChecked(1)
            self.ui.PBdesigncurve_browse.setEnabled(0)
            self.ui.PBdesigncurve_pathbox.setText("no file")
        else:
            self.ui.PBdesignUB_box.setChecked(0)
            self.ui.PBdesigncurve_browse.setEnabled(1)
            self.ui.PBdesigncurve_pathbox.setText(str(self.module.getParameter("PBdescur_path")))

        QtCore.QObject.connect(self.ui.PBdesigncurve_browse, QtCore.SIGNAL("clicked()"), self.openFileDialog_PB)
        QtCore.QObject.connect(self.ui.PBdesignUB_box, QtCore.SIGNAL("clicked()"), self.PBdesign_enable)

        #Design Information

        #combo box with specs
        if self.module.getParameter("PBspec_MD") == 0.25:
            self.ui.PBspecs_combo.setCurrentIndex(0)
        elif self.module.getParameter("PBspec_MD") == 0.50:
            self.ui.PBspecs_combo.setCurrentIndex(1)
        elif self.module.getParameter("PBspec_MD") == 0.75:
            self.ui.PBspecs_combo.setCurrentIndex(2)
        elif self.module.getParameter("PBspec_MD") == 1.00:
            self.ui.PBspecs_combo.setCurrentIndex(3)
        elif self.module.getParameter("PBspec_MD") == 1.25:
            self.ui.PBspecs_combo.setCurrentIndex(4)

        if self.module.getParameter("PBexfil") == 0:
            self.ui.PBexfil_combo.setCurrentIndex(0)
        elif self.module.getParameter("PBexfil") == 0.18:
            self.ui.PBexfil_combo.setCurrentIndex(1)
        elif self.module.getParameter("PBexfil") == 0.36:
            self.ui.PBexfil_combo.setCurrentIndex(2)
        elif self.module.getParameter("PBexfil") == 1.8:
            self.ui.PBexfil_combo.setCurrentIndex(3)
        elif self.module.getParameter("PBexfil") == 3.6:
            self.ui.PBexfil_combo.setCurrentIndex(4)

        self.ui.PBminsize_box.setText(str(self.module.getParameter("PBminsize")))
        self.ui.PBmaxsize_box.setText(str(self.module.getParameter("PBmaxsize")))
        self.ui.PBavglifespin.setValue(int(self.module.getParameter("PBavglife")))

        #futher design info coming soon

        #---------- Porous/Pervious Pavement ----------------------------------#
        if self.module.getParameter("PPstatus") == 1:
            self.ui.PPstatus_box.setChecked(1)
        else:
            self.ui.PPstatus_box.setChecked(0)

        #---------- Rainwater Tank --------------------------------------------#
        if self.module.getParameter("RTstatus") == 1:
            self.ui.RTstatus_box.setChecked(1)
        else:
            self.ui.RTstatus_box.setChecked(0)

        self.ui.RT_maxdepth_box.setText(str(self.module.getParameter("RT_maxdepth")))
        self.ui.RT_mindead_box.setText(str(self.module.getParameter("RT_mindead")))

        if self.module.getParameter("RTlot") == 1:
            self.ui.RTscale_lot_box.setChecked(1)
        else:
            self.ui.RTscale_lot_box.setChecked(0)

        if self.module.getParameter("RTneigh") == 1:
            self.ui.RTscale_neighb_box.setChecked(1)
        else:
            self.ui.RTscale_neighb_box.setChecked(0)

        if self.module.getParameter("RTflow") == 1:
            self.ui.RTpurp_flood_box.setChecked(1)
        else:
            self.ui.RTpurp_flood_box.setChecked(0)

        if self.module.getParameter("RTrecycle") == 1:
            self.ui.RTpurp_recyc_box.setChecked(1)
        else:
            self.ui.RTpurp_recyc_box.setChecked(0)

        if self.module.getParameter("RTdesignUB") == 1:
            self.ui.RTdesignUB_box.setChecked(1)
            self.ui.RTdesigncurve_browse.setEnabled(0)
            self.ui.RTdesigncurve_pathbox.setText("no file")
        else:
            self.ui.RTdesignUB_box.setChecked(0)
            self.ui.RTdesigncurve_browse.setEnabled(1)
            self.ui.RTdesigncurve_pathbox.setText(str(self.module.getParameter("RTdescur_path")))

        QtCore.QObject.connect(self.ui.RTdesigncurve_browse, QtCore.SIGNAL("clicked()"), self.openFileDialog_RT)
        QtCore.QObject.connect(self.ui.RTdesignUB_box, QtCore.SIGNAL("clicked()"), self.RTdesign_enable)

        #---------- Sand/Peat/Gravel Filter -----------------------------------#
        if self.module.getParameter("SFstatus") == 1:
            self.ui.SFstatus_box.setChecked(1)
        else:
            self.ui.SFstatus_box.setChecked(0)

        #---------- Subsurface Irrigation System ------------------------------#
        if self.module.getParameter("IRRstatus") == 1:
            self.ui.IRRstatus_box.setChecked(1)
        else:
            self.ui.IRRstatus_box.setChecked(0)

        #---------- Subsurface Wetland/Reed Bed -------------------------------#
        if self.module.getParameter("WSUBstatus") == 1:
            self.ui.WSUBstatus_box.setChecked(1)
        else:
            self.ui.WSUBstatus_box.setChecked(0)

        #---------- Surface Wetland -------------------------------------------#
        if self.module.getParameter("WSURstatus") == 1:
            self.ui.WSURstatus_box.setChecked(1)
        else:
            self.ui.WSURstatus_box.setChecked(0)

        #Available Scales
        if self.module.getParameter("WSURneigh") == 1:
            self.ui.WSURneigh_check.setChecked(1)
        else:
            self.ui.WSURneigh_check.setChecked(0)

        if self.module.getParameter("PBprec") == 1:
            self.ui.WSURprec_check.setChecked(1)
        else:
            self.ui.WSURprec_check.setChecked(0)

        #Available Applications
        if self.module.getParameter("WSURflow") == 1:
            self.ui.WSURflow_check.setChecked(1)
        else:
            self.ui.WSURflow_check.setChecked(0)

        if self.module.getParameter("WSURpollute") == 1:
            self.ui.WSURpollute_check.setChecked(1)
        else:
            self.ui.WSURpollute_check.setChecked(0)

        if self.module.getParameter("WSURrecycle") == 1:
            self.ui.WSURrecycle_check.setChecked(1)
        else:
            self.ui.WSURrecycle_check.setChecked(0)

        #Design Curves
        if self.module.getParameter("WSURdesignUB") == 1:
            self.ui.WSURdesignUB_box.setChecked(1)
        else:
            self.ui.WSURdesignUB_box.setChecked(0)

        if self.module.getParameter("WSURdesignUB") == 1:
            self.ui.WSURdesignUB_box.setChecked(1)
            self.ui.WSURdesigncurve_browse.setEnabled(0)
            self.ui.WSURdesigncurve_pathbox.setText("no file")
        else:
            self.ui.WSURdesignUB_box.setChecked(0)
            self.ui.WSURdesigncurve_browse.setEnabled(1)
            self.ui.WSURdesigncurve_pathbox.setText(str(self.module.getParameter("PBdescur_path")))

        QtCore.QObject.connect(self.ui.WSURdesigncurve_browse, QtCore.SIGNAL("clicked()"), self.openFileDialog_WSUR)
        QtCore.QObject.connect(self.ui.WSURdesignUB_box, QtCore.SIGNAL("clicked()"), self.WSURdesign_enable)

        #Design Information

        #combo box with specs
        if self.module.getParameter("WSURspec_EDD") == 0.25:
            self.ui.WSURspecs_combo.setCurrentIndex(0)
        elif self.module.getParameter("WSURspec_EDD") == 0.50:
            self.ui.WSURspecs_combo.setCurrentIndex(1)
        elif self.module.getParameter("WSURspec_EDD") == 0.75:
            self.ui.WSURspecs_combo.setCurrentIndex(2)
        elif self.module.getParameter("WSURspec_EDD") == 0.25:
            self.ui.WSURspecs_combo.setCurrentIndex(3)
        elif self.module.getParameter("WSURspec_EDD") == 0.50:
            self.ui.WSURspecs_combo.setCurrentIndex(4)
        elif self.module.getParameter("WSURspec_EDD") == 0.75:
            self.ui.WSURspecs_combo.setCurrentIndex(5)

        if self.module.getParameter("WSURexfil") == 0:
            self.ui.WSURexfil_combo.setCurrentIndex(0)
        elif self.module.getParameter("WSURexfil") == 0.18:
            self.ui.WSURexfil_combo.setCurrentIndex(1)
        elif self.module.getParameter("WSURexfil") == 0.36:
            self.ui.WSURexfil_combo.setCurrentIndex(2)
        elif self.module.getParameter("WSURexfil") == 1.8:
            self.ui.WSURexfil_combo.setCurrentIndex(3)
        elif self.module.getParameter("WSURexfil") == 3.6:
            self.ui.WSURexfil_combo.setCurrentIndex(4)

        self.ui.WSURminsize_box.setText(str(self.module.getParameter("WSURminsize")))
        self.ui.WSURmaxsize_box.setText(str(self.module.getParameter("WSURmaxsize")))
        self.ui.WSURavglifespin.setValue(int(self.module.getParameter("WSURavglife")))
        #futher design info coming soon

        #---------- Swales/Buffer Strips --------------------------------------#
        if self.module.getParameter("SWstatus") == 1:
            self.ui.SWstatus_box.setChecked(1)
        else:
            self.ui.SWstatus_box.setChecked(0)

        #Available Scales
        if self.module.getParameter("SWstreet") == 1:
            self.ui.SWstreet_check.setChecked(1)
        else:
            self.ui.SWstreet_check.setChecked(0)

        if self.module.getParameter("SWneigh") == 1:
            self.ui.SWneigh_check.setChecked(1)
        else:
            self.ui.SWneigh_check.setChecked(0)

        #Available Applications
        if self.module.getParameter("SWflow") == 1:
            self.ui.SWflow_check.setChecked(1)
        else:
            self.ui.SWflow_check.setChecked(0)

        if self.module.getParameter("SWpollute") == 1:
            self.ui.SWpollute_check.setChecked(1)
        else:
            self.ui.SWpollute_check.setChecked(0)

        #Design Curves
        if self.module.getParameter("SWdesignUB") == 1:
            self.ui.SWdesignUB_box.setChecked(1)
        else:
            self.ui.SWdesignUB_box.setChecked(0)

        if self.module.getParameter("SWdesignUB") == 1:
            self.ui.SWdesignUB_box.setChecked(1)
            self.ui.SWdesigncurve_browse.setEnabled(0)
            self.ui.SWdesigncurve_pathbox.setText("no file")
        else:
            self.ui.SWdesignUB_box.setChecked(0)
            self.ui.SWdesigncurve_browse.setEnabled(1)
            self.ui.SWdesigncurve_pathbox.setText(str(self.module.getParameter("SWdescur_path")))

        QtCore.QObject.connect(self.ui.SWdesigncurve_browse, QtCore.SIGNAL("clicked()"), self.openFileDialog_SW)
        QtCore.QObject.connect(self.ui.SWdesignUB_box, QtCore.SIGNAL("clicked()"), self.SWdesign_enable)

        #Design Information

        if self.module.getParameter("SWexfil") == 0:
            self.ui.SWexfil_combo.setCurrentIndex(0)
        elif self.module.getParameter("SWexfil") == 0.18:
            self.ui.SWexfil_combo.setCurrentIndex(1)
        elif self.module.getParameter("SWexfil") == 0.36:
            self.ui.SWexfil_combo.setCurrentIndex(2)
        elif self.module.getParameter("SWexfil") == 1.8:
            self.ui.SWexfil_combo.setCurrentIndex(3)
        elif self.module.getParameter("SWexfil") == 3.6:
            self.ui.SWexfil_combo.setCurrentIndex(4)

        #combo box with specs
        self.ui.SWminsize_box.setText(str(self.module.getParameter("SWminsize")))
        self.ui.SWmaxsize_box.setText(str(self.module.getParameter("SWmaxsize")))
        self.ui.SWavglifespin.setValue(int(self.module.getParameter("SWavglife")))
        #futher design info coming soon

        #--------- Tree Pits --------------------------------------------------#
        if self.module.getParameter("TPSstatus") == 1:
            self.ui.TPSstatus_box.setChecked(1)
        else:
            self.ui.TPSstatus_box.setChecked(0)

        #---------- Urine-Separation Toilets ----------------------------------#
        if self.module.getParameter("UTstatus") == 1:
            self.ui.UTstatus_box.setChecked(1)
        else:
            self.ui.UTstatus_box.setChecked(0)

        #---------- Wastewater Recovery/Recycling Plant -----------------------#
        if self.module.getParameter("WWRRstatus") == 1:
            self.ui.WWRRstatus_box.setChecked(1)
        else:
            self.ui.WWRRstatus_box.setChecked(0)

        #---------- Waterless/Composting Toilet -------------------------------#
        if self.module.getParameter("WTstatus") == 1:
            self.ui.WTstatus_box.setChecked(1)
        else:
            self.ui.WTstatus_box.setChecked(0)

        #--- ## --- Regional Information --------------------------------------#
        if self.module.getParameter("regioncity") == "Adelaide":
            self.ui.regioncity_combo.setCurrentIndex(0)
        elif self.module.getParameter("regioncity") == "Brisbane":
            self.ui.regioncity_combo.setCurrentIndex(1)
        elif self.module.getParameter("regioncity") == "Melbourne":
            self.ui.regioncity_combo.setCurrentIndex(2)
        elif self.module.getParameter("regioncity") == "Perth":
            self.ui.regioncity_combo.setCurrentIndex(3)
        elif self.module.getParameter("regioncity") == "Sydney":
            self.ui.regioncity_combo.setCurrentIndex(4)

        #######################################
        #Select Evaluation Criteria Tab
        #######################################
        #-------- Evaluation Metrics Select------------------------------------#
        if self.module.getParameter("scoringmatrix_default") == 1:
            self.ui.mca_scoringmat_check.setChecked(1)
            self.ui.mca_scoringmat_browse.setEnabled(0)
            self.ui.mca_scoringmat_box.setText("no file")
            self.ui.bottomlines_techN_spin.setEnabled(0)
            self.ui.bottomlines_envN_spin.setEnabled(0)
            self.ui.bottomlines_ecnN_spin.setEnabled(0)
            self.ui.bottomlines_socN_spin.setEnabled(0)
        else:
            self.ui.mca_scoringmat_check.setChecked(0)
            self.ui.mca_scoringmat_browse.setEnabled(1)
            self.ui.mca_scoringmat_box.setText(str(self.module.getParameter("scoringmatrix_path")))
            self.ui.bottomlines_techN_spin.setEnabled(1)
            self.ui.bottomlines_envN_spin.setEnabled(1)
            self.ui.bottomlines_ecnN_spin.setEnabled(1)
            self.ui.bottomlines_socN_spin.setEnabled(1)

        QtCore.QObject.connect(self.ui.mca_scoringmat_browse, QtCore.SIGNAL("clicked()"), self.openFileDialog_mca)
        QtCore.QObject.connect(self.ui.mca_scoringmat_check, QtCore.SIGNAL("clicked()"), self.mca_scoringmat_enable)

        #-------- Customize Evaluation Criteria--------------------------------#
        if self.module.getParameter("bottomlines_tech") == 1:
            self.ui.bottomlines_tech_check.setChecked(1)
        else:
            self.ui.bottomlines_tech_check.setChecked(0)

        if self.module.getParameter("bottomlines_env") == 1:
            self.ui.bottomlines_env_check.setChecked(1)
        else:
            self.ui.bottomlines_env_check.setChecked(0)

        if self.module.getParameter("bottomlines_ecn") == 1:
            self.ui.bottomlines_ecn_check.setChecked(1)
        else:
            self.ui.bottomlines_ecn_check.setChecked(0)

        if self.module.getParameter("bottomlines_soc") == 1:
            self.ui.bottomlines_soc_check.setChecked(1)
        else:
            self.ui.bottomlines_soc_check.setChecked(0)

        self.ui.bottomlines_techN_spin.setValue(int(self.module.getParameter("bottomlines_tech_n")))
        self.ui.bottomlines_envN_spin.setValue(int(self.module.getParameter("bottomlines_env_n")))
        self.ui.bottomlines_ecnN_spin.setValue(int(self.module.getParameter("bottomlines_ecn_n")))
        self.ui.bottomlines_socN_spin.setValue(int(self.module.getParameter("bottomlines_soc_n")))

        self.ui.bottomlines_techW_spin.setValue(int(self.module.getParameter("bottomlines_tech_w")))
        self.ui.bottomlines_envW_spin.setValue(int(self.module.getParameter("bottomlines_env_w")))
        self.ui.bottomlines_ecnW_spin.setValue(int(self.module.getParameter("bottomlines_ecn_w")))
        self.ui.bottomlines_socW_spin.setValue(int(self.module.getParameter("bottomlines_soc_w")))

        #-------- EVALUATION SCOPE & METHOD -----------------------------------#
        if self.module.getParameter("score_method") == "WPM":
            self.ui.eval_method_combo.setCurrentIndex(0)
        elif self.module.getParameter("score_method") == "WSM":
            self.ui.eval_method_combo.setCurrentIndex(1)

        if self.module.getParameter("scope_stoch") == 1:
            self.ui.scope_stoch_check.setChecked(1)
        else:
            self.ui.scope_stoch_check.setChecked(0)

        if self.module.getParameter("ingroup_scoring") == "Avg":
            self.ui.radioScoreAvg.setChecked(True)
        if self.module.getParameter("ingroup_scoring") == "Med":
            self.ui.radioScoreMed.setChecked(True)
        if self.module.getParameter("ingroup_scoring") == "Min":
            self.ui.radioScoreMin.setChecked(True)
        if self.module.getParameter("ingroup_scoring") == "Max":
            self.ui.radioScoreMax.setChecked(True)

        #-------- RANKING OF STRATEGIES ---------------------------------------#
        if self.module.getParameter("ranktype") == "RK":
            self.ui.top_score_combo.setCurrentIndex(0)
            self.ui.top_rank_spin.setEnabled(1)
            self.ui.top_CI_spin.setEnabled(0)
        elif self.module.getParameter("ranktype") == "CI":
            self.ui.top_score_combo.setCurrentIndex(1)
            self.ui.top_rank_spin.setEnabled(0)
            self.ui.top_CI_spin.setEnabled(1)

        QtCore.QObject.connect(self.ui.top_score_combo, QtCore.SIGNAL("currentIndexChanged(int)"), self.top_score_change)

        self.ui.top_rank_spin.setValue(int(self.module.getParameter("topranklimit")))
        self.ui.top_CI_spin.setValue(int(self.module.getParameter("conf_int")))

        #CONNECT DETAILS WITH THE OK BUTTON SO THAT GUI UPDATES MODULE
        QtCore.QObject.connect(self.ui.buttonBox, QtCore.SIGNAL("accepted()"), self.save_values)
        
    ### GENERAL TAB ###
    def enableLotRigour(self):
        if self.ui.strategy_lot_check.isChecked() == True:
            self.ui.strategy_lot_rigour.setEnabled(1)
            self.ui.strategy_lot_rigour_box.setEnabled(1)
        else:
            self.ui.strategy_lot_rigour.setEnabled(0)
            self.ui.strategy_lot_rigour_box.setEnabled(0)

    def enableStreetRigour(self):
        if self.ui.strategy_street_check.isChecked() == True:
            self.ui.strategy_street_rigour.setEnabled(1)
            self.ui.strategy_street_rigour_box.setEnabled(1)
        else:
            self.ui.strategy_street_rigour.setEnabled(0)
            self.ui.strategy_street_rigour_box.setEnabled(0)

    def enableNeighRigour(self):
        if self.ui.strategy_neigh_check.isChecked() == True:
            self.ui.strategy_neigh_rigour.setEnabled(1)
            self.ui.strategy_neigh_rigour_box.setEnabled(1)
        else:
            self.ui.strategy_neigh_rigour.setEnabled(0)
            self.ui.strategy_neigh_rigour_box.setEnabled(0)

    def enableSubbasRigour(self):
        if self.ui.strategy_subbas_check.isChecked() == True:
            self.ui.strategy_subbas_rigour.setEnabled(1)
            self.ui.strategy_subbas_rigour_box.setEnabled(1)
        else:
            self.ui.strategy_subbas_rigour.setEnabled(0)
            self.ui.strategy_subbas_rigour_box.setEnabled(0)

    def adjustRigourLot(self, currentValue):
        self.ui.strategy_lot_rigour_box.setText(str(currentValue))

    def adjustRigourStreet(self, currentValue):
        self.ui.strategy_street_rigour_box.setText(str(currentValue))

    def adjustRigourNeigh(self, currentValue):
        self.ui.strategy_neigh_rigour_box.setText(str(currentValue))

    def adjustRigourSubbas(self, currentValue):
        self.ui.strategy_subbas_rigour_box.setText(str(currentValue))

    ### RETROFIT TAB ###
    def decom_update(self, currentValue):
        self.ui.decom_box.setText(str(currentValue)+"%")
        self.module.setParameter("decom_thresh", str(currentValue))
        if self.ui.renew_slider.value() > self.ui.decom_slider.value():
            self.renew_all_update(self.ui.decom_slider.value())

    def renew_update(self, currentValue):
        self.ui.renew_box.setText(str(currentValue)+"%")
        self.module.setParameter("renewal_thresh", str(currentValue))
        if self.ui.renew_slider.value() > self.ui.decom_slider.value():
            self.renew_all_update(self.ui.decom_slider.value())

    def renew_all_update(self, currentValue):
        self.ui.renew_box.setText(str(currentValue)+"%")
        self.ui.renew_slider.setValue(currentValue)
        self.module.setParameter("renewal_thresh", str(currentValue))

    def update_retrofitoptions(self, currentind):
        if currentind == 0:
            self.ui.lot_renew_check.setEnabled(0)
            self.ui.lot_decom_check.setEnabled(0)
            self.ui.street_decom_check.setEnabled(0)
            self.ui.street_renew_check.setEnabled(0)
            self.ui.neigh_renew_check.setEnabled(0)
            self.ui.neigh_decom_check.setEnabled(0)
            self.ui.prec_renew_check.setEnabled(0)
            self.ui.prec_decom_check.setEnabled(0)
            self.ui.decom_slider.setEnabled(0)
            self.ui.decom_box.setEnabled(0)
            self.ui.renew_slider.setEnabled(0)
            self.ui.renew_box.setEnabled(0)
            self.ui.radioKeep.setEnabled(0)
            self.ui.radioDecom.setEnabled(0)
        else:
            self.ui.lot_renew_check.setEnabled(1)
            self.ui.lot_decom_check.setEnabled(1)
            self.ui.street_decom_check.setEnabled(1)
            self.ui.street_renew_check.setEnabled(1)
            self.ui.neigh_renew_check.setEnabled(1)
            self.ui.neigh_decom_check.setEnabled(1)
            self.ui.prec_renew_check.setEnabled(1)
            self.ui.prec_decom_check.setEnabled(1)
            self.ui.decom_slider.setEnabled(1)
            self.ui.decom_box.setEnabled(1)
            self.ui.renew_slider.setEnabled(1)
            self.ui.renew_box.setEnabled(1)
            self.ui.radioKeep.setEnabled(1)
            self.ui.radioDecom.setEnabled(1)

    ### WATER USE AND RECYCLING ###
    def WEF_consider_update(self):
        if self.ui.WEF_consider.isChecked() == 1:
            self.ui.WEF_rating_system_combo.setEnabled(1)
            self.ui.WEF_loc_house_check.setEnabled(1)
            self.ui.WEF_loc_apart_check.setEnabled(1)
            self.ui.WEF_constant_radio.setEnabled(1)
            self.ui.WEF_distribution_radio.setEnabled(1)
            if self.ui.WEF_constant_radio.isChecked() == 1:
                self.ui.WEF_constant_combo.setEnabled(1)
            elif self.ui.WEF_distribution_radio.isChecked() == 1:
                self.ui.WEF_distribution_combo.setEnabled(1)
                self.ui.WEF_distribution_select.setEnabled(1)
                self.ui.WEF_distribution_check.setEnabled(1)
        else:
            self.ui.WEF_consider.setChecked(0)
            self.ui.WEF_rating_system_combo.setEnabled(0)
            self.ui.WEF_loc_house_check.setEnabled(0)
            self.ui.WEF_loc_apart_check.setEnabled(0)
            self.ui.WEF_constant_radio.setEnabled(0)
            self.ui.WEF_distribution_radio.setEnabled(0)
            self.ui.WEF_constant_combo.setEnabled(0)
            self.ui.WEF_distribution_combo.setEnabled(0)
            self.ui.WEF_distribution_select.setEnabled(0)
            self.ui.WEF_distribution_check.setEnabled(0)

    def update_WEF_determine(self):
        if self.ui.WEF_constant_radio.isChecked() == True:
            self.ui.WEF_constant_combo.setEnabled(1)
            self.ui.WEF_distribution_combo.setEnabled(0)
            self.ui.WEF_distribution_select.setEnabled(0)
            self.ui.WEF_distribution_check.setEnabled(0)
        elif self.ui.WEF_distribution_radio.isChecked() == True:
            self.ui.WEF_constant_combo.setEnabled(0)
            self.ui.WEF_distribution_combo.setEnabled(1)
            self.ui.WEF_distribution_select.setEnabled(1)
            self.ui.WEF_distribution_check.setEnabled(1)

    ### TECHNOLOGIES TABS ###

    #BIOFILTRATION SYSTEMS SIGNAL-SLOT FUNCTIONS
    def openFileDialog_BF(self):
        fname = QtGui.QFileDialog.getOpenFileName(self, "Choose Design Curve File...", os.curdir, str("Design Curves (*.dcv *.txt)"))
        if fname:
            self.ui.BFdesigncurve_pathbox.setText(fname)
    def BFdesign_enable(self):
        if self.ui.BFdesignUB_box.isChecked() == 1:
            self.ui.BFdesigncurve_browse.setEnabled(0)
        else:
            self.ui.BFdesigncurve_browse.setEnabled(1)

    #INFILTRATION SYSTEMS SIGNAL-SLOT FUNCTIONS
    def openFileDialog_IS(self):
        fname = QtGui.QFileDialog.getOpenFileName(self, "Choose Design Curve File...", os.curdir, str("Design Curves (*.dcv *.txt)"))
        if fname:
            self.ui.ISdesigncurve_pathbox.setText(fname)
    def ISdesign_enable(self):
        if self.ui.ISdesignUB_box.isChecked() == 1:
            self.ui.ISdesigncurve_browse.setEnabled(0)
        else:
            self.ui.ISdesigncurve_browse.setEnabled(1)

    #PONDS/BASIN SYSTEM SIGNAL-SLOT FUNCTIONS
    def openFileDialog_PB(self):
        fname = QtGui.QFileDialog.getOpenFileName(self, "Choose Design Curve File...", os.curdir, str("Design Curves (*.dcv *.txt)"))
        if fname:
            self.ui.PBdesigncurve_pathbox.setText(fname)
    def PBdesign_enable(self):
        if self.ui.PBdesignUB_box.isChecked() == 1:
            self.ui.PBdesigncurve_browse.setEnabled(0)
        else:
            self.ui.PBdesigncurve_browse.setEnabled(1)

    #RAINWATER TANK SIGNAL-SLOT FUNCTIONS
    def openFileDialog_RT(self):
        fname = QtGui.QFileDialog.getOpenFileName(self, "Choose Design Curve File...", os.curdir, str("Design Curves (*.dcv *.txt)"))
        if fname:
            self.ui.RTdesigncurve_pathbox.setText(fname)
    def RTdesign_enable(self):
        if self.ui.RTdesignD4W_box.isChecked() == 1:
            self.ui.RTdesigncurve_browse.setEnabled(0)
        else:
            self.ui.RTdesigncurve_browse.setEnabled(1)

    #SURFACE WETLAND SYSTEMS SIGNAL-SLOT FUNCTIONS
    def openFileDialog_WSUR(self):
        fname = QtGui.QFileDialog.getOpenFileName(self, "Choose Design Curve File...", os.curdir, str("Design Curves (*.dcv *.txt)"))
        if fname:
            self.ui.WSURdesigncurve_pathbox.setText(fname)
    def WSURdesign_enable(self):
        if self.ui.WSURdesignUB_box.isChecked() == 1:
            self.ui.WSURdesigncurve_browse.setEnabled(0)
        else:
            self.ui.WSURdesigncurve_browse.setEnabled(1)

    #SWALE SYSTEMS SIGNAL-SLOT FUNCTIONS
    def openFileDialog_SW(self):
        fname = QtGui.QFileDialog.getOpenFileName(self, "Choose Design Curve File...", os.curdir, str("Design Curves (*.dcv *.txt)"))
        if fname:
            self.ui.SWdesigncurve_pathbox.setText(fname)
    def SWdesign_enable(self):
        if self.ui.SWdesignUB_box.isChecked() == 1:
            self.ui.SWdesigncurve_browse.setEnabled(0)
        else:
            self.ui.SWdesigncurve_browse.setEnabled(1)

    ### EVALUATION CRITERIA SIGNAL-SLOT FUNCTIONS
    def openFileDialog_mca(self):
        fname = QtGui.QFileDialog.getOpenFileName(self, "Choose scoring matrix...", os.curdir, str("Scoring Matrix (*.csv)"))
        if fname:
            self.ui.mca_scoringmat_box.setText(fname)
    def mca_scoringmat_enable(self):
        if self.ui.mca_scoringmat_check.isChecked() == 1:
            self.ui.mca_scoringmat_browse.setEnabled(0)
            self.ui.bottomlines_techN_spin.setEnabled(0)
            self.ui.bottomlines_envN_spin.setEnabled(0)
            self.ui.bottomlines_ecnN_spin.setEnabled(0)
            self.ui.bottomlines_socN_spin.setEnabled(0)
        else:
            self.ui.mca_scoringmat_browse.setEnabled(1)
            self.ui.bottomlines_techN_spin.setEnabled(1)
            self.ui.bottomlines_envN_spin.setEnabled(1)
            self.ui.bottomlines_ecnN_spin.setEnabled(1)
            self.ui.bottomlines_socN_spin.setEnabled(1)

    def top_score_change(self):
        if self.ui.top_score_combo.currentIndex() == 0:         #RK option
            self.ui.top_rank_spin.setEnabled(1)
            self.ui.top_CI_spin.setEnabled(0)
        if self.ui.top_score_combo.currentIndex() == 1:         #CI option
            self.ui.top_rank_spin.setEnabled(0)
            self.ui.top_CI_spin.setEnabled(1)


    #OK BUTTON PRESS FUNCTION
    def save_values(self):

        ################################
        #Select Design Criteria Tab
        ################################

        #-------- DESIGN RATIONALE --------------------------------------------#
        self.module.setParameter("ration_runoff", int(self.ui.ration_runoff_check.isChecked()))
        self.module.setParameter("ration_pollute", int(self.ui.ration_pollute_check.isChecked()))
        self.module.setParameter("ration_harvest", int(self.ui.ration_harvest_check.isChecked()))
        self.module.setParameter("runoff_pri", self.ui.runoff_pri_spin.value())
        self.module.setParameter("pollute_pri", self.ui.pollute_pri_spin.value())
        self.module.setParameter("harvest_pri", self.ui.harvest_pri_spin.value())

        #-------- MANAGEMENT TARGETS ------------------------------------------#
        self.module.setParameter("targets_runoff", self.ui.targets_runoff_spin.value())
        self.module.setParameter("targets_TSS", self.ui.targets_TSS_spin.value())
        self.module.setParameter("targets_TN", self.ui.targets_TN_spin.value())
        self.module.setParameter("targets_TP", self.ui.targets_TP_spin.value())
        self.module.setParameter("targets_reliability", self.ui.targets_reliability_spin.value())

        #-------- SERVICE LEVELS ----------------------------------------------#
        self.module.setParameter("service_swmQty", self.ui.service_swmQty.value())
        self.module.setParameter("service_swmWQ", self.ui.service_swmWQ.value())
        self.module.setParameter("service_rec", self.ui.service_rec.value())

        self.module.setParameter("service_res", int(self.ui.service_res.isChecked()))
        self.module.setParameter("service_hdr", int(self.ui.service_hdr.isChecked()))
        self.module.setParameter("service_com", int(self.ui.service_com.isChecked()))
        self.module.setParameter("service_li", int(self.ui.service_li.isChecked()))
        self.module.setParameter("service_hi", int(self.ui.service_li.isChecked()))

        self.module.setParameter("service_redundancy", self.ui.service_redundancy.value())
        #-------- STRATEGY SETUP ----------------------------------------------#
        self.module.setParameter("strategy_lot_check", int(self.ui.strategy_lot_check.isChecked()))
        self.module.setParameter("strategy_street_check", int(self.ui.strategy_street_check.isChecked()))
        self.module.setParameter("strategy_neigh_check", int(self.ui.strategy_neigh_check.isChecked()))
        self.module.setParameter("strategy_subbas_check", int(self.ui.strategy_subbas_check.isChecked()))
        self.module.setParameter("lot_rigour", self.ui.strategy_lot_rigour.value())
        self.module.setParameter("street_rigour", self.ui.strategy_street_rigour.value())
        self.module.setParameter("neigh_rigour", self.ui.strategy_neigh_rigour.value())
        self.module.setParameter("subbas_rigour", self.ui.strategy_subbas_rigour.value())

        self.module.setParameter("scalepref", int(self.ui.strategy_scalepref_slider.value()))

        #######################################
        #Retrofit Tab
        #######################################
        retrofit_scenario_matrix = ["N", "R", "F"]
        retrofit_index = self.ui.area_retrofit_combo.currentIndex()
        retrofit_scenario = retrofit_scenario_matrix[retrofit_index]
        self.module.setParameter("retrofit_scenario", str(retrofit_scenario))

        if self.ui.retrofit_renewal_check.isChecked() == 1:
            renewal_cycle_def = 1
        else:
            renewal_cycle_def = 0
        self.module.setParameter("renewal_cycle_def", renewal_cycle_def)

        renewal_lot_years = self.ui.renewal_lot_years.value()
        self.module.setParameter("renewal_lot_years", renewal_lot_years)

        renewal_lot_perc = self.ui.renewal_lot_spin.value()
        self.module.setParameter("renewal_lot_perc", renewal_lot_perc)

        renewal_street_years = self.ui.renewal_street_years.value()
        self.module.setParameter("renewal_street_years", renewal_street_years)

        renewal_neigh_years = self.ui.renewal_neigh_years.value()
        self.module.setParameter("renewal_neigh_years", renewal_neigh_years)

        if self.ui.retrofit_forced_street_check.isChecked() == 1:
            force_street = 1
        else:
            force_street = 0
        self.module.setParameter("force_street", force_street)

        if self.ui.retrofit_forced_neigh_check.isChecked() == 1:
            force_neigh = 1
        else:
            force_neigh = 0
        self.module.setParameter("force_neigh", force_neigh)

        if self.ui.retrofit_forced_prec_check.isChecked() == 1:
            force_prec = 1
        else:
            force_prec = 0
        self.module.setParameter("force_prec", force_prec)

        if self.ui.lot_renew_check.isChecked() == 1:
            lot_renew = 1
        else:
            lot_renew = 0
        self.module.setParameter("lot_renew", lot_renew)

        if self.ui.lot_decom_check.isChecked() == 1:
            lot_decom = 1
        else:
            lot_decom = 0
        self.module.setParameter("lot_decom", lot_decom)

        if self.ui.street_renew_check.isChecked() == 1:
            street_renew = 1
        else:
            street_renew = 0
        self.module.setParameter("street_renew", street_renew)

        if self.ui.street_decom_check.isChecked() == 1:
            street_decom = 1
        else:
            street_decom = 0
        self.module.setParameter("street_decom", street_decom)

        if self.ui.neigh_renew_check.isChecked() == 1:
            neigh_renew = 1
        else:
            neigh_renew = 0
        self.module.setParameter("neigh_renew", neigh_renew)

        if self.ui.neigh_decom_check.isChecked() == 1:
            neigh_decom = 1
        else:
            neigh_decom = 0
        self.module.setParameter("neigh_decom", neigh_decom)

        if self.ui.prec_renew_check.isChecked() == 1:
            prec_renew = 1
        else:
            prec_renew = 0
        self.module.setParameter("prec_renew", prec_renew)

        if self.ui.prec_decom_check.isChecked() == 1:
            prec_decom = 1
        else:
            prec_decom = 0
        self.module.setParameter("prec_decom", prec_decom)

        decom_thresh = self.ui.decom_slider.value()
        self.module.setParameter("decom_thresh", decom_thresh)

        renewal_thresh = self.ui.renew_slider.value()
        self.module.setParameter("renewal_thresh", renewal_thresh)

        if self.ui.radioKeep.isChecked() == True:
            renewal_alternative = "K"
        if self.ui.radioDecom.isChecked() == True:
            renewal_alternative = "D"
        self.module.setParameter("renewal_alternative", renewal_alternative)

        #######################################
        #Water Use and Recycling Tab
        #######################################
        #--> Water Demands
        ffp_matrix = ["PO", "NP", "RW", "SW", "GW"]
        self.module.setParameter("freq_kitchen", float(self.ui.freq_kitchen_box.text()))
        self.module.setParameter("freq_shower", float(self.ui.freq_shower_box.text()))
        self.module.setParameter("freq_toilet", float(self.ui.freq_toilet_box.text()))
        self.module.setParameter("freq_laundry", float(self.ui.freq_laundry_box.text()))
        self.module.setParameter("dur_kitchen", float(self.ui.dur_kitchen_box.text()))
        self.module.setParameter("dur_shower", float(self.ui.dur_shower_box.text()))
        self.module.setParameter("demandvary_kitchen", float(self.ui.demandvary_kitchen_box.value()))
        self.module.setParameter("demandvary_shower", float(self.ui.demandvary_shower_box.value()))
        self.module.setParameter("demandvary_toilet", float(self.ui.demandvary_toilet_box.value()))
        self.module.setParameter("demandvary_laundry", float(self.ui.demandvary_laundry_box.value()))
        self.module.setParameter("priv_irr_vol", float(self.ui.priv_irr_vol_box.text()))

        self.module.setParameter("ffp_kitchen", str(ffp_matrix[self.ui.ffp_kitchen_combo.currentIndex()]))
        self.module.setParameter("ffp_shower", str(ffp_matrix[self.ui.ffp_shower_combo.currentIndex()]))
        self.module.setParameter("ffp_toilet", str(ffp_matrix[self.ui.ffp_toilet_combo.currentIndex()]))
        self.module.setParameter("ffp_laundry", str(ffp_matrix[self.ui.ffp_laundry_combo.currentIndex()]))
        self.module.setParameter("ffp_garden", str(ffp_matrix[self.ui.ffp_garden_combo.currentIndex()]))

        self.module.setParameter("com_demand", float(self.ui.comdemand_box.text()))
        self.module.setParameter("li_demand", float(self.ui.lidemand_box.text()))
        self.module.setParameter("hi_demand", float(self.ui.hidemand_box.text()))
        self.module.setParameter("com_demandvary", float(self.ui.comdemand_spin.value()))
        self.module.setParameter("li_demandvary", float(self.ui.lidemand_spin.value()))
        self.module.setParameter("hi_demandvary", float(self.ui.hidemand_spin.value()))

        demandunits = ['sqm', 'cap']
        self.module.setParameter("com_demandunits", str(demandunits[self.ui.comdemand_units.currentIndex()]))
        self.module.setParameter("li_demandunits", str(demandunits[self.ui.lidemand_units.currentIndex()]))
        self.module.setParameter("hi_demandunits", str(demandunits[self.ui.hidemand_units.currentIndex()]))

        self.module.setParameter("public_irr_vol", float(self.ui.public_irr_volume.text()))
        self.module.setParameter("irrigate_nonres", int(self.ui.public_irr_nonres.isChecked()))
        self.module.setParameter("irrigate_parks", int(self.ui.public_irr_pg.isChecked()))
        self.module.setParameter("irrigate_refs", int(self.ui.public_irr_ref.isChecked()))
        self.module.setParameter("public_irr_wq", str(ffp_matrix[self.ui.public_irr_wq.currentIndex()]))

        #--> Water Efficiency
        if self.ui.WEF_consider.isChecked() == 1:
            WEFstatus = 1
        else:
            WEFstatus = 0
        self.module.setParameter("WEFstatus", WEFstatus)

        ###NOTE: NOT LINKING COMBO BOX WITH RATING SYSTEM, AS6400 the only one for now

        if self.ui.WEF_loc_house_check.isChecked() == 1:
            WEF_loc_house = 1
        else:
            WEF_loc_house = 0
        self.module.setParameter("WEF_loc_house", WEF_loc_house)

        if self.ui.WEF_loc_apart_check.isChecked() == 1:
            WEF_loc_apart = 1
        else:
            WEF_loc_apart = 0
        self.module.setParameter("WEF_loc_apart", WEF_loc_apart)

        if self.ui.WEF_loc_nonres_check.isChecked() == 1:
            WEF_loc_nonres = 1
        else:
            WEF_loc_nonres = 0
        self.module.setParameter("WEF_loc_nonres", WEF_loc_nonres)

        if self.ui.WEF_constant_radio.isChecked() == 1:
            WEF_method = "C"
        elif self.ui.WEF_distribution_radio.isChecked() == 1:
            WEF_method = "D"
        self.module.setParameter("WEF_method", str(WEF_method))

        self.module.setParameter("WEF_c_rating", int(self.ui.WEF_constant_combo.currentIndex()+1))
        self.module.setParameter("WEF_d_rating", int(self.ui.WEF_distribution_combo.currentIndex()+1))
        self.module.setParameter("WEF_distribution", str(self.WEFdist[self.ui.WEF_distribution_select.currentIndex()]))
        self.module.setParameter("WEF_includezero", int(self.ui.WEF_distribution_check.isChecked()))

        #--> Water Recycling Strategy & Additional Options
        self.module.setParameter("rec_demrange_min", float(self.ui.rec_demrange_min.value()))
        self.module.setParameter("rec_demrange_max", float(self.ui.rec_demrange_max.value()))
        self.module.setParameter("ww_kitchen", int(self.ui.rec_ww_kitchen.isChecked()))
        self.module.setParameter("ww_shower", int(self.ui.rec_ww_shower.isChecked()))
        self.module.setParameter("ww_toilet", int(self.ui.rec_ww_toilet.isChecked()))
        self.module.setParameter("ww_laundry", int(self.ui.rec_ww_laundry.isChecked()))

        if self.ui.radio_hsdown.isChecked() == 1:
            hs_strategy = "ud"
        elif self.ui.radio_hsup.isChecked() == 1:
            hs_strategy = "uu"
        elif self.ui.radio_hsall.isChecked() == 1:
            hs_strategy = "ua"
        self.module.setParameter("hs_strategy", str(hs_strategy))

        self.module.setParameter("sb_method", str(self.sbmethod[self.ui.rec_assessment_combo.currentIndex()]))
        self.module.setParameter("rain_length", self.ui.rec_rainfall_spin.value())

        #######################################
        #Choose & Customize Technologies Tab
        #######################################

        #--------- Advanced Stormwater Harvesting Plant -----------------------#
        if self.ui.ASHPstatus_box.isChecked() == 1:
            ASHPstatus = 1
        else:
            ASHPstatus = 0
        self.module.setParameter("ASHPstatus", ASHPstatus)

        #--------- Aquaculture/Living Systems ---------------------------------#
        if self.ui.AQstatus_box.isChecked() == 1:
            AQstatus = 1
        else:
            AQstatus = 0
        self.module.setParameter("AQstatus", AQstatus)

        #--------- Aquifer Storage & Recovery ---------------------------------#
        if self.ui.ASRstatus_box.isChecked() == 1:
            ASRstatus = 1
        else:
            ASRstatus = 0
        self.module.setParameter("ASRstatus", ASRstatus)

        #--------- Biofiltration/Raingardens ----------------------------------#
        if self.ui.BFstatus_box.isChecked() == 1:
            BFstatus = 1
        else:
            BFstatus = 0
        self.module.setParameter("BFstatus", BFstatus)

        #Available Scales
        if self.ui.BFlot_check.isChecked() == 1:
            BFlot = 1
        else:
            BFlot = 0
        self.module.setParameter("BFlot", BFlot)

        if self.ui.BFstreet_check.isChecked() == 1:
            BFstreet = 1
        else:
            BFstreet = 0
        self.module.setParameter("BFstreet", BFstreet)

        if self.ui.BFneigh_check.isChecked() == 1:
            BFneigh = 1
        else:
            BFneigh = 0
        self.module.setParameter("BFneigh", BFneigh)

        if self.ui.BFprec_check.isChecked() == 1:
            BFprec = 1
        else:
            BFprec = 0
        self.module.setParameter("BFprec", BFprec)

        #Available Applications
        if self.ui.BFflow_check.isChecked() == 1:
            BFflow = 1
        else:
            BFflow = 0
        self.module.setParameter("BFflow", BFflow)

        if self.ui.BFpollute_check.isChecked() == 1:
            BFpollute = 1
        else:
            BFpollute = 0
        self.module.setParameter("BFpollute", BFpollute)

        if self.ui.BFrecycle_check.isChecked() == 1:
            BFrecycle = 1
        else:
            BFrecycle = 0
        self.module.setParameter("BFrecycle", BFrecycle)

        #Design Curves
        if self.ui.BFdesignUB_box.isChecked() == 1:
            BFdesignUB = 1
        else:
            BFdesignUB = 0
        self.module.setParameter("BFdesignUB", BFdesignUB)

        BFdescur_path = str(self.ui.BFdesigncurve_pathbox.text())
        self.module.setParameter("BFdescur_path", BFdescur_path)

        #Design Information

        #combo box
        BFspec_matrix = [[0,0.1,0.2,0.3,0.4],[0.2,0.4,0.6,0.8]]
        BFspec_EDDindex = self.ui.BFspecs_EDD_combo.currentIndex()
        BFspec_FDindex = self.ui.BFspecs_FD_combo.currentIndex()
        BFspec_EDD = BFspec_matrix[0][BFspec_EDDindex]
        BFspec_FD = BFspec_matrix[1][BFspec_FDindex]
        self.module.setParameter("BFspec_EDD", BFspec_EDD)
        self.module.setParameter("BFspec_FD", BFspec_FD)

        BFexfil_matrix = [0, 0.18, 0.36, 1.8, 3.6]
        self.module.setParameter("BFexfil", int(BFexfil_matrix[self.ui.BFexfil_combo.currentIndex()]))

        self.module.setParameter("BFminsize", float(self.ui.BFminsize_box.text()))
        self.module.setParameter("BFmaxsize", float(self.ui.BFmaxsize_box.text()))
        self.module.setParameter("BFavglife", self.ui.BFavglifespin.value())

        #further design parameters coming soon...

        #--------- Green Roof -------------------------------------------------#
        if self.ui.GRstatus_box.isChecked() == 1:
            GRstatus = 1
        else:
            GRstatus = 0
        self.module.setParameter("GRstatus", GRstatus)

        #--------- Greywater Tank/Treatment -----------------------------------#
        if self.ui.GTstatus_box.isChecked() == 1:
            GTstatus = 1
        else:
            GTstatus = 0
        self.module.setParameter("GTstatus", GTstatus)

        #--------- Gross Pollutant Trap ---------------------------------------#
        if self.ui.GPTstatus_box.isChecked() == 1:
            GPTstatus = 1
        else:
            GPTstatus = 0
        self.module.setParameter("GPTstatus", GPTstatus)

        #--------- Infiltration System ----------------------------------------#
        if self.ui.ISstatus_box.isChecked() == 1:
            ISstatus = 1
        else:
            ISstatus = 0
        self.module.setParameter("ISstatus", ISstatus)

        #Available Scales
        if self.ui.ISlot_check.isChecked() == 1:
            ISlot = 1
        else:
            ISlot = 0
        self.module.setParameter("ISlot", ISlot)

        if self.ui.ISstreet_check.isChecked() == 1:
            ISstreet = 1
        else:
            ISstreet = 0
        self.module.setParameter("ISstreet", ISstreet)

        if self.ui.ISneigh_check.isChecked() == 1:
            ISneigh = 1
        else:
            ISneigh = 0
        self.module.setParameter("ISneigh", ISneigh)

        #Available Applications
        if self.ui.ISflow_check.isChecked() == 1:
            ISflow = 1
        else:
            ISflow = 0
        self.module.setParameter("ISflow", ISflow)

        if self.ui.ISpollute_check.isChecked() == 1:
            ISpollute = 1
        else:
            ISpollute = 0
        self.module.setParameter("ISpollute", ISpollute)

        #Design Curves
        if self.ui.ISdesignUB_box.isChecked() == 1:
            ISdesignUB = 1
        else:
            ISdesignUB = 0
        self.module.setParameter("ISdesignUB", ISdesignUB)

        ISdescur_path = str(self.ui.ISdesigncurve_pathbox.text())
        self.module.setParameter("ISdescur_path", ISdescur_path)

        #Design Information
        #combo box
        ISspec_matrix = [[0.1,0.2,0.3,0.4,0.5],[0.2,0.4,0.6,0.8]]
        ISspec_EDDindex = self.ui.ISspecs_EDD_combo.currentIndex()
        ISspec_FDindex = self.ui.ISspecs_FD_combo.currentIndex()
        ISspec_EDD = ISspec_matrix[0][ISspec_EDDindex]
        ISspec_FD = ISspec_matrix[1][ISspec_FDindex]
        self.module.setParameter("ISspec_EDD", ISspec_EDD)
        self.module.setParameter("ISspec_FD", ISspec_FD)

        ISexfil_matrix = [1.8, 3.6, 18, 36]
        self.module.setParameter("ISexfil", int(ISexfil_matrix[self.ui.ISexfil_combo.currentIndex()]))

        self.module.setParameter("ISminsize", float(self.ui.ISminsize_box.text()))
        self.module.setParameter("ISmaxsize", float(self.ui.ISmaxsize_box.text()))
        self.module.setParameter("ISavglife", float(self.ui.ISavglifespin.value()))

        #--------- Packaged Plants --------------------------------------------#
        if self.ui.PPLstatus_box.isChecked() == 1:
            PPLstatus = 1
        else:
            PPLstatus = 0
        self.module.setParameter("PPLstatus", PPLstatus)

        #--------- Ponds/Sedimentation Basins ---------------------------------#
        if self.ui.PBstatus_box.isChecked() == 1:
            PBstatus = 1
        else:
            PBstatus = 0
        self.module.setParameter("PBstatus", PBstatus)

        #Available Scales
        if self.ui.PBneigh_check.isChecked() == 1:
            PBneigh = 1
        else:
            PBneigh = 0
        self.module.setParameter("PBneigh", PBneigh)

        if self.ui.PBprec_check.isChecked() == 1:
            PBprec = 1
        else:
            PBprec = 0
        self.module.setParameter("PBprec", PBprec)

        #Available Applications
        if self.ui.PBflow_check.isChecked() == 1:
            PBflow = 1
        else:
            PBflow = 0
        self.module.setParameter("PBflow", PBflow)

        if self.ui.PBpollute_check.isChecked() == 1:
            PBpollute = 1
        else:
            PBpollute = 0
        self.module.setParameter("PBpollute", PBpollute)

        if self.ui.PBrecycle_check.isChecked() == 1:
            PBrecycle = 1
        else:
            PBrecycle = 0
        self.module.setParameter("PBrecycle", PBrecycle)

        #Design Curves
        if self.ui.PBdesignUB_box.isChecked() == 1:
            PBdesignUB = 1
        else:
            PBdesignUB = 0
        self.module.setParameter("PBdesignUB", PBdesignUB)

        PBdescur_path = str(self.ui.PBdesigncurve_pathbox.text())
        self.module.setParameter("PBdescur_path", PBdescur_path)

        #Design Information
        #combo box
        PBspec_matrix = ["0.25", "0.50", "0.75", "1.00", "1.25"]
        PBspec_MDindex = self.ui.PBspecs_combo.currentIndex()
        PBspec_MD = PBspec_matrix[PBspec_MDindex]
        self.module.setParameter("PBspec_MD", PBspec_MD)

        PBexfil_matrix = [0, 0.18, 0.36, 1.8, 3.6]
        self.module.setParameter("PBexfil", str(PBexfil_matrix[self.ui.PBexfil_combo.currentIndex()]))

        self.module.setParameter("PBminsize", str(self.ui.PBminsize_box.text()))
        self.module.setParameter("PBmaxsize", str(self.ui.PBmaxsize_box.text()))
        self.module.setParameter("PBavglife", str(self.ui.PBavglifespin.value()))
        #further design parameters coming soon...

        #---------- Porous/Pervious Pavements ---------------------------------#
        if self.ui.PPstatus_box.isChecked() == 1:
            PPstatus = 1
        else:
            PPstatus = 0
        self.module.setParameter("PPstatus", PPstatus)

        #---------- Rainwater Tank --------------------------------------------#
        if self.ui.RTstatus_box.isChecked() == 1:
            RTstatus = 1
        else:
            RTstatus = 0
        self.module.setParameter("RTstatus", RTstatus)

        RT_maxdepth = float(self.ui.RT_maxdepth_box.text())
        self.module.setParameter("RT_maxdepth", RT_maxdepth)
        RT_mindead = float(self.ui.RT_mindead_box.text())
        self.module.setParameter("RT_mindead", RT_mindead)

        if self.ui.RTscale_lot_box.isChecked() == 1:
            RTscale_lot = 1
        else:
            RTscale_lot = 0
        self.module.setParameter("RTlot", RTscale_lot)

        if self.ui.RTscale_neighb_box.isChecked() == 1:
            RTscale_neigh = 1
        else:
            RTscale_neigh = 0
        self.module.setParameter("RTneigh", RTscale_neigh)

        if self.ui.RTpurp_flood_box.isChecked() == 1:
            RTpurp_flood = 1
        else:
            RTpurp_flood = 0
        self.module.setParameter("RTflow", RTpurp_flood)

        if self.ui.RTpurp_recyc_box.isChecked() == 1:
            RTpurp_recyc = 1
        else:
            RTpurp_recyc = 0
        self.module.setParameter("RTrecycle", RTpurp_recyc)

        if self.ui.RTdesignUB_box.isChecked() == 1:
            RTdesignUB = 1
        else:
            RTdesignUB = 0
        self.module.setParameter("RTdesignUB", RTdesignUB)

        RTdescur_path = str(self.ui.RTdesigncurve_pathbox.text())
        self.module.setParameter("RTdescur_path", RTdescur_path)

        #---------- Sand/Peat/Gravel Filter -----------------------------------#
        if self.ui.SFstatus_box.isChecked() == 1:
            SFstatus = 1
        else:
            SFstatus = 0
        self.module.setParameter("SFstatus", SFstatus)

        #---------- Subsurface Irrigation System ------------------------------#
        if self.ui.IRRstatus_box.isChecked() == 1:
            IRRstatus = 1
        else:
            IRRstatus = 0
        self.module.setParameter("IRRstatus", IRRstatus)

        #---------- Subsurface Wetland/Reed Bed -------------------------------#
        if self.ui.WSUBstatus_box.isChecked() == 1:
            WSUBstatus = 1
        else:
            WSUBstatus = 0
        self.module.setParameter("WSUBstatus", WSUBstatus)

        #---------- Surface Wetland -------------------------------------------#
        if self.ui.WSURstatus_box.isChecked() == 1:
            WSURstatus = 1
        else:
            WSURstatus = 0
        self.module.setParameter("WSURstatus", WSURstatus)

        #Available Scales
        if self.ui.WSURneigh_check.isChecked() == 1:
            WSURneigh = 1
        else:
            WSURneigh = 0
        self.module.setParameter("WSURneigh", WSURneigh)

        if self.ui.WSURprec_check.isChecked() == 1:
            WSURprec = 1
        else:
            WSURprec = 0
        self.module.setParameter("WSURprec", WSURprec)

        #Available Applications
        if self.ui.WSURflow_check.isChecked() == 1:
            WSURflow = 1
        else:
            WSURflow = 0
        self.module.setParameter("WSURflow", WSURflow)

        if self.ui.WSURpollute_check.isChecked() == 1:
            WSURpollute = 1
        else:
            WSURpollute = 0
        self.module.setParameter("WSURpollute", WSURpollute)

        if self.ui.WSURrecycle_check.isChecked() == 1:
            WSURrecycle = 1
        else:
            WSURrecycle = 0
        self.module.setParameter("WSURrecycle", WSURrecycle)

        #Design Curves
        if self.ui.WSURdesignUB_box.isChecked() == 1:
            WSURdesignUB = 1
        else:
            WSURdesignUB = 0
        self.module.setParameter("WSURdesignUB", WSURdesignUB)

        WSURdescur_path = str(self.ui.WSURdesigncurve_pathbox.text())
        self.module.setParameter("WSURdescur_path", WSURdescur_path)

        #Design Information
        #combo box
        WSURspec_matrix = ["0.25", "0.50", "0.75", "0.25", "0.50", "0.75"]
        WSURspec_EDDindex = self.ui.WSURspecs_combo.currentIndex()
        WSURspec_EDD = WSURspec_matrix[WSURspec_EDDindex]
        self.module.setParameter("WSURspec_EDD", WSURspec_EDD)

        WSURexfil_matrix = [0, 0.18, 0.36, 1.8, 3.6]
        self.module.setParameter("WSURexfil", WSURexfil_matrix[self.ui.WSURexfil_combo.currentIndex()])

        self.module.setParameter("WSURminsize", float(self.ui.WSURminsize_box.text()))
        self.module.setParameter("WSURmaxsize", float(self.ui.WSURmaxsize_box.text()))
        self.module.setParameter("WSURavglife", float(self.ui.WSURavglifespin.value()))
        #further design parameters coming soon...

        #---------- Swales/Buffer Strips --------------------------------------#
        if self.ui.SWstatus_box.isChecked() == 1:
            SWstatus = 1
        else:
            SWstatus = 0
        self.module.setParameter("SWstatus", SWstatus)

        #Available Scales
        if self.ui.SWstreet_check.isChecked() == 1:
            SWstreet = 1
        else:
            SWstreet = 0
        self.module.setParameter("SWstreet", SWstreet)

        if self.ui.SWneigh_check.isChecked() == 1:
            SWneigh = 1
        else:
            SWneigh = 0
        self.module.setParameter("SWneigh", SWneigh)

        #Available Applications
        if self.ui.SWflow_check.isChecked() == 1:
            SWflow = 1
        else:
            SWflow = 0
        self.module.setParameter("SWflow", SWflow)

        if self.ui.SWpollute_check.isChecked() == 1:
            SWpollute = 1
        else:
            SWpollute = 0
        self.module.setParameter("SWpollute", SWpollute)

        #Design Curves
        if self.ui.SWdesignUB_box.isChecked() == 1:
            SWdesignUB = 1
        else:
            SWdesignUB = 0
        self.module.setParameter("SWdesignUB", SWdesignUB)

        SWdescur_path = str(self.ui.SWdesigncurve_pathbox.text())
        self.module.setParameter("SWdescur_path", SWdescur_path)

        #Design Information
        #combo box

        SWexfil_matrix = [0, 0.18, 0.36, 1.8, 3.6]
        self.module.setParameter("SWexfil", SWexfil_matrix[self.ui.SWexfil_combo.currentIndex()])

        self.module.setParameter("SWminsize", float(self.ui.SWminsize_box.text()))
        self.module.setParameter("SWmaxsize", float(self.ui.SWmaxsize_box.text()))
        self.module.setParameter("SWavglife", float(self.ui.SWavglifespin.value()))
        #further design parameters coming soon...

        #--------- Tree Pits --------------------------------------------------#
        if self.ui.TPSstatus_box.isChecked() == 1:
            TPSstatus = 1
        else:
            TPSstatus = 0
        self.module.setParameter("TPSstatus", TPSstatus)

        #---------- Urine-separating Toilets ----------------------------------#
        if self.ui.UTstatus_box.isChecked() == 1:
            UTstatus = 1
        else:
            UTstatus = 0
        self.module.setParameter("UTstatus", UTstatus)

        #---------- Wastwater Recovery/Recycling Plant ------------------------#
        if self.ui.WWRRstatus_box.isChecked() == 1:
            WWRRstatus = 1
        else:
            WWRRstatus = 0
        self.module.setParameter("WWRRstatus", WWRRstatus)

        #---------- Waterless/Composting Toilets ------------------------------#
        if self.ui.WTstatus_box.isChecked() == 1:
            WTstatus = 1
        else:
            WTstatus = 0
        self.module.setParameter("WTstatus", WTstatus)

        #--- ## --- REGIONAL INFORMATION---------------------------------------#
        regioncity_matrix = ["Adelaide", "Brisbane", "Melbourne", "Perth", "Sydney"]

        regioncity_index = self.ui.regioncity_combo.currentIndex()
        regioncity = regioncity_matrix[regioncity_index]
        self.module.setParameter("regioncity", regioncity)


        ################################
        #Select Evaluation Criteria Tab
        ################################

        #-------- Evaluation Metrics Select------------------------------------#
        if self.ui.mca_scoringmat_check.isChecked() == 1:
            scoringmatrix_default = 1
        else:
            scoringmatrix_default = 0
        self.module.setParameter("scoringmatrix_default", scoringmatrix_default)

        scoringmatrix_path = str(self.ui.mca_scoringmat_box.text())
        self.module.setParameter("scoringmatrix_path", scoringmatrix_path)

        #-------- Customize Evaluation Criteria--------------------------------#
        if self.ui.bottomlines_tech_check.isChecked() == 1:
            bottomlines_tech = 1
        else:
            bottomlines_tech = 0
        self.module.setParameter("bottomlines_tech", bottomlines_tech)

        if self.ui.bottomlines_env_check.isChecked() == 1:
            bottomlines_env = 1
        else:
            bottomlines_env = 0
        self.module.setParameter("bottomlines_env", bottomlines_env)

        if self.ui.bottomlines_ecn_check.isChecked() == 1:
            bottomlines_ecn = 1
        else:
            bottomlines_ecn = 0
        self.module.setParameter("bottomlines_ecn", bottomlines_ecn)

        if self.ui.bottomlines_soc_check.isChecked() == 1:
            bottomlines_soc = 1
        else:
            bottomlines_soc = 0
        self.module.setParameter("bottomlines_soc", bottomlines_soc)

        bottomlines_tech_n = self.ui.bottomlines_techN_spin.value()
        self.module.setParameter("bottomlines_tech_n", bottomlines_tech_n)

        bottomlines_env_n = self.ui.bottomlines_envN_spin.value()
        self.module.setParameter("bottomlines_env_n", bottomlines_env_n)

        bottomlines_ecn_n = self.ui.bottomlines_ecnN_spin.value()
        self.module.setParameter("bottomlines_ecn_n", bottomlines_ecn_n)

        bottomlines_soc_n = self.ui.bottomlines_socN_spin.value()
        self.module.setParameter("bottomlines_soc_n", bottomlines_soc_n)

        bottomlines_tech_w = self.ui.bottomlines_techW_spin.value()
        self.module.setParameter("bottomlines_tech_w", bottomlines_tech_w)

        bottomlines_env_w = self.ui.bottomlines_envW_spin.value()
        self.module.setParameter("bottomlines_env_w", bottomlines_env_w)

        bottomlines_ecn_w = self.ui.bottomlines_ecnW_spin.value()
        self.module.setParameter("bottomlines_ecn_w", bottomlines_ecn_w)

        bottomlines_soc_w = self.ui.bottomlines_socW_spin.value()
        self.module.setParameter("bottomlines_soc_w", bottomlines_soc_w)

        #-------- EVALUATION SCOPE & METHOD -----------------------------------#
        score_method_matrix = ["WPM", "WSM"]
        score_index = self.ui.eval_method_combo.currentIndex()
        score_method = score_method_matrix[score_index]
        self.module.setParameter("score_method", score_method)

        if self.ui.scope_stoch_check.isChecked() == 1:
            scope_stoch = 1
        else:
            scope_stoch = 0
        self.module.setParameter("scope_stoch", scope_stoch)

        if self.ui.radioScoreAvg.isChecked() == True:
            ingroup_scoring = "Avg"
        if self.ui.radioScoreMed.isChecked() == True:
            ingroup_scoring = "Med"
        if self.ui.radioScoreMin.isChecked() == True:
            ingroup_scoring = "Min"
        if self.ui.radioScoreMax.isChecked() == True:
            ingroup_scoring = "Max"
        self.module.setParameter("ingroup_scoring", ingroup_scoring)

        #-------- RANKING OF STRATEGIES ---------------------------------------#
        rank_method_matrix = ["RK", "CI"]
        rank_index = self.ui.top_score_combo.currentIndex()
        ranktype = rank_method_matrix[rank_index]
        self.module.setParameter("ranktype", ranktype)

        topranklimit = self.ui.top_rank_spin.value()
        self.module.setParameter("topranklimit", topranklimit)

        conf_int = self.ui.top_CI_spin.value()
        self.module.setParameter("conf_int", conf_int)