from cricMongoDB.database import db
from bs4 import BeautifulSoup
import requests

url = "https://m.cricbuzz.com/cricket-search/player/A/1024"
res = requests.get(url)
soup = BeautifulSoup(res.text, 'lxml')
outputFileName = open("output.txt", 'a+')
# outputFileName.write("\n")

temp = soup.find_all("a",{"class":"cb-list-item"})

for i in range(869,1025):
    url = "https://m.cricbuzz.com/cricket-search/player/A/" + str(i+1)
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'lxml')


    temp1 = soup.find_all("a", {"class": "cb-list-item"})
    temp2 = soup.find_all("img")

    temp2 = temp2[2:]
    #print(temp1)

    print(i)
    for i in range(len(temp1)):
        name = str(temp1[i].text).strip()
        href = str(temp1[i]["href"]).strip()
        img  = str(temp2[i]["src"]).strip()

        #print(name,href,img)
        outputFileName.write(name+ "|" + href + "|" + img + "\n")
