from src.logic.pattern_generator import generate_triangle, generate_inverted_triangle, generate_number_pyramid
from src.logic.matrix_calculator import generate_multiplication_table, render_matrix
from src.utils.file_handler import load_matrix_presets

def display_menu():
    """Menampilkan menu utama antarmuka CLI."""
    print("=" * 45)
    print("🌀  05 - NESTED LOOP & MATRIX SIMULATION CLI  🌀")
    print("=" * 45)
    print("1. 📐 Cetak Pola Segitiga Bintang")
    print("2. 🔺 Cetak Pola Segitiga Terbalik")
    print("3. 🔢 Cetak Pola Piramida Angka")
    print("4. ✖️  Generasi Tabel Perkalian (Matriks NxN)")
    print("5. 📂 Tampilkan Preset Matriks (JSON)")
    print("0. 🚪 Keluar")
    print("=" * 45)

def run_cli():
    """Menjalankan loop antarmuka CLI utama."""
    while True:
        display_menu()
        choice = input("Pilih menu (0-5): ").strip()
        
        if choice == "1":
            rows = int(input("Masukkan jumlah baris: "))
            print("\n" + generate_triangle(rows) + "\n")
        elif choice == "2":
            rows = int(input("Masukkan jumlah baris: "))
            print("\n" + generate_inverted_triangle(rows) + "\n")
        elif choice == "3":
            rows = int(input("Masukkan jumlah baris: "))
            print("\n" + generate_number_pyramid(rows) + "\n")
        elif choice == "4":
            n = int(input("Masukkan ukuran matriks N (contoh 5): "))
            matrix = generate_multiplication_table(n)
            print("\n" + render_matrix(matrix) + "\n")
        elif choice == "5":
            presets = load_matrix_presets()
            print("\n--- Preset Matriks Tersimpan ---")
            for p in presets:
                print(f"• {p['name']} ({p['rows']}x{p['cols']})")
            print()
        elif choice == "0":
            print("\nTerima kasih! Sampai jumpa di Pertemuan 6! 👋✨\n")
            break
        else:
            print("\n[-] Pilihan tidak valid, silakan coba lagi.\n")