from src.ui.menu import (
    add_contact_menu,
    delete_contact_menu,
    search_contact_menu,
    show_all_contacts_menu,
)


def main():
    while True:
        print("\n==========================================")
        print("📞 Module 12: Phonebook & Contact Manager")
        print("==========================================")
        print("1. ➕ Tambah Kontak Baru")
        print("2. 📇 Lihat Semua Kontak")
        print("3. 🔍 Cari Kontak")
        print("4. 🗑️ Hapus Kontak")
        print("5. 🚪 Keluar")
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            add_contact_menu()
        elif pilihan == "2":
            show_all_contacts_menu()
        elif pilihan == "3":
            search_contact_menu()
        elif pilihan == "4":
            delete_contact_menu()
        elif pilihan == "5":
            print("\nTerima kasih! Sampai jumpa 👋")
            break
        else:
            print("❌ Pilihan tidak valid, coba lagi.")


if __name__ == "__main__":
    main()
