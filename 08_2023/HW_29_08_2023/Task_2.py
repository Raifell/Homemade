# В массиве, содержащем положительные и отрицательные целые числа, вычислить сумму четных положительных элементов.
import numpy as np
import random

a = [random.randint(-10, 10) for _ in range(len(np.arange(0, 30)))]
print('Список: ', a)
print('Сумма четных, положительных элементов: ', sum([x for x in a if x > 0 and x % 2 == 0]))
