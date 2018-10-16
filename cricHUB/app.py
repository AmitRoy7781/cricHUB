from flask import Flask, render_template
from cricAuth.auth import app as auth
from cricRanking.show_ranking import app as ranking

app = Flask(__name__)
app.secret_key = 'TishuPaperIsNoMore'

# authentication blueprint
app.register_blueprint(auth)

# show ranking blueprint
app.register_blueprint(ranking)

@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(port=5000,debug=True)
