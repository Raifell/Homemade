# Дан двумерный массив. Составить программу:
# а) расчета суммы двух любых элементов второй строки массива;
# б) расчета произведения главной диагонали матрица.

import numpy as np
import random

a = np.array([[random.randint(1, 10) for _ in range(5)] for _ in range(5)]).reshape(5, 5)
b = random.sample(range(0, 4), 2)
c = sum([a[x, x] for x in range(len(a))])

print(a)
print()
print('Sum of elements of the second row by indexes: ', f'{b}\n', 'Result: ', sum(a[1][b]), sep='')
print('The sum of the elements of the main diagonal of the matrix: ', c)
