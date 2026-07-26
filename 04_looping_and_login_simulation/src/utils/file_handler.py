"""
Modul Penanganan Berkas (Pertemuan 4)
Menangani pembacaan data JSON untuk sistem autentikasi.
"""

import json
import os


def load_user_data(file_path):
    """
    Membaca data pengguna dari file JSON.
    """
    if not os.path.exists(file_path):
        return {"users": []}

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except Exception as e:
        print(f"⚠️ Gagal membaca berkas data: {e}")
        return {"users": []}