import sys
import os

# Menambahkan root direktori ke path agar modul src bisa terimpor dengan aman
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.ui.menu import run_cli

if __name__ == "__main__":
    run_cli()