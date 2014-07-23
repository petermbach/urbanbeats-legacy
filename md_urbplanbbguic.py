# -*- coding: utf-8 -*-
"""
@file
@author  Peter M Bach <peterbach@gmail.com>
@version 1.0
@section LICENSE

This file is part of UrbanBEATS (www.urbanbeatsmodel.com), DynaMind
Copyright (C) 2011, 2012  Peter M Bach

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
from PyQt4 import QtCore, QtGui
#from pydynamind import *
from md_urbplanbbgui import Ui_BuildingBlockDialog

class UrbplanbbGUILaunch(QtGui.QDialog):
    def __init__(self, activesim, tabindex, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_BuildingBlockDialog()
        self.ui.setupUi(self)
        self.module = activesim.getModuleUrbplanbb(tabindex)
        #Assign Default Values & Connect Signal/Slots
    
        ##########################
        #General Rules Tab
        ##########################
        #--> General City Structure
        if self.module.getParameter("cityarchetype") == "MC":
            self.ui.citymono_radio.setChecked(1)
        elif self.module.getParameter("cityarchetype") == "PC":
            self.ui.citypoly_radio.setChecked(1)
    
        self.ui.citysprawl_spin.setValue(float(self.module.getParameter("citysprawl")))
        self.ui.mun_localmap_check.setChecked(bool(self.module.getParameter("locality_mun_trans")))
    
        #--> Decision Variables for Block Dynamics
        if self.module.getParameter("lucredev") == 1:
            self.ui.lucredevelop_check.setChecked(1)
            self.ui.lucredevelop_spin.setEnabled(1)
        else:
            self.ui.lucredevelop_check.setChecked(0)
            self.ui.lucredevelop_spin.setEnabled(0)
    
        if self.module.getParameter("popredev") == 1:
            self.ui.popredevelop_check.setChecked(1)
            self.ui.popredevelop_spin.setEnabled(1)
        else:
            self.ui.popredevelop_check.setChecked(0)
            self.ui.popredevelop_spin.setEnabled(0)
    
        if self.module.getParameter("noredev") == 1:
            self.ui.noredevelop_check.setChecked(1)
            self.ui.lucredevelop_check.setEnabled(0)
            self.ui.lucredevelop_spin.setEnabled(0)
            self.ui.popredevelop_check.setEnabled(0)
            self.ui.popredevelop_spin.setEnabled(0)
        else:
            self.ui.noredevelop_check.setChecked(0)
            self.ui.lucredevelop_check.setEnabled(1)
            if self.ui.lucredevelop_check.isChecked() == 1:
                self.ui.lucredevelop_spin.setEnabled(1)
            else:
                self.ui.lucredevelop_spin.setEnabled(0)
    
            self.ui.popredevelop_check.setEnabled(1)
            if self.ui.popredevelop_check.isChecked() == 1:
                self.ui.popredevelop_spin.setEnabled(1)
            else:
                self.ui.popredevelop_spin.setEnabled(0)
    
        self.ui.lucredevelop_spin.setValue(int(self.module.getParameter("lucredev_thresh")))
        self.ui.popredevelop_spin.setValue(int(self.module.getParameter("popredev_thresh")))
    
        QtCore.QObject.connect(self.ui.lucredevelop_check, QtCore.SIGNAL("clicked()"), self.enableReDevThresh)
        QtCore.QObject.connect(self.ui.popredevelop_check, QtCore.SIGNAL("clicked()"), self.enableReDevThresh)
        QtCore.QObject.connect(self.ui.noredevelop_check, QtCore.SIGNAL("clicked()"), self.enableReDevThresh)
    
        ##########################
        #Residential Tab
        ##########################
        self.ui.occup_avg_box.setText(str(self.module.getParameter("occup_avg")))
        self.ui.occup_max_box.setText(str(self.module.getParameter("occup_max")))
        self.ui.person_space_box.setText(str(self.module.getParameter("person_space")))
        self.ui.extra_comm_area_box.setText(str(self.module.getParameter("extra_comm_area")))
        self.ui.setback_f_min_box.setText(str(self.module.getParameter("setback_f_min")))
        self.ui.setback_f_max_box.setText(str(self.module.getParameter("setback_f_max")))
        self.ui.setback_s_min_box.setText(str(self.module.getParameter("setback_s_min")))
        self.ui.setback_s_max_box.setText(str(self.module.getParameter("setback_s_max")))
        self.ui.fsetbackmed_check.setChecked(bool(int(self.module.getParameter("setback_f_med"))))
        self.ui.ssetbackmed_check.setChecked(bool(int(self.module.getParameter("setback_s_med"))))
        self.ui.carports_max_box.setText(str(self.module.getParameter("carports_max")))
        self.ui.garage_incl_box.setChecked(bool(int(self.module.getParameter("garage_incl"))))
        self.ui.w_driveway_min_box.setText(str(self.module.getParameter("w_driveway_min")))
        self.ui.patio_area_max_box.setText(str(self.module.getParameter("patio_area_max")))
        self.ui.patio_covered_box.setChecked(bool(int(self.module.getParameter("patio_covered"))))
        self.ui.house_floors.setValue(int(self.module.getParameter("floor_num_max")))
        self.ui.occup_flat_avg_box.setText(str(self.module.getParameter("occup_flat_avg")))
        self.ui.indoor_com_spin.setValue(int(self.module.getParameter("commspace_indoor")))
        self.ui.flat_area_max_box.setText(str(self.module.getParameter("flat_area_max")))
        self.ui.outdoor_com_spin.setValue(int(self.module.getParameter("commspace_outdoor")))
        self.ui.setback_HDR_avg_box.setText(str(self.module.getParameter("setback_HDR_avg")))
        self.ui.aptbldg_floors.setValue(int(self.module.getParameter("floor_num_HDRmax")))

        if self.module.getParameter("parking_HDR") == "On":
            self.ui.parking_on.setChecked(1)
        elif self.module.getParameter("parking_HDR") == "Off":
            self.ui.parking_off.setChecked(1)
        elif self.module.getParameter("parking_HDR") == "Var":
            self.ui.parking_vary.setChecked(1)
        elif self.module.getParameter("parking_HDR") == "NA":
            self.ui.parking_none.setChecked(1)

        self.ui.OSR_parks_include.setChecked(bool(int(self.module.getParameter("park_OSR"))))

        if self.module.getParameter("roof_connected") == "Direct":
            self.ui.roof_connected_radiodirect.setChecked(1)
        elif self.module.getParameter("roof_connected") == "Disconnect":
            self.ui.roof_connected_radiodisc.setChecked(1)
        elif self.module.getParameter("roof_connected") == "Vary":
            self.ui.roof_connected_radiovary.setChecked(1)

        self.checkRoofDced()
        QtCore.QObject.connect(self.ui.roof_connected_radiodirect, QtCore.SIGNAL("clicked()"), self.checkRoofDced)
        QtCore.QObject.connect(self.ui.roof_connected_radiodisc, QtCore.SIGNAL("clicked()"), self.checkRoofDced)
        QtCore.QObject.connect(self.ui.roof_connected_radiovary, QtCore.SIGNAL("clicked()"), self.checkRoofDced)

        self.ui.roofdced_vary_spin.setValue(int(self.module.getParameter("roof_dced_p")))
        self.ui.avg_imp_dced_spin.setValue(int(self.module.getParameter("imperv_prop_dced")))

        ##########################
        #Non-Residential Tab
        ##########################
        #--> Employment Details
        if self.module.getParameter("employment_mode") == "I":
            self.ui.jobs_direct_radio.setChecked(1)
            self.ui.jobs_define_stack.setCurrentIndex(0)
        elif self.module.getParameter("employment_mode") == "D":
            self.ui.jobs_dist_radio.setChecked(1)
            self.ui.jobs_define_stack.setCurrentIndex(1)
        elif self.module.getParameter("employment_mode") == "S":
            self.ui.jobs_total_radio.setChecked(1)
            self.ui.jobs_define_stack.setCurrentIndex(2)

        self.ui.dist_ind_spin.setValue(int(self.module.getParameter("ind_edist")))
        self.ui.dist_com_spin.setValue(int(self.module.getParameter("com_edist")))
        self.ui.dist_orc_spin.setValue(int(self.module.getParameter("orc_edist")))
        self.ui.totjobs_box.setText(str(self.module.getParameter("employment_total")))

        QtCore.QObject.connect(self.ui.jobs_direct_radio, QtCore.SIGNAL("clicked()"), self.employment_pagechange)
        QtCore.QObject.connect(self.ui.jobs_dist_radio, QtCore.SIGNAL("clicked()"), self.employment_pagechange)
        QtCore.QObject.connect(self.ui.jobs_total_radio, QtCore.SIGNAL("clicked()"), self.employment_pagechange)

        #-->Land Subdivision & Site Layout
        self.ui.ind_subd_min.setText(str(self.module.getParameter("ind_subd_min")))
        self.ui.ind_subd_max.setText(str(self.module.getParameter("ind_subd_max")))
        self.ui.com_subd_min.setText(str(self.module.getParameter("com_subd_min")))
        self.ui.com_subd_max.setText(str(self.module.getParameter("com_subd_max")))

        self.ui.nres_setback_box.setText(str(self.module.getParameter("nres_minfsetback")))
        self.ui.nres_setback_auto.setChecked(bool(int(self.module.getParameter("nres_setback_auto"))))
        self.ui.nres_maxfloors_spin.setValue(int(self.module.getParameter("nres_maxfloors")))

        if self.module.getParameter("nres_setback_auto") == 1:
            self.ui.nres_setback_auto.setChecked(1)
            self.ui.nres_setback_box.setEnabled(0)
        else:
            self.ui.nres_setback_auto.setChecked(0)
            self.ui.nres_setback_box.setEnabled(1)

        QtCore.QObject.connect(self.ui.nres_setback_auto, QtCore.SIGNAL("clicked()"), self.nres_minfsetback_check)

        if self.module.getParameter("nres_nolimit_floors") == 1:
            self.ui.nres_maxfloors_nolimit.setChecked(1)
            self.ui.nres_maxfloors_spin.setEnabled(0)
        else:
            self.ui.nres_maxfloors_nolimit.setChecked(0)
            self.ui.nres_maxfloors_spin.setEnabled(1)

        QtCore.QObject.connect(self.ui.nres_maxfloors_nolimit, QtCore.SIGNAL("clicked()"), self.nres_floors_check)

        self.ui.plotratio_ind_box.setText(str(float(self.module.getParameter("maxplotratio_ind"))/100))
        self.ui.plotratio_ind_slider.setValue(int(self.module.getParameter("maxplotratio_ind")))
        QtCore.QObject.connect(self.ui.plotratio_ind_slider, QtCore.SIGNAL("valueChanged(int)"), self.plotratio_ind_update)

        self.ui.plotratio_com_box.setText(str(float(self.module.getParameter("maxplotratio_com"))/100))
        self.ui.plotratio_com_slider.setValue(int(self.module.getParameter("maxplotratio_com")))
        QtCore.QObject.connect(self.ui.plotratio_com_slider, QtCore.SIGNAL("valueChanged(int)"), self.plotratio_com_update)

        #--> Car Parking and Loading Bay
        self.ui.carpark_dimW_box.setText(str(self.module.getParameter("carpark_Wmin")))
        self.ui.carpark_dimD_box.setText(str(self.module.getParameter("carpark_Dmin")))
        self.ui.carpark_imp_spin.setValue(int(self.module.getParameter("carpark_imp")))
        self.ui.carpark_ind_box.setText(str(self.module.getParameter("carpark_ind")))
        self.ui.carpark_com_box.setText(str(self.module.getParameter("carpark_com")))
        self.ui.loadingbay_box.setText(str(self.module.getParameter("loadingbay_A")))

        #--> Landscaping & Drainage
        self.ui.lscape_hsbalance_slide.setValue(int(self.module.getParameter("lscape_hsbalance")))
        self.ui.lscape_impdced_spin.setValue(int(self.module.getParameter("lscape_impdced")))

        #--> Municipal Facilities
        if self.module.getParameter("mun_explicit") == 1:
            self.ui.civ_consider_check.setChecked(1)
            self.ui.edu_school_box.setEnabled(1)
            self.ui.edu_uni_box.setEnabled(1)
            self.ui.edu_lib_box.setEnabled(1)
            self.ui.civ_hospital_box.setEnabled(1)
            self.ui.civ_clinic_box.setEnabled(1)
            self.ui.civ_police_box.setEnabled(1)
            self.ui.civ_fire_box.setEnabled(1)
            self.ui.civ_jail_box.setEnabled(1)
            self.ui.civ_religion_box.setEnabled(1)
            self.ui.civ_leisure_box.setEnabled(1)
            self.ui.civ_museum_box.setEnabled(1)
            self.ui.civ_zoo_box.setEnabled(1)
            self.ui.civ_sports_box.setEnabled(1)
            self.ui.civ_race_box.setEnabled(1)
            self.ui.civ_dead_box.setEnabled(1)
        else:
            self.ui.civ_consider_check.setChecked(0)
            self.ui.edu_school_box.setEnabled(0)
            self.ui.edu_uni_box.setEnabled(0)
            self.ui.edu_lib_box.setEnabled(0)
            self.ui.civ_hospital_box.setEnabled(0)
            self.ui.civ_clinic_box.setEnabled(0)
            self.ui.civ_police_box.setEnabled(0)
            self.ui.civ_fire_box.setEnabled(0)
            self.ui.civ_jail_box.setEnabled(0)
            self.ui.civ_religion_box.setEnabled(0)
            self.ui.civ_leisure_box.setEnabled(0)
            self.ui.civ_museum_box.setEnabled(0)
            self.ui.civ_zoo_box.setEnabled(0)
            self.ui.civ_sports_box.setEnabled(0)
            self.ui.civ_race_box.setEnabled(0)
            self.ui.civ_dead_box.setEnabled(0)
        QtCore.QObject.connect(self.ui.civ_consider_check, QtCore.SIGNAL("clicked()"), self.mun_on_off_enable)

        self.ui.edu_school_box.setChecked(bool(int(self.module.getParameter("edu_school"))))
        self.ui.edu_uni_box.setChecked(bool(int(self.module.getParameter("edu_uni"))))
        self.ui.edu_lib_box.setChecked(bool(int(self.module.getParameter("edu_lib"))))
        self.ui.civ_hospital_box.setChecked(bool(int(self.module.getParameter("civ_hospital"))))
        self.ui.civ_clinic_box.setChecked(bool(int(self.module.getParameter("civ_clinic"))))
        self.ui.civ_police_box.setChecked(bool(int(self.module.getParameter("civ_police"))))
        self.ui.civ_fire_box.setChecked(bool(int(self.module.getParameter("civ_fire"))))
        self.ui.civ_jail_box.setChecked(bool(int(self.module.getParameter("civ_jail"))))
        self.ui.civ_religion_box.setChecked(bool(int(self.module.getParameter("civ_worship"))))
        self.ui.civ_leisure_box.setChecked(bool(int(self.module.getParameter("civ_leisure"))))
        self.ui.civ_museum_box.setChecked(bool(int(self.module.getParameter("civ_museum"))))
        self.ui.civ_zoo_box.setChecked(bool(int(self.module.getParameter("civ_zoo"))))
        self.ui.civ_sports_box.setChecked(bool(int(self.module.getParameter("civ_stadium"))))
        self.ui.civ_race_box.setChecked(bool(int(self.module.getParameter("civ_racing"))))
        self.ui.civ_dead_box.setChecked(bool(int(self.module.getParameter("civ_cemetery"))))

        ##########################
        #Transport Tab
        ##########################
        #--> Frontage & Pedestrian Information
        self.ui.w_resfootpath_min_box.setText(str(self.module.getParameter("res_fpwmin")))
        self.ui.w_resfootpath_max_box.setText(str(self.module.getParameter("res_fpwmax")))
        self.ui.w_resnaturestrip_min_box.setText(str(self.module.getParameter("res_nswmin")))
        self.ui.w_resnaturestrip_max_box.setText(str(self.module.getParameter("res_nswmax")))
        self.ui.w_resfootpath_med_check.setChecked(bool(int(self.module.getParameter("res_fpmed"))))
        self.ui.w_resnaturestrip_med_check.setChecked(bool(int(self.module.getParameter("res_nsmed"))))

        self.ui.w_comfootpath_min_box.setText(str(self.module.getParameter("nres_fpwmin")))
        self.ui.w_comfootpath_max_box.setText(str(self.module.getParameter("nres_fpwmax")))
        self.ui.w_comnaturestrip_min_box.setText(str(self.module.getParameter("nres_nswmin")))
        self.ui.w_comnaturestrip_max_box.setText(str(self.module.getParameter("nres_nswmax")))
        self.ui.w_comfootpath_med_check.setChecked(bool(int(self.module.getParameter("nres_fpmed"))))
        self.ui.w_comnaturestrip_med_check.setChecked(bool(int(self.module.getParameter("nres_nsmed"))))

        self.ui.w_collectlane_min_box.setText(str(self.module.getParameter("lane_wmin")))
        self.ui.w_collectlane_max_box.setText(str(self.module.getParameter("lane_wmax")))
        self.ui.collect_crossfall_box.setText(str(self.module.getParameter("lane_crossfall")))
        self.ui.w_collectlane_med_check.setChecked(bool(int(self.module.getParameter("lane_wmed"))))

        self.ui.w_arterial_min_box.setText(str(self.module.getParameter("hwy_wlanemin")))
        self.ui.w_arterial_max_box.setText(str(self.module.getParameter("hwy_wlanemax")))
        self.ui.w_arterialmed_minbox.setText(str(self.module.getParameter("hwy_wmedianmin")))
        self.ui.w_arterialmed_maxbox.setText(str(self.module.getParameter("hwy_wmedianmax")))
        self.ui.w_arterialsh_minbox.setText(str(self.module.getParameter("hwy_wbufmin")))
        self.ui.w_arterialsh_maxbox.setText(str(self.module.getParameter("hwy_wbufmax")))
        self.ui.w_arterial_med_check.setChecked(bool(int(self.module.getParameter("hwy_lanemed"))))
        self.ui.w_arterialmed_med_check.setChecked(bool(int(self.module.getParameter("hwy_medmed"))))
        self.ui.w_arterialsh_med_check.setChecked(bool(int(self.module.getParameter("hwy_bufmed"))))
        self.ui.arterial_crossfall_box.setText(str(self.module.getParameter("hwy_crossfall")))
        self.ui.w_arterialmed_nodev_check.setChecked(bool(int(self.module.getParameter("hwy_restrict"))))
        self.ui.highway_buffer_check.setChecked(bool(int(self.module.getParameter("hwy_buffer"))))

        #--> Other Transport
        if self.module.getParameter("considerTRFacilities") == 1:
            self.ui.trans_on_off_check.setChecked(1)
            self.ui.trans_airport_box.setEnabled(1)
            self.ui.trans_seaport_box.setEnabled(1)
            self.ui.trans_busdepot_box.setEnabled(1)
            self.ui.trans_rail_box.setEnabled(1)
        else:
            self.ui.trans_on_off_check.setChecked(0)
            self.ui.trans_airport_box.setEnabled(0)
            self.ui.trans_seaport_box.setEnabled(0)
            self.ui.trans_busdepot_box.setEnabled(0)
            self.ui.trans_rail_box.setEnabled(0)
        QtCore.QObject.connect(self.ui.trans_on_off_check, QtCore.SIGNAL("clicked()"), self.trans_on_off_enable)

        self.ui.trans_airport_box.setChecked(bool(int(self.module.getParameter("trans_airport"))))
        self.ui.trans_seaport_box.setChecked(bool(int(self.module.getParameter("trans_seaport"))))
        self.ui.trans_busdepot_box.setChecked(bool(int(self.module.getParameter("trans_busdepot"))))
        self.ui.trans_rail_box.setChecked(bool(int(self.module.getParameter("trans_railterminal"))))

        ##########################
        #Open Space Tab
        ##########################
        #--> Parks, Squares and Gardens
        self.ui.pg_ggratio_slide.setValue(int(self.module.getParameter("pg_greengrey_ratio")))
        self.ui.pg_ggratio_box.setText(str(self.module.getParameter("pg_greengrey_ratio")))
        QtCore.QObject.connect(self.ui.pg_ggratio_slide, QtCore.SIGNAL("valueChanged(int)"), self.ggratio_update)
        #CONNECT GREYGREEN SLIDER TO TEXTBOX

        if self.module.getParameter("pgsq_distribution") == "C":
            self.ui.pg_dist_mix_radio.setChecked(1)
        elif self.module.getParameter("pgsq_distribution") == "S":
            self.ui.pg_dist_sep_radio.setChecked(1)

        self.ui.pg_usable_spin.setValue(int(self.module.getParameter("pg_unused_space")))
        self.ui.pg_usable_prohibit.setChecked(bool(int(self.module.getParameter("pg_restrict"))))

        #--> Reserves & Floodways
        if self.module.getParameter("ref_usable") == 1:
            self.ui.ref_usable_check.setChecked(1)
            self.ui.ref_usable_spin.setEnabled(1)
        else:
            self.ui.ref_usable_check.setChecked(0)
            self.ui.ref_usable_spin.setEnabled(0)

        self.ui.ref_usable_spin.setValue(int(self.module.getParameter("ref_usable_percent")))

        QtCore.QObject.connect(self.ui.ref_usable_check, QtCore.SIGNAL("clicked()"), self.ref_usable_update)

        self.ui.ref_limit_check.setChecked(bool(int(self.module.getParameter("ref_limit_stormwater"))))

        #--> Services & Utilities
        svu_water = int(self.module.getParameter("svu_water"))
        svu_nonwater = 100 - svu_water
        self.ui.svu_wat_box.setText(str(svu_water))
        self.ui.svu_nonwat_box.setText(str(svu_nonwater))

        self.ui.svu_slider.setValue(int(svu_water))
        QtCore.QObject.connect(self.ui.svu_slider, QtCore.SIGNAL("valueChanged(int)"), self.svu_slider_update)

        if self.module.getParameter("svu4supply") == 1:
            self.ui.svu_supply_check.setChecked(1)
            self.ui.svu_supply_spin.setEnabled(1)
        else:
            self.ui.svu_supply_check.setChecked(0)
            self.ui.svu_supply_spin.setEnabled(0)

        if self.module.getParameter("svu4waste") == 1:
            self.ui.svu_waste_check.setChecked(1)
            self.ui.svu_waste_spin.setEnabled(1)
        else:
            self.ui.svu_waste_check.setChecked(0)
            self.ui.svu_waste_spin.setEnabled(0)

        if self.module.getParameter("svu4storm") == 1:
            self.ui.svu_storm_check.setChecked(1)
            self.ui.svu_storm_spin.setEnabled(1)
        else:
            self.ui.svu_storm_check.setChecked(0)
            self.ui.svu_storm_spin.setEnabled(0)

        self.ui.svu_supply_spin.setValue(int(self.module.getParameter("svu4supply_prop")))
        self.ui.svu_waste_spin.setValue(int(self.module.getParameter("svu4waste_prop")))
        self.ui.svu_storm_spin.setValue(int(self.module.getParameter("svu4storm_prop")))

        QtCore.QObject.connect(self.ui.svu_supply_check, QtCore.SIGNAL("clicked()"), self.svu_supply_update)
        QtCore.QObject.connect(self.ui.svu_waste_check, QtCore.SIGNAL("clicked()"), self.svu_waste_update)
        QtCore.QObject.connect(self.ui.svu_storm_check, QtCore.SIGNAL("clicked()"), self.svu_storm_update)

        ##########################
        #Others Tab
        ##########################
        #--> Unclassified Land
        if self.module.getParameter("unc_merge") == 1:
            self.ui.unc_merge_check.setChecked(1)
            self.ui.unc_merge2ref_check.setEnabled(1)
            self.ui.unc_merge2pg_check.setEnabled(1)
            self.ui.unc_merge2trans_check.setEnabled(1)
            self.ui.unc_merge2ref_spin.setEnabled(1)
            self.ui.unc_merge2pg_spin.setEnabled(1)
            self.ui.unc_merge2trans_spin.setEnabled(1)
        else:
            self.ui.unc_merge_check.setChecked(0)
            self.ui.unc_merge2ref_check.setEnabled(0)
            self.ui.unc_merge2pg_check.setEnabled(0)
            self.ui.unc_merge2trans_check.setEnabled(0)
            self.ui.unc_merge2ref_spin.setEnabled(0)
            self.ui.unc_merge2pg_spin.setEnabled(0)
            self.ui.unc_merge2trans_spin.setEnabled(0)
        QtCore.QObject.connect(self.ui.unc_merge_check, QtCore.SIGNAL("clicked()"), self.unc_merge_enable)

        if self.module.getParameter("unc_pgmerge") == 1:
            self.ui.unc_merge2pg_check.setChecked(1)
        else:
            self.ui.unc_merge2pg_check.setChecked(0)
            self.ui.unc_merge2pg_spin.setEnabled(0)
        QtCore.QObject.connect(self.ui.unc_merge2pg_check, QtCore.SIGNAL("clicked()"), self.unc_merge2pg_enable)

        if self.module.getParameter("unc_refmerge") == 1:
            self.ui.unc_merge2ref_check.setChecked(1)
        else:
            self.ui.unc_merge2ref_check.setChecked(0)
            self.ui.unc_merge2ref_spin.setEnabled(0)
        QtCore.QObject.connect(self.ui.unc_merge2ref_check, QtCore.SIGNAL("clicked()"), self.unc_merge2ref_enable)

        if self.module.getParameter("unc_rdmerge") == 1:
            self.ui.unc_merge2trans_check.setChecked(1)
        else:
            self.ui.unc_merge2trans_check.setChecked(0)
            self.ui.unc_merge2trans_spin.setEnabled(0)
        QtCore.QObject.connect(self.ui.unc_merge2trans_check, QtCore.SIGNAL("clicked()"), self.unc_merge2trans_enable)

        self.ui.unc_merge2ref_spin.setValue(float(self.module.getParameter("unc_refmerge_w")))
        self.ui.unc_merge2pg_spin.setValue(float(self.module.getParameter("unc_pgmerge_w")))
        self.ui.unc_merge2trans_spin.setValue(float(self.module.getParameter("unc_rdmerge_w")))

        if self.module.getParameter("unc_custom") == 1:
            self.ui.unc_custom_check.setChecked(1)
            self.ui.unc_areathresh_spin.setEnabled(1)
            self.ui.unc_customimp_spin.setEnabled(1)
            self.ui.unc_customirrigate_check.setEnabled(1)
        else:
            self.ui.unc_custom_check.setChecked(0)
            self.ui.unc_areathresh_spin.setEnabled(0)
            self.ui.unc_customimp_spin.setEnabled(0)
            self.ui.unc_customirrigate_check.setEnabled(0)
        QtCore.QObject.connect(self.ui.unc_custom_check, QtCore.SIGNAL("clicked()"), self.unc_custom_check_enable)

        self.ui.unc_areathresh_spin.setValue(float(self.module.getParameter("unc_customthresh")))
        self.ui.unc_customimp_spin.setValue(float(self.module.getParameter("unc_customimp")))

        if self.module.getParameter("unc_landirrigate") == 1:
            self.ui.unc_customirrigate_check.setChecked(1)
        else:
            self.ui.unc_customirrigate_check.setChecked(0)

        #--> Undeveloped
        if self.module.getParameter("und_state") == "M":
            self.ui.und_statemanual_radio.setChecked(1)
            self.ui.und_statemanual_combo.setEnabled(1)
        elif self.module.getParameter("und_state") == "A":
            self.ui.und_stateauto_radio.setChecked(1)
            self.ui.und_statemanual_combo.setEnabled(0)

        self.undev_matrix = ["GF", "BF", "AG"]
        undev_type = self.module.getParameter("und_type_manual")
        undevindex = self.undev_matrix.index(undev_type)
        self.ui.und_statemanual_combo.setCurrentIndex(int(undevindex))

        QtCore.QObject.connect(self.ui.und_statemanual_radio, QtCore.SIGNAL("clicked()"), self.und_typeEnable)
        QtCore.QObject.connect(self.ui.und_stateauto_radio, QtCore.SIGNAL("clicked()"), self.und_typeEnable)

        self.ui.und_allowdev_check.setChecked(bool(int(self.module.getParameter("und_allowdev"))))

        #CONNECT DETAILS WITH THE OK BUTTON SO THAT GUI UPDATES MODULE
        QtCore.QObject.connect(self.ui.buttonBox, QtCore.SIGNAL("accepted()"), self.save_values)


    ###############################
    #   Update functions          #
    ###############################

    #--> GENERAL TAB
    def enableReDevThresh(self):
        if self.ui.lucredevelop_check.isChecked() == 1:
            self.ui.lucredevelop_spin.setEnabled(1)
        else:
            self.ui.lucredevelop_spin.setEnabled(0)

        if self.ui.popredevelop_check.isChecked() == 1:
            self.ui.popredevelop_spin.setEnabled(1)
        else:
            self.ui.popredevelop_spin.setEnabled(0)

        if self.ui.noredevelop_check.isChecked() == 1:
            self.ui.lucredevelop_check.setEnabled(0)
            self.ui.lucredevelop_spin.setEnabled(0)
            self.ui.popredevelop_check.setEnabled(0)
            self.ui.popredevelop_spin.setEnabled(0)
        else:
            self.ui.lucredevelop_check.setEnabled(1)
            if self.ui.lucredevelop_check.isChecked() == 1:
                self.ui.lucredevelop_spin.setEnabled(1)
            else:
                self.ui.lucredevelop_spin.setEnabled(0)

            self.ui.popredevelop_check.setEnabled(1)
            if self.ui.popredevelop_check.isChecked() == 1:
                self.ui.popredevelop_spin.setEnabled(1)
            else:
                self.ui.popredevelop_spin.setEnabled(0)

    #--> RESIDENTIAL TAB
    def checkRoofDced(self):
        if self.ui.roof_connected_radiodirect.isChecked() or self.ui.roof_connected_radiodisc.isChecked():
            self.ui.roofdced_vary_spin.setEnabled(0)
        else:
            self.ui.roofdced_vary_spin.setEnabled(1)

    #--> NON-RESIDENTIAL TAB
    def employment_pagechange(self):
        if self.ui.jobs_direct_radio.isChecked() == 1:
            self.ui.jobs_define_stack.setCurrentIndex(0)
        elif self.ui.jobs_dist_radio.isChecked() == 1:
            self.ui.jobs_define_stack.setCurrentIndex(1)
        elif self.ui.jobs_total_radio.isChecked() == 1:
            self.ui.jobs_define_stack.setCurrentIndex(2)

    def nres_minfsetback_check(self):
        if self.ui.nres_setback_auto.isChecked() == 1:
            self.ui.nres_setback_box.setEnabled(0)
        else:
            self.ui.nres_setback_box.setEnabled(1)

    def nres_floors_check(self):
        if self.ui.nres_maxfloors_nolimit.isChecked() == 1:
            self.ui.nres_maxfloors_spin.setEnabled(0)
        else:
            self.ui.nres_maxfloors_spin.setEnabled(1)

    def plotratio_ind_update(self, currentValue):
        self.ui.plotratio_ind_box.setText(str(float(currentValue)/100))

    def plotratio_com_update(self, currentValue):
        self.ui.plotratio_com_box.setText(str(float(currentValue)/100))

    def mun_on_off_enable(self):
        if self.ui.civ_consider_check.isChecked() == 1:
            self.ui.edu_school_box.setEnabled(1)
            self.ui.edu_uni_box.setEnabled(1)
            self.ui.edu_lib_box.setEnabled(1)
            self.ui.civ_hospital_box.setEnabled(1)
            self.ui.civ_clinic_box.setEnabled(1)
            self.ui.civ_police_box.setEnabled(1)
            self.ui.civ_fire_box.setEnabled(1)
            self.ui.civ_jail_box.setEnabled(1)
            self.ui.civ_religion_box.setEnabled(1)
            self.ui.civ_leisure_box.setEnabled(1)
            self.ui.civ_museum_box.setEnabled(1)
            self.ui.civ_zoo_box.setEnabled(1)
            self.ui.civ_sports_box.setEnabled(1)
            self.ui.civ_race_box.setEnabled(1)
            self.ui.civ_dead_box.setEnabled(1)
        else:
            self.ui.edu_school_box.setEnabled(0)
            self.ui.edu_uni_box.setEnabled(0)
            self.ui.edu_lib_box.setEnabled(0)
            self.ui.civ_hospital_box.setEnabled(0)
            self.ui.civ_clinic_box.setEnabled(0)
            self.ui.civ_police_box.setEnabled(0)
            self.ui.civ_fire_box.setEnabled(0)
            self.ui.civ_jail_box.setEnabled(0)
            self.ui.civ_religion_box.setEnabled(0)
            self.ui.civ_leisure_box.setEnabled(0)
            self.ui.civ_museum_box.setEnabled(0)
            self.ui.civ_zoo_box.setEnabled(0)
            self.ui.civ_sports_box.setEnabled(0)
            self.ui.civ_race_box.setEnabled(0)
            self.ui.civ_dead_box.setEnabled(0)

    #--> TRANSPORT TAB
    def trans_on_off_enable(self):
        if self.ui.trans_on_off_check.isChecked() == 1:
            self.ui.trans_airport_box.setEnabled(1)
            self.ui.trans_seaport_box.setEnabled(1)
            self.ui.trans_busdepot_box.setEnabled(1)
            self.ui.trans_rail_box.setEnabled(1)
        else:
            self.ui.trans_airport_box.setEnabled(0)
            self.ui.trans_seaport_box.setEnabled(0)
            self.ui.trans_busdepot_box.setEnabled(0)
            self.ui.trans_rail_box.setEnabled(0)

    #--> OPEN SPACE TAB
    def ggratio_update(self, currentValue):
        self.ui.pg_ggratio_box.setText(str(currentValue))

    def ref_usable_update(self):
        if self.ui.ref_usable_check.isChecked() == 1:
            self.ui.ref_usable_spin.setEnabled(1)
        else:
            self.ui.ref_usable_spin.setEnabled(0)

    def svu_slider_update(self, currentValue):
        self.ui.svu_wat_box.setText(str(currentValue))
        self.ui.svu_nonwat_box.setText(str(100-currentValue))

    def svu_supply_update(self):
        if self.ui.svu_supply_check.isChecked() == 1:
            self.ui.svu_supply_spin.setEnabled(1)
        else:
            self.ui.svu_supply_spin.setEnabled(0)

    def svu_waste_update(self):
        if self.ui.svu_waste_check.isChecked() == 1:
            self.ui.svu_waste_spin.setEnabled(1)
        else:
            self.ui.svu_waste_spin.setEnabled(0)

    def svu_storm_update(self):
        if self.ui.svu_storm_check.isChecked() == 1:
            self.ui.svu_storm_spin.setEnabled(1)
        else:
            self.ui.svu_storm_spin.setEnabled(0)

    #--> OTHERS TAB
    def unc_merge_enable(self):
        if self.ui.unc_merge_check.isChecked() == 1:
            self.ui.unc_merge2ref_check.setEnabled(1)
            self.ui.unc_merge2pg_check.setEnabled(1)
            self.ui.unc_merge2trans_check.setEnabled(1)
            self.unc_merge2ref_enable()
            self.unc_merge2pg_enable()
            self.unc_merge2trans_enable()
        else:
            self.ui.unc_merge2ref_check.setEnabled(0)
            self.ui.unc_merge2pg_check.setEnabled(0)
            self.ui.unc_merge2trans_check.setEnabled(0)
            self.ui.unc_merge2ref_spin.setEnabled(0)
            self.ui.unc_merge2pg_spin.setEnabled(0)
            self.ui.unc_merge2trans_spin.setEnabled(0)

    def unc_merge2ref_enable(self):
        if self.ui.unc_merge2ref_check.isChecked() == 1:
            self.ui.unc_merge2ref_spin.setEnabled(1)
        else:
            self.ui.unc_merge2ref_spin.setEnabled(0)

    def unc_merge2pg_enable(self):
        if self.ui.unc_merge2pg_check.isChecked() == 1:
            self.ui.unc_merge2pg_spin.setEnabled(1)
        else:
            self.ui.unc_merge2pg_spin.setEnabled(0)

    def unc_merge2trans_enable(self):
        if self.ui.unc_merge2trans_check.isChecked() == 1:
            self.ui.unc_merge2trans_spin.setEnabled(1)
        else:
            self.ui.unc_merge2trans_spin.setEnabled(0)

    def unc_custom_check_enable(self):
        if self.ui.unc_custom_check.isChecked() == 1:
            self.ui.unc_areathresh_spin.setEnabled(1)
            self.ui.unc_customimp_spin.setEnabled(1)
            self.ui.unc_customirrigate_check.setEnabled(1)
        else:
            self.ui.unc_areathresh_spin.setEnabled(0)
            self.ui.unc_customimp_spin.setEnabled(0)
            self.ui.unc_customirrigate_check.setEnabled(0)

    def und_typeEnable(self):
        if self.ui.und_statemanual_radio.isChecked() == 1:
            self.ui.und_statemanual_combo.setEnabled(1)
        else:
            self.ui.und_statemanual_combo.setEnabled(0)

    #################################
    # OK Button/Cancel Button Click #
    #################################

    def save_values(self):
        ffp_matrix = ["PO", "NP", "RW", "SW", "GW"]
        ##########################
        #General Rules Tab
        ##########################
        #-->General City Structure
        if self.ui.citymono_radio.isChecked() == 1:
            self.module.setParameter("cityarchetype", "MC")
        elif self.ui.citypoly_radio.isChecked() == 1:
            self.module.setParameter("cityarchetype", "PC")

        self.module.setParameter("citysprawl", float(self.ui.citysprawl_spin.value()))
        self.module.setParameter("locality_mun_trans", int(self.ui.mun_localmap_check.isChecked()))
        #building block dynamics parameters
        self.module.setParameter("lucredev", int(self.ui.lucredevelop_check.isChecked()))
        self.module.setParameter("popredev", int(self.ui.popredevelop_check.isChecked()))
        self.module.setParameter("lucredev_thresh", float(self.ui.lucredevelop_spin.value()))
        self.module.setParameter("popredev_thresh", float(self.ui.popredevelop_spin.value()))
        self.module.setParameter("noredev", int(self.ui.noredevelop_check.isChecked()))

        ##########################
        #Residential Tab
        ##########################
        self.module.setParameter("occup_avg", float(self.ui.occup_avg_box.text()))
        self.module.setParameter("occup_max", float(self.ui.occup_max_box.text()))
        self.module.setParameter("person_space", float(self.ui.person_space_box.text()))
        self.module.setParameter("extra_comm_area", float(self.ui.extra_comm_area_box.text()))
        self.module.setParameter("setback_f_min", float(self.ui.setback_f_min_box.text()))
        self.module.setParameter("setback_f_max", float(self.ui.setback_f_max_box.text()))
        self.module.setParameter("setback_s_min", float(self.ui.setback_s_min_box.text()))
        self.module.setParameter("setback_s_max", float(self.ui.setback_s_max_box.text()))
        self.module.setParameter("setback_f_med", int(self.ui.fsetbackmed_check.isChecked()))
        self.module.setParameter("setback_s_med", int(self.ui.ssetbackmed_check.isChecked()))
        self.module.setParameter("carports_max", float(self.ui.carports_max_box.text()))
        self.module.setParameter("garage_incl", int(self.ui.garage_incl_box.isChecked()))
        self.module.setParameter("w_driveway_min", float(self.ui.w_driveway_min_box.text()))
        self.module.setParameter("patio_area_max", float(self.ui.patio_area_max_box.text()))
        self.module.setParameter("patio_covered", int(self.ui.patio_covered_box.isChecked()))
        self.module.setParameter("floor_num_max", float(self.ui.house_floors.value()))
        self.module.setParameter("occup_flat_avg", float(self.ui.occup_flat_avg_box.text()))
        self.module.setParameter("commspace_indoor", float(self.ui.indoor_com_spin.value()))
        self.module.setParameter("flat_area_max", float(self.ui.flat_area_max_box.text()))
        self.module.setParameter("commspace_outdoor", float(self.ui.outdoor_com_spin.value()))
        self.module.setParameter("setback_HDR_avg", float(self.ui.setback_HDR_avg_box.text()))
        self.module.setParameter("floor_num_HDRmax", float(self.ui.aptbldg_floors.value()))

        if self.ui.parking_on.isChecked() == 1:
            self.module.setParameter("parking_HDR", "On")
        elif self.ui.parking_off.isChecked() == 1:
            self.module.setParameter("parking_HDR", "Off")
        elif self.ui.parking_vary.isChecked() == 1:
            self.module.setParameter("parking_HDR", "Var")
        elif self.ui.parking_none.isChecked() == 1:
            self.module.setParameter("parking_HDR", "NA")

        self.module.setParameter("park_OSR", int(self.ui.OSR_parks_include.isChecked()))

        if self.ui.roof_connected_radiodirect.isChecked() == True:
            self.module.setParameter("roof_connected", "Direct")
        if self.ui.roof_connected_radiodisc.isChecked() == True:
            self.module.setParameter("roof_connected", "Disconnect")
        if self.ui.roof_connected_radiovary.isChecked() == True:
            self.module.setParameter("roof_connected", "Vary")

        self.module.setParameter("roof_dced_p", int(self.ui.roofdced_vary_spin.value()))
        self.module.setParameter("imperv_prop_dced", int(self.ui.avg_imp_dced_spin.value()))

        ##########################
        #Non-Residential Tab
        ##########################
        #--> Employment Details
        if self.ui.jobs_direct_radio.isChecked() == True:
            self.module.setParameter("employment_mode", "I")
        if self.ui.jobs_dist_radio.isChecked() == True:
            self.module.setParameter("employment_mode", "D")
        if self.ui.jobs_total_radio.isChecked() == True:
            self.module.setParameter("employment_mode", "S")

        self.module.setParameter("ind_edist", float(self.ui.dist_ind_spin.value()))
        self.module.setParameter("com_edist", float(self.ui.dist_com_spin.value()))
        self.module.setParameter("orc_edist", float(self.ui.dist_orc_spin.value()))
        self.module.setParameter("employment_total", float(self.ui.totjobs_box.text()))

        #--> Land Subdivision & Site Layout
        self.module.setParameter("ind_subd_min", float(self.ui.ind_subd_min.text()))
        self.module.setParameter("ind_subd_max", float(self.ui.ind_subd_max.text()))
        self.module.setParameter("com_subd_min", float(self.ui.com_subd_min.text()))
        self.module.setParameter("com_subd_max", float(self.ui.com_subd_max.text()))

        self.module.setParameter("nres_minfsetback", float(self.ui.nres_setback_box.text()))
        self.module.setParameter("nres_maxfloors", float(self.ui.nres_maxfloors_spin.value()))
        self.module.setParameter("nres_setback_auto", int(self.ui.nres_setback_auto.isChecked()))
        self.module.setParameter("nres_nolimit_floors", int(self.ui.nres_maxfloors_nolimit.isChecked()))

        self.module.setParameter("maxplotratio_ind", float(self.ui.plotratio_ind_slider.value()))
        self.module.setParameter("maxplotratio_com", float(self.ui.plotratio_com_slider.value()))

        #--> Car Parking and Loading Bay
        self.module.setParameter("carpark_Wmin", float(self.ui.carpark_dimW_box.text()))
        self.module.setParameter("carpark_Dmin", float(self.ui.carpark_dimD_box.text()))
        self.module.setParameter("carpark_imp", float(self.ui.carpark_imp_spin.value()))
        self.module.setParameter("carpark_ind", float(self.ui.carpark_ind_box.text()))
        self.module.setParameter("carpark_com", float(self.ui.carpark_com_box.text()))
        self.module.setParameter("loadingbay_A", float(self.ui.loadingbay_box.text()))

        #--> Landscaping & Drainage
        lscape_hsbalance = self.ui.lscape_hsbalance_slide.value()
        self.module.setParameter("lscape_hsbalance", float(lscape_hsbalance))

        lscape_impdced = self.ui.lscape_impdced_spin.value()
        self.module.setParameter("lscape_impdced", float(lscape_impdced))

        #--> Municipal Facilities
        self.module.setParameter("mun_explicit", int(self.ui.civ_consider_check.isChecked()))
        self.module.setParameter("edu_school", int(self.ui.edu_school_box.isChecked()))
        self.module.setParameter("edu_uni", int(self.ui.edu_uni_box.isChecked()))
        self.module.setParameter("edu_lib", int(self.ui.edu_lib_box.isChecked()))
        self.module.setParameter("civ_hospital", int(self.ui.civ_hospital_box.isChecked()))
        self.module.setParameter("civ_clinic", int(self.ui.civ_clinic_box.isChecked()))
        self.module.setParameter("civ_police", int(self.ui.civ_police_box.isChecked()))
        self.module.setParameter("civ_fire", int(self.ui.civ_fire_box.isChecked()))
        self.module.setParameter("civ_jail", int(self.ui.civ_jail_box.isChecked()))
        self.module.setParameter("civ_worship", int(self.ui.civ_religion_box.isChecked()))
        self.module.setParameter("civ_leisure", int(self.ui.civ_leisure_box.isChecked()))
        self.module.setParameter("civ_museum", int(self.ui.civ_museum_box.isChecked()))
        self.module.setParameter("civ_zoo", int(self.ui.civ_zoo_box.isChecked()))
        self.module.setParameter("civ_stadium", int(self.ui.civ_sports_box.isChecked()))
        self.module.setParameter("civ_racing", int(self.ui.civ_race_box.isChecked()))
        self.module.setParameter("civ_cemetery", int(self.ui.civ_dead_box.isChecked()))

        ##########################
        #Transport Tab
        ##########################
        #--> Frontage & Pedestrian Information
        self.module.setParameter("res_fpwmin", float(self.ui.w_resfootpath_min_box.text()))
        self.module.setParameter("res_fpwmax", float(self.ui.w_resfootpath_max_box.text()))
        self.module.setParameter("res_fpmed", int(self.ui.w_resfootpath_med_check.isChecked()))
        self.module.setParameter("res_nswmin", float(self.ui.w_resnaturestrip_min_box.text()))
        self.module.setParameter("res_nswmax", float(self.ui.w_resnaturestrip_max_box.text()))
        self.module.setParameter("res_nsmed", int(self.ui.w_resnaturestrip_med_check.isChecked()))

        self.module.setParameter("nres_fpwmin", float(self.ui.w_comfootpath_min_box.text()))
        self.module.setParameter("nres_fpwmax", float(self.ui.w_comfootpath_max_box.text()))
        self.module.setParameter("nres_fpmed", int(self.ui.w_comfootpath_med_check.isChecked()))
        self.module.setParameter("nres_nswmin", float(self.ui.w_comnaturestrip_min_box.text()))
        self.module.setParameter("nres_nswmax", float(self.ui.w_comnaturestrip_max_box.text()))
        self.module.setParameter("nres_nsmed", int(self.ui.w_comnaturestrip_med_check.isChecked()))

        self.module.setParameter("lane_wmin", float(self.ui.w_collectlane_min_box.text()))
        self.module.setParameter("lane_wmax", float(self.ui.w_collectlane_max_box.text()))
        self.module.setParameter("lane_wmed", int(self.ui.w_collectlane_med_check.isChecked()))
        self.module.setParameter("lane_crossfall", float(self.ui.collect_crossfall_box.text()))

        self.module.setParameter("hwy_wlanemin", float(self.ui.w_arterial_min_box.text()))
        self.module.setParameter("hwy_wlanemax", float(self.ui.w_arterial_max_box.text()))
        self.module.setParameter("hwy_lanemed", int(self.ui.w_arterial_med_check.isChecked()))
        self.module.setParameter("hwy_wmedianmin", float(self.ui.w_arterialmed_minbox.text()))
        self.module.setParameter("hwy_wmedianmax", float(self.ui.w_arterialmed_maxbox.text()))
        self.module.setParameter("hwy_medmed", int(self.ui.w_arterialmed_med_check.isChecked()))
        self.module.setParameter("hwy_wbufmin", float(self.ui.w_arterialsh_minbox.text()))
        self.module.setParameter("hwy_wbufmax", float(self.ui.w_arterialsh_maxbox.text()))
        self.module.setParameter("hwy_bufmed", int(self.ui.w_arterialsh_med_check.isChecked()))
        self.module.setParameter("hwy_crossfall", float(self.ui.arterial_crossfall_box.text()))
        self.module.setParameter("hwy_restrict", int(self.ui.w_arterialmed_nodev_check.isChecked()))
        self.module.setParameter("hwy_buffer", int(self.ui.highway_buffer_check.isChecked()))

        #--> Other Transportation
        self.module.setParameter("considerTRFacilities", int(self.ui.trans_on_off_check.isChecked()))
        self.module.setParameter("trans_airport", int(self.ui.trans_airport_box.isChecked()))
        self.module.setParameter("trans_seaport", int(self.ui.trans_seaport_box.isChecked()))
        self.module.setParameter("trans_busdepot", int(self.ui.trans_busdepot_box.isChecked()))
        self.module.setParameter("trans_railterminal", int(self.ui.trans_rail_box.isChecked()))

        ##########################
        #Open Space Tab
        ##########################
        #--> Parks, Squares & Gardens
        self.module.setParameter("pg_greengrey_ratio", self.ui.pg_ggratio_slide.value())
        if self.ui.pg_dist_mix_radio.isChecked() == 1:
            self.module.setParameter("pgsq_distribution", "C")
        if self.ui.pg_dist_sep_radio.isChecked() == 1:
            self.module.setParameter("pgsq_distribution", "S")

        self.module.setParameter("pg_unused_space", float(self.ui.pg_usable_spin.value()))
        self.module.setParameter("pg_restrict", int(self.ui.pg_usable_prohibit.isChecked()))

        #--> Reserves & Floodways
        self.module.setParameter("ref_usable", int(self.ui.ref_usable_check.isChecked()))
        self.module.setParameter("ref_usable_percent", float(self.ui.ref_usable_spin.value()))
        self.module.setParameter("ref_limit_stormwater", int(self.ui.ref_limit_check.isChecked()))

        #--> Services & Utilities
        self.module.setParameter("svu_water", str(self.ui.svu_wat_box.text()))
        self.module.setParameter("svu4supply", int(self.ui.svu_supply_check.isChecked()))
        self.module.setParameter("svu4waste", int(self.ui.svu_waste_check.isChecked()))
        self.module.setParameter("svu4storm", int(self.ui.svu_storm_check.isChecked()))
        self.module.setParameter("svu4supply_prop", float(self.ui.svu_supply_spin.value()))
        self.module.setParameter("svu4waste_prop", float(self.ui.svu_waste_spin.value()))
        self.module.setParameter("svu4storm_prop", float(self.ui.svu_storm_spin.value()))

        ##########################
        #Others Tab
        ##########################
        #--> Unclassified
        self.module.setParameter("unc_merge", int(self.ui.unc_merge_check.isChecked()))
        self.module.setParameter("unc_refmerge", int(self.ui.unc_merge2ref_check.isChecked()))
        self.module.setParameter("unc_pgmerge", int(self.ui.unc_merge2pg_check.isChecked()))
        self.module.setParameter("unc_rdmerge", int(self.ui.unc_merge2trans_check.isChecked()))
        self.module.setParameter("unc_pgmerge_w", float(self.ui.unc_merge2pg_spin.value()))
        self.module.setParameter("unc_refmerge_w", float(self.ui.unc_merge2ref_spin.value()))
        self.module.setParameter("unc_rdmerge_w", float(self.ui.unc_merge2trans_spin.value()))
        self.module.setParameter("unc_custom", int(self.ui.unc_custom_check.isChecked()))
        self.module.setParameter("unc_customthresh", float(self.ui.unc_areathresh_spin.value()))
        self.module.setParameter("unc_customimp", float(self.ui.unc_customimp_spin.value()))
        self.module.setParameter("unc_landirrigate", int(self.ui.unc_customirrigate_check.isChecked()))

        #--> Undeveloped
        if self.ui.und_statemanual_radio.isChecked() == True:
            und_state = "M"
        if self.ui.und_stateauto_radio.isChecked() == True:
            und_state = "A"
        self.module.setParameter("und_state", und_state)

        undev_type = self.undev_matrix[self.ui.und_statemanual_combo.currentIndex()]
        self.module.setParameter("und_type_manual", undev_type)

        self.module.setParameter("und_allowdev", int(self.ui.und_allowdev_check.isChecked()))

        #----------------END OF SAVE VALUES------------------------------------#