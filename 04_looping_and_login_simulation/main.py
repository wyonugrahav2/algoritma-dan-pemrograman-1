"""
Entry Point Aplikasi Modul Pertemuan 4
Program Utama Simulasi Perulangan dan System Login CLI
"""

import os
import sys

# Menambahkan direktori utama proyek ke sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.ui.menu import show_main_menu
from src.utils.file_handler import load_user_data


def main():
    # Jalur berkas data users.json
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(base_dir, "data", "users.json")

    # Memuat data pengguna
    user_db = load_user_data(data_path)

    # Menjalankan antarmuka menu utama
    show_main_menu(user_db)


if __name__ == "__main__":
    main()