from bs4 import BeautifulSoup
import requests


page = requests.get("https://www.cricbuzz.com/cricket-stats/icc-rankings/batsmen-rankings")
soup = BeautifulSoup(page.text, "lxml")

big = soup.find_all('div', {'class': 'cb-rank-plyr'}) # most popular news
for i in big:
    print(str(i.text))
print(big)
