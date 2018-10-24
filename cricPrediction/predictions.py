from flask import render_template, request, redirect, session, Blueprint

app = Blueprint('predictions', __name__)

@app.route('/predictions/')
def predictions():
    return render_template("prediction/prediction.html")