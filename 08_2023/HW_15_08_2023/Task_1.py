# Задание №1
# а) Загрузите массив json – объектов с сайта jsonplaceholder, используя библиотеку requests.
# б) Сохраните циклом каждый в отдельный файл, в одну новую папку.

import requests
import json
from os import makedirs

url = 'https://jsonplaceholder.typicode.com/users'


def get_json(url):
    session = requests.session()
    response = session.get(url=url).json()
    return response


def main(li):
    for i in range(len(li)):
        path = f'Users/user-{li[i]["id"]}'
        makedirs(path, exist_ok=True)

        with open(f'{path}/file.json', 'w') as file:
            json.dump(li[i], file, indent=2)


if __name__ == '__main__':
    main(get_json(url))
