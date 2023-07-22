# Задание №3
# Создайте базовый класс Shape для рисования плоских фигур.
# Определите методы:
# Show() — вывод на экран информации о фигуре;
# Save() — сохранение фигуры в файл;
# Load() — считывание фигуры из файла.
# Определите производные классы:
# Square — квадрат, который характеризуется координатами левого верхнего угла и длиной стороны;
# Rectangle — прямоугольник с заданными координатами верхнего левого угла и размерами;

class Shape:
    def __init__(self, x=None, y=None, a=None, b=None):
        self.x = x
        self.y = y
        self.a = a
        self.b = b
        self.value = None
        self.read = None

    def show_f(self):
        if self.b:
            print('Rectangle shape')
            print(f'Coord X: {self.x}')
            print(f'Coord Y: {self.y}')
            print(f'Length A: {self.a}')
            print(f'Length B: {self.b}')
            print()
        else:
            print('Square shape')
            print(f'Coord X: {self.x}')
            print(f'Coord Y: {self.y}')
            print(f'Length A: {self.a}')
            print()

    def save_f(self):
        if self.b:
            self.value = [f'Coord X: {self.x}', f'Coord Y: {self.y}', f'Length A: {self.a}', f'Length B: {self.b}']
            with open('Rectangle.txt', 'w') as file:
                for x in self.value:
                    file.write(x + '\n')
                print('Rectangle shape saved')
                print()
        else:
            self.value = [f'Coord X: {self.x}', f'Coord Y: {self.y}', f'Length A: {self.a}']
            with open('Square.txt', 'w') as file:
                for x in self.value:
                    file.write(x + '\n')
                print('Square shape saved')
                print()

    def load_f(self):
        if self.b:
            with open('Rectangle.txt', 'r') as file:
                self.read = file.read()
                print('Rectangle shape loaded')
                print(self.read)
        else:
            with open('Square.txt', 'r') as file:
                self.read = file.read()
                print('Square shape loaded')
                print(self.read)




class Square(Shape):
    def __init__(self, x, y, a):
        super().__init__(x, y, a)


class Rectangle(Shape):
    def __init__(self, x, y, a, b):
        super().__init__(x, y, a, b)


s = Square(0, 1, 2)
s.show_f()
s.save_f()
s.load_f()

r = Rectangle(0, 1, 2, 3)
r.show_f()
r.save_f()
r.load_f()

