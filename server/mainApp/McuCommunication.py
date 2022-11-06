import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from data.app import DataLogger


def receiveMeasurments(temperature, humidity):
    """
    Funtion is forwarding data from STM to dataLogger
    """
    DataLogger.logData(temperature, humidity)


def setMeasurmentPeriod():
    pass