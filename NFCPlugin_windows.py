# -*- coding: utf-8 -*-
"""

@author: Abhay Poddar
"""

import importlib
import dummyTag
class NFCPlugin():
    'NFC operation plugin for windows'
    #filename=""
    def __init__(self, filename="try0.txt"):
        self.filename=filename
        #print (filename," ",self.filename, " ")
        
    def readFromTag(self,mode=0,createT=0):
        if createT==1:
            self.filename=dummyTag.genFile()
        elif mode==2:
            self.filename=createT
        #print (self.filename, " ")
        file=open(self.filename, "r")
        data=file.readline()
        fields=data.split("|")
        file.close()
        if mode==0:
            return fields[1]
        else:
            return fields[0]
        
    def writeToTag(self, data):
        #print (self.filename, " ")
        file=open(self.filename, "a+")
        data="|"+data
        file.write(data)
        file.close()