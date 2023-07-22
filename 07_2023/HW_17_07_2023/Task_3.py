# Задание №3
# Вам необходимо создать класс Airplane (самолет).
# С помощью перегрузки операторов реализовать:
# Проверка на равенство типов самолетов (операция = =);
# Увеличение и уменьшение пассажиров в салоне самолета (операции + - += -=);
# Сравнение двух самолетов по максимально возможному количеству пассажиров на борту (операции > < <= >=).

class Airplane:
    def __init__(self, model, place, count):
        self.model = model
        self.place = place
        self.count = count

    def __eq__(self, other):
        if self.model == other.model:
            return True
        else:
            return False

    def __add__(self, other):
        value = other if isinstance(other, int) else other.place
        return Airplane(self.model, self.place + value, self.count)

    def __sub__(self, other):
        value = other if isinstance(other, int) else other.place
        return Airplane(self.model, self.place - value, self.count)

    def __iadd__(self, other):
        value = other if isinstance(other, int) else other.place
        self.place += value
        return self

    def __isub__(self, other):
        value = other if isinstance(other, int) else other.place
        self.place -= value
        return self

    def __lt__(self, other):
        return self.count < other.count

    def __le__(self, other):
        return self.count <= other.count

    def __gt__(self, other):
        return self.count > other.count

    def __ge__(self, other):
        return self.count >= other.count

    def __str__(self):
        return f'Model: {self.model}\nPassengers: {self.place}\nPlaces: {self.count}\n'


a = Airplane('Concord', 12, 60)
b = Airplane('Boing 747', 50, 180)
c = Airplane('Boing 747', 80, 180)

print(a)
print(b)
print(c)
print('Concord == Boing 747\n', a == b, '\n')
print('Boing 747 == Boing 747\n', b == c, '\n')
a = a + 8
print(a)
a = a - 2
print(a)
a += 4
print(a)
a -= 2
print(a)
print(a > b)
print(b > a)
