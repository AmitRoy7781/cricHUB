<<<<<<< HEAD
from gevent import monkey
monkey.patch_all()

from flask import Flask, render_template, session, request
from flask_socketio import SocketIO, emit, join_room

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'nuttertools'
socketio = SocketIO(app)


=======
>>>>>>> 80dc6e7fdc85f621808a06baa2fb0c5de1fca90e
