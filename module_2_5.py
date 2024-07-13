# Задание №1
def get_matrix(n, m, value):
    # Задание №2
    matrix = []
    # Задание №3
    for i in range(n):
        # Задание №4
        row = []
        # Задание №5
        for j in range(m):
            # Задание №6
            row.append(value)
        matrix.append(row)
    # Задание №7
    return matrix


# Задание №8
matrixx = get_matrix(3, 8, 1997)
print(matrixx)
