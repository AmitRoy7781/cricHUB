from flask import Flask, redirect, session, render_template

from cricAuth.auth import app as auth
from cricNEWS.news import app as news
from cricPlayer.player import app as player
from cricRanking.rank_try import app as ranking_try
from cricRanking.show_ranking import app as ranking
from cricSTAT.t20Stat import app as stat
from cricMongoDB.database import db
import cricAuth.auth

app = Flask(__name__)
app.secret_key = 'TishuPaperIsNoMore'

# authentication blueprint
app.register_blueprint(auth)

# show ranking blueprint
app.register_blueprint(ranking)
app.register_blueprint(ranking_try)

# t20 Statistics blueprint
app.register_blueprint(stat)

# news blueprint
app.register_blueprint(news)

# player blueprint
app.register_blueprint(player)


@app.route('/')
def home():
    if 'username' not in session.keys():
        return redirect('/auth/signin')
    return render_template('newsTwitter.html')


@app.route('/live-score/')
def score():
    if 'username' not in session.keys():
        return redirect('/auth/signin')

    return render_template('LiveScore.html')


@app.route('/contact-us/')
def profile():
    if 'username' not in session.keys():
        return redirect('/auth/signin')

    users = db.users

    loogged_in = session["username"]

    query = {"username": loogged_in}
    profile = users.find_one(query)

    return render_template('user_profile.html', name=profile["name"], email=profile["email"], phone=profile["phone_number"])

if __name__ == '__main__':
    app.run(port=5000, debug=True)
