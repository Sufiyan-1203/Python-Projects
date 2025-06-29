import tkinter as tk

def press(key):
    global expression
    expression += str(key)
    input_text.set(expression)

def clear():
    global expression
    expression = ""
    input_text.set("")

def equal():
    global expression
    try:
        result = str(eval(expression))
        input_text.set(result)
        expression = result
    except:
        input_text.set("Error")
        expression = ""

def backspace():
    global expression
    expression = expression[:-1]
    input_text.set(expression)

root = tk.Tk()
root.title("Calculator")
root.configure(bg="#1e1e1e")
root.resizable(False, False)

expression = ""
input_text = tk.StringVar()

entry_frame = tk.Frame(root, bd=2, bg="#000000", relief='ridge')
entry_frame.pack(pady=10, padx=10)

entry = tk.Entry(entry_frame, font=('Segoe UI', 24), textvariable=input_text,
                 bg="#1e1e1e", fg="white", bd=0, justify='right', insertbackground='white')
entry.pack(ipady=20, ipadx=10, fill='both')

btn_frame = tk.Frame(root, bg="#1e1e1e")
btn_frame.pack()

btn_style = {'font': ('Segoe UI', 16), 'bd': 0, 'fg': 'white', 'bg': '#333333',
             'activebackground': '#444444', 'activeforeground': 'white', 'width': 5, 'height': 2}

buttons = [
    ['%', 'CE', 'C', '⌫'],
    ['1/x', 'x²', '√', '/'],
    ['7', '8', '9', '*'],
    ['4', '5', '6', '-'],
    ['1', '2', '3', '+'],
    ['+/-', '0', '.', '=']
]

logic_map = {
    'C': clear,
    '=': equal,
    '⌫': backspace,
    '+/-': lambda: press('-') if not expression or expression[-1] in '+-*/' else None,
    '1/x': lambda: press("1/("),
    'x²': lambda: press("**2"),
    '√': lambda: press("**0.5"),
    'CE': clear,
}

for row_values in buttons:
    row = tk.Frame(btn_frame, bg="#1e1e1e")
    row.pack(expand=True, fill='both')
    for val in row_values:
        action = logic_map.get(val, lambda ch=val: press(ch))
        btn = tk.Button(row, text=val, command=action, **btn_style)
        if val == '=':
            btn.configure(bg="#00bcd4", fg="black", activebackground="#00acc1")
        btn.pack(side='left', expand=True, fill='both', padx=2, pady=2)

root.mainloop()
