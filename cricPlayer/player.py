from flask import render_template, request, redirect, session, Blueprint

app = Blueprint('player', __name__)


@app.route("/players/")
def search_players():
    if 'username' not in session.keys():
        return redirect('/auth/signin')
    return render_template("player/search.html")