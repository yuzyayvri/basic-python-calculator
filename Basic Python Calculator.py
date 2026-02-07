from tkinter import *
from tkinter import ttk
from tkinter import font

firstNum = ''
secondNum = ''
operation = ''

def setOperation(op):
    global operation
    operation = op

def Calculate():
    try:
        if operation not in ['+', '-', '*', '/']:
            result.config(text="Error: No operation selected")
            return
        firstNum=input1.get()
        secondNum=input2.get()
        if operation == '+':
            output = float(firstNum) + float(secondNum)
        elif operation == '-':
            output = float(firstNum) - float(secondNum)
        elif operation == '*':
            output = float(firstNum) * float(secondNum)
        elif operation == '/':
            output = float(firstNum) / float(secondNum)
        result.config(text='Result: ' + str(output))
    except ZeroDivisionError:
        result.config(text="Division by Zero Error occurred")
    except ValueError:
        result.config(text="Value Error occured")
    except FloatingPointError:
        result.config(text="Floating Point Error occurred")

def Clear():
    global operation
    operation = ''
    input1.delete(0, END)
    input2.delete(0, END)
    result.config(text='Result: ')

def button_click_effect(btn, callback=None):
    original_bg = btn.cget('bg')
    btn.config(bg='lightgray')
    if callback:
        callback()
    window.after(100, lambda: btn.config(bg=original_bg))

window = Tk()
frame = ttk.Frame(window,padding=10)
frame.grid()
window.title('Basic Python Calculator')

text = ttk.Label(frame, text='Basic Python Calculator', font=('Verdana', 14, 'bold'))
text.grid(row=0, column=0, columnspan=4, pady=10)

input1 = ttk.Entry(frame, width=15)
input1.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

input2 = ttk.Entry(frame, width=15)
input2.grid(row=1, column=2, columnspan=2, padx=5, pady=5)

addition = Button(frame, text='+', command=lambda:button_click_effect(addition, lambda:setOperation('+')), width=5, font=('Verdana', 10))
addition.grid(row=2, column=0, padx=5, pady=5)

subtraction = Button(frame, text='-', command=lambda:button_click_effect(subtraction, lambda:setOperation('-')), width=5, font=('Verdana', 10))
subtraction.grid(row=2, column=1, padx=5, pady=5)

division = Button(frame, text='/', command=lambda:button_click_effect(division, lambda:setOperation('/')), width=5, font=('Verdana', 10))
division.grid(row=2, column=2, padx=5, pady=5)

multiplication = Button(frame, text='*', command=lambda:button_click_effect(multiplication, lambda:setOperation('*')), width=5, font=('Verdana', 10))
multiplication.grid(row=2, column=3, padx=5, pady=5)

result = ttk.Label(frame, text='Result: ', style='Bold.TLabel')
result.grid(row=3, column=0, columnspan=4, pady=10)

button = Button(frame, text='Calculate', command=lambda:button_click_effect(button, Calculate), width=10, font=('Verdana', 10))
button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

clear = Button(frame, text='Clear', command=lambda:button_click_effect(clear, Clear), width=10, font=('Verdana', 10))
clear.grid(row=4, column=2, columnspan=2, padx=5, pady=5)

quit = Button(frame, text='Quit', command=lambda:button_click_effect(quit, window.quit), width=20, font=('Verdana', 10))
quit.grid(row=5, column=0, columnspan=4, padx=5, pady=5)

window.bind('<Return>', lambda _: button_click_effect(button, Calculate))
window.bind('<Control-q>', lambda _: button_click_effect(quit, window.quit))
window.bind('+', lambda _: button_click_effect(addition, lambda:setOperation('+')))
window.bind('-', lambda _: button_click_effect(subtraction, lambda:setOperation('-')))
window.bind('*', lambda _: button_click_effect(multiplication, lambda:setOperation('*')))
window.bind('/', lambda _: button_click_effect(division, lambda:setOperation('/')))

font = font.Font(family='Verdana', size=10)
style = ttk.Style()
style.configure('TLabel', font=('Verdana', 10))
style.configure('TButton', font=('Verdana', 10))
style.configure('TEntry', font=('Verdana', 10))
style.configure('Bold.TLabel', font=('Verdana', 10, 'bold'))

window.mainloop()