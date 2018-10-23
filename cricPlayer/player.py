from flask import render_template, request, redirect, session, Blueprint
from bs4 import BeautifulSoup
import requests

app = Blueprint('player', __name__)


@app.route("/players/")
def search_players(player_list=None):
    if 'username' not in session.keys():
        return redirect('/auth/signin')

    return render_template("player/search.html",player_list=player_list)

@app.route("/players/show_players", methods=['POST', 'GET'])
def show_players():

    search_for = request.form.to_dict()["player_name"]
    search_for = search_for.lower()



    file = open("/home/amit-roy/SDP Resources/cricHUB/cricPlayer/player_data.txt", "r")
    data = file.read()
    file_data = data
    file_data = file_data.lower()
    file_data = file_data.splitlines()


    player_list = []
    for i in range(len(file_data)):
        x = file_data[i].split("|")
        if (x[0].find(search_for)) != -1:
            url = x[1]
            print(url)
            res = requests.get(url)
            soup = BeautifulSoup(res.text, 'lxml')

            player = soup.find("div", {"id": "playerProfile"})
            soup = BeautifulSoup(str(player), 'lxml')

            temp = {}
            temp["player_name"] = soup.find("h1", {"itemprop": "name"}).text
            temp["player_img"] = soup.find("img", {"class": "cb-plyr-thum-img"})["src"]
            temp["player_country"] = soup.find("h3", {"class": "text-gray"}).text
            player_list.append(temp)

    file.close()

    return search_players(player_list)

@app.route("/players/show_profile", methods=['POST', 'GET'])
def show_profile():
    return "NOT YET IMPELEMENTED"
