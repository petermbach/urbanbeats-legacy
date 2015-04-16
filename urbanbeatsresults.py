# -*- coding: utf-8 -*-
"""
@file
@author  Peter M Bach <peterbach@gmail.com>
@version 0.5
@section LICENSE

This file is part of UrbanBEATS
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

__author__ = 'Peter M Bach'

import sys, os
#import mapnik
from urbanbeatscore import *
import PyQt4
from PyQt4 import QtGui, QtCore, QtWebKit
from urbanbeatsresultsgui import Ui_ResultsBrowseDialog
import ubhighcharts, ubleafletjs, urbanbeatssummaries

def createTopLevelItem(name):
    """Creates a top level item for a tree widget"""
    category = QtGui.QTreeWidgetItem()
    category.setText(0, str(name))
    return category

class ResultsBrowseDialogLaunch(QtGui.QDialog):
    def __init__(self, activesim, parent = None):
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_ResultsBrowseDialog()
        self.ui.setupUi(self)
        self.module = activesim
        self.options_root = activesim.getGlobalOptionsRoot()
        #Add children to TreeWidget
        self.ui.ue_categoryTree.clear()

        self.project_path = activesim.getActiveProjectPath()
        self.gis_details = activesim.getGISExportDetails()
        self.map_files = self.gis_details["Filename"]

        #PROJECT SUMMARY WINDOW
        toplevitems = [createTopLevelItem("FULL SUMMARY"), createTopLevelItem("General Info"), createTopLevelItem("Synopsis"), createTopLevelItem("Simulation Details")]
        narratives = activesim.getAllNarratives()
        for i in range(len(narratives)):
            toplevitems.append(createTopLevelItem(str(narratives[i][0])))
        toplevitems.append(createTopLevelItem("Available Outputs"))
        self.ui.ps_categoryTree.addTopLevelItems(toplevitems)
        summaryhtml = urbanbeatssummaries.getProjectSummary(activesim, 'all')
        self.ui.ps_WebView.setHtml(summaryhtml)

        #SPATIAL MAP VIEWER - LEAFLET MAP TILES
        self.htmlscript0 = ubleafletjs.writeLeafletScript("off", self.project_path, self.map_files, self.options_root)
        self.ui.sm_WebView.setHtml(self.htmlscript0)


        #URBAN ENVIRONMENT RESULTS



        #Some example charts
        category1 = QtGui.QTreeWidgetItem()
        category1.setText(0, "BasicLinePlot")
        category2 = QtGui.QTreeWidgetItem()
        category2.setText(0, "PieChart")
        category3 = QtGui.QTreeWidgetItem()
        category3.setText(0, "BasicBarChart")
        category4 = QtGui.QTreeWidgetItem()
        category4.setText(0, "BasicColumnChart")
        category5 = QtGui.QTreeWidgetItem()
        category5.setText(0, "ScatterPlotExample")
        category6 = QtGui.QTreeWidgetItem()
        category6.setText(0, "SpiderWeb")
        category7 = QtGui.QTreeWidgetItem()
        category7.setText(0, "BoxPlotExample")
        category8 = QtGui.QTreeWidgetItem()
        category8.setText(0, "BarNegativeStack")
        category9 = QtGui.QTreeWidgetItem()
        category9.setText(0, "ColumnStackedExample")
        category10 = QtGui.QTreeWidgetItem()
        category10.setText(0, "")
        toplevitems = [category1, category2, category3, category4, category5, category6, category7, category8, category9]
        self.ui.ue_categoryTree.addTopLevelItems(toplevitems)

        #Data Prep for CATEGORY 1
        testcharttitle = "Random temperatures for different cities"
        testcategories = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        testdatadict = {"Tokyo":[7.0, 6.9, 9.5, 14.5, 18.2, 21.5, 25.2, 26.5, 23.3, 18.3, 13.9, 9.6],
                        "New York":[-0.2, 0.8, 5.7, 11.3, 17.0, 22.0, 24.8, 24.1, 20.1, 14.1, 8.6, 2.5],
                        "Berlin":[-0.9, 0.6, 3.5, 8.4, 13.5, 17.0, 18.6, 17.9, 14.3, 9.0, 3.9, 1.0],
                        "London":[3.9, 4.2, 5.7, 8.5, 11.9, 15.2, 17.0, 16.6, 14.2, 10.3, 6.6, 4.8],
                        "Melbourne":[40.0, 35.0, 27.2, 18.0, 15.1, 10.1, 12.5, 15.9, 19.4, 23.8, 29.1, 34.1]}
        testxlabel = "Month of the year"
        testylabel = "Temperature (degrees Celcius)"
        testunits = "oC"
        self.htmlscript1 = ubhighcharts.line_basic(self.options_root, testcharttitle, testcategories, testxlabel, testylabel, testunits, testdatadict)

        #Data Prep for CATEGORY 2
        testcharttitle = "Utilisation of WSUD within Project Region"
        testseriesname = "Technology Type"
        testdatadict = {"Biofilters":35.0, "Infiltration":10.0, "Swales":26.8, "Ponds":12.8, "Greywater":8.5, "Wetlands":6.2, "Raintanks":0.7}        
        self.htmlscript2 = ubhighcharts.pie_basic(self.options_root, testcharttitle, testseriesname, testdatadict)

        #Data Prep for CATEGORY 3
        testcharttitle = "BasicBarChartExample"
        testcategories = ['Africa', 'America', 'Asia', 'Europe', 'Oceania']
        testlabel = 'Population (millions)'
        testunits = 'millions'
        testdatadict = {"Year 1800":[107, 31, 635, 203, 2],
                        "Year 1900":[133, 156, 947, 408, 6],
                        "Year 2008":[973, 914, 4054, 732, 34],
                        "Year 2013":[1000, 999, 4800, 922, 100]}                
        self.htmlscript3 = ubhighcharts.bar_basic(self.options_root, testcharttitle, testcategories, testlabel, testunits, testdatadict)
        
        #Data Prep for CATEGORY 4
        testcharttitle = "BasicColumnChartExample"
        testcategories = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        testdatadict = {"Tokyo":[49.9, 71.5, 106.4, 129.2, 144.0, 176.0, 135.6, 148.5, 216.4, 194.1, 95.6, 54.4],
                        "New York":[83.6, 78.8, 98.5, 93.4, 106.0, 84.5, 105.0, 104.3, 91.2, 83.5, 106.6, 92.3],
                        "London":[48.9, 38.8, 39.3, 41.4, 47.0, 48.3, 59.0, 59.6, 52.4, 65.2, 59.3, 51.2],
                        "Berlin":[42.4, 33.2, 34.5, 39.7, 52.6, 75.5, 57.4, 60.4, 47.6, 39.1, 46.8, 51.1]}
        testlabel = "Rainfall [mm]"
        labelformat = [-45, 'right', 13, 'Verdana, sans-serif']
        testunits = "mm"        
        self.htmlscript4 = ubhighcharts.column_basic(self.options_root, testcharttitle, testcategories, testlabel, labelformat, testunits, testdatadict)

        #Data Prep for CATEGORY 5
        testcharttitle = "ScatterPlotExample"
        testdatadict = {'Specimen1':[[161.2, 51.6],[167.5, 59.0],[159.5, 49.2], [157.0, 63.0], [155.8, 53.6],[170.0, 59.0], [159.1, 47.6],
                    [166.0, 69.8],[176.2, 66.8], [160.2, 75.2],[172.5, 55.2], [170.9, 54.2], [172.9, 62.5],[153.4, 42.0], [160.0, 50.0],
                    [147.2, 49.8], [168.2, 49.2], [175.0, 73.2],[157.0, 47.8], [167.6, 68.8],[159.5, 50.6], [175.0, 82.5], [166.8, 57.2],[176.5, 87.8], [170.2, 72.8],
                    [174.0, 54.5], [173.0, 59.8], [179.9, 67.3],[170.5, 67.8], [160.0, 47.0],[154.4, 46.2], [162.0, 55.0], [176.5, 83.0],[160.0, 54.4], [152.0, 45.8],
                    [162.1, 53.6], [170.0, 73.2], [160.2, 52.1],[161.3, 67.9], [166.4, 56.6],[168.9, 62.3], [163.8, 58.5], [167.6, 54.5],[160.0, 50.2], [161.3, 60.3],
                    [167.6, 58.3], [165.1, 56.2], [160.0, 50.2],[170.0, 72.9], [157.5, 59.8],[167.6, 61.0], [160.7, 69.1], [163.2, 55.9],[152.4, 46.5], [157.5, 54.3],
                    [168.3, 54.8], [180.3, 60.7], [165.5, 60.0],[165.0, 62.0], [164.5, 60.3],[156.0, 52.7], [160.0, 74.3], [163.0, 62.0],[165.7, 73.1], [161.0, 80.0],
                    [162.0, 54.7], [166.0, 53.2], [174.0, 75.7],[172.7, 61.1], [167.6, 55.7],[151.1, 48.7], [164.5, 52.3], [163.5, 50.0],[152.0, 59.3], [169.0, 62.5],
                    [164.0, 55.7], [161.2, 54.8], [155.0, 45.9],[170.0, 70.6], [176.2, 67.2],[170.0, 69.4], [162.5, 58.2], [170.3, 64.8],[164.1, 71.6], [169.5, 52.8],
                    [163.2, 59.8], [154.5, 49.0], [159.8, 50.0],[173.2, 69.2], [170.0, 55.9],[161.4, 63.4], [169.0, 58.2], [166.2, 58.6],[159.4, 45.7], [162.5, 52.2],
                    [159.0, 48.6], [162.8, 57.8], [159.0, 55.6],[179.8, 66.8], [162.9, 59.4],[161.0, 53.6], [151.1, 73.2], [168.2, 53.4],[168.9, 69.0], [173.2, 58.4],
                    [171.8, 56.2], [178.0, 70.6], [164.3, 59.8],[163.0, 72.0], [168.5, 65.2],[166.8, 56.6], [172.7, 105.2], [163.5, 51.8],[169.4, 63.4], [167.8, 59.0],
                    [159.5, 47.6], [167.6, 63.0], [161.2, 55.2],[160.0, 45.0], [163.2, 54.0],[162.2, 50.2], [161.3, 60.2], [149.5, 44.8],[157.5, 58.8], [163.2, 56.4],
                    [172.7, 62.0], [155.0, 49.2], [156.5, 67.2],[164.0, 53.8], [160.9, 54.4],[162.8, 58.0], [167.0, 59.8], [160.0, 54.8],[160.0, 43.2], [168.9, 60.5],
                    [158.2, 46.4], [156.0, 64.4], [160.0, 48.8],[167.1, 62.2], [158.0, 55.5],[167.6, 57.8], [156.0, 54.6], [162.1, 59.2],[173.4, 52.7], [159.8, 53.2],
                    [170.5, 64.5], [159.2, 51.8], [157.5, 56.0],[161.3, 63.6], [162.6, 63.2],[160.0, 59.5], [168.9, 56.8], [165.1, 64.1],[162.6, 50.0], [165.1, 72.3],
                    [166.4, 55.0], [160.0, 55.9], [152.4, 60.4],[170.2, 69.1], [162.6, 84.5],[170.2, 55.9], [158.8, 55.5], [172.7, 69.5],[167.6, 76.4], [162.6, 61.4],
                    [167.6, 65.9], [156.2, 58.6], [175.2, 66.8],[172.1, 56.6], [162.6, 58.6],[160.0, 55.9], [165.1, 59.1], [182.9, 81.8],[166.4, 70.7], [165.1, 56.8]],
                        'Specimen2':[[177.8, 60.0], [165.1, 58.2], [175.3, 72.7],[154.9, 54.1], [158.8, 49.1],
                    [172.7, 75.9], [168.9, 55.0], [161.3, 57.3],[167.6, 55.0], [165.1, 65.5],[175.3, 65.5], [157.5, 48.6], [163.8, 58.6],[167.6, 63.6], [165.1, 55.2],
                    [165.1, 62.7], [168.9, 56.6], [162.6, 53.9],[164.5, 63.2], [176.5, 73.6],[168.9, 62.0], [175.3, 63.6], [159.4, 53.2],[160.0, 53.4], [170.2, 55.0],
                    [162.6, 70.5], [167.6, 54.5], [162.6, 54.5],[160.7, 55.9], [160.0, 59.0],[157.5, 63.6], [162.6, 54.5], [152.4, 47.3],[170.2, 67.7], [165.1, 80.9],
                    [172.7, 70.5], [165.1, 60.9], [170.2, 63.6],[170.2, 54.5], [170.2, 59.1],[161.3, 70.5], [167.6, 52.7], [167.6, 62.7],[165.1, 86.3], [162.6, 66.4],
                    [152.4, 67.3], [168.9, 63.0], [170.2, 73.6],[175.2, 62.3], [175.2, 57.7],[160.0, 55.4], [165.1, 104.1], [174.0, 55.5],[170.2, 77.3], [160.0, 80.5],
                    [167.6, 64.5], [167.6, 72.3], [167.6, 61.4],[154.9, 58.2], [162.6, 81.8],[175.3, 63.6], [171.4, 53.4], [157.5, 54.5],[165.1, 53.6], [160.0, 60.0],
                    [174.0, 73.6], [162.6, 61.4], [174.0, 55.5],[162.6, 63.6], [161.3, 60.9],[156.2, 60.0], [149.9, 46.8], [169.5, 57.3],[160.0, 64.1], [175.3, 63.6],
                    [169.5, 67.3], [160.0, 75.5], [172.7, 68.2],[162.6, 61.4], [157.5, 76.8],[176.5, 71.8], [164.4, 55.5], [160.7, 48.6],[174.0, 66.4], [163.8, 67.3],
                    [188.0, 82.7], [175.3, 86.4], [170.5, 67.7], [179.1, 92.7], [177.8, 93.6],[175.3, 70.9], [182.9, 75.0], [170.8, 93.2], [188.0, 93.2], [180.3, 77.7],
                    [177.8, 61.4], [185.4, 94.1], [168.9, 75.0], [185.4, 83.6], [180.3, 85.5],[174.0, 73.9], [167.6, 66.8], [182.9, 87.3], [160.0, 72.3], [180.3, 88.6],
                    [167.6, 75.5], [186.7, 101.4], [175.3, 91.1], [175.3, 67.3], [175.9, 77.7],[175.3, 81.8], [179.1, 75.5], [181.6, 84.5], [177.8, 76.6], [182.9, 85.0],
                    [177.8, 102.5], [184.2, 77.3], [179.1, 71.8], [176.5, 87.9], [188.0, 94.3],[174.0, 70.9], [167.6, 64.5], [170.2, 77.3], [167.6, 72.3], [188.0, 87.3],
                    [174.0, 80.0], [176.5, 82.3], [180.3, 73.6], [167.6, 74.1], [188.0, 85.9],[180.3, 73.2], [167.6, 76.3], [183.0, 65.9], [183.0, 90.9], [179.1, 89.1],
                    [170.2, 62.3], [177.8, 82.7], [179.1, 79.1], [190.5, 98.2], [177.8, 84.1],[180.3, 83.2], [180.3, 83.2]],
                        'Specimen3':[[174.0, 65.6], [175.3, 71.8], [193.5, 80.7], [186.5, 72.6], [187.2, 78.8],
                    [181.5, 74.8], [184.0, 86.4], [184.5, 78.4], [175.0, 62.0], [184.0, 81.6],[180.0, 76.6], [177.8, 83.6], [192.0, 90.0], [176.0, 74.6], [174.0, 71.0],
                    [184.0, 79.6], [192.7, 93.8], [171.5, 70.0], [173.0, 72.4], [176.0, 85.9],[176.0, 78.8], [180.5, 77.8], [172.7, 66.2], [176.0, 86.4], [173.5, 81.8],
                    [178.0, 89.6], [180.3, 82.8], [180.3, 76.4], [164.5, 63.2], [173.0, 60.9],[183.5, 74.8], [175.5, 70.0], [188.0, 72.4], [189.2, 84.1], [172.8, 69.1],
                    [170.0, 59.5], [182.0, 67.2], [170.0, 61.3], [177.8, 68.6], [184.2, 80.1],[186.7, 87.8], [171.4, 84.7], [172.7, 73.4], [175.3, 72.1], [180.3, 82.6],
                    [182.9, 88.7], [188.0, 84.1], [177.2, 94.1], [172.1, 74.9], [167.0, 59.1],[169.5, 75.6], [174.0, 86.2], [172.7, 75.3], [182.2, 87.1], [164.1, 55.2],
                    [163.0, 57.0], [171.5, 61.4], [184.2, 76.8], [174.0, 86.8], [174.0, 72.2],[177.0, 71.6], [186.0, 84.8], [167.0, 68.2], [171.8, 66.1], [182.0, 72.0],
                    [167.0, 64.6], [177.8, 74.8], [164.5, 70.0], [192.0, 101.6], [175.5, 63.2],[171.2, 79.1], [181.6, 78.9], [167.4, 67.7], [181.1, 66.0], [177.0, 68.2],
                    [174.5, 63.9], [177.5, 72.0], [170.5, 56.8], [182.4, 74.5], [197.1, 90.9],[180.1, 93.0], [175.5, 80.9], [180.6, 72.7], [184.4, 68.0], [175.5, 70.9],
                    [180.6, 72.5], [177.0, 72.5], [177.1, 83.4], [181.6, 75.5], [176.5, 73.0],[175.0, 70.2], [174.0, 73.4], [165.1, 70.5], [177.0, 68.9], [192.0, 102.3],
                    [176.5, 68.4], [169.4, 65.9], [182.1, 75.7], [179.8, 84.5], [175.3, 87.7],[184.9, 86.4], [177.3, 73.2], [167.4, 53.9], [178.1, 72.0], [168.9, 55.5],
                    [157.2, 58.4], [180.3, 83.2], [170.2, 72.7], [177.8, 64.1], [172.7, 72.3],[165.1, 65.0], [186.7, 86.4], [165.1, 65.0], [174.0, 88.6], [175.3, 84.1],
                    [185.4, 66.8], [177.8, 75.5], [180.3, 93.2], [180.3, 82.7], [177.8, 58.0],[177.8, 79.5], [177.8, 78.6], [177.8, 71.8], [177.8, 116.4], [163.8, 72.2],
                    [188.0, 83.6], [198.1, 85.5], [175.3, 90.9], [166.4, 85.9], [190.5, 89.1],[166.4, 75.0], [177.8, 77.7], [179.7, 86.4], [172.7, 90.9], [190.5, 73.6],
                    [185.4, 76.4], [168.9, 69.1], [167.6, 84.5], [175.3, 64.5], [170.2, 69.1],[190.5, 108.6], [177.8, 86.4], [190.5, 80.9], [177.8, 87.7], [184.2, 94.5],
                    [176.5, 80.2], [177.8, 72.0], [180.3, 71.4], [171.4, 72.7], [172.7, 84.1],[172.7, 76.8], [177.8, 63.6], [177.8, 80.9], [182.9, 80.9], [170.2, 85.5],
                    [167.6, 68.6], [175.3, 67.7], [165.1, 66.4], [185.4, 102.3], [181.6, 70.5],[172.7, 95.9], [190.5, 84.1], [179.1, 87.3], [175.3, 71.8], [170.2, 65.9],
                    [193.0, 95.9], [171.4, 91.4], [177.8, 81.8], [177.8, 96.8], [167.6, 69.1],[167.6, 82.7], [180.3, 75.5], [182.9, 79.5], [176.5, 73.6], [186.7, 91.8],
                    [188.0, 84.1], [188.0, 85.9], [177.8, 81.8], [174.0, 82.5], [177.8, 80.5],[171.4, 70.0], [185.4, 81.8], [185.4, 84.1], [188.0, 90.5], [188.0, 91.4],
                    [182.9, 89.1], [176.5, 85.0], [175.3, 69.1], [175.3, 73.6], [188.0, 80.5]]}
        self.htmlscript5 = ubhighcharts.scatter_plot(self.options_root, testcharttitle, "Height(cm)", "Weight(cm)", 4, "cm", "kg", testdatadict)

        #Data Prep for CATEGORY 6
        testcharttitle = "Spiderweb Example"
        testcategories = ["RES", "COM", "HI", "LI", "ORC", "PG", "REF", "RD", "TR", "CIV", "NA", "UND"]
        testdatadict = {"Block 57":[50, 0, 0, 0, 0, 10, 5, 7, 0,10,0,18], "Block 77": [30, 20, 0, 20, 0,0,30,0,0,0,0,0]}
        self.htmlscript6 = ubhighcharts.spiderweb(self.options_root, testcharttitle,testcategories, "%", testdatadict)

        #Data Prep for CATEGORY 7
        testcharttitle = "Boxplot Example"
        testcategories = ["Apples", "Oranges", "Bananas", "Watermelons", "Apricots", "Grapes"]
        #test data dict: Data is organised as [ [ min, Lower Quartile, Median, Upper Quartile, Max], ...] and Outliers [Category, value] where category
        #takes the index of the categories vector (starting from zero 0)
        testdatadict = {"Data": [[20, 23, 26, 28, 34], [11, 16, 18, 20, 27], [34, 37, 42, 49, 50], [23, 27, 33, 36, 40], [11, 13, 17, 21, 24], [54, 58, 61, 63, 68]],
                        "Outliers": [[0,13],[0, 14],[1, 44],[3, 70],[3,20],[5, 32]]}
        self.htmlscript7 = ubhighcharts.box_plot(self.options_root, testcharttitle, testcategories, "Fruit Type", "Distribution", "kg", testdatadict)

        #Data Prep for CATEGORY 8
        testcharttitle = "Negative Stack Example"
        #Categories and length of data matrix must match up. The datadict only contains two series: these are compared against each other.
        #All values in one series must be multiple by -1 to put them on the opposite end of the scale.
        testcategories = ["Population", "Developed Area", "Age", "Wealth", "Employment", "Runoff", "Evaporation", "Planning", "WSUD"]
        testdatadict = {'Basin 7':[-1746181, -1884428, -2089758, -2222362, -2537431, -2507081, -2443179,-2664537, -3556505],
                        'Basin 9':[1656154, 1787564, 1981671, 2108575, 2403438, 2366003, 2301402, 2519874,3360596]}
        self.htmlscript8 = ubhighcharts.bar_negative_stack(self.options_root, testcharttitle, testcategories, testdatadict)

        #Data Prep for CATEGORY 9
        testcharttitle = "StackedColumn Example"
        testcategories = ["Apples", "Oranges", "Grapes", "Watermelons"]
        testdatadict = {"John":[2, 3, 2, 5], "Kate":[1, 5, 4, 2], "Elizabeth":[3, 3, 2, 1], "James":[2, 1, 2, 2]}
        self.htmlscript9 = ubhighcharts.column_stacked(self.options_root, testcharttitle,testcategories,"Total Consumption", testdatadict)

        #Test - Click on Export Button to plot a chart in the GUI
        self.connect(self.ui.ue_categoryTree, QtCore.SIGNAL("itemSelectionChanged()"), self.plotHighChart)


        #WATER DEMAND RESULTS
        self.updateWDList()
        self.ui.wd_unitskl.setChecked(1)
        self.connect(self.ui.wd_comboScope, QtCore.SIGNAL("currentIndexChanged(int)"), self.updateWDList)
        self.connect(self.ui.wd_listwidget, QtCore.SIGNAL("itemSelectionChanged()"), self.plotWD)
        self.connect(self.ui.wd_listwidget, QtCore.SIGNAL("itemSelectionChanged()"), self.updateWDQuickInfo)
        self.connect(self.ui.wd_exportResults, QtCore.SIGNAL("clicked()"), self.export_wd_results)
        self.connect(self.ui.wd_unitskl, QtCore.SIGNAL("clicked()"), self.plotWD)
        self.connect(self.ui.wd_unitslps, QtCore.SIGNAL("clicked()"), self.plotWD)

    def export_wd_results(self):
        pass

    def adjustUnits(self):
        pass


    def updateWDQuickInfo(self, blockdata, peak, maxuse, plotunits):
        """Updates the quick info box to match the selection"""
        self.ui.wd_summarybox.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Quick Info</span></p>\n"
                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">ID: "+str(blockdata.getAttribute("BlockID"))+"</span></p>\n"
                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Population: "+str(int(blockdata.getAttribute("Pop")))+"</span></p>\n"
                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Households: "+str(int(blockdata.getAttribute("ResHouses")))+"</span></p>\n"
                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Flats: "+str(int(blockdata.getAttribute("HDRFlats")))+"</span></p>\n"
                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Efficiency Rating: "+str(int(blockdata.getAttribute("wd_Rating")))+"</span></p>\n"
                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Peak Demand: "+str(peak[0])+plotunits+" @ "+str(int(peak[1]))+":00</span></p>\n"
                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Largest Use: "+str(maxuse[1])+" ("+str(maxuse[0])+plotunits+")</span></p>\n"
                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Recycling: NO</span></p></body></html>")

    def plotWD(self):
        """Plots the water demand stack chart based on the combo box's settings"""
        timeaxis = "['0:00', '1:00', '2:00', '3:00', '4:00', '5:00', '6:00', '7:00', '8:00', '9:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00', '22:00', '23:00']"

        #Determine Units
        if self.ui.wd_unitslps.isChecked():
            plotunits = "L/sec"
        else:
            plotunits = "kL"

        axes = ["Time HH:MM", "Water Demand ["+str(plotunits)+"]"]

        if self.ui.wd_comboSelect.currentIndex() == 0:
            return True #Do nothing
        elif self.ui.wd_comboSelect.currentIndex() == 1:
            #Summary Demand Plot
            pass
        elif self.ui.wd_comboSelect.currentIndex() == 2:
            #24 hour Pattern Plot
            if self.ui.wd_comboScope.currentIndex() == 1:
                #Block Data
                blockdata = self.module.getAssetWithName(str(self.ui.wd_listwidget.currentItem().text()))

                plotdata = self.getDemandPatternsBlock(blockdata, plotunits)
                peakvalue, time = self.getPeakDemandValue(plotdata)
                maxuse, maxusetype = self.getLargestEndUse(plotdata)
                self.updateWDQuickInfo(blockdata, [peakvalue, time], [maxuse, maxusetype], plotunits)

                self.htmlscriptWD = ubhighcharts.stacked_chart(self.options_root, "24-hour Water Demand Pattern",
                                                               timeaxis, axes, "L", plotdata, plotunits)
                self.ui.wd_WebView.setHtml(self.htmlscriptWD)


        elif self.ui.wd_comboSelect.currentIndex() == 3:
            #Extended Period Demand Pattern
            pass

    def getLargestEndUse(self, patterndict):
        """Determines the largest end use and the hourly value"""
        maxenduse = 0   #Stores max value
        maxtype = ""    #stores type name
        for i in patterndict.keys():
            if max(patterndict[i]) > maxenduse:
                maxenduse = max(patterndict[i])
                maxtype = i
        return maxenduse, maxtype

    def getPeakDemandValue(self, patterndict):
        """Calculates the peak value in the stacked chart and returns the value and time of occurrence
        :param patterndict:
        :return:
        """
        totaldemseries = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        for i in patterndict.keys():
            for j in range(len(patterndict[i])):
                totaldemseries[j] += patterndict[i][j]
        peakdem = max(totaldemseries)
        peaktime = totaldemseries.index(peakdem)
        return peakdem, peaktime

    def getDemandPatternsBlock(self, blockdata, plotunits):
        map_attr = self.module.getAssetWithName("MapAttributes")
        enduses = ["kitchen", "shower", "toilet", "laundry", "irrigation", "com", "ind", "publicirri"]
        plotlabels = ["Kitchen", "Shower", "Toilet", "Laundry", "Garden", "Commercial", "Industrial", "Public Irrigation"]
        patterndict = {}
        if plotunits == "L/sec":
            conversionfactor = float(1.0/(24.0*3600.0))
        else:
            conversionfactor = float(1.0/24.0)

        for i in range(len(enduses)):
            pattern = map_attr.getAttribute("wdp_"+enduses[i])   #retrieve the array with pattern info
            if pattern == 0:
                print "WARNING Perf Assess probably not configured properly!"
                pattern = [1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0]

            avgdemand = float(blockdata.getAttribute("Blk_"+enduses[i])*conversionfactor)  #retrieve kl/day and convert to representative units
            demandseries = []
            for j in range(len(pattern)):
                demandseries.append(round(avgdemand * 1000 * pattern[j],2))     #Converts to Litres
            patterndict[plotlabels[i]] = demandseries
        return patterndict

    def updateWDList(self):
        """Water Demand Tab: Updates the list widget with either a list of blocks or basin IDs to choose from"""
        cat_types = ['none', 'block', 'basin']
        self.addCategoriesToList(self.ui.wd_listwidget, cat_types[self.ui.wd_comboScope.currentIndex()])

    def addCategoriesToList(self, listobject, cat_type):
        listobject.clear()
        if cat_type == 'none':
            return True
        elif cat_type == 'block':
            blockslist=  self.module.getAssetsWithIdentifier("BlockID")
            blockIDlist = []
            for i in blockslist:
                if i.getAttribute("Status") == 0:
                    continue
                blockIDlist.append(i.getAttribute("BlockID"))
            blockIDlist.sort()
            for i in range(len(blockIDlist)):
                c = QtGui.QListWidgetItem()
                c.setText("BlockID"+str(blockIDlist[i]))
                self.ui.wd_listwidget.addItem(c)
        elif cat_type == 'basin':
            basins = self.module.getAssetWithName("MapAttributes").getAttribute("TotalBasins")
            print basins
            for i in range(basins):
                c = QtGui.QListWidgetItem()
                c.setText("BasinID"+str(i+1))
                self.ui.wd_listwidget.addItem(c)
        return True


    def changeLeafletMap(self, tabindex):

        htmlscript = """ """

        return htmlscript


    def plotHighChart(self):
        print "plotting highchart"        
        treewitem = self.ui.ue_categoryTree.currentItem().text(0)
        if treewitem == "BasicLinePlot":
            self.ui.ue_WebView.setHtml(self.htmlscript1)
        elif treewitem == "PieChart":
            self.ui.ue_WebView.setHtml(self.htmlscript2)
        elif treewitem == "BasicBarChart":
            self.ui.ue_WebView.setHtml(self.htmlscript3)
        elif treewitem == "BasicColumnChart":
            self.ui.ue_WebView.setHtml(self.htmlscript4)
        elif treewitem == "ScatterPlotExample":
            self.ui.ue_WebView.setHtml(self.htmlscript5)
        elif treewitem == "SpiderWeb":
            self.ui.ue_WebView.setHtml(self.htmlscript6)
        elif treewitem == "BoxPlotExample":
            self.ui.ue_WebView.setHtml(self.htmlscript7)
        elif treewitem == "BarNegativeStack":
            self.ui.ue_WebView.setHtml(self.htmlscript8)
        elif treewitem == "ColumnStackedExample":
            self.ui.ue_WebView.setHtml(self.htmlscript9)


        
        
        
            