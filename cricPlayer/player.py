import os
from flask import render_template, request, redirect, session, Blueprint
from cricPlayer.player_search import get_data

app = Blueprint('player', __name__)

class ConcreteCommand:

    @app.route("/players/show_profile", methods=['POST', 'GET'])
    def show_profile(self=None):
        url = request.form.to_dict()["player_url"]
        return get_data(url)

class Command:

    @app.route("/players/")
    def search_players(player_list=None, search_status=None):
        # if 'username' not in session.keys():
        #     return redirect('/auth/signin')

        if search_status is None:
            search_status = ""
        # print(search_status)
        return render_template("player/search.html", player_list=player_list, search_status=search_status)


class Receiever:

    @app.route("/players/show_players", methods=['POST', 'GET'])
    def show_players(self=None):
        search_for = request.form.to_dict()["player_name"]
        search_for = search_for.lower()

        if len(search_for) < 4:
            return Command.search_players(None, "Please type at least 4 characters")

        os.chdir(os.path.dirname(__file__))

        file = open(os.getcwd() + "/output.txt", "r")
        data = file.read()
        file_data = data
        file_data = file_data.splitlines()

        player_list = []
        for i in range(len(file_data)):

            x = file_data[i].split("|")

            name = x[0]
            href = "https://www.cricbuzz.com" + x[1]
            img = str(x[2])

            if (x[0].lower().find(search_for)) != -1:
                temp = {}
                temp["player_name"] = name.capitalize()
                temp["player_href"] = href
                temp["player_img"] = img

                player_list.append(temp)

        file.close()

        if player_list == []:
            return Command.search_players(player_list, "Sorry No Data Found!!! \n Check Spelling and Try Again")
        return Command.search_players(player_list, "Search Results")
