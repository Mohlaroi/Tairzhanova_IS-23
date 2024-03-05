#В матрице элементы последнего
# столбца заменить на -1
import numpy as np
def zamena(matrix):
    for row in matrix:
        yield list(row[:-1]) + [-1]
matrix = np.random.randint (0, 20, (3, 3))
matrix2 = zamena(matrix)
print(matrix)

for row in matrix2:
    print(row)

