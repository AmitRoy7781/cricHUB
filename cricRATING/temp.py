import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pymongo

def takePoints(elem):
    return elem[6]


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["cricHUBdb"]
mycol = mydb["t20Ranking"]

tournament_name = "PSL"


mydoc = mycol.find({"Tournament":tournament_name})
#print(mydoc)

team_names = []
col_names = ['Mat', 'Won', 'Lost', 'Tied', 'No Result', 'Points','Net Run Rate']
pnt_tbl = []
cnt = 0

data = []

for x in mydoc:

    print(x["Year"])