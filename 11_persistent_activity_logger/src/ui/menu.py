from src.utils.file_handler import append_log, clear_logs, read_all_logs, search_logs


def _print_entries(entries: list[dict]) -> None:
    if not entries:
        print("Tidak ada aktivitas untuk ditampilkan.")
        return

    print("\nWaktu\t\t\tAktivitas\t\tKeterangan")
    print("-" * 60)
    for entry in entries:
        print(f"{entry['timestamp']}\t{entry['aktivitas']}\t\t{entry['keterangan']}")


def add_activity_menu() -> None:
    print("\n--- 📝 Tambah Aktivitas Baru ---")
    aktivitas = input("Nama aktivitas: ")
    keterangan = input("Keterangan (opsional): ")

    try:
        append_log(aktivitas, keterangan)
        print("✅ Aktivitas berhasil dicatat!")
    except ValueError as e:
        print(f"❌ Gagal mencatat aktivitas: {e}")


def show_all_activity_menu() -> None:
    print("\n--- 📜 Riwayat Aktivitas ---")
    entries = read_all_logs()
    _print_entries(entries)


def search_activity_menu() -> None:
    print("\n--- 🔍 Cari Aktivitas ---")
    keyword = input("Masukkan kata kunci: ")
    hasil = search_logs(keyword)

    if not hasil:
        print(f"Tidak ditemukan aktivitas dengan kata kunci '{keyword}'.")
        return
    print(f"Ditemukan {len(hasil)} aktivitas:")
    _print_entries(hasil)


def clear_activity_menu() -> None:
    print("\n--- 🗑️ Hapus Semua Log Aktivitas ---")
    konfirmasi = input("Yakin ingin menghapus semua log? (y/n): ").strip().lower()

    if konfirmasi == "y":
        clear_logs()
        print("✅ Semua log aktivitas telah dihapus.")
    else:
        print("Dibatalkan.")
