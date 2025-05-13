import requests
import pandas as pd
from football_prediction_bot.config import API_TOKEN

HEADERS = {'X-Auth-Token': API_TOKEN}

def fetch_matches():
    url = "https://api.football-data.org/v4/competitions/PL/matches?season=2023"
    response = requests.get(url, headers=HEADERS)
    matches = response.json()["matches"]
    data = []
    for match in matches:
        if match['status'] == "FINISHED":
            data.append({
                "date": match['utcDate'],
                "home_team": match['homeTeam']['name'],
                "away_team": match['awayTeam']['name'],
                "home_score": match['score']['fullTime']['homeTeam'],
                "away_score": match['score']['fullTime']['awayTeam']
            })
    df = pd.DataFrame(data)
    df.to_csv("historical_matches.csv", index=False)
    print("Données récupérées et sauvegardées.")
