# Задание №3.
# Реализуйте программу, чтобы выбрать все воскресенья определенного года.

import tkinter as tk, datetime as dt



class Example:
    def __init__(self):
        self.win = tk.Tk()
        self.win.title('Task_3(B-1)')
        self.win.geometry('350x300+200+300')
        # self.win.resizable(False, False)

        self.labelA = tk.Label(self.win, text='Программа выводит все воскресения определенного года', bg='yellow')
        self.labelA.grid(row=0, column=0, ipady=5, sticky='we', columnspan=2)
        self.labelB = tk.Label(self.win, justify=tk.LEFT, width=30, height=10)
        self.labelB.grid(row=3, column=0, pady=20, ipady=5, sticky='we', columnspan=2)

        self.labelC = tk.Label(self.win, text='Введите год')
        self.labelC.grid(row=1, column=0)

        self.outA = tk.Entry(self.win)
        self.outA.grid(row=1, column=1)

        self.btn_1 = tk.Button(self.win, text='Получить результат', command=lambda: self.result())
        self.btn_1.grid(row=2, column=0, columnspan=2, padx=40, sticky='w')
        self.btn_2 = tk.Button(self.win, text='Очистить', command=lambda: self.clear())
        self.btn_2.grid(row=2, column=1)

        self.win.columnconfigure(0, minsize=200)
        self.win.columnconfigure(1, minsize=150)

        self.win.mainloop()

    def clear(self):
        self.outA.delete(0, tk.END)

    def result(self):
        count = 0
        year = self.outA.get()
        try:
            self.labelB['text'] = ''
            if len(year) < 4:
                raise Exception()
            for x in self.get_time(int(year)):
                if count < 4:
                    self.labelB['text'] += f' {str(x)}  '
                    count += 1
                else:
                    self.labelB['text'] += f'  {str(x)}  \n'
                    count = 0
        except:
            self.labelB['text'] = f'Неверное значение!'

    def get_time(self, year):
        b = dt.date(year, 1, 1)
        cu = []
        while True:
            try:
                if b.weekday() == 6:
                    cu.append(b)

                b = dt.date(b.year, b.month, b.day + 1)

                if b.month == 12 and b.day == 31:
                    if b.weekday() == 6:
                        cu.append(b)
                    break
            except:
                b = dt.date(b.year, b.month + 1, 1)
        return cu


app = Example()
