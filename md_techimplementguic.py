# -*- coding: utf-8 -*-
"""
@file
@author  Peter M Bach <peterbach@gmail.com>
@version 0.5
@section LICENSE

This file is part of VIBe2
Copyright (C) 2011  Peter M Bach

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
from md_techimplementgui import Ui_TechImplement_Dialog

class TechimplementGUILaunch(QtGui.QDialog):
    def __init__(self, activesim, tabindex, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_TechImplement_Dialog()
        self.ui.setupUi(self)
        self.module = activesim.getModuleTechimplement(tabindex)
        #Set all default parameters contained in the module file into the GUI's fields

        #RULES AT DIFFERENT SCALES
        if self.module.getParameter("dynamic_rule") == "B":
            self.ui.implementdynamics_combo.setCurrentIndex(0)
        elif self.module.getParameter("dynamic_rule") == "P":
            self.ui.implementdynamics_combo.setCurrentIndex(1)

        self.ui.block_dev_threshold.setValue(float(self.module.getParameter("block_based_thresh")))

        if self.module.getParameter("bb_lot_rule") == "AMAP":
            self.ui.lot_amap_radio.setChecked(1)
        elif self.module.getParameter("bb_lot_rule") == "STRICT":
            self.ui.lot_strict_radio.setChecked(1)

        self.ui.street_forceimplement_check.setChecked(bool(int(self.module.getParameter("bb_street_zone"))))
        self.ui.neigh_forceimplement_check.setChecked(bool(int(self.module.getParameter("bb_neigh_zone"))))

        if self.module.getParameter("pb_lot_rule") == "G":
            self.ui.parcel_rule_lot.setCurrentIndex(0)
        elif self.module.getParameter("pb_lot_rule") == "I":
            self.ui.parcel_rule_lot.setCurrentIndex(1)
        elif self.module.getParameter("pb_lot_rule") == "D":
            self.ui.parcel_rule_lot.setCurrentIndex(2)

        if self.module.getParameter("pb_street_rule") == "G":
            self.ui.parcel_rule_street.setCurrentIndex(0)
        elif self.module.getParameter("pb_street_rule") == "I":
            self.ui.parcel_rule_street.setCurrentIndex(1)
        elif self.module.getParameter("pb_street_rule") == "D":
            self.ui.parcel_rule_street.setCurrentIndex(2)

        if self.module.getParameter("pb_neigh_rule") == "G":
            self.ui.parcel_rule_neigh.setCurrentIndex(0)
        elif self.module.getParameter("pb_neigh_rule") == "I":
            self.ui.parcel_rule_neigh.setCurrentIndex(1)
        elif self.module.getParameter("pb_neigh_rule") == "D":
            self.ui.parcel_rule_neigh.setCurrentIndex(2)

        self.ui.parcel_rule_neigh_check.setChecked(bool(int(self.module.getParameter("pb_neigh_zone_ignore"))))

        if self.module.getParameter("prec_rule") == "G":
            self.ui.prec_impl_rule.setCurrentIndex(0)
        elif self.module.getParameter("prec_rule") == "I":
            self.ui.prec_impl_rule.setCurrentIndex(1)
        elif self.module.getParameter("prec_rule") == "D":
            self.ui.prec_impl_rule.setCurrentIndex(2)

        self.ui.prec_impl_force_check.setChecked(bool(int(self.module.getParameter("prec_zone_ignore"))))

        if self.module.getParameter("prec_dev_threshold") == 1:
            self.ui.prec_impl_thresh_check.setChecked(1)
            self.ui.prec_impl_thresh_spin.setEnabled(1)
        else:
            self.ui.prec_impl_thresh_check.setChecked(0)
            self.ui.prec_impl_thresh_spin.setEnabled(0)

        self.ui.prec_impl_thresh_spin.setValue(float(self.module.getParameter("prec_dev_percent")))

        #DRIVERS
        self.ui.peoplepref_check.setChecked(self.module.getParameter("driver_people"))
        self.ui.legal_check.setChecked(self.module.getParameter("driver_legal"))
        self.ui.establish_check.setChecked(self.module.getParameter("driver_establish"))

        QtCore.QObject.connect(self.ui.prec_impl_thresh_check, QtCore.SIGNAL("clicked()"), self.prec_threshold_enable)
        QtCore.QObject.connect(self.ui.buttonBox, QtCore.SIGNAL("accepted()"), self.save_values)

    def prec_threshold_enable(self):
        if self.ui.prec_impl_thresh_check.isChecked() == 1:
            self.ui.prec_impl_thresh_spin.setEnabled(1)
        else:
            self.ui.prec_impl_thresh_spin.setEnabled(0)

    def save_values(self):
        #RULES AT ALL SCALES
        dynamic_rule_matrix = ["B", "P"]
        self.module.setParameter("dynamic_rule", dynamic_rule_matrix[self.ui.implementdynamics_combo.currentIndex()])
        self.module.setParameter("block_based_thresh", float(self.ui.block_dev_threshold.value()))

        if self.ui.lot_amap_radio.isChecked() == 1:
            bb_lot_rule = "AMAP"
        elif self.ui.lot_strict_radio.isChecked() == 1:
            bb_lot_rule = "STRICT"
        self.module.setParameter("bb_lot_rule", str(bb_lot_rule))

        self.module.setParameter("bb_street_zone", int(self.ui.street_forceimplement_check.isChecked()))
        self.module.setParameter("bb_neigh_zone", int(self.ui.neigh_forceimplement_check.isChecked()))

        rules_matrix = ["G", "I", "D"]
        self.module.setParameter("pb_lot_rule", rules_matrix[self.ui.parcel_rule_lot.currentIndex()])
        self.module.setParameter("pb_street_rule", rules_matrix[self.ui.parcel_rule_street.currentIndex()])
        self.module.setParameter("pb_neigh_rule", rules_matrix[self.ui.parcel_rule_neigh.currentIndex()])
        self.module.setParameter("prec_rule", rules_matrix[self.ui.prec_impl_rule.currentIndex()])

        self.module.setParameter("pb_neigh_zone_ignore", int(self.ui.parcel_rule_neigh_check.isChecked()))
        self.module.setParameter("prec_zone_ignore", int(self.ui.prec_impl_force_check.isChecked()))
        self.module.setParameter("prec_dev_threshold", int(self.ui.prec_impl_thresh_check.isChecked()))

        self.module.setParameter("prec_dev_percent", float(self.ui.prec_impl_thresh_spin.value()))

        #DRIVERS
        self.module.setParameter("driver_people", int(self.ui.peoplepref_check.isChecked()))
        self.module.setParameter("driver_legal", int(self.ui.legal_check.isChecked()))
        self.module.setParameter("driver_establish", int(self.ui.establish_check.isChecked()))


        
        
    
