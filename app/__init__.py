from flask import Flask
from flask_socketio import SocketIO,send

def create_app():
    global socketio
    app = Flask(__name__)
    from .routes import main
    app.register_blueprint(main)
    app.config['SECRET'] = "123!DontTell"
    socketio = SocketIO(app, cors_allowed_origins="*")
    from . import sockets
    return app, socketio
