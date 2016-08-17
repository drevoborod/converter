#!/usr/bin/env python3

"""Graphical user interface for converter."""

import tkinter as tk

import convert


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
