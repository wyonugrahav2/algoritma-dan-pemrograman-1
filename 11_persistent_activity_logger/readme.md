# 📝 11 - Persistent Activity Logger (CLI)

Proyek ini adalah implementasi praktikum Pertemuan 11 mata kuliah Algoritma dan Pemrograman 1 yang berfokus pada penerapan **File I/O** untuk menyimpan data secara persisten menggunakan file teks (`.txt`).

## 📌 Fitur Utama

- ➕ **Tambah Aktivitas:** Mencatat aktivitas baru beserta waktu (timestamp) dan keterangan, disimpan dengan mode **append (`a`)**.
- 📜 **Lihat Riwayat Aktivitas:** Membaca seluruh log aktivitas dari file menggunakan mode **read (`r`)**.
- 🔍 **Cari Aktivitas:** Menyaring log berdasarkan kata kunci pada aktivitas/keterangan.
- 🗑️ **Hapus Semua Log:** Mengosongkan file log menggunakan mode **write (`w`)**.

## 🏗️ Struktur Proyek

- `data/`: Berkas log aktivitas (`activity_log.txt`).
- `src/logic/`: Modul pembentukan, penguraian, dan validasi baris log (`log_entry.py`).
- `src/utils/`: Modul operasi file — baca, tulis, append (`file_handler.py`).
- `src/ui/`: Modul tampilan menu interaktif (`menu.py`).
- `tests/`: Pengujian unit untuk logika format/parse/validasi log.

## 💾 Format Penyimpanan

Setiap baris pada `activity_log.txt` disimpan dengan format:

```
YYYY-MM-DD HH:MM:SS | <aktivitas> | <keterangan>
```

## 🚀 Cara Menjalankan Program

```bash
python 11_persistent_activity_logger/main.py
```
