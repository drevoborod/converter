#!/usr/bin/env python3

"""Graphical user interface for converter."""

import tkinter as tk
from tkinter import ttk

import convert


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        tk.Label(self, text="Исходное число:").grid(row=0, column=0)
        tk.Label(self, text="Основание:").grid(row=0, column=1)
        self.input_entry = tk.Entry(self)
        self.input_entry.grid(row=1, column=0, padx=5, pady=5)
        self.input_menu = DropdownMenu(self)
        self.input_menu.grid(row=1, column=1, padx=5, pady=5)
        tk.Label(self, text="Результат:").grid(row=3, column=0)
        tk.Label(self, text="Основание:").grid(row=3, column=1)
        self.output_entry = tk.Entry(self, state='disabled')
        self.output_entry.grid(row=4, column=0, padx=5, pady=5)
        self.output_menu = DropdownMenu(self)
        self.output_menu.grid(row=4, column=1, padx=5, pady=5)
        tk.Frame(self, height=25).grid(row=5)
        tk.Button(self, text="Вычислить", command=self.calculate).grid(row=6, column=0, padx=5, pady=5)
        tk.Button(self, text="Выход", command=self.destroy).grid(row=6, column=1, padx=5, pady=5)
        self.mainloop()

    def calculate(self):
        print(self.input_entry.get())


class DropdownMenu(ttk.Combobox):
    def __init__(self, parent, values=[x for x in range(2, 20)]):
        super().__init__(master=parent, values=values)
        self.current(0)


if __name__ == "__main__": MainWindow()