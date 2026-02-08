from tkinter import *
from tkinter import ttk
import datetime
import os
os.makedirs("logs", exist_ok=True)

class Calculator:
    
    def __init__(self, root):
        self.window = root
        self.window.configure(bg='black')
        self.operation = None
        self.functions = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y,
            '^': lambda x, y: x ** y
        }
        self.easter_eggs_enabled = True
        self.dark_theme_enabled = True
        
        self.setup_ui()
        self.apply_theme(dark=True)
        
    def apply_theme(self, dark=True):
        if dark:
            back = 'black'
            fore = 'white'
            entry_bg = 'black'
        else:
            back = 'white'
            fore = 'black'
            entry_bg = 'white'
        
        self.window.configure(bg=back)
        
        style = ttk.Style()
        style.configure("TFrame", background=back)
        self.frame.configure(style="TFrame")
        style.configure("TEntry", fieldbackground=entry_bg, foreground=fore)
        for widget in self.frame.winfo_children():
            if isinstance(widget, (Label, Button, Checkbutton)):
                widget.configure(bg=back, fg=fore)
            elif isinstance(widget, Listbox):
                widget.configure(bg=entry_bg, fg=fore)
    
    def setup_ui(self):
        self.frame = ttk.Frame(self.window, padding=30, width=700, height=550, style='TFrame')
        self.frame.grid(row=0, column=0, sticky="nsew")
        self.frame.grid_propagate(False)
        self.window.title('Basic Python Calculator')
        self.window.grid_rowconfigure(0, weight=1)
        self.window.grid_columnconfigure(0, weight=1)
        
        for i in range(11):
            self.frame.grid_columnconfigure(i, weight=1)
        for i in range(6):
            self.frame.grid_rowconfigure(i, weight=1)
        
        text = Label(self.frame, text='Basic Python Calculator', font=('Verdana', 18, 'bold'), fg='white')
        text.grid(row=0, column=2, columnspan=5, pady=20)
        
        self.input1 = ttk.Entry(self.frame, width=20, font=('Verdana', 12), justify='center', style='TEntry')
        self.input1.grid(row=1, column=1, columnspan=3, padx=10, pady=15)
        
        self.input2 = ttk.Entry(self.frame, width=20, font=('Verdana', 12), justify='center', style='TEntry')
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
        
        self.result = Label(self.frame, text='Result: ', font=('Verdana', 14, 'bold'), fg='white')
        self.result.grid(row=3, column=1, columnspan=7, pady=20)
        
        self.calc_button = Button(self.frame, text='Calculate', command=lambda: self.button_click_effect(self.calc_button, self.calculate), width=12, font=('Verdana', 11), padx=15, pady=8)
        self.calc_button.grid(row=4, column=1, columnspan=2, padx=8, pady=12)
        
        self.clear_button = Button(self.frame, text='Clear', command=lambda: self.button_click_effect(self.clear_button, self.clear), width=12, font=('Verdana', 11), padx=15, pady=8)
        self.clear_button.grid(row=4, column=6, columnspan=2, padx=8, pady=12)
        
        self.quit_button = Button(self.frame, text='Quit', command=lambda: self.button_click_effect(self.quit_button, self.window.quit), width=18, font=('Verdana', 11), padx=15, pady=8)
        self.quit_button.grid(row=6, column=2, columnspan=5, padx=8, pady=12)
        
        self.history = Listbox(self.frame, height=5, width=50, font=('Verdana', 12))
        self.history.grid(row=5, column=1, columnspan=7, pady=10)
        
        self.settings_button = Button(self.frame, text='Settings', command=lambda: self.button_click_effect(self.settings_button, self.settings_handler), width=12, font=('Verdana', 11), padx=15, pady=8)
        self.settings_button.grid(row=4, column=3, columnspan=3, padx=8, pady=12)
        
        self.bind_keys()
        self.configure_styles()

    def configure_styles(self):
        style = ttk.Style()
        style.configure('TEntry', font=('Verdana', 10), background = 'black', fieldbackground='white')
        style.configure('TFrame', background = 'black', foreground = 'white')
        style.theme_use('alt')
        
    def settings_handler(self):
        settings_window = Toplevel(self.window)
        settings_window.title("Settings")
        
        eggs_toggled = BooleanVar(value=self.easter_eggs_enabled)
        dark_toggled = BooleanVar(value=self.dark_theme_enabled)
        
        def theme_settings():
            if dark_toggled.get():
                settings_window.configure(bg='black')
                for widget in settings_window.winfo_children():
                    if isinstance(widget, (Label, Button, Checkbutton)):
                        widget.configure(bg='black', fg='white')
            else:
                settings_window.configure(bg='white')
                for widget in settings_window.winfo_children():
                    if isinstance(widget, (Label, Button, Checkbutton)):
                        widget.configure(bg='white', fg='black')
                        
        theme_settings()
        
        def toggle_eggs():
            self.easter_eggs_enabled = eggs_toggled.get()
        def dark_theme():
            self.dark_theme_enabled = dark_toggled.get()
            if not dark_toggled.get():
                self.apply_theme(dark=False)
                theme_settings()
            else:
                self.apply_theme(dark=True)
                theme_settings()
                    
        dark_toggle = Checkbutton(settings_window, text=("Enable Dark Theme?"), variable=dark_toggled, command=dark_theme, font=('Verdana', 12), fg='white', bg='black', selectcolor='black')
        dark_toggle.pack(padx=20, pady=10)
            
        eggs_checkbox = Checkbutton(settings_window, text=("Enable Easter Eggs?"), variable=eggs_toggled, command=toggle_eggs, font=('Verdana', 12), fg='white', bg='black', selectcolor='black')
        eggs_checkbox.pack(padx=20, pady=20)
        
    def log_error(self, err_msg):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("logs\error_log.txt", "a") as log_file:
            log_file.write(f"{timestamp} - {err_msg}\n")
            
    def piastri(self):
        self.piastri_window = Toplevel(self.window)
        self.piastri_window.title("OSCAR PIASTRIIII")
        
        self.piastri_img = PhotoImage(file="piastri.png")
        img_label = Label(self.piastri_window, image=self.piastri_img)
        img_label.pack(padx=20, pady=20)

    
    def set_operation(self, op):
        self.operation = op
    
    def calculate(self):
        try:
            if self.operation not in self.functions:
                self.result.config(text="You have no operation selected. ERR:invopErr", fg='red')
                return
            first_num = self.input1.get()
            second_num = self.input2.get()
            output = self.functions[self.operation](float(first_num), float(second_num))
            self.result.config(text='Result: ' + str(output), fg='green')
            self.history.insert(END, f"{first_num} {self.operation} {second_num} = {output}")
            if abs(output - 81) < 1e-9:
                if self.easter_eggs_enabled:
                    self.piastri()
        except ZeroDivisionError:
            err_msg = "You cannot divide by zero. ERR:zerodivErr"
            self.result.config(text=err_msg, fg='red')
            self.log_error(err_msg)
        except ValueError:
            err_msg = "Your input(s) is not a valid number. ERR:valErr"
            self.result.config(text=err_msg, fg='red')
            self.log_error(err_msg)
        except FloatingPointError:
            err_msg = "A floating point error occurred. ERR:floatErr"
            self.result.config(text=err_msg, fg='red')
            self.log_error(err_msg)
    
    def clear(self):
        self.operation = ''
        self.input1.delete(0, END)
        self.input2.delete(0, END)
        self.result.config(text='Result: ', fg='white')
    
    def button_click_effect(self, btn, callback=None):
        original_bg = btn.cget('bg')
        btn.config(bg='lightgray')
        self.window.after(100, lambda: btn.config(bg=original_bg))
        if callback:
            callback()
    
    def bind_keys(self):
        self.window.bind('<Return>', lambda _: self.button_click_effect(self.calc_button, self.calculate))
        self.window.bind('<Control-q>', lambda _: self.button_click_effect(self.quit_button, self.window.quit))
        self.window.bind('+', lambda _: self.button_click_effect(self.addition, lambda: self.set_operation('+')))
        self.window.bind('-', lambda _: self.button_click_effect(self.subtraction, lambda: self.set_operation('-')))
        self.window.bind('*', lambda _: self.button_click_effect(self.multiplication, lambda: self.set_operation('*')))
        self.window.bind('/', lambda _: self.button_click_effect(self.division, lambda: self.set_operation('/')))
        self.window.bind('^', lambda _: self.button_click_effect(self.exponent, lambda: self.set_operation('^')))
        

if __name__ == '__main__':
    root = Tk()
    root.resizable(False, False)
    root.configure(bg='black')
    app = Calculator(root)
    root.mainloop()