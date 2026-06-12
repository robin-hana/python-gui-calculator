import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Python GUI Calculator")
        self.root.geometry("360x500")
        self.root.resizable(False, False)
        
        self.expression = ""
        self.display_var = tk.StringVar()
        
        # Display
        display = tk.Entry(root, textvariable=self.display_var, font=("Arial", 24), 
                          bd=0, insertwidth=4, width=14, borderwidth=4, 
                          justify="right", state="readonly")
        display.grid(row=0, column=0, columnspan=4, padx=10, pady=20, ipadx=8, ipady=20)
        
        # Buttons
        buttons = [
            'C', '±', '%', '/',
            '7', '8', '9', '*',
            '4', '5', '6', '-',
            '1', '2', '3', '+',
            '0', '.', '='
        ]
        
        row = 1
        col = 0
        for button in buttons:
            if button == '0':
                btn = tk.Button(root, text=button, font=("Arial", 18), padx=20, pady=20,
                               command=lambda b=button: self.on_button_click(b))
                btn.grid(row=row, column=col, columnspan=2, sticky="nsew")
                col += 2
            elif button == '=':
                btn = tk.Button(root, text=button, font=("Arial", 18, "bold"), padx=20, pady=20,
                               bg="#ff9500", fg="white",
                               command=lambda b=button: self.on_button_click(b))
                btn.grid(row=row, column=col, rowspan=2, sticky="nsew")
            else:
                btn = tk.Button(root, text=button, font=("Arial", 18), padx=20, pady=20,
                               command=lambda b=button: self.on_button_click(b))
                btn.grid(row=row, column=col, sticky="nsew")
                col += 1
            
            if col > 3:
                col = 0
                row += 1
        
        # Make grid expandable
        for i in range(4):
            root.columnconfigure(i, weight=1)
        for i in range(1, 6):
            root.rowconfigure(i, weight=1)

    def on_button_click(self, char):
        if char == 'C':
            self.expression = ""
        elif char == '±':
            if self.expression and self.expression[0] == '-':
                self.expression = self.expression[1:]
            elif self.expression:
                self.expression = '-' + self.expression
        elif char == '%':
            try:
                self.expression = str(float(self.expression) / 100)
            except:
                self.expression = "Error"
        elif char == '=':
            try:
                result = eval(self.expression, {"__builtins__": {}}, {})
                self.expression = str(result)
            except:
                self.expression = "Error"
        else:
            if self.expression == "Error":
                self.expression = ""
            self.expression += char
        
        self.display_var.set(self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()