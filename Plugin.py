# -*- coding: utf-8 -*-
"""


@author: Abhay Poddar
"""

import importlib
import platform
class Plugin:
    def __init__(self):
        self.system=platform.system()
        #print("Current operating system: ",self.system)
        if self.system=="Windows":
            self.plugin_name="NFCPlugin_windows"
        elif self.system=="Linux":
            self.plugin_name="NFCPlugin_linux"
        elif self.system=="Unix":
            self.plugin_name="NFCPlugin_unix"
        
        self.plugin_module=importlib.import_module(self.plugin_name, ".")
        #print (self.plugin_module)
        self.plugin=self.plugin_module.NFCPlugin()