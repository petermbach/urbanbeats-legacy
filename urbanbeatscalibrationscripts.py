# -*- coding: utf-8 -*-
"""
@file
@author  Peter M Bach <peterbach@gmail.com>
@version 1.0
@section LICENSE

This file is part of VIBe2
Copyright (C) 2016 Peter M Bach

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

def estimateTIF_MW(inputdata):
    pass




def calculateNashE(real,mod):
    nashE = 0


    return nashE



def calculateRMSE(real,mod):
    rmse = 0


    return rmse




def calculateRelativeError(real,mod):
    relErr = 0

    return relErr


def readCalibrationData(filename):
    """Reads the calibration data file and returns an array.
    :param filename: filename containing the calibration data set split into two columns: Block ID and Value
    :return: final array [ [BlockID], [Value] ]
    """
    rawdata = []
    calibdata = []
    final = [ [] , [] ]
    f = open(filename, 'r')
    for lines in f:
        rawdata.append(lines.split(','))
    f.close()
    for i in range(len(rawdata)):
        try:
            calibdata.append([int(rawdata[i][0]), float(rawdata[i][1])])
        except ValueError:
            pass
    for i in range(len(calibdata)):
        final[0].append(calibdata[i][0])
        final[1].append(calibdata[i][1])
    return final