# Задание №_2 Напишите программу, в котором пользователь вводит в текстовое поле предложение,
# и при нажатии на кнопку во втором появляется то же предложение наоборот.
# Входные данные: На улице очень жаркая погода
# Вывод: адогоп яакраж ьнечо ецилу аН

import tkinter as tk


class Example:
    def __init__(self):
        self.win = tk.Tk()  # Создаем окно программы
        self.win.title('Task_2')  # Заголовок окна
        self.win.geometry('450x400+200+300')  # Геометрия размеров и положения окна программы при запуске
        self.win.config(bg='grey')  # Цвет фона окна
        self.win.resizable(False, False)  # Отключениевозможности изменения размеров окна

        # Виджеты Label, располагаются в главном окне

        self.labelA = tk.Label(self.win, text='Данная программа преобразует введенную строку в строку наоборот.',
                               bg='yellow', height=2, font=('Arial', 10))
        self.labelA.grid(row=0, column=0, columnspan=2, sticky='we')
        self.labelB = tk.Label(self.win, text='Строка ввода данных', bg='grey', font=('Arial', 10))
        self.labelB.grid(row=1, column=0, sticky='we')
        self.labelC = tk.Label(self.win, text='Строка вывода данных', bg='grey', font=('Arial', 10))
        self.labelC.grid(row=2, column=0, sticky='we')

        # Виджеты Entry располагаются в главном окне

        self.inp = tk.Entry(self.win)
        self.inp.grid(row=1, column=1, sticky='we', ipady=2, pady=1, padx=1)
        self.out = tk.Entry(self.win)
        self.out.grid(row=2, column=1, sticky='we', ipady=2, pady=1, padx=1)

        # Кнопки Button располагаются в главном окне

        self.button_1 = tk.Button(self.win, text='Преобразовать', command=lambda: self.grover())
        self.button_1.grid(row=3, column=0, sticky='we', padx=1, pady=1)
        self.button_2 = tk.Button(self.win, text='Очистить', command=lambda: self.clear())
        self.button_2.grid(row=3, column=1, sticky='we', padx=1, pady=1)

        self.win.grid_columnconfigure(0, minsize=150)  # Минимальные размеры для первой колонки
        self.win.grid_columnconfigure(1, minsize=300)  # Минимальные размеры для второй колонки

        self.win.mainloop()

    def grover(self):  # Функция нажатия кнопки "Преобразовать"
        vir = self.inp.get()  # Получает значения из строки ввода данных
        self.out.delete(0, tk.END)  # Очищает строку вывода данных
        self.out.insert(0, vir[::-1])  # Отображает результат в строке вывода данных

    def clear(self):  # Функция нажатия кнопки "Очистить"
        self.inp.delete(0, tk.END)
        self.out.delete(0, tk.END)


app = Example()
