# -*- coding: utf-8 -*-
"""
Created on Mon Aug 06 23:50:37 2012

@author: Peter M Bach
"""

from distutils.core import setup
import py2exe
import sys
sys.setrecursionlimit(5000)

setup(windows=[{ "script": "main.pyw",
                 "icon_resources": [(1, "ubeats.ico")],
                   }],
      options = {
          "py2exe": {"dll_excludes": ['MSVCP90.dll',
                                        'IPHLPAPI.DLL',
                                        'NSI.dll',
                                        'WINNSI.DLL',
                                        'WTSAPI32.dll',
                                        'SHFOLDER.dll',
                                        'PSAPI.dll',
                                        'MSVCR120.dll',
                                        'MSVCP120.dll',
                                        'CRYPT32.dll',
                                        'GDI32.dll',
                                        'ADVAPI32.dll',
                                        'CFGMGR32.dll',
                                        'USER32.dll',
                                        'POWRPROF.dll',
                                        'MSIMG32.dll',
                                        'WINSTA.dll',
                                        'MSVCR90.dll',
                                        'KERNEL32.dll',
                                        'MPR.dll',
                                        'Secur32.dll',
                                        'api-ms-win-core-string-l1-1-0.dll',
                                        'api-ms-win-core-processthreads-l1-1-2.dll',
                                        'api-ms-win-core-sysinfo-l1-2-1.dll',
                                        'api-ms-win-core-synch-l1-2-0.dll',
                                        'api-ms-win-core-libraryloader-l1-2-1.dll',
                                        'api-ms-win-core-atoms-l1-1-0.dll',
                                        'api-ms-win-core-winrt-error-l1-1-1.dll',
                                        'api-ms-win-core-sidebyside-l1-1-0.dll',
                                        'api-ms-win-core-localization-obsolete-l1-3-0.dll',
                                        'api-ms-win-core-heap-l1-2-0.dll',
                                        'api-ms-win-core-heap-l2-1-0.dll',
                                        'api-ms-win-core-delayload-l1-1-1.dll',
                                        'api-ms-win-core-libraryloader-l1-2-0.dll',
                                        'api-ms-win-core-rtlsupport-l1-2-0.dll',
                                        'api-ms-win-core-shlwapi-obsolete-l1-2-0.dll',
                                        'api-ms-win-security-base-l1-2-0.dll',
                                        'api-ms-win-core-handle-l1-1-0.dll',
                                        'api-ms-win-core-registry-l1-1-0.dll',
                                        'api-ms-win-core-string-obsolete-l1-1-0.dll',
                                        'api-ms-win-core-errorhandling-l1-1-1.dll',
                                        'api-ms-win-crt-runtime-l1-1-0.dll',
                                        'api-ms-win-crt-private-l1-1-0.dll',
                                        'api-ms-win-core-interlocked-l1-2-0.dll',
                                        'api-ms-win-core-debug-l1-1-1.dll',
                                        'api-ms-win-core-profile-l1-1-0.dll'
                                      ],
                     "includes":["sip", "PyQt4.QtNetwork", "scipy.sparse", "scipy.sparse.csgraph._validation", "scipy.spatial"]}})

#scipy.sparse.csgraph._validation
#--- Run the script in the command line by navigating to the root folder of the software where main.pyw is
#located and then type the following command... ---#

#python createubeatsexe.py py2exe