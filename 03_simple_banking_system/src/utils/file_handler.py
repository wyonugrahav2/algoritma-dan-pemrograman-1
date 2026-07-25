import json
import os

DATA_FILE = os.path.join(os.path.dirname(__file__), "../../data/accounts.json")


def load_accounts():
    """Membaca data akun dari berkas JSON."""
    if not os.path.exists(DATA_FILE):
        return []

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        return []


def save_accounts(accounts):
    """Menyimpan pembaruan data akun ke berkas JSON."""
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(accounts, file, indent=2)
        return True
    except Exception as e:
        print(f"Gagal menyimpan data: {e}")
        return False