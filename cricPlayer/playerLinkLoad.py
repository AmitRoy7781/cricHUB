from cricMongoDB.database import db
from bs4 import BeautifulSoup
import requests

url = "https://m.cricbuzz.com/cricket-search/player/A/1024"
res = requests.get(url)
soup = BeautifulSoup(res.text, 'lxml')
outputFileName = open("output.txt", 'a+')
# outputFileName.write("\n")

temp = soup.find_all("a",{"class":"cb-list-item"})

for i in range(0,1024):
    url = "https://m.cricbuzz.com/cricket-search/player/A/" + str(i+1)
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'lxml')

    temp = soup.find_all("a", {"class": "cb-list-item"})
    print(i)

    for i in temp:
        x = i.text + "|https://www.cricbuzz.com" + i["href"]
        x = x.strip()
        #outputFileName.write(x+"\n")
