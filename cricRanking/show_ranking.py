import requests
from bs4 import BeautifulSoup
from flask import render_template, request, redirect, session, Blueprint

from cricMongoDB.database import db

app = Blueprint('ranking', __name__)


class Decorator:


    def get_element(url,rank_type, format):

        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'lxml')

        # print("#" + rank_type + "-" + format + " div.text-center")
        #print(url)

        param1 = ""
        param2 = ""
        param3 = ""

        if rank_type=="batting":
            rank_type = "batsmen"
        elif rank_type == "bowling":
            rank_type = "bowlers"
        elif rank_type == "team":
            rank_type = "teams"
        elif rank_type=="all-rounder":
            rank_type = "allrounders"  #kaj na korle remove hyphen

        if format == "test":
            format = "tests"
        elif format == "odi":
            format = "odis"
        else:
            format = "t20s"


        maindiv = soup.select("#" + rank_type + "-" + format + " div.text-center")
        #print(maindiv)
        return soup, maindiv


def change_params(rank_type, format):

    temp_rank_type = ""
    temp_format = ""

    if rank_type == "batting":
        temp_rank_type = "batsmen"
    elif rank_type == "bowling":
        temp_rank_type = "bowlers"
    elif rank_type == "team":
        temp_rank_type = "teams"
    elif rank_type == "all-rounder":
        temp_rank_type = "allrounders"  # kaj na korle remove hyphen

    if format == "test":
        temp_format = "tests"
    elif format == "odi":
        temp_format = "odis"
    else:
        temp_format = "t20s"

    return temp_rank_type,temp_format



class ConcreteComponent:


    @app.route('/rankings/')
    def ranking(rank_info=None):
        # if 'username' not in session.keys():
        #     return redirect('/auth/signin')

        return render_template('ranking/ranking.html', ranking_info=rank_info)


class Component:


    @app.route('/show_rank', methods=['POST', 'GET'])
    def show_ranking(self=None):
        # if 'username' not in session.keys():
        #     return redirect('/auth/signin')

        data = request.form.to_dict()

        #print(data)

        format = data["format"]
        gender = data["gender"]
        rank_type = data["rank_type"]

        rank_limit = ""
        rank_status = ""

        if "rank_limit" in data:
            rank_limit = int(data["rank_limit"])
        if "rank_status" in data:
            rank_status = data["rank_status"]

        RANK_DATA = None

        flag = True

        if format == 'test' and gender == 'women':
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
            return ConcreteComponent.ranking(data)

        url = "https://www.cricbuzz.com/cricket-stats/icc-rankings"

        url = url + "/" + gender + "/" + rank_type

        #print(url)



        #if rank type is teams then no image is available

        if rank_type!="teams":


            res = requests.get(url)
            soup = BeautifulSoup(res.text, 'lxml')

            temp_rank_type,temp_format = change_params(rank_type,format)
            scrape_html = soup.find('div', {'ng-show': "'" + temp_rank_type + "-" + temp_format + "' == act_rank_format"})
            soup = BeautifulSoup(str(scrape_html), 'lxml')

            #print(soup)
            POSITION_INDICATOR_CLASS = soup.find_all(['span', {'class': 'cb-ico'}, ])
            # print(POSITION_INDICATOR_CLASS)
            IMG = soup.find_all('img', {'class': 'img-responsive cb-rank-plyr-img'})
            #print(IMG)

            soup, maindiv = Decorator.get_element(url,rank_type, format)
            #print(maindiv)

            PLAYER_DATA = []

            for d in maindiv[1:]:
                temp = {}
                row_data = u",".join(
                    s.strip() for s in filter(None, (t.find(text=True, recursive=False) for t in d.find_all())))
                if row_data:
                    # print(row_data)
                    row_data = row_data.split(',')
                    temp["position"] = row_data[0]
                    temp["position_change"] = row_data[3]
                    temp["name"] = row_data[5]
                    temp["country"] = row_data[6]
                    temp["rating"] = row_data[7]

                    #print(temp)

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



        #Rank Type is not Teams so we can show images
        else:


            soup, maindiv = Decorator.get_element(url,rank_type, format)
            #print(soup.prettify())
            #print(maindiv)
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
                    #print(temp)
            # print(TEAM_DATA)
            RANK_DATA = TEAM_DATA
            # print(RANK_DATA)




        # print(RANK_DATA)

        # print(rank_limit)
        # print(len(RANK_DATA))

        if rank_limit is "" or rank_limit == len(RANK_DATA):
            rank_limit = 10
        else:
            rank_limit = len(RANK_DATA)

        if rank_status is "" or rank_status == "Top 10":
            rank_status = "Full Ranking"
        else:
            rank_status = "Top 10"

        # print("Updated ", rank_limit)

        return render_template("ranking/show_ranking.html"
                               , format=format
                               , gender=gender
                               , rank_type=rank_type
                               , RANK_DATA=RANK_DATA
                               , rank_limit=rank_limit
                               , rank_status=rank_status)