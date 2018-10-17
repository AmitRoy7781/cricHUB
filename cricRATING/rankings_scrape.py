import csv

from bs4 import BeautifulSoup
import requests
import pprint


def scrape_url(url, tp):
    try:
        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'lxml')
        a = soup.find_all('tr', {'class': 'table-body'})
        data = {}
        for i in a:
            team = []
            name = ''
            rating = ''
            try:
                rank = int(i.contents[1].text)
            except:
                pass
            try:
                name = i.contents[3].text.replace('\n', '')
                name = " ".join(name.split())
                if rank == 1 and tp == 'player-rankings':
                    name = name[0:-3]
            except:
                pass

            try:
                rating = i.contents[9].text
            except:
                if rank == 1:
                    rating = i.contents[5].text
                else:
                    rating = i.contents[7].text

            team.extend([name, rating])
            data[rank] = team

        return data

    except:
        print("Sorry couldn't find the data right now")


def save_to_csv(data, name:str):
    name = name + '.csv'
    with open(name, 'w', newline='') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(data)
    csvFile.close()
    return

def get_formatted_data(data, url, gender, match_format, tp, player_type=""):
    raw_data = scrape_url(url, tp)
    if (tp == 'team-rankings'):
        for i in sorted(raw_data):
            data.append([gender, match_format, 'team', i, raw_data[i][0], raw_data[i][1]])
    else:
        for i in sorted(raw_data):
            data.append([gender, match_format, player_type, i, raw_data[i][0], raw_data[i][1]])
    return data

def generate_team_data(data):
    gender = ['mens', 'womens']
    m_format = ['test', 'odi', 't20i']
    base_url = 'https://www.icc-cricket.com/rankings/'
    tp = 'team-rankings'

    #team
    for g in gender:
        for m in m_format:
            if (g == 'womens') and (m == 'test'):
                continue
            url = base_url + g + '/team-rankings/' + m
            data = get_formatted_data(data, url=url, gender=g, match_format=m, tp=tp)
            #save_to_csv(data, collection.replace('.', '_'))

    return data


def generate_player_data(data):
    gender = ['mens', 'womens']
    m_format = ['odi', 't20i', 'test']
    player_type = ['batting', 'bowling','all-rounder']
    base_url = 'https://www.icc-cricket.com/rankings/'
    tp = 'player-rankings'
    for g in gender:
        for m in m_format:
            if (g == 'womens') and (m == 'test'):
                continue
            for p in player_type:
                url = base_url + g + '/player-rankings/' + m + '/' + p
                data = get_formatted_data(data,url, g, m, tp,p)
                #save_to_csv(data, collection.replace('.', '_'))
    return data


def generate_ranking_data():
    data = [['gender', 'format', 'player_type', 'rank', 'name', 'rating']]
    data = generate_team_data(data)
    data = generate_player_data(data)
    return data


if __name__ == "__main__":
    pprint.pprint(generate_ranking_data())
    # pprint.pprint(generate_player_data())