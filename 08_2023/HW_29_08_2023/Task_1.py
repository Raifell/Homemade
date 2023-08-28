# Заполнить одномерный массив случайными числами. Найти и вывести на экран наибольший
# его элемент и порядковый номер этого элемента
import numpy as np
import random

a = [random.randint(0, 10) for _ in range(len(np.arange(0, 30)))]
print('Список: ', a)
print('Максимальный элемент в списке: ', max(a))
print('Индекс(ы) максимального элемента: ', *[i for i in range(len(a)) if a[i] == max(a)])
