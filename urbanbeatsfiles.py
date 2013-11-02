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
        - pcycledata.txt & icycledata.txt - the data currently set for each cycle in the simulation
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

    Note that for the module files, one txt is created per instantiation of module, filenames delimited with an index
    number representing the tabindex.
    """
    tempfiles = []
    archive = tarfile.open(filename, 'w')     #creates the tar archive

    #Create the individual text files in the same location, then add to the tar archive - *||* is used as delimiter
    f = open("projinfo.txt", 'w')
    projdetails = activesim.getProjectDetails() #Obtains the project information dictionary
    for keys in projdetails.keys():
        f.write(keys+"*||*"+str(projdetails[keys])+"\n")
    f.close()
    archive.add("projinfo.txt")
    tempfiles.append("projinfo.txt")    #---END OF PROJECT FILE DATA SAVE

    f = open("dataarch.txt", 'w')
    dataarchive = activesim.showDataArchive()   #Obtains the data archive dictionary
    for datatype in dataarchive.keys():
        f.write(str(datatype)+"\n")
        for files in dataarchive[datatype]:
            f.write(str(files)+"\n")
        f.write("---eol---\n")  #End of line marker for that particular data type, file is read until this is encountered
    f.close()
    archive.add("dataarch.txt")
    tempfiles.append("dataarch.txt")    #---END OF DATA ARCHIVE DATA SAVE

    f = open("narrative.txt", 'w')
    narratives = activesim.getAllNarratives()       #Obtains all narratives, one narrative per line on the file
    for line in range(len(narratives)):
        nar = narratives[line]
        f.write(str(nar[0]+"*||*"+nar[1]+"\n"))
    f.close()
    archive.add("narrative.txt")
    tempfiles.append("narrative.txt")

    f = open("outputcfg.txt", 'w')
    gisoptions = activesim.getGISExportDetails()
    #reportoptions = activesim.getReportingOptions()
    for keys in gisoptions.keys():
        f.write(str(keys)+"*||*"+str(gisoptions[keys])+"\n")
    #for keys in reportoptions.keys():
        #f.write(str(keys)+"*||*"+str(reportoptions[keys])+"\n")
    f.close()
    archive.add("outputcfg.txt", 'w')
    tempfiles.append("outputcfg.txt", 'w')

    #Transfer Data Arrays into three separate text files for planning, implementation and performance assessment cycles
    datafname = ["pcycledata.txt", "icycledata.txt", "perfdata.txt"]
    datacycles = ["pc", "ic", "pa"]
    for i in range(len(datafname)):
        fname = datafname[i]
        cycle = datacycles[i]
        f = open(fname, 'w')
        dataarray = activesim.getAllCycleDataSets(cycle)
        for j in range(len(dataarray)):
            f.write("TabIndex"+str(j)+"\n")
            data = dataarray[j]
            for k in data.keys():
                f.write(str(k)+"*||*"+str(data[k])+"\n")
            f.write("---eol---\n")
        f.close()
        archive.add(fname)
        tempfiles.append(fname)

    #Transfer Module Data into separate files for each module
    #---DELINBLOCKS----
    f = open("delinblocks.txt", 'w')
    delinblocksmodule = activesim.getModuleDelinblocks()
    parameters = delinblocksmodule.getModuleParameterList()
    for i in parameters.keys():
        f.write(str(i)+"*||*"+str(parameters[i])+"*||*"+str(delinblocksmodule.__dict__[i])+"\n")
    f.close()
    archive.add("delinblocks.txt")
    tempfiles.append("delinblocks.txt")

    #---OTHER PLANNING-SUPPORT MODULES----
    #modulefnames = {"urbplanbb":activesim.getModuleUrbplanbb,
    #                "techplacement":activesim.getModuleTechplacement,
    #                "techimplement":activesim.getModuleTechimplement}
    #for i in range(len(modulefnames)):
    #    fname = modulefname[i]


    #Save the archive and finish up
    archive.close()
    for file in tempfiles:
        if os.path.exists(file): os.remove(file)
    return True
#
#def getCompleteCycleString(modulevector, parametername):
#    stringoutput = str(parametername)+";"
#    for i in modulevector:
#        if type(i.getParameter(parametername)) == bool:
#            stringoutput += str(int(i.getParameter(parametername)))+";"
#        else:
#            stringoutput += str(i.getParameter(parametername))+";"
#    stringoutput.rstrip(';')
#    stringoutput += "\n"
#    return stringoutput

def loadSimFile(activesim, filename):


    return True

#    simulationdetails = {}
#    simdataarchive = {"Elevation" : [],               "Soil" : [],                "Land Use" : [],
#                      "Population" : [],              "Employment" : [],          "Planning" : [],
#                      "Locality" : [],                "Groundwater" : [],         "Rivers" : [],
#                      "Lakes" : [],                   "Social Parameters" : [],   "Existing Systems" : [],
#                      "Rainfall" : [],                "Evapotranspiration" : [],  "Solar Radiation" : []                }       #will contain the full library
#    md_delinblocks = {}
#    md_urbplanbb = {}
#    md_techplace = {}
#    md_techimpl = {}
#    md_perf = {}
#    line = 0
#    f = open(filename, 'r')
#    while str(line) != "--- PROJECT INFO ---\n":
#        line = f.readline()
#    #print "Before project info"
#    #--- PROJECT INFO ---
#    lines = readUntil(f, "--- DATA ARCHIVE ---\n")
#    simulationdetails = transferFileDataToDict(lines, simulationdetails)
#
#    staticsimfeatures = [int(simulationdetails["static_ubpconstant"]), \
#                         int(simulationdetails["static_techplaninclude"]),\
#                         int(simulationdetails["static_techplanconstant"]),\
#                         int(simulationdetails["static_techimplinclude"]),\
#                         int(simulationdetails["static_techimplconstant"]),\
#                         int(simulationdetails["static_perfinclude"])]
#    simulationdetails["staticsimfeatures"] = staticsimfeatures
#    staticdataoptions = [int(simulationdetails["static_mapchange"]),\
#                         int(simulationdetails["static_climateconstant"])]
#    simulationdetails["staticdataoptions"] = staticdataoptions
#    dynsimfeatures = [int(simulationdetails["dyn_ubpconstant"]),\
#                      int(simulationdetails["dyn_techplanconstant"]),\
#                      int(simulationdetails["dyn_techimplconstant"]),\
#                      int(simulationdetails["dyn_perfinclude"]),\
#                      int(simulationdetails["dyn_perfconstant"])]
#    simulationdetails["dynsimfeatures"] = dynsimfeatures
#
#    dyndatafeatures = [int(simulationdetails["dyn_mplanconstant"]),\
#                       int(simulationdetails["dyn_climateconstant"])]
#    simulationdetails["dyndatafeatures"] = dyndatafeatures
#
#    #--- DATA ARCHIVE ---
#    f.readline()
#    f.readline()
#    f.readline()    #Read the three lines that make up the Table's header
#    lines = readUntil(f, "--- OUTPUT OPTIONS ---\n")
#    simdatadict = {}
#    for i in lines:
#        i = i.strip("\n")
#        datasplit = i.split(";")
#        if len(i) > 1:
#            simdataarchive[str(datasplit[1])].append(str(datasplit[2]))
#            simdatadict[int(datasplit[0])] = [str(datasplit[1]),str(datasplit[2])]
#    #print simdataarchive
#    #print simdatadict
#    #--- OUTPUT OPTIONS ---
#    lines = readUntil(f, "--- CYCLE DATA SETS ---\n")
#    simulationdetails = transferFileDataToDict(lines, simulationdetails)
#
#    #--- CYCLE DATA SETS ---
#    f.readline()
#    f.readline()
#    f.readline()    #Read the next three lines of Table Header
#    lines = readUntil(f, "--- DELINBLOCKS PARAMETERS ---\n")
#    activedataitemspc = []
#    activedataitemsic = []
#    activedataitemspa = []
#
#    lineindex = 0
#    for i in lines:
#        i = i.strip("\n")
#        i = i.split(";")
#
#        if len(i) <= 1:
#            continue
#        for cols in range(len(i)):
#            if cols == 0 or i[cols] == 'none':
#                continue
#            i[cols] = i[cols].split(",")        #Will give something like [0, [1, 3, 5, 6], [4, 6, 6, 2], 'none']
#            for values in range(len(i[cols])):
#                i[cols][values] = int(i[cols][values])
#
#        activedataitemspc.append({})        #activedataitems = [ {dictionary 1}, {dictionary 2}, {dictionary 3}]
#        if i[1] != 'none':                  #{dictionary1} = {Elevation: file, Land Use: file, ...}
#            for selection in i[1]:
#                activedataitemspc[lineindex][simdatadict[int(selection)][0]] = simdatadict[int(selection)][1]     #simdatadict[selection][0] = label of data type e.g. "Elevation"
#                                                                                                #simdatadict[selection][1] = filename
#        activedataitemsic.append({})
#        if i[2] != 'none':
#            for selection in i[2]:
#                activedataitemsic[lineindex][simdatadict[int(selection)][0]] = simdatadict[int(selection)][1]
#
#        activedataitemspa.append({})
#        if i[3] != 'none':
#            for selection in i[3]:
#                activedataitemspa[lineindex][simdatadict[int(selection)][0]] = simdatadict[int(selection)][1]
#        #print "Set Cycle Data Variables"
#        lineindex += 1
#        #END OF FOR LOOP
#
#    #simulationdetails = transferFileDataToDict(lines, simulationdetails)
#
#    #--- DELINBLOCKS PARAMETERS ---
#    lines = readUntil(f, "--- URBAN PLANNING PARAMETERS (PLANNING) ---\n")
#    md_delinblocks = transferFileDataToDict(lines, md_delinblocks)
#
#    #--- URBAN PLANNING PARAMETERS ---
#    lines = readUntil(f, "--- TECHNOLOGY PLANNING PARAMETERS ---\n")
#    md_urbplanbb = transferFileDataToDict(lines, md_urbplanbb)
#    #--- TECHNOLOGY PLANNING PARAMETERS ---
#
#    #--- TECHNOLOGY IMPLEMENTATION PARAMETERS ---
#
#    f.close()
#
#    #Transfer Project Details data
#    projectdetails = activesim.getProjectDetails()
#    for key in projectdetails:
#        try:
#            #print projectdetails[key]
#            #print simulationdetails[key]
#            projectdetails[key] = type(projectdetails[key])(simulationdetails[key])
#        except KeyError:
#            print "WARNING, project file does not contain info about: "+str(key)
#    #Transfer data library data
#    dataarchive = activesim.showDataArchive()
#    for key in dataarchive:
#        try:
#            dataarchive[key] = simdataarchive[key]
#        except KeyError:
#            print "ATTENTION, no "+str(key)+" data specified"
#
#    #Transfer output options
#    gisoutputs = activesim.getGISExportDetails()
#    for key in gisoutputs:
#        try:
#            if type(gisoutputs[key]) == bool:
#                gisoutputs[key] = type(gisoutputs[key])(int(simulationdetails[key]))
#            else:
#                gisoutputs[key] = type(gisoutputs[key])(simulationdetails[key])
#        except KeyError:
#            print "WARNING, project file does not contain info about: "+str(key)
#
#    return simulationdetails, activedataitemspc, activedataitemsic, activedataitemspa, md_delinblocks, md_urbplanbb, md_techplace, md_techimpl, md_perf
#
#def transferFileDataToDict(lines, simdict):
#    for i in lines:
#        i = i.strip("\n")
#        datasplit = i.split(";")
#        #print datasplit
#        if len(datasplit) > 1 and len(datasplit) == 2:
#            simdict[str(datasplit[0])] = datasplit[1]
#        else:
#            simdict[str(datasplit[0])] = datasplit[1:]

def readUntil(fname, label):
    lines = []
    line = ""
    while str(line) != label:
        line = fname.readline()
        if str(line) != label:
            lines.append(line)
    return lines