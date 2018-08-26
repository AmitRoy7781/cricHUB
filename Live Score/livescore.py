from bs4 import BeautifulSoup
import requests




def URL():

    url = 'https://www.cricbuzz.com/cricket-match/live-scores'
    return url


def SOUP(url):
    try:
        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'lxml')

        data = {}
        a = soup.find_all('div',{'class':'cb-mtch-all'})


        cnt = 0
        for i in a:
            data[cnt] = str(i.contents[0]).split('"')[5]
            cnt = cnt + 1


        return data
    except:
        print("Sorry couldn't find the data right now")



def Print(data):


    for i in data:
        print(data[i])
        print()


def livescore():
    """
    Diplays of current matches and results

    Args : None (No arguements are passed into this function)

    Returns : None (No value is returned by this function)

    """

    url= URL()
    data = SOUP(url)
    Print(data)


if __name__ == '__main__':
    #while True:
        livescore()

