# Задание №4
# Реализуйте программу на Python, для создания HTML-календаря с данными за определенный год и месяц.

# Так как мы еще не касались как таковой темы HTML, данно задание будет выполнено с использованием
# возможностей библиотеки tkinter

import tkinter as tk, datetime as dt


class Example:
    def __init__(self):
        self.fr = 0
        self.win = tk.Tk()
        self.win.title('Task_4(B-2)')
        self.win.geometry('350x510+200+300')
        self.win.resizable(False, False)

        self.labelA = tk.Label(self.win, text='Календарь выводит данные за указаный месяц\nопределенного года',
                               height=3, bg='yellow')
        self.labelA.grid(row=0, column=0, columnspan=7, sticky='we')

        self.labelB = tk.Label(self.win, text='Введите год:')
        self.labelB.grid(row=1, column=0, columnspan=3, ipady=1)
        self.labelC = tk.Label(self.win, text='Введите месяц:')
        self.labelC.grid(row=2, column=0, columnspan=3, ipady=1)

        self.labelD = tk.Label(self.win, height=3, font=('Arial', 10, 'bold'))
        self.labelD.grid(row=4, column=0, columnspan=7, sticky='we')

        self.btn_1 = tk.Button(self.win, text='Получить результат', command=self.find_count)
        self.btn_1.grid(row=3, column=0, columnspan=3, pady=2)
        self.btn_2 = tk.Button(self.win, text='Очистить', command=self.clear)
        self.btn_2.grid(row=3, column=4, columnspan=3, pady=2)

        self.outA = tk.Entry(self.win)
        self.outA.grid(row=1, column=4, columnspan=3)
        self.outB = tk.Entry(self.win)
        self.outB.grid(row=2, column=4, columnspan=3)

        self.win.columnconfigure(0, minsize=50)
        self.win.columnconfigure(1, minsize=50)
        self.win.columnconfigure(2, minsize=50)
        self.win.columnconfigure(3, minsize=50)
        self.win.columnconfigure(4, minsize=50)
        self.win.columnconfigure(5, minsize=50)
        self.win.columnconfigure(6, minsize=50)

        self.win.mainloop()

    def clear(self):
        self.outA.delete(0, tk.END)
        self.outB.delete(0, tk.END)
        self.labelD['text'] = ''
        self.end_f()

    def find_count(self):
        year = self.outA.get()
        month = self.outB.get()
        d = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        m = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

        try:
            b = dt.date(int(year), int(month), 1)
            self.labelD['text'] = f'{b.year}-{m[b.month-1]}'
            if len(year) != 4:
                raise Exception()
        except:
            self.end_d()

        else:

            x = 0
            ind = 1
            self.end_f()
            self.frm_1 = tk.Frame(self.win)
            self.frm_1.grid(row=5, column=0, columnspan=7, padx=5)
            self.fr += 1
            while True:
                try:
                    date = d[b.weekday()]
                    count = b.weekday()
                    b = dt.datetime(b.year, b.month, b.day + 1)

                except:
                    break

                finally:
                    a = tk.Label(self.frm_1, text=f'{ind}\n{date}', height=3, font=('Arial', 10, 'bold'))
                    a.grid(row=x, column=count, sticky='we')
                    ind += 1
                    if date == 'Sat' or date == 'Sun':
                        a['bg'] = 'red'

                    if count >= 6:
                        count = 0
                        x += 1

    def end_d(self):
        self.labelD['text'] = 'Неправильное значение!'
        if self.fr > 0:
            self.frm_1.destroy()

    def end_f(self):
        if self.fr > 0:
            self.frm_1.destroy()
        return


app = Example()
