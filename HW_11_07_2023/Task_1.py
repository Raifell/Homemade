# Задание №1
# Напишите программу, в которой есть главный класс с текстовым полем. В главном классе должен быть метод для
# присваивания значения полю: без аргументов и с одним текстовым аргументом. Объект главного класса создаётся
# передачей одного текстового аргумента конструктору. На основе главного класса создается класс потомок.
# В классе-потомке нужно добавить числовое поле. У конструктора класса-потомка два аргумента.

class Main:
    def __init__(self, string):
        self.__string = string
        self.__empty = None
        self.__example = 'some string'

    def get_info(self):
        if len(self.__string) > 5:
            self.__empty = 'The length input string more than five'
        elif len(self.__string) == 5:
            self.__empty = 'The length input string is equal to five'
        else:
            self.__empty = 'The length input string less than five'
        print(f'Input string is: {self.__string}\n{self.__empty}')
        print()


class Side(Main):
    def __init__(self, string, integer):
        super().__init__(string)
        self.__string = string
        self.__integer = integer

    def get_info(self):
        print(f'Input string form main class: {self.__string}\nInput integer is: {self.__integer}')
        print()


ch_str = input('Enter string: ')
a = Main(ch_str)
a.get_info()

ch_int = int(input('Enter integer: '))
b = Side(ch_str, ch_int)
b.get_info()

# Данное задание выполнено с использованием полиморфизма, аргументы класса выполнены через инкапсуляцию.
