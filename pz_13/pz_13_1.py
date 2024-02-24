#В матрице элементы последнего
# столбца заменить на -1
import numpy as np
def zamena(matrix, value):
    for row in matrix:
        row[-1] = value

#create NumPy matrix of random integers
matrix = np.random.randint (0, 20, (3, 3))

zamena(matrix, -1)

# Вывод измененной матрицы
for row in matrix:
    print(row)

