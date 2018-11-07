from flask import Blueprint, render_template

from cricSchedule.schedule_adapter import Adapter

app = Blueprint('schedule', __name__)


@app.route('/schedule/')
def schedule():
    data = Adapter()
    return render_template('schedule/Upcoming_matches.html', matches=data.get_match_data())
