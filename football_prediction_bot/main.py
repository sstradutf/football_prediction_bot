from .data_fetcher import fetch_matches
from .telegram_alert import send_message

def main():
    matches = fetch_matches()
    msg = "📊 Prédictions du jour :\n"
    for m in matches[:5]:  # Exemple : les 5 premiers
        msg += f"🏟️ {m['homeTeam']['name']} vs {m['awayTeam']['name']}\n"
    send_message(msg)

if __name__ == '__main__':
    main()
