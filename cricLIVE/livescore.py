from flask import render_template, request, redirect, session, Blueprint
from bs4 import BeautifulSoup
import requests

app = Blueprint('livescore', __name__)


@app.route('/live-score/')
def score():
	
    if 'username' not in session.keys():
        return redirect('/auth/signin')

    url = 'https://www.cricbuzz.com/cricket-match/live-scores'
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'lxml')

    # print(soup.prettify())

    match_data = []
    a = soup.find_all('div', {'class': 'cb-lv-main'})
    # print(a)

    for i in a:

        match_header = ""
        match_name = ""
        match_no = ""
        match_venue = ""
        match_status = ""
        match_href = ""
        team1 = ""
        team2 = ""
        team1score = ""
        team2score = ""

        x = BeautifulSoup(str(i), "lxml").find("h2", {"class": "cb-lv-scr-mtch-hdr"})
        if x is not None:
            match_header = x.text

        x = BeautifulSoup(str(i), "lxml").find("h3", {"class": "cb-lv-scr-mtch-hdr"})
        if x is not None:
            match_name = x.text

        x = BeautifulSoup(str(i), "lxml").find_all("span", {"class": "text-gray"})
        if x is not None and len(x) >= 1:
            match_no = x[0].text
            match_no = match_no.strip()

        x = BeautifulSoup(str(i), "lxml").find_all("span", {"class": "text-gray"})
        if x is not None and len(x) >= 2:
            match_venue = x[1].text
            match_venue = match_venue.strip()

        x = BeautifulSoup(str(i), "lxml").find_all("span", {"class": "text-bold"})

        if x is not None and len(x) >= 1:
            team1 = x[0].text
        if x is not None and len(x) >= 2:
            team2 = x[1].text

        x = BeautifulSoup(str(i), "lxml").find("div", {"class": "cb-lv-scrs-col"})

        if x is not None:
            score = x.text
            score = score.split("•")
            team1score = str(score[0][:len(score[0]) - 2]).strip()
            team2score = str(score[1][2:]).strip()

        x = BeautifulSoup(str(i), "lxml").find("div", {"class": "cb-text-live"})
        y = BeautifulSoup(str(i), "lxml").find("div", {"class": "cb-text-complete"})
        if x is not None:
            match_status = x.text
        elif y is not None:
            match_status = y.text


        x = BeautifulSoup(str(i), "lxml").find("a", {"class": "text-hvr-underline text-bold"})
        if x is not None:
            match_href = "https://www.cricbuzz.com" + x["href"]

        temp = {}
        temp["match_header"] = match_header
        temp["match_name"] = match_name
        temp["match_no"] = match_no
        temp["match_venue"] = match_venue
        temp["match_status"] = match_status
        temp["match_href"] = match_href
        temp["team1"] = team1
        temp["team2"] = team2
        temp["team1score"] = team1score
        temp["team2score"] = team2score
        match_data.append(temp)

        # print(match_header)
        # print(match_name)
        # print(match_no)
        # print(match_venue)
        # print(team1)
        # print(team2)
        # print(team1score)
        # print(team2score)
        # print("-----------------------------------------------")

    return render_template('livescore/score.html',match_data=match_data)
