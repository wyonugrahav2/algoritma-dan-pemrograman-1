def calculate_factorial(n: int) -> int:
    """Menghitung faktorial dari n (n!) menggunakan for loop."""
    if n < 0:
        raise ValueError("Angka tidak boleh negatif!")
    hasil = 1
    for i in range(1, n + 1):
        hasil *= i
    return hasil

def generate_power_table(limit: int = 5) -> list[dict]:
    """Menggenerasi data tabel bilangan, kuadrat, dan kubik."""
    table_data = []
    for i in range(1, limit + 1):
        table_data.append({
            "bilangan": i,
            "kuadrat": i ** 2,
            "kubik": i ** 3
        })
    return table_data