# 🌀 04 - Looping and Login Simulation (CLI)

Proyek ini adalah implementasi praktikum **Pertemuan 4** mata kuliah **Algoritma dan Pemrograman 1** yang berfokus pada **Struktur Kontrol Perulangan (*Looping*)**.

---

## 📌 Fitur Utama
* **🔐 Simulasi Login Berbatas Percobaan:** Menggunakan perulangan `while` untuk membatasi percobaan login maksimal 3 kali.
* **🔺 Generasi Pola Piramida Terbalik:** Menggunakan *nested loop* (`for`) untuk membentuk pola bintang terbalik secara dinamis.
* **🔢 Kalkulator Deret & Total Genap:** Menggunakan perulangan `for` dan fungsi `range()` untuk mencari dan menjumlahkan semua bilangan genap dari 1 hingga $N$.
* **📂 Integrasi Data JSON:** Membaca data pengguna secara aman dari berkas `data/users.json`.

---

## 🏗️ Struktur Proyek
- `data/`: Menyimpan berkas `users.json`.
- `src/logic/`: Modul logika autentikasi (`auth.py`) dan perulangan pola (`pattern.py`).
- `src/ui/`: Modul tampilan menu antarmuka CLI (`menu.py`).
- `src/utils/`: Modul utilitas pembaca berkas (`file_handler.py`).
- `tests/`: Pengujian unit untuk logika autentikasi (`test_auth.py`).

---

## 🚀 Cara Menjalankan Program

Jalankan perintah berikut dari direktori utama repositori:

```bash
python 04_looping_and_login_simulation/main.py