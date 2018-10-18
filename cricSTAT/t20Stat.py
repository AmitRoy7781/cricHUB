from flask import render_template, request, redirect, session, Blueprint
from cricMongoDB.database import db
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

app = Blueprint('t20Stat', __name__)

def takePoints(elem):
    return elem[6]

@app.route('/stats/')
def stats(info = None,data=None,image=None):
    if 'username' not in session.keys():
        return redirect('/auth/signin')
    #print(info)
    return render_template('t20Stat.html',stat_info = info,stat_data=data,stat_image=image)


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

        team_names = []
        col_names = ['Matches', 'Won', 'Lost', 'Tied', 'No Result', 'Points', 'Net Run Rate']
        pnt_tbl = []
        cnt = 0

        for x in mydoc:
            team_names.append(x["Team"])

            pnt_tbl.append(x["Matches"])
            pnt_tbl.append(x["Won"])
            pnt_tbl.append(x["Lost"])
            pnt_tbl.append(x["Tied"])
            pnt_tbl.append(x["No Result"])
            pnt_tbl.append(x["Points"])
            pnt_tbl.append(x["Net Run Rate"])

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

        np_pnt_tbl = (np.array(pnt_tbl)).reshape(len(team_names), 7)
        np_pnt_tbl = np_pnt_tbl.astype(float)
        team_abr = []

        for teams in team_names:
            short_form = ''
            for initial in teams.split(' '):
                short_form = short_form + initial[0]
            team_abr.append(short_form)

        title = Tournament + " " + Year + ' Number of match won by teams'

        val_ticks = []
        lost_ticks = []
        for i in range(len(team_names)):
            val_ticks.append(i)
            lost_ticks.append(i + 0.4)

        # val_ticks = [1,2,3,4,5,6,7,8]
        # lost_ticks = [1.4,2.4,3.4,4.4,5.4,6.4,7.4,8.4]

        plt.bar(val_ticks, np_pnt_tbl[:, 1], width=0.4, color='g', alpha=0.6, label='Won')
        plt.bar(lost_ticks, np_pnt_tbl[:, 2], width=0.4, color='r', alpha=0.6, label='Lost')
        plt.yticks(val_ticks)
        plt.ylabel("Matches")
        plt.xticks(val_ticks, team_abr, rotation='vertical')
        plt.grid(True)
        plt.legend()
        plt.title(title)

        if os.path.exists("myfig.png"):
            os.remove("myfig.png")

        plt.savefig("myfig.png")


        #stat_data.sort(key=takePoints, reverse=True)
        return stats(data,stat_data)

    return  stats(data,None)