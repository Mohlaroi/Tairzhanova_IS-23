#В матрице элементы второго столбца
# заменить элементами из одномерного
# динамического массива соответствующей размерности
import numpy as np
def zamena(matrix, array):
    for i in range(len(matrix)):
        matrix[i][1] = array[i]
        yield matrix[i]

matrix = np.random.randint (0, 20, (3, 3))
matrix2 = [1, 2, 3]
print(matrix)

new_matrix = zamena(matrix, matrix2)
for row in new_matrix:
    print(row)
