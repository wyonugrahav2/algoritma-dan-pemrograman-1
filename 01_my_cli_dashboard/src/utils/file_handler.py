import json
import os
from pathlib import Path

# Adjust path based on execution location
DATA_FILE = Path('data/transactions.json')

def load_data():
    if not DATA_FILE.exists():
        return []
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)