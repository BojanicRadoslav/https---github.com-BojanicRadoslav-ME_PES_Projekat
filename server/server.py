from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from server.utils import LocalNetwork
from mainApp import McuCommunication

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def hello():
    return render_template('main.html')

@socketio.on('my_event', namespace='/test')
def test_message(message):
    print(message)

@socketio.on('buttonClick', namespace='/test')
def button_clicked(message):
    print("BUTTON CLICKED BABY")
    emit('my response', "ODGOVOR OD SERVERA")    



if __name__ == "__main__":
    app.run(host = LocalNetwork.getIp(), 
            port = LocalNetwork.getPort(), 
            debug = True)

    socketio.run(app)