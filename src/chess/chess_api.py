import requests

CHESS_API_BASE = "https://api.chess.com/pub"

headers = {"accept" : "application/json",
           "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Python/3.14 requests/2.32.5"}

def make_api_call(url: str) -> str:
    response = requests.get(url=url, headers=headers)
    response.raise_for_status()
    return response.json()

def get_profile_player(username):
    url = f"{CHESS_API_BASE}/player/{username}"
    return make_api_call(url)

def get_player_stats(username):
    url = f"{CHESS_API_BASE}/player/{username}/stats"
    return make_api_call(url)