# задание №_1 Написать программу, которая будет проверять, является ли введенное число трехзначным,
# поиск результата осуществить, через функцию

def search_number():                            # Функция
    x = int(input('Введите простое число: '))

    if len(str(x)) == 3:                        # Результат, если число трехзначное
        print('Число:', x, 'трехзначное!')
    else:                                       # Резултат, если число не трехзначное
        print('Число', x, 'не трехзначное!')


search_number()         # Вызов функции