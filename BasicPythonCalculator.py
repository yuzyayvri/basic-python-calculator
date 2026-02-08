from tkinter import *
from tkinter import ttk

class Calculator:
    def __init__(self, root):
        self.window = root
        self.operation = None
        self.functions = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y,
            '^': lambda x, y: x ** y
        }
        
        self.setup_ui()
    
    def setup_ui(self):
        self.frame = ttk.Frame(self.window, padding=30, width=700, height=550)
        self.frame.grid(row=0, column=0, sticky="nsew")
        self.frame.grid_propagate(False)
        self.window.title('Basic Python Calculator')
        self.window.grid_rowconfigure(0, weight=1)
        self.window.grid_columnconfigure(0, weight=1)
        
        for i in range(11):
            self.frame.grid_columnconfigure(i, weight=1)
        for i in range(6):
            self.frame.grid_rowconfigure(i, weight=1)
        
        text = ttk.Label(self.frame, text='Basic Python Calculator', font=('Verdana', 18, 'bold'))
        text.grid(row=0, column=2, columnspan=5, pady=20)
        
        self.input1 = ttk.Entry(self.frame, width=20, font=('Verdana', 12), justify='center')
        self.input1.grid(row=1, column=1, columnspan=3, padx=10, pady=15)
        
        self.input2 = ttk.Entry(self.frame, width=20, font=('Verdana', 12), justify='center')
        self.input2.grid(row=1, column=5, columnspan=3, padx=10, pady=15)
        
        self.addition = Button(self.frame, text='+', command=lambda: self.button_click_effect(self.addition, lambda: self.set_operation('+')), width=8, font=('Verdana', 12), padx=10, pady=5)
        self.addition.grid(row=2, column=2, padx=8, pady=12)
        
        self.subtraction = Button(self.frame, text='-', command=lambda: self.button_click_effect(self.subtraction, lambda: self.set_operation('-')), width=8, font=('Verdana', 12), padx=10, pady=5)
        self.subtraction.grid(row=2, column=3, padx=8, pady=12)
        
        self.division = Button(self.frame, text='/', command=lambda: self.button_click_effect(self.division, lambda: self.set_operation('/')), width=8, font=('Verdana', 12), padx=10, pady=5)
        self.division.grid(row=2, column=4, padx=8, pady=12)
        
        self.multiplication = Button(self.frame, text='*', command=lambda: self.button_click_effect(self.multiplication, lambda: self.set_operation('*')), width=8, font=('Verdana', 12), padx=10, pady=5)
        self.multiplication.grid(row=2, column=5, padx=8, pady=12)
        
        self.exponent = Button(self.frame, text='^', command=lambda: self.button_click_effect(self.exponent, lambda: self.set_operation('^')), width=8, font=('Verdana', 12), padx=10, pady=5)
        self.exponent.grid(row=2, column=6, padx=8, pady=12)
        
        self.result = ttk.Label(self.frame, text='Result: ', style='Bold.TLabel', font=('Verdana', 14, 'bold'))
        self.result.grid(row=3, column=1, columnspan=7, pady=20)
        
        self.calc_button = Button(self.frame, text='Calculate', command=lambda: self.button_click_effect(self.calc_button, self.calculate), width=12, font=('Verdana', 11), padx=15, pady=8)
        self.calc_button.grid(row=4, column=1, columnspan=2, padx=8, pady=12)
        
        self.clear_button = Button(self.frame, text='Clear', command=lambda: self.button_click_effect(self.clear_button, self.clear), width=12, font=('Verdana', 11), padx=15, pady=8)
        self.clear_button.grid(row=4, column=6, columnspan=2, padx=8, pady=12)
        
        self.quit_button = Button(self.frame, text='Quit', command=lambda: self.button_click_effect(self.quit_button, self.window.quit), width=18, font=('Verdana', 11), padx=15, pady=8)
        self.quit_button.grid(row=6, column=2, columnspan=5, padx=8, pady=12)
        
        self.history = Listbox(self.frame, height=5, width=50, font=('Verdana', 12))
        self.history.grid(row=5, column=1, columnspan=7, pady=10)
        
        self.bind_keys()
        self.configure_styles()
    
    def set_operation(self, op):
        self.operation = op
    
    def calculate(self):
        try:
            if self.operation not in self.functions:
                self.result.config(text="Error: No operation selected")
                return
            first_num = self.input1.get()
            second_num = self.input2.get()
            output = self.functions[self.operation](float(first_num), float(second_num))
            self.result.config(text='Result: ' + str(output))
            self.history.insert(END, f"{first_num} {self.operation} {second_num} = {output}")
        except ZeroDivisionError:
            self.result.config(text="Division by Zero Error occurred")
        except ValueError:
            self.result.config(text="Value Error occured")
        except FloatingPointError:
            self.result.config(text="Floating Point Error occurred")
    
    def clear(self):
        self.operation = ''
        self.input1.delete(0, END)
        self.input2.delete(0, END)
        self.result.config(text='Result: ')
    
    def button_click_effect(self, btn, callback=None):
        original_bg = btn.cget('bg')
        btn.config(bg='lightgray')
        if callback:
            callback()
        self.window.after(100, lambda: btn.config(bg=original_bg))
    
    def bind_keys(self):
        self.window.bind('<Return>', lambda _: self.button_click_effect(self.calc_button, self.calculate))
        self.window.bind('<Control-q>', lambda _: self.button_click_effect(self.quit_button, self.window.quit))
        self.window.bind('+', lambda _: self.button_click_effect(self.addition, lambda: self.set_operation('+')))
        self.window.bind('-', lambda _: self.button_click_effect(self.subtraction, lambda: self.set_operation('-')))
        self.window.bind('*', lambda _: self.button_click_effect(self.multiplication, lambda: self.set_operation('*')))
        self.window.bind('/', lambda _: self.button_click_effect(self.division, lambda: self.set_operation('/')))
    
    def configure_styles(self):
        style = ttk.Style()
        style.configure('TLabel', font=('Verdana', 10))
        style.configure('TButton', font=('Verdana', 10))
        style.configure('TEntry', font=('Verdana', 10))
        style.configure('Bold.TLabel', font=('Verdana', 10, 'bold'))

if __name__ == '__main__':
    root = Tk()
    root.resizable(False, False)
    app = Calculator(root)
    root.mainloop()