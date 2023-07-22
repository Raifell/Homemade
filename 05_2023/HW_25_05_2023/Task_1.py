# Задание №_1 Программа, которая проверяет длину пароля. В случае если длина пароля меньше 8
# выбрасывать исключение. Проверять есть ли в пароле спецсимволы

print('Для создания пароля необходимо использовать минимум одну цифру, минимум один спецсимвол\n'
      'из списка: [! @ # $ % ^ & * / + , . - * _], так же условием создания является, минимум\n'
      'один символ в верхнем регистре.\n')

while True:
    passwords = input('Задайте пароль: ')
    count = len(passwords)
    ssymbol = ['!', '@', '#', '$', '%', '^', '&', '_', '.', ',', '/', '*', '-', '+']
    count_symbol = 0
    count_number = 0
    count_upper = 0

    try:
        if count < 8:
            raise Exception()
        else:
            for i in passwords:
                if i in ssymbol:
                    count_symbol += 1

        if count_symbol == 0:
            raise Exception()
        else:
            for i in passwords:
                if i.isdigit() == True:
                    count_number += 1

        if count_number == 0:
            raise Exception()
        else:
            for i in passwords:
                if i not in ssymbol:
                    if i.isdigit() == False:
                        if i == i.upper():
                            count_upper += 1

        if count_upper == 0:
            raise Exception()


    except Exception:
        print('Не соблюдены условия создания пароля!')

    else:
        print('Пароль успешно создан!')
        break


# По ходу выполнения задачи, так же добавил проверку на символ верхнего регистра, цикл этой проверки проходит
# только по тем элементам, которые не являются спецсимволами или цифрами.
# Исключения заданы самостоятельно, через raise Exception()
