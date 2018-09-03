from bs4 import BeautifulSoup
import requests
import pprint

class Vividict(dict):
    def __missing__(self, key):
        value = self[key] = type(self)()
        return value


def Menu():
    print('\n1. Men \n2. Women\n')
    gen = Gender()
    print('\n1. Team Rankings \n2. Player Ranking\n')
    tp = TeamOrPlayer()

    mode = ''
    val = ''

    if gen == 'mens':
        print('\n1. Test\n2. ODI\n3. T20\n')
        mode = Mode()

    if tp == 'player-rankings':
        if mode == '':
            print('\n1. ODI\n2. T20\n')
            mode = Mode2()
        print('\n1. Batting\n2. Bowling\n3. All-Rounder\n')
        val = Value()

    return gen, tp, mode, val


def Gender():
    gender = input('Enter your choice:')
    code = {'1': 'mens', '2': 'womens'}

    if gender in code:
        return code[gender]

    else:
        print('\nInvalid Input\nTry Again\n')
        return Gender();


def TeamOrPlayer():
    choice = input('Enter your choice:')
    tp = {'1': 'team-rankings', '2': 'player-rankings'}

    if choice in tp:
        return tp[choice]

    else:
        print('\nInvalid Input\nTry Again\n')
        return TeamOrPlayer();


def Mode():
    choice = input('Enter your choice:')
    word = {'1': '/test', '2': '/odi', '3': '/t20i'}

    if choice in word:
        return word[choice]

    else:
        print('\nInvalid Input\nTry Again\n')
        return Mode();


def Mode2():
    choice = input('Enter your choice:')
    word = {'1': '/odi', '2': '/t20i'}

    if choice in word:
        return word[choice]

    else:
        print('\nInvalid Input\nTry Again\n')
        return Mode2();


def Value():
    choice = input('Enter your choice:')
    val = {'1': 'batting', '2': 'bowling', '3': 'all-rounder'}

    if choice in val:
        return val[choice]

    else:
        print('\nInvalid Input\nTry Again\n')
        return Value()


def URL():
    gen, tp, mode, val = Menu()
    url = 'https://www.icc-cricket.com/rankings/' + gen + '/' + tp + mode + '/' + val

    header = gen.upper() + ' ' + mode[1:].upper() + ' ' + val.upper()
    print('\n{:<15}  {:<30}\n{:<15}  {:<30}'.format('', tp.upper(), '', header))
    return url, tp


def SOUP(url, tp):
    try:
        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'lxml')

        a = soup.find_all('tr', {'class': 'table-body'})

        data = {}

        for i in a:
            team = []
            name = ''
            rating = ''


            try:
                rank = int(i.contents[1].text)
            except:
                pass

            try:
                name = i.contents[3].text.replace('\n', '')
                name = " ".join(name.split())
                if rank == 1 and tp == 'player-rankings':
                    name = name[0:-3]
            except:
                pass

            try:
                rating = i.contents[9].text
            except:
                if rank == 1:
                    rating = i.contents[5].text
                else:
                    rating = i.contents[7].text

            team.extend([name, rating])
            data[rank] = team

        return data

    except:
        print("Sorry couldn't find the data right now")


def Print(data):

    for i in sorted(data):
        print('{:<10}       '.format(i), end='')
        for j in range(len(data[i])):
            pass;
            print('{:<26}'.format(data[i][j]), end='     ')
        print()


def rankings():
    """
    Diplays cricket rankings based on the input given by users

    Args : None (No arguements are passed into this function)

    Returns : None (No value is returned by this function)

    """

    url, tp = URL()
    data = SOUP(url, tp)
    Print(data)


def add_to_dict(data, url, gender, match_format, tp, player_type=""):
    print(url)
    raw_data = SOUP(url, tp)
    if(tp == 'team-rankings'):
        for i in sorted(raw_data):
            data[tp][gender][match_format][str(i)]['team'] = raw_data[i][0]
            data[tp][gender][match_format][str(i)]['rating'] = raw_data[i][1]
    else:
        for i in sorted(raw_data):
            data[tp][gender][match_format][player_type][str(i)]['player'] = raw_data[i][0]
            data[tp][gender][match_format][player_type][str(i)]['rating'] = raw_data[i][1]




def generate_team_data():
    gender = ['mens', 'womens']
    m_format = ['test', 'odi', 't20i']
    base_url = 'https://www.icc-cricket.com/rankings/'
    tp = 'team-rankings'
    data = Vividict()

    #team
    for g in gender:
        if (g == 'mens'):
            for m in m_format:
                url = base_url + g + '/team-rankings/' + m
                add_to_dict(data = data, url = url, gender=g, match_format=m, tp=tp)
        else:
            url = base_url + g + '/team-rankings/'
            add_to_dict(data = data, url = url, gender=g, match_format='all', tp=tp)



    return data


def generate_player_data():
    gender = ['mens', 'womens']
    m_format = ['odi', 't20i']
    player_type = ['batting', 'bowling','all-rounder']
    base_url = 'https://www.icc-cricket.com/rankings/'
    tp = 'player-rankings'
    data = Vividict()

    #team
    for g in gender:
        for m in m_format:
            for p in player_type:
                url = base_url + g + '/player-rankings/' + m + '/' + p
                add_to_dict(data, url, g, m, tp,p)


    return data


if __name__ == '__main__':
    # while True:
    #     rankings()
    # pprint.pprint(generate_team_data())
    pprint.pprint(generate_player_data())

