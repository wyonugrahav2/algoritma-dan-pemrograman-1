from src.utils.file_handler import (
    add_contact,
    delete_contact,
    load_contacts,
    search_contacts,
)


def _print_contacts(contacts: list[dict]) -> None:
    if not contacts:
        print("Tidak ada kontak untuk ditampilkan.")
        return

    print("\nNama\t\tTelepon\t\tEmail")
    print("-" * 55)
    for contact in contacts:
        print(f"{contact['nama']}\t\t{contact['telepon']}\t\t{contact['email']}")


def add_contact_menu() -> None:
    print("\n--- ➕ Tambah Kontak Baru ---")
    nama = input("Nama: ")
    telepon = input("Nomor telepon: ")
    email = input("Email (opsional): ")

    try:
        add_contact(nama, telepon, email)
        print("✅ Kontak berhasil disimpan!")
    except ValueError as e:
        print(f"❌ Gagal menyimpan kontak: {e}")


def show_all_contacts_menu() -> None:
    print("\n--- 📇 Daftar Semua Kontak ---")
    contacts = load_contacts()
    _print_contacts(contacts)


def search_contact_menu() -> None:
    print("\n--- 🔍 Cari Kontak ---")
    keyword = input("Masukkan nama/telepon/email: ")
    hasil = search_contacts(keyword)

    if not hasil:
        print(f"Tidak ditemukan kontak dengan kata kunci '{keyword}'.")
        return
    print(f"Ditemukan {len(hasil)} kontak:")
    _print_contacts(hasil)


def delete_contact_menu() -> None:
    print("\n--- 🗑️ Hapus Kontak ---")
    telepon = input("Masukkan nomor telepon yang ingin dihapus: ")

    if delete_contact(telepon):
        print("✅ Kontak berhasil dihapus.")
    else:
        print(f"❌ Kontak dengan nomor '{telepon}' tidak ditemukan.")
