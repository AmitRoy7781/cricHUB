from flask import render_template, request, redirect, session, Blueprint
from cricPrediction.predictor import ServePrediction

app = Blueprint('predictions', __name__)

@app.route('/predictions/')
def predictions():
    return render_template("prediction/prediction.html")

@app.route('/pred-deliver/', methods=['GET', 'POST'])
def get_prediction():
    global team2, team1, venue
    if request.method == 'POST':
        team1 = request.form['team1']
        team2 = request.form['team2']
        venue = request.form['venue']
    if team1 == team2:
        return "Not found"
    predictor = ServePrediction(app.root_path)
    pred = predictor.predict(team1, team2, venue)
    formatted_pred = predictor.get_formatted_prediction(team1, team2, pred)
    return render_template("prediction/pred-deliver.html", pred = formatted_pred)