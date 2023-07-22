# Задание №2
# Реализуйте класс «Книга». Необходимо хранить в полях класса: название книги, год выпуска, издателя,
# жанр, автора, цену. Реализуйте методы класса для ввода данных, вывода данных, реализуйте доступ к
# отдельным полям через методы класса.

import time


class Book:
    def __init__(self):
        self.name = '"White Dragon"'
        self.year = '1978'
        self.publisher = 'Ballantine Books'
        self.genre = 'Science fiction (sci-fi)'
        self.author = 'Anne McCaffrey'
        self.price = 12

    def get_info(self, choice):
        if choice == 1:
            print(self.name, self.year, self.publisher, self.genre, self.author, self.price, sep=', ')
        elif choice == 2:
            print(self.name)
        elif choice == 3:
            print(self.year)
        elif choice == 4:
            print(self.publisher)
        elif choice == 5:
            print(self.genre)
        elif choice == 6:
            print(self.author)
        elif choice == 7:
            print(self.price)


a = Book()

while True:
    time.sleep(1)
    ch = input('1) - All info\n2) - Book name\n3) - Year\n4) - Publisher\n5) - Genre\n6) - Author\n7) - Price\nChoice: ')
    try:
        a.get_info(int(ch))
        break
    except ValueError:
        print('Error value!')
