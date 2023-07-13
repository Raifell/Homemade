# Задание №1
# Используя понятие множественного наследования, разработайте класс «Окружность, вписанная в квадрат».

class Circle:
    def __init__(self):
        self.circle = 'Circle'


class Square(Circle):
    def __init__(self):
        super().__init__()
        self.square = 'Square'


class Figure(Square):
    def __str__(self):
        return f'Figure: [{self.circle}] in figure [{self.square}]'


a = Figure()
print(a)
