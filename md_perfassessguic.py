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

from md_perfassessgui import Ui_Perfconfig_Dialog
from PyQt4 import QtGui, QtCore

class PerfAssessGUILaunch(QtGui.QDialog):
    def __init__(self, activesim, tabindex, parent = None):
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_Perfconfig_Dialog()
        self.ui.setupUi(self)
        self.module = activesim.getModulePerfAssess(tabindex)

        #Set all default parameters contained in the module file into the GUI's fields

        #----------------------------------------------------------------------#
        #-------- SELECT ANALYSES ---------------------------------------------#
        #----------------------------------------------------------------------#

        # self.ui.blocksize_in.setValue(int(self.module.getParameter("BlockSize")))
        #
        # if self.module.getParameter("blocksize_auto") == 1:
        #     self.ui.blocksize_auto.setChecked(1)
        #     self.ui.blocksize_in.setEnabled(0)
        # else:
        #     self.ui.blocksize_auto.setChecked(0)
        #     self.ui.blocksize_in.setEnabled(1)
        #
        # QtCore.QObject.connect(self.ui.blocksize_auto, QtCore.SIGNAL("clicked()"), self.block_auto_size)

        #----------------------------------------------------------------------#
        #-------- MUSIC -------------------------------------------------------#
        #----------------------------------------------------------------------#

        pass


        #----------------------------------------------------------------------#
        #-------- ECONOMICS ---------------------------------------------------#
        #----------------------------------------------------------------------#




        #----------------------------------------------------------------------#
        #-------- MICROCLIMATE ------------------------------------------------#
        #----------------------------------------------------------------------#




        #----------------------------------------------------------------------#
        #-------- EPANET ------------------------------------------------------#
        #----------------------------------------------------------------------#



        #----------------------------------------------------------------------#
        #-------- INTEGRATED WATER CYCLE MODEL  -------------------------------#
        #----------------------------------------------------------------------#




    def ed_MUSIC(self):
        return True


    def ed_Economics(self):
        return True


    def ed_Microclimate(self):
        return True


    def ed_EPANET(self):
        return True


    def ed_CD3(self):
        return True


    #Save values function
    def save_values(self):
        #----------------------------------------------------------------------#
        #-------- SELECT ANALYSES ---------------------------------------------#
        #----------------------------------------------------------------------#
        # self.module.setParameter("BlockSize", self.ui.blocksize_in.value())
        # self.module.setParameter("blocksize_auto", int(int(self.ui.blocksize_auto.isChecked())))

         #----------------------------------------------------------------------#
        #-------- MUSIC -------------------------------------------------------#
        #----------------------------------------------------------------------#




        #----------------------------------------------------------------------#
        #-------- ECONOMICS ---------------------------------------------------#
        #----------------------------------------------------------------------#




        #----------------------------------------------------------------------#
        #-------- MICROCLIMATE ------------------------------------------------#
        #----------------------------------------------------------------------#




        #----------------------------------------------------------------------#
        #-------- EPANET ------------------------------------------------------#
        #----------------------------------------------------------------------#



        #----------------------------------------------------------------------#
        #-------- INTEGRATED WATER CYCLE MODEL  -------------------------------#
        #----------------------------------------------------------------------#



        pass
        # self.emit(QtCore.SIGNAL("updatedDetails"))
