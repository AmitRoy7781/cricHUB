from flask import render_template, request, redirect, session, Blueprint
from cricMongoDB.database import db

app = Blueprint('ranking', __name__)

@app.route('/rankings/')
def show_ranking(data=None,rank_data=None):
    if 'username' not in session.keys():
        return redirect('/auth/signin')
    if rank_data is not None:
        data["contain_rank"] = True
    print(data)
    return render_template('ranking.html',ranking_info=data,rank_data=rank_data)

@app.route('/show_rank',methods=['POST', 'GET'])
def test():
    data = request.form.to_dict()
    format = data["format"]
    gender = data["gender"]
    rank_type = data["rank_type"]

    flag = True

    if format== 'test' and gender =='womens':
        flag= False
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

    if flag is True:
        posts = db.ranking
        myquery = {"format": format,"gender":gender,"player_type":rank_type}
        print(format)
        print(gender)
        print(rank_type)
        mydoc = posts.find(myquery)
        # print(mydoc)
        rank_data = []
        temp = {""}
        for x in mydoc:
            temp = {}
            # print(x)
            temp["rank"] = x["rank"]
            temp["name"] = x["name"]
            temp["rating"] = x["rating"]
            temp["gender"] = x["gender"]
            temp["format"] = x["format"]
            temp["player_type"] = x["player_type"]
            rank_data.append(temp)

        return render_template("show_ranking.html",ranking_info=data,rank_data=rank_data)

    return show_ranking(data,None)


