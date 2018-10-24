from flask import render_template, request, redirect, session, Blueprint
from bs4 import BeautifulSoup
import requests

app = Blueprint('livescore', __name__)

def SCORE(url):
    try:
        res = requests.get(url)
        ret = ""
        soup = BeautifulSoup(res.text,'lxml')
        a = soup.find_all('div',{'class':"cb-scrs-wrp"})

        for i in a:
            ret = ret + str(i.text) +"\n"
        #a = soup.find('div', {'class': "cb-min-stts",'class': "cb-text-inprogress"})
        #ret = ret + str(a.text)
        #print(ret)

    except:
        ret = ""

    ret.strip();
    ret = ret[1:]
    return ret;


def URL():

    url = 'https://www.cricbuzz.com/cricket-match/live-scores'
    return url


def SOUP(url):
    try:
        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'lxml')

        data = {}
        score = {}
        a = soup.find_all('div',{'class':'cb-mtch-all'})
        #print(a)

        cnt = 0
        for i in a:
            print(i)
            data[cnt] = str(i.contents[0]).split('"')[5]
            scoreurl  =  'https://www.cricbuzz.com' + str(i.contents[0]).split('"')[1]
            score[cnt]= SCORE(scoreurl)

            #print(scoreurl)
            #print(SCORE(scoreurl))

            print()
            print()
            print(data[cnt])
            print(score[cnt])
            print()
            print()
            print("-----------------------------------------------")
            cnt = cnt + 1


        return data,score
    except:
        print("Sorry couldn't find the data right now")





def livescore():
    """
    Diplays of current matches, scores and results

    """

    url= URL()
    SOUP(url)


if __name__ == '__main__':
    livescore()

