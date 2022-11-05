import socket  

Hostname=socket.gethostname()  
Port = 8888
IP = 'localhost'

def getIp():
    global Hostname
    global IP
    IP=socket.gethostbyname(Hostname)   
    return IP

def getLocalhostIp():
    global IP
    IP = 'localhost'
    return IP

def getPcName():
    global Hostname
    Hostname=socket.gethostname()   
    return Hostname

def setPort(port):
    global Port
    Port =  port

def getPort():
    global Port
    return Port

def restoreDefaultConfig():
    global Port
    global IP
    Port = 8888
    IP = 'localhost'