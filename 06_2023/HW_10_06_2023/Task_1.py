# Задание №_1 Создайте массив словарей с 10 товарами со структурой имя товара, модель,
# цена (например телефоны). Выгрузите эти данные в CSV файл.

import csv

data = [] # Пусой список/сюда загружаем стартовые данные

with open('Task_1.txt', 'r') as file: # Открываем файл и добавляем из него данные в список [data]
    count = file.readlines()
    for line in count:
        data.append(line.split())


with open('Task_1.csv', 'w', newline='') as file: # Открываем/создаем файл Task_1.csv в формате записи
    writer = csv.writer(file) # Создаем переменную управления файлом
    writer.writerows(data) # Загружаем данные в файл построчно

with open('Task_1.csv', 'r') as file: # Открываем файл Task_1.csv в формате чтения
    result = csv.reader(file, delimiter=',') # Передаем результатсчитывания данных в переменную
    count_row = 0
    for i in result:
        if count_row == 0:
            print('Columns:', ' | '.join(i)) # Вывод в консоли первой строки с названиями колонок
        else:
            print(f'Row {count_row}:', ' | '.join(i)) # Вывод информации в остальных колонках построчно
        count_row += 1


# Для выполнения данной задачи, дополнительно создал файл Task_1.txt, данный файл содержит стартовую информацию
# для передачи в файл Task_1.csv
# Файл Task_1.csv будет создан автоматически, после запуска программы
