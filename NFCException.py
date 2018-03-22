# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 10:49:53 2018

@author: Abhay Poddar
"""

class NFCException(Exception):
    """Base class for other NFC exceptions"""
    pass
class NFCDbException(NFCException):
    """Exceptions due to database operations"""
    pass
class NFCModeException(NFCException):
    """Exception due to wrong mode initialization"""
    pass
class NFCEncException(NFCException):
    """Exception, unable to encrypt"""
    pass
class NFCDecException(NFCException):
    """Exception, unable to decrypt"""
    pass
class NFCIOException(NFCException):
    """Exception, unable to complete NFC read/write"""
    pass
class NFCIOTimeout(NFCIOException):
    """Exception, NFC I/O Timeout"""
    pass
class NFCRidFullException(NFCException):
    """Exception, all possible rid used"""
    pass
class NFCPluginException(NFCException):
    """Exception, plugin not loaded"""
    pass
class NFCPlatformException(NFCPluginException):
    """Exception, plugin for current platform not supported"""
    pass