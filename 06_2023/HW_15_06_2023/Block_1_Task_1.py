# Задание №1.
# Реализуйте программу, чтобы получить номер недели.
# Date: 2015, 6, 16
# Output: 25

import datetime as dt, tkinter as tk


class Example:
    def __init__(self):
        self.win = tk.Tk()
        self.win.title('Task_1(B-1)')
        self.win.geometry('350x200+200+300')
        self.win.resizable(False, False)

        self.labelA = tk.Label(self.win, text='Программа выводит номер недели\nотносительно времени системы', bg='yellow')
        self.labelA.grid(row=0, column=0, ipady=5, sticky='we')
        self.labelB = tk.Label(self.win)
        self.labelB.grid(row=1, column=0, pady=20, ipady=5, sticky='we')

        self.btn_1 = tk.Button(self.win, text='Получить номер недели', command=self.get_time)
        self.btn_1.grid(row=2, column=0, pady=20)

        self.win.columnconfigure(0, minsize=350)

        self.win.mainloop()

    def get_time(self):
        vir1 = dt.datetime.now().strftime('%d %m %Y')
        vir2 = dt.datetime.now().strftime('%V')
        self.labelB['text'] = f'Текущая дата: {str(vir1)}\n' \
                              f'Номер недели:        {str(vir2)}'

app = Example()
