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

__author__ = 'Peter M Bach'
import time

class UBModule(object):
    """Abstract class for UrbanBEATS module classes. All modules within the module will inherit from this class. This
    abstract class contains observer pattern, some other key variables."""
    def __init__(self):
        self.__observers = []
        self.__parameters = {}      #Holds all parameter names and type

    def attach(self, observers):
        for i in observers:
            if not i in self.__observers:
                self.__observers.append(i)
        return True

    def detach(self, observers):
        for i in observers:
            try:
                self.__observers.remove(i)
            except ValueError:
                pass
        return True

    def notify(self, updateMessage):
        self.__observers[0].updateObserver(str(updateMessage))

    def notifyProgress(self, value):
        self.__observers[1].updateObserver(value)

    def createParameter(self, name, type, descript):
        self.__parameters[name] = [type, descript]

    def getParameterType(self, name):
        try:
            return self.__parameters[name][0]
        except KeyError:
            return None

    def getParameter(self, name):   #UBCORE FUNCTION
        return self.__dict__.get(name)

    def setParameter(self, name, value):    #UBCORE FUNCTION
        self.__dict__.__setitem__(name, value)

    def getModuleParameterList(self):
        return self.__parameters

#KEYWORDS FOR VARIABLES (THIS IS HERE TO MAINTAIN COMPATIBILITY WITH DYNAMIND SYNTAX)
DOUBLE = 'DOUBLE'
BOOL = 'BOOL'
STRING = 'STRING'