# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 18:51:20 2015

@author: Peter Bach
"""

#UrbanBEATS Post-processing


from osgeo import ogr
import os, numpy

#####################################################################################
##                                                                                 ##
## =-=-=-=-=-=-= POST-PROCESSING FUNCTIONS FOR URBANBEATS DATA FILES =-=-=-=-=-=-= ##
##                                                                                 ##
#####################################################################################

#GLOBAL VARIABLES
SYSTYPES = ["BF", "WSUR", "RT", "IS", "SW", "PB"]
SCALETYPES = ["L_RES", "L_LI", "L_COM", "L_HI", "L_ORC", "S", "N", "B"]
SCALETYPESSIMPLE = ["L", "S", "N", "B"]


#----- FUNCTIONS FOR FINDING OUTPUT FILES AND PRE-PROCESSING THESE FOR ANALYSIS -----##

def getOutputFiles(folderpaths, filetype):
    """Retrieves all filenames within a given folderpath of the given urbanbeats output file type
    and returns a list of full filepaths for further analysis
    
    Arguments:
        folderpath -- string path to the folder containing the UrbanBEATS files
        filetype -- type of shapefile being retrieved (pc_Blocks | ic_Blocks | PlannedWSUD | ImplementedWSUD | Network)
    
    Outputs:
        filelist -- an array or strings containing the full filepath to each shapefile of the selected
                    type in the folderpath
    """
    filenames = []

    if type(folderpaths) == str:
        for file in os.listdir(folderpaths):
            if file.endswith(".shp") and filetype in file:
                filenames.append(folderpaths+file)
    elif type(folderpaths) == list:
        for path in folderpaths:
            for file in os.listdir(path):
                if file.endswith(".shp") and filetype in file:
                    filenames.append(path+file)
        
    return filenames  


def loadFolderPaths(pathtxtfile):
    """Loads a .txt file containing a list of paths and returns a list of paths
    that contain output data. Useful for batch analysis and division of scenarios
    
    Arguments:
        pathtxtfile -- full path to .txt file containing python-compatible paths
    
    Outputs:
        pathlist -- a list of strings, each being one folder path
    """
    pathlist = []
    f = open(pathtxtfile, 'r')
    for lines in f:
        pathlist.append(lines.rstrip('\n'))
    f.close()
    return pathlist
    

def filterScenarioFiles(filenames, scenarioname):
    """Filters a filelist based on a particular scenarioname tag. Function scans
    filenames for the presence of a string defined by 'scenarioname' argument and returnts
    a reduced list of file.
    
    Arguments:
        filenames -- array of filenames, retrieved by getOutputFiles()
        scenarioname -- string to search for in filenames (e.g. "noMCA-Trial1")
    
    Outputs:
        filterlist -- reduced list of filenames based on the scenarioname filter
    """    
    filterlist = []    
    for i in range(len(filenames)):
        if scenarioname in filenames[i]:
            filterlist.append(filenames[i])
    return filterlist
    

#----- FUNCTIONS FOR POST-PROCESSING BLOCKS DATA SETS -----##
    
def retrieveBlocks(scenario):
    pass
    return True
    
def loadCalibrationData(filename):
    pass
    return True
    
def evaluateCalibration(blockdata, calibdata, attname, criterion):
    pass
    return True
    
def evaluateBlockVariability(blockdatasets):
    pass
    return True
    
    
    
#----- FUNCTIONS FOR POST-PROCESSING TECHNOLOGIES DATA SETS -----##

def retrieveWSUDlayout(scenario):
    """Opens the WSUD shapefile and retrieves all attributes from the data as a python
    dictionary
    
    Arguments:
        scenario -- input path to the WSUD scenario file
        
    Outputs:
        wsuddata -- output list of dictionaries containing all attributes from the input scenario file
    """
    wsuddata = []
    
    drv = ogr.GetDriverByName('ESRI Shapefile')
    shapefile = drv.Open(scenario)
    layer = shapefile.GetLayer(0)
    
    layerdefn = layer.GetLayerDefn()
    attnames = []
    fieldcount = layerdefn.GetFieldCount()

    for i in range(int(fieldcount)):
        attnames.append(layerdefn.GetFieldDefn(i).GetName())
    
    features = layer.GetFeatureCount()
    for i in range(int(features)):
        feature = layer.GetFeature(i)
        featuredata = {}
        for j in attnames:
            featuredata[j] = feature.GetField(j)
        
        try:
            featuredata["Aeff"] = float(featuredata["SysArea"])/float(featuredata["EAFact"])
        except ZeroDivisionError:
            featuredata["Aeff"] = 0
            
        wsuddata.append(featuredata)
    
    shapefile.Destroy()   
    
    return wsuddata


def mergeDataSets(wsuddatasets):
    """Merges a number of WSUD shapefiles into a single continuous data set (useful for
    benchmark analysis)
    
    Arguments:
        wsuddatasets -- input list of dictionaries containing all attributes of the WSUD layout
        
    Outputs:
        wsudmerge -- merged dictionary of WSUD systems with an additional attribute, Strategy No.
    """
    wsudmerge = []
    
    for i in range(len(wsuddatasets)):
        stratno = i+1
        curstrat = wsuddatasets[i]
        for j in range(len(curstrat)):
            curtech = curstrat[j]
            curtech["Strategy"] = stratno
            wsudmerge.append(curtech)
            
    return wsudmerge


def calculateUtilisation(wsuddata, attname):
    """Calculates the utilisation for all system types in a given list of WSUD assets
    
    Arguments:
        wsuddata -- list of dictionaries containing data from a WSUD shapefile (output from retrieveWSUDlayout())
        attname -- attribute name that is used to calculate Utilisation (e.g. ImpT or CurImpT)
        
    Outputs:
        utildict -- dictionary of system types, each with the associated Utilisation [%] in that particular strategy
    """    
    utildict = {}
    totImpT = 0
            
    for t in SYSTYPES:              #For each system type    
        utildict[t] = []
        for i in range(len(wsuddata)):  #Scan the WSUD list
            if wsuddata[i]["Type"] == t:
                utildict[t].append(wsuddata[i][attname])
    
    for i in utildict.keys():
        utildict[i] = sum(utildict[i])  #Sum the total treatment of each system type
        totImpT += utildict[i]          #Add this to a global total at the same time
    
    for i in utildict.keys():
        if totImpT != 0:
            utildict[i] = float(utildict[i])/float(totImpT) * 100.0
        else:
            utildict[i] = 0
    
    return utildict
            

def calculateSelectFreq(wsuddata):
    """Calculates the selection frequency of all system types in a given list of WSUD assets
    
    Arguments:
        wsuddata -- list of dictionaries containing data from a WSUD shapefile (output from retrieveWSUDlayout())

    Outputs:
        sfdict -- dictionary of systems types, each with the associated Selection Frequency [%] in that particular strategy
                  format: sfdict = {"WSUR": x, "PB": x, "BF": x, ...}
    """
    sfdict = {}
    syscount = len(wsuddata)
            
    for t in SYSTYPES:              #For each system type    
        sfdict[t] = 0

    for t in range(len(wsuddata)):
        sfdict[wsuddata[t]["Type"]] += 1
    
    for t in sfdict.keys():
        sfdict[t] = float(sfdict[t])/float(syscount) * 100.0
        
    return sfdict


def calculateAttributeSum(wsuddata, attname):
    """Calculates the sum of an attribute (e.g. impervious treatment, etc.) for a particular WSUD
    layout. Usually used for "Aeff", "SysArea", "ImpT", "CurImpT". Function is a simple summation
    or attributes.    
    
    Arguments:
        wsuddata -- list of dictionaries containing data from a WSUD shapefile (output from retrieveWSUDlayout())
        attname -- the attribute name to sum up
        
    Outputs:
        areadict -- dictionary of systems types, each with associated Total Effective System surface ara [sqm] in that particular strategy
                    format: areadict = {"WSUR": x ,"PB": x, "BF: x, ...}
    """    
    areadict = {}
    
    for t in SYSTYPES:
        areadict[t] = 0
    
    for t in range(len(wsuddata)):
        areadict[wsuddata[t]["Type"]] += wsuddata[t][attname]
    
    return areadict
    

#Add scales analysis


#----- FUNCTIONS FOR EXPORTING ANALYSES TO COMMON FILE FORMATS -----##

def exportBoxPlotStats(results_fname, dictionaryarray):
    """Calculates and writes summary statistics for building boxplots to a .csv file.
    Users still need to use post-processing to plot the data.
    
    Arguments:
        results_fname -- full path and filename of the csv without extension
        **kwargs -- each additional argument is a summary array of dictionaries obtained from
                    running the 'calculate...' functions. The full use with three
                    attributes would be: Utilisation=utildict, SelectFreq=sfsdict, Areas=areadict
    
    Outputs:
        .csv summary file -- contains the min, max, percentiles, quartiles and median and outliers
    """        
    f = open(results_fname+".csv", 'w')
    
    f.write("Name, Min, 5th %ile, Q1, Median, Q3, 95th %ile, Max\n")

    datacompile = {}
    
    for i in dictionaryarray[0].keys():
        datacompile[i] = []
        for j in range(len(dictionaryarray)):
            datacompile[i].append(dictionaryarray[j][i])
   
    for i in datacompile.keys():
        linedata = str(results_fname)+str(i)+","
        linedata += str(numpy.min(datacompile[i]))+","
        linedata += str(numpy.percentile(datacompile[i], 5))+","
        linedata += str(numpy.percentile(datacompile[i], 25))+","
        linedata += str(numpy.median(datacompile[i]))+","
        linedata += str(numpy.percentile(datacompile[i], 75))+","
        linedata += str(numpy.percentile(datacompile[i], 95))+","
        linedata += str(numpy.max(datacompile[i]))+"\n"
        f.write(linedata)
    
    f.close()
    return True


def exportRawTableToCSV(results_fname, tablevar):
    """Writes a .csv file of a dictionary table based on its keys() and saves it to the
    computer.
    
    Arguments:
        results_fname -- full path and file name of the csv without extension
        tablevar -- dictionary variable containing the tabulated data
        
    Outputs:
        .csv file -- exports a .csv to the provided results_fname
    """
    if len(tablevar) == 0:
        return "Error, no data in Table"
        
    f = open(results_fname+".csv", 'w')
    
    #Write headings
    headingsline = ""
    attnames = tablevar[0].keys()
    for i in attnames:
        headingsline += i + ","
    headingsline.rstrip(',')
    f.write(headingsline + "\n")

    #Write data
    for i in range(len(tablevar)):
        dataline = ""
        for j in tablevar[i].keys():
            dataline += str(tablevar[i][j])+","
        dataline.rstrip(",")
        f.write(dataline + "\n")
    
    #Save the file
    f.close()
    

def exportAnalysisToCSV(results_fname, filenames, **kwargs):
    """Writes a summary .csv file of the analysed data sets. Export is scalable
    depending on how many different anlayses were done. Each line in the .csv contains
    summary statistics for an entire WSUD layout, e.g. 100 lines = 100 layouts analysed
    
    Arguments:
        results_fname -- full path and file name of the csv without extension
        filenames -- denotes all files analysed, inserted into the 1st column
        **kwargs -- each additional argument is a summary array of dictionaries obtained from
                    running the 'calculate...' functions. The full use with three
                    attributes would be: Utilisation=utildict, SelectFreq=sfsdict, Areas=areadict
                        
    Outputs:
        .csv summary file -- exports a .csv to the provided results_fname
    """
    datadict = {}    
    for key, value in kwargs.iteritems():
        datadict[key] = value       #{Utilisation: [ {WSUR:x, BF:y, ...}, {WSUR:x, ...} ] }
        
    f = open(results_fname+".csv", 'w')
    
    #Write headings
    headingsline = "Filename,"
    for i in datadict.keys():
        for j in datadict[i][0].keys():
            headingsline += str(i)+"_"+str(j)+","

    f.write(headingsline.rstrip(",")+"\n")
    
    for i in range(len(filenames)):
        datastring = str(filenames[i])+","
        for j in datadict.keys():
            curdict = datadict[j][i]
            for k in curdict.keys():
                datastring += str(curdict[k])+","
        
        f.write(datastring.rstrip(",")+"\n")
    
    f.close()
    return True


