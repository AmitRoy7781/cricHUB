from flask import render_template, request, redirect, session, Blueprint

app = Blueprint('ranking', __name__)

@app.route('/rankings/')
def show_ranking():
    if 'username' not in session.keys():
        return redirect('/auth/signin')
    return render_template('ranking.html')
