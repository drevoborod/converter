#!/usr/bin/python3
# -*- coding: utf-8 -*-

class CalcEngineErrors(Exception): pass

class Count():
    screen = ["0"]
    to_clear = 0
    operation = None
    digit1 = ["0"]
    last_button = 0
    
    def screen_clear(self):
        self.screen = ["0"]
        
    def screen_append_list(self, l):
        """Добавление целой строки."""
        if len(l) > 20:
            raise CalcEngineErrors
        else:
            self.screen = l
            if self.to_clear == 1:
                self.to_clear = 0
       
    def screen_append_symbol(self, symbol):
        """Добавление одного символа. Вызывать при нажатии на кнопку с цифрой."""
        if self.to_clear == 1:
            self.screen_clear()
            if symbol is ".":
                self.screen.append(symbol)
            elif symbol is "-":
                self.screen.insert(0, symbol)
            elif symbol is "0":
                pass
            else:
                self.screen[0] = symbol
            self.to_clear = 0
        else:
            if self.screen[0] is "-" and len(self.screen) == 21:
                if symbol is "-":
                    self.screen.pop(0)
                else:
                    raise CalcEngineErrors
            elif self.screen[0] is not "-" and len(self.screen) == 20:
                if symbol is "-":
                    self.screen.insert(0, symbol)
                else:
                    raise CalcEngineErrors
            else:
                if symbol is ".":
                    if symbol not in self.screen:
                        self.screen.append(symbol)
                elif symbol is "-" and symbol is not self.screen[0]:
                    self.screen.insert(0, symbol)
                else:
                    if self.screen[0] is not "-":
                        if len(self.screen) == 1 and int(self.screen[0]) == 0:
                            self.screen[0] = symbol
                        else:
                            self.screen.append(symbol)
                    else:
                        if self.screen[0] is symbol:
                            self.screen.pop(0)
                        elif len(self.screen) == 2 and int(self.screen[1]) == 0:
                            self.screen[1] = symbol
                        else:
                            self.screen.append(symbol)


                ##debug:
                # print("Self.screen:", self.screen)
                ##

        
    def screen_backspace(self):
        """Удалить один символ. Если он один, то обнулить screen."""
        if self.to_clear == 1:
            self.screen_clear()
        else:
            if (len(self.screen) == 1) or (len(self.screen) == 2 and self.screen[0] is "-"):
                self.screen_clear()
            else:
                self.screen.pop()
            
    def last_button(self, button):
        """Записывается, какая кнопка нажата.
        Вызывать после других функций!"""
        self.last_button = button
    
    def arifm_operation(self, oper):
        """Функция принимает знак арифметической операции и сохраняет его.
        Если знак операции уже есть, то старая операция выполняется и 
        записывается новый."""
        # Такая странная сборка нужна потому, что в этих переменных могут быть строки и числа в куче:
        screen = str(float(self.join_list(self.screen[:])))
        digit = str(float(self.join_list(self.digit1[:])))
##D:
        print("screen = {0}\ndigit ={1}".format(screen, digit))
##
        # Если знака операции ещё нет, то содержимое экрана записывается 
        # в self.digit1, и ставится признак очистки экрана:
        if self.operation is None:
            self.digit1 = self.screen[:]
            self.to_clear = 1
            self.operation = oper[:]
        # Иначе, если знак операции уже есть, то есть ранее уже вводились данные:
        else:
            # Если предыдущее нажатие было на кнопку операции,
            # то юзер просто передумал:
            if self.last_button == 1:
                self.operation = oper[:]
            else:
                # если на экране что-то содержательное, то с ним выполняется записанная
                # операция и результат пишется в self.digit1, а в переменную self.operation
                # пишется знак новой операции:
                if float(screen) != 0:
                    # Если нужно вычислить корень:
                    try:
                        if self.operation == "sqrt":
                            self.digit1 = list(str(float(digit) ** (1/float(screen))))
                        else:
                            exec(compile("self.digit1 = list(str({0} {1} {2}))".format(digit, self.operation, screen), {}, "exec"))
                    except OverflowError:
### Разобраться! 1) Ошибки должны райзиться на уровень гуя
### 2) После ошибки переполнения при вычислении буфер надо сбрасывать.
                        self.screen = "Error"
                        self.vars_clear()
                    else:
                        self.operation = oper[:]
                        try:
                            self.screen_append_list(self.digit1[:])
                        except CalcEngineErrors:
                            self.screen = "Error"
                            self.vars_clear()
                    # И готовимся очищать экран:
                    finally:
                        self.to_clear = 1
                # Если на экране 0, то старый знак операции просто перезаписывается новым
                # (это означает, что юзер просто передумал и ввёл новый знак сразу за старым):
               # else:
                #    self.operation = oper[:]
                 #   self.to_clear = 1
##D:
        print("self.operation =", self.operation)
        print("self.screen =", self.screen)
        print("self.digit1 =", self.digit1)
##
                
    def result(self):
        """Вызывать при нажатии на "=". """
        if self.operation is not None:
            screen = str(float(self.join_list(self.screen[:])))
            digit = str(float(self.join_list(self.digit1[:])))
##D:
            print("screen = {0}\ndigit ={1}".format(screen, digit))
            print("self.screen =", self.screen)
            print("self.digit1 =", self.digit1)
##
            if float(screen) != 0:
                # Если нужно вычислить корень:
                try:
                    if self.operation == "sqrt":
                        if self.to_clear == 1:
                            self.screen_append_list(list(str(float(digit) ** (1/2))))
                        else:
                            self.screen_append_list(list(str(float(digit) ** (1/float(screen)))))
                    else:
                        exec(compile("self.screen = list(str({0} {1} {2}))".format(digit, self.operation, screen), {}, "exec"))
                except (OverflowError, CalcEngineErrors):
                    self.screen = "Error"
                    self.vars_clear()
                # И готовимся очищать экран:
                self.to_clear = 1
                self.operation = None
                self.digit1 = ["0"]
##D:
        print("self.operation =", self.operation)
        print("self.screen =", self.screen)
        print("self.digit1 =", self.digit1)
##  
    def vars_clear(self):
        """Сброс всех переменных."""
        self.digit1 = ['0']
        self.operation = None
        self.last_button = 0
                      
                
    def all_clear(self):
        """Вызывать при нажатии на сброс."""
        self.screen_clear()
        self.vars_clear()
        
    def join_list(self, a_list):
##D:
        print("Source:", a_list)
##
        """Превращает список a_list в строку."""
        return "".join(map(str, a_list))

            
if __name__ == "__main__":
    calc = Count()
    
    def screen():
        print(calc.join_list(calc.screen[:]))
        
    while True:
        screen()
        digit = input("Введите число: ")
        calc.screen_append_list(list(digit))
        screen()
        symbol = input("Введите знак операции: ")
        if symbol == "=":
            calc.result()
        elif symbol == "c":
            calc.all_clear()
        elif symbol == "e":
            break
        else:
            calc.arifm_operation(symbol)
        

