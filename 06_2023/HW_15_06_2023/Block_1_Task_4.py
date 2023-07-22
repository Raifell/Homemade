# Задание №4.
# Реализуйте программу на Python, чтобы добавить год (ы) с заданной датой и отобразить новую дату.
# Example: (addYears - это имя пользовательской функции)
# print (addYears (datetime.date (2015,1,1), -1))
# print (addYears (datetime.date (2015,1,1), 0))
# print (addYears (datetime.date (2015,1,1), 2))
# печати (addYears (datetime.date (2000,2,29), 1))
# Output:
# 2014-01-01
# 2015-01-01
# 2017-01-01
# 2001-03-01

import tkinter as tk, datetime as dt



class Example:
    def __init__(self):
        self.win = tk.Tk()
        self.win.title('Task_4(B-2)')
        self.win.geometry('350x300+200+300')
        self.win.resizable(False, False)

        self.labelA = tk.Label(self.win, text='Программа выводит все воскресения определенного года', bg='yellow')
        self.labelA.grid(row=0, column=0, ipady=5, sticky='we', columnspan=2)
        self.labelB = tk.Label(self.win)
        self.labelB.grid(row=4, column=0, pady=40, ipady=5, sticky='we', columnspan=2)

        self.labelC = tk.Label(self.win, text='Введите год (YYYY,MM,DD)')
        self.labelC.grid(row=1, column=0)
        self.labelD = tk.Label(self.win, text='Введите модификатор (+-INT)')
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

    def get_date(self):
        vir1 = self.outA.get()
        vir2 = self.outB.get()
        result = ''
        try:
            vir3 = dt.datetime.strptime(vir1, '%Y,%m,%d').date()
            vir2 = int(vir2)
        except:
            result += 'Неверное значение!'
        else:

            try:
                result = dt.date(vir3.year + vir2, vir3.month, vir3.day)
            except ValueError:
                result = dt.date(vir3.year + vir2, vir3.month + 1, 1)

        self.labelB['text'] = result


app = Example()
