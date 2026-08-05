"""
Modul UI: Menu Interaktif
Pertemuan 10 - Kalkulator Geometri Modular

Menghubungkan modul geometry_2d, geometry_3d, dan stats_utils
melalui import modular, lalu menampilkannya sebagai menu CLI.

Catatan scope variabel:
- `histori` dibuat sebagai variabel LOKAL di dalam main_menu() lalu
  dikirim sebagai parameter ke fungsi-fungsi menu lain. Ini sengaja
  dilakukan agar tidak bergantung pada variabel global, sesuai
  praktik penulisan fungsi yang baik (menerima input via parameter,
  bukan membaca/menulis variabel di luar fungsinya).
"""

from src.logic.geometry_2d import (
    luas_persegi,
    keliling_persegi,
    luas_persegi_panjang,
    keliling_persegi_panjang,
    luas_segitiga,
    luas_lingkaran,
    keliling_lingkaran,
)
from src.logic.geometry_3d import (
    volume_kubus,
    volume_balok,
    volume_tabung,
    volume_bola,
)
from src.utils.stats_utils import ringkasan_hasil


def _input_angka(teks: str) -> float:
    """Meminta input angka dari pengguna, mengulang jika tidak valid."""
    while True:
        try:
            return float(input(teks))
        except ValueError:
            print("❌ Masukkan angka yang valid.")


def menu_bangun_datar(histori: dict) -> None:
    print("\n--- 📐 Kalkulator Bangun Datar (2D) ---")
    print("1. Persegi")
    print("2. Persegi Panjang")
    print("3. Segitiga")
    print("4. Lingkaran")
    pilihan = input("Pilih bangun (1-4): ")

    if pilihan == "1":
        sisi = _input_angka("Masukkan panjang sisi: ")
        luas = luas_persegi(sisi)
        keliling = keliling_persegi(sisi)
        print(f"✨ Luas persegi   : {luas}")
        print(f"✨ Keliling persegi: {keliling}")
        histori["luas_persegi"] = luas

    elif pilihan == "2":
        panjang = _input_angka("Masukkan panjang: ")
        lebar = _input_angka("Masukkan lebar: ")
        luas = luas_persegi_panjang(panjang, lebar)
        keliling = keliling_persegi_panjang(panjang, lebar)
        print(f"✨ Luas persegi panjang   : {luas}")
        print(f"✨ Keliling persegi panjang: {keliling}")
        histori["luas_persegi_panjang"] = luas

    elif pilihan == "3":
        alas = _input_angka("Masukkan alas: ")
        tinggi = _input_angka("Masukkan tinggi: ")
        luas = luas_segitiga(alas, tinggi)
        print(f"✨ Luas segitiga: {luas}")
        histori["luas_segitiga"] = luas

    elif pilihan == "4":
        jari_jari = _input_angka("Masukkan jari-jari: ")
        luas = luas_lingkaran(jari_jari)
        keliling = keliling_lingkaran(jari_jari)
        print(f"✨ Luas lingkaran   : {luas}")
        print(f"✨ Keliling lingkaran: {keliling}")
        histori["luas_lingkaran"] = luas

    else:
        print("❌ Pilihan tidak valid.")


def menu_bangun_ruang(histori: dict) -> None:
    print("\n--- 📦 Kalkulator Bangun Ruang (3D) ---")
    print("1. Kubus")
    print("2. Balok")
    print("3. Tabung")
    print("4. Bola")
    pilihan = input("Pilih bangun (1-4): ")

    if pilihan == "1":
        sisi = _input_angka("Masukkan panjang sisi: ")
        volume = volume_kubus(sisi)
        print(f"✨ Volume kubus: {volume}")
        histori["volume_kubus"] = volume

    elif pilihan == "2":
        panjang = _input_angka("Masukkan panjang: ")
        lebar = _input_angka("Masukkan lebar: ")
        tinggi = _input_angka("Masukkan tinggi: ")
        volume = volume_balok(panjang, lebar, tinggi)
        print(f"✨ Volume balok: {volume}")
        histori["volume_balok"] = volume

    elif pilihan == "3":
        jari_jari = _input_angka("Masukkan jari-jari: ")
        tinggi = _input_angka("Masukkan tinggi: ")
        volume = volume_tabung(jari_jari, tinggi)
        print(f"✨ Volume tabung: {volume}")
        histori["volume_tabung"] = volume

    elif pilihan == "4":
        jari_jari = _input_angka("Masukkan jari-jari: ")
        volume = volume_bola(jari_jari)
        print(f"✨ Volume bola: {volume}")
        histori["volume_bola"] = volume

    else:
        print("❌ Pilihan tidak valid.")


def menu_ringkasan(histori: dict) -> None:
    print("\n--- 🧮 Ringkasan Hasil Perhitungan ---")
    if not histori:
        print("Belum ada perhitungan yang dilakukan pada sesi ini.")
        return

    ringkasan = ringkasan_hasil(**histori)
    print(f"Jumlah perhitungan  : {ringkasan['jumlah_data']}")
    print(f"Rata-rata hasil     : {ringkasan['rata_rata']:.2f}")
    print(f"Hasil tertinggi     : {ringkasan['label_tertinggi']} = {ringkasan['nilai_tertinggi']}")

    print("\nRincian per perhitungan:")
    for label, nilai in histori.items():
        print(f"  - {label}: {nilai}")


def main_menu() -> None:
    histori: dict = {}

    while True:
        print("\n==========================================")
        print("🧮 Kalkulator Geometri Modular")
        print("==========================================")
        print("1. 📐 Bangun Datar (2D)")
        print("2. 📦 Bangun Ruang (3D)")
        print("3. 🧾 Ringkasan Hasil Sesi Ini")
        print("4. 🚪 Keluar")
        pilihan = input("Pilih menu (1-4): ")

        if pilihan == "1":
            menu_bangun_datar(histori)
        elif pilihan == "2":
            menu_bangun_ruang(histori)
        elif pilihan == "3":
            menu_ringkasan(histori)
        elif pilihan == "4":
            print("\nTerima kasih! Sampai jumpa 👋")
            break
        else:
            print("❌ Pilihan tidak valid, coba lagi.")
