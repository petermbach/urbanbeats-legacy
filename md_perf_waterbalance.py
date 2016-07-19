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

ENDUSE_NAMES = ["kitchen", "toilet", "shower", "laundry", "irrigation", "com", "ind", "publicirri", "losses"]

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
        elif d in ["publicirri"]:
            allDemands[d] = allDemands[d] * patscale * seasonFact   #Public irrigation still continues
        elif d in ["losses"]:
            allDemands[d] = allDemands[d]

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

class Storage_Sim(object):
    def __init__(self, obID, storeType, location, scale, quantity, impT, unitcapacity):
        self.__storageID = obID
        self.__storageType = storeType
        self.__storageLocation = location
        self.__storageScale = scale
        self.__storageQuantities = quantity
        self.__upstreamImp = impT
        self.__capacity = unitcapacity
        self.__capacityTotal = unitcapacity * quantity
        self.__currentV = 0.0
        self.__initcapacity = 0.0

        self.__routedt = 0
        self.__virtual_space = []

    def setRoutingTime(self, dt):
        self.__routedt = dt     #time steps for reusable purpose

    def initialiseStorageVol(self, init_cap):
        """Initialises the storage volume based on an initial-capacity input [%], the current
        storage initial condition is dependent on the system's total capacity.

        :param init_cap: initial capacity [%] or [] proportion.
        """
        if init_cap > 1.0:
            self.__currentV = float(self.__capacitytotal * init_cap / 100.0)
            self.__initcapacity = self.__currentV
        else:
            self.__currentV = float(self.__capacitytotal * init_cap)
            self.__initcapacity = self.__currentV

    def resetStorage_Sim(self):
        """Resets the virtual storage for routing back to zeros, resets the current volume to
        initial capacity.
        """
        self.__virtual_space = [0]*self.__routedt       #Reset the routing array
        self.__currentV = self.__initcapacity           #Reset initial capacity

    def calculateStorageBehaviour(self, rain, evap, demands):
        """Simulates one single time step of storage-behaviour water balance. Inputs are used
        to update the storage conditions of the system as well, what the current volume is.

        :param rain: Input rainfall [mm]
        :param evap: Input evapotranspiration [mm]
        :param demands: Demand array, the ordered demands based on priority for that
                        time step, e.g. if priority is (1) outdoor, (2) indoor non-contact,...
                        then array will be [x kL, y kL, z kL]. The array is fed back as output
        :return: An array of water balance data for writing into a file
                [initial Volume, inflow for that dt, spill from system, other losses, total demand, total supplied,
                updated demand list, final volume]
        """
        #(1) Inflow and current Volume
        newinflow = rain/1000 * self.__upstreamImp     #[kL]
        initV = self.__currentV
        self.__virtual_space.append(newinflow)

        inflow = self.__virtual_space[0]    #Routing - add newest inflow to the end of the array
        self.__virtual_space.pop(0)         #Pop the current 0th index of the array
        self.__currentV += inflow           #Add that inflow to the system

        #(2) Spills and Losses from system (yield after spill order)
        spill = max(self.__currentV - self.__capacityTotal, 0)  #calculate spill
        otherloss = 0
        self.__currentV -= spill
        if self.__storageType in ["PB", "WSUR"] and rain == 0:
            pass        #Remove water through evaporation
            otherloss += 0

        #(3) Supply Demand and Update Storage
        totalDemand = sum(demands)
        totalSupply = 0
        while self.__currentV > 0:
            #Supply demands one by one
            pass
            totalSupply += 0

        return [initV, inflow, spill, otherloss, totalDemand, totalSupply, demands, self.__currentV]

    def emptyStorageVol(self, flowrate, simdt):
        """Orders the storage system to drain its current storage volume based on a pre-defined
        flow-rate [L/sec], if this is called in a time step, the storage will slowly empty its
        capacity downstream.

        :param flowrate: in [L/sec]
        :param simdt: simulation time step to work out volume reduction [mins]
        :return: simply updates the current Volume, affects supply
        """
        flowrate = flowrate * 60.0 / 1000.0    #[kL/min]
        emptiedVol = flowrate * simdt
        self.__currentV = max(self.__currentV - emptiedVol, 0)  #empty the store
        return True

    def getStoreID(self):
        return self.__storageID

    def getStoreLocation(self):
        return self.__storageLocation

    def getStoreType(self):
        return self.__storeType

    def getStoreScale(self):
        return self.__storageScale
