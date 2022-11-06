import matplotlib.pyplot as plt
import csv
import os, sys
import glob
import re

import glob
file = ""
files = glob.glob("server\data\database\*")

time = []
temp = []
hum = []

# lines = plt.plot(time, temp, 'ro', legend="temp", time, hum, 'bo', legend="temp")
# plt.clf()
# plt.plot(time, temp, 'ro', label="Temperature")
# plt.plot(time, hum, 'bo', label="Humidity")
# plt.legend(loc="upper left")
# plt.xlabel("Time")
# plt.show()

def databaseDiscovery():
    """
    Function is searching for all available files in database directory
    """
    files = glob.glob("server\data\database\*")
    return files 

def loadValues(database):
    """
    Function is reading values for time, temp and hum from the given database
    """
    global time, temp, hum

    time = []
    temp = []
    hum = []

    with open(database, 'r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            time.append(row[0])
            temp.append(row[1])
            hum.append(row[2])

def generateGraphObject():
    """
    Function is creating graph object from global variables readed using loadValues()
    """
    plt.clf()
    plt.plot(time, temp, 'ro', label="Temperature")
    plt.plot(time, hum, 'bo', label="Humidity")
    plt.legend(loc="upper left")
    plt.xlabel("Time")

def generatePng(database):
    """
    Function is generating PNG immage names after the given database and savesit in graphs folder
    """
    loadValues(database)
    generateGraphObject()
    plt.title(getFileName(database))
    fileName = 'server\static\graphs\\' + getFileName(database) + '.png'
    plt.savefig(fileName)
    return fileName

def getPngPathFromFileName(fileName):
    fileName = '../static/graphs/' + fileName + '.png'
    return fileName

def getFileName(database):
    """
    Function is reading file name without path or extension using regex rule
    """
    reg = re.search("[0-9].*csv", database)
    fileName = database[reg.span()[0]:reg.span()[1]-4]
    return fileName

def getDatabaseNames():
    """
    Function is extracting names of all the available databases
    """
    databases = databaseDiscovery()
    names = []
    for database in databases:
        names.append(getFileName(database))
    return names

def graphAllDatabases():
    
    pass

