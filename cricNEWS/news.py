from bs4 import BeautifulSoup
import requests



def URL():
    url = 'https://www.cricbuzz.com'
    return url


def SOUP(url):
    try:
        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'lxml')

        big = soup.find_all('div', {'class': 'big-crd-main'})  # most popular news
        small = soup.find_all('div', {'class': 'sml-crd-main'})

        # print(big)
        for i in big:
            #print(i)
            soup = BeautifulSoup(str(i), 'lxml')

            context = str(soup.find('div', {'class': 'crd-cntxt'}).text)
            headline = str(soup.find('h2', {'class': 'big-crd-hdln'}).text)
            description = str(soup.find('div', {'class': 'cb-nws-intr'}).text)
            link = "www.cricbuzz.com" + soup.find('a')['href']




            related_item_html = soup.find_all('div', {'class': 'big-crd-reltd-itm'})
            related_item = {}
            related_link = {}
            cnt = 0

            for j in related_item_html:
                soup = BeautifulSoup(str(j), 'lxml')
                related_item[cnt] = str(soup.find('a', {'class': 'big-crd-rltd-txt'}).text)
                related_link[cnt] = "www.cricbuzz.com" + soup.find('a')['href']
                cnt = cnt + 1

            print(context)
            print(headline)
            print(description)
            print(link)
            print()
            for p in related_item:
                print(related_item[p])
                print(related_link[p])
            print()
            print("--------------------------------------------------------------------")
            print()




        # print(small)
        for i in small:
            #print(i)
            soup = BeautifulSoup(str(i), 'lxml')


            context = soup.find('div', {'class': 'crd-cntxt'})
            if context is None:
                continue

            context  = context.text
            headline = soup.find('h3',{'class':'sml-crd-hdln'}).text
            newstime = soup.find('div',{'class':'sml-crd-subtxt'}).text
            description  = soup.find('div',{'class':'cb-nws-intr'}).text

            related_item_html = soup.find_all('div', {'class': 'big-crd-reltd-itm'})
            related_item = {}
            cnt = 0

            for j in related_item_html:
                soup = BeautifulSoup(str(j), 'lxml')
                related_item[cnt] = str(soup.find('a', {'class': 'big-crd-rltd-txt'}).text)
                cnt = cnt + 1

            print(context)
            print(headline)
            print(newstime)
            print(description)
            for p in related_item:
                 print(related_item[p])
            print()
            print()



    except:
        print("Sorry couldn't find the data right now")


def news():
    """
    Diplays latest news of cricket

    """

    url = URL()
    SOUP(url)


if __name__ == '__main__':
    news()
