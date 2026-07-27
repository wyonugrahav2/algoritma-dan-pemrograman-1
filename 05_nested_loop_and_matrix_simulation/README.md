# 🌀 05 - Nested Loop and Matrix Simulation (CLI)

Proyek ini adalah implementasi praktikum **Pertemuan 5** mata kuliah **Algoritma dan Pemrograman 1** yang berfokus pada **Struktur Kontrol Perulangan Bersarang (*Nested Loop*)**.

---

## 📌 Fitur Utama
* **🎨 Visual Pattern Generator:** Menggenerate berbagai bentuk pola 2D (segitiga, piramida, dan persegi) menggunakan kombinasi *nested loop* (`for` & `while`).
* **✖️ Multiplication Table Matrix:** Menampilkan tabel perkalian interaktif skala $N \times N$ menggunakan logika perulangan dua lapis.
* **🔢 Number Pyramid Builder:** Mengolah logika perulangan bersarang untuk mencetak pola angka berurutan dan terbalik secara dinamis.

---

## 🏗️ Struktur Proyek
- `data/`: Menyimpan berkas `matrix_presets.json`.
- `src/logic/`: Modul logika pola bintang (`pattern.py`) dan matriks (`matrix.py`).
- `src/ui/`: Modul tampilan menu pilihan pola dan pengatur format grid (`menu.py`).
- `src/utils/`: Modul utilitas pembaca berkas (`file_handler.py`).
- `tests/`: Pengujian unit untuk logika pola dan matriks.

---

## 🚀 Cara Menjalankan Program

Jalankan perintah berikut dari direktori utama repositori:

```bash
python 05_nested_loop_and_matrix_simulation/main.py