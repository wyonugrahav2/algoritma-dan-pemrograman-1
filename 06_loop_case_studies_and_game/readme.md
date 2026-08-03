# 🌀 06 - Loop Case Studies & Game Simulation (CLI)

Proyek ini adalah implementasi praktikum Pertemuan 6 mata kuliah Algoritma dan Pemrograman 1 yang berfokus pada penerapan logika perulangan (For & While Loop) dalam berbagai studi kasus simulasi dan mini-game interaktif.

## 📌 Fitur Utama
- 🔢 **Factorial & Power Table:** Perhitungan faktorial dan generator tabel pangkat ($n^2$, $n^3$) interaktif.
- 🎮 **Number Guessing Game:** Game tebak angka dinamis dengan sistem umpan balik dan pencatat kesempatan tebak.
- 💾 **Score & History Tracker:** Penyimpanan riwayat permainan ke berkas JSON.

## 🏗️ Struktur Proyek
- `data/`: Berkas riwayat permainan (`game_history.json`).
- `src/logic/`: Modul perhitungan matematika (`math_cases.py`) dan game (`guessing_game.py`).
- `src/ui/`: Modul tampilan menu interaktif (`menu.py`).
- `src/utils/`: Modul pembaca dan penyimpan riwayat (`score_tracker.py`).
- `tests/`: Pengujian unit logika matematika dan game.

## 🚀 Cara Menjalankan Program
```bash
python 06_loop_case_studies_and_game/main.py