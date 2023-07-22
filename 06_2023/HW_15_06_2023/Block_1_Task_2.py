# Задание №2.
# Реализуйте программу, чтобы найти дату первого понедельника данной недели.
# Date: 2015, 50
# Output: пн 14 декабря 00:00:00 2015

import tkinter as tk, time


class Example:
    def __init__(self):
        self.win = tk.Tk()
        self.win.title('Task_2(B-1)')
        self.win.geometry('350x200+200+300')
        self.win.resizable(False, False)

        self.labelA = tk.Label(self.win, text='Программа выводит дату первого понедельника\n данной недели', bg='yellow')
        self.labelA.grid(row=0, column=0, ipady=5, sticky='we', columnspan=2)
        self.labelB = tk.Label(self.win)
        self.labelB.grid(row=3, column=0, pady=20, ipady=5, sticky='we', columnspan=2)

        self.labelC = tk.Label(self.win, text='Введите год')
        self.labelC.grid(row=1)
        self.labelC = tk.Label(self.win, text='Введите количество недель')
        self.labelC.grid(row=2)

        self.outA = tk.Entry(self.win)
        self.outA.grid(row=1, column=1)
        self.outB = tk.Entry(self.win)
        self.outB.grid(row=2, column=1)

        self.btn_1 = tk.Button(self.win, text='Получить номер недели', command=lambda: self.result())
        self.btn_1.grid(row=4, column=0, columnspan=2, padx=40, sticky='w')
        self.btn_2 = tk.Button(self.win, text='Очистить', command=lambda: self.clear())
        self.btn_2.grid(row=4, column=1)

        self.win.columnconfigure(0, minsize=200)
        self.win.columnconfigure(1, minsize=150)

        self.win.mainloop()

    def clear(self):
        self.outA.delete(0, tk.END)
        self.outB.delete(0, tk.END)

    def result(self):
        a = self.outA.get()
        b = self.outB.get()
        self.get_time(a, b)

    def get_time(self, year, week):
        try:
            d = time.asctime(time.strptime(f'{year} {week} 1', '%Y %W %w')) # Год/неделя/день недели
            self.labelB['text'] = f'Дата: {d}'
        except:
            self.labelB['text'] = f'Введены неверные данные!'


app = Example()

# Для выполнения этой задачи была использована библиотека time, возможности этой библиотеки
# позволяют выполнить задачу в одно действие и не разводить большую функцию, как в случае
# использования библиотеки datetime
