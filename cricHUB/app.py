from flask import Flask,redirect,session, render_template
from cricAuth.auth import app as auth
from cricRanking.show_ranking import app as ranking
from cricSTAT.t20Stat import app as stat
from cricNEWS.news import app as news

app = Flask(__name__)
app.secret_key = 'TishuPaperIsNoMore'

# authentication blueprint
app.register_blueprint(auth)

# show ranking blueprint
app.register_blueprint(ranking)

# t20 Statistics blueprint
app.register_blueprint(stat)

# news blueprint
app.register_blueprint(news)


@app.route('/')
def home():
    if 'username' not in session.keys():
        return redirect('/auth/signin')
    return render_template('newsTwitter.html')


@app.route('/live-score/')
def score():
    return render_template('LiveScore.html')


if __name__ == '__main__':
    app.run(port=5000,debug=True)
