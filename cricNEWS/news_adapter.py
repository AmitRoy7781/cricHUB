import abc

import requests
from bs4 import BeautifulSoup
from flask import render_template, request, Blueprint


app = Blueprint('news', __name__)


class Target(metaclass=abc.ABCMeta):
    """
    Define the domain-specific interface that Client uses.
    """

    def __init__(self):
        self._adaptee = Adaptee()

    @abc.abstractmethod
    def news_headline(self):
        pass

    @abc.abstractmethod
    def more_news(self):
        pass

    @abc.abstractmethod
    def news_details(self):
        pass


class Adapter(Target):
    """
    Adapt the interface of Adaptee to the Target interface.
    """

    def news_headline(self):
        self._adaptee.get_news()

    def more_news(self):
        self._adaptee.get_more()

    def news_details(self):
        self._adaptee.get_details()


class Adaptee:
    """
    Define an existing interface that needs adapting.
    """

    @app.route('/news/')
    def get_news(page_no=None):
        url = 'https://www.cricbuzz.com/cricket-news'

        if page_no != None:
            url = url + '/' + page_no
        else:
            page_no = '1'

        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'lxml')
        news_context = soup.find_all('div', {'class': 'cb-nws-time'})
        news_headline = soup.find_all('a', {'class': 'cb-nws-hdln-ancr'})
        news_details = soup.find_all('div', {'class': 'cb-nws-intr'})
        news_time = soup.find_all('span', {'class': 'cb-nws-time'})

        temp = soup.find_all('div', {'itemprop': 'image'})
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

        return render_template("news/news.html", news_data=data, page_no=page_no)



    @app.route("/news/more_news", methods=['POST', 'GET'])
    def get_more(self=None):
        page_no = int(request.form["more_news"])
        return Adaptee.get_news(str(page_no + 1))



    @app.route("/news/detail_news", methods=['POST', 'GET'])
    def get_details(self=None):

        news_topic = ""
        news_headline = ""
        news_author = ""
        news_time = ""
        news_img = ""
        news_img_caption = ""
        news_fb_href = ""
        news_twt_href = ""

        url = request.form["detail_news"]
        url = "https://" + url

        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'lxml')

        x = soup.find_all('span', {'class': 'cb-text-gray'})
        if x is not None and len(x) >= 1:
            news_topic = x[0].text

        x = soup.find_all('h1', {'itemprop': 'headline'})
        if x is not None and len(x) >= 1:
            news_headline = x[0].text

        x = soup.find_all('span', {'itemprop': 'author'})
        if x is not None and len(x) >= 1:
            news_author = x[0].text

        x = soup.find_all('time', {'itemprop': 'dateModified'})
        if x is not None and len(x) >= 1:
            news_time = x[0].text

        x = soup.find_all('img', {'itemprop': 'contentUrl'})
        y = soup.find_all('img', {'class': 'playerPoster'})

        if x is not None and len(x) >= 1:
            news_img = x[0]["src"]
        elif y is not None and len(y) >= 1:
            news_img = y[0]["src"]

        x = soup.find_all('div', {'class': 'cb-img-cptn'})
        if x is not None and len(x) >= 1:
            news_img_caption = x[0].text

        all_paras = soup.find_all('p')
        news_para = []
        for temp in all_paras:
            if temp.text != "" and temp.text != "{{suggest.tag}}" and temp.text != "Search for “”":
                news_para.append(temp.text)

        x = soup.find_all('a', {'class': 'cb-social-ancr-fb'})
        if x is not None and len(x) >= 1:
            news_fb_href = x[0]["href"]

        x = soup.find_all('a', {'class': 'cb-social-ancr-twt'})
        if x is not None and len(x) >= 1:
            news_twt_href = x[0]["href"]

        return render_template('/news/detail_news.html',
                               news_topic=news_topic,
                               news_headline=news_headline,
                               news_author=news_author,
                               news_time=news_time,
                               news_img=news_img,
                               news_img_caption=news_img_caption,
                               news_para=news_para,
                               news_fb_href=news_fb_href,
                               news_twt_href=news_twt_href)



news = Adapter()

def show_news():
    news.news_headline()


def more_news():
    news.more_news()


def details_news():
    news.news_details()