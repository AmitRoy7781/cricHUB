import time

import requests
import requests_cache
import json

from cricHub.config import cric_api_key

requests_cache.install_cache('match_cache', backend='sqlite', expire_after=1800)


def get_matches():
  params = {
    'apikey': cric_api_key
  }
  url = 'http://cricapi.com/api/matches'
  r = requests.get(url, params=params)
  now = time.ctime(int(time.time()))
  print("Time: {0} / Used Cache: {1}".format(now, r.from_cache))
  return json.loads(r.text)['matches']