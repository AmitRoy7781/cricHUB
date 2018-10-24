import requests
from bs4 import BeautifulSoup
import pandas as pd

from cricSTAT.html_table_parser import HTMLTableParser


def scrape():
    url_start = "http://stats.espncricinfo.com/ci/engine/stats/index.html?class="
    url_end = ";filter=advanced;orderby=team;size=200;spanmin1=01+Jan+2008;spanval1=span;template=results;type=team;view=year"
    stats = []
    for i in range(1,4):
        url = url_start + str(i) + url_end
        hp = HTMLTableParser()
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        test = []
        for table in soup.find_all('table'):
            test.append(table)
        # print(len(test))
        table = hp.parse_html_table(test[2])  # Grabbing the table from the tuple
        # print(table.head())
        # print(table.shape)
        table.drop(table.columns[13], axis=1, inplace=True)
        if i ==1 :
            table['type'] = 'test'
            stats.append(table.copy())
        elif i == 2:
            table['type'] = 'odi'
            stats.append(table.copy())
        else:
            table['type'] = 't20i'
            stats.append(table.copy())

    return stats[0].append(stats[1], sort = False).append(stats[2], sort = False).fillna(0)




#table.to_csv("stat_team_year.csv", index= False)


if __name__ == '__main__':
    tb = scrape()
    print(list(tb))
