from sklearn.externals import joblib
import numpy as np
from os import path
from flask import url_for



class ServePrediction:
    clf = None

    def __init__(self, root):
        file_path = path.join(root, 'svm.joblib')
        self.clf = joblib.load(file_path)


    def set_first_innings(self, data, team: int):
        if team == 1:
            data[0, 28] = 1.
            data[0, 31] = 1.
        elif team == 2:
            data[0, 30] = 1.
            data[0, 29] = 1.
        return data

    def set_home_venue(self, data, team: int):
        if team == 1:
            data[0, 33] = 1.
            data[0, 35] = 1.
        elif team == 2:
            data[0, 32] = 1.
            data[0, 36] = 1.
        else:
            data[0, 34] = 1.
            data[0, 37] = 1.
        return data


    def set_team(self, data, team:str, slot:int):
        team_map = {'Afghanistan': 0, 'Australia': 1, 'Bangladesh': 2, 'England': 3, 'India': 4, 'Ireland': 5,
                    'Kenya': 6, 'New Zealand': 7, 'Pakistan': 8, 'Scotland': 9, 'South Africa': 10, 'Sri Lanka': 11,
                    'West Indies': 12, 'Zimbabwe': 13}
        if slot == 1:
            data[0, team_map[team]] = 1.
        if slot == 2:
            team2_index = 23 + team_map[team]
            data[0, team2_index] = 1
        return data


    def get_data_with_innings(self, data):
        l = []
        l.append(self.set_first_innings(np.copy(data), 1))
        l.append(self.set_first_innings(np.copy(data), 2))
        return np.vstack(l)

    def prepare_data_for_prediction(self, team1: str, team2: str, venue: int):
        team_map = {'Afghanistan': 0, 'Australia': 1, 'Bangladesh': 2, 'England': 3, 'India': 4, 'Ireland': 5,
                    'Kenya': 6, 'New Zealand': 7, 'Pakistan': 8, 'Scotland': 9, 'South Africa': 10, 'Sri Lanka': 11,
                    'West Indies': 12, 'Zimbabwe': 13}
        data = np.zeros((1, 38))
        data = self.set_home_venue(data, venue)
        d1 = self.set_team(np.copy(data), team1, 1)
        d1 = self.set_team(d1, team2, 2)

        list = []
        list.append(self.get_data_with_innings(d1))

        d2 = self.set_team(data, team1, 2)
        d2 = self.set_team(d2, team2, 1)

        list.append(self.get_data_with_innings(d2))

        return list

    def predict(self, team1: str, team2: str, venue: int):
        d = self.prepare_data_for_prediction(team1, team2, venue)
        pred1 = self.clf.predict_proba(d[0])
        pred2 = 1 - self.clf.predict_proba(d[1])
        return np.divide(pred1+pred2, 2)*100


    def get_formatted_prediction(self, team1, team2, pred:np.ndarray):
        result = {}
        result[team1] = {'bat_first': pred[0,0], 'ball_first': pred[1,0]}
        result[team2] = {'bat_first': pred[0,1], 'ball_first' : pred[1,1]}
        return result







def main():
    pass
    # s = ServePrediction()
    # s.predict('England', 'Bangladesh', 1)



if __name__ == "__main__":
    main()