from bs4 import BeautifulSoup
import  numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import requests

#bpls
#https://www.cricbuzz.com/cricket-series/2627/bangladesh-premier-league-2017/points-table
#https://www.cricbuzz.com/cricket-series/2526/bangladesh-premier-league-2016/points-table
#https://www.cricbuzz.com/cricket-series/2393/bangladesh-premier-league-2015/points-table
#https://www.cricbuzz.com/cricket-series/2172/bangladesh-premier-league-2013/points-table
#https://www.cricbuzz.com/cricket-series/2117/bangladesh-premier-league-2012/points-table

#ipls
#https://www.cricbuzz.com/cricket-series/2676/indian-premier-league-2018/points-table
#https://www.cricbuzz.com/cricket-series/2568/indian-premier-league-2017/points-table
#https://www.cricbuzz.com/cricket-series/2430/indian-premier-league-2016/points-table
#https://www.cricbuzz.com/cricket-series/2330/indian-premier-league-2015/points-table
#https://www.cricbuzz.com/cricket-series/2261/indian-premier-league-2014/points-table
#https://www.cricbuzz.com/cricket-series/2170/indian-premier-league-2013/points-table
#https://www.cricbuzz.com/cricket-series/2115/indian-premier-league-2012/points-table
#https://www.cricbuzz.com/cricket-series/2037/indian-premier-league-2011/points-table
#https://www.cricbuzz.com/cricket-series/2060/indian-premier-league-2010/points-table
#https://www.cricbuzz.com/cricket-series/2059/indian-premier-league-2009/points-table
#https://www.cricbuzz.com/cricket-series/2058/indian-premier-league-2008/points-table

#bbls
#https://www.cricbuzz.com/cricket-series/2727/big-bash-league-2018-19/points-table
#https://www.cricbuzz.com/cricket-series/2600/big-bash-league-2017-18/points-table
#https://www.cricbuzz.com/cricket-series/2471/big-bash-league-2016-17/points-table
#https://www.cricbuzz.com/cricket-series/2361/big-bash-league-2015-16/points-table
#https://www.cricbuzz.com/cricket-series/2302/big-bash-league-2014-15/points-table
#https://www.cricbuzz.com/cricket-series/2215/big-bash-league-2013-14/points-table
#https://www.cricbuzz.com/cricket-series/2161/big-bash-league-2012-13/points-table

#psls
#https://www.cricbuzz.com/cricket-series/2656/pakistan-super-league-2018/points-table
#https://www.cricbuzz.com/cricket-series/2412/pakistan-super-league-2016/points-table
#https://www.cricbuzz.com/cricket-series/2528/pakistan-super-league-2017/points-table


#cpls
#https://www.cricbuzz.com/cricket-series/2717/caribbean-premier-league-2018/points-table
#https://www.cricbuzz.com/cricket-series/2584/caribbean-premier-league-2017/points-table
#https://www.cricbuzz.com/cricket-series/2442/caribbean-premier-league-2016/points-table
#https://www.cricbuzz.com/cricket-series/2335/caribbean-premier-league-2015/points-table
#https://www.cricbuzz.com/cricket-series/2288/caribbean-premier-league-2014/points-table
#https://www.cricbuzz.com/cricket-series/2196/caribbean-premier-league-2013/points-table




page = requests.get("https://www.cricbuzz.com/cricket-series/2676/indian-premier-league-2018/points-table")
soup = BeautifulSoup(page.text,"lxml")
#print(soup.prettify())

tbl = soup.find("table",class_="table cb-srs-pnts");
#print(soup.prettify())

col_names = [x.get_text() for x in tbl.find_all('td',class_="cb-srs-pnts-th")]
col_names[5]='pts'
#print(col_names)

team_names = [x.get_text() for x in tbl.find_all('td',class_="cb-srs-pnts-name")]
#print(team_names)

pnt_tbl = [x.get_text() for x in tbl.find_all('td',class_="cb-srs-pnts-td")]
#print(pnt_tbl)

np_pnt_tbl = (np.array(pnt_tbl)).reshape(len(team_names),7)
np_pnt_tbl = np.delete(np_pnt_tbl,6,1)
np_pnt_tbl = np_pnt_tbl.astype(int)
#print(np_pnt_tbl)

consol_tbl = pd.DataFrame(np_pnt_tbl,index=team_names,columns=col_names)
consol_tbl.columns.name = "Teams"
print(consol_tbl)

team_abr = []

for teams in team_names:
    short_form = ''
    for initial in teams.split(' '):
            short_form = short_form + initial[0]
    team_abr.append(short_form)


title = 'IPL 2018 Number of match won by teams'

val_ticks = [1,2,3,4,5,6,7,8]
lost_ticks = [1.4,2.4,3.4,4.4,5.4,6.4,7.4,8.4]

plt.bar(val_ticks,np_pnt_tbl[:,1],width=0.4,color='g',alpha=0.6,label='Won')
plt.bar(lost_ticks,np_pnt_tbl[:,2],width=0.4,color='r',alpha=0.6,label='Lost')
plt.yticks(val_ticks)
plt.ylabel("Matches")
plt.xticks(val_ticks,team_abr,rotation='vertical')
plt.grid(True)
plt.legend()
plt.title(title)

plt.show()


