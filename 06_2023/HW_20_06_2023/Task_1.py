# Задание №1
# а) Создайте json файл в операционной системе, заполните его данными с сайта https://jsonplaceholder.typicode.com/todos/
# б) Прочитайте этот файл в массив python-словарей.
# в) Запишите каждый из этих словарей в отдельный json-файл.

# Внимание! данный API предоставляет доступ к 200 значениям, чтобы не создавать в системе 200 файлов .json
# я реализовал вариант решения, с созданием 10 файлов и сортировкой записи в них по ключу "userId"

import json, requests

response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text) # Загружаем данные в переменную в формате json


json_name = [
    "file_1(id=1).json",
    "file_2(id=2).json",
    "file_3(id=3).json",
    "file_4(id=4).json",
    "file_5(id=5).json",
    "file_6(id=6).json",
    "file_7(id=7).json",
    "file_8(id=8).json",
    "file_9(id=9).json",
    "file_10(id=10).json"
]


def form(name, todos):
    count_id = [] # Список элементов по ключу "userId"
    count_list = [] # Плавающий список для передачи результата в count_file
    count_file = [] # Для каждого нового значения "userId", новый список внутри списка

    for x in todos: # Поиск и запись всех повторяющихся значений ключа "userId"
        if x["userId"] not in count_id:
            count_id.append(x["userId"])

    index = 0
    for x in todos: # Формирование общего списка для одинаковых значений ключа "userId" и передачей в count_file
        if x["userId"] in count_id:
            if count_id.index(x["userId"]) == index:
                count_list.append(x)

            else:
                index += 1
                count_file.append(count_list)
                count_list = []
                count_list.append(x)

    count_file.append(count_list) # Запись последнего загруженного списка в count_file

    for x in range(len(count_file)): # Запись каждого элемента count_file в отдельный файл
        with open(name[x], 'w') as file:
            json.dump(count_file[x], file, indent=2)


form(json_name, todos) # Вызов функции, аргументы: cписок с названиями файлов, данные json
