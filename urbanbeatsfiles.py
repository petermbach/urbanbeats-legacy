# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 18:10:12 2013

@author: pbach
"""
import tarfile, os


def saveSimFile(activesim, filename):
    """Saves a .ubs file to the save location chosen by the user using the activesim object's information. The .ubs file
    is .tar archive with the extension *.ubs containing several text files that contain all the information relevant to
    setting up the project and simulation file:
        - projinfo.txt - project information (parameters entered when the project is first started, this file is
                        also relevant for determining size of several arrays and the number of modules to instantiate
        - dataarch.txt - data archive listing all data files currently in the data browser of the project including their
                        type (e.g. land use, elevation, etc.)
        - pcycledata.txt & icycledata.txt & perfdata.txt - the data currently set for each cycle in the simulation
        - outputcfg.txt - all parameters relating to the outputs requested from UrbanBEATS by the user for the current
                        simulation
        - narrative.txt - narratives for each of the cycles, this is the context-specific information of the proejct that
                        the user entered for each snapshot or time period
        - delinblocks.txt - parameters for delinblocks module
        - urbplanbb.txt - parameters for urbplanbb module(s), read as an array of parameters and can be easily re-assigned
                        based on cycle
        - techplacement.txt - parameters for techplacement module(s), read as an array of parameters and can be easily
                        re-assigned based on cycle
        - techimplement.txt - parameters for techimplement module(s), read as an array of parameters and can be easily
                        re-assigned based on cycle
        - perfassess.txt - parameters for performance assessment module(s)

    Note that for the module files, one txt is created per instantiation of module, filenames delimited with an index
    number representing the tabindex.
    """
    tempfiles = []
    directory = os.path.dirname(str(filename))
    if os.path.exists(str(filename)): os.remove(str(filename))
    archive = tarfile.open(str(filename), 'w')     #creates the tar archive

    #Create the individual text files in the same location, then add to the tar archive - *||* is used as delimiter
    if os.path.exists(directory+"/projinfo.txt"): os.remove(directory+"/projinfo.txt")
    f = open(directory+"/projinfo.txt", 'w')
    projdetails = activesim.getProjectDetails() #Obtains the project information dictionary
    for keys in projdetails.keys():
        f.write(keys+"*||*"+str(projdetails[keys])+"*||*\n")
    f.close()
    archive.add(directory+"/projinfo.txt", arcname="projinfo.txt")
    tempfiles.append("projinfo.txt")    #---END OF PROJECT FILE DATA SAVE

    if os.path.exists(directory+"/dataarch.txt"): os.remove(directory+"/dataarch.txt")
    f = open(directory+"/dataarch.txt", 'w')
    dataarchive = activesim.showDataArchive()   #Obtains the data archive dictionary
    for datatype in dataarchive.keys():
        f.write(str(datatype)+"*||*\n")
        for files in dataarchive[datatype]:
            f.write(str(files)+"*||*\n")
        f.write("---eol---\n")  #End of line marker for that particular data type, file is read until this is encountered
    f.close()
    archive.add(directory+"/dataarch.txt", arcname="dataarch.txt")
    tempfiles.append("dataarch.txt")    #---END OF DATA ARCHIVE DATA SAVE

    if os.path.exists(directory+"/narrative.txt"): os.remove(directory+"/narrative.txt")
    f = open(directory+"/narrative.txt", 'w')
    narratives = activesim.getAllNarratives()       #Obtains all narratives, one narrative per line on the file
    for line in range(len(narratives)):
        nar = narratives[line]
        f.write(str(nar[0]+"*||*"+nar[1]+"*||*\n"))
    f.close()
    archive.add(directory+"/narrative.txt", arcname="narrative.txt")
    tempfiles.append("narrative.txt")

    if os.path.exists(directory+"/outputcfg.txt"): os.remove(directory+"/outputcfg.txt")
    f = open(directory+"/outputcfg.txt", 'w')
    gisoptions = activesim.getGISExportDetails()
    #reportoptions = activesim.getReportingOptions()
    for keys in gisoptions.keys():
        f.write(str(keys)+"*||*"+str(gisoptions[keys])+"*||*\n")
    #for keys in reportoptions.keys():
        #f.write(str(keys)+"*||*"+str(reportoptions[keys])+"\n")
    f.close()
    archive.add(directory+"/outputcfg.txt", arcname="outputcfg.txt")
    tempfiles.append("outputcfg.txt")

    if os.path.exists(directory+"/reportcfg.txt"): os.remove(directory+"/reportcfg.txt")
    f = open(directory+"/reportcfg.txt", 'w')
    reportoptions = activesim.getReportingOptions()
    for keys in reportoptions.keys():
        f.write(str(keys)+"*||*"+str(reportoptions[keys])+"*||*\n")
    f.close()
    archive.add(directory+"/reportcfg.txt", arcname="reportcfg.txt")
    tempfiles.append("reportcfg.txt")

    #Transfer Data Arrays into three separate text files for planning, implementation and performance assessment cycles
    datafname = ["pcycledata.txt", "icycledata.txt", "perfdata.txt"]
    datacycles = ["pc", "ic", "pa"]
    for i in range(len(datafname)):
        fname = datafname[i]
        cycle = datacycles[i]
        dataarray = activesim.getAllCycleDataSets(cycle)
        if len(dataarray) == 0:     #If the array is empty, that data cycle is not featured
            continue    #Skip saving that particular file

        if os.path.exists(directory+"/"+fname): os.remove(directory+"/"+fname)
        f = open(directory+"/"+fname, 'w')
        for j in range(len(dataarray)):
            f.write("TabIndex"+str(j)+"*||*\n")
            data = dataarray[j]
            for k in data.keys():
                f.write(str(k)+"*||*"+str(data[k])+"*||*\n")
            f.write("---eol---\n")
        f.close()
        archive.add(directory+"/"+fname, arcname=fname)
        tempfiles.append(fname)

    #Transfer Module Data into separate files for each module
    #---DELINBLOCKS----
    if os.path.exists(directory+"/delinblocks.txt"): os.remove(directory+"/delinblocks.txt")
    f = open(directory+"/delinblocks.txt", 'w')
    delinblocksmodule = activesim.getModuleDelinblocks()
    parameters = delinblocksmodule.getModuleParameterList()
    for i in parameters.keys():
        f.write(str(i)+"*||*"+str(delinblocksmodule.__dict__[i])+"*||*\n")
    f.close()
    archive.add(directory+"/delinblocks.txt", arcname="delinblocks.txt")
    tempfiles.append("delinblocks.txt")

    #---OTHER PLANNING-SUPPORT MODULES----
    modulefnames = {"urbplanbb":activesim.getModuleUrbplanbb,
                    "techplacement":activesim.getModuleTechplacement,
                    "techimplement":activesim.getModuleTechimplement}
    for modname in modulefnames.keys():
        modules = modulefnames[modname](9999)   #Calls the representative function
        for i in range(len(modules)):
            fname = str(modname)+str(i)+".txt"
            if os.path.exists(directory+"/"+fname): os.remove(directory+"/"+fname)
            f = open(directory+"/"+fname, 'w')
            curmodule = modules[i]
            parameters = curmodule.getModuleParameterList()
            for par in parameters.keys():
                f.write(str(par)+"*||*"+str(curmodule.__dict__[par])+"*||*\n")
            f.close()
            archive.add(directory+"/"+fname, arcname=fname)
            tempfiles.append(fname)

    #Save the archive and finish up
    archive.close()
    for file in tempfiles:
        if os.path.exists(directory+"/"+file): os.remove(directory+"/"+file)
    return True

def getSimFileProjectPath(filename):
    archive = tarfile.open(str(filename), 'r')
    f = archive.extractfile("projinfo.txt")
    for lines in f:
        data = lines.split("*||*")
        if str(data[0]) == "projectpath":
            return str(data[1])
    return ""   #If that attribute is not in the savefile, then simply create a new one

def loadSimFile(activesim, filename, projectpath):
    archive = tarfile.open(str(filename), 'r')
    #Retrieve Project Details
    projectinfo = {}
    f = archive.extractfile("projinfo.txt")
    for lines in f:
        data = lines.split("*||*")
        projectinfo[str(data[0])] = str(data[1])
    for key in projectinfo.keys():
        activesim.setParameter(key, type(activesim.getParameter(key))(projectinfo[key]))
    f.close()
    activesim.setParameter("projectpath", str(projectpath))
    activesim.initializeSimulationCore()
    activesim.setActiveProjectPath(projectpath)
    activesim.setFullFileName(filename)
    #Restore Data Archive
    f = archive.extractfile("dataarch.txt")     #Category, then read lines until '---eol---'
    dataarray = []
    categories = []
    for lines in f:
        dataarray.append(lines.split('*||*'))
    category = dataarray[0][0]
    i = 1
    while i <= (len(dataarray)-1):
        if 'eol' in dataarray[i][0]:
            i += 1
            if i < len(dataarray):
                category = dataarray[i][0]
                i += 1
                continue
            else:
                continue
        activesim.addDataToArchive(category, dataarray[i][0])
        i += 1
    f.close()

    #Restore Narratives
    f = archive.extractfile("narrative.txt")
    tabindex = 0
    for lines in f:
        nar = lines.split('*||*')
        activesim.setNarrative(tabindex, [nar[0], nar[1]])
        tabindex += 1
    f.close()

    #Write project output options into file
    outputoptions = {}
    f = archive.extractfile("outputcfg.txt")
    for lines in f:
        data = lines.split("*||*")
        outputoptions[str(data[0])] = str(data[1])
    #Now transfer to gisexportoptions and other options
    gisoptions = activesim.getGISExportDetails()
    for keys in gisoptions.keys():
        activesim.setGISExportDetails(keys, type(gisoptions[keys])(outputoptions[keys]))
    f.close()

    reportingoptions = {}
    reporttemplate = activesim.getReportingOptions()
    f = archive.extractfile("reportcfg.txt")
    for lines in f:
        data = lines.split("*||*")
        if data[0] == "SectionInclude":
            data[1] = data[1].split(",")
            data[1][0] = data[1][0].strip("[")
            data[1][len(data[1])-1] = data[1][len(data[1])-1].strip("]")
            for i in range(len(data[1])):
                data[1][i] = int(data[1][i])
            reportingoptions[str(data[0])] = data[1]
        else:
            reportingoptions[str(data[0])] = type(reporttemplate[str(data[0])])(data[1])
    activesim.setReportingOptions(reportingoptions)

    #Set Cycle Data Sets
    datafname = ["pcycledata.txt", "icycledata.txt", "perfdata.txt"]
    datacycles = ["pc", "ic", "pa"]
    for i in range(len(datafname)):
        fname = datafname[i]
        #print fname
        cycle = datacycles[i]
        #print archive.getnames()
        if fname not in archive.getnames():   #if the datafname file is not in the archive, skip
            continue
        f = archive.extractfile(fname)
        dataarray = []  #transfer data to an array
        for lines in f:
            dataarray.append(lines)

        tabindex = 0 #counter
        j = 1   #Skip the first line
        dataset = {}    #individual data sets for different cycles
        while j <= len(dataarray):
            if 'eol' in dataarray[j]:        #If an 'end of line' is encountered, set data set
                activesim.setCycleDataSet(cycle, tabindex, dataset, "F")
                #print dataset
                dataset = {}
                tabindex += 1
                j += 2  #Skips two lines ahead (the next header onto the first line
                continue
            line = dataarray[j].split("*||*")
            #print line
            dataset[line[0]] = line[1]
            j += 1
        f.close()

    #Update modules
    delinblocksmodule = activesim.getModuleDelinblocks()
    moduledata = {}
    f = archive.extractfile("delinblocks.txt")
    for lines in f:
        data = lines.split("*||*")
        moduledata[data[0]] = data[1]
    for keys in moduledata.keys():
        #print keys, moduledata[keys], type(delinblocksmodule.getParameter(keys))
        if type(delinblocksmodule.getParameterType(keys)) == 'BOOL':
            delinblocksmodule.setParameter(keys, type(delinblocksmodule.getParameter(keys))(int(moduledata[keys])))
        else:
            delinblocksmodule.setParameter(keys, type(delinblocksmodule.getParameter(keys))(moduledata[keys]))
    f.close()

    modulenames = {"urbplanbb":activesim.getModuleUrbplanbb,
                    "techplacement":activesim.getModuleTechplacement,
                    "techimplement":activesim.getModuleTechimplement}

    for modname in modulenames.keys():
        modules = modulenames[modname](9999)
        for i in range(len(modules)):
            curmodule = modules[i]
            moduledata = {}
            fname = str(modname)+str(i)+".txt"
            f = archive.extractfile(fname)
            for lines in f:
                data = lines.split("*||*")
                moduledata[data[0]] = data[1]
            for keys in moduledata.keys():
                #print keys, (moduledata[keys]), type(curmodule.getParameter(keys))
                if curmodule.getParameterType(keys) == 'BOOL':
                    curmodule.setParameter(keys, type(curmodule.getParameter(keys))(int(float(moduledata[keys]))))
                elif curmodule.getParameterType(keys) == 'STRING':
                    curmodule.setParameter(keys, type(curmodule.getParameter(keys))(moduledata[keys]))
                else:
                    curmodule.setParameter(keys, type(curmodule.getParameter(keys))(float(moduledata[keys])))
            f.close()

    archive.close()
    return True

def exportDataArchiveFile(activesim, filename):
    """Saves the current data archive to a separate file, which can be independently imported into a new project. This
    saves the user from reloading the data archive. The file extension is .uda for "UrbanBEATS Data Archive"
    """
    if os.path.exists(str(filename)): os.remove(str(filename))
    f = open(str(filename), 'w')
    dataarchive = activesim.showDataArchive()   #Obtains the data archive dictionary
    for datatype in dataarchive.keys():
        f.write(str(datatype)+"*||*\n")
        for files in dataarchive[datatype]:
            f.write(str(files)+"*||*\n")
        f.write("---eol---\n")  #End of line marker for that particular data type, file is read until this is encountered
    f.close()
    return True

def importDataArchiveFile(activesim, filename, filetype):
    """Loads the data archive from a specific file (filetype = 'uda') or project (filetype = 'ubs') and adds
    whatever is available to the existing data archive."""
    if filetype == "ubs":   #Code to extract archive file from the project archive
        arch = tarfile.open(str(filename), 'r')
        f = arch.extractfile("dataarch.txt")     #Category, then read lines until '---eol---'
    elif filetype == "uda": #Code to load the file as per normal
        f = open(filename, 'r')     #Category, then read lines until '---eol---'

    else:
        return True
    dataarray = []
    for lines in f:
        dataarray.append(lines.split('*||*'))
    category = dataarray[0][0]      #Set the initial category
    i = 1
    while i <= (len(dataarray)-1):
        if 'eol' in dataarray[i][0]:
            i += 1
            if i < len(dataarray):
                category = dataarray[i][0]
                i += 1
                continue
            else:
                continue
        activesim.addDataToArchive(category, dataarray[i][0])
        i += 1
    f.close()

    if filetype == "ubs": arch.close()
    return True

def readGlobalOptionsConfig(root_directory):
    """Reads the config file of global options and returns the dictionary of global options."""
    global_options = {}
    f = open(root_directory+"/config.cfg",'r')
    if f == None:
        resetGlobalOptions()
        f = open(root_directory+"/config.cfg",'r')
    for lines in f:
        if lines == "":
            continue
        line = lines.rstrip("\n")
        line = line.split("*||*")
        global_options[line[0]] = type(default_global_options[line[0]])(line[1])
    f.close()
    return global_options

def updateCFGFromOptions(newoptions, root_directory):
    """Updates the configuration of the program and its simulations by overwriting the config file"""
    f = open(root_directory+"/config.cfg", 'w')
    for entry in newoptions.keys():
        f.write(str(entry)+"*||*"+str(newoptions[entry])+"\n")
    f.close()
    return True

def resetGlobalOptions(root_directory):
    """Resets the .cfg file in the root directory to the original options"""
    f = open(root_directory+"/config.cfg", 'w')
    for key in default_global_options.keys():
        f.write(str(key)+"*||*"+str(default_global_options[key])+"\n")
    f.close()
    return True

default_global_options = {"defaultmodeller": "<none>", "defaultaffil":"<none>", "iterations":1000, "city": "Melbourne",
                      "decisiontype":"H", "numstrats":5,  "MUSICwrite":1, "MUSICauto":0, "MUSICpath":"", "MUSICver":"Version5", "MUSICtte":0,
                      "MUSICflux":0, "mapstyle":"Style1", "tileserverURL":"", "gearth_path": "", "gearth_auto": 0}
