from bs4 import BeautifulSoup
import requests

def SCORE(url):
    try:
        res = requests.get(url)
        ret = ""
        soup = BeautifulSoup(res.text,'lxml')
        a = soup.find_all('div',{'class':"cb-min-tm"})

        for i in a:
            ret = ret + str(i.text) +"\n"
        a = soup.find('div', {'class': "cb-min-stts"})
        ret = ret + str(a.text)
        #print(ret)

    except:
        ret = ""

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


        cnt = 0
        for i in a:
            data[cnt] = str(i.contents[0]).split('"')[5]
            scoreurl  =  'https://www.cricbuzz.com' + str(i.contents[0]).split('"')[1]
            #print(scoreurl)
            #print(SCORE(scoreurl))
            print()
            print()
            score[cnt]= SCORE(scoreurl)
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

