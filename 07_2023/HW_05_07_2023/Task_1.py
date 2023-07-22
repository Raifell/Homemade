# Задание №1
# Реализуйте класс «Автомобиль». Необходимо хранить в полях класса: название модели, год выпуска, производителя,
# объем двигателя, цвет машины, цену. Реализуйте методы класса для ввода данных, вывода данных, реализуйте доступ к
# отдельным полям через методы класса.

import time


class Car:
    def __init__(self):
        self.model = 'Ford'
        self.year = '2009'
        self.manufacturer = 'General Motors'
        self.drive = 1.6
        self.color = 'Black'
        self.price = 12000

    def get_info(self, choice):
        if choice == 1:
            print(self.model, self.year, self.manufacturer, self.drive, self.color, self.price, sep=', ')
        elif choice == 2:
            print(self.model)
        elif choice == 3:
            print(self.year)
        elif choice == 4:
            print(self.manufacturer)
        elif choice == 5:
            print(self.drive)
        elif choice == 6:
            print(self.color)
        elif choice == 7:
            print(self.price)


a = Car()

while True:
    time.sleep(1)
    ch = input('1) - All info\n2) - Model\n3) - Year\n4) - Manufacturer\n5) - Drive\n6) - Color\n7) - Price\nChoice: ')
    try:
        a.get_info(int(ch))
        break
    except ValueError:
        print('Error value!')
