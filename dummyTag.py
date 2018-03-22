# -*- coding: utf-8 -*-
"""


@author: Abhay Poddar
"""
import random
import string
import os.path
def genFile():
    count=0
    i = "try"+str(count)+".txt"
    i=str(i)
    while os.path.exists(i):
        count=count+1
        i = "try"+str(count)+".txt"
        i=str(i)
        
    file=open(i, "w+")
    data= ''.join([random.choice(string.ascii_letters + string.digits) for n in range(7)])
    file.write(data)
    file.close()
    return i
    
