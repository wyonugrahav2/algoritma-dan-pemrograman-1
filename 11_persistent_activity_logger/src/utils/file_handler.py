import os

from src.logic.log_entry import format_log_entry, matches_keyword, parse_log_entry

LOG_FILE = os.path.join(os.path.dirname(__file__), "../../data/activity_log.txt")


def append_log(aktivitas: str, keterangan: str = "-") -> None:
    """Menambahkan satu baris log baru ke file (mode 'a' - append)."""
    entry_line = format_log_entry(aktivitas, keterangan)
    with open(LOG_FILE, "a", encoding="utf-8") as file:
        file.write(entry_line)


def read_all_logs() -> list[dict]:
    """Membaca seluruh isi log (mode 'r' - read), baris demi baris."""
    if not os.path.exists(LOG_FILE):
        return []

    entries = []
    try:
        with open(LOG_FILE, "r", encoding="utf-8") as file:
            for baris in file:
                if baris.strip():
                    entries.append(parse_log_entry(baris))
    except FileNotFoundError:
        return []
    return entries


def search_logs(keyword: str) -> list[dict]:
    """Mencari entri log yang mengandung kata kunci tertentu."""
    entries = read_all_logs()
    return [entry for entry in entries if matches_keyword(entry, keyword)]


def clear_logs() -> None:
    """Mengosongkan seluruh isi log (mode 'w' - overwrite/truncate)."""
    with open(LOG_FILE, "w", encoding="utf-8") as file:
        file.write("")
