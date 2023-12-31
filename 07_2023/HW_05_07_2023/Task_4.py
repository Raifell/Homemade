# Задание №4
# Напишите программу, в которой есть главный класс с текстовым полем. В главном классе должен быть метод для
# присваивания значения полю: без аргументов и с одним текстовым аргументом. Объект главного класса создаётся
# передачей одного текстового аргумента конструктору. На основе главного класса создается класс потомок.
# В классе-потомке нужно добавить числовое поле. У конструктора класса-потомка два аргумента.

class Main:
    def __init__(self, string):
        self.string = string
        self.empty = None
        self.example = 'some string'

    def get_info(self):
        if len(self.string) > 5:
            self.empty = 'The length string more than five'
        elif len(self.string) == 5:
            self.empty = 'The length string is equal to five'
        else:
            self.empty = 'The length string less than five'
        print(f'{self.string}\n{self.empty}')


class Side(Main):
    def __init__(self, integer):
        super().__init__(self)
        self.integer = integer

    def get_result(self):
        print(self.integer)
        print(self.example)


ch_str = input('Enter string: ')
a = Main(ch_str)
a.get_info()

ch_int = int(input('Enter integer: '))
b = Side(ch_int)
b.get_result()

