"""
Modul Pola & Iterasi (Pertemuan 4)
Menangani pembuatan pola piramida terbalik dan kalkulasi deret genap
menggunakan struktur perulangan for, range(), dan nested loop.
"""

def generate_reverse_pyramid(rows=5):
    """
    Menghasilkan pola piramida terbalik menggunakan nested loop (for).
    """
    result = []
    for i in range(rows, 0, -1):
        # Membuat spasi dan bintang sesuai baris
        spaces = " " * (rows - i)
        stars = "*" * (2 * i - 1)
        result.append(spaces + stars)
    return "\n".join(result)


def sum_even_numbers(n):
    """
    Menghitung jumlah dan total bilangan genap dari 1 hingga N.
    """
    even_list = []
    total = 0
    for num in range(1, n + 1):
        if num % 2 == 0:
            even_list.append(num)
            total += num
    return total, even_list