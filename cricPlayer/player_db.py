import requests
from bs4 import BeautifulSoup


class Singleton:

    file = open("/home/amit-roy/SDP Resources/cricHUB/cricPlayer/player_data.txt", "r")
    outputfile = open("/home/amit-roy/SDP Resources/cricHUB/cricPlayer/player_full_data", "a+")
    data = file.read()
    file_data = data
    file_data = file_data.lower()
    file_data = file_data.splitlines()


class Instance:

    def player_database():

        for i in range(449, len(Singleton.file_data)):
            x = Singleton.file_data[i].split("|")
            url = x[1]

        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'lxml')

        player = soup.find("div", {"id": "playerProfile"})
        soup = BeautifulSoup(str(player), 'lxml')

        x = soup.find("h1", {"itemprop": "name"})
        y = soup.find("img", {"class": "cb-plyr-thum-img"})
        z = soup.find("h3", {"class": "text-gray"})

        if x is not None and y is not None and z is not None:
            temp = {}
            temp["player_name"] = str(x.text).strip()
            temp["player_img"] = str(y["src"]).strip()
            temp["player_country"] = str(z.text).strip()
            temp["player_url"] = str(url).strip()

            # posts = db.players
            # posts.insert_one(temp)
            Singleton.outputfile.write(temp["player_name"] + "|" + temp["player_img"] + "|"
                                       + temp["player_country"] + "|" + url + "\n")
            print(i + 1)
