# Задание №3
# Реализуйте класс «Стадион». Необходимо хранить в полях класса: название стадиона, дату открытия,
# страну, город, вместимость. Реализуйте методы класса для ввода данных, вывода данных, реализуйте доступ
# к отдельным полям через методы класса.

import time


class Arena:
    def __init__(self):
        self.name = 'Japan National Stadium'
        self.open_date = '30 Nov 2019'
        self.country = 'Japan'
        self.city = 'Tokyo'
        self.count = 68000

    def get_info(self, choice):
        if choice == 1:
            print(self.name, self.open_date, self.country, self.city, self.count, sep=', ')
        elif choice == 2:
            print(self.name)
        elif choice == 3:
            print(self.open_date)
        elif choice == 4:
            print(self.country)
        elif choice == 5:
            print(self.city)
        elif choice == 6:
            print(self.count)


a = Arena()

while True:
    time.sleep(1)
    ch = input('1) - All info\n2) - Arena name\n3) - Open date\n4) - Country\n5) - City\n6) - Count\nChoice: ')
    try:
        a.get_info(int(ch))
        break
    except ValueError:
        print('Error value!')
