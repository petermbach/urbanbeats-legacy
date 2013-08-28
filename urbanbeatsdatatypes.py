# -*- coding: utf-8 -*-
"""
@file
@author  Peter M Bach <peterbach@gmail.com>
@version 1.0
@section LICENSE

This file is part of UrbanBEATS
Copyright (C) 2011,2012,2013  Peter M Bach

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
from osgeo import ogr, osr
import os
import ogr2ogr

### IMPORT FUNCTIONS

def importRasterData(filepath):
    """Imports a raster data file and creates an output rasterdata object, which contains
    the data from the import file. The input file is passed as the only argument to this function
    in the form of a string of the full path and filename.

    Raster data loaded from this function is flipped to ensure that it coincides with x and y. The
    indexing of the raster data, however, starts from zero! So ncols and nrows indices should be
    subtracted by 1 if the value is to be called from the file.

    Output RasterData Type has following functions:
        - getValue(x,y) - returns value in the raster at the given coordinates
        - getDimensions() - returns a vector [x,y] of dimensions of the raster
        - getExtents() - returns the [x,y] map coordinates of the raster
        - getCellSize() - returns the cell size of the raster file in the units of the input .txt file
        - resetData() - erases the raster data completely, leaving an empty object, keeps basic info data
    """
    f = open(filepath, 'r')     #Load the raster data
    linecounter = 0
    infoarray = []
    dataarray = []
    for lines in f:
        a = lines.split()
        if linecounter <= 5:
            infoarray.append(float(a[1]))
        else:
            dataarray.append(a)
        linecounter += 1
    f.close()    
    
    #Create the Raster Data Object
    rasterdata = RasterData(int(infoarray[0]), int(infoarray[1]), infoarray[2], infoarray[3], infoarray[4], infoarray[5])
    rasterdata.setData(dataarray)
    return rasterdata            

### GIS EXPORT FUNCTIONS

def exportGISShapeFile(activesim):
    """Exports the Active Simulation's Asset Data to the specified shapefiles requested
    using the Osgeo GDAL library"""
    #Get the following info:
    gisoptions = activesim.getGISExportDetails()
    map_data = activesim.getAssetWithName("MapAttributes")
    fname = gisoptions["Filename"]
    if gisoptions["ProjUser"] == True:
        proj = gisoptions["Proj4"]
    else:
        proj = gisoptions["Projection"]

    if gisoptions["Offset"] == "I":    
        offsets = [map_data.getAttribute("xllcorner"), map_data.getAttribute("yllcorner")]
    elif gisoptions["Offset"] == "C":
        offsets = [gisoptions["OffsetCustX"], gisoptions["OffsetCustY"]]
    miscoptions = [proj, offsets[0], offsets[1]]

    kmlbool = gisoptions["GoogleEarth"]
    print "kmlbool", kmlbool
    #what maps to export
    
    os.chdir(activesim.getActiveProjectPath())
    
    if gisoptions["BuildingBlocks"] == 1:
        print "Exporting Blocks"
        #Get all assets from activesim
        assets = activesim.getAssetsWithIdentifier("BlockID")
        exportBuildingBlocks(fname, assets, miscoptions, map_data, kmlbool)
        
    if gisoptions["PatchData"] == 1:
        print "Exporting Patch Data"
        #Get all assets from activesim        
        assets = activesim.getAssetsWithIdentifier("PatchID")        
        exportPatchData(fname, assets, miscoptions, map_data)

    if gisoptions["Flowpaths"] == 1:
        print "Exporting Flow Paths"
        #Get all assets from activesim
        assets = activesim.getAssetsWithIdentifier("NetworkID")
        exportFlowPaths(fname, assets, miscoptions, map_data, kmlbool)

    if gisoptions["Localities"] == 1:
        print "Exporting Block Localities"
        #Get all assets from activesim
        assets = activesim.getAssetsWithIdentifier("FacilityID")
        exportBlockLocalities(fname, assets, miscoptions, map_data)

    if gisoptions["PlannedWSUD"] == 1:
        print "Exporting WSUD Planned"
        #Get all assets from activesim
        assets = 0
        exportPlannedWSUD(fname, assets, miscoptions, map_data)

    if gisoptions["ImplementedWSUD"] == 1:
        print "Exporting WSUD Implemented"
        #Get all assets from activesim
        assets = 0
        exportImplementWSUD(fname, assets, miscoptions, map_data, kmlbool)

    if gisoptions["CentrePoints"] == 1:
        print "Exporting Block Centres"
        #Get all assets from activesim
        assets = activesim.getAssetsWithIdentifier("CP")
        exportBlockCentre(fname, assets, miscoptions, map_data, kmlbool)
        
    print "Export Complete"          
    
    return True

def exportBuildingBlocks(filename, assets, miscoptions, map_attr, kmlbool):
    """Exports the Blocks to a GIS Shapefile using the Osgeo GDAL Library"""
     
    spatialRef = osr.SpatialReference()                #Define Spatial Reference
    spatialRef.ImportFromProj4(miscoptions[0])
    
    driver = ogr.GetDriverByName('ESRI Shapefile')
    if os.path.exists(str(filename)+"_Blocks.shp"): os.remove(str(filename)+"_Blocks.shp")
    shapefile = driver.CreateDataSource(str(filename)+"_Blocks.shp")
    
    layer = shapefile.CreateLayer('layer1', spatialRef, ogr.wkbPolygon)
    layerDefinition = layer.GetLayerDefn()
    
    #DEFINE ATTRIBUTES
    fielddefmatrix = []
        #>>> FROM DELINBLOCKS
    fielddefmatrix.append(ogr.FieldDefn("BlockID", ogr.OFTInteger))
    fielddefmatrix.append(ogr.FieldDefn("BasinID", ogr.OFTInteger))
    fielddefmatrix.append(ogr.FieldDefn("LocateX", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("LocateY", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("CentreX", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("CentreY", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("OriginX", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("OriginY", ogr.OFTReal))             
    fielddefmatrix.append(ogr.FieldDefn("Status", ogr.OFTInteger))         
    fielddefmatrix.append(ogr.FieldDefn("Active", ogr.OFTReal))            
    fielddefmatrix.append(ogr.FieldDefn("Nhd_N", ogr.OFTInteger))          
    fielddefmatrix.append(ogr.FieldDefn("Nhd_S", ogr.OFTInteger))          
    fielddefmatrix.append(ogr.FieldDefn("Nhd_W", ogr.OFTInteger))          
    fielddefmatrix.append(ogr.FieldDefn("Nhd_E", ogr.OFTInteger))          
    fielddefmatrix.append(ogr.FieldDefn("Nhd_NE", ogr.OFTInteger))         
    fielddefmatrix.append(ogr.FieldDefn("Nhd_NW", ogr.OFTInteger))         
    fielddefmatrix.append(ogr.FieldDefn("Nhd_SE", ogr.OFTInteger))         
    fielddefmatrix.append(ogr.FieldDefn("Nhd_SW", ogr.OFTInteger))         
    fielddefmatrix.append(ogr.FieldDefn("Soil_k", ogr.OFTReal))            
    fielddefmatrix.append(ogr.FieldDefn("AvgElev", ogr.OFTReal))           
    fielddefmatrix.append(ogr.FieldDefn("pLU_RES", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("pLU_COM", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("pLU_ORC", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("pLU_LI", ogr.OFTReal)) 
    fielddefmatrix.append(ogr.FieldDefn("pLU_HI", ogr.OFTReal)) 
    fielddefmatrix.append(ogr.FieldDefn("pLU_CIV", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("pLU_SVU", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("pLU_RD", ogr.OFTReal)) 
    fielddefmatrix.append(ogr.FieldDefn("pLU_TR", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("pLU_PG", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("pLU_REF", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("pLU_UND", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("pLU_NA", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("Pop", ogr.OFTReal))           
    
    if map_attr.getAttribute("include_employment") : fielddefmatrix.append(ogr.FieldDefn("Employ", ogr.OFTReal)) 
    if map_attr.getAttribute("include_groundwater") : fielddefmatrix.append(ogr.FieldDefn("GWDepth", ogr.OFTReal))
    if map_attr.getAttribute("include_soc_par1") : fielddefmatrix.append(ogr.FieldDefn("SocPar1", ogr.OFTReal))
    if map_attr.getAttribute("include_soc_par2") : fielddefmatrix.append(ogr.FieldDefn("SocPar2", ogr.OFTReal))
    if map_attr.getAttribute("include_plan_map") : fielddefmatrix.append(ogr.FieldDefn("PM_RES", ogr.OFTReal))
    if map_attr.getAttribute("include_plan_map") : fielddefmatrix.append(ogr.FieldDefn("PM_COM", ogr.OFTReal))
    if map_attr.getAttribute("include_plan_map") : fielddefmatrix.append(ogr.FieldDefn("PM_LI", ogr.OFTReal))
    if map_attr.getAttribute("include_plan_map") : fielddefmatrix.append(ogr.FieldDefn("PM_HI", ogr.OFTReal))
    if map_attr.getAttribute("include_rivers") : fielddefmatrix.append(ogr.FieldDefn("HasRiv", ogr.OFTReal))
    if map_attr.getAttribute("include_lakes") : fielddefmatrix.append(ogr.FieldDefn("HasLake", ogr.OFTReal))
    if map_attr.getAttribute("include_lakes") : fielddefmatrix.append(ogr.FieldDefn("LakeAr", ogr.OFTReal))
    if map_attr.getAttribute("include_local_map") : fielddefmatrix.append(ogr.FieldDefn("HasLoc", ogr.OFTReal))
    if map_attr.getAttribute("include_local_map") : fielddefmatrix.append(ogr.FieldDefn("NFacil", ogr.OFTReal))
    if map_attr.getAttribute("patchdelin") : fielddefmatrix.append(ogr.FieldDefn("Patches", ogr.OFTInteger))                                          
    if map_attr.getAttribute("spatialmetrics") : fielddefmatrix.append(ogr.FieldDefn("Rich", ogr.OFTReal))            
    if map_attr.getAttribute("spatialmetrics") : fielddefmatrix.append(ogr.FieldDefn("ShDIV", ogr.OFTReal))           
    if map_attr.getAttribute("spatialmetrics") : fielddefmatrix.append(ogr.FieldDefn("ShDOM", ogr.OFTReal))           
    if map_attr.getAttribute("spatialmetrics") : fielddefmatrix.append(ogr.FieldDefn("ShEVEN", ogr.OFTReal))          
    
    fielddefmatrix.append(ogr.FieldDefn("downID", ogr.OFTReal))          
    fielddefmatrix.append(ogr.FieldDefn("maxdZ", ogr.OFTReal))           
    fielddefmatrix.append(ogr.FieldDefn("slope", ogr.OFTReal))           
    fielddefmatrix.append(ogr.FieldDefn("drainID", ogr.OFTReal))         
    fielddefmatrix.append(ogr.FieldDefn("h_pond", ogr.OFTReal))          
    fielddefmatrix.append(ogr.FieldDefn("Outlet", ogr.OFTInteger))          

    if map_attr.getAttribute("considerCBD") : fielddefmatrix.append(ogr.FieldDefn("CBDdist", ogr.OFTReal))          
    if map_attr.getAttribute("considerCBD") : fielddefmatrix.append(ogr.FieldDefn("CBDdir", ogr.OFTReal))
 
     #>>> FROM URBPLANBB
    fielddefmatrix.append(ogr.FieldDefn("MiscAtot", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("UndType", ogr.OFTString))
    fielddefmatrix.append(ogr.FieldDefn("UND_av", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("OpenSpace", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("AGardens", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("ASquare", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("PG_av", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("REF_av", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("ANonW_Utils", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("SVU_avWS", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("SVU_avWW", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("SVU_avSW", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("SVU_avOTH", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("RoadTIA", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("ParkBuffer", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("RD_av", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("RDMedW", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("DemPublicI", ogr.OFTReal))
    
    fielddefmatrix.append(ogr.FieldDefn("HouseOccup", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("avSt_RES", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("WResNstrip", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("ResAllots", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("ResDWpLot", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("ResHouses", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("ResLotArea", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("ResRoof", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("avLt_RES", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("ResHFloors", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("ResLotTIA", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("ResLotEIA", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("ResGarden", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("DemPrivI", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("ResRoofCon", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("HDRFlats", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("HDRRoofA", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("HDROccup", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("HDR_TIA", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("HDR_EIA", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("HDRFloors", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("av_HDRes", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("HDRGarden", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("HDRCarPark", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("DemAptI", ogr.OFTReal))
    
    fielddefmatrix.append(ogr.FieldDefn("LIestates", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("avSt_LI", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("LIAfront", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("LIAfrEIA", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("LIAestate", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("LIAeBldg", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("LIFloors", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("LIAeLoad", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("LIAeCPark", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("avLt_LI", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("LIAeLgrey", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("LIAeEIA", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("LIAeTIA", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("LI_IDD", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("LI_OAD", ogr.OFTReal))
    
    fielddefmatrix.append(ogr.FieldDefn("HIestates", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("avSt_HI", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("HIAfront", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("HIAfrEIA", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("HIAestate", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("HIAeBldg", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("HIFloors", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("HIAeLoad", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("HIAeCPark", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("avLt_HI", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("HIAeLgrey", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("HIAeEIA", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("HIAeTIA", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("HI_IDD", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("HI_OAD", ogr.OFTReal))
    
    fielddefmatrix.append(ogr.FieldDefn("COMestates", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("avSt_COM", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("COMAfront", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("COMAfrEIA", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("COMAestate", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("COMAeBldg", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("COMFloors", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("COMAeLoad", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("COMAeCPark", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("avLt_COM", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("COMAeLgrey", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("COMAeEIA", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("COMAeTIA", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("COM_IDD", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("COM_OAD", ogr.OFTReal))
    
    fielddefmatrix.append(ogr.FieldDefn("ORCestates", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("avSt_ORC", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("ORCAfront", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("ORCAfrEIA", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("ORCAestate", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("ORCAeBldg", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("ORCFloors", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("ORCAeLoad", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("ORCAeCPark", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("avLt_ORC", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("ORCAeLgrey", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("ORCAeEIA", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("ORCAeTIA", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("ORC_IDD", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("ORC_OAD", ogr.OFTReal))
    
    fielddefmatrix.append(ogr.FieldDefn("Blk_TIA", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("Blk_EIA", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("Blk_EIF", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("Blk_TIF", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("Blk_RoofsA", ogr.OFTReal))
    
        #>>> FROM TECHPLACEMENT

    #Create the fields
    for field in fielddefmatrix:
        layer.CreateField(field)
        layer.GetLayerDefn()
    
    #Get Blocks View
    for i in range(len(assets)):
        currentAttList = assets[i]
        if currentAttList.getAttribute("Status") == 0:
            continue
        #Draw Geometry
        line = ogr.Geometry(ogr.wkbPolygon)
        ring = ogr.Geometry(ogr.wkbLinearRing)
        nl = currentAttList.getCoordinates()        #returns [(x, y, z), (x, y, z), (x, y, z), (x, y, z)]
        for point in nl:
            ring.AddPoint(point[0]+miscoptions[1], point[1]+miscoptions[2])     #x + offsetX, y + offsetY
        line.AddGeometry(ring)
        
        feature = ogr.Feature(layerDefinition)
        feature.SetGeometry(line)
        feature.SetFID(0)
        
        #Add Attributes
        feature.SetField("BlockID", int(currentAttList.getAttribute("BlockID")))
        feature.SetField("BasinID", int(currentAttList.getAttribute("BasinID")))
        feature.SetField("LocateX", currentAttList.getAttribute("LocateX"))
        feature.SetField("LocateY", currentAttList.getAttribute("LocateY"))
        feature.SetField("CentreX", currentAttList.getAttribute("CentreX"))
        feature.SetField("CentreY", currentAttList.getAttribute("CentreY"))
        feature.SetField("OriginX", currentAttList.getAttribute("OriginX"))
        feature.SetField("OriginY", currentAttList.getAttribute("OriginY"))            
        feature.SetField("Status", int(currentAttList.getAttribute("Status")))         
        feature.SetField("Active", currentAttList.getAttribute("Active"))            
        feature.SetField("Nhd_N", int(currentAttList.getAttribute("Nhd_N")))          
        feature.SetField("Nhd_S", int(currentAttList.getAttribute("Nhd_S")))          
        feature.SetField("Nhd_W", int(currentAttList.getAttribute("Nhd_W")))          
        feature.SetField("Nhd_E", int(currentAttList.getAttribute("Nhd_E")))          
        feature.SetField("Nhd_NE", int(currentAttList.getAttribute("Nhd_NE")))
        feature.SetField("Nhd_NW", int(currentAttList.getAttribute("Nhd_NW")))         
        feature.SetField("Nhd_SE", int(currentAttList.getAttribute("Nhd_SE")))         
        feature.SetField("Nhd_SW", int(currentAttList.getAttribute("Nhd_SW")))         
        feature.SetField("Soil_k", currentAttList.getAttribute("Soil_k"))            
        feature.SetField("AvgElev", currentAttList.getAttribute("AvgElev"))           
        feature.SetField("pLU_RES", currentAttList.getAttribute("pLU_RES"))
        feature.SetField("pLU_COM", currentAttList.getAttribute("pLU_COM"))
        feature.SetField("pLU_ORC", currentAttList.getAttribute("pLU_ORC"))
        feature.SetField("pLU_LI", currentAttList.getAttribute("pLU_LI")) 
        feature.SetField("pLU_HI", currentAttList.getAttribute("pLU_HI")) 
        feature.SetField("pLU_CIV", currentAttList.getAttribute("pLU_CIV"))
        feature.SetField("pLU_SVU", currentAttList.getAttribute("pLU_SVU"))
        feature.SetField("pLU_RD", currentAttList.getAttribute("pLU_RD")) 
        feature.SetField("pLU_TR", currentAttList.getAttribute("pLU_TR"))
        feature.SetField("pLU_PG", currentAttList.getAttribute("pLU_PG"))
        feature.SetField("pLU_REF", currentAttList.getAttribute("pLU_REF"))
        feature.SetField("pLU_UND", currentAttList.getAttribute("pLU_UND"))
        feature.SetField("pLU_NA", currentAttList.getAttribute("pLU_NA"))
        feature.SetField("Pop", currentAttList.getAttribute("Pop"))           
        
        if map_attr.getAttribute("include_employment"): feature.SetField("Employ", currentAttList.getAttribute("Employ")) 
        if map_attr.getAttribute("include_groundwater"): feature.SetField("GWDepth", currentAttList.getAttribute("GWDepth"))
        if map_attr.getAttribute("include_soc_par1"): feature.SetField("SocPar1", currentAttList.getAttribute("SocPar1"))
        if map_attr.getAttribute("include_soc_par2"): feature.SetField("SocPar2", currentAttList.getAttribute("SocPar2"))
        if map_attr.getAttribute("include_plan_map"): feature.SetField("PM_RES", currentAttList.getAttribute("PM_RES"))
        if map_attr.getAttribute("include_plan_map"): feature.SetField("PM_COM", currentAttList.getAttribute("PM_COM"))
        if map_attr.getAttribute("include_plan_map"): feature.SetField("PM_LI", currentAttList.getAttribute("PM_LI"))
        if map_attr.getAttribute("include_plan_map"): feature.SetField("PM_HI", currentAttList.getAttribute("PM_HI"))
        if map_attr.getAttribute("include_rivers"): feature.SetField("HasRiv", currentAttList.getAttribute("HasRiv"))
        if map_attr.getAttribute("include_lakes"): feature.SetField("HasLake", currentAttList.getAttribute("HasLake"))
        if map_attr.getAttribute("include_lakes"): feature.SetField("LakeAr", currentAttList.getAttribute("LakeAr"))
        if map_attr.getAttribute("include_local_map"): feature.SetField("HasLoc", currentAttList.getAttribute("HasLoc"))
        if map_attr.getAttribute("include_local_map"): feature.SetField("NFacil", currentAttList.getAttribute("NFacil"))
        if map_attr.getAttribute("patchdelin"): feature.SetField("Patches", currentAttList.getAttribute("Patches"))
        if map_attr.getAttribute("spatialmetrics"): feature.SetField("Rich", currentAttList.getAttribute("Rich"))            
        if map_attr.getAttribute("spatialmetrics"): feature.SetField("ShDIV", currentAttList.getAttribute("ShDIV"))           
        if map_attr.getAttribute("spatialmetrics"): feature.SetField("ShDOM", currentAttList.getAttribute("ShDOM"))          
        if map_attr.getAttribute("spatialmetrics"): feature.SetField("ShEVEN", currentAttList.getAttribute("ShEVEN"))          
        
        feature.SetField("downID", currentAttList.getAttribute("downID"))          
        feature.SetField("maxdZ", currentAttList.getAttribute("maxdZ"))           
        feature.SetField("slope", currentAttList.getAttribute("slope"))           
        feature.SetField("drainID", currentAttList.getAttribute("drainID"))         
        feature.SetField("h_pond", currentAttList.getAttribute("h_pond"))          
        feature.SetField("Outlet", int(currentAttList.getAttribute("Outlet")))

        if map_attr.getAttribute("considerCBD") : feature.SetField("CBDdist", currentAttList.getAttribute("CBDdist"))          
        if map_attr.getAttribute("considerCBD") : feature.SetField("CBDdir", currentAttList.getAttribute("CBDdir"))
        
        #From Urbplanbb
        feature.SetField("MiscAtot", currentAttList.getAttribute("MiscAtot").getDouble())
        feature.SetField("UndType", currentAttList.getAttribute("UndType").getString())
        feature.SetField("UND_av", currentAttList.getAttribute("UND_av").getDouble())
        feature.SetField("OpenSpace", currentAttList.getAttribute("OpenSpace").getDouble())
        feature.SetField("AGardens", currentAttList.getAttribute("AGardens").getDouble())
        feature.SetField("ASquare", currentAttList.getAttribute("ASquare").getDouble())
        feature.SetField("PG_av", currentAttList.getAttribute("PG_av").getDouble())
        feature.SetField("REF_av", currentAttList.getAttribute("REF_av").getDouble())
        feature.SetField("ANonW_Utils", currentAttList.getAttribute("ANonW_Utils").getDouble())
        feature.SetField("SVU_avWS", currentAttList.getAttribute("SVU_avWS").getDouble())
        feature.SetField("SVU_avWW", currentAttList.getAttribute("SVU_avWW").getDouble())
        feature.SetField("SVU_avSW", currentAttList.getAttribute("SVU_avSW").getDouble())
        feature.SetField("SVU_avOTH", currentAttList.getAttribute("SVU_avOTH").getDouble())
        feature.SetField("RoadTIA", currentAttList.getAttribute("RoadTIA").getDouble())
        feature.SetField("ParkBuffer", currentAttList.getAttribute("ParkBuffer").getDouble())
        feature.SetField("RD_av", currentAttList.getAttribute("RD_av").getDouble())
        feature.SetField("RDMedW", currentAttList.getAttribute("RDMedW").getDouble())
        feature.SetField("DemPublicI", currentAttList.getAttribute("DemPublicI").getDouble())
        
        feature.SetField("HouseOccup", currentAttList.getAttribute("HouseOccup").getDouble())
        feature.SetField("avSt_RES", currentAttList.getAttribute("avSt_RES").getDouble())
        feature.SetField("WResNstrip", currentAttList.getAttribute("WResNstrip").getDouble())
        feature.SetField("ResAllots", currentAttList.getAttribute("ResAllots").getDouble())
        feature.SetField("ResDWpLot", currentAttList.getAttribute("ResDWpLot").getDouble())
        feature.SetField("ResHouses", currentAttList.getAttribute("ResHouses").getDouble())
        feature.SetField("ResLotArea", currentAttList.getAttribute("ResLotArea").getDouble())
        feature.SetField("ResRoof", currentAttList.getAttribute("ResRoof").getDouble())
        feature.SetField("avLt_RES", currentAttList.getAttribute("avLt_RES").getDouble())
        feature.SetField("ResHFloors", currentAttList.getAttribute("ResHFloors").getDouble())
        feature.SetField("ResLotTIA", currentAttList.getAttribute("ResLotTIA").getDouble())
        feature.SetField("ResLotEIA", currentAttList.getAttribute("ResLotEIA").getDouble())
        feature.SetField("ResGarden", currentAttList.getAttribute("ResGarden").getDouble())
        feature.SetField("DemPrivI", currentAttList.getAttribute("DemPrivI").getDouble())
        feature.SetField("ResRoofCon", currentAttList.getAttribute("ResRoofCon").getDouble())
        feature.SetField("HDRFlats", currentAttList.getAttribute("HDRFlats").getDouble())
        feature.SetField("HDRRoofA", currentAttList.getAttribute("HDRRoofA").getDouble())
        feature.SetField("HDROccup", currentAttList.getAttribute("HDROccup").getDouble())
        feature.SetField("HDR_TIA", currentAttList.getAttribute("HDR_TIA").getDouble())
        feature.SetField("HDR_EIA", currentAttList.getAttribute("HDR_EIA").getDouble())
        feature.SetField("HDRFloors", currentAttList.getAttribute("HDRFloors").getDouble())
        feature.SetField("av_HDRes", currentAttList.getAttribute("av_HDRes").getDouble())
        feature.SetField("HDRGarden", currentAttList.getAttribute("HDRGarden").getDouble())
        feature.SetField("HDRCarPark", currentAttList.getAttribute("HDRCarPark").getDouble())
        feature.SetField("DemAptI", currentAttList.getAttribute("DemAptI").getDouble())
        
        feature.SetField("LIestates", currentAttList.getAttribute("LIestates").getDouble())
        feature.SetField("avSt_LI", currentAttList.getAttribute("avSt_LI").getDouble())
        feature.SetField("LIAfront", currentAttList.getAttribute("LIAfront").getDouble())
        feature.SetField("LIAfrEIA", currentAttList.getAttribute("LIAfrEIA").getDouble())
        feature.SetField("LIAestate", currentAttList.getAttribute("LIAestate").getDouble())
        feature.SetField("LIAeBldg", currentAttList.getAttribute("LIAeBldg").getDouble())
        feature.SetField("LIFloors", currentAttList.getAttribute("LIFloors").getDouble())
        feature.SetField("LIAeLoad", currentAttList.getAttribute("LIAeLoad").getDouble())
        feature.SetField("LIAeCPark", currentAttList.getAttribute("LIAeCPark").getDouble())
        feature.SetField("avLt_LI", currentAttList.getAttribute("avLt_LI").getDouble())
        feature.SetField("LIAeLgrey", currentAttList.getAttribute("LIAeLgrey").getDouble())
        feature.SetField("LIAeEIA", currentAttList.getAttribute("LIAeEIA").getDouble())
        feature.SetField("LIAeTIA", currentAttList.getAttribute("LIAeTIA").getDouble())
        feature.SetField("LI_IDD", currentAttList.getAttribute("LI_IDD").getDouble())
        feature.SetField("LI_OAD", currentAttList.getAttribute("LI_OAD").getDouble())
        
        feature.SetField("HIestates", currentAttList.getAttribute("HIestates").getDouble())
        feature.SetField("avSt_HI", currentAttList.getAttribute("avSt_HI").getDouble())
        feature.SetField("HIAfront", currentAttList.getAttribute("HIAfront").getDouble())
        feature.SetField("HIAfrEIA", currentAttList.getAttribute("HIAfrEIA").getDouble())
        feature.SetField("HIAestate", currentAttList.getAttribute("HIAestate").getDouble())
        feature.SetField("HIAeBldg", currentAttList.getAttribute("HIAeBldg").getDouble())
        feature.SetField("HIFloors", currentAttList.getAttribute("HIFloors").getDouble())
        feature.SetField("HIAeLoad", currentAttList.getAttribute("HIAeLoad").getDouble())
        feature.SetField("HIAeCPark", currentAttList.getAttribute("HIAeCPark").getDouble())
        feature.SetField("avLt_HI", currentAttList.getAttribute("avLt_HI").getDouble())
        feature.SetField("HIAeLgrey", currentAttList.getAttribute("HIAeLgrey").getDouble())
        feature.SetField("HIAeEIA", currentAttList.getAttribute("HIAeEIA").getDouble())
        feature.SetField("HIAeTIA", currentAttList.getAttribute("HIAeTIA").getDouble())
        feature.SetField("HI_IDD", currentAttList.getAttribute("HI_IDD").getDouble())
        feature.SetField("HI_OAD", currentAttList.getAttribute("HI_OAD").getDouble())
        
        feature.SetField("COMestates", currentAttList.getAttribute("COMestates"))
        feature.SetField("avSt_COM", currentAttList.getAttribute("avSt_COM"))
        feature.SetField("COMAfront", currentAttList.getAttribute("COMAfront"))
        feature.SetField("COMAfrEIA", currentAttList.getAttribute("COMAfrEIA"))
        feature.SetField("COMAestate", currentAttList.getAttribute("COMAestate"))
        feature.SetField("COMAeBldg", currentAttList.getAttribute("COMAeBldg"))
        feature.SetField("COMFloors", currentAttList.getAttribute("COMFloors"))
        feature.SetField("COMAeLoad", currentAttList.getAttribute("COMAeLoad"))
        feature.SetField("COMAeCPark", currentAttList.getAttribute("COMAeCPark"))
        feature.SetField("avLt_COM", currentAttList.getAttribute("avLt_COM"))
        feature.SetField("COMAeLgrey", currentAttList.getAttribute("COMAeLgrey"))
        feature.SetField("COMAeEIA", currentAttList.getAttribute("COMAeEIA"))
        feature.SetField("COMAeTIA", currentAttList.getAttribute("COMAeTIA"))
        feature.SetField("COM_IDD", currentAttList.getAttribute("COM_IDD"))
        feature.SetField("COM_OAD", currentAttList.getAttribute("COM_OAD"))
        
        feature.SetField("ORCestates", currentAttList.getAttribute("ORCestates"))
        feature.SetField("avSt_ORC", currentAttList.getAttribute("avSt_ORC"))
        feature.SetField("ORCAfront", currentAttList.getAttribute("ORCAfront"))
        feature.SetField("ORCAfrEIA", currentAttList.getAttribute("ORCAfrEIA"))
        feature.SetField("ORCAestate", currentAttList.getAttribute("ORCAestate"))
        feature.SetField("ORCAeBldg", currentAttList.getAttribute("ORCAeBldg"))
        feature.SetField("ORCFloors", currentAttList.getAttribute("ORCFloors"))
        feature.SetField("ORCAeLoad", currentAttList.getAttribute("ORCAeLoad"))
        feature.SetField("ORCAeCPark", currentAttList.getAttribute("ORCAeCPark"))
        feature.SetField("avLt_ORC", currentAttList.getAttribute("avLt_ORC"))
        feature.SetField("ORCAeLgrey", currentAttList.getAttribute("ORCAeLgrey"))
        feature.SetField("ORCAeEIA", currentAttList.getAttribute("ORCAeEIA"))
        feature.SetField("ORCAeTIA", currentAttList.getAttribute("ORCAeTIA"))
        feature.SetField("ORC_IDD", currentAttList.getAttribute("ORC_IDD"))
        feature.SetField("ORC_OAD", currentAttList.getAttribute("ORC_OAD"))
        
        feature.SetField("Blk_TIA", currentAttList.getAttribute("Blk_TIA"))
        feature.SetField("Blk_EIA", currentAttList.getAttribute("Blk_EIA"))
        feature.SetField("Blk_EIF", currentAttList.getAttribute("Blk_EIF"))
        feature.SetField("Blk_TIF", currentAttList.getAttribute("Blk_TIF"))
        feature.SetField("Blk_RoofsA", currentAttList.getAttribute("Blk_RoofsA"))
                
        layer.CreateFeature(feature)
    
    shapefile.Destroy()
    
    if kmlbool:
        convertSHPtoKML(str(filename)+"_Blocks")
    
    return True

def exportPatchData(filename, assets, miscoptions, map_attr):
    if map_attr.getAttribute("patchdelin") == 0:
        return True
    
    spatialRef = osr.SpatialReference()                #Define Spatial Reference
    spatialRef.ImportFromProj4(miscoptions[0])
    
    driver = ogr.GetDriverByName('ESRI Shapefile')
    if os.path.exists(str(filename)+"_Patches.shp"): os.remove(str(filename)+"_Patches.shp")
    shapefile = driver.CreateDataSource(str(filename)+"_Patches.shp")
    
    layer = shapefile.CreateLayer('layer1', spatialRef, ogr.wkbPolygon)
    layerDefinition = layer.GetLayerDefn()
    
    #DEFINE ATTRIBUTES
    fielddefmatrix = []
    fielddefmatrix.append(ogr.FieldDefn("LandUse", ogr.OFTInteger))
    fielddefmatrix.append(ogr.FieldDefn("Area", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("AvgElev", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("SoilK", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("BlockID", ogr.OFTInteger))
    
    #Create the fields
    for field in fielddefmatrix:
        layer.CreateField(field)
        layer.GetLayerDefn()
    
    #Get Blocks View
    for i in range(len(assets)):
        currentAttList = assets[i]
    
        #Draw Geometry
        line = ogr.Geometry(ogr.wkbPolygon)
        ring = ogr.Geometry(ogr.wkbLinearRing)
        nl = currentAttList.getCoordinates()
        for point in nl:
            ring.AddPoint(point[0]+miscoptions[1], point[1]+miscoptions[2])
        line.AddGeometry(ring)
        
        feature = ogr.Feature(layerDefinition)
        feature.SetGeometry(line)
        feature.SetFID(0)
        
        #Add Attributes
        feature.SetField("LandUse", int(currentAttList.getAttribute("LandUse")))
        feature.SetField("Area", currentAttList.getAttribute("Area"))
        feature.SetField("AvgElev", currentAttList.getAttribute("AvgElev"))
        feature.SetField("SoilK", currentAttList.getAttribute("SoilK"))
        feature.SetField("BlockID", int(currentAttList.getAttribute("BlockID")))
    
        layer.CreateFeature(feature)
    
    shapefile.Destroy()
    return True

def exportFlowPaths(filename, assets, miscoptions, map_attr, kmlbool):
    spatialRef = osr.SpatialReference()                #Define Spatial Reference
    spatialRef.ImportFromProj4(miscoptions[0])
    
    driver = ogr.GetDriverByName('ESRI Shapefile')
    if os.path.exists(str(filename)+"_Network.shp"): os.remove(str(filename)+"_Network.shp")
    shapefile = driver.CreateDataSource(str(filename)+"_Network.shp")
    
    layer = shapefile.CreateLayer('layer1', spatialRef, ogr.wkbLineString)
    layerDefinition = layer.GetLayerDefn()
    
    #DEFINE ATTRIBUTES
    fielddefmatrix = []
    fielddefmatrix.append(ogr.FieldDefn("BlockID", ogr.OFTInteger))
    fielddefmatrix.append(ogr.FieldDefn("DownID", ogr.OFTInteger))
    fielddefmatrix.append(ogr.FieldDefn("Z_up", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("Z_down", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("max_Zdrop", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("Type", ogr.OFTInteger))
    fielddefmatrix.append(ogr.FieldDefn("avg_slope", ogr.OFTReal))
    
    #Create the fields
    for field in fielddefmatrix:
        layer.CreateField(field)
        layer.GetLayerDefn()
    
    #Get Blocks View
    for i in range(len(assets)):
        currentAttList = assets[i]
    
        #Draw Geometry
        line = ogr.Geometry(ogr.wkbLineString)
        p1 = currentAttList.getCoordinates()[0]
        p2 = currentAttList.getCoordinates()[1]
        
        line.AddPoint(p1[0] + miscoptions[1], p1[1] + miscoptions[2])
        line.AddPoint(p2[0] + miscoptions[1], p2[1] + miscoptions[2])
        
        feature = ogr.Feature(layerDefinition)
        feature.SetGeometry(line)
        feature.SetFID(0)
        
        #Add Attributes
        feature.SetField("BlockID", int(currentAttList.getAttribute("BlockID")))
        feature.SetField("DownID", int(currentAttList.getAttribute("DownID")))
        feature.SetField("Z_up", currentAttList.getAttribute("Z_up"))
        feature.SetField("Z_down", currentAttList.getAttribute("Z_down"))
        feature.SetField("max_Zdrop", currentAttList.getAttribute("max_Zdrop"))
        feature.SetField("Type", int(currentAttList.getAttribute("Type")))
        feature.SetField("avg_slope", currentAttList.getAttribute("avg_slope"))
    
        layer.CreateFeature(feature)
    
    shapefile.Destroy()
    
    if kmlbool:
        convertSHPtoKML(str(filename)+"_Network")
    
    return True

def exportBlockLocalities(filename, assets, miscoptions, map_attr):
    
    spatialRef = osr.SpatialReference()                #Define Spatial Reference
    spatialRef.ImportFromProj4(miscoptions[0])
    
    driver = ogr.GetDriverByName('ESRI Shapefile')
    if os.path.exists(str(filename)+"_Localities.shp"): os.remove(str(filename)+"_Localities.shp")
    shapefile = driver.CreateDataSource(str(filename)+"_Localities.shp")
    
    layer = shapefile.CreateLayer('layer1', spatialRef, ogr.wkbPoint)
    layerDefinition = layer.GetLayerDefn()
    
    #DEFINE ATTRIBUTES
    fielddefmatrix = []
    fielddefmatrix.append(ogr.FieldDefn("BlockID", ogr.OFTInteger))
    fielddefmatrix.append(ogr.FieldDefn("Type", ogr.OFTString))
    fielddefmatrix.append(ogr.FieldDefn("Area", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("TIF", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("ARoof", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("AvgWD", ogr.OFTReal))
    
    #Create the fields
    for field in fielddefmatrix:
        layer.CreateField(field)
        layer.GetLayerDefn()
    
    #Get Blocks View
    for i in range(len(assets)):
        currentAttList = assets[i]
    
        #Draw Geometry
        point = ogr.Geometry(ogr.wkbPoint)
        point.SetPoint(0, currentAttList.getCoordinates()[0][0] + miscoptions[1], currentAttList.getCoordinates()[0][1] + miscoptions[2])
        
        feature = ogr.Feature(layerDefinition)
        feature.SetGeometry(point)
        feature.SetFID(0)
        
        #Add Attributes
        feature.SetField("BlockID", int(currentAttList.getAttribute("BlockID")))
        feature.SetField("Type", currentAttList.getAttribute("Type"))
        feature.SetField("Area", currentAttList.getAttribute("Area"))
        feature.SetField("Area", currentAttList.getAttribute("TIF"))
        feature.SetField("Area", currentAttList.getAttribute("ARoof"))
        feature.SetField("Area", currentAttList.getAttribute("AvgWD"))
        layer.CreateFeature(feature)
    
    shapefile.Destroy()
    return True

def exportPlannedWSUD(filename, assets, miscoptions, map_attr, kmlbool):
    return True


def exportImplementWSUD(filename, assets, miscoptions, map_attr, kmlbool):
    return True

def exportBlockCentre(filename, assets, miscoptions, map_attr, kmlbool):
    
    spatialRef = osr.SpatialReference()                #Define Spatial Reference
    spatialRef.ImportFromProj4(miscoptions[0])
    
    driver = ogr.GetDriverByName('ESRI Shapefile')
    if os.path.exists(str(filename)+"_CentrePoints.shp"): os.remove(str(filename)+"_CentrePoints.shp")
    shapefile = driver.CreateDataSource(str(filename)+"_CentrePoints.shp")
    
    layer = shapefile.CreateLayer('layer1', spatialRef, ogr.wkbPoint)
    layerDefinition = layer.GetLayerDefn()
    
    #DEFINE ATTRIBUTES
    fielddefmatrix = []
    fielddefmatrix.append(ogr.FieldDefn("BlockID", ogr.OFTInteger))
    fielddefmatrix.append(ogr.FieldDefn("AvgElev", ogr.OFTReal))
    fielddefmatrix.append(ogr.FieldDefn("Type", ogr.OFTString))
    
    #Create the fields
    for field in fielddefmatrix:
        layer.CreateField(field)
        layer.GetLayerDefn()
    
    #Get Blocks View
    for i in range(len(assets)):
        currentAttList = assets[i]
    
        #Draw Geometry
        point = ogr.Geometry(ogr.wkbPoint)
        point.SetPoint(0, currentAttList.getCoordinates()[0][0] + miscoptions[1], currentAttList.getCoordinates()[0][1] + miscoptions[2])
        
        feature = ogr.Feature(layerDefinition)
        feature.SetGeometry(point)
        feature.SetFID(0)
        
        #Add Attributes
        feature.SetField("BlockID", int(currentAttList.getAttribute("BlockID")))
        feature.SetField("AvgElev", currentAttList.getAttribute("AvgElev"))
        feature.SetField("Type", currentAttList.getAttribute("Type"))
        layer.CreateFeature(feature)
    
    shapefile.Destroy()
    return True

def convertSHPtoKML(filename):
    output_filename = str(filename)+"KML"
    input_filename = filename
    ogr2ogr.main(["", "-f", "KML", str(output_filename)+".kml", str(input_filename)+".shp"])
    return True
    

### DATA CLASSES

class RasterData(object):
    def __init__(self, cols, rows, xc, yc, cs, ndv):
        self.__ncols = cols
        self.__nrows = rows
        self.__xllcorner = xc
        self.__yllcorner = yc
        self.__cellsize = cs
        self.__nodatavalue = ndv
        self.__data = []
    
    def setData(self, data):
        #Adds the info to the data matrix so that x and y cells can be called up
        #flips the raster data matrix at the same time
        currentrow = self.__nrows - 1   #must count backwards
        while currentrow >= 0:
            row = data[currentrow]
            for i in range(len(row)):
                row[i] = float(row[i])
            self.__data.append(row)
            currentrow -= 1
        return True

    def getValue(self, col, row):
        #Returns the cells value of the given column (x) and row (y)
        try:        
            return self.__data[row][col]        #data[y][x]
        except IndexError:
            return self.__nodatavalue
    
    def getDimensions(self):
        #Returns a vector or [x,y] number of columns, number of rows
        return [self.__ncols, self.__nrows]
    
    def getExtents(self):
        #Returns a vector of the [x,y] extents of the raster data file
        return [self.__xllcorner, self.__yllcorner]
    
    def getCellSize(self):
        #Returns the cell size of the raster data
        return self.__cellsize
    
    def resetData(self):
        #Erases the data matrix (to free up memory)
        self.__data = []
        return True
        
class UBComponent(object):
    def __init__(self):
        self.__attributes = {}
    
    def addAttribute(self, name, value):
        self.__attributes[name] = value
        return True

    def setAttribute(self, name, value):
        if self.__attributes[name]:
            self.__attributes[name] = value
        else:
            print "WARNING NO ATTTRIBUTE NAMED: "+str(name)
        return True
    
    def getAttribute(self, name):
        try:
            return self.__attributes[name]
        except KeyError:
            #print "Error, no such attribute, "+str(name)+". returning zero"
            return 0
    
class UBVector(UBComponent):
    def __init__(self, coordinates):
        UBComponent.__init__(self)        
        self.__dtype = ""
        self.__coordinates = coordinates
        self.determineGeometry(self.__coordinates)
    
    def changeCoordinates(self, coordinates):
        currentgeometry = self.__dtype
        self.__coordinates = coordinates
        self.determineGeometry(self.__coordinates)
        if currentgeometry != self.__dtype:
            print "WARNING: GEOMETRY TYPE HAS CHANGED!"
        return True
    
    def getCoordinates(self):
        """Returns an array of points (tuples), each having (x, y, z) sets of 
        coordinates"""
        return self.__coordinates
    
    def determineGeometry(self, coordinates):
        if len(coordinates) == 1:
            self.__dtype = "POINT"
        elif len(coordinates) == 2:
            self.__dtype = "LINE"
        elif len(coordinates) > 2:
            if coordinates[0] == coordinates[len(coordinates)-1]:
                self.__dtype = "FACE"
            else:
                self.__dtype = "POLYLINE"
        return True

class UBCollection(object):
    def __init__(self):
        self.__assetcount = 0
        self.__assets = []
    
    def appendAsset(self, asset):
        self.__assets.append(asset)
        return True
    
    def getAssetByAttribute(self, asset, attribute, value):
        return True


        