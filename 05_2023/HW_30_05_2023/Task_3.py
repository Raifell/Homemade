# Задание №_3 Класс Покупатель: Фамилия, Имя, Отчество, Адрес, Номер кредитной карточки,
# Номер банковского счета; Конструктор; Методы: установка значений атрибутов, получение значений атрибутов,
# вывод информации. Создать массив объектов данного класса. Вывести список покупателей в алфавитном порядке и
# список покупателей, у которых номер кредитной карточки находится в заданном диапазоне.

class Buyer:

    def __init__(self, surname, name, double_surname, address, pre_number, bank_number):
        self.surname = surname
        self.name = name
        self.double_surname = double_surname
        self.address = address
        self.pre_number = pre_number
        self.card_number = int(pre_number[12:]) # Номер кредитной карты закрыт, записываем последние 4 цифры
        self.bank_number = bank_number

    def get_info(self, maX=9999, miN=1000):
        if self.card_number < maX and self.card_number > miN:
            print('Покупатель:', '[' + self.surname, self.name, self.double_surname + ']', 'Адрес:', '[' + self.address
                  + ']', 'Номер карты:', '[' + self.pre_number + ']', 'Номер счета:', '[' + self.bank_number + ']')

    def create(self):
        return self.surname, self.name, self.double_surname, self.address, self.pre_number, self.bank_number


def choice(): # Функция выбора поиска по диапазону, возвращает True/False
    result = False
    print('(Если пропустить выбор, будет выведена вся картотека покупателей)')
    ch = input('Хотите выбрать диапазон номера кредитнойкарты? Y/N: ')
    ch = ch.lower()
    if ch == 'y':
        result = True
    return result


def check_fn(count): # Функция поиска по диапазону, возвращает maX/min/result
    print('(Поиск осуществляется по последним четырем цифрам карты)')
    while True:
        try:
            maX = int(input('Введите верхний диапазон: '))
            miN = int(input('Введите нижний диапазон: '))
            if len(str(maX)) < 4 or len(str(miN)) < 4:
                raise Exception()
        except:
            print('Введено неверное значение!')
        else:
            result = False
            for i in range(len(count)):
                f = count[i][4]
                search = int(f[12:])
                if search < maX and search > miN:
                    result = True
            return maX, miN, result


count = [] # Пустой список, сюда загружаем информацию из файла Task_3.txt

with open('Task_3.txt', 'r', encoding='utf-8') as f:
    file = f.readlines()
    for i in range(len(file)):
        vir_1 = file[i].split()
        vir_2 = Buyer(vir_1[0], vir_1[1], vir_1[2], vir_1[3], vir_1[4], vir_1[5])
        count.append(vir_2.create())

count = sorted(count) # Сортируем данные в списке в алфавитном порядке
choice = choice()

if choice == False:
    for i in range(len(count)):
        vir = Buyer(count[i][0], count[i][1], count[i][2], count[i][3], count[i][4], count[i][5])
        vir.get_info()
else:
    check = check_fn(count)
    if check[2] == True:
        for i in range(len(count)):
            vir = Buyer(count[i][0], count[i][1], count[i][2], count[i][3], count[i][4], count[i][5])
            vir.get_info(check[0], check[1])
    else:
        print('Поиск не дал результатов!')

# Для упрощения выполнения задачи, создал файл Task_3.txt, в нем хранится информация о покупателях,
# данные кредитных карт представил в формате ************1234, диапазон задается в пределах величины
# последних четырех цифр, что бы не забивать консоль лишней информацией, сначала предлагается осуществить
# поиск в пределах диапазона введенных чисел, если пропустить поиск, будет выведена информация обо всех
# имеющихся в системе покупателях.
