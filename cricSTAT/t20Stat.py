from flask import render_template, request, redirect, session, Blueprint
from cricMongoDB.database import db

app = Blueprint('t20Stat', __name__)

@app.route('/stats/')
def stats(info = None,data=None):
    if 'username' not in session.keys():
        return redirect('/auth/signin')
    #print(info)
    return render_template('t20Stat.html',stat_info = info,stat_data=data)


@app.route('/show_stats',methods=['POST', 'GET'])
def show_stats():
    data = request.form.to_dict()
    Tournament = data["Tournament"]
    Year = data["Year"]

    flag = True

    if Tournament == 'Choose...':
        flag = False
        data["Tournament_msg"] = 'Choose one'

    if Year == 'Choose...':
        flag = False
        data["Year_msg"] = 'Choose one'

    if flag is True:
        posts = db.t20TournamentStat
        myquery = {"Tournament":Tournament,"Year":Year}
        mydoc = posts.find(myquery)

        stat_data=[]

        for x in mydoc:
            temp = {}
            temp["Team"] = x["Team"]
            temp["Matches"] = x["Matches"]
            temp["Won"] = x["Won"]
            temp["Lost"] = x["Lost"]
            temp["Tied"] = x["Tied"]
            temp["No Result"] = x["No Result"]
            temp["Net Run Rate"] = x["Net Run Rate"]
            temp["Points"] = x["Points"]
            stat_data.append(temp)
        return stats(data,stat_data)

    return  stats(data,None)