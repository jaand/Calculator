from tkinter import ttk, StringVar, END, Tk


class Calculator:
    calc_value = 0.0  # the value at the beginning

    def __init__(self, window):

        self.entered_value = StringVar(window)
        self.trigger = None
        self.ZERO_DIVISION_MESSAGE = "You can't divide by zero"
        self.actions = {
            "/": self.divide,
            "+": self.add,
            "*": self.mult,
            "-": self.subt,
        }

        window.title("SimpleCalculator")  # define the name/title which appears on program window
        window.geometry("447x220")  # define the size of program window
        window.resizable(width=False, height=False)  # blocks ability to resize the Calculator

        style = ttk.Style()
        style.configure("TButton",
                        font="Dublin 10",
                        padding=10)

        style.configure("TEntry",
                        font="Dublin 20",
                        padding=10)

        # below are all existing buttons
        # their size, "name", and placement
        self.number_entered = ttk.Entry(window,
                                        textvariable=self.entered_value, width=40)
        self.number_entered.grid(row=0, columnspan=3)

        self.b1 = ttk.Button(window, text="1",
                             command=lambda: self.button_press('1')).grid(row=1, column=0)

        self.b2 = ttk.Button(window, text="2",
                             command=lambda: self.button_press('2')).grid(row=1, column=1)

        self.b3 = ttk.Button(window, text="3",
                             command=lambda: self.button_press('3')).grid(row=1, column=2)

        self.b4 = ttk.Button(window, text="4",
                             command=lambda: self.button_press('4')).grid(row=2, column=0)

        self.b5 = ttk.Button(window, text="5",
                             command=lambda: self.button_press('5')).grid(row=2, column=1)

        self.b6 = ttk.Button(window, text="6",
                             command=lambda: self.button_press('6')).grid(row=2, column=2)

        self.b7 = ttk.Button(window, text="7",
                             command=lambda: self.button_press('7')).grid(row=3, column=0)

        self.b8 = ttk.Button(window, text="8",
                             command=lambda: self.button_press('8')).grid(row=3, column=1)

        self.b9 = ttk.Button(window, text="9",
                             command=lambda: self.button_press('9')).grid(row=3, column=2)

        self.b0 = ttk.Button(window, text="0",
                             command=lambda: self.button_press('0')).grid(row=4, column=1)

        self.b_dot = ttk.Button(window, text=".",
                                command=lambda: self.button_press('.')).grid(row=4, column=0)

        self.b_equal = ttk.Button(window, text="=",
                                  command=lambda: self.equal_button_press()).grid(row=0, column=3)

        self.b_div = ttk.Button(window, text="/",
                                command=lambda: self.math_button_press('/')).grid(row=1, column=3)

        self.b_mult = ttk.Button(window, text="*",
                                 command=lambda: self.math_button_press('*')).grid(row=2, column=3)

        self.b_add = ttk.Button(window, text="+",
                                command=lambda: self.math_button_press('+')).grid(row=3, column=3)

        self.b_subt = ttk.Button(window, text="-",
                                 command=lambda: self.math_button_press('-')).grid(row=4, column=3)

        self.b_ac = ttk.Button(window, text="AC",
                               command=lambda: self.delete_button_press()).grid(row=4, column=2)

    def button_press(self, value):

        entered_value = self.number_entered.get()  # shows proper value in entry window1

        if entered_value == self.ZERO_DIVISION_MESSAGE:
            self.number_entered.delete(0, END)
            self.number_entered.insert(0, value)
        else:
            entered_value = self.number_entered.get()
            entered_value += value  # writes clicked number next to existing number (

            self.number_entered.delete(0, END)  # deletes current entry window

            self.number_entered.insert(0, entered_value)  # shows value we pressed

    def check_if_float(self, string_value):
        try:
            float(string_value)
            return True
        except ValueError:
            return False

    def math_button_press(self, value):
        if self.check_if_float(str(self.number_entered.get())):
            self.calc_value = float(self.entered_value.get())

            self.trigger = value

            self.number_entered.delete(0, END)  # deletes entry window after you clicked any of this buttons

    def delete_button_press(self):
        self.number_entered.delete(0, END)

    def add(self):
        return self.calc_value + float(self.entered_value.get())

    def mult(self):
        return self.calc_value * float(self.entered_value.get())

    def subt(self):
        return self.calc_value - float(self.entered_value.get())

    def divide(self):
        try:
            return self.calc_value / float(self.entered_value.get())
        except ZeroDivisionError:
            print(self.ZERO_DIVISION_MESSAGE)  # only for debugging
            self.number_entered.delete(0, END)  # deletes all data when trying divide by zero
            return self.ZERO_DIVISION_MESSAGE

    def equal_button_press(self):
        equal = self.actions[self.trigger]
        solution = equal()

        self.number_entered.delete(0, END)

        self.number_entered.insert(0, solution)


if __name__ == "__main__":  #
    window = Tk()  # creating main window of program
    Calculator(window)

    window.mainloop()
