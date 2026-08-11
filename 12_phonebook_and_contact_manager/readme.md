# 📞 12 - Phonebook & Contact Manager (CLI)

Proyek ini adalah implementasi praktikum Pertemuan 12 mata kuliah Algoritma dan Pemrograman 1 yang berfokus pada **implementasi File Handling** menggunakan format CSV untuk membangun sistem buku kontak persisten.

## 📌 Fitur Utama

- ➕ **Tambah Kontak:** Menyimpan nama, telepon, dan email baru menggunakan mode **append (`a`)**.
- 📇 **Lihat Semua Kontak:** Membaca seluruh data kontak dari file menggunakan mode **read (`r`)**.
- 🔍 **Cari Kontak:** Menyaring kontak berdasarkan nama, telepon, atau email.
- 🗑️ **Hapus Kontak:** Menghapus kontak tertentu dengan membaca ulang & menulis ulang seluruh data menggunakan mode **write (`w`)**.

## 🏗️ Struktur Proyek

- `data/`: Berkas data kontak dalam format CSV (`contacts.txt`).
- `src/logic/`: Modul pembentukan, penguraian, dan validasi data kontak (`contact_entry.py`).
- `src/utils/`: Modul operasi file — baca, tulis, append, hapus (`file_handler.py`).
- `src/ui/`: Modul tampilan menu interaktif (`menu.py`).
- `tests/`: Pengujian unit untuk logika format/parse/validasi kontak.

## 💾 Format Penyimpanan

Setiap baris pada `contacts.txt` disimpan dengan format CSV:

```
nama,telepon,email
```

## 🚀 Cara Menjalankan Program

```bash
python 12_phonebook_and_contact_manager/main.py
```
