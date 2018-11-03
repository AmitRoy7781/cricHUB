import json
import os
import pandas as pd

from bson import json_util
from flask import Flask, jsonify, make_response

from cricMongoDB.database import db

app = Flask(__name__)

# DB_NAME = 'cric_backend'
# DB_HOST = 'ds143262.mlab.com'
# DB_PORT = 43262
# DB_USER = 'tht'
# DB_PASS = 'aabbcc11'
#
# connection = MongoClient(DB_HOST, DB_PORT)
# db = connection[DB_NAME]
# db.authenticate(DB_USER, DB_PASS)


def insert_data_from_dataframe(collection: str, data):
    data = pd.DataFrame.from_records(data[1:], columns= data[0])
    db_cm = db[collection]
    data_json = json.loads(data.to_json(orient='records'))
    db_cm.remove()
    db_cm.insert(data_json)



@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Notfound'}), 404)


@app.route("/get/bd")
def show_bd():
    response = db.team_stats.find({'Team': 'Bangladesh', 'type':'odi', 'Year' : '2010'}, {'_id': False})
    return json_util.dumps({'result': response})


@app.route("/get/player/mens/odi/batting")
def show_rank_pmo():
    response = db.ranking['player-rankings'].mens.odi.batting.find({},{'_id': False})
    return json_util.dumps(response)


@app.route("/insert/rank")
def insert_rank():
    from cricRATING.rankings_scrape import generate_ranking_data
    data = generate_ranking_data()
    insert_data_from_dataframe('ranking', data)
    return "success"


@app.route("/insert/stat")
def insert_stat():
    from cricSTAT import scraper
    data = scraper.scrape()
    data.drop(data.columns[14], axis=1, inplace=True)
    db_cm = db.team_stats
    data_json = json.loads(data.to_json(orient='records'))
    db_cm.remove()
    db_cm.insert(data_json)
    return "success"


if __name__ == "__main__":
    app.run()
