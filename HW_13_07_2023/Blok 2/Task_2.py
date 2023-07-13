# Задание №2
# Используя механизм множественного наследования разработайте класс “Автомобиль”.
# Должны быть классы «Колеса», «Двигатель», «Двери».

class Wheels:
    def __init__(self, wheel):
        self.wheel = wheel


class Drive(Wheels):
    def __init__(self, wheel, drive):
        super().__init__(wheel)
        self.drive = drive


class Doors(Drive):
    def __init__(self, wheel, drive, doors):
        super().__init__(wheel, drive)
        self.doors = doors


class Car(Doors):
    def __init__(self, wheel, drive, doors, mark, model):
        super().__init__(wheel, drive, doors)
        self.mark = mark
        self.model = model

    def __str__(self):
        return f'Car: {self.mark}\nModel: {self.model}\n' \
               f'Count wheels: {self.wheel}\nDrive: {self.drive}\nDoors: {self.doors}'


a = Car(4, 1.2, 5, 'Volkswagen', 'Polo')
print(a)

