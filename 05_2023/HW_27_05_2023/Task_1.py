# Задание №_ 1Создать и заполнить файл случайными целыми значениями.
# Выполнить сортировку содержимого файла по возрастанию.

import random

myList = []  # Создаем пустой список и заполняем его цифровыми значениями
for i in range(random.randint(10, 20)):
    myList.append(random.randint(0, 15))

myList.sort()  # Сортируем список в порядке возрастания

newList = []  # Создаем новый писок, в него передаем значения из списка myList в строчном виде
for i in myList:
    newList.append(str(i))

with open('Task_1.txt', 'w') as f:  # Открываем/создаем файл Task_2.txt
    f.write(' '.join(newList))  # Записываем в файл информацию из списка newList, создав строку из содержимого
    # списка .join()

# Указывать закрытие файла нет необходимости, в такой конструкциифайл автоматически закрывается сам.