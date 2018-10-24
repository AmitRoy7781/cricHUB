from cffi.setuptools_ext import execfile
from flask import Flask,redirect,session, render_template
#from twisted.python.compat import execfile

# start
from gevent import monkey
monkey.patch_all()
from flask_socketio import SocketIO, emit, join_room
from cricMongoDB.database import db
import pymongo, json
# end

from cricAuth.auth import app as auth
from cricRanking.show_ranking import app as ranking
from cricRanking.rank_try import app as ranking_try
from cricSTAT.t20Stat import app as stat
from cricNEWS.news import app as news
from cricPlayer.player import app as player
#from cricCHAT.server import app as chat
#from cricCHAT import server

app = Flask(__name__)
app.secret_key = 'TishuPaperIsNoMore'

# start
app.debug = True
socketio = SocketIO(app)
# end

# authentication blueprint
app.register_blueprint(auth)

# show ranking blueprint
app.register_blueprint(ranking)
app.register_blueprint(ranking_try)

# t20 Statistics blueprint
app.register_blueprint(stat)

# news blueprint
app.register_blueprint(news)

#player blueprint
app.register_blueprint(player)

#chat-box
#app.register_blueprint(chat)

@app.route('/')
def home():
    if 'username' not in session.keys():
        return redirect('/auth/signin')
    return render_template('newsTwitter.html')

@app.route('/live-score/')
def score():
    return render_template('LiveScore.html')

#@app.route('/chat-box')
#def chat():
#    execfile('server.py')


# start
@app.route('/chat-box/')
def chat():

  data = [];
  data = db.chat.find();

  message = [];
  for item in data:
    tmp = [];
    tmp.append(item["author"]);
    tmp.append(item["message"]);
    message.append(tmp);

  return render_template("chat.html", list=message)

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

# end
if __name__ == '__main__':
    app.run(port=5000, debug=True)
