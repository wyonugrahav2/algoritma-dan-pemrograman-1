"""
Modul Logika: Pengurutan Data (Sorting)
Pertemuan 8 - Algoritma Pencarian dan Pengurutan Data

Berisi implementasi Bubble Sort untuk mengurutkan data nilai
mahasiswa, baik secara ascending (nilai terendah -> tertinggi)
maupun descending (nilai tertinggi -> terendah / ranking).
"""


def bubble_sort_by_score(data: list[dict], descending: bool = True) -> list[dict]:
    """Mengurutkan list data mahasiswa berdasarkan nilai memakai Bubble Sort.

    Setiap iterasi membandingkan dua elemen bersebelahan dan menukarnya
    jika urutan salah, sehingga nilai "menggelembung" ke posisi yang tepat.

    Args:
        data: list of dict dengan key "nama" dan "nilai".
        descending: True untuk ranking (nilai tertinggi di atas),
            False untuk urutan ascending.

    Returns:
        list dict baru yang sudah terurut (data asli tidak diubah).
    """
    hasil = data.copy()
    n = len(hasil)

    for i in range(n - 1):
        for j in range(n - i - 1):
            if descending:
                harus_tukar = hasil[j]["nilai"] < hasil[j + 1]["nilai"]
            else:
                harus_tukar = hasil[j]["nilai"] > hasil[j + 1]["nilai"]

            if harus_tukar:
                hasil[j], hasil[j + 1] = hasil[j + 1], hasil[j]

    return hasil


def tambahkan_peringkat(data_terurut: list[dict]) -> list[dict]:
    """Menambahkan nomor peringkat (rank) pada data yang sudah terurut."""
    hasil = []
    for index, mhs in enumerate(data_terurut, start=1):
        mhs_dengan_rank = mhs.copy()
        mhs_dengan_rank["peringkat"] = index
        hasil.append(mhs_dengan_rank)
    return hasil
