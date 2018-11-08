from os import path

import numpy as np
from sklearn.externals import joblib

from cricPrediction.DataPreparationFacade import DataPreparationFacade

"""
Object pool pattern
Offer a significant performance boost; most effective in situations where the cost of initializing a class instance
 is high, the rate of instantiation of a class is high, and the number of instantiations in use at any one time is low.
"""


class PredictionModelPool:
    """
    Manage Reusable objects for use by Client objects.
    """

    def __init__(self, root, size=3):
        self._reusables = [PredictionModel(root) for _ in range(size)]

    def acquire(self):
        return self._reusables.pop()

    def release(self, reusable):
        self._reusables.append(reusable)


class PredictionModel:
    def __init__(self, root):
        file_path = path.join(root, 'svm.joblib')
        self._clf = joblib.load(file_path)

    def predict_probability(self, data):
        return self._clf.predict_proba(data)


class ServePrediction:

    def __init__(self):
        self._data_helper = DataPreparationFacade()

    def predict(self, model: PredictionModel, team1: str, team2: str, venue: int):
        d = self._data_helper.prepare_data_for_prediction(team1, team2, venue)
        pred1 = model.predict_probability(d[0])
        pred2 = 1 - model.predict_probability(d[1])
        return np.divide(pred1 + pred2, 2) * 100

    def get_formatted_prediction(self, team1, team2, pred: np.ndarray):
        result = {}
        result[team1] = {'bat_first': pred[0, 0], 'ball_first': pred[1, 0]}
        result[team2] = {'bat_first': pred[0, 1], 'ball_first': pred[1, 1]}
        return result

# def main():
#     reusable_pool = PredictionModelPool("", 2)
#     reusable = reusable_pool.acquire()
#     serve = ServePrediction()
#     print(serve.predict(reusable, 'England', 'Bangladesh', 1))
#     reusable_pool.release(reusable)
#
#
# if __name__ == "__main__":
#     main()
