#!/usr/bin/python3
# -*- coding: utf-8 -*-

import tkinter
import convert
import calc_engine

class MainGui():
    buttons_dict = {0: 0, 1: ".", 2: "-", 3: 1, 4: 2, 5: 3, 6: 4, 7: 5, 8: 6, 9: 7, 10: 8, 11: 9}
    oper_buttons_dict = {18: "+", 19: "-", 16: "*", 17: "/", 14: "**", 15: "sqrt"}
    
    def __init__(self):
        self.frames()
        self.indicator()
        self.number_buttons()

    def indicator(self):
        self.indicator = tkinter.Label(text="0", anchor="w", height=1, width=21, font="Arial 20", relief="sunken")
        self.indicator.grid(row=0)
    
    def frames(self):
        self.frame1 = tkinter.Frame(root, height=100, width=540, bd=5)
        self.frame2 = tkinter.Frame(root, height=440, width=540, bd=0)
        # Рамка с символьными кнопками:
        self.frame3 = tkinter.Frame(self.frame2, width=380, height=440, bd=5)
        # Рамка с кнопками операций:
        self.frame4 = tkinter.Frame(self.frame2, width=160, height=440, bd=0)
        # Рамка с кнопками сброса:
        self.frame5 = tkinter.Frame(root, height=80, width=540, bd=10)
        self.frame1.grid(row=0)
        self.frame5.grid(row=1)
        self.frame2.grid(row=2)
        self.frame3.grid(row=0, column=0)
        self.frame4.grid(row=0, column=1)

        
    def coords_list(self, x_count, y_count):
        """Функция возвращает список кортежей координат объектов для 
        сетки заданного размера."""
        # Список координат кнопок:
        coords = []
        for y in range(0, y_count):
            l=[]
            for x in range(0, x_count):
                l.append((y, x))
            l.reverse()
            for n in l:
                coords.append(n)
        coords.reverse()
        return coords        
        
    def number_buttons(self):
        # Список координат кнопок:
        coords = self.coords_list(3, 5)
        #создаём переменные класса для каждой кнопки и размещаем их:
        for number in reversed(range(0, 12)):
            setattr(self, "image%d" % number, tkinter.PhotoImage(file='./images/calc/%d.gif' % number))
            #setattr(self, "button%d" % number, tkinter.Button(self.frame3, image=self.image{0}, width=123, height=110, relief='raised', command=(lambda: self.button_action({0}))))
            #exec(compile("self.image{0} = tkinter.PhotoImage(file='./images/calc/{0}.gif')".format(number), {}, "exec"))
            exec(compile("self.button{0} = tkinter.Button(self.frame3, image=self.image{0}, width=123, height=110, relief='raised', command=(lambda: self.button_action({0})))".format(number), {}, "exec"))
            exec(compile("self.button{0}.grid(row=coords[{0}][0], column=coords[{0}][1])".format(number), {}, "exec"))
            
            

    def change_indicator(self):
        ##d
        #print(self.calc.screen)
        ##
        self.indicator.configure(text=self.calc.join_list(self.calc.screen[:]))
        

    def write_button(self, button):
        print("button %d pressed" % button)
"""
    def act_button0(self):
        self.button_action(0)
    def act_button1(self):
        self.button_action(1)
    def act_button2(self):
        self.button_action(2)
    def act_button3(self):
        self.button_action(3)
    def act_button4(self):
        self.button_action(4)
    def act_button5(self):
        self.button_action(5)
    def act_button6(self):
        self.button_action(6)
    def act_button7(self):
        self.button_action(7)
    def act_button8(self):
        self.button_action(8)
    def act_button9(self):
        self.button_action(9)
    def act_button10(self):
        self.button_action(10)
    def act_button11(self):
        self.button_action(11)
    def act_button12(self):
        self.button_action(12)
    def act_button13(self):
        self.button_action(13)
    def act_button14(self):
        self.button_action(14)
    def act_button15(self):
        self.button_action(15)
    def act_button16(self):
        self.button_action(16)
    def act_button17(self):
        self.button_action(17)
    def act_button18(self):
        self.button_action(18)
    def act_button19(self):
        self.button_action(19)
    def act_button20(self):
        self.button_action(20)
"""
class Calculator(MainGui):
    def __init__(self):
        MainGui.__init__(self)
        self.function_buttons()
        # Инициализируем движок калькулятора:
        self.calc = calc_engine.Count()


    def function_buttons(self):
        coords = self.coords_list(2, 4)
        for number in reversed(range(14, 20)):
            #exec(compile("self.image{0} = tkinter.PhotoImage(file='./images/calc/{0}.gif')".format(number), {}, "exec"))
            setattr(self, "image%d" % number, tkinter.PhotoImage(file='./images/calc/%d.gif' % number))
            exec(compile("self.button{0} = tkinter.Button(self.frame4, image=self.image{0}, width=75, height=110, relief='raised', command=(lambda: self.button_action({0})))".format(number), {}, "exec"))
            exec(compile("self.button{0}.grid(row=coords[{1}][0], column=coords[{1}][1])".format(number, number-12), {}, "exec"))
        # "=":
        self.image12 = tkinter.PhotoImage(file='./images/calc/12.gif')
        self.button12 = tkinter.Button(self.frame4, image=self.image12, width=150, height=110, relief='raised', command=(lambda: self.button_action(12)))
        self.button12.grid(row=3, columnspan=2)
        # "C":
        self.image13 = tkinter.PhotoImage(file='./images/calc/13.gif')
        self.button13 = tkinter.Button(self.frame5, image=self.image13, width=123, height=110, relief='raised', command=(lambda: self.button_action(13)))
        self.button13.grid(row=0, column=0)
        # "<-":
        self.image20 = tkinter.PhotoImage(file='./images/calc/20.gif')
        self.button20 = tkinter.Button(self.frame5, image=self.image20, width=123, height=110, relief='raised', command=(lambda: self.button_action(20)))
        self.button20.grid(row=0, column=1)


    def button_action(self, button_number):
        self.write_button(button_number)
        if button_number in range(0, 12):
            try:
                self.calc.screen_append_symbol(self.buttons_dict[button_number])
                self.calc.last_button = 0
            except calc_engine.CalcEngineErrors:
                pass    # Здесь будет всплывающее окно.
        elif button_number in range(14, 20):
            ###D:
            # print("Operation from dict:", self.oper_buttons_dict[button_number])
            ####
            self.calc.arifm_operation(self.oper_buttons_dict[button_number])
            self.calc.last_button = 1
        elif button_number == 20:
            self.calc.screen_backspace()
            self.calc.last_button = 0
        elif button_number == 13:
            self.calc.all_clear()
        elif button_number == 12:
            self.calc.result()
            self.calc.last_button = 1
        self.change_indicator()

class Converter(MainGui):
    def __init__(self):
        MainGui.__init__()

def select_gui(menu_item):
    if menu_item == 0:
        return Calculator()
    elif menu_item == 1:
        return Converter()


if __name__ == "__main__":
    root = tkinter.Tk()
    gui = select_gui(0)
    root.mainloop()
