import numpy as np

matrix = np.empty((3, 3), dtype=int)

value = 2
for i in range(3):
    for j in range(3):
        matrix[i, j] = value
        value += 1

print(matrix)