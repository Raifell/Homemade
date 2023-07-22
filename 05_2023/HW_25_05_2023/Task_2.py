# Задание №_2 Создать модуль конвертера температуры с функциями конвертации Цельсия в Фаренгейт,
# Цельсий в Кельвин, Фаренгейт в Цельсий и Кельвин в Цельсий.

import Task_2_fn as fn

print('1 = Цельсий\n2 = Фарингейт\n3 = Кельвин')

while True:
    count = 0
    try:
        count += int(input('Сделайте выбор: '))
        if count > 3:
            raise Exception()

    except (ValueError, Exception):
        print('Выберите из предложеных значений 1, 2, 3')

    else:
        if count == 1:
            print('Вы выбрали "Цельсий"')
            try:
                cel = int(input('Введите количество градусов: '))
            except ValueError:
                print('Некорректный ввод!')
            else:
                far, kel = fn.convertor(count, cel)
                print(cel, 'Цельсия =', far, 'Фарингейта')
                print(cel, 'Цельсия =', kel, 'Кельвина')
                break

        elif count == 2:
            print('Вы выбрали "Фарингейт"')
            try:
                far = int(input('Введите количество градусов: '))
            except ValueError:
                print('Некорректный ввод!')
            else:
                cel, kel = fn.convertor(count, far)
                print(far, 'Фарингейта =', cel, 'Цельсия')
                print(far, 'Фарингейта =', kel, 'Кельвина')
                break

        elif count == 3:
            print('Вы выбрали "Кельвин"')
            try:
                kel = int(input('Введите количество градусов: '))
            except ValueError:
                print('Некорректный ввод!')
            else:
                cel, far = fn.convertor(count, kel)
                print(kel, 'Кельвина =', cel, 'Цельсия')
                print(kel, 'Кельвина =', far, 'Фарингейта')
                break

# Для выполнения задания, создал файл Task_2_fn.py в нем находитсся функция конвертации,
# файл подключен к текущему файлу, через команду imporn Task_2_fn