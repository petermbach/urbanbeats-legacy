# -*- coding: utf-8 -*-

"""
@file
@author  Peter M Bach <peterbach@gmail.com>
@version 0.5
@section LICENSE

This file is part of UrbanBEATS
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

__author__ = 'Peter M Bach'

import os

def writeLeafletScript(viewmode, project_path, filename, output_path):
    """Creates the HTML code for the leafletjs map, returns a string object with html code"""

    htmlscript = ""
    htmlscript += writeLeafletHeader(viewmode)
    htmlscript += writeLeafletBody(viewmode, project_path, filename, output_path)
    htmlscript += """</html>"""

    return htmlscript


def writeLeafletHeader(viewmode):
    """Adds the <head> </head> bracket for the leaflet code"""
    if viewmode == "on":
        linkrel = """<link rel="stylesheet" href="http://cdn.leafletjs.com/leaflet-0.6.4/leaflet.css" />"""
    else:
        linkrel = """<link rel="stylesheet" href=\""""+str(os.path.dirname(__file__))+"""/ancillary/leafletjs-0.6.4/leaflet.css\" />"""

    htmlscript = """
    <!DOCTYPE HTML>
    <html>
	<head>
		<title>Leafletjs Map</title>
		<meta charset="utf-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		"""+linkrel+"""
	</head>
    """
    return htmlscript

def writeLeafletBody(viewmode, project_path, filename, output_path):
    """Writes the main body of the leaflet map"""
    blocksfile = open(output_path+"/tempgeojson_0pc_Blocks.geojson")
    blockscode = """ """
    for lines in blocksfile:
        blockscode += lines
    blocksfile.close()



    if viewmode == "on":
        linkrel = """<script src="http://cdn.leafletjs.com/leaflet-0.6.4/leaflet.js"></script>"""
    else:
        linkrel = """<script src=\""""+str(os.path.dirname(__file__))+"""/ancillary/leafletjs-0.6.4/leaflet.js\"></script> """

    htmlscript = """
    <body>
		<!-- Create the container for the map using the div tag and set the map's style features with CSS -->
		<div id="map" style="height:700px"> </div>

		<!-- Add the javascript file leaflet.js -->
		"""+linkrel+"""

		<!-- Now put the actual script to generate the map -->
		<script>
			var map = L.map('map').setView([-37.8136, 144.9631], 16);	  //Create a default map and set its initial coordinates
					//setView( LatLng, Zoom, Pan Options )

			L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
				attribution: 'Map data &copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
				maxZoom: 25
			}).addTo(map);
				//The cloudmade numbers after the URL represents the API-key, which you will need to get the tiling is done
				//automatically

            function onEachFeature(feature, layer) {
                var popupContent = "<p>I started out as a GeoJSON " +
                        feature.geometry.type + ", but now I'm a Leaflet vector!</p>";

                if (feature.properties && feature.properties.popupContent) {
                    popupContent += feature.properties.popupContent;
                }

                layer.bindPopup(popupContent);
            }

            //Add layers to Leaflet: Blocks, Flowpaths, Planned WSUD, Implemented WSUD, Localities
            var geoJsonBlocks = """+blockscode+""";
            L.geoJson(geoJsonBlocks).addTo(map);

            //add other layers


			//Up to this point: Basic Map has been generated and you can browse through it

            //Add the layer control

		</script>
	</body>
    """
    return htmlscript