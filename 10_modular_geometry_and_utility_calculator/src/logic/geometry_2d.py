"""
Modul Logika: Geometri Bangun Datar (2D)
Pertemuan 10 - Fungsi & Modularisasi

Setiap bangun datar diwakili oleh sepasang fungsi (luas & keliling).
Modul ini mendemonstrasikan parameter positional dan parameter
default (mis. nilai phi pada lingkaran).
"""


def luas_persegi(sisi: float) -> float:
    """Menghitung luas persegi. return -> luas (float)."""
    return sisi ** 2


def keliling_persegi(sisi: float) -> float:
    """Menghitung keliling persegi."""
    return 4 * sisi


def luas_persegi_panjang(panjang: float, lebar: float) -> float:
    """Menghitung luas persegi panjang (dua parameter positional)."""
    return panjang * lebar


def keliling_persegi_panjang(panjang: float, lebar: float) -> float:
    """Menghitung keliling persegi panjang."""
    return 2 * (panjang + lebar)


def luas_segitiga(alas: float, tinggi: float) -> float:
    """Menghitung luas segitiga."""
    return 0.5 * alas * tinggi


def luas_lingkaran(jari_jari: float, phi: float = 3.14) -> float:
    """Menghitung luas lingkaran.

    `phi` memiliki nilai default 3.14 (default parameter), sehingga
    pemanggil boleh tidak menyertakannya jika nilai default sudah cukup.
    """
    return phi * jari_jari ** 2


def keliling_lingkaran(jari_jari: float, phi: float = 3.14) -> float:
    """Menghitung keliling lingkaran."""
    return 2 * phi * jari_jari
