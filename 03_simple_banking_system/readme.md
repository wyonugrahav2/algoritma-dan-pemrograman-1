# 03 - Simple Banking System (CLI)

Proyek ini adalah simulasi sistem perbankan/ATM berbasis antarmuka baris perintah (CLI) yang dibangun menggunakan Python.

## 🎯 Fitur Utama
- **Autentikasi PIN**: Verifikasi akun nasabah sebelum masuk menu.
- **Cek Saldo**: Menampilkan saldo terkini dalam format Rupiah.
- **Setor Tunai**: Menambah nilai saldo akun.
- **Tarik Tunai**: Mengurangi saldo dengan validasi batas kecukupan saldo.
- **Penyimpanan Data (JSON)**: Data nasabah tersimpan secara persisten.

## 🏗️ Struktur Proyek
- `data/`: Menyimpan file `accounts.json`.
- `src/logic/`: Modul logika autentikasi dan transaksi.
- `src/ui/`: Modul tampilan menu dan output format.
- `src/utils/`: Modul pembaca/penyimpan berkas.

## 🚀 Cara Menjalankan Program

```bash
python 03_simple_banking_system/main.py