# -*- coding: utf-8 -*-
"""
@file
@author  Peter M Bach <peterbach@gmail.com>
@version 1.0
@section LICENSE

This file is part of UrbanBEATS (www.urbanbeatsmodel.com)
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
from md_perfassessguic import *        #UBCORE
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import PyQt4

from urbanbeatsmodule import *      #UBCORE

class PerformanceAssess(UBModule):      #UBCORE
    """Performs performance assessment actions on the output set of blocks and WSUD options
    performance assessment is quite modular.

    v1.0: Initial build of revised concept of Performance Assessment
        - Three key features: MUSIC simulation file creation, economics, microclimate
        - MUSIC interface quite simplistic, but allows linkage with WSC Toolkit

	@ingroup UrbanBEATS
        @author Peter M Bach
        """

    def __init__(self, activesim, tabindex, cycletype):      #UBCORE
        UBModule.__init__(self)      #UBCORE
        self.cycletype = cycletype       #UBCORE: contains either planning or implementation (so it knows what to do and whether to skip)
        self.tabindex = tabindex        #UBCORE: the simulation period (knowing what iteration this module is being run at)
        self.activesim = activesim      #UBCORE

        #PARAMETER LIST START
        #-----------------------------------------------------------------------
        #SELECT ANALYSES TAB
        self.createParameter("perf_MUSIC", BOOL, "Yes/No MUSIC")
        self.createParameter("perf_Economics", BOOL, "Yes/No Economic Stuff")
        self.createParameter("perf_Microclimate", BOOL, "Yes/No Microclimate Stuff")
        self.createParameter("perf_EPANET", BOOL, "Yes/No EPANET Link")
        self.createParameter("perf_CD3", BOOL, "Yes/No Integrated Water Cycle Model")
        self.perf_MUSIC = 0
        self.perf_Economics = 0
        self.perf_Microclimate = 0
        self.perf_EPANET = 0
        self.perf_CD3 = 0

        #MUSIC TAB
        self.createParameter("musicversion", DOUBLE, "Active MUSIC Version for file writing")
        self.createParameter("musicclimatefile", STRING, "Path to the .mlb climate file")
        self.createParameter("musicseparatebasin", BOOL, "Write separate .msf files per basin?")
        self.musicversion = 6.0
        self.musicclimatefile = ""
        self.musicseparatebasin = 1

        self.createParameter("bf_tncontent", DOUBLE, "TN content of Bioretention filter media")
        self.createParameter("bf_orthophosphate", DOUBLE, "Orthophosphate content of filter media")
        self.bf_tncontent = 800.0
        self.bf_orthophosphate = 50.0

        #ECONOMICS TAB

        #MICROCLIMATE TAB

        #WATER SUPPLY

        #INTEGRATED WATER CYCLE MODEL

        #ADVANCED PARAMETERS ---------------------------------------------------------


        # ----------------------------------------------------------------------------

    def run(self):
        self.notify("Now Running Performance Assessment")

        #Identify total number of performance assessments to undertake.
        #   Static = all top ranking options
        #   Dynamic = the chosen option

        options = 10

        for i in range(options):    #For each option, loop and conduct each selected analysis
            current = i

            if self.perf_MUSIC:
                self.writeMUSIC()


            if self.perf_Economics:
                self.runEconomicAnalysis()


            if self.perf_Microclimate:
                self.runMicroclimateAnalysis()


            if self.perf_EPANET:
                self.runWaterSupply()


            if self.perf_CD3:
                self.runIWCM()

        return True


    def writeMUSIC(self):
        """ Executes the export option to a MUSIC simulation file, the program uses the options
        to create a number of MUSIC files to the export directory with the given block attributes
        system options and parameters.
        """
        pass

        return True

    def runEconomicAnalysis(self):
        """Conducts an economic analysis of the life cycle costs and a number of other factors based
        on the planned options
        """
        pass

        return True

    def runMicroclimateAnalysis(self):
        """ Undertakes land cover analysis followed by applying land surface and air temperature
        relationships to understand local microclimate of the current modelled urban environment.
        """
        pass

        return True

    def runWaterSupply(self):
        """ Conducts integration with EPANET and water supply modelling. Coming Soon. Subject of
        future research
        """
        pass

        return True

    def runIWCM(self):
        """ Creates a simulation file and calls the CityDrain3 Modelling Platform to undertake
        detailed performance assessment of the integrated urban water cycle from a quantity and
        quality perspective.
        """
        pass

        return True




