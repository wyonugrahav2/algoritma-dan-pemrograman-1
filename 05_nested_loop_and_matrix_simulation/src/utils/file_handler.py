import json
import os

def load_matrix_presets(filepath="05_nested_loop_and_matrix_simulation/data/matrix_presets.json"):
    """Membaca preset matriks dari berkas JSON."""
    if not os.path.exists(filepath):
        return []
    
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data.get("presets", [])
    except Exception as e:
        print(f"[-] Error membaca JSON: {e}")
        return []