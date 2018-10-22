from flask import render_template, request, redirect, session, Blueprint, json
from bs4 import BeautifulSoup
import requests


app = Blueprint('news', __name__)

@app.route('/news/')
def show_news(page_no=None):
    if 'username' not in session.keys():
        return redirect('/auth/signin')

    url = 'https://www.cricbuzz.com/cricket-news'

    if page_no!=None:
        url = url + '/' + page_no
    else:
        page_no = '1'

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

    # print(page_no)
    return render_template("news/news.html", news_data=data,page_no= page_no)



@app.route("/news/more_news",methods=['POST', 'GET'])
def more_news():
    if 'username' not in session.keys():
        return redirect('/auth/signin')
    # print(request.form["more_news"])
    page_no = int(request.form["more_news"])
    return show_news(str(page_no+1))


@app.route("/news/detail_news",methods=['POST', 'GET'])
def detail_news():
    if 'username' not in session.keys():
        return redirect('/auth/signin')

    url = request.form["detail_news"]
    url = "https://" + url

    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'lxml')
    news_topic = soup.find_all('span', {'class': 'cb-text-gray'})[0].text
    news_headline = soup.find_all('h1', {'itemprop': 'headline'})[0].text
    news_author = soup.find_all('span', {'itemprop': 'author'})[0].text
    news_time = soup.find_all('time', {'itemprop': 'dateModified'})[0].text
    news_img = soup.find_all('img', {'itemprop': 'contentUrl'})[0]["src"]
    news_img_caption = soup.find_all('div', {'class': 'cb-img-cptn'})[0].text

    all_paras = soup.find_all('p')
    news_para = []
    for temp in all_paras:
        if temp.text != "" and temp.text != "{{suggest.tag}}" and temp.text != "Search for “”":
            news_para.append(temp.text)

    news_fb_href = soup.find_all('a', {'class': 'cb-social-ancr-fb'})[0]["href"]
    news_twt_href = soup.find_all('a', {'class': 'cb-social-ancr-twt'})[0]["href"]

    return render_template('/news/detail_news.html',
                           news_topic=news_topic,
                           news_headline=news_headline,
                           news_author=news_author,
                           news_time=news_time,
                           news_img=news_img,
                           news_img_caption=news_img_caption,
                           news_para = news_para,
                           news_fb_href=news_fb_href,
                           news_twt_href=news_twt_href)