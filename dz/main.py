def read_matrix_from_file(file_path):
    with open(file_path, 'r') as file:
        matrix = [list(map(int, line.split())) for line in file]
    return matrix

def find_min_in_column(matrix, k):
    min_value = float('inf')
    min_index = -1
    for i in range(len(matrix)):
        if matrix[i][k] < min_value:
            min_value = matrix[i][k]
            min_index = i
    return min_value, min_index

def sum_of_abs_elements(row):
    return sum(abs(x) for x in row)

# Основная логика программы
file_path = '1.txt'
matrix = read_matrix_from_file(file_path)

k = int(input("Введите номер столбца k (начиная с 0): "))

min_value, min_index = find_min_in_column(matrix, k)

print(f"Минимальный элемент в {k}-м столбце: {min_value}")

row_with_min = matrix[min_index]
sum_abs = sum_of_abs_elements(row_with_min)

print(f"Сумма модулей элементов в строке с минимальным элементом: {sum_abs}")
