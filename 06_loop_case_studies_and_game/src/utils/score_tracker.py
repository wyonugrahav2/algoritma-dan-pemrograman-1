import json
import os

DATA_FILE = os.path.join(
    os.path.dirname(__file__), "../../data/game_history.json"
)


def load_history() -> list[dict]:
    """Membaca riwayat permainan dari file JSON."""
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        return []


def save_game_result(player_name: str, attempts: int, secret_number: int):
    """Menyimpan hasil permainan baru ke dalam file JSON."""
    history = load_history()
    new_record = {
        "player_name": player_name,
        "attempts": attempts,
        "secret_number": secret_number,
    }
    history.append(new_record)

    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(history, file, indent=2)