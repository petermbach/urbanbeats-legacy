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

import numpy as np

def calculateNashE(real,mod):
    #1 - sum(mod/obs diff squared) / sum(mod/modavg diff squared)
    modavg = np.average(mod)

    omsq = 0
    mmsq = 0

    for i in range(len(real)):
        omsq += pow((real[i] - mod[i]),2)
        mmsq += pow((mod[i] - modavg),2)

    return (1.0 - (omsq/mmsq))

def calculateRMSE(real,mod):
    errordiff = 0

    for i in range(len(real)):
        errordiff += pow((real[i]-mod[i]),2)

    return np.sqrt(errordiff/float(len(real)))

def calculateRelativeError(real,mod):
    relErrors = []
    for i in range(len(real)):
        if real[i] == 0:
            relErrors.append(100.0)
        else:
            relErrors.append(abs(round((real[i] - mod[i])/real[i],1)*100.0))

    avgerr = np.average(relErrors)
    maxerr = np.max(relErrors)
    minerr = np.min(relErrors)

    counterr50 = 0
    counterr30 = 0
    counterr10 = 0
    for i in range(len(relErrors)):
        if relErrors[i] < 10.0:
            counterr50 += 1
            counterr30 += 1
            counterr10 += 1
        elif relErrors[i] < 30.0:
            counterr50 += 1
            counterr30 += 1
        elif relErrors[i] < 50.0:
            counterr50 += 1
    return avgerr, minerr, maxerr, counterr10, counterr30, counterr50



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