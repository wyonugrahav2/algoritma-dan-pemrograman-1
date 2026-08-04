"""
Modul Logika: Pencarian Data (Searching)
Pertemuan 8 - Algoritma Pencarian dan Pengurutan Data

Berisi implementasi Linear Search untuk mencari data mahasiswa
berdasarkan nama (parsial, tidak peka huruf besar/kecil) maupun
berdasarkan nilai yang persis sama.
"""


def linear_search_by_name(data: list[dict], kata_kunci: str) -> list[dict]:
    """Mencari mahasiswa berdasarkan nama menggunakan Linear Search.

    Program membandingkan kata kunci dengan nama setiap mahasiswa
    satu per satu dari elemen pertama hingga akhir list.

    Args:
        data: list of dict data mahasiswa.
        kata_kunci: potongan nama yang dicari.

    Returns:
        list mahasiswa yang namanya mengandung kata_kunci.
    """
    hasil = []
    kunci = kata_kunci.strip().lower()

    for mhs in data:
        if kunci in mhs["nama"].lower():
            hasil.append(mhs)

    return hasil


def linear_search_by_score(data: list[dict], nilai_target: int) -> list[dict]:
    """Mencari mahasiswa dengan nilai yang persis sama menggunakan Linear Search."""
    hasil = []

    for mhs in data:
        if mhs["nilai"] == nilai_target:
            hasil.append(mhs)

    return hasil
