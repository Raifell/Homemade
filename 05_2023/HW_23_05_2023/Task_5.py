# Задача №_5 Создайте словарь, где ключами являются числа, а значениями – строки.
# Примените к нему метод items(), полученный объект dict_items передайте в написанную вами функцию,
# которая создает и возвращает новый словарь, "обратный" исходному, т. е. ключами являются строки,
# а значениями – числа.


myDict = dict({1: 'one', 2: 'two', 3: 'three', 4: 'four'}) # Изначальный словарь
ax = myDict.items() # Переменная, куда выгружаем dict_items


def new_dict(value): # Функция, принимает на вход словарь, возвращает новый словарь
    newDict = {}
    for i in value:
        newDict.update({i[-1]: i[0]})

    return print(newDict)


new_dict(ax) # Вызов функции