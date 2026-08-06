from datetime import datetime

SEPARATOR = " | "


def validate_activity(aktivitas: str) -> str:
    """Memvalidasi input aktivitas. Melempar ValueError jika tidak valid."""
    aktivitas = aktivitas.strip()
    if not aktivitas:
        raise ValueError("Aktivitas tidak boleh kosong!")
    if SEPARATOR.strip() in aktivitas:
        raise ValueError("Aktivitas tidak boleh mengandung karakter '|'.")
    return aktivitas


def format_log_entry(aktivitas: str, keterangan: str = "-") -> str:
    """Membentuk satu baris log dengan format: timestamp | aktivitas | keterangan"""
    aktivitas = validate_activity(aktivitas)
    keterangan = keterangan.strip() or "-"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"{timestamp}{SEPARATOR}{aktivitas}{SEPARATOR}{keterangan}\n"


def parse_log_entry(line: str) -> dict:
    """Mengurai satu baris log menjadi dictionary {timestamp, aktivitas, keterangan}."""
    line = line.strip()
    parts = line.split(SEPARATOR)
    if len(parts) != 3:
        raise ValueError(f"Format baris log tidak valid: '{line}'")
    return {
        "timestamp": parts[0],
        "aktivitas": parts[1],
        "keterangan": parts[2],
    }


def matches_keyword(entry: dict, keyword: str) -> bool:
    """Mengecek apakah sebuah entri log cocok dengan kata kunci pencarian."""
    keyword = keyword.lower().strip()
    gabungan = f"{entry['aktivitas']} {entry['keterangan']}".lower()
    return keyword in gabungan
