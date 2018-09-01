from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import requests
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["cricHUBdb"]
mycol = mydb["t20Ranking"]


# mydoc = mycol.find({"Tournament":"IPL","Year":"2011"})
#
# for x in mydoc:
#     print(x)

# bpls
# https://www.cricbuzz.com/cricket-series/2627/bangladesh-premier-league-2017/points-table
# https://www.cricbuzz.com/cricket-series/2526/bangladesh-premier-league-2016/points-table
# https://www.cricbuzz.com/cricket-series/2393/bangladesh-premier-league-2015/points-table
# https://www.cricbuzz.com/cricket-series/2172/bangladesh-premier-league-2013/points-table
# https://www.cricbuzz.com/cricket-series/2117/bangladesh-premier-league-2012/points-table

# ipls
# https://www.cricbuzz.com/cricket-series/2676/indian-premier-league-2018/points-table
# https://www.cricbuzz.com/cricket-series/2568/indian-premier-league-2017/points-table
# https://www.cricbuzz.com/cricket-series/2430/indian-premier-league-2016/points-table
# https://www.cricbuzz.com/cricket-series/2330/indian-premier-league-2015/points-table
# https://www.cricbuzz.com/cricket-series/2261/indian-premier-league-2014/points-table
# https://www.cricbuzz.com/cricket-series/2170/indian-premier-league-2013/points-table
# https://www.cricbuzz.com/cricket-series/2115/indian-premier-league-2012/points-table
# https://www.cricbuzz.com/cricket-series/2037/indian-premier-league-2011/points-table
# https://www.cricbuzz.com/cricket-series/2060/indian-premier-league-2010/points-table  - no points table
# https://www.cricbuzz.com/cricket-series/2059/indian-premier-league-2009/points-table  - no points table
# https://www.cricbuzz.com/cricket-series/2058/indian-premier-league-2008/points-table  - no points table

# bbls
# https://www.cricbuzz.com/cricket-series/2727/big-bash-league-2018-19/points-table
# https://www.cricbuzz.com/cricket-series/2600/big-bash-league-2017-18/points-table
# https://www.cricbuzz.com/cricket-series/2471/big-bash-league-2016-17/points-table
# https://www.cricbuzz.com/cricket-series/2361/big-bash-league-2015-16/points-table
# https://www.cricbuzz.com/cricket-series/2302/big-bash-league-2014-15/points-table
# https://www.cricbuzz.com/cricket-series/2215/big-bash-league-2013-14/points-table
# https://www.cricbuzz.com/cricket-series/2161/big-bash-league-2012-13/points-table

# psls
# https://www.cricbuzz.com/cricket-series/2656/pakistan-super-league-2018/points-table
# https://www.cricbuzz.com/cricket-series/2412/pakistan-super-league-2016/points-table
# https://www.cricbuzz.com/cricket-series/2528/pakistan-super-league-2017/points-table


# cpls
# https://www.cricbuzz.com/cricket-series/2717/caribbean-premier-league-2018/points-table
# https://www.cricbuzz.com/cricket-series/2584/caribbean-premier-league-2017/points-table
# https://www.cricbuzz.com/cricket-series/2442/caribbean-premier-league-2016/points-table
# https://www.cricbuzz.com/cricket-series/2335/caribbean-premier-league-2015/points-table
# https://www.cricbuzz.com/cricket-series/2288/caribbean-premier-league-2014/points-table
# https://www.cricbuzz.com/cricket-series/2196/caribbean-premier-league-2013/points-table


page = requests.get("https://www.cricbuzz.com/cricket-series/2717/caribbean-premier-league-2018/points-table")
soup = BeautifulSoup(page.text, "lxml")
# print(soup.prettify())

tbl = soup.find("table", class_="table cb-srs-pnts");
# print(soup.prettify())

col_names = [x.get_text() for x in tbl.find_all('td', class_="cb-srs-pnts-th")]
col_names[0] = 'Matches'
col_names[4] = 'No Result'
col_names[5] = 'Points'
col_names.append('Net Run Rate')
# print(col_names)

team_names = [x.get_text() for x in tbl.find_all('td', class_="cb-srs-pnts-name")]
# print(team_names)

pnt_tbl = [x.get_text() for x in tbl.find_all('td', class_="cb-srs-pnts-td")]
# print(len(team_names))
# print(len(pnt_tbl))

cnt = 0
for i in range(len(team_names)):
    thisdict = {}
    # print("Team ",team_names[i],end=" ",flush=True)
    thisdict["Team"] = team_names[i]
    for j in range(len(col_names)):
        # print(col_names[j],pnt_tbl[cnt],end=' ', flush=True)
        thisdict[str(col_names[j])] = pnt_tbl[cnt]
        cnt = cnt + 1

    thisdict["Tournament"] = "CPL"
    thisdict["Year"] = "2018"
    x = mycol.insert_one(thisdict)

    # print(thisdict)

# np_pnt_tbl = (np.array(pnt_tbl)).reshape(len(team_names),6)
# np_pnt_tbl = np.delete(np_pnt_tbl,6,1)
# np_pnt_tbl = np_pnt_tbl.astype(int)
# print(np_pnt_tbl)

# for i in np_pnt_tbl:
#     for j in range(len(i)):
#         print(i[j], end=' ', flush=True)
#     print()

# for i in range(0,8):
#     print(team_names[i])


# consol_tbl = pd.DataFrame(np_pnt_tbl,index=team_names,columns=col_names)
# consol_tbl.columns.name = "Teams"
# print(consol_tbl)
#
#
#
#
#
#
# team_abr = []
#
# for teams in team_names:
#     short_form = ''
#     for initial in teams.split(' '):
#             short_form = short_form + initial[0]
#     team_abr.append(short_form)
#
#
# title = 'IPL 2018 Number of match won by teams'
#
# val_ticks = [1,2,3,4,5,6,7,8]
# lost_ticks = [1.4,2.4,3.4,4.4,5.4,6.4,7.4,8.4]
#
# plt.bar(val_ticks,np_pnt_tbl[:,1],width=0.4,color='g',alpha=0.6,label='Won')
# plt.bar(lost_ticks,np_pnt_tbl[:,2],width=0.4,color='r',alpha=0.6,label='Lost')
# plt.yticks(val_ticks)
# plt.ylabel("Matches")
# plt.xticks(val_ticks,team_abr,rotation='vertical')
# plt.grid(True)
# plt.legend()
# plt.title(title)

# plt.show()
