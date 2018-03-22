# -*- coding: utf-8 -*-
"""


@author: Abhay Poddar
"""

import importlib
import NFCPlugin_windows
import Plugin
import platform

from cryptography.fernet import Fernet
from Crypto.Cipher import AES
#import NFCAuth
obj=NFCPlugin_windows.NFCPlugin("try.txt")
print(obj)
obj.writeToTag("asd")
print(obj.readFromTag())
obj2=Plugin.Plugin()
obj2.plugin.writeToTag("asdw")
print(obj2.plugin.readFromTag())
kwargs=platform.uname()
dbname=kwargs[0]+'_'+kwargs[1]+".db"
print(dbname)
key="aaasvcdahdandfuy"
rid='This is an IV456'
enc=AES.new(key,AES.MODE_CFB,rid)
stri=''
stri=kwargs[0]+kwargs[1]+kwargs[2]+kwargs[3]+kwargs[4]
print(stri)
text=enc.encrypt(stri)
print (text)

dec=AES.new(key,AES.MODE_CFB,rid)
ptext=dec.decrypt(text)
print (ptext)
print (str(1/7))

import sqlite3
import NFCAuth
obj3=NFCAuth.NFCAuth(0)
cred=obj3.get()
print(obj3.get())
print (cred)
obj3.write(username="Ash",passw="123")
obj3.write(username="Abhay Poddar",passw="asd123123")
connection=sqlite3.connect("Windows_Peace.db")
res=connection.execute("SELECT * FROM NFCPRIV")
res1=res.fetchall()
for i in res1:
    print(i[1])
    print(i[0])

import NFCAuth
obj4=NFCAuth.NFCAuth(1)
obj4.write(dev1=12345,dev2=789456,dev3=1223456)
auth=obj4.get(12346)
auth2=obj4.get(789456)
print(auth)
print(auth2)
for i in range(len(cred)):
    #if i==devid:
        #break
    print(i)
#res=connection.execute("SELECT * FROM NFCPRIV")
#print(res)
#resu=res.fetchall()
#print(resu)
#query="INSERT INTO NFCPRIV VALUES (123, 'Ashish')"
#a=123
#b="ash"
#connection.execute("INSERT INTO NFCPRIV(rid,ciepher) VALUES(?,?)",(a,b))
connection.execute("INSERT INTO NFCPRIV VALUES(?,?)",(157,'ash'))
connection.commit()
res=connection.execute("SELECT * FROM NFCPRIV")
res1=res.fetchall()
for i in res1:
    print(i[1])
    print(i[0])
connection.close()
query="SELECT * FROM NFCPRIV WHERE rid= 'Ulkw9KQM9jwL3Q5n'"
result=connection.execute(query)
res2=result.fetchall()
print(str(res2[1:]))
for j in res2:
    print(j[1])
    print(j[0])
print(res2[0:])
k=str(res2[1:])
print(j[1])
k=k[1:len(k)-2]

import dummyTag
dummyTag.genFile()
str=input("Enter your name")
print (str)