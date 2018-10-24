from gevent import monkey
monkey.patch_all()

from flask import Flask, render_template, session, request, Blueprint
from flask_socketio import SocketIO, emit, join_room

from cricMongoDB.database import db
import pymongo, json

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'nuttertools'
socketio = SocketIO(app)

@app.route('/')
def chat():

  list = [];
  list = db.chat.find();

  message = [];
  for item in list:
    tmp = [];
    tmp.append(item["author"]);
    tmp.append(item["message"]);
    message.append(tmp);

  return render_template("chat.html", list=message)

@app.route('/login')
def login():
  return render_template('login.html')

@socketio.on('message', namespace='/chat')
def chat_message(message):

  print("message = ", message)
  print(message["data"]["author"] + " " + message["data"]["message"])

  if message["data"]["message"] != "":

    # insert into database
    db.chat.insert({"author": message["data"]["author"], "message": message["data"]["message"]});

    emit('message', {'data': message['data']}, broadcast=True)


@socketio.on('connect', namespace='/chat')
def test_connect():
  emit('my response', {'data': 'Connected', 'count': 0})

if __name__ == '__main__':
  socketio.run(app)