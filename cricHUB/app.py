import pytz
from flask import Flask, redirect, session, render_template, make_response, request

from cricMongoDB.database import db

from cricAuth.auth import app as auth
from cricCHAT.cricCHAT import app as cricCHAT
from cricLIVE.livescore import app as livescore
from cricNEWS.news import app as news
from cricPlayer.player import app as player
from cricPrediction.predictions import app as prediction
from cricProfile.user_data import app as profile
from cricRanking.show_ranking import app as ranking_try
from cricSTAT.t20Stat import app as stat
from cricBLOG.blog import app as blog
from cricBETTING.betting import app as betting


app = Flask(__name__)
app.secret_key = 'TishuPaperIsNoMore'


# authentication blueprint
app.register_blueprint(auth)

# live score blueprint
app.register_blueprint(livescore)

# prediction blueprint
app.register_blueprint(prediction)

# show ranking blueprint
app.register_blueprint(ranking_try)

# t20 Statistics blueprint
app.register_blueprint(stat)

# news blueprint
app.register_blueprint(news)

# player blueprint
app.register_blueprint(player)

# user profile blueprint
app.register_blueprint(profile)

# user profile blueprint
app.register_blueprint(cricCHAT)

# blog blueprint
app.register_blueprint(blog)

# betting blueprint
app.register_blueprint(betting)


@app.route('/')
def home():
    # if 'username' not in session.keys():
    #     return redirect('/auth/signin')
    return render_template('index.html')


@app.template_filter('formatdatetime')
def format_datetime(value, format="%a %d %B %I:%M %p"):
    if value is None:
        return ""
    tz = pytz.timezone('Asia/Dacca')  # timezone you want to convert to from UTC
    utc = pytz.timezone('UTC')
    value = utc.localize(value, is_dst=None).astimezone(pytz.utc)
    local_dt = value.astimezone(tz)
    return local_dt.strftime(format)


# start
@app.route('/chat-box/')
def chat():
    if 'username' not in session.keys():
        return redirect('/auth/signin')

    data = []
    data = db.chat.find()

    message = []
    for item in data:
        tmp = []
        tmp.append(item["author"])
        tmp.append(item["message"])
        message.append(tmp)

    if request.cookies.get('realtime-chat-nickname') is None:
        res = make_response(render_template("chat.html", list=message))
        res.set_cookie('realtime-chat-nickname', session['username'])
        print(res)
        return res

    else:
        return render_template("chat.html", list=message)


@app.route('/schedule/')
def schedule():
    from cricSchedule import schedule_adapter
    data = schedule_adapter.Adapter()
    return render_template('schedule/Upcoming_matches.html', matches=data.get_match_data())


if __name__ == '__main__':
    app.run()
