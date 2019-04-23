import requests, json
from pprint import pprint
my_key = 'd7f99ce0-b397-4fc9-a921-1f6db5'
payload = {
 #'api_key': my_key,
 #'start_date': '2017-03-09',
 #'end_date': '2017-03-11'
}
endpoint = 'https://api.mysportsfeeds.com/v1.2/pull/mlb/current/cumulative_player_stats.json'
try:
    r = requests.get(endpoint)
    data = r.json()
    pprint(data)
except:
    print('please try again')
