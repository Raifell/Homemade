# Задача №_7 Строковый метод isdigit() проверяет, состоит ли строка только из цифр.
# Напишите программу, которая запрашивает с ввода два целых числа и выводит их сумму.
# В случае некорректного ввода программа не должна завершаться с ошибкой, а должна продолжать запрашивать.



while True:
    a = input("Введите число A: ")
    ax = a.isdigit()
    b = input("Введите число B: ")
    bx = b.isdigit()

    if ax == False or bx == False:
        print('Некорректный ввод, введите число!')
    else:
        result = int(a) + int(b)

        print('Сумма чисел А и B:', result)
        break


# В решении данной задачи, использовал цикл while, в случае, если проверка методом .isdigit() возвращает False,
# программа предложит повторно ввести значения чисел A и B