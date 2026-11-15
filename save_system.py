import json
import os
from characters import Player

SAVE_FILE = "savegame.json"


def save_game(player):
    with open(SAVE_FILE, "w") as f:
        json.dump(player.to_dict(), f, indent=4)
    print("Game Saved!")

def load_game():
    if not os.path.exists(SAVE_FILE):
        print("No save file found.")
        return None

    with open(SAVE_FILE, "r") as f:
        data = json.load(f)
        print(f"Loaded save for {data[f'name']} (level {data['level']})!")
        input()
        return Player.from_dict(data)
