# Задание №2
# Создайте класс Ship, который содержит информацию о корабле. С помощью механизма наследования,
# реализуйте класс Frigate (содержит информацию о фрегате),
# класс Destroyer (содержит информацию об эсминце), класс Cruiser (содержит информацию о крейсере).
# Каждый из классов должен содержать необходимые для работы методы.

class Ship:
    def __init__(self, navy):
        self.navy = navy


class Frigate(Ship):
    def __init__(self, navy, speed):
        super().__init__(navy)
        self.speed = speed

    def __str__(self):
        print('Frigate')
        return f'Fleet: {self.navy}\nSpeed: {self.speed}'


class Destroyer(Ship):
    def __init__(self, navy, artillery):
        super().__init__(navy)
        self.artillery = artillery

    def __str__(self):
        print('Destroyer')
        return f'Fleet: {self.navy}\nArtillery barrels: {self.artillery}'


class Cruiser(Ship):
    def __init__(self, navy, rocket):
        super().__init__(navy)
        self.rocket = rocket

    def __str__(self):
        print('Cruiser')
        return f'Device: {self.navy}\nCount rockets: {self.rocket}'


a = Frigate('United States Fifth Fleet', '20ch')
b = Destroyer('United States Fifth Fleet', 24)
c = Cruiser('United States Fifth Fleet', 28)

choice = input('1) - Frigate\n2) - Destroyer\n3) - Cruiser\nChoice: ')

if choice == '1':
    print(a)
elif choice == '2':
    print(b)
elif choice == '3':
    print(c)
else:
    print('Somthing go wrong.')
