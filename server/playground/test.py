import os, sys
import time
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from data.app import DataLogger
DataLogger.clearCsvFile()
DataLogger.logData(24, 55)
time.sleep(1)
DataLogger.logData(24, 54)
time.sleep(1)
DataLogger.logData(22, 55)
time.sleep(1)
DataLogger.logData(22, 55)
time.sleep(1)
DataLogger.logData(22, 55)
time.sleep(1)
DataLogger.logData(22, 55)
time.sleep(1)