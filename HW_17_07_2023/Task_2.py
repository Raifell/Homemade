# Задание №2
# Создайте класс Complex (комплексное число).
# Создайте перегруженные операторы для реализации арифметических операций
# для по работе с комплексными числами (операции +, -, *, /).

class Complex:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        value = other if isinstance(other, int) else other.num
        return Complex(self.num + value)

    def __sub__(self, other):
        value = other if isinstance(other, int) else other.num
        return Complex(self.num - value)

    def __mul__(self, other):
        value = other if isinstance(other, int) else other.num
        return Complex(self.num * value)

    def __truediv__(self, other):
        value = other if isinstance(other, int) else other.num
        if value != 0:
            if self.num / value % 2 == 0 or self.num / value % 2 == 1:
                return Complex(int(self.num / value))
            else:
                return Complex(self.num / value)
        else:
            print('Error, divide by zero!')
            return self.num

    def __str__(self):
        return str(self.num)


a = Complex(10)
b = Complex(2)

print('a = ', a)
a = a + 2
print('a(10) + 2 =', a)
a = a * b
print('a(12) * b(2) =', a)
a = a - 4
print('a(24) - 4 =', a)
a = a / 2
print('a(20) / 2 =', a)
a = a / 0
print('a not changed =', a)
