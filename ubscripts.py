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

__author__ = 'pbach'

def convertYearList(datavalues, dataformat):
    if dataformat == "GUI":     #If transferring data back into the GUI
        yearstring = ""
        for i in datavalues:
            yearstring += str(i)+", "
        yearstring = yearstring.rstrip(',')
        return yearstring
    elif dataformat == "MOD":   #If creating the parameter list.
        if len(datavalues) <= 4:
            return []
        yeararray = datavalues.split(',')
        for i in range(len(yeararray)):
            yeararray[i] = int(yeararray[i])
        return yeararray
    else:
        return []