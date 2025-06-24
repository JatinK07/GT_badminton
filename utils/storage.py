import json
import os
from models.player import Player

# Use a writable temp directory for file storage (works on Render and similar platforms)
DATA_DIR = "/tmp"
PLAYERS_FILE = os.path.join(DATA_DIR, "players.json")
MATCHES_FILE = os.path.join(DATA_DIR, "matches.json")

def ensure_files_exist():
    os.makedirs(DATA_DIR, exist_ok=True)
    if not os.path.exists(PLAYERS_FILE):
        with open(PLAYERS_FILE, "w") as f:
            json.dump({}, f)
    if not os.path.exists(MATCHES_FILE):
        with open(MATCHES_FILE, "w") as f:
            json.dump([], f)

def load_players():
    ensure_files_exist()
    with open(PLAYERS_FILE, "r") as f:
        data = json.load(f)
        return {pid: Player.from_dict(pdata) for pid, pdata in data.items()}

def save_players(players):
    ensure_files_exist()
    with open(PLAYERS_FILE, "w") as f:
        json.dump({pid: player.to_dict() for pid, player in players.items()}, f, indent=4)

def load_matches():
    ensure_files_exist()
    with open(MATCHES_FILE, "r") as f:
        return json.load(f)

def save_matches(matches):
    ensure_files_exist()
    with open(MATCHES_FILE, "w") as f:
        json.dump(matches, f, indent=4)
