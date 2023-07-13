# Задание №1
# Создайте класс Device, который содержит информацию об устройстве. С помощью механизма наследования,
# реализуйте класс CoffeeMachine (содержит информацию о кофемашине),
# класс Blender (содержит информацию о блендере),
# класс MeatGrinder (содержит информацию о мясорубке).
# Каждый из классов должен содержать необходимые для работы методы.

class Device:
    def __init__(self, mark):
        self.mark = mark
        self.device = 'Home device'
        self.volt = '220V'


class CoffeeMachine(Device):
    def __init__(self, mark, color):
        super().__init__(mark)
        self.color = color

    def __str__(self):
        print('CoffeeMachine')
        return f'Device: {self.device}\nVoltage: {self.volt}\nMark: {self.mark}\nColor: {self.color}'


class Blender(Device):
    def __init__(self, mark, speed):
        super().__init__(mark)
        self.speed = speed

    def __str__(self):
        print('Blender')
        return f'Device: {self.device}\nVoltage: {self.volt}\nMark: {self.mark}\nSpeed count: {self.speed}'


class MeatGrinder(Device):
    def __init__(self, mark, blade):
        super().__init__(mark)
        self.blade = blade

    def __str__(self):
        print('Blender')
        return f'Device: {self.device}\nVoltage: {self.volt}\nMark: {self.mark}\nBlade variant: {self.blade}'


a = CoffeeMachine('Bosh', 'black')
b = Blender('Bosh', 2)
c = MeatGrinder('Bosh', 'Cross')

choice = input('1) - CoffeeMachine\n2) - Blender\n3) - MeatGrinder\nChoice: ')

if choice == '1':
    print(a)
elif choice == '2':
    print(b)
elif choice == '3':
    print(c)
else:
    print('Somthing go wrong.')
