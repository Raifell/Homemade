# Задание №4
# Создать класс Flat (квартира). Реализовать перегруженные операторы:
# Проверка на равенство площадей квартир (операция ==);
# Проверка на неравенство площадей квартир (операция !=);
# Сравнение двух квартир по цене (операции > < <= >=).

class Flat:
    def __init__(self, square, price):
        self.square = square
        self.price = price

    def __eq__(self, other):
        if self.square == other.square:
            return True
        else:
            return False

    def __ne__(self, other):
        if self.square != other.square:
            return True
        else:
            return False

    def __lt__(self, other):
        return self.price < other.price

    def __le__(self, other):
        return self.price <= other.price

    def __gt__(self, other):
        return self.price > other.price

    def __ge__(self, other):
        return self.price >= other.price

    def __str__(self):
        return f'Flat square: {self.square}\nPrice: {str(self.price) + " $"}\n'


a = Flat(50, 70000)
b = Flat(40, 55000)

print(a)
print(b)
print(a == b)
print(a != b)
print(a > b)
print(a < b)
