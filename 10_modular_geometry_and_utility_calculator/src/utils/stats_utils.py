"""
Modul Utilitas: Ringkasan Hasil Perhitungan
Pertemuan 10 - Fungsi & Modularisasi

Modul ini fokus mendemonstrasikan parameter *args (jumlah nilai
tidak tetap) dan **kwargs (pasangan label-nilai yang tidak tetap),
dipakai untuk merangkum hasil perhitungan geometri dalam satu sesi.
"""


def rata_rata(*nilai: float) -> float:
    """Menghitung rata-rata dari sejumlah nilai (parameter *args)."""
    if not nilai:
        return 0
    return sum(nilai) / len(nilai)


def nilai_tertinggi(*nilai: float) -> float:
    """Mencari nilai tertinggi dari sejumlah nilai (parameter *args)."""
    if not nilai:
        return 0
    tertinggi = nilai[0]
    for angka in nilai:
        if angka > tertinggi:
            tertinggi = angka
    return tertinggi


def ringkasan_hasil(**hasil_hitung: float) -> dict:
    """Merangkum beberapa hasil perhitungan geometri (parameter **kwargs).

    Args:
        **hasil_hitung: pasangan label=nilai, misalnya
            luas_persegi=25, volume_balok=60.

    Returns:
        dict berisi rata-rata, label hasil tertinggi, dan jumlah data.
    """
    if not hasil_hitung:
        return {"rata_rata": 0, "label_tertinggi": None, "jumlah_data": 0}

    nilai_list = list(hasil_hitung.values())
    label_tertinggi = max(hasil_hitung, key=hasil_hitung.get)

    return {
        "rata_rata": rata_rata(*nilai_list),
        "label_tertinggi": label_tertinggi,
        "nilai_tertinggi": hasil_hitung[label_tertinggi],
        "jumlah_data": len(hasil_hitung),
    }
