# -*- coding: utf-8 -*-
"""
@file
@author  Peter M Bach <peterbach@gmail.com>
@version 1.0
@section LICENSE

This file is part of UrbanBEATS
Copyright (C) 2015  Peter M Bach

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

EPANETHEADERS = ["[TITLE]", "[JUNCTIONS]", "[RESERVOIR]", "[TANKS]", "[PIPES]", "[PUMPS]", "[VALVES]", "[EMITTERS]",
                 "[CURVES]", "[PATTERNS]", "[ENERGY]", "[STATUS]", "[CONTROLS]", "[RULES]", "[DEMANDS]",
                 "[QUALITY]", "[REACTIONS]", "[SOURCES]", "[MIXING]",
                 "[OPTIONS]", "[TIMES]", "[REPORT]",
                 "[COORDINATES]", "[VERTICES]", "[LABELS]", "[BACKDROP]", "[TAGS]"]

def readInpFile(filename):
    """Opens and reads the EPANET .inp file line by line, transfers the data into a variable"""
    f = open(filename, 'r')
    lines = []
    for line in f:
        lines.append(line)
    f.close()
    return lines

def returnHeaderBlock(headername):


    return

def getNodeCoordinates(inpfile):
    """Scans the .inp file data for the node coordinates and writes these to an array of (x,y) points
    for further analysis.
    :param inpfile: variable containing the EPANET .inp file data
    :return: coordinates array ["node-name", "x", "y"]
    """
    i, found = 0, 0
    while found == 0:
        if "[COORDINATES]" not in inpfile[i]:
            i += 1
        else:
            found = 1
    coordinates = []

    while True:
        i += 1
        if inpfile[i].strip() == "":
            continue    #No data
        elif inpfile[i].strip()[0] == ';':
            continue    #If a comment or an empty line, skip
        elif inpfile[i].strip()[0] == "[":
            break       #If program detects an open square brace, this denotes a new section
        print inpfile[i]
        coordinates.append(inpfile[i].strip().split())
    return coordinates


def getPipeProperties():


    return

def setAttribute():


    return

def setDefaultParameter():


    return

def defineRule():


    return




