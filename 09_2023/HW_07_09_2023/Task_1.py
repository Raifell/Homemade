# Задание №1
# Создайте класс Roman (РимскоеЧисло), представляющий римское число и поддерживающий операции +, -, *, /.
# При реализации класса:
# операции +, -, *, / реализуйте как специальные методы
# методы преобразования как статические методы.


class Roman:
    def __init__(self, num):
        self.num = self.check(num)
        self.arr = {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX', 10: 'X',
                    0: 'Nulla', 'e': 'Not int type'}
        self.rom = self.get_roman(self.num, self.arr)

    def __add__(self, other):
        value = other if isinstance(other, int) else other.num
        return Roman(self.num + value)

    def __sub__(self, other):
        value = other if isinstance(other, int) else other.num
        return Roman(self.num - value)

    def __mul__(self, other):
        value = other if isinstance(other, int) else other.num
        return Roman(self.num * value)

    def __truediv__(self, other):
        value = other if isinstance(other, int) else other.num
        return Roman(self.num / value) if value > 0 else "Can't divide by zero"

    def __str__(self):
        return self.rom

    @staticmethod
    def check(num):
        return num if num == int(num) else 'e'

    @staticmethod
    def get_roman(num, ar):
        if num in [x for x in ar]:
            return ar[num]
        else:
            dec = num // 10
            ren = num % 10
            return f'{ar[10]*dec}{ar[ren]}'

a = Roman(6)
b = Roman(2)
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print()
a = Roman(4)
b = Roman(0)
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print()
a = Roman(3)
b = Roman(2)
print(a / b)
