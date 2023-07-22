# Задание №1
# Реализуйте программу, чтобы узнать время по Гринвичу и местное время.

import time, datetime as dt, tkinter as tk


class Example:
    def __init__(self):
        self.win = tk.Tk()
        self.win.title('Task_1(B-1)')
        self.win.geometry('350x200+200+300')
        self.win.resizable(False, False)

        self.labelA = tk.Label(self.win, text='Программа выводит текущее время GMT модификатор', bg='yellow')
        self.labelA.grid(row=0, column=0, ipady=5, sticky='we')
        self.labelB = tk.Label(self.win)
        self.labelB.grid(row=1, column=0, pady=20, ipady=5, sticky='we')

        self.btn_1 = tk.Button(self.win, text='Получить номер недели', command=self.get_time)
        self.btn_1.grid(row=2, column=0, pady=20)

        self.win.columnconfigure(0, minsize=350)

        self.win.mainloop()

    def get_time(self):
        vir1 = dt.datetime.now().strftime('%H:%M:%S')
        self.labelB['text'] = f'Текущее время: {str(vir1)}\n' \
                              f'GMT: {time.strftime("%z", time.gmtime())}'

app = Example()
