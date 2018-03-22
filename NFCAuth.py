# -*- coding: utf-8 -*-
"""


@author: Abhay Poddar
"""

import Plugin
import sqlite3
import platform
import random
import string
from Crypto.Cipher import AES    
import sys
class NFCAuth:
    def __init__(self, mode=0):
        self.mode=mode
        self.plugin=Plugin.Plugin()
        if mode==0:
            print("initialized in credential mode")
        elif mode==1:
            print("initialized in Authenticator mode")
        else:
            print("Invalid mode selection")
            sys.exit(0)
        plat=platform.uname()
        dbname=plat[0]+'_'+plat[1]+".db"
        try:
            self.connection=sqlite3.connect(dbname)
        except:
            print("Error in Database connection")
            return -2
        try:
            self.connection.execute("CREATE TABLE NFCPRIV(rid TEXT PRIMARY KEY, cipher TEXT NOT NULL)")
            print("Table created")
        except:
            print("Table exists, adding or reading records")
    
    def encrypt(uid,rid,**kwargs):
        osn=platform.system()[:3]
        if not osn:
            osn='Emb'
        padd=str(1/7)[2:8]
        key=uid+osn+padd
        #print(uid)
        #print(key, " ",rid)
        param=''
        for i in kwargs:
            param+=str(kwargs[i])+'|'
        print (param)
        try:
            enc_suite=AES.new(key, AES.MODE_CFB, str(rid))#add IV as rid
            cipher_text=enc_suite.encrypt(param)
        except:
            print("Unable to Encrypt")
        return cipher_text

    def write(self, **kwargs):
        try:
            uid=self.plugin.plugin.readFromTag(1,1)
        except:
            return -1
        rid=NFCAuth.genRid(self)
        cipher=NFCAuth.encrypt(uid,rid,**kwargs)
        print("write ",cipher," ",rid, " ", uid)
        try:
            self.plugin.plugin.writeToTag(rid)
        except:
            return -1
        try:
            self.connection.execute("INSERT INTO NFCPRIV VALUES(?,?)",(rid,cipher))
            self.connection.commit()
        except:
            return -2
        return 0
        
    def genRid(self):
        while True:
            i = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(16)])
            i=str(i)
            query="SELECT * FROM NFCPRIV WHERE rid= '"+i+"'"
            result=self.connection.execute(query)
            if(len(result.fetchall())==0):
                return i
    
    def decrypt(text,uid,rid): #this rid is extracted from the tag and text is ciphered text
        osn=platform.system()[:3]
        if not osn:
            osn='Emb'
        padd=str(1/7)[2:8]
        key=uid+osn+padd
        #print(len(key), " ", key)
        dec_suite=AES.new(key,AES.MODE_CFB,str(rid))#add IV as rid
        deciphered_text=dec_suite.decrypt(text)
        deciphered_text=str(deciphered_text)
        deciphered_text=deciphered_text[2:len(deciphered_text)-2]
        deciphered_text=deciphered_text.split('|')
        return deciphered_text
    
    def get(self,devid=0):
        try:
            if devid!=0 and self.mode==0:
                uid=self.plugin.plugin.readFromTag(2,devid)
            else:
                uid=self.plugin.plugin.readFromTag(1)
            rid=self.plugin.plugin.readFromTag(0)
            #print(uid," ",rid)
        except:
            return -1
        try:
            query="SELECT * FROM NFCPRIV WHERE rid= '"+rid+"'"
            result=self.connection.execute(query)
            res2=result.fetchall()
        except:
            return -2
        for j in res2:
            pass
        cred=NFCAuth.decrypt(j[1],uid,rid)
        if devid==0 and self.mode==0:
            return cred
        elif devid!=0 and self.mode==1:
            for i in cred:
                if i==str(devid):
                    return [True,uid]
            return [False,uid]
        elif devid!=0 and self.mode==0:
            return cred
        else:
            print("Wrong mode")
        #cred=str(cred)
        #cred=cred[:len(cred)-1]
        #cred=cred.split('|')
        #print(cred)