from bson import ObjectId
from flask import Flask, jsonify, request
from flask_pymongo import MongoClient

app = Flask(__name__)

DB_NAME = 'cric_backend'
DB_HOST = 'ds143262.mlab.com'
DB_PORT = 43262
DB_USER = 'tht'
DB_PASS = 'aabbcc11'

connection = MongoClient(DB_HOST, DB_PORT)
db = connection[DB_NAME]
db.authenticate(DB_USER, DB_PASS)

@app.route("/get/team")
def show_rank():
    response = db.ranking.find_one()
    return jsonify(response['team-rankings'])


@app.route("/get/player")
def show_rank_p():
    response = db.ranking.find_one({"_id": ObjectId("5b8d49d66f45632c1865b95c")})
    print(response)
    return jsonify(response['player-rankings'])



@app.route("/insert/rank")
def insert_rank():
    from cricRATING.rankings import generate_player_data, generate_team_data
    #db.ranking.insert_one(generate_team_data())
    db.ranking.insert_one(generate_player_data())
    return "success"



if __name__ == "__main__":
    app.run()