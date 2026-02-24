from tkinter import *
from tkinter import ttk
import datetime
import os

DIR = os.path.dirname(os.path.abspath(__file__))
LOG_PATH = os.path.join(DIR, "logs")
os.makedirs(LOG_PATH, exist_ok=True)

class Calculator:
    def __init__(self, root):
        self.window = root
        self.operation = None
        self.functions = {
            '+': lambda x, y: x + y, '-': lambda x, y: x - y,
            '*': lambda x, y: x * y, '/': lambda x, y: x / y,
            '^': lambda x, y: x ** y, '√': lambda x, y: x ** (1/y)
        }
        self.easter_eggs_enabled = True
        self.dark_theme_enabled = True
        self.theme_registry = []
        
        self.setup_ui()
        self.apply_theme(dark=True)

    def apply_theme(self, dark=True):
        self.dark_theme_enabled = dark
        colors = {"bg": "black" if dark else "white", "fg": "white" if dark else "black"}
        self.current_theme = colors
        self.window.configure(bg=colors["bg"])
        ttk.Style().configure("TFrame", background=colors["bg"])
        
        for w in self.theme_registry:
            w.configure(bg=colors["bg"], fg=colors["fg"])
            
            if isinstance(w, (Button, Checkbutton)):
                w.configure(activebackground="lightgray", activeforeground=colors["fg"])
                if isinstance(w, Checkbutton):
                    w.configure(selectcolor=colors["bg"])
            
            elif isinstance(w, Entry):
                w.configure(insertbackground=colors["fg"], highlightbackground=colors["bg"])
                
            elif isinstance(w, Listbox):
                w.configure(highlightbackground=colors["bg"])

    def create_btn(self, text, row, col, cmd, colspan=1, width=8):
        btn = Button(self.frame, text=text, width=width, font=('Verdana', 11), padx=10, pady=5,
                     command=lambda: self.button_click_effect(btn, cmd))
        btn.grid(row=row, column=col, columnspan=colspan, padx=8, pady=8)
        self.theme_registry.append(btn)
        return btn

    def setup_ui(self):
        self.frame = ttk.Frame(self.window, padding=30, width=700, height=550)
        self.frame.grid(row=0, column=0, sticky="nsew")
        self.frame.grid_propagate(False)
        self.window.title('Basic Python Calculator')
        
        for i in range(11): self.frame.grid_columnconfigure(i, weight=1)
        for i in range(8): self.frame.grid_rowconfigure(i, weight=1)

        hdr = Label(self.frame, text='Basic Python Calculator v0.6.0', font=('Verdana', 18, 'bold'))
        hdr.grid(row=0, column=2, columnspan=5, pady=20)
        
        self.input1 = Entry(self.frame, width=20, font=('Verdana', 24), justify='center')
        self.input1.grid(row=1, column=1, columnspan=3, padx=10)
        self.input2 = Entry(self.frame, width=20, font=('Verdana', 24), justify='center')
        self.input2.grid(row=1, column=5, columnspan=3, padx=10)
        
        self.result = Label(self.frame, text='Result: ', font=('Verdana', 14, 'bold'))
        self.result.grid(row=4, column=1, columnspan=7, pady=20)

        self.theme_registry.extend([hdr, self.input1, self.input2, self.result])

        ops = [('+', 2, 3), ('-', 2, 4), ('/', 2, 5), ('*', 3, 3), ('^', 3, 4), ('√', 3, 5)]
        for txt, r, c in ops:
            self.create_btn(txt, r, c, lambda t=txt: self.set_operation(t))

        self.create_btn('Settings', 5, 1, self.settings_handler, colspan=2, width=12)
        self.calc_btn = self.create_btn('Calculate', 5, 3, self.calculate, colspan=3, width=12)
        self.create_btn('Clear', 5, 6, self.clear, colspan=2, width=12)
        self.create_btn('Quit', 7, 2, self.window.quit, colspan=5, width=18)

        self.history = Listbox(self.frame, height=5, width=50, font=('Verdana', 12))
        self.history.grid(row=6, column=1, columnspan=7, pady=10)
        self.theme_registry.append(self.history)
        self.bind_keys()

    def settings_handler(self):
        sw = Toplevel(self.window)
        sw.title("Settings")
        d_var, e_var = BooleanVar(value=self.dark_theme_enabled), BooleanVar(value=self.easter_eggs_enabled)

        def sync():
            self.apply_theme(d_var.get())
            bg, fg = self.current_theme["bg"], self.current_theme["fg"]
            sw.configure(bg=bg)
            for w in sw.winfo_children():
                if isinstance(w, Checkbutton):
                    w.configure(bg=bg, fg=fg, selectcolor=bg, activebackground=bg)

        Checkbutton(sw, text="Dark Theme", variable=d_var, command=sync, font=('Verdana', 12)).pack(padx=20, pady=10)
        Checkbutton(sw, text="Easter Eggs", variable=e_var, command=lambda: setattr(self, 'easter_eggs_enabled', e_var.get()), font=('Verdana', 12)).pack(padx=20, pady=20)
        sync()

    def _display_error(self, msg):
        self.result.config(text=msg, fg='red')
        with open(os.path.join(LOG_PATH, "error_log.txt"), "a") as f:
            f.write(f"[{datetime.datetime.now():%Y-%m-%d %H:%M:%S}] {msg}\n")
        self.window.after(3000, self.clear)

    def set_operation(self, op): self.operation = op

    def calculate(self):
        try:
            if not self.operation: raise ValueError("No operation selected")
            v1, v2 = float(self.input1.get()), float(self.input2.get())
            res = self.functions[self.operation](v1, v2)
            self.result.config(text=f'Result: {res}', fg=self.current_theme["fg"])
            self.history.insert(0, f"{v1} {self.operation} {v2} = {res}")
            if self.history.size() > 15: self.history.delete(END)
            if abs(res - 81) < 1e-9 and self.easter_eggs_enabled: print("Oscar Piastri!") 
        except Exception as e:
            self._display_error(str(e))

    def clear(self):
        self.operation = None
        for i in (self.input1, self.input2): i.delete(0, END)
        self.result.config(text='Result: ', fg=self.current_theme["fg"])

    def button_click_effect(self, btn, callback=None):
        orig = btn.cget('bg')
        btn.config(bg='lightgray')
        self.window.after(100, lambda: btn.config(bg=orig))
        if callback: callback()

    def bind_keys(self):
        self.window.bind('<Return>', lambda _: self.button_click_effect(self.calc_btn, self.calculate))
        for k in ['+', '-', '*', '/', '^']:
            self.window.bind(k, lambda e, op=k: self.set_operation(op))

if __name__ == '__main__':
    root = Tk()
    root.resizable(False, False)
    Calculator(root)
    root.mainloop()