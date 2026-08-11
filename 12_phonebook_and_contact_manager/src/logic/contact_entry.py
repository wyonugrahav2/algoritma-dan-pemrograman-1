def validate_contact(nama: str, telepon: str, email: str) -> tuple[str, str, str]:
    """Memvalidasi data kontak. Melempar ValueError jika tidak valid."""
    nama = nama.strip()
    telepon = telepon.strip()
    email = email.strip() or "-"

    if not nama:
        raise ValueError("Nama tidak boleh kosong!")
    if "," in nama or "," in telepon or "," in email:
        raise ValueError("Data tidak boleh mengandung karakter koma (,).")
    if not telepon:
        raise ValueError("Nomor telepon tidak boleh kosong!")
    if not telepon.replace("+", "").replace("-", "").isdigit():
        raise ValueError("Nomor telepon hanya boleh berisi angka, '+', dan '-'.")

    return nama, telepon, email


def format_contact_line(nama: str, telepon: str, email: str) -> str:
    """Membentuk satu baris CSV: nama,telepon,email"""
    nama, telepon, email = validate_contact(nama, telepon, email)
    return f"{nama},{telepon},{email}\n"


def parse_contact_line(line: str) -> dict:
    """Mengurai satu baris CSV menjadi dictionary {nama, telepon, email}."""
    line = line.strip()
    parts = line.split(",")
    if len(parts) != 3:
        raise ValueError(f"Format baris kontak tidak valid: '{line}'")
    return {
        "nama": parts[0],
        "telepon": parts[1],
        "email": parts[2],
    }


def matches_keyword(contact: dict, keyword: str) -> bool:
    """Mengecek apakah sebuah kontak cocok dengan kata kunci pencarian."""
    keyword = keyword.lower().strip()
    gabungan = f"{contact['nama']} {contact['telepon']} {contact['email']}".lower()
    return keyword in gabungan
