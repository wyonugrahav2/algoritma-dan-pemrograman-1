"""
Modul Tampilan Antarmuka CLI (Pertemuan 4)
Menyajikan menu interaktif untuk simulasi perulangan dan login.
"""

from src.logic.auth import run_login_simulation
from src.logic.pattern import generate_reverse_pyramid, sum_even_numbers


def show_main_menu(user_db):
    """
    Menampilkan menu utama setelah berhasil dikonfirmasi atau sebagai navigasi fitur.
    """
    while True:
        print("\n" + "=" * 45)
        print("🌀 MODUL PERTEMUAN 4: STRUKTUR PERULANGAN")
        print("=" * 45)
        print("1. 🔐 Simulasi Login (Max 3 Attempts)")
        print("2. 🔺 Cetak Pola Piramida Terbalik (Nested Loop)")
        print("3. 🔢 Kalkulator Total Bilangan Genap (Range)")
        print("0. 🚪 Keluar Modul M4")
        print("=" * 45)

        choice = input("Pilih menu (0-3): ").strip()

        if choice == "1":
            run_login_simulation(user_db)
        elif choice == "2":
            rows = input("Masukkan jumlah baris piramida (default 5): ").strip()
            rows_num = int(rows) if rows.isdigit() else 5
            print("\n" + generate_reverse_pyramid(rows_num))
        elif choice == "3":
            val = input("Masukkan batas angka N: ").strip()
            if val.isdigit():
                n = int(val)
                total, evens = sum_even_numbers(n)
                print(f"\n✅ Bilangan genap dari 1-{n}: {evens}")
                print(f"📊 Total penjumlahan: {total}")
            else:
                print("❌ Input harus berupa angka bulat!")
        elif choice == "0":
            print("\n👋 Kembali ke Dashboard Utama...")
            break
        else:
            print("❌ Pilihan tidak valid, silakan coba lagi!")