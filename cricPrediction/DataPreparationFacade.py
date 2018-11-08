import numpy as np


class DataPreparationFacade:
    """
    Know which subsystem classes are responsible for a request.
    Delegate client requests to appropriate subsystem objects.
    """

    def __init__(self):
        self._subsystem_team = TeamDataMaker()
        self._subsystem_match = MatchDataMaker()

    def prepare_data_for_prediction(self, team1: str, team2: str, venue: int):
        data = np.zeros((1, 38))
        data = self._subsystem_team.set_home_venue(data, venue)
        d1 = self._subsystem_team.set_team(np.copy(data), team1, 1)
        d1 = self._subsystem_team.set_team(d1, team2, 2)

        list = [self._subsystem_match.get_data_with_innings(d1)]

        d2 = self._subsystem_team.set_team(data, team1, 2)
        d2 = self._subsystem_team.set_team(d2, team2, 1)

        list.append(self._subsystem_match.get_data_with_innings(d2))

        return list


class TeamDataMaker:
    """
    Implement subsystem functionality.
    Handle work assigned by the Facade object.
    """

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

    def set_team(self, data, team: str, slot: int):
        team_map = {'Afghanistan': 0, 'Australia': 1, 'Bangladesh': 2, 'England': 3, 'India': 4, 'Ireland': 5,
                    'Kenya': 6, 'New Zealand': 7, 'Pakistan': 8, 'Scotland': 9, 'South Africa': 10, 'Sri Lanka': 11,
                    'West Indies': 12, 'Zimbabwe': 13}
        if slot == 1:
            data[0, team_map[team]] = 1.
        if slot == 2:
            team2_index = 23 + team_map[team]
            data[0, team2_index] = 1
        return data


class MatchDataMaker:
    def set_first_innings(self, data, team: int):
        if team == 1:
            data[0, 28] = 1.
            data[0, 31] = 1.
        elif team == 2:
            data[0, 30] = 1.
            data[0, 29] = 1.
        return data

    def get_data_with_innings(self, data):
        l = []
        l.append(self.set_first_innings(np.copy(data), 1))
        l.append(self.set_first_innings(np.copy(data), 2))
        return np.vstack(l)
