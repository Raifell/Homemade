# 1. Дан двумерный массив:
# а) Вывести на экран элемент, расположенный в правом верхнем углу массива.
# б) Вывести на экран элемент, расположенный в левом нижнем углу массива.

import numpy as np
import random

a = np.array([[random.randint(1, 10) for _ in range(5)] for _ in range(5)]).reshape(5, 5)

print(a)
print()
print('Upper left corner: ', a[0, 0])
print('Lower right corner: ', a[-1, -1])
