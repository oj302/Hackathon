from flask_socketio import SocketIO, send
from . import socketio

@socketio.on('message')
def handle_message(message):
    print("Recieved message: " + message)
    if message != "User Connected!":
        send(message, broadcast=True)   
