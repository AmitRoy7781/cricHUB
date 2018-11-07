import pytz
from flask import Flask, render_template

from cricAuth.auth import app as auth
from cricBETTING.betting import app as betting
from cricBLOG.blog import app as blog
from cricCHAT.cricCHAT import app as cricCHAT
from cricLIVE.livescore import app as livescore
from cricNEWS.news import app as news
from cricPlayer.player import app as player
from cricPrediction.predictions import app as prediction
from cricProfile.user_data import app as profile
from cricRanking.show_ranking import app as ranking_try
from cricSTAT.t20Stat import app as stat
from cricSchedule.schedule_blueprint import app as schedule

app = Flask(__name__)
app.secret_key = 'TishuPaperIsNoMore'


# authentication blueprint
app.register_blueprint(auth)

# live score blueprint
app.register_blueprint(livescore)

#schedule blueprint
app.register_blueprint(schedule)

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

if __name__ == '__main__':
    app.run()
