"""
WiFi API that will allow user to find all memorized WiFi SIDs and their passwords
"""

import os, subprocess

networkUsers = {}
"""
List of all wifi users with their passwords. getWifiUsers() needs to be called in order to catch users
"""

def getMemorizedNetworks():
    """
    Function will find all memorized WiFi's and return it as a list
    """
    users = []
    userProfiles = ""
    cmd = "netsh wlan show profiles"
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    userProfiles, err = p.communicate()
    userProfiles = str(userProfiles)
    userProfiles = userProfiles.split('\\n')

    for line in userProfiles:
        if "All User Profile" in line:
            
            line = line.split("All User Profile     : ")
            line[1] = line[1].split("\\r")
            users.append(line[1][0])

    return users

def printUsers():
    """
    Function will print all memroized WiFi users to the command line
    """
    global users
    for element in users:
        print(element)

def getPassword(user):
    """
    Function will find password based on the given user id
    @param user id
    @return True and pwd or False and "'
    """
    pwdFound = False
    cmd = "netsh wlan show profiles " + user +  " key=clear"
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    profileInfo, err = p.communicate()
    profileInfo = str(profileInfo)
    profileInfo = profileInfo.split('\\n')

    for line in profileInfo:
        if "Key Content" in line:
            line = line.split(': ')
            pwd = line[1].split('\\r')
            pwdFound = True
            return pwdFound, pwd[0]
    return pwdFound, ""

def getWifiUsers():
    """
    Function will map all discovered users with the passwords related to them
    """
    global networkUsers
    users = getMemorizedNetworks()
    for id in users:
        pwdFound, pwd = getPassword(id)
        if pwdFound is True:
            networkUsers[id] = pwd

