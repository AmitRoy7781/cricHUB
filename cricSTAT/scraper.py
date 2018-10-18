import requests
from bs4 import BeautifulSoup
import pandas as pd

from cricSTAT.html_table_parser import HTMLTableParser


def scrape():
    url = "http://stats.espncricinfo.com/ci/engine/stats/index.html?class=2;filter=advanced;orderby=team;" \
          "result=1;result=2;size=200;spanmin1=01+Jan+2008;spanval1=span;template=results;type=team;view=year"
    hp = HTMLTableParser()
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    test = []
    for table in soup.find_all('table'):
        test.append(table)
    #print(len(test))
    table = hp.parse_html_table(test[2])  # Grabbing the table from the tuple
    #print(table.head())
    #print(table.shape)
    table.drop(table.columns[13], axis=1, inplace=True)
    return table



#table.to_csv("stat_team_year.csv", index= False)
