# -*- coding: utf-8 -*-
"""
@file
@author  Peter M Bach <peterbach@gmail.com>
@version 1.0
@section LICENSE

This file is part of daCapo v1 and UrbanBEATS v1 (www.urbanbeatsmodel.com)
Copyright (C) 2013  Peter M Bach, Cintia Dotto
MUSIC is licensed by eWater

"""
__author__ = 'Peter M Bach'

#Python Libraries
import numpy as np

#Other Software-related imports

MUSIC_VERSION = 6

def setMUSICversion(version_no):
    MUSIC_VERSION = int(version_no)
    return True

def createMUSICmcf(path, name):
    g = open(str(path)+"/"+str(name)+".mcf", 'w')
    return g

def writeMUSICmcfHeader(g):
    g.write("Version=100\n")
    g.write("Delimiter = #44\n")

def writeMUSICmcfExportLines(g, nodedb):
    for i in nodedb.keys():
        if nodedb[i][0] != "catchment":
            g.write('Export_TTE ('+str(i)+',"'+str(nodedb[i][1])+'.txt")\n')

def writeMUSICmcfFooter(g):
    g.close()

def writeMUSICbatfile(path, name, musicpath, msfname, mcfname):
    f = open(str(path)+"/"+str(name)+".bat", 'w')
    f.write('"'+str(musicpath)+'" "'+str(msfname)+'.msf" "'+str(mcfname)+'.mcf" -light -silent')
    f.close()

def createMUSICmsf(path, name):
    f = open(str(path)+"/"+str(name)+".msf", 'w')
    return f

def writeMUSICheader(f, climatepath):
    path = climatepath
    f.write("====================================================================================\n")
    f.write("DESCRIPTION\n")
    f.write("daCapo MUSIC File Input\n")
    f.write("====================================================================================\n")
    if MUSIC_VERSION == 6:
        f.write("VersionNumber,204,{MUSIC Setup File version number}\n")
    if MUSIC_VERSION == 5:
        f.write("VersionNumber,200,{MUSIC Setup File version number}\n")
    f.write("------------------------------------------------------------------------------------\n")
    f.write("MeteorologicalTemplate,"+path+",{MLB Filename}\n")
    if MUSIC_VERSION == 6:
        f.write("------------------------------------------------------------------------------------\n")
        f.write("ConstituentAbbreviation,TSS,{Constituent Abbreviation}\n")
        f.write("------------------------------------------------------------------------------------\n")
        f.write("ConstituentName,Total Suspended Solids,{Constituent Name}\n")
        f.write("------------------------------------------------------------------------------------\n")
        f.write("MUSIC-link Project - Enabled,1,{0 = enabled | 1 = disabled}\n")
        f.write("MUSIC-link - Music Version,,{The music version this was created with} \n")
        f.write("MUSIC-link - Metadata Version,,{The version of the metadata used}\n")
        f.write("MUSIC-link - Council Name,,{The name of the council}\n")
        f.write("MUSIC-link - Area Name,,{The name of the audit area}\n")
        f.write("MUSIC-link - Scenario Name,,{The name of the audit scenario}\n")
    f.write("====================================================================================\n")
    return True

def writeMUSICcatchmentnode(f, ID, nodepart, ncount, x, y, parameter_list):
    #f = filename variables, ID = block ID, nodepart = lot/street/treat/untreat x = x-coordinate of block, y = y-coordinate of block
    f.write("Node Type,UrbanSourceNode,{Node Type}\n")
    f.write("Node Name,BlockID"+str(ID)+str(nodepart)+",{Node Name}\n")
    f.write("Node ID,"+str(ncount)+",{Node ID}\n")
    f.write("Coordinates,"+str(x)+":"+str(y)+",{Coordinates}{X:Y}\n")
    f.write("General - Location,BlockID"+str(ID)+str(nodepart)+",\n")
    f.write("General - Notes,,\n")
    f.write("General - Fluxes - Daily,,\n")
    f.write("General - Fluxes - Sub-Daily,,\n")
    if MUSIC_VERSION == 6:
        f.write("General - Flux unit,mm,\n")
    f.write("Areas - Total Area (ha),"+str(parameter_list["area"])+",{ha}\n")
    f.write("Areas - Impervious (%),"+str(parameter_list["impervious"])+",{%}\n")
    f.write("Areas - Pervious (%),"+str(parameter_list["pervious"])+",{%}\n")
    f.write("Rainfall-Runoff - Impervious Area - Rainfall Threshold (mm/day),"+str(parameter_list["rain_thresh"])+",{mm/day}\n")
    f.write("Rainfall-Runoff - Pervious Area - Soil Storage Capacity (mm),"+str(parameter_list["soil_store_cap"])+",{mm}\n")
    f.write("Rainfall-Runoff - Pervious Area - Initial Storage (% of Capacity),"+str(parameter_list["initial_soil"])+",{% of Capacity}\n")
    f.write("Rainfall-Runoff - Pervious Area - Field Capacity (mm),"+str(parameter_list["field_cap"])+",{mm}\n")
    f.write("Rainfall-Runoff - Pervious Area - Infiltration Capacity Coefficient - a,"+str(parameter_list["infil_a"])+",\n")
    f.write("Rainfall-Runoff - Pervious Area - Infiltration Capacity Exponent - b,"+str(parameter_list["infil_b"])+",\n")
    f.write("Rainfall-Runoff - Groundwater Properties - Initial Depth (mm),"+str(parameter_list["gw_init"])+",{mm}\n")
    f.write("Rainfall-Runoff - Groundwater Properties - Daily Recharge Rate (%),"+str(parameter_list["gw_recharge"])+",{%}\n")
    f.write("Rainfall-Runoff - Groundwater Properties - Daily Baseflow Rate (%),"+str(parameter_list["gw_base"])+",{%}\n")
    f.write("Rainfall-Runoff - Groundwater Properties - Daily Deep Seepage Rate (%),"+str(parameter_list["gw_deep"])+",{%}\n")
    f.write("Total Suspended Solids - Base Flow Concentration - Mean (log mg/L),"+str(parameter_list["TSS_base_m"])+",{log mg/L}\n")
    f.write("Total Suspended Solids - Base Flow Concentration - Std Dev (log mg/L),"+str(parameter_list["TSS_base_s"])+",{log mg/L}\n")
    f.write("Total Suspended Solids - Base Flow Concentration - Estimation Method,"+str(parameter_list["pollute_estimate"])+",{Index from 0 to 1 for \"Mean\" | \"Stochastically generated\"}\n")
    f.write("Total Suspended Solids - Base Flow Concentration - Serial Correlation (R squared),"+str(parameter_list["pollut_correl"])+",{R squared}\n")
    f.write("Total Suspended Solids - Storm Flow Concentration - Mean (log mg/L),"+str(parameter_list["TSS_storm_m"])+",{log mg/L}\n")
    f.write("Total Suspended Solids - Storm Flow Concentration - Std Dev (log mg/L),"+str(parameter_list["TSS_storm_s"])+",{log mg/L}\n")
    f.write("Total Suspended Solids - Storm Flow Concentration - Estimation Method,"+str(parameter_list["pollute_estimate"])+",{Index from 0 to 1 for \"Mean\" | \"Stochastically generated\"}\n")
    f.write("Total Suspended Solids - Storm Flow Concentration - Serial Correlation (R squared),"+str(parameter_list["pollut_correl"])+",{R squared}\n")
    f.write("Total Phosphorus - Base Flow Concentration - Mean (log mg/L),"+str(parameter_list["TP_base_m"])+",{log mg/L}\n")
    f.write("Total Phosphorus - Base Flow Concentration - Std Dev (log mg/L),"+str(parameter_list["TP_base_s"])+",{log mg/L}\n")
    f.write("Total Phosphorus - Base Flow Concentration - Estimation Method,"+str(parameter_list["pollute_estimate"])+",{Index from 0 to 1 for \"Mean\" | \"Stochastically generated\"}\n")
    f.write("Total Phosphorus - Base Flow Concentration - Serial Correlation (R squared),"+str(parameter_list["pollut_correl"])+",{R squared}\n")
    f.write("Total Phosphorus - Storm Flow Concentration - Mean (log mg/L),"+str(parameter_list["TP_storm_m"])+",{log mg/L}\n")
    f.write("Total Phosphorus - Storm Flow Concentration - Std Dev (log mg/L),"+str(parameter_list["TP_storm_s"])+",{log mg/L}\n")
    f.write("Total Phosphorus - Storm Flow Concentration - Estimation Method,"+str(parameter_list["pollute_estimate"])+",{Index from 0 to 1 for \"Mean\" | \"Stochastically generated\"}\n")
    f.write("Total Phosphorus - Storm Flow Concentration - Serial Correlation (R squared),"+str(parameter_list["pollut_correl"])+",{R squared}\n")
    f.write("Total Nitrogen - Base Flow Concentration - Mean (log mg/L),"+str(parameter_list["TN_base_m"])+",{log mg/L}\n")
    f.write("Total Nitrogen - Base Flow Concentration - Std Dev (log mg/L),"+str(parameter_list["TN_base_s"])+",{log mg/L}\n")
    f.write("Total Nitrogen - Base Flow Concentration - Estimation Method,"+str(parameter_list["pollute_estimate"])+",{Index from 0 to 1 for \"Mean\" | \"Stochastically generated\"}\n")
    f.write("Total Nitrogen - Base Flow Concentration - Serial Correlation (R squared),"+str(parameter_list["pollut_correl"])+",{R squared}\n")
    f.write("Total Nitrogen - Storm Flow Concentration - Mean (log mg/L),"+str(parameter_list["TN_storm_m"])+",{log mg/L}\n")
    f.write("Total Nitrogen - Storm Flow Concentration - Std Dev (log mg/L),"+str(parameter_list["TN_storm_s"])+",{log mg/L}\n")
    f.write("Total Nitrogen - Storm Flow Concentration - Estimation Method,"+str(parameter_list["pollute_estimate"])+",{Index from 0 to 1 for \"Mean\" | \"Stochastically generated\"}\n")
    f.write("Total Nitrogen - Storm Flow Concentration - Serial Correlation (R squared),"+str(parameter_list["pollut_correl"])+",{R squared}\n")
    if MUSIC_VERSION == 6:
        f.write("Import Flow Properties - Import Flow Enabled,1,\n")
        f.write("Import Flow Properties - Import Flow File,,\n")
        f.write("Import Flow Properties - Header lines,0,\n")
        f.write("Import Flow Properties - Baseflow Column,0,\n")
        f.write("Import Flow Properties - Impervious Stormflow Column,0,\n")
        f.write("Import Flow Properties - Pervious Stormflow Column,0,\n")
        f.write('Import Flow Properties - Unit,5,{Index from 0 to 14 for "ML" | "kL" | "L" | "mL" | "ML/s" | "m3/s" | "L/s" | "mL/s" | "ML/day" | "kL/day" | "L/day" | "mL/day" | "km" | "m" | "mm"}\n')
        f.write("Import Flow Properties - Catchment Area for GP (ha),1,{ha}\n")
    f.write("------------------------------------------------------------------------------------\n")
    return True

def writeMUSICnodeBF(f, ID, nodename, ncount, x, y, surfarea, exfil, edd, fd, subzone, bf_params):
    #Calculate unlined filter media perimeter
    bf_width = np.sqrt(surfarea/bf_params["aspectratio"])
    bf_length = surfarea/bf_width
    unlined_perim = 2*bf_width + 2*bf_length

    if exfil == 0:
        lined = 0   #YES = 0
    else:
        lined = 1   #NO = 1

    if bf_params["underdrain"] == 0:
        udrain = 1
    else:
        udrain = 0

    f.write("Node Type,BioRetentionNodeV4,{Node Type}\n")
    f.write("Node Name,"+str(nodename)+",{Node Name}\n")
    f.write("Node ID,"+str(ncount)+",{Node ID}\n")
    f.write("Coordinates,"+str(x)+":"+str(y)+",{Coordinates}{X:Y}\n")
    f.write("General - Location,BF"+str(nodename)+",\n")
    f.write("General - Notes,,\n")
    f.write("General - Fluxes,,\n")
    if MUSIC_VERSION == 6:
        f.write("General - Flux File Timestep (in seconds),360,{in seconds}\n")
    f.write("Inlet Properties - Low Flow By-pass (cubic metres per sec),"+str(bf_params["lowbypass"])+",{cubic metres per sec}\n")
    f.write("Inlet Properties - High Flow By-pass (cubic metres per sec),"+str(bf_params["highbypass"])+",{cubic metres per sec}\n")
    f.write("Storage Properties - Extended Detention Depth (metres),"+str(edd)+",{metres}\n")
    f.write("Storage Properties - Surface Area (square metres),"+str(surfarea)+",{square metres}\n")
    f.write("Filter and Media Properties - Filter Area (square metres),"+str(surfarea)+",{square metres}\n")
    f.write("Filter and Media Properties - Unlined Filter Media Perimeter (metres),"+str(unlined_perim)+",{metres}\n")
    f.write("Filter and Media Properties - Saturated Hydraulic Conductivity (mm/hr),"+str(bf_params["ksat"])+",{mm/hr}\n")
    f.write("Filter and Media Properties - Filter Depth (metres),"+str(fd)+",{metres}\n")
    f.write("Filter and Media Properties - TN Content of Filter Media (mg/kg),"+str(bf_params["TNcontent"])+",{mg/kg}\n")
    f.write("Filter and Media Properties - Orthophosphate Content of Filter Media (mg/kg),"+str(bf_params["orthophos"])+",{mg/kg}\n")
    f.write("Infiltration Properties - Exfiltration Rate (mm/hr),"+str(exfil)+",{mm/hr}\n")
    f.write("Lining Properties - Base Lined,"+str(int(lined))+",\n")  #0 = YES, 1 = NO - what the hell illogical....!!
    f.write("Vegetation Properties - Vegetation Properties,"+str(bf_params["vegetation"])+",{Index from 0 to 2 for \"Vegetated with Effective Nutrient Removal Plants\" | \"Vegetated with Ineffective Nutrient Removal Plants\" | \"Unvegetated\"}\n")
    f.write("Outlet Properties - Overflow Weir Width (metres),"+str(bf_params["weirwidth"])+",{metres}\n")
    f.write("Outlet Properties - Underdrain Present,"+str(udrain)+",\n")
    f.write("Outlet Properties - Submerged Zone With Carbon Present,0,\n")
    f.write("Outlet Properties - Submerged Zone Depth (metres),"+str(subzone)+",{metres}\n")
    f.write("Advanced Properties - Total Suspended Solids - k (m/yr),8000,{m/yr}\n")
    f.write("Advanced Properties - Total Suspended Solids - C* (mg/L),20,{mg/L}\n")
    f.write("Advanced Properties - Total Phosphorus - k (m/yr),6000,{m/yr}\n")
    f.write("Advanced Properties - Total Phosphorus - C* (mg/L),0.13,{mg/L}\n")
    f.write("Advanced Properties - Total Nitrogen - k (m/yr),500,{m/yr}\n")
    f.write("Advanced Properties - Total Nitrogen - C* (mg/L),1.4,{mg/L}\n")
    f.write("Advanced Properties - Filter Media Soil Type,1,{Index from 0 to 4 for \"Sand\" | \"Loamy Sand\" | \"Sandy Loam\" | \"Silt Loam\" | \"Loam\"}\n")
    f.write("Advanced Properties - Weir Coefficient,1.7,\n")
    f.write("Advanced Properties - Pet Scaling Factor,2.1,\n")
    f.write("Advanced Properties - Number of CSTR Cells,3,\n")
    f.write("Advanced Properties - Porosity of Filter Media,0.35,\n")
    f.write("Advanced Properties - Porosity of Submerged Zone,0.35,\n")
    f.write("Advanced Properties - Horizontal Flow Coefficient,3,\n")
    f.write("------------------------------------------------------------------------------------\n")
    return True

def writeMUSICnodeWSUR(f, ID, nodename, ncount, x, y, surfarea, exfil, edd, wsur_params):
    f.write("Node Type,WetlandNode,{Node Type}\n")
    f.write("Node Name,"+str(nodename)+",{Node Name}\n")
    f.write("Node ID,"+str(ncount)+",{Node ID}\n")
    f.write("Coordinates,"+str(x)+":"+str(y)+",{Coordinates}{X:Y}\n")
    f.write("General - Location,WSUR"+str(nodename)+",\n")
    f.write("General - Notes,,\n")
    f.write("General - Fluxes,,\n")
    if MUSIC_VERSION == 6:
        f.write("General - Flux File Timestep (in seconds),360,{in seconds}\n")
    f.write("Reuse Properties - Reuse Enabled,1,\n")
    f.write("Reuse Properties - Annual Demand Enabled,1,\n")
    f.write("Reuse Properties - Annual Demand Value (ML/year),0,{ML/year}\n")
    f.write("Reuse Properties - Annual Demand Distribution,0,{Index from 0 to 2 for \"PET\" | \"PET - Rain\" | \"Monthly\"}\n")
    f.write("Reuse Properties - Monthly Distribution Values,8.33;8.33;8.33;8.33;8.33;8.33;8.33;8.33;8.33;8.33;8.33;8.33,\n")
    f.write("Reuse Properties - Daily Demand Enabled,1,\n")
    f.write("Reuse Properties - Daily Demand Value (ML/day),0,{ML/day}\n")
    f.write("Reuse Properties - Custom Demand Enabled,1,\n")
    f.write("Reuse Properties - Custom Demand Time Series File,,\n")
    f.write("Reuse Properties - Custom Demand Time Series Units,5,{Index from 0 to 11 for \"ML\" | \"kL\" | \"L\" | \"mL\" | \"ML/s\" | \"m3/s\" | \"L/s\" | \"mL/s\" | \"ML/day\" | \"kL/day\" | \"L/day\" | \"mL/day\"}\n")
    f.write("Reuse Properties - Minimum Draw down height,0,\n")
    f.write("Inlet Properties - Low Flow By-pass (cubic metres per sec),"+str(wsur_params[""])+",{cubic metres per sec}\n")
    f.write("Inlet Properties - High Flow By-pass (cubic metres per sec),"+str(wsur_params[""])+",{cubic metres per sec}\n")
    f.write("Inlet Properties - Inlet Pond Volume (cubic metres),"+str(wsur_params[""])+",{cubic metres}\n")
    f.write("Storage Properties - Surface Area (square metres),"+str(surfarea)+",{square metres}\n")
    f.write("Storage Properties - Extended Detention Depth (metres),"+str(edd)+",{metres}\n")
    f.write("Storage Properties - Permanent Pool Volume (cubic metres),"+str(wsur_params[""])+",{cubic metres}\n")
    f.write("Storage Properties - Initial Volume,"+str(wsur_params[""])+",\n")
    f.write("Storage Properties - Exfiltration Rate (mm/hr),"+str(exfil)+",{mm/hr}\n")
    f.write("Storage Properties - Evaporative Loss as % of PET,"+str(wsur_params[""])+",\n")
    f.write("Outlet Properties - Equivalent Pipe Diameter (mm),200,{mm}\n")
    f.write("Outlet Properties - Overflow Weir Width (metres),"+str(wsur_params[""])+",{metres}\n")
    f.write("Outlet Properties - Notional Detention Time (hrs),0.149022412970911,{hrs}\n")
    f.write("Advanced Properties - Orifice Discharge Coefficient,0.6,\n")
    f.write("Advanced Properties - Weir Coefficient,1.7,\n")
    f.write("Advanced Properties - Number of CSTR Cells,4,\n")
    f.write("Advanced Properties - Total Suspended Solids - k (m/yr),1500,{m/yr}\n")
    f.write("Advanced Properties - Total Suspended Solids - C* (mg/L),6,{mg/L}\n")
    f.write("Advanced Properties - Total Suspended Solids - C** (mg/L),6,{mg/L}\n")
    f.write("Advanced Properties - Total Phosphorus - k (m/yr),1000,{m/yr}\n")
    f.write("Advanced Properties - Total Phosphorus - C* (mg/L),0.06,{mg/L}\n")
    f.write("Advanced Properties - Total Phosphorus - C** (mg/L),0.06,{mg/L}\n")
    f.write("Advanced Properties - Total Nitrogen - k (m/yr),150,{m/yr}\n")
    f.write("Advanced Properties - Total Nitrogen - C* (mg/L),1,{mg/L}\n")
    f.write("Advanced Properties - Total Nitrogen - C** (mg/L),1,{mg/L}\n")
    f.write("Advanced Properties - Threshold Hydraulic Loading for C** (m/yr),3500,{m/yr}\n")
    f.write("Advanced Properties - User Defined Storage-Discharge-Height,,\n")
    f.write("------------------------------------------------------------------------------------\n")
    return True

def writeMUSICnodePB(f, ID, nodename, ncount, x, y, surfarea, exfil, edd, pb_params):
    f.write("Node Type,PondNode,{Node Type}\n")
    f.write("Node Name,"+str(nodename)+",{Node Name}\n")
    f.write("Node ID,"+str(ncount)+",{Node ID}\n")
    f.write("Coordinates,"+str(x)+":"+str(y)+",{Coordinates}{X:Y}\n")
    f.write("General - Location,PB"+str(nodename)+",\n")
    f.write("General - Notes,,\n")
    f.write("General - Fluxes,,\n")
    if MUSIC_VERSION == 6:
        f.write("General - Flux File Timestep (in seconds),360,{in seconds}\n")
    f.write("Reuse Properties - Reuse Enabled,1,\n")
    f.write("Reuse Properties - Annual Demand Enabled,1,\n")
    f.write("Reuse Properties - Annual Demand Value (ML/year),0,{ML/year}\n")
    f.write("Reuse Properties - Annual Demand Distribution,0,{Index from 0 to 2 for \"PET\" | \"PET - Rain\" | \"Monthly\"}\n")
    f.write("Reuse Properties - Monthly Distribution Values,8.33;8.33;8.33;8.33;8.33;8.33;8.33;8.33;8.33;8.33;8.33;8.33,\n")
    f.write("Reuse Properties - Daily Demand Enabled,1,\n")
    f.write("Reuse Properties - Daily Demand Value (ML/day),0,{ML/day}\n")
    f.write("Reuse Properties - Custom Demand Enabled,1,\n")
    f.write("Reuse Properties - Custom Demand Time Series File,,\n")
    f.write("Reuse Properties - Custom Demand Time Series Units,5,{Index from 0 to 11 for \"ML\" | \"kL\" | \"L\" | \"mL\" | \"ML/s\" | \"m3/s\" | \"L/s\" | \"mL/s\" | \"ML/day\" | \"kL/day\" | \"L/day\" | \"mL/day\"}\n")
    f.write("Reuse Properties - Minimum Draw down height,0,\n")
    f.write("Inlet Properties - Low Flow By-pass (cubic metres per sec),"+str(pb_params[""])+",{cubic metres per sec}\n")
    f.write("Inlet Properties - High Flow By-pass (cubic metres per sec),"+str(pb_params[""])+",{cubic metres per sec}\n")
    f.write("Storage and Infiltration Properties - Surface Area (square metres),"+str(surfarea)+",{square metres}\n")
    f.write("Storage and Infiltration Properties - Extended Detention Depth (metres),"+str(edd)+",{metres}\n")
    f.write("Storage and Infiltration Properties - Permanent Pool Volume (cubic metres),"+str(pb_params[""])+",{cubic metres}\n")
    f.write("Storage and Infiltration Properties - Initial Volume,"+str(pb_params[""])+",\n")
    f.write("Storage and Infiltration Properties - Exfiltration Rate (mm/hr),"+str(exfil)+",{mm/hr}\n")
    f.write("Storage and Infiltration Properties - Evaporative Loss as % of PET,"+str(pb_params[""])+",\n")
    f.write("Outlet Properties - Equivalent Pipe Diameter (mm),"+str(pb_params[""])+",{mm}\n")
    f.write("Outlet Properties - Overflow Weir Width (metres),"+str(pb_params[""])+",{metres}\n")
    f.write("Outlet Properties - Notional Detention Time (hrs),0.0936664522315673,{hrs}\n")
    f.write("Advanced Properties - Orifice Discharge Coefficient,0.6,\n")
    f.write("Advanced Properties - Weir Coefficient,1.7,\n")
    f.write("Advanced Properties - Number of CSTR Cells,2,\n")
    f.write("Advanced Properties - Total Suspended Solids - k (m/yr),400,{m/yr}\n")
    f.write("Advanced Properties - Total Suspended Solids - C* (mg/L),12,{mg/L}\n")
    f.write("Advanced Properties - Total Suspended Solids - C** (mg/L),12,{mg/L}\n")
    f.write("Advanced Properties - Total Phosphorus - k (m/yr),300,{m/yr}\n")
    f.write("Advanced Properties - Total Phosphorus - C* (mg/L),0.09,{mg/L}\n")
    f.write("Advanced Properties - Total Phosphorus - C** (mg/L),0.09,{mg/L}\n")
    f.write("Advanced Properties - Total Nitrogen - k (m/yr),40,{m/yr}\n")
    f.write("Advanced Properties - Total Nitrogen - C* (mg/L),1,{mg/L}\n")
    f.write("Advanced Properties - Total Nitrogen - C** (mg/L),1,{mg/L}\n")
    f.write("Advanced Properties - Threshold Hydraulic Loading for C** (m/yr),3500,{m/yr}\n")
    f.write("Advanced Properties - User Defined Storage-Discharge-Height,,\n")
    f.write("------------------------------------------------------------------------------------\n")
    return True

def writeMUSICnodeIS(f, ID, nodename, ncount, x, y, surfarea, exfil, edd, fd, is_params):
    f.write("Node Type,InfiltrationSystemNodeV4,{Node Type}\n")
    f.write("Node Name,"+str(nodename)+",{Node Name}\n")
    f.write("Node ID,"+str(ncount)+",{Node ID}\n")
    f.write("Coordinates,"+str(x)+":"+str(y)+",{Coordinates}{X:Y}\n")
    f.write("General - Location,IS"+str(nodename)+",\n")
    f.write("General - Notes,,\n")
    f.write("General - Fluxes,,\n")
    if MUSIC_VERSION == 6:
        f.write("General - Flux File Timestep (in seconds),360,{in seconds}\n")
    f.write("Inlet Properties - Low Flow By-pass (cubic metres per sec),"+str(is_params[""])+",{cubic metres per sec}\n")
    f.write("Inlet Properties - High Flow By-pass (cubic metres per sec),"+str(is_params[""])+",{cubic metres per sec}\n")
    f.write("Storage and Infiltration Properties - Pond Surface Area (square metres),"+str(surfarea)+",{square metres}\n")
    f.write("Storage and Infiltration Properties - Extended Detention Depth (metres),"+str(edd)+",{metres}\n")
    f.write("Storage and Infiltration Properties - Filter Area (square metres),"+str(surfarea)+",{square metres}\n")
    f.write("Storage and Infiltration Properties - Unlined Filter Media Perimeter (metres),"+str()+",{metres}\n")
    f.write("Storage and Infiltration Properties - Depth of Infiltration Media (metres),"+str(fd)+",{metres}\n")
    f.write("Storage and Infiltration Properties - Exfiltration Rate (mm/hr),"+str(exfil)+",{mm/hr}\n")
    f.write("Storage and Infiltration Properties - Evaporative Loss as % of PET,"+str(is_params[""])+",\n")
    f.write("Outlet Properties - Overflow Weir Width (metres),"+str(is_params[""])+",{metres}\n")
    f.write("Advanced Properties - Weir Coefficient,1.7,\n")
    f.write("Advanced Properties - Number of CSTR Cells,1,\n")
    f.write("Advanced Properties - Total Suspended Solids - k (m/yr),400,{m/yr}\n")
    f.write("Advanced Properties - Total Suspended Solids - C* (mg/L),12,{mg/L}\n")
    f.write("Advanced Properties - Total Suspended Solids - C** (mg/L),12,{mg/L}\n")
    f.write("Advanced Properties - Total Phosphorus - k (m/yr),300,{m/yr}\n")
    f.write("Advanced Properties - Total Phosphorus - C* (mg/L),0.09,{mg/L}\n")
    f.write("Advanced Properties - Total Phosphorus - C** (mg/L),0.09,{mg/L}\n")
    f.write("Advanced Properties - Total Nitrogen - k (m/yr),40,{m/yr}\n")
    f.write("Advanced Properties - Total Nitrogen - C* (mg/L),1,{mg/L}\n")
    f.write("Advanced Properties - Total Nitrogen - C** (mg/L),1,{mg/L}\n")
    f.write("Advanced Properties - Threshold Hydraulic Loading for C** (m/yr),3500,{m/yr}\n")
    f.write("Advanced Properties - Porosity of Infiltration Media,0.35,\n")
    f.write("Advanced Properties - Horizontal Flow Coefficient,3,\n")
    f.write("Advanced Properties - User Defined Storage-Discharge-Height,,\n")
    f.write("------------------------------------------------------------------------------------\n")
    return True

def writeMUSICnodeSW(f, ID, nodename, ncount, x, y, exfil, edd, sw_params):
    f.write("Node Type,SwaleNode,{Node Type}\n")
    f.write("Node Name,"+str(nodename)+",{Node Name}\n")
    f.write("Node ID,"+str(ncount)+",{Node ID}\n")
    f.write("Coordinates,"+str(x)+":"+str(y)+",{Coordinates}{X:Y}\n")
    f.write("General - Location,"+str(nodename)+",\n")
    f.write("General - Notes,,\n")
    f.write("General - Fluxes,,\n")
    if MUSIC_VERSION == 6:
        f.write("General - Flux File Timestep (in seconds),360,{in seconds}\n")
    f.write("Inlet Properties - Low Flow By-pass (cubic metres per sec),"+str(sw_params[""])+",{cubic metres per sec}\n")
    f.write("Storage Properties - Length (metres),"+str(sw_params[""])+",{metres}\n")
    f.write("Storage Properties - Bed Slope (%),"+str(sw_params[""])+",{%}\n")
    f.write("Storage Properties - Base Width (metres),"+str(sw_params[""])+",{metres}\n")
    f.write("Storage Properties - Top Width (metres),"+str(sw_params[""])+",{metres}\n")
    f.write("Storage Properties - Depth (metres),"+str(sw_params[""])+",{metres}\n")
    f.write("Storage Properties - Vegetation Height (metres),"+str(sw_params[""])+",{metres}\n")
    f.write("Storage Properties - Exfiltration Rate (mm/hr),"+str(exfil)+",{mm/hr}\n")
    f.write("Advanced Properties - Number of CSTR Cells,10,\n")
    f.write("Advanced Properties - Total Suspended Solids - k (m/yr),8000,{m/yr}\n")
    f.write("Advanced Properties - Total Suspended Solids - C* (mg/L),20,{mg/L}\n")
    f.write("Advanced Properties - Total Suspended Solids - C** (mg/L),14,{mg/L}\n")
    f.write("Advanced Properties - Total Phosphorus - k (m/yr),6000,{m/yr}\n")
    f.write("Advanced Properties - Total Phosphorus - C* (mg/L),0.13,{mg/L}\n")
    f.write("Advanced Properties - Total Phosphorus - C** (mg/L),0.13,{mg/L}\n")
    f.write("Advanced Properties - Total Nitrogen - k (m/yr),500,{m/yr}\n")
    f.write("Advanced Properties - Total Nitrogen - C* (mg/L),1.4,{mg/L}\n")
    f.write("Advanced Properties - Total Nitrogen - C** (mg/L),1.4,{mg/L}\n")
    f.write("Advanced Properties - Threshold Hydraulic Loading for C** (m/yr),3500,{m/yr}\n")
    f.write("------------------------------------------------------------------------------------\n")
    return True

def writeMUSICnodeRT(f, ID, nodename, ncount, x, y, exfil, edd, sw_params):
    f.write("Node Type,RainWaterTankNode,{Node Type}\n")
    f.write("Node Name,Rainwater Tank,{Node Name}\n")
    f.write("Node ID,5,{Node ID}\n")
    f.write("Coordinates,174.764595103578:77.2128060263654,{Coordinates}{X:Y}\n")
    f.write("General - Location,Rainwater Tank,\n")
    f.write("General - Notes,,\n")
    f.write("General - Fluxes,,\n")
    f.write("General - Flux File Timestep (in seconds),360,{in seconds}\n")
    f.write("Reuse Properties - Reuse Enabled,1,\n")
    f.write("Reuse Properties - Annual Demand Enabled,1,\n")
    f.write("Reuse Properties - Annual Demand Value (ML/year),0,{ML/year}\n")
    f.write("Reuse Properties - Annual Demand Distribution,0,{Index from 0 to 2 for \"PET\" | \"PET - Rain\" | \"Monthly\"}\n")
    f.write("Reuse Properties - Monthly Distribution Values,8.33;8.33;8.33;8.33;8.33;8.33;8.33;8.33;8.33;8.33;8.33;8.33,\n")
    f.write("Reuse Properties - Daily Demand Enabled,1,\n")
    f.write("Reuse Properties - Daily Demand Value (ML/day),0,{ML/day}\n")
    f.write("Reuse Properties - Custom Demand Enabled,1,\n")
    f.write("Reuse Properties - Custom Demand Time Series File,,\n")
    f.write("Reuse Properties - Custom Demand Time Series Units,5,{Index from 0 to 11 for \"ML\" | \"kL\" | \"L\" | \"mL\" | \"ML/s\" | \"m3/s\" | \"L/s\" | \"mL/s\" | \"ML/day\" | \"kL/day\" | \"L/day\" | \"mL/day\"}\n")
    f.write("Reuse Properties - Minimum Draw down height,0,\n")
    f.write("Inlet Properties - Low Flow By-pass (cubic metres per sec),0,{cubic metres per sec}\n")
    f.write("Inlet Properties - High Flow By-pass (cubic metres per sec),100,{cubic metres per sec}\n")
    f.write("Storage Properties - NumTanks,1,\n")
    f.write("Storage Properties - Surface Area (square metres),5,{square metres}\n")
    f.write("Storage Properties - Depth above overflow (metres),0.2,{metres}\n")
    f.write("Storage Properties - Volume below overflow pipe (kL),10,{kL}\n")
    f.write("Storage Properties - Initial Volume,10,\n")
    f.write("Outlet Properties - Overflow Pipe Diameter (mm),50,{mm}\n")
    f.write("Advanced Properties - Orifice Discharge Coefficient,0.6,\n")
    f.write("Advanced Properties - Number of CSTR Cells,2,\n")
    f.write("Advanced Properties - Total Suspended Solids - k (m/yr),400,{m/yr}\n")
    f.write("Advanced Properties - Total Suspended Solids - C* (mg/L),12,{mg/L}\n")
    f.write("Advanced Properties - Total Suspended Solids - C** (mg/L),12,{mg/L}\n")
    f.write("Advanced Properties - Total Phosphorus - k (m/yr),300,{m/yr}\n")
    f.write("Advanced Properties - Total Phosphorus - C* (mg/L),0.13,{mg/L}\n")
    f.write("Advanced Properties - Total Phosphorus - C** (mg/L),0.13,{mg/L}\n")
    f.write("Advanced Properties - Total Nitrogen - k (m/yr),40,{m/yr}\n")
    f.write("Advanced Properties - Total Nitrogen - C* (mg/L),1.4,{mg/L}\n")
    f.write("Advanced Properties - Total Nitrogen - C** (mg/L),1.4,{mg/L}\n")
    f.write("Advanced Properties - Threshold Hydraulic Loading for C** (m/yr),3500,{m/yr}\n")
    f.write("Advanced Properties - User Defined Storage-Discharge-Height,,\n")
    f.write("------------------------------------------------------------------------------------\n")
    return True

def writeMUSICnodeGPT():
    """
    Node Type,GPTNode,{Node Type}
    Node Name,Gross Pollutant Trap,{Node Name}
    Node ID,6,{Node ID}
    Coordinates,92.8436911487759:45.1977401129944,{Coordinates}{X:Y}
    Fluxes,,{Flux file name}
    Flux File Timestep (in seconds),1,{Flux time step}
    Lo-flow bypass rate (cum/sec),0,{Lo-flow bypass rate (cum/sec)}
    High Flow By-pass (cubic metres per sec),100,{High-flow bypass rate (cum/sec)}
    Flow Transfer Enabled,0,{0 Enabled, 1 Disabled}
    Flow Transfer Function - Input #1,0,{Flow Transfer Input (cum/sec)}
    Flow Transfer Function - Output #1,0,{Flow Transfer Output (cum/sec)}
    Flow Transfer Function - Input #2,10,{Flow Transfer Input (cum/sec)}
    Flow Transfer Function - Output #2,10,{Flow Transfer Output (cum/sec)}
    Flow Transfer Function - Input #3,,{Flow Transfer Input (cum/sec)}
    Flow Transfer Function - Output #3,,{Flow Transfer Output (cum/sec)}
    Flow Transfer Function - Input #4,,{Flow Transfer Input (cum/sec)}
    Flow Transfer Function - Output #4,,{Flow Transfer Output (cum/sec)}
    Flow Transfer Function - Input #5,,{Flow Transfer Input (cum/sec)}
    Flow Transfer Function - Output #5,,{Flow Transfer Output (cum/sec)}
    Flow Transfer Function - Input #6,,{Flow Transfer Input (cum/sec)}
    Flow Transfer Function - Output #6,,{Flow Transfer Output (cum/sec)}
    Flow Transfer Function - Input #7,,{Flow Transfer Input (cum/sec)}
    Flow Transfer Function - Output #7,,{Flow Transfer Output (cum/sec)}
    Flow Transfer Function - Input #8,,{Flow Transfer Input (cum/sec)}
    Flow Transfer Function - Output #8,,{Flow Transfer Output (cum/sec)}
    Flow Transfer Function - Input #9,,{Flow Transfer Input (cum/sec)}
    Flow Transfer Function - Output #9,,{Flow Transfer Output (cum/sec)}
    Flow Transfer Function - Input #10,,{Flow Transfer Input (cum/sec)}
    Flow Transfer Function - Output #10,,{Flow Transfer Output (cum/sec)}
    GP Transfer Enabled,0,{0 Enabled, 1 Disabled}
    GP Transfer Function - Input #1,0,{GP Transfer Input (kg/year)}
    GP Transfer Function - Output #1,0,{GP Transfer Output (kg/year)}
    GP Transfer Function - Input #2,15,{GP Transfer Input (kg/year)}
    GP Transfer Function - Output #2,15,{GP Transfer Output (kg/year)}
    GP Transfer Function - Input #3,,{GP Transfer Input (kg/year)}
    GP Transfer Function - Output #3,,{GP Transfer Output (kg/year)}
    GP Transfer Function - Input #4,,{GP Transfer Input (kg/year)}
    GP Transfer Function - Output #4,,{GP Transfer Output (kg/year)}
    GP Transfer Function - Input #5,,{GP Transfer Input (kg/year)}
    GP Transfer Function - Output #5,,{GP Transfer Output (kg/year)}
    GP Transfer Function - Input #6,,{GP Transfer Input (kg/year)}
    GP Transfer Function - Output #6,,{GP Transfer Output (kg/year)}
    GP Transfer Function - Input #7,,{GP Transfer Input (kg/year)}
    GP Transfer Function - Output #7,,{GP Transfer Output (kg/year)}
    GP Transfer Function - Input #8,,{GP Transfer Input (kg/year)}
    GP Transfer Function - Output #8,,{GP Transfer Output (kg/year)}
    GP Transfer Function - Input #9,,{GP Transfer Input (kg/year)}
    GP Transfer Function - Output #9,,{GP Transfer Output (kg/year)}
    GP Transfer Function - Input #10,,{GP Transfer Input (kg/year)}
    GP Transfer Function - Output #10,,{GP Transfer Output (kg/year)}
    TN Transfer Enabled,0,{0 Enabled, 1 Disabled}
    TN Transfer Function - Input #1,0,{TN Transfer Input (mg/L)}
    TN Transfer Function - Output #1,0,{TN Transfer Output (mg/L)}
    TN Transfer Function - Input #2,50,{TN Transfer Input (mg/L)}
    TN Transfer Function - Output #2,50,{TN Transfer Output (mg/L)}
    TN Transfer Function - Input #3,,{TN Transfer Input (mg/L)}
    TN Transfer Function - Output #3,,{TN Transfer Output (mg/L)}
    TN Transfer Function - Input #4,,{TN Transfer Input (mg/L)}
    TN Transfer Function - Output #4,,{TN Transfer Output (mg/L)}
    TN Transfer Function - Input #5,,{TN Transfer Input (mg/L)}
    TN Transfer Function - Output #5,,{TN Transfer Output (mg/L)}
    TN Transfer Function - Input #6,,{TN Transfer Input (mg/L)}
    TN Transfer Function - Output #6,,{TN Transfer Output (mg/L)}
    TN Transfer Function - Input #7,,{TN Transfer Input (mg/L)}
    TN Transfer Function - Output #7,,{TN Transfer Output (mg/L)}
    TN Transfer Function - Input #8,,{TN Transfer Input (mg/L)}
    TN Transfer Function - Output #8,,{TN Transfer Output (mg/L)}
    TN Transfer Function - Input #9,,{TN Transfer Input (mg/L)}
    TN Transfer Function - Output #9,,{TN Transfer Output (mg/L)}
    TN Transfer Function - Input #10,,{TN Transfer Input (mg/L)}
    TN Transfer Function - Output #10,,{TN Transfer Output (mg/L)}
    TP Transfer Enabled,0,{0 Enabled, 1 Disabled}
    TP Transfer Function - Input #1,0,{TP Transfer Input (mg/L)}
    TP Transfer Function - Output #1,0,{TP Transfer Output (mg/L)}
    TP Transfer Function - Input #2,5,{TP Transfer Input (mg/L)}
    TP Transfer Function - Output #2,5,{TP Transfer Output (mg/L)}
    TP Transfer Function - Input #3,,{TP Transfer Input (mg/L)}
    TP Transfer Function - Output #3,,{TP Transfer Output (mg/L)}
    TP Transfer Function - Input #4,,{TP Transfer Input (mg/L)}
    TP Transfer Function - Output #4,,{TP Transfer Output (mg/L)}
    TP Transfer Function - Input #5,,{TP Transfer Input (mg/L)}
    TP Transfer Function - Output #5,,{TP Transfer Output (mg/L)}
    TP Transfer Function - Input #6,,{TP Transfer Input (mg/L)}
    TP Transfer Function - Output #6,,{TP Transfer Output (mg/L)}
    TP Transfer Function - Input #7,,{TP Transfer Input (mg/L)}
    TP Transfer Function - Output #7,,{TP Transfer Output (mg/L)}
    TP Transfer Function - Input #8,,{TP Transfer Input (mg/L)}
    TP Transfer Function - Output #8,,{TP Transfer Output (mg/L)}
    TP Transfer Function - Input #9,,{TP Transfer Input (mg/L)}
    TP Transfer Function - Output #9,,{TP Transfer Output (mg/L)}
    TP Transfer Function - Input #10,,{TP Transfer Input (mg/L)}
    TP Transfer Function - Output #10,,{TP Transfer Output (mg/L)}
    TSS Transfer Enabled,0,{0 Enabled, 1 Disabled}
    TSS Transfer Function - Input #1,0,{TSS Transfer Input (mg/L)}
    TSS Transfer Function - Output #1,0,{TSS Transfer Output (mg/L)}
    TSS Transfer Function - Input #2,1449.72856127219,{TSS Transfer Input (mg/L)}
    TSS Transfer Function - Output #2,855.045966237349,{TSS Transfer Output (mg/L)}
    TSS Transfer Function - Input #3,,{TSS Transfer Input (mg/L)}
    TSS Transfer Function - Output #3,,{TSS Transfer Output (mg/L)}
    TSS Transfer Function - Input #4,,{TSS Transfer Input (mg/L)}
    TSS Transfer Function - Output #4,,{TSS Transfer Output (mg/L)}
    TSS Transfer Function - Input #5,,{TSS Transfer Input (mg/L)}
    TSS Transfer Function - Output #5,,{TSS Transfer Output (mg/L)}
    TSS Transfer Function - Input #6,,{TSS Transfer Input (mg/L)}
    TSS Transfer Function - Output #6,,{TSS Transfer Output (mg/L)}
    TSS Transfer Function - Input #7,,{TSS Transfer Input (mg/L)}
    TSS Transfer Function - Output #7,,{TSS Transfer Output (mg/L)}
    TSS Transfer Function - Input #8,,{TSS Transfer Input (mg/L)}
    TSS Transfer Function - Output #8,,{TSS Transfer Output (mg/L)}
    TSS Transfer Function - Input #9,,{TSS Transfer Input (mg/L)}
    TSS Transfer Function - Output #9,,{TSS Transfer Output (mg/L)}
    TSS Transfer Function - Input #10,,{TSS Transfer Input (mg/L)}
    TSS Transfer Function - Output #10,,{TSS Transfer Output (mg/L)}
    TSS Flow-Efficiency Enabled,0,{{0 = enabled, 1 = disabled}
    TSS flow-efficiency values,[0:1];[0.5:0.5];[1:0.2],{Flow Efficiency values e.g. [0.0:1.0];[0.0:2.0];}
    TN Flow-Efficiency Enabled,0,{{0 = enabled, 1 = disabled}
    TN flow-efficiency values,[0:1];[0.5:0.5];[1:0.2],{Flow Efficiency values e.g. [0.0:1.0];[0.0:2.0];}
    TP Flow-Efficiency Enabled,0,{{0 = enabled, 1 = disabled}
    TP flow-efficiency values,[0:1];[0.5:0.5];[1:0.2],{Flow Efficiency values e.g. [0.0:1.0];[0.0:2.0];}
    GP Flow-Efficiency Enabled,0,{{0 = enabled, 1 = disabled}
    GP flow-efficiency values,[0:1];[0.5:0.5];[1:0.2],{Flow Efficiency values e.g. [0.0:1.0];[0.0:2.0];}"""
    return True

def writeMUSIClink(f, upN, downN):
    f.write("Link Name,Drainage Link,\n")
    f.write("Source Node ID,"+str(upN)+",{The is the ID of the upstream node}\n")
    f.write("Target Node ID,"+str(downN)+",{This is the ID of the downstream node}\n")
    f.write("Routing,Not Routed,{either \"Not Routed\" or \"Routed\"}\n")
    f.write("Muskingum K,30,{no value required for no routing or \"numerical value\" for routed}\n")
    f.write("Muskingum Theta,0.25,{no value required for no routing or \"numerical value\" for routed. Must be between 0.1 and 0.49}\n")
    f.write("------------------------------------------------------------------------------------\n")
    return True

def writeMUSICsecondarylink(f, upN, downN, components):
    f.write("Link Name,Secondary Drainage Link,\n")
    f.write("Source Node ID,8,{The is the ID of the upstream node}\n")
    f.write("Target Node ID,6,{This is the ID of the downstream node}\n")
    f.write("Routing,Not Routed,{either \"Not Routed\" or \"Routed\"}\n")
    f.write("Muskingum K,30,{no value required for no routing or \"numerical value\" for routed}\n")
    f.write("Muskingum Theta,0.25,{no value required for no routing or \"numerical value\" for routed. Must be between 0.1 and 0.49}\n")
    f.write("Secondary Outflow Components,Deep Seepage,{for secondary drainage link only}\n")
    f.write("------------------------------------------------------------------------------------\n")
    return True

def writeMUSICfooter(f):
    f.write("====================================================================================\n")
    f.close()
    return True

def getTTEdata(fname, loads):
    """Retrieves the treatment train effectiveness data from a given filename 'fname'. The function
    is based on MUSIC's template output file for TTE. The other argument 'loads' is a boolean
    and will also return the pollutant loads if true."""
    f = open(fname, 'r')
    lines = []
    for line in f:
        lines.append(line.split(','))
    f.close()
    tte = [float(lines[1][3]),
           float(lines[2][3]),
           float(lines[3][3]),
           float(lines[4][3])]
    if loads:
        out = [float(lines[1][2]),
               float(lines[2][2]),
               float(lines[3][2]),
               float(lines[4][2])]
        return tte, out
    return tte, 0
