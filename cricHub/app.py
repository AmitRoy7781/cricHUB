from flask import Flask
from flask import render_template

from cricHub.upcoming_matches import get_matches

app = Flask(__name__)


@app.route('/')
def hello_world():
    #return render_template('index.html', title='Home', matches=get_matches()) #use this if u have api key
    return render_template('index.html', title='Home')


if __name__ == '__main__':
    app.run(port=5000,debug=True)
