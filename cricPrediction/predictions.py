from flask import render_template, request, redirect, session, Blueprint

app = Blueprint('predictions', __name__)

@app.route('/predictions/')
def predictions():
    return "Not Yet Implemented"