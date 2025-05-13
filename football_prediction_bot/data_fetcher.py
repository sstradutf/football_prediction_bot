import requests
from .config import API_TOKEN

def fetch_matches():
    url = 'https://api.football-data.org/v4/matches'
    headers = {'X-Auth-Token': API_TOKEN}
    response = requests.get(url, headers=headers)
    return response.json()['matches']
