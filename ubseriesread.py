 # -*- coding: utf-8 -*-
"""
@file
@author  Peter M Bach <peterbach@gmail.com>
@version 1.0
@section LICENSE

This file is part of UrbanBEATS
Copyright (C) 2013  Peter M Bach

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

import datetime
import dateutil.parser as dtparse

def loadClimate(filename, dt_out, numyears):
    """Updated (2016) function that retrieves climate data from a .csv file. Note that the csv file needs
    to have its time stamps in ISO format.

    Legal Formats:
        "YYYY-MM-DD HH:MM:SS"   - standard hyphenation and colon use for ISO dates
        "yyyymmddhhmmss"        - complete string of all data no interruptions
        "yyyymmddThhmmss        - uses the T to separate date and time in ISO standard
        "yyyymmdd hhmmss"       - uses a space to separate date and time

    Input Arguments:
        filename - name of the CSV file (full path)
        dt_out - output time step
        numyears - number of years to extract

    Output:
        data on the climate file

    """
    #Open climate file, grab data and figure out dt
    print filename
    f = open(filename, 'r')
    datavec = []    #initialize vector that contains data [[Date] [Rain]]
    f.readline()    #skip the first line of the file
    for lines in f:
        datavec.append(lines)
    f.close()
    for i in range(len(datavec)):
        datavec[i] = datavec[i].split(",")
        #datavec[i][0] = dtparse.parse(datavec[i][0])   #Parsing every single line takes too long, parse on demand
        datavec[i][1] = datavec[i][1].rstrip("\n")
        if datavec[i][1] in ['', "0", "", "NaN"]:
            datavec[i][1] = "0"
        datavec[i][1] = float(datavec[i][1])
        #now we have datavec = [ [<datetime.datetime>, <float>], [] ,[]]

    print dtparse.parse(datavec[1][0])
    print dtparse.parse(datavec[0][0])
    dt_in = dtparse.parse(datavec[1][0]) - dtparse.parse(datavec[0][0])
    dt_in = dt_in.total_seconds() / 60.0
    print dt_in
    
    timesteps = len(datavec)
    timelength = float(dt_in) * float(timesteps)    #Minutes
    
    if numyears == 0:
        numyears = 1.0
    
    requiredlength = numyears * 365.0 * 24.0 * 60.0 / dt_in       #How long should the array be?
    if requiredlength > timelength:
        requiredlength = timelength     #If we have less data than required, then use the whole data
    else:
        del datavec[int(requiredlength):]

    #Rescale the data
    if dt_out < dt_in:
        dt_out = dt_in      #if output time step is finer, cannot use the data!
        return datavec
    
    datalines = int(dt_out / dt_in)     #Number of lines of input time step per output time step
    rescaledData = []
    linecounter = 0
    datasum = 0
    startdt = 0    

    for i in range(len(datavec)):
        linecounter += 1
        datasum += datavec[i][1]
        if startdt == 0:            #If the datetime stamp has not been set, set it
            startdt = datavec[i][0]
        if linecounter == datalines:
            rescaledData.append([startdt, datasum])
            linecounter, startdt, datasum = 0, 0, 0     #Reset variables
    if linecounter != 0:
        rescaledData.append([startdt, datasum])
    datavec = []    #Clear memory
    #Now we have rescaled data in the matrix rescaledData[] stored in the form of [<isostring>, <float>]

    return rescaledData

def convertClimateToScalars(datavec):
    """Converts an input series to a set of scaling factors based on the annual data (2016 version)
    Used main for evapotranspiration factors.

    :param datavec: [<isostring>, <float>] format of evap data retrieved from loadClimate()
    :return: scalefactors array
    """

    #Get a total annual value array
    anndata = []
    yeartrack = int(dtparse.parse(datavec[0][0]).date().year)
    datasum = 0
    for i in range(len(datavec)):
        curyear = int(datavec[i][0][0:4])   #ISO format, the first four characters are ALWAYS the year (more efficient than converting the whole date)
        if curyear == yeartrack:
            datasum += datavec[i][1]
        elif curyear != yeartrack:
            anndata.append([yeartrack, datasum])
            datasum = datavec[i][1]         #reinitialize datasum, but set to value of current year
            yeartrack = curyear
    anndata.append([yeartrack, datasum])

    #Rescale the data
    scalefactors = []
    yeartrack = int(dtparse.parse(datavec[0][0]).date().year)   #Reinitialise
    anndataindex = 0
    for i in range(len(datavec)):
        curyear = int(datavec[i][0][0:4])   #ISO format, the first four characters are ALWAYS the year (more efficient than converting the whole date)
        if curyear == yeartrack:
            scalefactors.append([datavec[i][0], datavec[i][1]/anndata[anndataindex][1]])
        else:
            yeartrack = curyear
            anndataindex += 1
            scalefactors.append([datavec[i][0], datavec[i][1]/anndata[anndataindex][1]])

    return scalefactors

def removeDateStampFromSeries(data, colnum):
    """Removes the datestamp from the dataseries 'data' and returns a single-dimensional
    vector containing only data values."""
    dataseries = []
    for i in range(len(data)):
        dataseries.append(data[i][colnum])
    return dataseries

def convertDataToMonthly(data):
    """Converts an input data set to monthly time step"""
    mdata = []
    datasum = 0
    curmonth = data[0][1]
    for i in range(len(data)):
        if data[i][1] == curmonth:
            datasum += data[i][2]
        else:
            mdata.append([data[i-1][0], curmonth, datasum])
            datasum = data[i][2]
            curmonth = data[i][1]
    mdata.append([data[i-1][0], curmonth, datasum])
    return mdata
    
def convertDataToAnnual(data):
    """Converts an input data set to annual time step"""
    anndata = []
    yeartrack = data[0][0]      #initialize to start year
    datasum = 0
    for i in range(len(data)):
        curyear = data[i][0]
        if curyear == yeartrack:
            datasum += data[i][2]
        elif curyear != yeartrack:
            anndata.append([yeartrack, datasum])
            datasum = data[i][2] #reinitialize datasum, but set to value of current year
            yeartrack = curyear
    anndata.append([yeartrack, datasum])
    return anndata

def convertDataToInflowSeries(data, catchment, includedatestamp):
    """Converts an input rain-data series to an inflow time series [kL/dt] based on
    a specified catchment area
        - data: the data vector [year, month, data[mm]] 
        - catchment: catchment area [sqm]
        - includedatestamp: if false, just returns a single-dimensional vector
        """
    inflowseries = []
    #Check for DateStamp
    if type(data[0]) != type([]):       #NO has no date stamp
        for i in range(len(data)):
            inflowseries.append(data[i]/1000*catchment)
    else:       #Has a date stamp
        for i in range(len(data)):
            if includedatestamp:
                inflowseries.append([data[i][0], data[i][1], data[i][2]/1000 * catchment])
            else:
                inflowseries.append(data[i][2]/1000 * catchment)
    return inflowseries

def createScaledDataSeries(annualvalue, scalingfactors, includedatestamp):
    """Converts single annual water usage value [kL] to a time series based on
    the scalingfactors array.
        - annualvalue: total annual water demand [kL]
        - scalingfactors: time series of scaling factors obtained from 
                        convertVectorToScalingFactors()
        - includedatestamp: if false, just returns a single-dimensional vector"""
    dataseries = []
    for i in range(len(scalingfactors)):
        if includedatestamp:
            dataseries.append([scalingfactors[i][0], scalingfactors[i][1]*annualvalue])
        else:
            dataseries.append(scalingfactors[i][1]*annualvalue)
    return dataseries

def createConstantDataSeries(dailyvalue, timesteps):
    """Converts a daily water usage value [kL/day] into a time series of length "timesteps"
    and returns this as a vector that does not include a datestamp
        - Dailyvalue: of water demand [kL/day]
        - timesteps: total length of time period [days]
    """
    dataseries = []
    for i in range(timesteps):
        dataseries.append(dailyvalue)
    return dataseries

def mergeTimeSeries(timeseries1, timeseries2, includedatestamp):
    """Merges two time series of the same time step into a single continuous time series.
    If time steps differ, it will return the longer one
        - timeseries1, 2: respective time series matrices either in the form [value] or [date, value]
        - datestamp: removes the datestamp if False"""
    merger = []
    #Check the length of both time series to make sure they can be merged
    length1 = len(timeseries1)
    length2 = len(timeseries2)
    if length1 != length2:      #return the longer one
        print "Error, time series are not of same length"
        if length1 > length2:
            return timeseries1
        else:
            return timeseries2
        
    #Check format of time series (i.e. whether simply [data] or [[date, data]] format
    if type(timeseries1[0]) == type([]):    #if of type list    
        format1 = len(timeseries1[0])
    else:
        format1 = 1
    if type(timeseries2[0]) == type([]):
        format2 = len(timeseries2[0])       #can be done by checking the first row
    else:
        format2 = 1
    #Possibilities: 1 - [data], 2 - [year, data], 3 - [year, month, data]
    if format1 > 1 or format2 > 1:      #then there is date data
        if format1 == format2:
            controltseries = timeseries1        #If they are the same length, assume they have same data structure
        elif format1 > format2:
            controltseries = timeseries1
        else:
            controltseries = timeseries2
    else:
        includedatestamp = False
        
    for i in range(length1):
        timestepsum = 0
        if format1 > 1: 
            timestepsum += timeseries1[i][len(timeseries1[i])-1]
        else: 
            timestepsum += timeseries1[i]
        if format2 > 1: 
            timestepsum += timeseries2[i][len(timeseries2[i])-1]
        else: 
            timestepsum += timeseries2[i]
                
        if includedatestamp:
            merger.append(controltseries[i][0:(len(controltseries[0])-1)])
            merger[i].append(timestepsum)
        else:
            merger.append(timestepsum)
    return merger

def scaleClimateSeries(data, scalars):
    print "Scalars", scalars
    for i in range(len(data)):
        data[i][1] = data[i][1] * scalars[int(data[i][0][5:7]) - 1]
    return data


# DEPRECATED CODE
#
# def loadClimateFile(filename, filetype, dt_in, dt_out, numyears):
#     """Retrieves climate file based on the input filename and format specified. Format
#     can take different styles, e.g. .ixx, .csv, etc.
#         - filename: the full path to the file, so that the program can find it
#         - format: the filetype extension that also defines how the raindata is delimited
#         - dt_in: input timestep of the file [mins]
#         - dt_out: desired output timestep of the file [mins]
#         - numyears: extracts data from startyear + numyears and returns it
#
#     Current support rainfile formats are: .csv, .ixx, .mse
#     """
#     #New timestep, determine how many lines of old time-step data need to be summed
#     if dt_out % dt_in == 0:
#         datalines = int(dt_out / dt_in)
#     else:
#         print "Error: cannot convert climate file timestep from dt-in to dt-out"
#         datalines = 1
#
#     #Grab the data from the file based on the format, returns [Year, Month, Data]
#     if filetype == "csv":
#         #Input Data format: "DD/MM/YYYY HH:MM, rain[mm]\n", skip first line of file
#         data = readFileCSV(filename, datalines)
#     elif filetype == "ixx":
#         #Input Data format: "DD.MM.YYYY.hh.mm.ss rain[mm/dt]\n", skip first line of file
#         data = readFileIXX(filename, datalines)
#     elif filetype == "mse":
#         #Input Data format: "YY MM DD hh mm ss rain[10E-3mm/dt]\n", skip first line of file
#         data = readFileMSE(filename, datalines)
#
#     #Narrow down the data to only what the user wants
#     datacut = extractDataSubSet(data, numyears)
#     return datacut
#
# def readFileCSV(filename, rescalelines):
#     """Read a .csv format data file containing climate data at a given time step.
#     Function also calls rescaling function to rescale the data to the desired d_out
#     timestep"""
#     f = open(filename, 'r')         #Open the file containin raindata
#     datavec = []                      #initialize the vector that contains the data [[Date][rain]]
#     f.readline()                        #skip the first line of the file
#     for lines in f:
#         datavec.append(lines)         #Add the subsequent lines to the rain file
#     f.close()
#     for i in range(len(datavec)):
#         datavec[i] = datavec[i].split(",")    #split the line based on the s
#         datavec[i][0] = datavec[i][0].split(" ")
#         datavec[i][1] = datavec[i][1].rstrip("\n")
#         if datavec[i][1] in ['', "0", ""]:
#             datavec[i][1] = "0"
#         datavec[i][1] = float(datavec[i][1])
#     #Transfer rain data into rain[] matrix, pay attention to month and year
#     for i in range(len(datavec)):
#         year, month = convertToYearMonth(datavec[i][0][0], "/", 2)
#         datavec[i] = [year, month, datavec[i][1]]
#     data = rescaleData(datavec, rescalelines)
#     return data
#
# def readFileIXX(filename, rescalelines):
#     return True
#
# def readFileMSE(filename, rescalelines):
#     return True
#
# def rescaleData(datavec, rescalelines):
#     """Rescale data to current dt_out timestep (using rescalelines). Sum up in groups of
#     #x lines where x = rescalelines"""
#     timecounter = 0
#     datasum = 0
#     data = []
#     for i in range(len(datavec)):
#         curyear = datavec[i][0]
#         curmonth = datavec[i][1]
#         timecounter += 1
#         datasum += datavec[i][2]
#         if timecounter == rescalelines:
#             data.append([curyear, curmonth, datasum])
#             timecounter = 0
#             datasum = 0
#     if timecounter != 0:
#         data.append([curyear, curmonth, datasum])
#     datavec = []        #Clear memory
#     #Now we have rescaled data in the matrix data[] stored in the form of [year, month, data]
#     return data
#
# def convertToYearMonth(datestring, delimiter, yearpos):
#     """Input date string 'DD/MM/YYYY' is converted into two output integers: year and month"""
#     date = datestring.split(delimiter)
#     year = int(date[yearpos])
#     if yearpos == 0:
#         month = int(date[yearpos + 1])
#     else:
#         month = int(date[yearpos - 1])
#     return year, month
#
# def getYearCount(inputvec):
#     """Scans the data vector for unique years to return the total number of years in
#         the time-series """
#     yearitems = []
#     for i in range(len(inputvec)):
#         if inputvec[i][0] not in yearitems:
#             yearitems.append(inputvec[i][0])
#     return len(yearitems)
#
# def extractDataSubSet(data, numyears):
#     """Scans the data file and returns a time series of length 'numyears' = number of
#     years the user wants of the data, if numyears = 0, returns one year only"""
#     years = getYearCount(data)
#     if numyears < 1:
#         numyears = 1    #cannot be less than 1
#     if numyears >= years:        #if time series shorter than what user wants, returns time-series
#         return data
#     startyear = data[0][0]       #get the start year
#     endyear = startyear + numyears   #the year to stop tracking
#     currentyear = startyear     #initialize current year variable
#     datacut = []
#     rowcounter = 0
#     while currentyear != endyear:
#         datacut.append(data[rowcounter])        #append the data
#         rowcounter += 1                         #increment row counter by one
#         currentyear = data[rowcounter][0]     #stops once the last line of the end year has been written
#     return datacut
#
# def convertVectorToScalingFactors(inputvec):
#     """Converts an input series to a set of scaling factors based on the annual data.
#     Used for evaporation factors for example."""
#     annualdata = convertDataToAnnual(inputvec)
#     yeartrack = inputvec[0][0]
#     anndataindex = 0
#     scalefactors = []
#     for i in range(len(inputvec)):
#         curyear = inputvec[i][0]
#         if curyear == yeartrack:
#             scalefactors.append([inputvec[i][0], inputvec[i][1], inputvec[i][2]/annualdata[anndataindex][1]])
#         else:
#             yeartrack = curyear
#             anndataindex += 1
#             scalefactors.append([inputvec[i][0], inputvec[i][1], inputvec[i][2]/annualdata[anndataindex][1]])
#     #scalefactors.append([inputvec[i][0], inputvec[i][1], inputvec[i][2]/annualdata[anndataindex][1]])
#     return scalefactors
