# 02 - User Profile & Health/Study Calculator

Modul ini merupakan bagian dari proyek **My CLI Dashboard**, dikerjakan untuk
mata kuliah **Algoritma dan Pemrograman 1 - Pertemuan 2 (M2)**.

## Materi yang Digunakan
Modul ini murni dibangun menggunakan materi yang diajarkan pada Pertemuan 2:
- Konsep variabel
- Tipe data dasar (`int`, `float`, `str`, `bool`)
- Fungsi `input()` dan `print()`
- Konversi tipe data (*type casting*)

Belum menggunakan logika bercabang (`if-else`), perulangan (`loop`), atau
fungsi/class kustom, karena materi tersebut belum dipelajari pada pertemuan ini.

## Fitur
Program menerima data diri mahasiswa lalu menampilkannya kembali dalam bentuk
*dashboard* ringkasan berformat ASCII di terminal.

**Data yang diminta dari pengguna:**
- Nama lengkap
- NPM
- Jurusan
- Umur (tahun)
- Tinggi badan (cm)
- Berat badan (kg)
- Target jam belajar harian

**Kalkulasi yang dilakukan:**
- Perkiraan tahun lahir (`tahun_sekarang - umur`)
- Konversi tinggi badan dari cm ke meter
- Skor BMI (*Body Mass Index*) sederhana: `berat / (tinggi_m * tinggi_m)`
- Total target jam belajar mingguan (`jam_belajar_harian * 7`)

**Output:**
Ringkasan profil, kesehatan, dan target belajar ditampilkan dalam tiga bagian
dashboard CLI yang rapi dengan border garis `=` dan `-`.

## Cara Menjalankan
```bash
cd 02_user_profile_calculator/src
python main.py
```

Program akan meminta input satu per satu, lalu menampilkan ringkasan di akhir.

## Struktur Folder
```
02_user_profile_calculator/
├── src/
│   └── main.py          # Kode utama program
├── README.md             # Dokumentasi modul ini
└── requirements.txt       # Daftar dependensi (tidak ada library eksternal)
```
