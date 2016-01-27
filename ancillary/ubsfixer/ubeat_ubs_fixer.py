# -*- coding: utf-8 -*-
"""
@file
@author  Peter M Bach <peterbach@gmail.com>
@version 1.0
@section LICENSE

This file is part of UrbanBEATS (www.urbanbeatsmodel.com)
Copyright (C) 2011, 2012, 2013  Peter M Bach

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

import os, sys
import tarfile

savefilename = "fixedubs.ubs"

print "Now repairing save file, saving as fixedubs.ubs"

#Get the root folder that the script is located in
rootpath = str(os.path.abspath(os.path.dirname(sys.argv[0])))           #Obtains the script's root directory
rootpath = rootpath.encode('string-escape')       #To avoid weird bugs e.g. if someone's folder path
                                                  #contains escape characters e.g. \testing or \newSoftware
#print "Root path", str(rootpath)

#Grab all TXT files here
filenames = []
for file in os.listdir(rootpath):
    if file.endswith(".txt"):
        filenames.append(file)

print "Filenames: ", filenames

if os.path.exists(str(savefilename)): 
    os.remove(str(savefilename))
    
archive = tarfile.open(str(savefilename), 'w')     #creates the tar archive

for i in range(len(filenames)):
    archive.add(filenames[i], arcname=filenames[i])

archive.close()

print "Completed Repair Successfully"

