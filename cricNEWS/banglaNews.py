import requests
from bs4 import BeautifulSoup
from flask import render_template, request, Blueprint

app = Blueprint('banglanews', __name__)

@app.route('/banglanews/')
def show_news(page_no=None):
    url = "https://www.prothomalo.com/sports/article/?tags=95&page="

    if page_no ==None:
        page_no = "1"
        url += "1"
    else:
        url += page_no

    res = requests.get(url)
    soup = BeautifulSoup(res.text,'lxml')

    #print(soup.prettify())

    temp1 = soup.find_all('span',{'class':'title'})
    temp2 = soup.find_all('div',{'class':'info has_ai'})
    temp3 = soup.find_all('span',{'class':'time aitm'})
    temp4 = soup.find_all('div',{'class':"image"})
    temp5 = soup.find_all('a',{'class':"link_overlay"})

    newsHeadline = []
    newsDetails = []
    newsTime = []
    newsImage = []
    newsHref = []

    for i in range(20):
        newsHeadline.append(str(temp1[i].text).strip())

        x = BeautifulSoup(str(temp2[i]), 'lxml').find("div",{"class":"summery"})
        if x !=None:
            newsDetails.append(x.text)
        else:
            newsDetails.append("")
        newsTime.append(str(temp3[i].text).strip())
        newsImage.append("https:" +  BeautifulSoup(str(temp4[i]),'lxml').find("img")["src"])
        newsHref.append("https://www.prothomalo.com" + BeautifulSoup(str(temp5[i]),'lxml').find("a")["href"])

        # print(newsHeadline[i])
        # print(newsDetails[i])
        # print(newsTime[i])
        # print(newsImage[i])
        # print(newsHref[i])
        #
        # print()

    data = []
    for i in range(20):
        temp = {}
        temp["news_headline"] = newsHeadline[i]
        temp["news_details"] = newsDetails[i]
        temp["news_time"] = newsTime[i]
        temp["news_title"] = newsHeadline[i]
        temp["news_img"] = newsImage[i]
        temp["news_img_title"] = newsHeadline[i]
        temp["news_href"] = newsHref[i]
        data.append(temp)

    return render_template("news/banglaNews.html", news_data=data, page_no=page_no)


@app.route("/banglanews/more_news",methods=['POST', 'GET'])
def more_news():
    page_no = int(request.form["more_news"])
    print(page_no)
    return show_news(str(page_no+1))


@app.route("/banglanews/detail_news",methods=['POST', 'GET'])
def detail_news():
    url = request.form["detail_news"]

    res = requests.get(url)
    soup = BeautifulSoup(res.text,'lxml')
    original = soup.find('div',{'itemprop':'articleBody'})

    newsHeader = ""
    newsDetails =  ""
    newsImg = ""
    newsImgCap = ""
    newsPar = []

    #print(soup.prettify())

    newsHeader = soup.find('h1',{'class':"title mb10"}).text
    #print(newsHeader)
    newsDetails = BeautifulSoup(str(original), 'lxml').find_all('div')[1].text
    #print(newsDetails)
    newsImg = BeautifulSoup(str(original), 'lxml').find('img')["src"]
    #print(newsImg)
    newsImgCap = BeautifulSoup(str(original), 'lxml').find('img')["alt"]
    #print(newsImgCap)
    temp = BeautifulSoup(str(original), 'lxml').find_all('p')
    for i in range(len(temp)):
        if i==0:

            continue
        newsPar.append(temp[i].text)
        #print(temp[i].text)
    return render_template("news/bangladetail_news.html"
                           ,newsHeader=newsHeader
                           ,newsDetails=newsDetails
                           ,newsImg=newsImg
                           ,newsImgCap=newsImgCap
                           ,newsPar=newsPar)
