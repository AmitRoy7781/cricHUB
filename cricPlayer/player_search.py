from flask import render_template
from bs4 import BeautifulSoup
import requests,re



PRINT_ON = False


def get_data(url):

    player_name = "--"
    player_img = "--"
    player_country = "--"

    player_born = "--"
    player_birth_place = "--"
    player_height = "--"

    player_role = "--"
    player_batting_style = "--"
    player_bowling_style = "--"

    player_test_batting_rank = "--"
    player_odi_batting_rank = "--"
    player_t20_batting_rank = "--"

    player_test_bowling_rank = "--"
    player_odi_bowling_rank = "--"
    player_t20_bowling_rank = "--"

    player_team = "--"

    player_test_batting_m = "--"
    player_test_batting_inn = "--"
    player_test_no = "--"
    player_test_batting_runs = "--"
    player_test_hs = "--"
    player_test_batting_avg = "--"
    player_test_bf = "--"
    player_test_batting_sr = "--"
    player_test_100 = "--"
    player_test_200 = "--"
    player_test_50 = "--"
    player_test_4s = "--"
    player_test_6s = "--"

    player_test_bowling_m = "--"
    player_test_bowling_inn = "--"
    player_test_b = "--"
    player_test_bowling_runs = "--"
    player_test_wkts = "--"
    player_test_bbi = "--"
    player_test_bbm = "--"
    player_test_econ = "--"
    player_test_bowling_avg = "--"
    player_test_bowling_sr = "--"
    player_test_5W = "--"
    player_test_10W = "--"

    player_odi_batting_m = "--"
    player_odi_batting_inn = "--"
    player_odi_no = "--"
    player_odi_batting_runs = "--"
    player_odi_hs = "--"
    player_odi_batting_avg = "--"
    player_odi_bf = "--"
    player_odi_batting_sr = "--"
    player_odi_100 = "--"
    player_odi_200 = "--"
    player_odi_50 = "--"
    player_odi_4s = "--"
    player_odi_6s = "--"

    player_odi_bowling_m = "--"
    player_odi_bowling_inn = "--"
    player_odi_b = "--"
    player_odi_bowling_runs = "--"
    player_odi_wkts = "--"
    player_odi_bbi = "--"
    player_odi_bbm = "--"
    player_odi_econ = "--"
    player_odi_bowling_avg = "--"
    player_odi_bowling_sr = "--"
    player_odi_5W = "--"
    player_odi_10W = "--"

    player_t20_batting_m = "--"
    player_t20_batting_inn = "--"
    player_t20_no = "--"
    player_t20_batting_runs = "--"
    player_t20_hs = "--"
    player_t20_batting_avg = "--"
    player_t20_bf = "--"
    player_t20_batting_sr = "--"
    player_t20_100 = "--"
    player_t20_200 = "--"
    player_t20_50 = "--"
    player_t20_4s = "--"
    player_t20_6s = "--"

    player_t20_bowling_m = "--"
    player_t20_bowling_inn = "--"
    player_t20_b = "--"
    player_t20_bowling_runs = "--"
    player_t20_wkts = "--"
    player_t20_bbi = "--"
    player_t20_bbm = "--"
    player_t20_econ = "--"
    player_t20_bowling_avg = "--"
    player_t20_bowling_sr = "--"
    player_t20_5W = "--"
    player_t20_10W = "--"

    player_ipl_batting_m = "--"
    player_ipl_batting_inn = "--"
    player_ipl_no = "--"
    player_ipl_batting_runs = "--"
    player_ipl_hs = "--"
    player_ipl_batting_avg = "--"
    player_ipl_bf = "--"
    player_ipl_batting_sr = "--"
    player_ipl_100 = "--"
    player_ipl_200 = "--"
    player_ipl_50 = "--"
    player_ipl_4s = "--"
    player_ipl_6s = "--"

    player_ipl_bowling_m = "--"
    player_ipl_bowling_inn = "--"
    player_ipl_b = "--"
    player_ipl_bowling_runs = "--"
    player_ipl_wkts = "--"
    player_ipl_bbi = "--"
    player_ipl_bbm = "--"
    player_ipl_econ = "--"
    player_ipl_bowling_avg = "--"
    player_ipl_bowling_sr = "--"
    player_ipl_5W = "--"
    player_ipl_10W = "--"

    player_test_debut = "--"
    player_last_test = "--"

    player_odi_debut = "--"
    player_last_odi = "--"

    player_t20_debut = "--"
    player_last_t20 = "--"

    player_ipl_debut = "--"
    player_last_ipl = "--"

    player_bio = "--"



    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'lxml')

    player = soup.find("div",{"id":"playerProfile"})
    soup = BeautifulSoup(str(player), 'lxml')


    player_name = soup.find("h1",{"itemprop":"name"}).text
    player_img = soup.find("img",{"class":"cb-plyr-thum-img"})["src"]
    player_country = soup.find("h3",{"class":"text-gray"}).text

    player_general_info = soup.find("div",{"class":"cb-hm-rght"})


    temp = BeautifulSoup(str(player_general_info),'lxml').find_all("div")



    for i in range(2,len(temp),1):
        x = temp[i]
        #print(x.text)
        if x.text=="Born":
            player_born = temp[i+1].text
        if x.text=="Birth Place":
            player_birth_place=temp[i+1].text
        if x.text == "Height":
            player_height = temp[i+1].text
        if x.text == "Role":
            player_role = temp[i+1].text
        if x.text == "Batting Style":
            player_batting_style = temp[i+1].text
        if x.text == "Bowling Style":
            player_bowling_style = temp[i+1].text

        if x.text == "Batting":
            player_test_batting_rank = temp[i+1].text
            player_odi_batting_rank = temp[i+2].text
            player_t20_batting_rank = temp[i+3].text
        if x.text == "Bowling":
            player_test_bowling_rank = temp[i+1].text
            player_odi_bowling_rank = temp[i+2].text
            player_t20_bowling_rank = temp[i+3].text
        if x.text == "Teams":
            player_team = temp[i+1].text


    tables = soup.find_all("div",{"class":"cb-plyr-tbl"})



    if len(tables)>=1:
        Batting = BeautifulSoup(str(tables[0]),"lxml").find_all("tr")

        for i in range(1,len(Batting)):
            row = BeautifulSoup(str(Batting[i]), "lxml").find_all("td")

            for j in range(len(row)):
                if row[j].text == "Test" and (j+13)<len(row):
                    player_test_batting_m = row[j+1].text
                    player_test_batting_inn = row[j+2].text
                    player_test_no = row[j+3].text
                    player_test_batting_runs = row[j+4].text
                    player_test_hs = row[j+5].text
                    player_test_batting_avg = row[j+6].text
                    player_test_bf = row[j+7].text
                    player_test_batting_sr = row[j+8].text
                    player_test_100 = row[j+9].text
                    player_test_200 = row[j+10].text
                    player_test_50 = row[j+11].text
                    player_test_4s = row[j+12].text
                    player_test_6s = row[j+13].text

                elif row[j].text == "ODI" and (j+13)<len(row):

                    player_odi_batting_m = row[j + 1].text
                    player_odi_batting_inn = row[j + 2].text
                    player_odi_no = row[j + 3].text
                    player_odi_batting_runs = row[j + 4].text
                    player_odi_hs = row[j + 5].text
                    player_odi_batting_avg = row[j + 6].text
                    player_odi_bf = row[j + 7].text
                    player_odi_batting_sr = row[j + 8].text
                    player_odi_100 = row[j + 9].text
                    player_odi_200 = row[j + 10].text
                    player_odi_50 = row[j + 11].text
                    player_odi_4s = row[j + 12].text
                    player_odi_6s = row[j + 13].text

                elif row[j].text == "T20I" and (j+13)<len(row):
                    player_t20_batting_m = row[j + 1].text
                    player_t20_batting_inn = row[j + 2].text
                    player_t20_no = row[j + 3].text
                    player_t20_batting_runs = row[j + 4].text
                    player_t20_hs = row[j + 5].text
                    player_t20_batting_avg = row[j + 6].text
                    player_t20_bf = row[j + 7].text
                    player_t20_batting_sr = row[j + 8].text
                    player_t20_100 = row[j + 9].text
                    player_t20_200 = row[j + 10].text
                    player_t20_50 = row[j + 11].text
                    player_t20_4s = row[j + 12].text
                    player_t20_6s = row[j + 13].text
                elif row[j].text == "IPL" and (j+13)<len(row):
                    player_ipl_batting_m = row[j + 1].text
                    player_ipl_batting_inn = row[j + 2].text
                    player_ipl_no = row[j + 3].text
                    player_ipl_batting_runs = row[j + 4].text
                    player_ipl_hs = row[j + 5].text
                    player_ipl_batting_avg = row[j + 6].text
                    player_ipl_bf = row[j + 7].text
                    player_ipl_batting_sr = row[j + 8].text
                    player_ipl_100 = row[j + 9].text
                    player_ipl_200 = row[j + 10].text
                    player_ipl_50 = row[j + 11].text
                    player_ipl_4s = row[j + 12].text
                    player_ipl_6s = row[j + 13].text

    if len(tables)>=2:
        Bowling = BeautifulSoup(str(tables[1]),"lxml").find_all("tr")

        for i in range(1, len(Bowling)):
            row = BeautifulSoup(str(Bowling[i]), "lxml").find_all("td")
            for j in range(len(row)):
                if row[j].text == "Test" and (j+12)<len(row):
                    player_test_bowling_m = row[j + 1].text
                    player_test_bowling_inn = row[j + 2].text
                    player_test_b = row[j + 3].text
                    player_test_bowling_runs = row[j + 4].text
                    player_test_wkts = row[j + 5].text
                    player_test_bbi = row[j + 6].text
                    player_test_bbm = row[j + 7].text
                    player_test_econ = row[j + 8].text
                    player_test_bowling_avg = row[j + 9].text
                    player_test_bowling_sr = row[j + 10].text
                    player_test_5W = row[j + 11].text
                    player_test_10W = row[j + 12].text

                elif row[j].text == "ODI" and (j+12)<len(row):

                    player_odi_bowling_m = row[j + 1].text
                    player_odi_bowling_inn = row[j + 2].text
                    player_odi_b = row[j + 3].text
                    player_odi_bowling_runs = row[j + 4].text
                    player_odi_wkts = row[j + 5].text
                    player_odi_bbi = row[j + 6].text
                    player_odi_bbm = row[j + 7].text
                    player_odi_econ = row[j + 8].text
                    player_odi_bowling_avg = row[j + 9].text
                    player_odi_bowling_sr = row[j + 10].text
                    player_odi_5W = row[j + 11].text
                    player_odi_10W = row[j + 12].text

                elif row[j].text == "T20I" and (j+12)<len(row):
                    player_t20_bowling_m = row[j + 1].text
                    player_t20_bowling_inn = row[j + 2].text
                    player_t20_b = row[j + 3].text
                    player_t20_bowling_runs = row[j + 4].text
                    player_t20_wkts = row[j + 5].text
                    player_t20_bbi = row[j + 6].text
                    player_t20_bbm = row[j + 7].text
                    player_t20_econ = row[j + 8].text
                    player_t20_bowling_avg = row[j + 9].text
                    player_t20_bowling_sr = row[j + 10].text
                    player_t20_5W = row[j + 11].text
                    player_t20_10W = row[j + 12].text
                elif row[j].text == "IPL" and (j+12)<len(row):
                    player_ipl_bowling_m = row[j + 1].text
                    player_ipl_bowling_inn = row[j + 2].text
                    player_ipl_b = row[j + 3].text
                    player_ipl_bowling_runs = row[j + 4].text
                    player_ipl_wkts = row[j + 5].text
                    player_ipl_bbi = row[j + 6].text
                    player_ipl_bbm = row[j + 7].text
                    player_ipl_econ = row[j + 8].text
                    player_ipl_bowling_avg = row[j + 9].text
                    player_ipl_bowling_sr = row[j + 10].text
                    player_ipl_5W = row[j + 11].text
                    player_ipl_10W = row[j + 12].text

    #print_all()
    debut_last = soup.find_all("div",{"class":"cb-ftr-lst"})

    for i in range(len(debut_last)):
        x = debut_last[i]

        if x.text == "Test debut":
            player_test_debut = debut_last[i+1].text
        if x.text == "Last Test":
            player_last_test = debut_last[i+1].text

        if x.text == "ODI debut":
            player_odi_debut = debut_last[i+1].text
        if x.text == "Last ODI":
            player_last_odi = debut_last[i+1].text

        if x.text == "T20 debut":
            player_t20_debut = debut_last[i+1].text
        if x.text == "Last T20":
            player_last_t20 = debut_last[i+1].text

        if x.text == "IPL debut":
            player_ipl_debut = debut_last[i + 1].text
        if x.text == "Last IPL":
            player_last_ipl = debut_last[i + 1].text


    bio = soup.find_all("div",{"class":"cb-player-bio"})

    if(len(bio)>=2):
        bio = bio[1]
        bio = str(bio)
        bio = bio[45:len(bio)-6]
        bio = bio.strip()

        bio = bio.replace("<b>","<br/>")
        bio = bio.replace("</b>", "<br/>")
        bio = bio.replace("<i>", "<br/>")
        bio = bio.replace("</i>", "<br/>")
        bio = bio.split("<br/>")

        print(bio[len(bio)-1])
        player_bio = []

        for x in bio:
            if x.strip()!="":
                player_bio.append(x)


    #print_all()

    if PRINT_ON:
        print("Name: ", player_name)
        print("Image: https:" + player_img)
        print("Country: ", player_country)
        print()
        print("Born: ", player_born)
        print("Birth Place: ", player_birth_place)
        print("Height: ", player_height)
        print()
        print("Role: ", player_role)
        print("Batting Style: ", player_batting_style)
        print("Bowling Style: ", player_bowling_style)
        print()
        print("Player Test Batting Rank: ", player_test_batting_rank)
        print("Player ODI Batting Rank: ", player_odi_batting_rank)
        print("Player T20 Batting Rank: ", player_t20_batting_rank)
        print()
        print("Player Test Bowling Rank: ", player_test_bowling_rank)
        print("Player ODI Bowling Rank: ", player_odi_bowling_rank)
        print("Player T20 Bowling Rank: ", player_t20_bowling_rank)
        print()
        print("Player Test Matches: ", player_test_batting_m)
        print("Player Test Innings: ", player_test_batting_inn)
        print("Player Test Not Outs: ", player_test_no)
        print("Player Test Runs Scored: ", player_test_batting_runs)
        print("Player Test High Scores: ", player_test_hs)
        print("Player Test Avg: ", player_test_batting_avg)
        print("Player Test Ball Faced: ", player_test_bf)
        print("Player Test Batting Strike Rate: ", player_test_batting_sr)
        print("Player Test 100s: ", player_test_100)
        print("Player Test 200s: ", player_test_200)
        print("Player Test 50s: ", player_test_50)
        print("Player Test 4s: ", player_test_4s)
        print("Player Test 6s: ", player_test_6s)
        print()
        print("Player ODI Matches: ", player_odi_batting_m)
        print("Player ODI Innings: ", player_odi_batting_inn)
        print("Player ODI Not Outs: ", player_odi_no)
        print("Player ODI Runs Scored: ", player_odi_batting_runs)
        print("Player ODI High Scores: ", player_odi_hs)
        print("Player ODI Avg: ", player_odi_batting_avg)
        print("Player ODI Ball Faced: ", player_odi_bf)
        print("Player ODI Batting Strike Rate: ", player_odi_batting_sr)
        print("Player ODI 100s: ", player_odi_100)
        print("Player ODI 200s: ", player_odi_200)
        print("Player ODI 50s: ", player_odi_50)
        print("Player ODI 4s: ", player_odi_4s)
        print("Player ODI 6s: ", player_odi_6s)
        print()
        print("Player T20I Matches: ", player_t20_batting_m)
        print("Player T20I Innings: ", player_t20_batting_m)
        print("Player T20I Not Outs: ", player_t20_no)
        print("Player T20I Runs Scored: ", player_t20_batting_runs)
        print("Player T20I High Scores: ", player_t20_hs)
        print("Player T20I Avg: ", player_t20_batting_avg)
        print("Player T20I Ball Faced: ", player_t20_bf)
        print("Player T20I Batting Strike Rate: ", player_t20_batting_sr)
        print("Player T20I 100s: ", player_t20_100)
        print("Player T20I 200s: ", player_t20_200)
        print("Player T20I 50s: ", player_t20_50)
        print("Player T20I 4s: ", player_t20_4s)
        print("Player T20I 6s: ", player_t20_6s)
        print()
        print("Player IPL Matches: ", player_ipl_batting_m)
        print("Player IPL Innings: ", player_ipl_batting_inn)
        print("Player IPL Not Outs: ", player_ipl_no)
        print("Player IPL Runs Scored: ", player_ipl_batting_runs)
        print("Player IPL High Scores: ", player_ipl_hs)
        print("Player IPL Avg: ", player_ipl_batting_avg)
        print("Player IPL Ball Faced: ", player_ipl_bf)
        print("Player IPL Batting Strike Rate: ", player_ipl_batting_sr)
        print("Player IPL 100s: ", player_ipl_100)
        print("Player IPL 200s: ", player_ipl_200)
        print("Player IPL 50s: ", player_ipl_50)
        print("Player IPL 4s: ", player_ipl_4s)
        print("Player IPL 6s: ", player_ipl_6s)
        print()
        print("Player Test Bowling Matches: ", player_test_bowling_m)
        print("Player Test Bowling Innings: ", player_test_bowling_inn)
        print("Player Test Balls Bowled: ", player_test_b)
        print("Player Test Runs Scored: ", player_test_bowling_runs)
        print("Player Test Wkts: ", player_test_wkts)
        print("Player Test Best Bowling Figure Innings: ", player_test_bbi)
        print("Player Test Best Bowling Figure Match: ", player_test_bbm)
        print("Player Test Economy: ", player_test_econ)
        print("Player Test Bowling Avg: ", player_test_bowling_avg)
        print("Player Test Bowling SR: ", player_test_bowling_sr)
        print("Player Test 5W: ", player_test_5W)
        print("Player Test 10W: ", player_test_10W)
        print()
        print("Player ODI Bowling Matches: ", player_odi_bowling_m)
        print("Player ODI Bowling Innings: ", player_odi_bowling_inn)
        print("Player ODI Balls Bowled: ", player_odi_b)
        print("Player ODI Runs Scored: ", player_odi_bowling_runs)
        print("Player ODI Wkts: ", player_odi_wkts)
        print("Player ODI Best Bowling Figure Innings: ", player_odi_bbi)
        print("Player ODI Best Bowling Figure Match: ", player_odi_bbm)
        print("Player ODI Economy: ", player_odi_econ)
        print("Player ODI Bowling Avg: ", player_odi_bowling_avg)
        print("Player ODI Bowling SR: ", player_odi_bowling_sr)
        print("Player ODI 5W: ", player_odi_5W)
        print("Player ODI 10W: ", player_odi_10W)
        print()
        print("Player T20I Bowling Matches: ", player_t20_bowling_m)
        print("Player T20I Bowling Innings: ", player_t20_bowling_inn)
        print("Player T20I Balls Bowled: ", player_t20_b)
        print("Player T20I Runs Scored: ", player_t20_bowling_runs)
        print("Player T20I Wkts: ", player_t20_wkts)
        print("Player T20I Best Bowling Figure Innings: ", player_t20_bbi)
        print("Player T20I Best Bowling Figure Match: ", player_t20_bbm)
        print("Player T20I Economy: ", player_t20_econ)
        print("Player T20I Bowling Avg: ", player_t20_bowling_avg)
        print("Player T20I Bowling SR: ", player_t20_bowling_sr)
        print("Player T20I 5W: ", player_t20_5W)
        print("Player T20I 10W: ", player_t20_10W)
        print()
        print("Player IPL Bowling Matches: ", player_ipl_bowling_m)
        print("Player IPL Bowling Innings: ", player_ipl_bowling_inn)
        print("Player IPL Balls Bowled: ", player_ipl_b)
        print("Player IPL Runs Scored: ", player_ipl_bowling_runs)
        print("Player IPL Wkts: ", player_ipl_wkts)
        print("Player IPL Best Bowling Figure Innings: ", player_ipl_bbi)
        print("Player IPL Best Bowling Figure Match: ", player_ipl_bbm)
        print("Player IPL Economy: ", player_ipl_econ)
        print("Player IPL Bowling Avg: ", player_ipl_bowling_avg)
        print("Player IPL Bowling SR: ", player_ipl_bowling_sr)
        print("Player IPL 5W: ", player_ipl_5W)
        print("Player IPL 10W: ", player_ipl_10W)
        print()
        print("Test Debut: ", player_test_debut)
        print("Last Test: ", player_last_test)
        print()
        print("ODI Debut: ", player_odi_debut)
        print("Last ODI: ", player_last_odi)
        print()
        print("T20 Debut: ", player_t20_debut)
        print("Last T20: ", player_last_t20)
        print()
        print("IPL Debut: ", player_ipl_debut)
        print("Last IPL: ", player_last_ipl)
        print()
        print("BIO of Player: ", player_bio)
        print()

    return render_template("player/show_player.html",
    player_name=player_name,
    player_img = player_img,
    player_country = player_country,

    player_born = player_born,
    player_birth_place = player_birth_place,
    player_height = player_height,

    player_role = player_role,
    player_batting_style = player_batting_style,
    player_bowling_style = player_bowling_style,

    player_test_batting_rank = player_test_batting_rank,
    player_odi_batting_rank = player_odi_batting_rank,
    player_t20_batting_rank = player_t20_batting_rank,

    player_test_bowling_rank = player_test_bowling_rank,
    player_odi_bowling_rank = player_odi_bowling_rank,
    player_t20_bowling_rank = player_t20_bowling_rank,

    player_team = player_team,

    player_test_batting_m= player_test_batting_m,
    player_test_batting_inn = player_test_batting_inn,
    player_test_no = player_test_no,
    player_test_batting_runs = player_test_batting_runs,
    player_test_hs = player_test_hs,
    player_test_batting_avg = player_test_batting_avg,
    player_test_bf = player_test_bf,
    player_test_batting_sr = player_test_batting_sr,
    player_test_100 = player_test_100,
    player_test_200 = player_test_200,
    player_test_50 = player_test_50,
    player_test_4s = player_test_4s,
    player_test_6s = player_test_6s,

    player_odi_batting_m = player_odi_batting_m,
    player_odi_batting_inn = player_odi_batting_inn,
    player_odi_no = player_odi_no,
    player_odi_batting_runs = player_odi_batting_runs,
    player_odi_hs = player_odi_hs,
    player_odi_batting_avg = player_odi_batting_avg,
    player_odi_bf = player_odi_bf,
    player_odi_batting_sr = player_odi_batting_sr,
    player_odi_100 = player_odi_100,
    player_odi_200 = player_odi_200,
    player_odi_50 = player_odi_50,
    player_odi_4s = player_odi_4s,
    player_odi_6s = player_odi_6s,

    player_t20_batting_m=player_t20_batting_m,
    player_t20_batting_inn = player_t20_batting_inn,
    player_t20_no = player_t20_no,
    player_t20_batting_runs = player_t20_batting_runs,
    player_t20_hs = player_t20_hs,
    player_t20_batting_avg = player_t20_batting_avg,
    player_t20_bf = player_t20_bf,
    player_t20_batting_sr = player_t20_batting_sr,
    player_t20_100 = player_t20_100,
    player_t20_200 = player_t20_200,
    player_t20_50 = player_t20_50,
    player_t20_4s = player_t20_4s,
    player_t20_6s = player_t20_6s,

    player_ipl_batting_m=player_ipl_batting_m,
    player_ipl_batting_inn = player_ipl_batting_inn,
    player_ipl_no = player_ipl_no,
    player_ipl_batting_runs = player_ipl_batting_runs,
    player_ipl_hs = player_ipl_hs,
    player_ipl_batting_avg = player_ipl_batting_avg,
    player_ipl_bf = player_ipl_bf,
    player_ipl_batting_sr = player_ipl_batting_sr,
    player_ipl_100 = player_ipl_100,
    player_ipl_200 = player_ipl_200,
    player_ipl_50 = player_ipl_50,
    player_ipl_4s = player_ipl_4s,
    player_ipl_6s = player_ipl_6s,

    player_test_bowling_m=player_test_bowling_m,
    player_test_bowling_inn = player_test_bowling_inn,
    player_test_b = player_test_b,
    player_test_bowling_runs = player_test_bowling_runs,
    player_test_wkts = player_test_wkts,
    player_test_bbi = player_test_bbi,
    player_test_bbm = player_test_bbm,
    player_test_econ = player_test_econ,
    player_test_bowling_avg = player_test_bowling_avg,
    player_test_bowling_sr = player_test_bowling_sr,
    player_test_5W = player_test_5W,
    player_test_10W = player_test_10W,

    player_odi_bowling_m=player_odi_bowling_m,
    player_odi_bowling_inn = player_odi_bowling_inn,
    player_odi_b = player_odi_b,
    player_odi_bowling_runs = player_odi_bowling_runs,
    player_odi_wkts = player_odi_wkts,
    player_odi_bbi = player_odi_bbi,
    player_odi_bbm = player_odi_bbm,
    player_odi_econ = player_odi_econ,
    player_odi_bowling_avg = player_odi_bowling_avg,
    player_odi_bowling_sr = player_odi_bowling_sr,
    player_odi_5W = player_odi_5W,
    player_odi_10W = player_odi_10W,

    player_t20_bowling_m=player_t20_bowling_m,
    player_t20_bowling_inn = player_t20_bowling_inn,
    player_t20_b = player_t20_b,
    player_t20_bowling_runs = player_t20_bowling_runs,
    player_t20_wkts = player_t20_wkts,
    player_t20_bbi = player_t20_bbi,
    player_t20_bbm = player_t20_bbm,
    player_t20_econ = player_t20_econ,
    player_t20_bowling_avg = player_t20_bowling_avg,
    player_t20_bowling_sr = player_t20_bowling_sr,
    player_t20_5W = player_t20_5W,
    player_t20_10W = player_t20_10W,

    player_ipl_bowling_m=player_ipl_bowling_m,
    player_ipl_bowling_inn = player_ipl_bowling_inn,
    player_ipl_b = player_ipl_b,
    player_ipl_bowling_runs = player_ipl_bowling_runs,
    player_ipl_wkts = player_ipl_wkts,
    player_ipl_bbi = player_ipl_bbi,
    player_ipl_bbm = player_ipl_bbm,
    player_ipl_econ = player_ipl_econ,
    player_ipl_bowling_avg = player_ipl_bowling_avg,
    player_ipl_bowling_sr = player_ipl_bowling_sr,
    player_ipl_5W = player_ipl_5W,
    player_ipl_10W = player_ipl_10W,

    player_test_debut = player_test_debut,
    player_last_test = player_last_test,

    player_odi_debut = player_odi_debut,
    player_last_odi = player_last_odi,

    player_t20_debut = player_t20_debut,
    player_last_t20 = player_last_t20,

    player_ipl_debut = player_ipl_debut,
    player_last_ipl = player_last_ipl,

    player_bio = player_bio)


