# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 18:10:12 2013

@author: pbach
"""

def saveSimFile(activesim, filename):
    f = open(filename, 'w')
    f.write("----------------------------------------------------------------------------------------\n")
    f.write("UrbanBEATS v1.0 Simulation Setup File\n")
    f.write("----------------------------------------------------------------------------------------\n")
    f.write("==============\n")
    f.write("Parameter List\n")
    f.write("==============\n\n")
    f.write("--- PROJECT INFO ---\n")
    
    projectinfo = activesim.getProjectDetails()
    simtype = projectinfo["simtype"]
    for key in projectinfo:
        if key in ["staticsimfeatures", "staticdataoptions", "dynsimfeatures", "dyndatafeatures"]:
            continue
        f.write(str(key)+";"+str(projectinfo[key])+"\n")
    f.write("static_ubpconstant;"+str(projectinfo["staticsimfeatures"][0])+"\n")
    f.write("static_techplaninclude;"+str(projectinfo["staticsimfeatures"][1])+"\n")
    f.write("static_techplanconstant;"+str(projectinfo["staticsimfeatures"][2])+"\n")
    f.write("static_techimplinclude;"+str(projectinfo["staticsimfeatures"][3])+"\n")
    f.write("static_techimplconstant;"+str(projectinfo["staticsimfeatures"][4])+"\n")
    f.write("static_perfinclude;"+str(projectinfo["staticsimfeatures"][5])+"\n")
    f.write("static_mapchange;"+str(projectinfo["staticdataoptions"][0])+"\n")
    f.write("static_climateconstant;"+str(projectinfo["staticdataoptions"][1])+"\n")
    f.write("dyn_ubpconstant;"+str(projectinfo["dynsimfeatures"][0])+"\n")
    f.write("dyn_techplanconstant;"+str(projectinfo["dynsimfeatures"][1])+"\n")
    f.write("dyn_techimplconstant;"+str(projectinfo["dynsimfeatures"][2])+"\n")
    f.write("dyn_perfinclude;"+str(projectinfo["dynsimfeatures"][3])+"\n")
    f.write("dyn_perfconstant;"+str(projectinfo["dynsimfeatures"][4])+"\n")
    f.write("dyn_mplanconstant;"+str(projectinfo["dyndatafeatures"][0])+"\n")
    f.write("dyn_climateconstant;"+str(projectinfo["dyndatafeatures"][1])+"\n")
     
    f.write("\n")
    f.write("--- DATA ARCHIVE ---\n")
    f.write("=====================================================================================================================\n")
    f.write("Id;Type;Filename\n")
    f.write("=====================================================================================================================\n")
    dataarchive = activesim.showDataArchive()
    indexcounter = 1
    savedatadict = []
    for key in dataarchive:
        for entries in dataarchive[key]:
            f.write(str(indexcounter)+";"+str(key)+";"+str(entries)+"\n")
            savedatadict.append(entries)     #FOR cycle data, index the entry in the list --> index is indexed + 1
            indexcounter += 1
    f.write("\n")
    f.write("--- OUTPUT OPTIONS ---\n")
    outputoptions = activesim.getGISExportDetails()
    for key in outputoptions:
        f.write(str(key)+";"+str(outputoptions[key])+"\n")
    f.write("\n")
    f.write("--- CYCLE DATA SETS ---\n")
    f.write("====================================\n")
    f.write("Cyc;Planning;Implement;Climate\n")
    f.write("====================================\n")
    pc_data = activesim.getAllCycleDataSets("pc")
    ic_data = activesim.getAllCycleDataSets("ic")
    pa_data = activesim.getAllCycleDataSets("pa")

    #print pc_data
    #print ic_data
    #print savedatadict    
    
    if simtype == "S":
        cycles = projectinfo["static_snapshots"]
    elif simtype == "D":
        cycles = projectinfo["dyn_breaks"]+1
    else:
        cycles = 1
    for i in range(int(cycles)):
        if len(pc_data) == 1:
            pc_current = pc_data[0]
        else:
            pc_current = pc_data[i]
        if len(ic_data) == 1:
            ic_current = ic_data[0]
        else:
            ic_current = ic_data[i]
        if len(pa_data) == 1:
            pa_current = pa_data[0]
        else:
            pa_current = pa_data[1]
        pcstring = ""
        icstring = ""
        pastring = ""
        if len(pc_current) == 0:
            pcstring = "none"
        else:
            for keys in pc_current:
                findex = savedatadict.index(pc_current[keys]) + 1
                pcstring += str(findex)+","
            pcstring = pcstring.strip(',')
        if len(ic_current) == 0:
            icstring = "none"
        else:
            for keys in ic_current:
                findex = savedatadict.index(ic_current[keys]) + 1
                icstring += str(findex)+","
            icstring = icstring.strip(',')
        if len(pa_current) == 0:
            pastring = "none"
        else:
            for keys in pa_current:
                findex = savedatadict.index(pa_current[keys]) + 1
                pastring += str(findex)+","
            pastring = pastring.strip(',')
        f.write(str(i)+";"+pcstring+";"+icstring+";"+pastring+"\n")
            
    #Code for cycle data sets
    f.write("\n")
    f.write("--- DELINBLOCKS PARAMETERS ---\n")
    delinblocksmod = activesim.getModuleDelinblocks()    
    f.write("BlockSize"+";"+str(delinblocksmod.getParameter("BlockSize"))+"\n")
    f.write("blocksize_auto"+";"+str(int(delinblocksmod.getParameter("blocksize_auto")))+"\n")
    f.write("popdatatype"+";"+str(delinblocksmod.getParameter("popdatatype"))+"\n")
    f.write("soildatatype"+";"+str(delinblocksmod.getParameter("soildatatype"))+"\n")
    f.write("soildataunits"+";"+str(delinblocksmod.getParameter("soildataunits"))+"\n")
    f.write("elevdatadatum"+";"+str(delinblocksmod.getParameter("elevdatadatum"))+"\n")
    f.write("elevdatacustomref"+";"+str(delinblocksmod.getParameter("elevdatacustomref"))+"\n")
    f.write("include_plan_map"+";"+str(int(delinblocksmod.getParameter("include_plan_map")))+"\n")
    f.write("include_local_map"+";"+str(int(delinblocksmod.getParameter("include_local_map")))+"\n")
    f.write("include_employment"+";"+str(int(delinblocksmod.getParameter("include_employment")))+"\n")
    f.write("jobdatatype"+";"+str(delinblocksmod.getParameter("jobdatatype"))+"\n")
    f.write("include_rivers"+";"+str(int(delinblocksmod.getParameter("include_rivers")))+"\n")
    f.write("include_lakes"+";"+str(int(delinblocksmod.getParameter("include_lakes")))+"\n")
    f.write("include_groundwater"+";"+str(int(delinblocksmod.getParameter("include_groundwater")))+"\n")
    f.write("groundwater_datum"+";"+str(delinblocksmod.getParameter("groundwater_datum"))+"\n")
    f.write("include_soc_par1"+";"+str(int(delinblocksmod.getParameter("include_soc_par1")))+"\n")
    f.write("include_soc_par2"+";"+str(int(delinblocksmod.getParameter("include_soc_par2")))+"\n")
    f.write("social_par1_name"+";"+str(delinblocksmod.getParameter("social_par1_name"))+"\n")
    f.write("social_par2_name"+";"+str(delinblocksmod.getParameter("social_par2_name"))+"\n")
    f.write("socpar1_type"+";"+str(delinblocksmod.getParameter("socpar1_type"))+"\n")
    f.write("socpar2_type"+";"+str(delinblocksmod.getParameter("socpar2_type"))+"\n")
    f.write("patchdelin"+";"+str(int(delinblocksmod.getParameter("patchdelin")))+"\n")
    f.write("spatialmetrics"+";"+str(int(delinblocksmod.getParameter("spatialmetrics")))+"\n")
    f.write("Neighbourhood"+";"+str(delinblocksmod.getParameter("Neighbourhood"))+"\n")
    f.write("vn4FlowPaths"+";"+str(int(delinblocksmod.getParameter("vn4FlowPaths")))+"\n")
    f.write("vn4Patches"+";"+str(int(delinblocksmod.getParameter("vn4Patches")))+"\n")
    f.write("flow_method"+";"+str(delinblocksmod.getParameter("flow_method"))+"\n")
    f.write("demsmooth_choose"+";"+str(int(delinblocksmod.getParameter("demsmooth_choose")))+"\n")
    f.write("demsmooth_passes"+";"+str(delinblocksmod.getParameter("demsmooth_passes"))+"\n")
    f.write("considerCBD"+";"+str(int(delinblocksmod.getParameter("considerCBD")))+"\n")
    f.write("locationOption"+";"+str(delinblocksmod.getParameter("locationOption"))+"\n")
    f.write("locationCity"+";"+str(delinblocksmod.getParameter("locationCity"))+"\n")
    f.write("locationLong"+";"+str(delinblocksmod.getParameter("locationLong"))+"\n")
    f.write("locationLat"+";"+str(delinblocksmod.getParameter("locationLat"))+"\n")
    f.write("marklocation"+";"+str(int(delinblocksmod.getParameter("marklocation")))+"\n")
    f.write("\n")
    f.write("--- URBAN PLANNING PARAMETERS (PLANNING) ---\n")
    urbplanbbmod = activesim.getModuleUrbplanbb(9999)    
    f.write(getCompleteCycleString(urbplanbbmod, "cityarchetype"))
    f.write(getCompleteCycleString(urbplanbbmod, "citysprawl"))
    f.write(getCompleteCycleString(urbplanbbmod, "locality_mun_trans"))
    f.write(getCompleteCycleString(urbplanbbmod, "lucredev"))
    f.write(getCompleteCycleString(urbplanbbmod, "popredev"))
    f.write(getCompleteCycleString(urbplanbbmod, "lucredev_thresh"))
    f.write(getCompleteCycleString(urbplanbbmod, "popredev_thresh"))
    f.write(getCompleteCycleString(urbplanbbmod, "noredev"))
    f.write(getCompleteCycleString(urbplanbbmod, "occup_avg"))
    f.write(getCompleteCycleString(urbplanbbmod, "occup_max"))
    f.write(getCompleteCycleString(urbplanbbmod, "person_space"))
    f.write(getCompleteCycleString(urbplanbbmod, "extra_comm_area"))
    f.write(getCompleteCycleString(urbplanbbmod, "setback_f_min"))
    f.write(getCompleteCycleString(urbplanbbmod, "setback_f_max"))
    f.write(getCompleteCycleString(urbplanbbmod, "setback_s_min"))
    f.write(getCompleteCycleString(urbplanbbmod, "setback_s_max"))
    f.write(getCompleteCycleString(urbplanbbmod, "setback_f_med"))
    f.write(getCompleteCycleString(urbplanbbmod, "setback_s_med"))
    f.write(getCompleteCycleString(urbplanbbmod, "carports_max"))
    f.write(getCompleteCycleString(urbplanbbmod, "garage_incl"))
    f.write(getCompleteCycleString(urbplanbbmod, "w_driveway_min"))
    f.write(getCompleteCycleString(urbplanbbmod, "patio_area_max"))
    f.write(getCompleteCycleString(urbplanbbmod, "patio_covered"))
    f.write(getCompleteCycleString(urbplanbbmod, "floor_num_max"))
    f.write(getCompleteCycleString(urbplanbbmod, "occup_flat_avg"))
    f.write(getCompleteCycleString(urbplanbbmod, "commspace_indoor"))
    f.write(getCompleteCycleString(urbplanbbmod, "commspace_outdoor"))
    f.write(getCompleteCycleString(urbplanbbmod, "flat_area_max"))
    f.write(getCompleteCycleString(urbplanbbmod, "floor_num_HDRmax"))
    f.write(getCompleteCycleString(urbplanbbmod, "setback_HDR_avg"))
    f.write(getCompleteCycleString(urbplanbbmod, "parking_HDR"))
    f.write(getCompleteCycleString(urbplanbbmod, "park_OSR"))
    f.write(getCompleteCycleString(urbplanbbmod, "roof_connected"))
    f.write(getCompleteCycleString(urbplanbbmod, "imperv_prop_dced"))
    f.write(getCompleteCycleString(urbplanbbmod, "freq_kitchen"))
    f.write(getCompleteCycleString(urbplanbbmod, "freq_shower"))
    f.write(getCompleteCycleString(urbplanbbmod, "freq_toilet"))
    f.write(getCompleteCycleString(urbplanbbmod, "freq_laundry"))
    f.write(getCompleteCycleString(urbplanbbmod, "dur_kitchen"))
    f.write(getCompleteCycleString(urbplanbbmod, "dur_shower"))
    f.write(getCompleteCycleString(urbplanbbmod, "demandvary_kitchen"))
    f.write(getCompleteCycleString(urbplanbbmod, "demandvary_shower"))
    f.write(getCompleteCycleString(urbplanbbmod, "demandvary_toilet"))
    f.write(getCompleteCycleString(urbplanbbmod, "demandvary_laundry"))
    f.write(getCompleteCycleString(urbplanbbmod, "ffp_kitchen"))
    f.write(getCompleteCycleString(urbplanbbmod, "ffp_shower"))
    f.write(getCompleteCycleString(urbplanbbmod, "ffp_toilet"))
    f.write(getCompleteCycleString(urbplanbbmod, "ffp_laundry"))
    f.write(getCompleteCycleString(urbplanbbmod, "priv_irr_vol"))
    f.write(getCompleteCycleString(urbplanbbmod, "ffp_garden"))
    f.write(getCompleteCycleString(urbplanbbmod, "employment_mode"))
    f.write(getCompleteCycleString(urbplanbbmod, "ind_edist"))
    f.write(getCompleteCycleString(urbplanbbmod, "com_edist"))
    f.write(getCompleteCycleString(urbplanbbmod, "orc_edist"))
    f.write(getCompleteCycleString(urbplanbbmod, "employment_total"))
    f.write(getCompleteCycleString(urbplanbbmod, "ind_subd_min"))
    f.write(getCompleteCycleString(urbplanbbmod, "ind_subd_max"))
    f.write(getCompleteCycleString(urbplanbbmod, "com_subd_min"))
    f.write(getCompleteCycleString(urbplanbbmod, "com_subd_max"))
    f.write(getCompleteCycleString(urbplanbbmod, "nres_minfsetback"))
    f.write(getCompleteCycleString(urbplanbbmod, "nres_maxfloors"))
    f.write(getCompleteCycleString(urbplanbbmod, "nres_setback_auto"))
    f.write(getCompleteCycleString(urbplanbbmod, "nres_nolimit_floors"))
    f.write(getCompleteCycleString(urbplanbbmod, "maxplotratio_ind"))
    f.write(getCompleteCycleString(urbplanbbmod, "maxplotratio_com"))
    f.write(getCompleteCycleString(urbplanbbmod, "carpark_Wmin"))
    f.write(getCompleteCycleString(urbplanbbmod, "carpark_Dmin"))
    f.write(getCompleteCycleString(urbplanbbmod, "carpark_imp"))
    f.write(getCompleteCycleString(urbplanbbmod, "carpark_ind"))
    f.write(getCompleteCycleString(urbplanbbmod, "carpark_com"))
    f.write(getCompleteCycleString(urbplanbbmod, "loadingbay_A"))
    f.write(getCompleteCycleString(urbplanbbmod, "lscape_hsbalance"))
    f.write(getCompleteCycleString(urbplanbbmod, "lscape_impdced"))
    f.write(getCompleteCycleString(urbplanbbmod, "com_demand"))
    f.write(getCompleteCycleString(urbplanbbmod, "com_demandvary"))
    f.write(getCompleteCycleString(urbplanbbmod, "li_demand"))
    f.write(getCompleteCycleString(urbplanbbmod, "li_demandvary"))
    f.write(getCompleteCycleString(urbplanbbmod, "hi_demand"))
    f.write(getCompleteCycleString(urbplanbbmod, "hi_demandvary"))
    f.write(getCompleteCycleString(urbplanbbmod, "mun_explicit"))
    f.write(getCompleteCycleString(urbplanbbmod, "edu_school"))
    f.write(getCompleteCycleString(urbplanbbmod, "edu_uni"))
    f.write(getCompleteCycleString(urbplanbbmod, "edu_lib"))
    f.write(getCompleteCycleString(urbplanbbmod, "civ_hospital"))
    f.write(getCompleteCycleString(urbplanbbmod, "civ_clinic"))
    f.write(getCompleteCycleString(urbplanbbmod, "civ_police"))
    f.write(getCompleteCycleString(urbplanbbmod, "civ_fire"))
    f.write(getCompleteCycleString(urbplanbbmod, "civ_jail"))
    f.write(getCompleteCycleString(urbplanbbmod, "civ_worship"))
    f.write(getCompleteCycleString(urbplanbbmod, "civ_leisure"))
    f.write(getCompleteCycleString(urbplanbbmod, "civ_museum"))
    f.write(getCompleteCycleString(urbplanbbmod, "civ_zoo"))
    f.write(getCompleteCycleString(urbplanbbmod, "civ_stadium"))
    f.write(getCompleteCycleString(urbplanbbmod, "civ_racing"))
    f.write(getCompleteCycleString(urbplanbbmod, "civ_cemetery"))
    f.write(getCompleteCycleString(urbplanbbmod, "res_fpwmin"))
    f.write(getCompleteCycleString(urbplanbbmod, "res_nswmin"))
    f.write(getCompleteCycleString(urbplanbbmod, "res_fpwmax"))
    f.write(getCompleteCycleString(urbplanbbmod, "res_nswmax"))
    f.write(getCompleteCycleString(urbplanbbmod, "nres_fpwmin"))
    f.write(getCompleteCycleString(urbplanbbmod, "nres_nswmin"))
    f.write(getCompleteCycleString(urbplanbbmod, "nres_fpwmax"))
    f.write(getCompleteCycleString(urbplanbbmod, "nres_nswmax"))
    f.write(getCompleteCycleString(urbplanbbmod, "res_fpmed"))
    f.write(getCompleteCycleString(urbplanbbmod, "res_nsmed"))
    f.write(getCompleteCycleString(urbplanbbmod, "nres_fpmed"))
    f.write(getCompleteCycleString(urbplanbbmod, "nres_nsmed"))
    f.write(getCompleteCycleString(urbplanbbmod, "lane_wmin"))
    f.write(getCompleteCycleString(urbplanbbmod, "lane_wmax"))
    f.write(getCompleteCycleString(urbplanbbmod, "lane_crossfall"))
    f.write(getCompleteCycleString(urbplanbbmod, "lane_wmed"))
    f.write(getCompleteCycleString(urbplanbbmod, "hwy_wlanemin"))
    f.write(getCompleteCycleString(urbplanbbmod, "hwy_wlanemax"))
    f.write(getCompleteCycleString(urbplanbbmod, "hwy_wmedianmin"))
    f.write(getCompleteCycleString(urbplanbbmod, "hwy_wmedianmax"))
    f.write(getCompleteCycleString(urbplanbbmod, "hwy_wbufmin"))
    f.write(getCompleteCycleString(urbplanbbmod, "hwy_wbufmax"))
    f.write(getCompleteCycleString(urbplanbbmod, "hwy_crossfall"))
    f.write(getCompleteCycleString(urbplanbbmod, "hwy_lanemed"))
    f.write(getCompleteCycleString(urbplanbbmod, "hwy_medmed"))
    f.write(getCompleteCycleString(urbplanbbmod, "hwy_bufmed"))
    f.write(getCompleteCycleString(urbplanbbmod, "hwy_restrict"))
    f.write(getCompleteCycleString(urbplanbbmod, "hwy_buffer"))
    f.write(getCompleteCycleString(urbplanbbmod, "considerTRFacilities"))
    f.write(getCompleteCycleString(urbplanbbmod, "trans_airport"))
    f.write(getCompleteCycleString(urbplanbbmod, "trans_seaport"))
    f.write(getCompleteCycleString(urbplanbbmod, "trans_busdepot"))
    f.write(getCompleteCycleString(urbplanbbmod, "trans_railterminal"))
    f.write(getCompleteCycleString(urbplanbbmod, "pg_greengrey_ratio"))
    f.write(getCompleteCycleString(urbplanbbmod, "pgsq_distribution"))
    f.write(getCompleteCycleString(urbplanbbmod, "pg_unused_space"))
    f.write(getCompleteCycleString(urbplanbbmod, "pg_restrict"))
    f.write(getCompleteCycleString(urbplanbbmod, "ref_usable"))
    f.write(getCompleteCycleString(urbplanbbmod, "ref_usable_percent"))
    f.write(getCompleteCycleString(urbplanbbmod, "ref_limit_stormwater"))
    f.write(getCompleteCycleString(urbplanbbmod, "svu_water"))
    f.write(getCompleteCycleString(urbplanbbmod, "svu4supply"))
    f.write(getCompleteCycleString(urbplanbbmod, "svu4waste"))
    f.write(getCompleteCycleString(urbplanbbmod, "svu4storm"))
    f.write(getCompleteCycleString(urbplanbbmod, "svu4supply_prop"))
    f.write(getCompleteCycleString(urbplanbbmod, "svu4waste_prop"))
    f.write(getCompleteCycleString(urbplanbbmod, "svu4storm_prop"))
    f.write(getCompleteCycleString(urbplanbbmod, "public_irr_vol"))
    f.write(getCompleteCycleString(urbplanbbmod, "irrigate_parks"))
    f.write(getCompleteCycleString(urbplanbbmod, "irrigate_refs"))
    f.write(getCompleteCycleString(urbplanbbmod, "public_irr_wq"))
    f.write(getCompleteCycleString(urbplanbbmod, "unc_merge"))
    f.write(getCompleteCycleString(urbplanbbmod, "unc_pgmerge"))
    f.write(getCompleteCycleString(urbplanbbmod, "unc_pgmerge_w"))
    f.write(getCompleteCycleString(urbplanbbmod, "unc_refmerge"))
    f.write(getCompleteCycleString(urbplanbbmod, "unc_refmerge_w"))
    f.write(getCompleteCycleString(urbplanbbmod, "unc_rdmerge"))
    f.write(getCompleteCycleString(urbplanbbmod, "unc_rdmerge_w"))
    f.write(getCompleteCycleString(urbplanbbmod, "unc_custom"))
    f.write(getCompleteCycleString(urbplanbbmod, "unc_customthresh"))
    f.write(getCompleteCycleString(urbplanbbmod, "unc_customimp"))
    f.write(getCompleteCycleString(urbplanbbmod, "unc_landirrigate"))
    f.write(getCompleteCycleString(urbplanbbmod, "und_state"))
    f.write(getCompleteCycleString(urbplanbbmod, "und_type_manual"))
    f.write(getCompleteCycleString(urbplanbbmod, "und_allowdev"))
    f.write("\n")
    f.write("--- TECHNOLOGY PLANNING PARAMETERS ---\n")
    f.write("================================================\n")
    f.write("Parameter;Cycle1;Cycle2;Cycle3;...\n")
    f.write("================================================\n")    
    f.write("\n")
    f.write("--- TECHNOLOGY IMPLEMENTATION PARAMETERS ---\n")
    f.write("================================================\n")
    f.write("Parameter;Cycle1;Cycle2;Cycle3;...\n")
    f.write("================================================\n")
    f.write("\n")    
    f.write("--- PERFORMANCE ASSESSMENT PARAMETERS (PLANNING) ---\n")
    f.write("================================================\n")
    f.write("Parameter;Cycle1;Cycle2;Cycle3;...\n")
    f.write("================================================\n")
    f.write("\n")    
    f.write("--- PERFORMANCE ASSESSMENT PARAMETERS (IMPLEMENTATION) ---\n")
    f.write("================================================\n")
    f.write("Parameter;Cycle1;Cycle2;Cycle3;...\n")
    f.write("================================================\n")    
    f.write("\n")    
    f.close()        
    return True

def getCompleteCycleString(modulevector, parametername):
    stringoutput = str(parametername)+";"
    for i in modulevector:
        if type(i.getParameter(parametername)) == bool:
            stringoutput += str(int(i.getParameter(parametername)))+";"
        else:
            stringoutput += str(i.getParameter(parametername))+";"
    stringoutput.rstrip(';')
    stringoutput += "\n"
    return stringoutput

def loadSimFile(activesim, filename):
    simulationdetails = {}
    simdataarchive = {"Elevation" : [],               "Soil" : [],                "Land Use" : [],
                      "Population" : [],              "Employment" : [],          "Planning" : [],
                      "Locality" : [],                "Groundwater" : [],         "Rivers" : [],
                      "Lakes" : [],                   "Social Parameters" : [],   "Existing Systems" : [],         
                      "Rainfall" : [],                "Evapotranspiration" : [],  "Solar Radiation" : []                }       #will contain the full library    
    md_delinblocks = {}
    md_urbplanbb = {}
    md_techplace = {}
    md_techimpl = {}
    md_perf = {}
    line = 0    
    f = open(filename, 'r')
    while str(line) != "--- PROJECT INFO ---\n":
        line = f.readline()
    #print "Before project info"    
    #--- PROJECT INFO ---
    lines = readUntil(f, "--- DATA ARCHIVE ---\n")
    simulationdetails = transferFileDataToDict(lines, simulationdetails)    
    
    staticsimfeatures = [int(simulationdetails["static_ubpconstant"]), \
                         int(simulationdetails["static_techplaninclude"]),\
                         int(simulationdetails["static_techplanconstant"]),\
                         int(simulationdetails["static_techimplinclude"]),\
                         int(simulationdetails["static_techimplconstant"]),\
                         int(simulationdetails["static_perfinclude"])]
    simulationdetails["staticsimfeatures"] = staticsimfeatures
    staticdataoptions = [int(simulationdetails["static_mapchange"]),\
                         int(simulationdetails["static_climateconstant"])]
    simulationdetails["staticdataoptions"] = staticdataoptions
    dynsimfeatures = [int(simulationdetails["dyn_ubpconstant"]),\
                      int(simulationdetails["dyn_techplanconstant"]),\
                      int(simulationdetails["dyn_techimplconstant"]),\
                      int(simulationdetails["dyn_perfinclude"]),\
                      int(simulationdetails["dyn_perfconstant"])]    
    simulationdetails["dynsimfeatures"] = dynsimfeatures
    
    dyndatafeatures = [int(simulationdetails["dyn_mplanconstant"]),\
                       int(simulationdetails["dyn_climateconstant"])]
    simulationdetails["dyndatafeatures"] = dyndatafeatures
    
    #--- DATA ARCHIVE ---
    f.readline()
    f.readline()
    f.readline()    #Read the three lines that make up the Table's header            
    lines = readUntil(f, "--- OUTPUT OPTIONS ---\n")
    simdatadict = {}
    for i in lines:
        i = i.strip("\n")
        datasplit = i.split(";")
        if len(i) > 1:
            simdataarchive[str(datasplit[1])].append(str(datasplit[2]))
            simdatadict[int(datasplit[0])] = [str(datasplit[1]),str(datasplit[2])]
    #print simdataarchive
    #print simdatadict
    #--- OUTPUT OPTIONS ---
    lines = readUntil(f, "--- CYCLE DATA SETS ---\n")
    simulationdetails = transferFileDataToDict(lines, simulationdetails)
    
    #--- CYCLE DATA SETS ---
    f.readline()
    f.readline()
    f.readline()    #Read the next three lines of Table Header
    lines = readUntil(f, "--- DELINBLOCKS PARAMETERS ---\n")
    activedataitemspc = []    
    activedataitemsic = []
    activedataitemspa = []

    lineindex = 0
    for i in lines:
        i = i.strip("\n")
        i = i.split(";")
        
        if len(i) <= 1:
            continue
        for cols in range(len(i)):
            if cols == 0 or i[cols] == 'none':
                continue
            i[cols] = i[cols].split(",")        #Will give something like [0, [1, 3, 5, 6], [4, 6, 6, 2], 'none']
            for values in range(len(i[cols])):
                i[cols][values] = int(i[cols][values])
        
        activedataitemspc.append({})        #activedataitems = [ {dictionary 1}, {dictionary 2}, {dictionary 3}]
        if i[1] != 'none':                  #{dictionary1} = {Elevation: file, Land Use: file, ...}
            for selection in i[1]:
                activedataitemspc[lineindex][simdatadict[int(selection)][0]] = simdatadict[int(selection)][1]     #simdatadict[selection][0] = label of data type e.g. "Elevation"
                                                                                                #simdatadict[selection][1] = filename
        activedataitemsic.append({})
        if i[2] != 'none':
            for selection in i[2]:
                activedataitemsic[lineindex][simdatadict[int(selection)][0]] = simdatadict[int(selection)][1]
        
        activedataitemspa.append({})
        if i[3] != 'none':
            for selection in i[3]:
                activedataitemspa[lineindex][simdatadict[int(selection)][0]] = simdatadict[int(selection)][1]
        #print "Set Cycle Data Variables"
        lineindex += 1
        #END OF FOR LOOP
    
    #simulationdetails = transferFileDataToDict(lines, simulationdetails)
    
    #--- DELINBLOCKS PARAMETERS ---
    lines = readUntil(f, "--- URBAN PLANNING PARAMETERS (PLANNING) ---\n")
    md_delinblocks = transferFileDataToDict(lines, md_delinblocks)
    
    #--- URBAN PLANNING PARAMETERS ---
    lines = readUntil(f, "--- TECHNOLOGY PLANNING PARAMETERS ---\n")
    md_urbplanbb = transferFileDataToDict(lines, md_urbplanbb)
    #--- TECHNOLOGY PLANNING PARAMETERS ---
    
    #--- TECHNOLOGY IMPLEMENTATION PARAMETERS ---
    
    f.close()
    
    #Transfer Project Details data
    projectdetails = activesim.getProjectDetails()
    for key in projectdetails:
        try:
            #print projectdetails[key]
            #print simulationdetails[key]
            projectdetails[key] = type(projectdetails[key])(simulationdetails[key])
        except KeyError:
            print "WARNING, project file does not contain info about: "+str(key)
    #Transfer data library data
    dataarchive = activesim.showDataArchive()
    for key in dataarchive:
        try:
            dataarchive[key] = simdataarchive[key]
        except KeyError:
            print "ATTENTION, no "+str(key)+" data specified"

    #Transfer output options
    gisoutputs = activesim.getGISExportDetails()
    for key in gisoutputs:
        try:
            if type(gisoutputs[key]) == bool:
                gisoutputs[key] = type(gisoutputs[key])(int(simulationdetails[key]))
            else:                
                gisoutputs[key] = type(gisoutputs[key])(simulationdetails[key])
        except KeyError:
            print "WARNING, project file does not contain info about: "+str(key)
    
    return simulationdetails, activedataitemspc, activedataitemsic, activedataitemspa, md_delinblocks, md_urbplanbb, md_techplace, md_techimpl, md_perf

def transferFileDataToDict(lines, simdict):
    for i in lines:
        i = i.strip("\n")
        datasplit = i.split(";")
        #print datasplit
        if len(datasplit) > 1 and len(datasplit) == 2:
            simdict[str(datasplit[0])] = datasplit[1]
        else:
            simdict[str(datasplit[0])] = datasplit[1:]
    return simdict

def readUntil(fname, label):
    lines = []
    line = ""
    while str(line) != label:
        line = fname.readline()
        if str(line) != label:
            lines.append(line)
    return lines