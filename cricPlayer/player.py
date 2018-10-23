from flask import render_template, request, redirect, session, Blueprint
from bs4 import BeautifulSoup
import requests,os

app = Blueprint('player', __name__)


@app.route("/players/")
def search_players(player_list=None,search_status=None):
    if 'username' not in session.keys():
        return redirect('/auth/signin')

    return render_template("player/search.html",player_list=player_list,search_status=search_status)

@app.route("/players/show_players", methods=['POST', 'GET'])
def show_players():

    search_for = request.form.to_dict()["player_name"]
    search_for = search_for.lower()

    os.chdir(os.path.dirname(__file__))


    file = open(os.getcwd()+"/output.txt", "r")
    data = file.read()
    file_data = data
    file_data = file_data.splitlines()


    player_list = []
    for i in range(len(file_data)):

        x = file_data[i].split("|")


        name = x[0]
        href = "https://www.cricbuzz.com" + str(x[1])
        img = str(x[2])



        if (x[0].lower().find(search_for)) != -1:

            temp = {}
            temp["player_name"] = name.capitalize()
            temp["player_href"] = href
            temp["player_img"] = img


            player_list.append(temp)

    file.close()

    if player_list == []:
        return search_players(player_list,"Sorry No Data Found!!! <br/>Check Spelling and Try Again")
    return search_players(player_list)

@app.route("/players/show_profile", methods=['POST', 'GET'])
def show_profile():
    return "NOT YET IMPELEMENTED"