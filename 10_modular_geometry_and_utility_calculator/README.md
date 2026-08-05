# 🧮 10 - Modular Geometry and Utility Calculator (CLI)

Proyek ini adalah implementasi praktikum **Pertemuan 10** mata kuliah **Algoritma dan Pemrograman 1** yang berfokus pada **Fungsi & Modularisasi**.

---

## 📌 Fitur Utama

- 📐 **Kalkulator Bangun Datar (2D):** Luas & keliling persegi, persegi panjang, segitiga, dan lingkaran.
- 📦 **Kalkulator Bangun Ruang (3D):** Volume kubus, balok, tabung, dan bola.
- 🧾 **Ringkasan Hasil Sesi:** Merangkum seluruh hasil perhitungan dalam satu sesi (rata-rata & hasil tertinggi) memakai parameter `**kwargs`.
- 🧩 **Modularisasi:** Logika dipisah ke beberapa modul (`geometry_2d.py`, `geometry_3d.py`, `stats_utils.py`) yang saling diimpor, bukan ditulis dalam satu file besar.

---

## 🧠 Konsep yang Diterapkan

- Fungsi dengan parameter & `return` (`def nama_fungsi(param): return nilai`).
- Parameter default, contoh: `phi: float = 3.14` pada fungsi lingkaran, tabung, dan bola.
- Parameter `*args` pada `rata_rata()` dan `nilai_tertinggi()` untuk menerima jumlah nilai yang tidak tetap.
- Parameter `**kwargs` pada `ringkasan_hasil()` untuk menerima pasangan label-nilai yang tidak tetap.
- Modularisasi lewat `import`, memisah setiap modul agar punya satu tanggung jawab.
- Scope variabel: `histori` dibuat lokal di `main_menu()` lalu dioper sebagai parameter ke fungsi lain, bukan diakses lewat variabel global.

---

## 🏗️ Struktur Proyek

- `src/logic/`: Modul perhitungan — `geometry_2d.py` (bangun datar) dan `geometry_3d.py` (bangun ruang).
- `src/utils/`: Modul `stats_utils.py` untuk merangkum hasil perhitungan (`*args` & `**kwargs`).
- `src/ui/`: Modul tampilan menu interaktif (`menu.py`).
- `tests/`: Pengujian unit untuk seluruh fungsi geometri dan utilitas statistik.

---

## 🚀 Cara Menjalankan Program

Jalankan perintah berikut dari direktori utama repositori:

```bash
python 10_modular_geometry_and_utility_calculator/main.py
```

Untuk menjalankan pengujian unit:

```bash
python -m unittest discover 10_modular_geometry_and_utility_calculator/tests
```
