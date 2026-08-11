import os

from src.logic.contact_entry import (
    format_contact_line,
    matches_keyword,
    parse_contact_line,
)

CONTACTS_FILE = os.path.join(os.path.dirname(__file__), "../../data/contacts.txt")


def load_contacts() -> list[dict]:
    """Membaca seluruh kontak dari file (mode 'r' - read), baris demi baris."""
    if not os.path.exists(CONTACTS_FILE):
        return []

    contacts = []
    try:
        with open(CONTACTS_FILE, "r", encoding="utf-8") as file:
            for baris in file:
                if baris.strip():
                    contacts.append(parse_contact_line(baris))
    except FileNotFoundError:
        return []
    return contacts


def add_contact(nama: str, telepon: str, email: str) -> None:
    """Menambahkan satu kontak baru ke file (mode 'a' - append)."""
    line = format_contact_line(nama, telepon, email)
    with open(CONTACTS_FILE, "a", encoding="utf-8") as file:
        file.write(line)


def search_contacts(keyword: str) -> list[dict]:
    """Mencari kontak yang mengandung kata kunci tertentu."""
    contacts = load_contacts()
    return [contact for contact in contacts if matches_keyword(contact, keyword)]


def delete_contact(telepon: str) -> bool:
    """
    Menghapus kontak berdasarkan nomor telepon.
    Membaca seluruh data, menyaring, lalu menulis ulang file (mode 'w' - overwrite).
    Mengembalikan True jika ada kontak yang dihapus.
    """
    contacts = load_contacts()
    sisa_kontak = [c for c in contacts if c["telepon"] != telepon.strip()]

    if len(sisa_kontak) == len(contacts):
        return False

    with open(CONTACTS_FILE, "w", encoding="utf-8") as file:
        for contact in sisa_kontak:
            file.write(f"{contact['nama']},{contact['telepon']},{contact['email']}\n")
    return True
