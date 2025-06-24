import json
from models.player import Player

def load_players(filepath):
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            return {pid: Player.from_dict(pdata) for pid, pdata in data.items()}
    except FileNotFoundError:
        return {}

def save_players(filepath, players):
    with open(filepath, "w") as f:
        json.dump({pid: player.to_dict() for pid, player in players.items()}, f, indent=4)

def load_matches(filepath):
    try:
        with open(filepath, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_matches(filepath, matches):
    with open(filepath, "w") as f:
        json.dump(matches, f, indent=4)
