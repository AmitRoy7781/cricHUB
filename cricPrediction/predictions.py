from flask import render_template, request, redirect, session, Blueprint, flash
from cricPrediction.predictor import ServePrediction

app = Blueprint('predictions', __name__)

@app.route('/predictions/')
def predictions():
    if 'username' not in session.keys():
        return redirect('/auth/signin')
    return render_template("prediction/prediction.html")

@app.route('/pred-deliver/', methods=['GET', 'POST'])
def get_prediction():
    global team2, team1, venue
    if request.method == 'POST':
        team1 = request.form['team1']
        team2 = request.form['team2']
        venue = request.form['venue']
    if team1 == team2:
        flash('Please select different teams')
        return render_template("prediction/prediction.html")
    predictor = ServePrediction(app.root_path)
    pred = predictor.predict(team1, team2, venue)
    formatted_pred = predictor.get_formatted_prediction(team1, team2, pred)
    legend = [team1+ ' bats first', team2 + ' bats first']
    labels = [team1, team2]
    values1 = pred[0, :].flatten().tolist()
    values2 = pred[1, :].flatten().tolist()
    return render_template('prediction/pred-deliver.html',
                               pred=formatted_pred, values1=values1, values2=values2, labels=labels, legend=legend)
