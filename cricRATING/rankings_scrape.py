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

def get_formatted_data(url, gender, match_format, tp, player_type=""):
    raw_data = scrape_url(url, tp)
    data = []
    if (tp == 'team-rankings'):
        collection = tp + '.' + gender + '.' + match_format
        data.append(['Rank', 'Team', 'Rating'])
        for i in sorted(raw_data):
            data.append([i, raw_data[i][0], raw_data[i][1]])
    else:
        collection = tp + '.' + gender + '.' + match_format + '.' + player_type
        data.append(['Rank', 'Player', 'Rating'])
        for i in sorted(raw_data):
            data.append([i, raw_data[i][0], raw_data[i][1]])
    return collection, data

def generate_team_data(collections):
    gender = ['mens', 'womens']
    m_format = ['test', 'odi', 't20i']
    base_url = 'https://www.icc-cricket.com/rankings/'
    tp = 'team-rankings'

    #team
    for g in gender:
        if (g == 'mens'):
            for m in m_format:
                url = base_url + g + '/team-rankings/' + m
                collection, data = get_formatted_data(url=url, gender=g, match_format=m, tp=tp)
                collections[collection] = data
                #save_to_csv(data, collection.replace('.', '_'))
        else:
            url = base_url + g + '/team-rankings/'
            collection, data = get_formatted_data(url=url, gender=g, match_format='all', tp=tp)
            collections[collection] = data
            #save_to_csv(data, collection.replace('.', '_'))

    return collections


def generate_data():
    collections = {}
    collections = generate_team_data(collections)
    collections = generate_player_data(collections)
    return collections


def generate_player_data(collections):
    gender = ['mens', 'womens']
    m_format = ['odi', 't20i']
    player_type = ['batting', 'bowling','all-rounder']
    base_url = 'https://www.icc-cricket.com/rankings/'
    tp = 'player-rankings'
    for g in gender:
        for m in m_format:
            for p in player_type:
                url = base_url + g + '/player-rankings/' + m + '/' + p
                collection, data = get_formatted_data(url, g, m, tp,p)
                collections[collection] = data
                #save_to_csv(data, collection.replace('.', '_'))
    return collections

if __name__ == "__main__":
    pprint.pprint(generate_data())
    # pprint.pprint(generate_player_data())