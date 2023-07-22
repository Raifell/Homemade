# Задание №2
# Реализуйте программу, для вычисления количества дней между двумя датами

import tkinter as tk, datetime as dt


class Example:
    def __init__(self):
        self.win = tk.Tk()
        self.win.title('Task_2(B-2)')
        self.win.geometry('350x300+200+300')
        self.win.resizable(False, False)

        self.labelA = tk.Label(self.win, text='Программа выводит разницу двух дат (в днях)', bg='yellow')
        self.labelA.grid(row=0, column=0, ipady=5, sticky='we', columnspan=2)
        self.labelB = tk.Label(self.win)
        self.labelB.grid(row=4, column=0, pady=40, ipady=5, sticky='we', columnspan=2)

        self.labelC = tk.Label(self.win, text='Введите первую дату (YYYY,MM,DD)')
        self.labelC.grid(row=1, column=0)
        self.labelD = tk.Label(self.win, text='Введите вторую дату (YYYY,MM,DD)')
        self.labelD.grid(row=2, column=0)

        self.outA = tk.Entry(self.win)
        self.outA.grid(row=1, column=1)
        self.outB = tk.Entry(self.win)
        self.outB.grid(row=2, column=1)

        self.btn_1 = tk.Button(self.win, text='Получить результат', command=lambda: self.get_date())
        self.btn_1.grid(row=3, column=0, columnspan=2, padx=40, sticky='w')
        self.btn_2 = tk.Button(self.win, text='Очистить', command=lambda: self.clear())
        self.btn_2.grid(row=3, column=1)

        self.win.columnconfigure(0, minsize=200)
        self.win.columnconfigure(1, minsize=150)

        self.win.mainloop()

    def clear(self):
        self.outA.delete(0, tk.END)
        self.outB.delete(0, tk.END)
        self.labelB['text'] = ''

    def get_date(self):
        try:
            a = self.outA.get()
            a1 = dt.datetime.strptime(a, '%Y,%m,%d').date()
            b = self.outB.get()
            b1 = dt.datetime.strptime(b, '%Y,%m,%d').date()
            result = a1 - b1
            self.labelB['text'] = f'Разница: {abs(result.days)} день'
        except:
            self.labelB['text'] = 'Неверное значение!'




app = Example()
