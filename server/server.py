"""
Main server app for handling client communication
"""

from flask import Flask, render_template, send_from_directory
from flask_socketio import SocketIO, emit
from utils import LocalNetwork
from mainApp import McuCommunication
from data.app.DataLogger import getDateTime
from data.app import Plotter
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['GRAPHS'] = 'server\data\graphs'
socketio = SocketIO(app)

relay_1 = False
relay_2 = False

@app.route('/')
def mainPage():
    """
    Function is used to return main html page to the client
    """
    return render_template('mainPage.html')

@app.route('/relayCtrl')
def relayCtrlPage():
    return render_template('relayControl.html')

@app.route('/graphingService')
def graphingServicePage():
    return render_template('graphs.html')

@app.route('/stmSettings')
def stmSettingsPage():
    return render_template('stm32Settings.html')

@app.route('/graphingService/<database>')
def databaseOpen(database):
    # Plotter.generatePng(database)
    Plotter.generatePng('server\\data\\database\\' + database + '.csv')
    full_filename = Plotter.getPngPathFromFileName(database)
    return render_template("showPlot.html", plot = full_filename)
    return 

# start of main page socketio events
@socketio.on('my_event', namespace='/mainPage')
def test_message(message):
    """
    Handler for receiving event named my_event from JS client
    """
    print(message)

@socketio.on('dateTimeRequest', namespace='/mainPage')
def sendTime(data):
    emit('dateTime', getDateTime())

# end of main page socketio events

# start of relay ctrl socketio events
@socketio.on('dateTimeRequest', namespace='/relayCtrl')
def sendTime(data):
    emit('dateTime', getDateTime())

@socketio.on('ConnectRelays', namespace='/relayCtrl')
def relayState():
    global relay_1, relay_2
    msg = "connect"
    emit('onRelay1', msg)
    emit('onRelay1', relay_1)
    emit('onRelay2', msg)
    emit('onRelay2', relay_2)

@socketio.on('relay1Ctrl', namespace='/relayCtrl')
def relay1Ctrl():
    global relay_1
    if relay_1 is 1:
        relay_1 = 0
    else:
        relay_1 = 1
    emit('onRelay1', relay_1, broadcast=True)

@socketio.on('relay2Ctrl', namespace='/relayCtrl')
def relay2Ctrl():
    global relay_2
    if relay_2 is 1:
        relay_2 = 0
    else:
        relay_2 = 1
    emit('onRelay2', relay_2, broadcast=True)
# end of relat ctrl socketio even

# start of graphing service socketio events
@socketio.on('dateTimeRequest', namespace='/graphingService')
def sendTime(data):
    emit('dateTime', getDateTime())

@socketio.on('getDatabases', namespace='/graphingService')
def getDatabases():
    datbases = Plotter.getDatabaseNames()
    print("\n\n\n", datbases, "\n\n\n")
    print(Plotter.databaseDiscovery())
    emit('onDatabaseNames', datbases)
# end of graphing service socketio events

# start of stm commander socketio events
@socketio.on('dateTimeRequest', namespace='/stmCommander')
def sendTime(data):
    emit('dateTime', getDateTime())
# end of stm commander socketio events

# start of stm32 socketio events
@socketio.on('StmMeasurments', namespace='/stm32')
def receiveMeasurements(data):
    McuCommunication.receiveMeasurments(data)
    emit('onStmData', data)
#  end of stm32 socketio events


if __name__ == "__main__":
    print(getDateTime())
    app.run(host = LocalNetwork.getIp(), 
            port = LocalNetwork.getPort(), 
            debug = True)

    socketio.run(app)