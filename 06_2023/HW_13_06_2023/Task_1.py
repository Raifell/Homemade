# Задание №_1 Написать программу, удовлетворяющую условиям домашнего задания указаного в файле:
# Домашнее задание 11.pdf

import tkinter as tk


class Example:
    def __init__(self):
        self.win = tk.Tk()
        self.win.title('Task_1')
        self.win.geometry('350x200+200+300')
        self.win.resizable(False, False)

        self.labelA = tk.Label(self.win, font=('Arial', 10, 'bold'))
        self.labelA.grid(row=0, column=0, columnspan=7, sticky='we', ipady=10)

        self.ent = tk.Entry(self.win, font=('Arial', 10, 'bold'))
        self.ent.grid(row=1, column=1, columnspan=5, pady=10, ipady=2)
        self.ent.bind("<Key>", lambda e: "break") # Отключаем возможность ввода информации в виджет Entry

        self.button_1 = tk.Button(self.win, bg='red', activebackground='red',
                                  command=lambda: self.color_text(0)) # Используем lambda для вызова функции с аргументом
        self.button_1.grid(row=2, column=0, sticky='we', ipady=8, padx=2)
        self.button_2 = tk.Button(self.win, bg='orange', activebackground='orange',
                                  command=lambda: self.color_text(1))
        self.button_2.grid(row=2, column=1, sticky='we', ipady=8, padx=2)
        self.button_3 = tk.Button(self.win, bg='yellow', activebackground='yellow',
                                  command=lambda: self.color_text(2))
        self.button_3.grid(row=2, column=2, sticky='we', ipady=8, padx=2)
        self.button_4 = tk.Button(self.win, bg='green', activebackground='green',
                                  command=lambda: self.color_text(3))
        self.button_4.grid(row=2, column=3, sticky='we', ipady=8, padx=2)
        self.button_5 = tk.Button(self.win, bg='grey', activebackground='grey',
                                  command=lambda: self.color_text(4))
        self.button_5.grid(row=2, column=4, sticky='we', ipady=8, padx=2)
        self.button_6 = tk.Button(self.win, bg='blue', activebackground='blue',
                                  command=lambda: self.color_text(5))
        self.button_6.grid(row=2, column=5, sticky='we', ipady=8, padx=2)
        self.button_7 = tk.Button(self.win, bg='purple', activebackground='purple',
                                  command=lambda: self.color_text(6))
        self.button_7.grid(row=2, column=6, sticky='we', ipady=8, padx=2)

        self.win.grid_columnconfigure(0, minsize=50)
        self.win.grid_columnconfigure(1, minsize=50)
        self.win.grid_columnconfigure(2, minsize=50)
        self.win.grid_columnconfigure(3, minsize=50)
        self.win.grid_columnconfigure(4, minsize=50)
        self.win.grid_columnconfigure(5, minsize=50)
        self.win.grid_columnconfigure(6, minsize=50)

        self.win.mainloop()

    def color_text(self, vir):
        if vir == 0:
            self.labelA['text'] = 'Red'
            self.clear()
            self.ent.insert(0, '           #FF0000')
        elif vir == 1:
            self.labelA['text'] = 'Orange'
            self.clear()
            self.ent.insert(0, '           #FFA500')
        elif vir == 2:
            self.labelA['text'] = 'Yellow'
            self.clear()
            self.ent.insert(0, '           #FFFF00')
        elif vir == 3:
            self.labelA['text'] = 'Green'
            self.clear()
            self.ent.insert(0, '           #008000')
        elif vir == 4:
            self.labelA['text'] = 'Grey'
            self.clear()
            self.ent.insert(0, '           #808080')
        elif vir == 5:
            self.labelA['text'] = 'Blue'
            self.clear()
            self.ent.insert(0, '           #0000ff')
        else:
            self.labelA['text'] = 'Purple'
            self.clear()
            self.ent.insert(0, '           #800080')

    def clear(self):
        self.ent.delete(0, tk.END)


app = Example()
