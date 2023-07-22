# Задание №_1 Создайте структуру с именем train, содержащую поля: название пункта назначения,
# номер поезда, время отправления. Ввести данные в массив из пяти элементов типа train,
# упорядочить элементы по номерам поездов. Добавить возможность вывода информации о поезде,
# номер которого введен пользователем

class Train:

    def __init__(self, number=0, station='', time=''): # Конструктор класса
        self.number = number
        self.station = station
        self.time = time

    def train(self): # Вывод информации через print()
        if self.number != 0:
            print('№_Поезда:', self.number, 'Станция:', '(' + self.station + ')', 'Время отправления:', self.time)
        else:
            print('По вашему запросу не найдено результатов!')

    def test(self): # Вывод информации tuple()
        return self.number, self.station, self.time


def choice(): # Функция выбора поиска по номеру, возвращает True/False
    result = False
    print('(Если пропустить выбор, будет выведен весь список поездов)')
    ch = input('Хотите выбрать номер поезда? Y/N: ')
    ch = ch.lower()
    if ch == 'y':
        result = True
    return result


def check_fn(check, count): # Функция поиска по номеру, возвращает None/tuple()
    for i in range(len(count)):
        if check == count[i][0]:
            return count[i]


numbers = [54, 53, 52, 51, 55, 56] # Список с номерами
station = ['Аккурган', 'Бекабад', 'Газалкент', 'Дустабад', 'Келес', 'Нурафшон'] # Список со станциями
times = ['15:30', '14:30', '13:30', '12:30', '16:30', '17:30'] # Список с временем отправления
trains = [] # Список, куда добавляем объекты на основе данных предидущих трех списков

for i in range(len(numbers)): # Цикл добавляет объекты в список
    result = Train(numbers[i], station[i], times[i])
    trains.append(result.test())

trains = sorted(trains) # Сортировка списка по номеру поезда
choice = choice()
if choice == False: # Результат, если поиск по номеру был отклонен
    for i in range(len(trains)):
        a = Train(trains[i][0], trains[i][1], trains[i][2])
        a.train()
else: # Результат, если был выбран поиск по номеру
    while True:
        try:
            check = int(input('Введите номер поезда: '))
        except:
            print('Неверное значение!')
        else:
            check = check_fn(check, trains)
            if check == None: # Результат, еслипоиск не дал результата
                a = Train()
                a.train()
                break
            else: # Результат, если номер введенный пользователем, совпадает с номером в списке
                a = Train(check[0], check[1], check[2])
                a.train()
                break
