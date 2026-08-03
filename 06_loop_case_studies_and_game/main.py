from src.ui.menu import play_game_menu, show_history_menu, show_math_menu


def main():
    while True:
        print("\n==========================================")
        print("🌀 Module 06: Loop Case Studies & Game")
        print("==========================================")
        print("1. 🔢 Fitur Matematika (Faktorial & Tabel)")
        print("2. 🎮 Main Game Tebak Angka")
        print("3. 📜 Lihat Riwayat Skor Game")
        print("4. 🚪 Keluar")
        pilihan = input("Pilih menu (1-4): ")

        if pilihan == "1":
            show_math_menu()
        elif pilihan == "2":
            play_game_menu()
        elif pilihan == "3":
            show_history_menu()
        elif pilihan == "4":
            print("\nTerima kasih! Sampai jumpa 👋")
            break
        else:
            print("❌ Pilihan tidak valid, coba lagi.")


if __name__ == "__main__":
    main()