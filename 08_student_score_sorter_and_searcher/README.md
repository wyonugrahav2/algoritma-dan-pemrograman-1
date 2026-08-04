# 📊 08 - Student Score Sorter and Searcher (CLI)

Proyek ini adalah implementasi praktikum **Pertemuan 8** mata kuliah **Algoritma dan Pemrograman 1** yang berfokus pada **Algoritma Pencarian dan Pengurutan Data (Searching & Sorting)**.

---

## 📌 Fitur Utama
- 📊 **Ranking Nilai (Bubble Sort):** Mengurutkan data nilai mahasiswa dari tertinggi ke terendah (atau sebaliknya) menggunakan algoritma Bubble Sort.
- 🔎 **Pencarian Data (Linear Search):** Mencari mahasiswa berdasarkan nama (pencarian sebagian) maupun berdasarkan nilai yang persis sama.
- ➕ **Input Data Dinamis:** Menambahkan data nilai mahasiswa baru secara interaktif melalui terminal.
- 💾 **Penyimpanan Data:** Data mahasiswa disimpan secara persisten ke berkas JSON.

---

## 🏗️ Struktur Proyek
- `data/`: Berkas data nilai mahasiswa (`students.json`).
- `src/logic/`: Modul algoritma inti — `sorting.py` (Bubble Sort) dan `searching.py` (Linear Search).
- `src/ui/`: Modul tampilan menu interaktif (`menu.py`).
- `src/utils/`: Modul pembaca dan penyimpan data (`data_handler.py`).
- `tests/`: Pengujian unit untuk logika sorting dan searching.

---

## 🚀 Cara Menjalankan Program

Jalankan perintah berikut dari direktori utama repositori:

```bash
python 08_student_score_sorter_and_searcher/main.py
```

Untuk menjalankan pengujian unit:

```bash
python -m unittest discover 08_student_score_sorter_and_searcher/tests
```
