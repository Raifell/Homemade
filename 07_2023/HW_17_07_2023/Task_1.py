# Задание №1
# Создайте класс Circle (окружность). Для данного класса реализуйте ряд перегруженных операторов:
# Проверка на равенство радиусов двух окружностей (операция = =);
# Сравнения длин двух окружностей (операции >, <, <=,>=);
# Пропорциональное изменение размеров окружности, путем изменения ее радиуса (операции + - += -=).

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __ne__(self, other):
        return self.radius != other.radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __lt__(self, other):
        return self.radius < other.radius

    def __le__(self, other):
        return self.radius <= other.radius

    def __gt__(self, other):
        return self.radius > other.radius

    def __ge__(self, other):
        return self.radius >= other.radius

    def __add__(self, other):
        value = other if isinstance(other, int) else other.radius
        return Circle(self.radius + value)

    def __sub__(self, other):
        value = other if isinstance(other, int) else other.radius
        return Circle(self.radius - value)

    def __iadd__(self, other):
        value = other if isinstance(other, int) else other.radius
        self.radius += value
        return self

    def __isub__(self, other):
        value = other if isinstance(other, int) else other.radius
        self.radius -= value
        return self

    def __str__(self):
        return str(self.radius)


a = Circle(18)
b = Circle(19)
c = Circle(18)
d = Circle(2)

print('a(18) == c(18)', a == c)
print('a(18) == b(19)', a == b)
print('b(19) > c(18)', b > c)
print('a(18) >= c(18)', a >= c)
c = c + 2
print('c(18) + 2 =', c)
print('a(18) >= c(20)', a >= c)
c = c - 3
print('c(20) - 3 =', c)
print('a(18) >= c(17)', a >= c)
c = c + d
print('c(17) + d(2) =', c)
print('a(18) >= c(19)', a >= c)
c += d
print('c(19) += d(2)', c)
c -= 4
print('c(21) - 4 =', c)

