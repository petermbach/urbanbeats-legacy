# -*- coding: utf-8 -*-
"""
Created on Mon Aug 06 23:50:37 2012

@author: Peter M Bach
"""

from distutils.core import setup
import py2exe

setup(windows=[{ "script": "main.pyw",
                 "icon_resources": [(1, "ubeats.ico")],
                   }],
      options = {
          "py2exe": {"dll_excludes": ["MSVCP90.dll"], "includes":["sip", "PyQt4.QtNetwork"]}})

#--- Run the script in the command line by navigating to the root folder of the software where main.pyw is
#located and then type the following command... ---#

#python createubeatsexe.py py2exe