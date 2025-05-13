import requests
from .config import TELEGRAM_TOKEN, CHAT_ID

# Ajoute ton propre ID ici
AUTHORIZED_USER_ID = 6567626016

def send_message(text: str, chat_id: int = AUTHORIZED_USER_ID):
    token = TELEGRAM_TOKEN  # importé depuis config.py
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "HTML"
    }

    response = requests.post(url, json=payload)
    return response.json()
