from flask import Flask, render_template
from cricAuth.auth import app as auth

app = Flask(__name__)
app.secret_key = 'TishuPaperIsNoMore'

# authentication blueprint
app.register_blueprint(auth)


@app.route('/rankings/')
def show_ranking():
    return render_template('ranking.html')


@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(port=5000,debug=True)
