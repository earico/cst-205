# Install the Python Requests library:
# `pip install requests`

import base64
import requests


def send_request():
    # Request

    try:
        response = requests.get(
            url="https://api.mysportsfeeds.com/v1.2/pull/mlb/current/cumulative_player_stats.json",
            params={
                "team": "lad"
            },
            headers={
                "Authorization": "Basic " + base64.b64encode('{}:{}'.format("d7f99ce0-b397-4fc9-a921-1f6db5","Kaliman5251").encode('utf-8')).decode('ascii')
            }
        )
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')

