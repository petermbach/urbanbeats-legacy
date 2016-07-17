# -*- coding: utf-8 -*-
"""
@file
@author Peter M Bach <peterbach@gmail.com>
@version 1.0
@section LICENSE

This file is part of UrbanBEATS
Copyright (C) 2016 Peter M Bach

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

import datetime
import dateutil.parser as dtparse

ENDUSE_NAMES = ["kitchen", "toilet", "shower", "laundry", "irrigation", "com", "ind", "publicirri"]

def UB_BlockDemand(t_current, rain, evap, seasonFact, temporal_params, blockdata):
    """ Runs through the full water demand calculation for a single block based on
    current input data and behavioural parameters. Returns an array of demand
    outputs for the current time step.

    :param t_current: current time T, full ISO format including date
    :param rain: Rainfall [mm] at time t
    :param evap: Evapotranspiration [mm] at time t
    :param scalefile: Seasonal Demand Scalar at time t
    :param temporal_params: Parameters for temporal analysis
    :param blockdata: asset containing data from current block
    :return: [Updated hourly water consumption fro all end uses for that block]
    """
    dt = dtparse.parse(t_current)
    hr = dt.hour        #index for 24-hr pattern
    wkd = dt.weekday()  #index to check if need weekend rules

    params = temporal_params    #Dictionary of all parameters
    curBlockID = blockdata.getAttribute("BlockID")
    #print "Current Block ID: ", curBlockID, " at H-", hr, " hour and WKD-", wkd, " weekday"
    allDemands = GetBlockEndUseAverages(blockdata)
    #print allDemands

    #Determine weekend factor?
    wkd_res = 1.0   #weekend residential demand scalar
    wkd_nres = 1.0  #weekend non-residential demand scalar

    if wkd in [5, 6]:   #if Saturday or Sunday i.e. if we are on a weekend
        if params["weekend_res"]:           #Are we scaling residential demands?
            wkd_res = params["weekend_resfact"] #Add the factors
        if params["weekend_nres"]:
            wkd_nres = params["weekend_nres"]

    for d in allDemands.keys():
        patscale = params[d+"_pat"][hr]
        if d in ["kitchen", "shower", "toilet", "laundry", "irrigation"]:
            allDemands[d] = allDemands[d] * patscale * seasonFact * wkd_res
        elif d in ["com", "ind"]:
            allDemands[d] = allDemands[d] * patscale * seasonFact * wkd_nres
        else:
            allDemands[d] = allDemands[d] * patscale * seasonFact   #Public irrigation still continues

    return allDemands


def GetBlockEndUseAverages(blockdata):
    enduses = {}
    for n in ENDUSE_NAMES:
        enduses[n] = blockdata.getAttribute("Blk_"+n)/float(24.0)       #Retrieve in kL/hour
    return enduses


def UB_BlockSupply():


    return True


def SetupBlockData(blockasset):

    resroof = blockasset.getAttribute("")




    pass


def Drainage_Lot(self, block, params):
    """ Conducts a lot drainage calculation for the current block
    :param self:
    :param block: The asset of the current block
    :param params: A dictionary of lot drainage parameters
    :return:
    """
