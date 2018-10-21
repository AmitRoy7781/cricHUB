from flask import render_template, request, redirect, session, Blueprint
from bs4 import BeautifulSoup
import requests


app = Blueprint('news', __name__)

@app.route('/news/')
def show_news():
    if 'username' not in session.keys():
        return redirect('/auth/signin')

    url = 'https://www.cricbuzz.com/cricket-news'
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'lxml')
    # print(soup.prettify())
    news_context = soup.find_all('div', {'class': 'cb-nws-time'})
    news_headline = soup.find_all('a', {'class': 'cb-nws-hdln-ancr'})
    news_details = soup.find_all('div', {'class': 'cb-nws-intr'})
    news_time = soup.find_all('span', {'class': 'cb-nws-time'})

    temp = soup.find_all('img', {'class': 'cb-lst-img'})
    news_title = []
    news_img = []
    news_img_title = []
    news_href = []

    for i in news_headline:
        soup = BeautifulSoup(str(i), 'lxml')
        news_title.append(soup.find('a')['title'])
        news_href.append(soup.find('a')['href'])

    for i in temp:
        soup = BeautifulSoup(str(i), 'lxml')
        news_img.append(soup.find('img')['src'])
        news_img_title.append(soup.find('img')['title'])


    # print(news_img)

    data = []
    for i in range(len(news_context)):
        temp = {}
        temp["news_context"] = news_context[i].text
        temp["news_headline"] = news_headline[i].text
        temp["news_details"] = news_details[i].text
        temp["news_time"] = news_time[i].text
        temp["news_title"] = news_title[i]
        temp["news_img"] = news_img[i]
        temp["news_img_title"] = news_img_title[i]
        temp["news_href"] = news_href[i]
        data.append(temp)

    #print(data)
    #     print(news_context[i].text)
    #     print(news_headline[i].text)
    #     print(news_details[i].text)
    #     print(news_time[i].text)
    #     print()
    #     print("--------------------------------------------------------")

    return render_template("news/news.html", news_data=data)



def get_News():
    url = 'https://www.cricbuzz.com/cricket-news'
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'lxml')
    #print(soup.prettify())
    news_context = soup.find_all('div', {'class': 'cb-nws-time'})
    news_headline = soup.find_all('a',{'class':'cb-nws-hdln-ancr'})
    news_details = soup.find_all('div', {'class': 'cb-nws-intr'})
    news_time =  soup.find_all('span', {'class': 'cb-nws-time'})

    temp = soup.find_all('img', {'class': 'cb-lst-img'})
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
        data.append(temp)

    print(data)

    #     print(news_context[i].text)
    #     print(news_headline[i].text)
    #     print(news_details[i].text)
    #     print(news_time[i].text)
    #     print()
    #     print("--------------------------------------------------------")

    return render_template("news/news.html", news_data=data)