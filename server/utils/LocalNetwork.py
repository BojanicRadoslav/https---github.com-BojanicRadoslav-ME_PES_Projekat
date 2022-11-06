import socket  
"""Module is accessing PC-id, IP address of the local network and setting port on which server will run"""

Hostname=socket.gethostname()  
"""Hostname instance from which PC name and IP will be obtained"""

Port = 8888
"""Port on which server will run, default is 8888"""

IP = 'localhost'
"""IP on which server will run, default is 'localhost'"""

def getIp():
    """
    Function will return local IP address
    """
    global Hostname
    global IP
    IP=socket.gethostbyname(Hostname)   
    return IP

def getLocalhostIp():
    """
    Function will set local ip to be localhost, this is useful for develoment
    """
    global IP
    IP = 'localhost'
    return IP

def getPcName():
    """
    Function will return PC name
    """
    global Hostname
    Hostname=socket.gethostname()   
    return Hostname

def setPort(port):
    """
    Function is setting port on which server will run, default is 8888
    """
    global Port
    Port =  port

def getPort():
    """
    Function is returning port on which server is running
    """
    global Port
    return Port

def getNetworkConfig():
    global IP
    global Port
    return IP, Port

def restoreDefaultConfig():
    """
    Function is restoring default server config
    @port = 8888
    @IP = 'localhost'
    """
    global Port
    global IP
    Port = 8888
    IP = 'localhost'