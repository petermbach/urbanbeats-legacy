# -*- coding: utf-8 -*-
"""
@file
@author  Peter M Bach <peterbach@gmail.com>
@version 0.5
@section LICENSE

This file is part of VIBe2
Copyright (C) 2011  Peter M Bach

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

import md_delinblocks, md_urbplanbb
import urbanbeatscore as ub

def getProjectSummary(activesim, content):
    htmlstring = """
    <!DOCTYPE html>
    <html>
        <head>
            <title>Project Summary</title>
        </head>

    <body>
        <h3>Project Name Goes Here...</h3>

    """
    htmlstring += """</body></html>"""
    return htmlstring

def getSummaryStringNarrative(activesim, tabindex):
    narrative = activesim.getNarrative(tabindex)
    htmlstring = """<strong>"""+narrative[0]+"""</strong>
    <div id=\"N"""+str(tabindex)+"""\"><p>"""+narrative[1]+"""</p></div>
    """
    return htmlstring

def getSummaryStringDelinBlocks(activesim):
    delinblocks = activesim.getModuleDelinblocks()
    yesnomatrix = ["No", "Yes"]        
    summarystring = ""
    summarystring += "<strong><em>Delineation of Building Blocks </em></strong><br><ul>"
    paramlist = delinblocks.getModuleParameterList()
    for param in paramlist.keys():
        if paramlist[param][0] == "BOOL":
            summarystring += "<li>"+str(paramlist[param][1])+" - "+str(yesnomatrix[int(delinblocks.getParameter(str(param)))])+"</li>"
        else:
            summarystring += "<li>"+str(paramlist[param][1])+" - "+str(delinblocks.getParameter(str(param)))+"</li>"
    #summarystring += "Include following data sets: \n"
    #summarystring += "  >> Planner's Map: "+str(yesnomatrix[int(delinblocks.getParameter("include_plan_map"))])+"\n"
    #summarystring += "  >> Locality Map: "+str(yesnomatrix[int(delinblocks.getParameter("include_local_map"))])+"\n"
    #summarystring += "  >> Employment Map: "+str(yesnomatrix[int(delinblocks.getParameter("include_employment"))])+"\n"
    #summarystring += "  >> Rivers Map: "+str(yesnomatrix[int(delinblocks.getParameter("include_rivers"))])+"\n"
    #summarystring += "  >> Lakes Map: "+str(yesnomatrix[int(delinblocks.getParameter("include_lakes"))])+"\n"
    #summarystring += "  >> Groundwater Map: "+str(yesnomatrix[int(delinblocks.getParameter("include_groundwater"))])+"\n"
    #summarystring += "  >> Social Parameter Map 1: "+str(yesnomatrix[int(delinblocks.getParameter("include_soc_par1"))])+"\n"
    #summarystring += "  >> Social Parameter Map 2: "+str(yesnomatrix[int(delinblocks.getParameter("include_soc_par2"))])+"\n"
    #summarystring += "Block Size: "+str(delinblocks.getParameter("BlockSize"))+"\n\n"
    #summarystring += "Additional Analyses: \n"
    #summarystring += "  >> Spatial Metrics: "+str(yesnomatrix[int(delinblocks.getParameter("spatialmetrics"))])+"\n"
    #summarystring += "  >> Patch Delineation: "+str(yesnomatrix[int(delinblocks.getParameter("patchdelin"))])+"\n"
    #summarystring += "  >> CBD Distance: "+str(yesnomatrix[int(delinblocks.getParameter("considerCBD"))])+"\n\n"
    #summarystring += "Flow Path Delineation Method: "+str(delinblocks.getParameter("flow_method"))+"\n\n"
    summarystring += "</ul>"
    return summarystring

def getSummaryStringUrbplanbb(activesim, index):
    urbplanbb = activesim.getModuleUrbplanbb(index)
    summarystring = ""
    summarystring += "<strong><em>Urban Planning Rules</em></strong><br>"
    summarystring += "General Planning Rules: \n"
    summarystring += "  >> City Type: "+str()+"\n"
    summarystring += "Residential Planning Rules: \n"
    summarystring += ""+str()+"\n"
    summarystring += "Non-residential Planning Rules: \n"
    summarystring += ""+str()+"\n"
    summarystring += "Urban Hotspots Explicitly Considered: \n"
    summarystring += "  >> NONE \n\n"
    summarystring += "Open Spaces, Roads and Other Land Uses: \n"
    summarystring += ""+str()+"\n\n"
    return summarystring
    