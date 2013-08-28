# -*- coding: utf-8 -*-
"""
Created on Mon Aug 06 23:50:37 2012

@author: Peter M Bach
"""

from distutils.core import setup
import py2exe

setup(windows=['main.pyw'],options = {"py2exe": {"dll_excludes": ["MSVCP90.dll"]}})
#python createubeatsexe.py py2exe --includes sip