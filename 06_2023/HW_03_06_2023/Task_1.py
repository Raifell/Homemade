# Задание №_1 Создать консольное приложение с использованием базы данных на тему «Телефонной книги».
# • Создать таблицу с полями id, name (имя), phone (номер телефона), count_call (количество звонков),
# date_last_call (дата последнего звонка)
# • Реализовать функции добавления, редактирования и удаления записей.
# • Реализовать функции для вызова абонента, которая будет при каждом вызове прибавлять единицу к count_call
# и изменять дату последнего звонка на текущий.


import time, sqlite3 as sql # Импортируем библиотеки time и sqlite3


def choice(vir, defolt): # Функция выбора, адаптирована под выбор всех значений предложеных в программе
    if vir == 0:
        print(f'1 - Показать все данные в базе данных.\n2 - Тест звонка.\n'
              f'3 - Тест удаления данных.\n4 - Тест добавления данных')
        while True:
            choice_1 = input('Сделайте выбор: ')
            try:
                choice_1 = int(choice_1)
                if choice_1 > 4:
                    raise Exception()
            except:
                print('Выберите из значений предложеных выше.')
            else:
                return choice_1
    elif vir == 1:
        print(f'Выберите номер ID, для тестового звонка (1-{defolt})')
        while True:
            choice_2 = input('Сделайте выбор: ')
            try:
                choice_2 = int(choice_2)
                if choice_2 > defolt:
                    raise Exception()
            except:
                print('Выберите из значений предложеных выше.')
            else:
                return choice_2


def defolt_conection():
    db = sql.connect('orders.db')  # Подключение к БД
    cur = db.cursor()  # Создание переменной управления БД
    cur.execute("SELECT * FROM phone_book;")  # Запрос вывода всей имеющейся информации в БД
    res = cur.fetchall()  # Загрузка всей имеющейся в БД информации в переменную
    db.close()
    result = 0
    for i in res:
        result += 1
    return result


def view_out(vir, con): # Функция вывода данных из БД, а так же перезаписи данных
    ct = time.strftime("%H:%M:%S", time.localtime()) # Переменная с текущим временем
    db = sql.connect('orders.db') # Подключение к БД
    cur = db.cursor() # Создание переменной управления БД
    cur.execute("SELECT * FROM phone_book;") # Запрос вывода всей имеющейся информации в БД
    result = cur.fetchall() # Загрузка всей имеющейся в БД информации в переменную
    if vir == 0 and con == 0:
        db.close() # Закрытие БД
        return result # Результат - вывод всей информации
    elif vir != 0 and con == 0:
        for i in range(len(result)):
            if result[i][0] == vir: # Поиск конкретного положения в БД
                update = """UPDATE phone_book SET count_call = ?, date_last_call = ? WHERE id = ?;"""
                data = (result[i][3] + 1, ct, vir) # Данные для обновления представлены в формате tuple(
                cur.execute(update, data) # Изменение установленых значений в БД
                db.commit() # Применение изменений
                db.close() # Закрытие БД
                return f'Изменены значения в БД, у пользователя №_{result[i][0]}, Name: {result[i][1]}\n' \
                       f'Значение совершенных звонков: {data[0]}, Время последнего звонка: {ct}'
    elif vir == 0 and con != 0:
        dell = """DELETE FROM phone_book WHERE id = ?;"""
        dell_data = (result[len(result)-1][0],)
        cur.execute(dell, dell_data)
        db.commit()
        db.close()
        return 'Из БД удалены данные последнего пользователя.'
    else:
        add = """INSERT INTO phone_book VALUES(?, ?, ?, ?, ?);"""
        add_date = (result[len(result)-1][0] + 1, 'Peter', 123327, 1, '12:30:00')
        cur.execute(add, add_date)
        db.commit()
        db.close()
        return f"В БД добавлены данные о новом пользователе, ID:{result[len(result) - 1][0] + 1}," \
               f"Name: 'Peter', Number: 123327, Count call: 1, Last call: '12:30:00')"



#--------------------------------------- Блок внизу создает базу данных ------------------------------------

# users_data = []
#
# with open('users.txt', 'r') as f:
#     count = f.readlines()
#     for i in range(len(count)):
#         users_data.append(tuple(count[i].split()))
#
#
# db = sql.connect('orders.db')
# cur = db.cursor()
#
# cur.execute("""CREATE TABLE IF NOT EXISTS phone_book(
#    id INT PRIMARY KEY,
#    name TEXT,
#    phone INT,
#    count_call INT,
#    date_last_call TEXT);
# """)
# db.commit()
#
# cur.executemany("INSERT INTO phone_book VALUES(?, ?, ?, ?, ?);", users_data)
# db.commit()
# db.close()

#-------------------------------------------------Конец блока---------------------------------------------

a = defolt_conection()

choice_one = choice(0, a) # Выбор из предложеных вариантов
if choice_one == 1:
    all = view_out(0, 0)
    for i in range(len(all)):
        print('ID', all[i][0], 'Name:', all[i][1], 'Number:', all[i][2], 'Count:', all[i][3], 'Last call:', all[i][4])
elif choice_one == 2:
    choice_two = choice(1, a) # Выбор конкретного пользователя для изменения его данных
    reset_one = view_out(choice_two, 0)
    print(reset_one)
elif choice_one == 3:
    reset_two = view_out(0, 1)
    print(reset_two)
else:
    reset_three = view_out(1, 1)
    print(reset_three)

# Для выполнения этой задачи, создал файл users.txt в этом файле хранится информация о всех имеющихся пользователях,
# информацию из этого файла загружаем в БД, блок создания и загрузки данных в БД закоментирован.
# По умолчанию у всех пользователей одинаковые значения количества звонков и дата последнего звонка, в
# процессе использования программы данные в БД будут изменены, при соблюдении условий.
