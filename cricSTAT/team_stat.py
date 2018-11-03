from cricMongoDB.database import db


def get_data(team):
    response = db.team_stats.find({'Team': team}, {'_id': False})
    #data = json_util.loads(response)
    labels = []
    values1 = []
    values2 = []
    values3 = []
    for row in response:
        win_per = ((row['Won'] + row['Draw']) / row['Mat']) * 100
        if row['type'] == 'odi':
            labels.append(row['Year'])
            values1.append(win_per)
        elif row['type'] == 'test':
            values2.append(win_per)
        else:
            values3.append(win_per)

    values = {'odi': values1, 'test': values2, 't20i': values3}
    return labels, values


if __name__ == "__main__":
    l,v = get_data('Bangladesh')
    print(l)