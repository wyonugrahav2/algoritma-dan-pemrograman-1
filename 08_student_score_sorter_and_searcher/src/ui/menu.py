"""
Modul UI: Menu Interaktif
Pertemuan 8 - Simulasi Ranking Nilai & Pencarian Data

Menghubungkan logika sorting & searching dengan input/output
pengguna di terminal (CLI).
"""

from src.logic.sorting import bubble_sort_by_score, tambahkan_peringkat
from src.logic.searching import linear_search_by_name, linear_search_by_score
from src.utils.data_handler import load_students, save_students, add_student


def tampilkan_tabel(data: list[dict], dengan_peringkat: bool = False) -> None:
    """Menampilkan data mahasiswa dalam bentuk tabel rapi di terminal."""
    if not data:
        print("Belum ada data mahasiswa.")
        return

    if dengan_peringkat:
        print(f"{'Rank':<6}{'Nama':<25}{'Nilai':<8}")
        print("-" * 39)
        for mhs in data:
            print(f"{mhs.get('peringkat', '-'):<6}{mhs['nama']:<25}{mhs['nilai']:<8}")
    else:
        print(f"{'Nama':<25}{'Nilai':<8}")
        print("-" * 33)
        for mhs in data:
            print(f"{mhs['nama']:<25}{mhs['nilai']:<8}")


def menu_tambah_data() -> None:
    print("\n--- ➕ Tambah Data Nilai Mahasiswa ---")
    data = load_students()

    nama = input("Masukkan nama mahasiswa: ").strip()
    try:
        nilai = int(input("Masukkan nilai (0-100): "))
    except ValueError:
        print("❌ Nilai harus berupa angka.")
        return

    data = add_student(data, nama, nilai)
    save_students(data)
    print(f"✅ Data '{nama}' dengan nilai {nilai} berhasil disimpan.")


def menu_ranking() -> None:
    print("\n--- 📊 Ranking Nilai Mahasiswa (Bubble Sort) ---")
    data = load_students()

    if not data:
        print("Belum ada data mahasiswa. Silakan tambah data terlebih dahulu.")
        return

    print("1. Urutkan Tertinggi -> Terendah (Ranking)")
    print("2. Urutkan Terendah -> Tertinggi")
    pilihan = input("Pilih mode urutan (1/2): ")

    descending = pilihan != "2"
    hasil_sort = bubble_sort_by_score(data, descending=descending)
    hasil_dengan_rank = tambahkan_peringkat(hasil_sort)

    print()
    tampilkan_tabel(hasil_dengan_rank, dengan_peringkat=True)


def menu_cari_data() -> None:
    print("\n--- 🔎 Cari Data Mahasiswa (Linear Search) ---")
    data = load_students()

    if not data:
        print("Belum ada data mahasiswa. Silakan tambah data terlebih dahulu.")
        return

    print("1. Cari berdasarkan Nama")
    print("2. Cari berdasarkan Nilai")
    pilihan = input("Pilih metode pencarian (1/2): ")

    if pilihan == "1":
        kata_kunci = input("Masukkan nama (boleh sebagian): ")
        hasil = linear_search_by_name(data, kata_kunci)
    elif pilihan == "2":
        try:
            nilai_target = int(input("Masukkan nilai yang dicari: "))
        except ValueError:
            print("❌ Nilai harus berupa angka.")
            return
        hasil = linear_search_by_score(data, nilai_target)
    else:
        print("❌ Pilihan tidak valid.")
        return

    print()
    if hasil:
        print(f"✅ Ditemukan {len(hasil)} data:")
        tampilkan_tabel(hasil)
    else:
        print("❌ Data tidak ditemukan.")


def menu_tampilkan_semua() -> None:
    print("\n--- 📋 Seluruh Data Mahasiswa ---")
    data = load_students()
    tampilkan_tabel(data)


def main_menu() -> None:
    while True:
        print("\n==========================================")
        print("📊 Simulasi Ranking Nilai & Pencarian Data")
        print("==========================================")
        print("1. ➕ Tambah Data Nilai Mahasiswa")
        print("2. 📊 Tampilkan Ranking (Bubble Sort)")
        print("3. 🔎 Cari Mahasiswa (Linear Search)")
        print("4. 📋 Tampilkan Semua Data")
        print("5. 🚪 Keluar")
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            menu_tambah_data()
        elif pilihan == "2":
            menu_ranking()
        elif pilihan == "3":
            menu_cari_data()
        elif pilihan == "4":
            menu_tampilkan_semua()
        elif pilihan == "5":
            print("\nTerima kasih! Sampai jumpa 👋")
            break
        else:
            print("❌ Pilihan tidak valid, coba lagi.")
