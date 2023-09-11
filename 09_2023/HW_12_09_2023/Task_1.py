# Напишите программу, в которой есть главный класс с текстовым полем. В главное классе должен быть метод для
# присваивания значения полю: без аргументов и с одним текстовым аргументом. Объект главного класса создаётся
# передачей одного текстового аргумента конструктору. На основе главного класса создается класса потомок.
# В классе-потомке нужно добавить числовое поле. У конструктора класса-потомка два аргумента.
import random


class Main:
    def __init__(self):
        self.string = input('Enter string: ')
        self.find = None


class Side(Main):
    def __init__(self):
        self.number = random.randint(1000, 9999)
        super().__init__()

    def __str__(self):
        return f'String :"{self.string}" from Main class\nNumber: {self.number} from Side class'


a = Side()
print(a)
