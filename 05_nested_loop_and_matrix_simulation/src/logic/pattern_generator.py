def generate_triangle(rows):
    """Membuat pola segitiga siku-siku bintang."""
    pattern = ""
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            pattern += "*"
        pattern += "\n"
    return pattern.strip()

def generate_inverted_triangle(rows):
    """Membuat pola segitiga terbalik."""
    pattern = ""
    for i in range(rows, 0, -1):
        for j in range(i):
            pattern += "*"
        pattern += "\n"
    return pattern.strip()

def generate_number_pyramid(rows):
    """Membuat pola angka berurutan."""
    pattern = ""
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            pattern += f"{j} "
        pattern += "\n"
    return pattern.strip()