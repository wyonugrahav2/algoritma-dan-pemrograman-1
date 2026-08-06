from src.ui.menu import (
    add_activity_menu,
    clear_activity_menu,
    search_activity_menu,
    show_all_activity_menu,
)


def main():
    while True:
        print("\n==========================================")
        print("📝 Module 11: Persistent Activity Logger")
        print("==========================================")
        print("1. ➕ Tambah Aktivitas Baru")
        print("2. 📜 Lihat Semua Log Aktivitas")
        print("3. 🔍 Cari Aktivitas")
        print("4. 🗑️ Hapus Semua Log")
        print("5. 🚪 Keluar")
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            add_activity_menu()
        elif pilihan == "2":
            show_all_activity_menu()
        elif pilihan == "3":
            search_activity_menu()
        elif pilihan == "4":
            clear_activity_menu()
        elif pilihan == "5":
            print("\nTerima kasih! Sampai jumpa 👋")
            break
        else:
            print("❌ Pilihan tidak valid, coba lagi.")


if __name__ == "__main__":
    main()
