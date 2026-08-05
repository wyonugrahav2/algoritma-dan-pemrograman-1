"""
Modul Logika: Geometri Bangun Ruang (3D)
Pertemuan 10 - Fungsi & Modularisasi

Berisi fungsi-fungsi volume untuk beberapa bangun ruang dasar.
Modul ini dipisah dari geometry_2d.py sebagai contoh penerapan
modularisasi: setiap file fokus pada satu tanggung jawab.
"""


def volume_kubus(sisi: float) -> float:
    """Menghitung volume kubus."""
    return sisi ** 3


def volume_balok(panjang: float, lebar: float, tinggi: float) -> float:
    """Menghitung volume balok."""
    return panjang * lebar * tinggi


def volume_tabung(jari_jari: float, tinggi: float, phi: float = 3.14) -> float:
    """Menghitung volume tabung (phi sebagai default parameter)."""
    return phi * jari_jari ** 2 * tinggi


def volume_bola(jari_jari: float, phi: float = 3.14) -> float:
    """Menghitung volume bola."""
    return (4 / 3) * phi * jari_jari ** 3
