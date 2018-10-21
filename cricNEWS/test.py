from bs4 import BeautifulSoup
import requests

def get_News():
    url = 'https://www.cricbuzz.com/cricket-news'
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'lxml')
    #print(soup.prettify())
    news_context = soup.find_all('div', {'class': 'cb-nws-time'})
    news_headline = soup.find_all('a',{'class':'cb-nws-hdln-ancr'})
    news_details = soup.find_all('div', {'class': 'cb-nws-intr'})
    news_time =  soup.find_all('span', {'class': 'cb-nws-time'})

    temp = soup.find_all('img',{'class':'cb-lst-img'})
    news_img = []

    for i in temp:
        soup = BeautifulSoup(str(i), 'lxml')
        news_img.append(soup.find('img')['src'])

    # print(news_img)

    data = []
    for i in range(len(news_context)):
        temp = {}
        temp["news_context"] = news_context[i].text
        temp["news_headline"] = news_headline[i].text
        temp["news_details"] = news_details[i].text
        temp["news_time"] = news_time[i].text
        temp["news_img"] = news_img[i]
        print(temp["news_img"])
        data.append(temp)

    #print(data)

if __name__ == '__main__':
    get_News()
