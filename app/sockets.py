from flask_socketio import SocketIO, send, emit
from flask import redirect
from . import socketio

@socketio.on('message')
def handle_message(message):
    print("Recieved message: " + message)
    if message != "User Connected!":
        send(message, broadcast=True)   

@socketio.on('start_game')
def start_game(data):
    print(data)
    print(type(data))
    username= data['username']
    gamemode= data['gamemode']
    print("user",username,"joined gamemode",gamemode)
    #emit('change_webpage', '/talk')
    ret_value = {'redirect':'/talk',
                'cookie': username}
    return ret_value