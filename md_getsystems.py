# -*- coding: utf-8 -*-
"""
@file
@author Peter M Bach <peterbach@gmail.com>
@version 0.5
@section LICENSE

This file is part of VIBe2
Copyright (C) 2011 Peter M Bach

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
"""

#from pyvibe import *
#from pydynamind import *
import urbanbeatsdatatypes as ubdata    #UBCORE
from urbanbeatsmodule import *      #UBCORE
from osgeo import ogr, osr
import sys
import os

class GetSystems(UBModule):
    """Loads the Points Shapefile and transfers all relevant information about water management systems into
    a suitable data management structure for use in implementation modules
        Inputs: Either project path or exact filename
            - Obtain file directly from a filename or from an ongoing simulation? - Boolean
        Filename: specify path
        Ongoing simulation: specify project path (it is likely the program will load a text file with information on how to grab the shapefile)
        Outputs: Vector Data containing block attributes (these are used in later modules as a comparison with the newly entered data)

    Log of Updates made at each version:
    v0.80 (March 2012):
        - First created. Imports a systems shape file, containing points of each system
        - Future work: To make sure the projection is adjusted if the file was not created by UrbanBEATS

    @ingroup UrbanBEATS
    @author Peter M Bach
    """
    def __init__(self, activesim, tabindex):
        UBModule.__init__(self)
        self.cycletype = "pc"           #UBCORE: contains either planning or implementation (so it knows what to do and whether to skip)
        self.tabindex = tabindex        #UBCORE: the simulation period (knowing what iteration this module is being run at)
        self.activesim = activesim      #UBCORE

        self.createParameter("ubeats_file", BOOL,"")
        self.createParameter("ongoing_sim", BOOL,"")
        self.createParameter("path_name", STRING,"")
        self.ubeats_file = 1 #Was this file created by UrbanBEATS or is it man-made?
        self.ongoing_sim = 0 #Is this module part of an ongoing simulation?
        #self.path_name = homeDir + '/Documents/UrbanBEATS/UrbanBeatsModules/data/0_screek-500msys-1970impl_points.shp'
        self.path_name = "D:\\Screek500m_PlannedWSUD1.shp" #specify C-drive as default value
        
    def run(self):
        self.notify("Start GetSystems Module")
        sys_global = ubdata.UBComponent() #write all general attributes in here

        #Get the correct driver (we are working with ESRI Shapefiles)
        driver = ogr.GetDriverByName('ESRI Shapefile')
        
        #Use the following file for testing
        save_file = "ubeats_out.shp"
        if self.ongoing_sim == True:
            file_name = self.path_name + save_file
        else:
            file_name = self.path_name
        
        self.notify(str(file_name))
        
        #open data source, check if it exists otherwise quit.
        dataSource = driver.Open(file_name, 0)
        if dataSource is None:
            self.notify("Error, could not open "+str(file_name))
            sys_global.addAttribute("TotalSystems", 0)
            self.activesim.addAsset("SysPrevGlobal", sys_global)
            return False
        
        layer = dataSource.GetLayer()
        total_systems = layer.GetFeatureCount()
        spatialRef = layer.GetSpatialRef()
        self.notify("Spatial Reference (Proj4): " + str(spatialRef.ExportToProj4()))
        
        #Perform some comparison to make sure that the projection of the loaded file is identical to that of the final desired format
        #Code...
        #...
        
        #add global attributes
        sys_global.addAttribute("TotalSystems", total_systems)
        self.notify("Total Systems in Map: "+str(total_systems))
        sys_global.addAttribute("UBFile", self.ubeats_file)
        
        #Loop through each feature and grab all the relevant information
        for i in range(int(total_systems)):
            feature = layer.GetFeature(i)
            sys_attr = ubdata.UBComponent()
            #city.addComponent(sys_attr,self.sysAttr)
            sys_attr.addAttribute("SysID", i+1)
            total_attrs = feature.GetFieldCount()  #gets total number of attributes
            for j in range(int(total_attrs)):           
                name = str(feature.GetFieldDefnRef(j).GetName())        #Obtain attribute name from FieldDefn object
                value = feature.GetField(j)                        #get the value from the field using the same index
                if value == None:
                    pass
                else:
                    sys_attr.addAttribute(str(name), value)                    #assign to block_attr vector

            feature.Destroy()      #destroy to save memory
            self.activesim.addAsset("SysPrevID"+str(i+1), sys_attr)
        self.activesim.addAsset("SysPrevGlobal", sys_global)
        #Destroy the shapefile to free up memory
        dataSource.Destroy()
        #END OF MODULE
