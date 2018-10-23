from flask import render_template, request, redirect, session, Blueprint
from cricMongoDB.database import db
from bs4 import BeautifulSoup
import requests

app = Blueprint('ranking_try', __name__)


@app.route('/rankings_try/')
def ranking(rank_info=None):
    if 'username' not in session.keys():
        return redirect('/auth/signin')

    return render_template('ranking/ranking_try.html', ranking_info=rank_info)


@app.route('/show_rank_try', methods=['POST', 'GET'])
def show_ranking():
    if 'username' not in session.keys():
        return redirect('/auth/signin')

    data = request.form.to_dict()

    print(data)

    format = data["format"]
    gender = data["gender"]
    rank_type = data["rank_type"]

    rank_limit  = ""
    rank_status = ""

    if "rank_limit" in data:
        rank_limit = int(data["rank_limit"])
    if "rank_status" in data:
        rank_status = data["rank_status"]

    RANK_DATA = None

    flag = True

    if format == 'tests' and gender == 'womens':
        flag = False
        data["gender_msg"] = 'No data for womens in test cricket.'

    if format == 'Choose...':
        flag = False
        data["format_msg"] = 'Choose one'

    if gender == 'Choose...':
        flag = False
        data["gender_msg"] = 'Choose one'

    if rank_type == 'Choose...':
        flag = False
        data["rank_type_msg"] = 'Choose one'

    if flag is False:
        return ranking(data)

    if gender == "womens":

        temp_format, temp_rank_type = change_params(format, rank_type)

        posts = db.ranking

        myquery = {"format": temp_format, "gender": gender, "player_type": temp_rank_type}
        mydoc = posts.find(myquery)

        WOMAN_DATA = []

        for x in mydoc:
            temp = {}
            temp["rank"] = x["rank"]
            temp["name"] = x["name"]
            temp["rating"] = x["rating"]
            WOMAN_DATA.append(temp)

        print(WOMAN_DATA)
        RANK_DATA = WOMAN_DATA
        # return "OK"

    elif rank_type == "teams":

        soup, maindiv = get_element(rank_type, format)
        # print(soup)
        TEAM_DATA = []

        for d in maindiv[1:]:
            temp = {}
            row_data = u",".join(
                s.strip() for s in filter(None, (t.find(text=True, recursive=False) for t in d.find_all())))
            if row_data:
                row_data = row_data.split(',')
                temp["position"] = row_data[0]
                temp["country"] = row_data[1]
                temp["rating"] = row_data[2]
                temp["points"] = row_data[3]

                TEAM_DATA.append(temp)

        print(TEAM_DATA)
        RANK_DATA = TEAM_DATA
        # return "OK"

    else:

        url = "https://www.cricbuzz.com/cricket-stats/icc-rankings"

        if rank_type == "batsmen":
            url = url + "/batsmen-rankings"
        elif rank_type == "bowlers":
            url = url + "/bowlers-rankings"

        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'lxml')

        scrape_html = soup.find('div', {'ng-show': "'" + rank_type + "-" + format + "' == act_rank_format"})
        soup = BeautifulSoup(str(scrape_html), 'lxml')

        # print(soup)
        POSITION_INDICATOR_CLASS = soup.find_all(['span', {'class': 'cb-ico'}, ])
        # print(POSITION_INDICATOR_CLASS)
        IMG = soup.find_all('img', {'class': 'cb-rank-plyr-img'})
        # print(IMG)

        soup, maindiv = get_element(rank_type, format)
        # print(maindiv)

        PLAYER_DATA = []

        for d in maindiv[1:]:
            temp = {}
            row_data = u",".join(
                s.strip() for s in filter(None, (t.find(text=True, recursive=False) for t in d.find_all())))
            if row_data:
                row_data = row_data.split(',')
                temp["position"] = row_data[0]
                temp["position_change"] = row_data[3]
                temp["name"] = row_data[5]
                temp["country"] = row_data[6]
                temp["rating"] = row_data[7]

                if rank_type == "batsmen" or rank_type == "bowlers":
                    temp["best_rank"] = row_data[8]

                PLAYER_DATA.append(temp)

        for i in range(len(PLAYER_DATA)):
            # PLAYER_DATA[i]["img_url"] = "http:" + IMG[i]["src"]
            PLAYER_DATA[i]["img_url"] = IMG[i]["src"]
            PLAYER_DATA[i]["position_indicator_class"] = POSITION_INDICATOR_CLASS[i]["class"][0]

            if PLAYER_DATA[i]["position_indicator_class"] == "cb-rank-diff-up":
                PLAYER_DATA[i]["position_change"] = "+" + PLAYER_DATA[i]["position_change"]
            elif PLAYER_DATA[i]["position_indicator_class"] == "cb-rank-diff-down":
                PLAYER_DATA[i]["position_change"] = "-" + PLAYER_DATA[i]["position_change"]

            # temp = PLAYER_DATA[i]
            # print(temp["position_indicator_class"])

        RANK_DATA = PLAYER_DATA



    #print(RANK_DATA)


    print(rank_limit)
    print(len(RANK_DATA))

    if rank_limit is "" or rank_limit==len(RANK_DATA):
        rank_limit = 10
    else:
        rank_limit = len(RANK_DATA)

    if rank_status is "" or rank_status == "Top 10":
        rank_status = "Full Ranking"
    else:
        rank_status = "Top 10"

    print("Updated ", rank_limit)

    return render_template("ranking/show_ranking_try.html"
                       , format=format
                       , gender=gender
                       , rank_type=rank_type
                       , RANK_DATA = RANK_DATA
                       , rank_limit = rank_limit
                       , rank_status = rank_status)


def get_element(rank_type, format):
    url = "https://www.cricbuzz.com/cricket-stats/icc-rankings/"

    if rank_type == "batsmen":
        url = url + "batsmen-rankings"
        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'lxml')

    elif rank_type == "bowlers":
        url = url + "bowlers-rankings"
        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'lxml')

    elif rank_type == "all-rounders":
        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'lxml')

    elif rank_type == "teams":
        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'lxml')

    # print("#" + rank_type + "-" + format + " div.text-center")

    maindiv = soup.select("#" + rank_type + "-" + format + " div.text-center")
    return soup, maindiv


def change_params(format, rank_type):
    temp_format = ""
    temp_rank_type = ""

    if format == "tests":
        temp_format = "test"
    elif format == "odis":
        temp_format = "odi"
    else:
        temp_format = "t20i"

    if rank_type == "batsmen":
        temp_rank_type = "batting"
    elif rank_type == "bowlers":
        temp_rank_type = "bowling"
    elif rank_type == "all-rounders":
        temp_rank_type = "all-rounder"
    elif rank_type == "teams":
        temp_rank_type = "team"

    return temp_format, temp_rank_type
