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



def UB_WaterBalance(rain, evap, blocks):

    evapindex = 0
    for i in range(len(rain)):
        #Current rain and evap
        currain = rain[i]
        curevap = evap[evapindex]


        print rain[i][0], rain[i][1]



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
