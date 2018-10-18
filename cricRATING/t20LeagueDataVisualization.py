import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pymongo
import os

def takePoints(elem):
    return elem[6]


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["cricHUBdb"]
mycol = mydb["t20Ranking"]

tournament_name = input("Enter t20 League Name: ")
year = input("Enter Year: ")


mydoc = mycol.find({"Tournament":tournament_name,"Year":year})
#print(mydoc)

team_names = []
col_names = ['Matches', 'Won', 'Lost', 'Tied', 'No Result', 'Points','Net Run Rate']
pnt_tbl = []
cnt = 0

data = []

for x in mydoc:

    team_names.append(x["Team"])

    pnt_tbl.append(x["Matches"])
    pnt_tbl.append(x["Won"])
    pnt_tbl.append(x["Lost"])
    pnt_tbl.append(x["Tied"])
    pnt_tbl.append(x["No Result"])
    pnt_tbl.append(x["Points"])
    pnt_tbl.append(x["Net Run Rate"])

    tmp= []

    tmp.append(x["Team"])
    tmp.append(x["Matches"])
    tmp.append(x["Won"])
    tmp.append(x["Lost"])
    tmp.append(x["Tied"])
    tmp.append(x["No Result"])
    tmp.append(int(x["Points"]))
    tmp.append(x["Net Run Rate"])

    data.append(tmp)

    #print(x["Team"],"",x["Matches"]," ",x["Won"]," ",x["Lost"]," ",x["Tied"]," ",x["No Result"]," ",x["Points"]," ",x["Net Run Rate"])

#print(team_names)
#print(pnt_tbl)

data.sort(key=takePoints,reverse=True)
print(col_names)
for i in data:
    print(i)

np_pnt_tbl = (np.array(pnt_tbl)).reshape(len(team_names),7)
#print(np_pnt_tbl)
np_pnt_tbl = np_pnt_tbl.astype(float)
#print(np_pnt_tbl)




team_abr = []

for teams in team_names:
    short_form = ''
    for initial in teams.split(' '):
            short_form = short_form + initial[0]
    team_abr.append(short_form)


title = tournament_name + " " +  year + ' Number of match won by teams'

val_ticks=[]
lost_ticks=[]
for i in range(len(team_names)):
    val_ticks.append(i)
    lost_ticks.append(i + 0.4)

# val_ticks = [1,2,3,4,5,6,7,8]
# lost_ticks = [1.4,2.4,3.4,4.4,5.4,6.4,7.4,8.4]

plt.bar(val_ticks,np_pnt_tbl[:,1],width=0.4,color='g',alpha=0.6,label='Won')
plt.bar(lost_ticks,np_pnt_tbl[:,2],width=0.4,color='r',alpha=0.6,label='Lost')
plt.yticks(val_ticks)
plt.ylabel("Matches")
plt.xticks(val_ticks,team_abr,rotation='vertical')
plt.grid(True)
plt.legend()
plt.title(title)

if os.path.exists("myfig.png"):
    os.remove("myfig.png")
plt.savefig("myfig.png")
#plt.show()
