import json
import pytz
import abc
import requests
from flask import Blueprint,render_template


app = Blueprint('schedule', __name__)

@app.route('/schedule/')
def schedule():
    data = Adapter()
    return render_template('schedule/Upcoming_matches.html', matches=data.get_match_data())




# Target interface
class UpcomingMatchData(metaclass=abc.ABCMeta):
    """
        Define the domain-specific interface that Client uses.
        """

    def __init__(self):
        self._adaptee = UpcomingMatchDataApi()


    @abc.abstractmethod
    def get_match_data(self): pass


class Adapter(UpcomingMatchData):
    """
    Adapt the interface of Adaptee to the Target interface.
    """

    def parse_date(self, date_str):
        from datetime import datetime
        return datetime.strptime(date_str,'%Y-%m-%dT%H:%M:%S.%fZ')


    def get_match_data(self):
        json_string = self._adaptee.get_upcoming_matches()
        r = json.loads(json_string)['matches']
        matches = []
        for l in r:
            if l['type'] == 'First-class':
                l['type'] = 'Test'
            elif l['type'] == 'ListA':
                continue
            l['date'] = self.parse_date(l['dateTimeGMT'])
            matches.append(l)
        return matches


#Adaptee
class UpcomingMatchDataApi:
    """
    Define an existing interface that needs adapting.
    """

    def get_upcoming_matches(self):
        cric_api_key = "mBnk5q5Ds8fW8cL1ZDoCpX0Bao03"
        params = {
            'apikey': cric_api_key
        }
        url = 'http://cricapi.com/api/matches'
        r = requests.get(url, params=params)
        return r.text


def main():
    adapter = Adapter()
    print(adapter.get_match_data())


if __name__ == "__main__":
    main()