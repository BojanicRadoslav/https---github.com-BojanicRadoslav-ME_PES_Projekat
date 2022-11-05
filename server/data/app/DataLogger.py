from datetime import date, datetime
import csv

timeLog = {}
"""Dictionary for logging data of the current day"""


def getDate():
    """Function will return todays date"""
    return date.today()

def logData(temperature: float, humidity: float):
    """
    Funnction will log data in timeLog dictionary and write it to the active CSV file
    """
    global timeLog
    timeLog[getTime()] = temperature, temperature
    print("Log entry: ", getDate(), getTime(), temperature, humidity)
    csvFile = 'data\database\\' + str(getDate()) + '.csv'
    with open(csvFile, "a+", newline='') as file:
            writer = csv.writer(file) 
            data = getTime(), temperature, humidity
            writer.writerow(data)

def getTimeLog():
    return timeLog

def generateCsv():
    """
    Function will re-generate CSV file from timeLog dictionary
    """
    csvFile = 'data\database\\' + str(getDate()) + '.csv'
    with open(csvFile, "w+", newline='') as file:
        writer = csv.writer(file)
        for element in timeLog:
            data = element, timeLog[element][0], timeLog[element][1]
            writer.writerow(data)

def clearCsvFile(file = 'data\database\\' + str(getDate()) + '.csv'):
    open(file, "w").close()

def generateGraph():
    pass



def getTime():
    """Function is returning current time in format %H:%M:%S"""
    now = datetime.now()
    return now.strftime("%H:%M:%S")
    pass


