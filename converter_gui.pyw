#!/usr/bin/env python3

"""Graphical user interface for converter."""

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

import convert


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Base converter")
        self.resizable(width=0, height=0)
        tk.Label(self, text="Исходное число:").grid(row=0, column=0)
        tk.Label(self, text="Основание:").grid(row=0, column=1, padx=5)
        self.input_entry = tk.Entry(self, width=60)
        self.input_entry.grid(row=1, column=0, padx=5, pady=5)
        self.input_menu = DropdownMenu(self, width=3)
        self.input_menu.grid(row=1, column=1, padx=5, pady=5)
        tk.Label(self, text="Результат:").grid(row=3, column=0)
        tk.Label(self, text="Основание:").grid(row=3, column=1, padx=5)
        self.output_entry = tk.Entry(self, state="disabled", width=60)
        self.output_entry.grid(row=4, column=0, padx=5, pady=5)
        self.output_menu = DropdownMenu(self, width=3)
        self.output_menu.grid(row=4, column=1, padx=5, pady=5)
        tk.Frame(self, height=25).grid(row=5)
        tk.Button(self, text="Вычислить", command=self.calculate).grid(row=6, column=0, padx=5, pady=5)
        tk.Button(self, text="Выход", command=self.destroy).grid(row=6, column=1, padx=5, pady=5)
        self.bind("<Return>", lambda e: self.calculate())
        self.mainloop()

    def calculate(self):
        source_ground = self.input_menu.get()  # Основание системы счисления исходного числа.
        target_ground = self.output_menu.get()  # Основание системы счисления результата.
        digit = self.input_entry.get()
        try:
            # Класс, отвечающий за перевод. Передаём основания систем счисления:
            conv = convert.FromXtoY(source_ground, target_ground)
            # Запускаем функцию перевода:
            res = conv.conversion(digit)
        except convert.ConverterError:
            showinfo("Ошибочный ввод", "Введены некорректные данные!")
        else:
            self.output_entry.config(state='normal')
            self.output_entry.delete(0, 'end')
            self.output_entry.insert(0, res)


class DropdownMenu(ttk.Combobox):
    def __init__(self, parent, values=[x for x in range(2, 20)], **kwargs):
        super().__init__(master=parent, values=values, **kwargs)
        self.current(0)


if __name__ == "__main__": MainWindow()