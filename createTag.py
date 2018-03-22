# -*- coding: utf-8 -*-
"""


@author: Abhay Poddar
"""

import NFCAuth

obj=NFCAuth.NFCAuth(1)
print("Create Tag:")
uname=input("Enter username: ")
passw=input("Enter password: ")
conf=obj.write(username=uname,password=passw)
if conf==0:
    print("Tag created: ",obj.get())
elif conf==-1:
    print("Error in file op")
elif conf==-2:
    print("Error in Database Operation")