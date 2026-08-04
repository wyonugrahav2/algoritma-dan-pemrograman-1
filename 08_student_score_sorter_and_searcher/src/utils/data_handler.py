"""
Modul Utilitas: Penyimpanan Data Mahasiswa

Bertugas membaca dan menulis data nilai mahasiswa dari/ke berkas
JSON di folder data/, sehingga data tetap tersimpan meskipun
program ditutup.
"""

import json
import os

DATA_FILE = os.path.join(
    os.path.dirname(__file__), "../../data/students.json"
)


def load_students() -> list[dict]:
    """Membaca data mahasiswa dari file JSON."""
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        return []


def save_students(data: list[dict]) -> None:
    """Menyimpan data mahasiswa ke file JSON."""
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)


def add_student(data: list[dict], nama: str, nilai: int) -> list[dict]:
    """Menambahkan satu data mahasiswa baru ke dalam list data."""
    data_baru = data.copy()
    data_baru.append({"nama": nama.strip(), "nilai": nilai})
    return data_baru
