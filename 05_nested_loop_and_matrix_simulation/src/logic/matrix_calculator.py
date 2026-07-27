def generate_multiplication_table(n):
    """Generasi tabel perkalian N x N menggunakan nested loop."""
    table = []
    for i in range(1, n + 1):
        row = []
        for j in range(1, n + 1):
            row.append(i * j)
        table.append(row)
    return table

def render_matrix(matrix):
    """Mengubah list 2D (matriks) menjadi tampilan string grid yang rapi."""
    output = ""
    for row in matrix:
        for val in row:
            output += f"{val:<4}"
        output += "\n"
    return output.strip()