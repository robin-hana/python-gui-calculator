import tkinter as tk
from tkinter import ttk
import math

class Calculator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Python GUI Calculator")
        self.root.geometry("400x600")
        self.root.resizable(False, False)
        
        # Variables
        self.expression = ""
        self.input_text = tk.StringVar()
        
        # Create display
        self.create_display()
        
        # Create buttons
        self.create_buttons()
        
        self.root.mainloop()
    
    def create_display(self):
        # Main display frame
        display_frame = ttk.Frame(self.root)
        display_frame.pack(pady=20)
        
        # Entry widget for display
        entry = ttk.Entry(display_frame, textvariable=self.input_text, font=("Arial", 24), 
                         justify="right", state="readonly", width=20)
        entry.pack(ipady=20)
    
    def create_buttons(self):
        # Button frame
        buttons_frame = ttk.Frame(self.root)
        buttons_frame.pack(pady=10)
        
        # Button layout
        buttons = [
            ['C', '±', '%', '÷'],
            ['7', '8', '9', '×'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '.', '='],
        ]
        
        for r, row in enumerate(buttons):
            for c, text in enumerate(row):
                if text == '0':
                    btn = ttk.Button(buttons_frame, text=text, command=lambda t=text: self.on_button_click(t))
                    btn.grid(row=r, column=c, columnspan=2, ipadx=20, ipady=20, padx=2, pady=2, sticky="nsew")
                else:
                    btn = ttk.Button(buttons_frame, text=text, command=lambda t=text: self.on_button_click(t))
                    btn.grid(row=r, column=c, ipadx=20, ipady=20, padx=2, pady=2, sticky="nsew")
        
        # Configure grid weights
        for i in range(5):
            buttons_frame.rowconfigure(i, weight=1)
        for i in range(4):
            buttons_frame.columnconfigure(i, weight=1)
    
    def on_button_click(self, char):
        if char == 'C':
            self.expression = ""
            self.input_text.set("")
        elif char == '=':
            try:
                # Replace symbols for evaluation
                expr = self.expression.replace('×', '*').replace('÷', '/')
                result = eval(expr)
                self.input_text.set(str(result))
                self.expression = str(result)
            except:
                self.input_text.set("Error")
                self.expression = ""
        elif char == '±':
            if self.expression and self.expression != '0':
                if self.expression.startswith('-'):
                    self.expression = self.expression[1:]
                else:
                    self.expression = '-' + self.expression
                self.input_text.set(self.expression)
        elif char == '%':
            try:
                result = float(self.expression) / 100
                self.input_text.set(str(result))
                self.expression = str(result)
            except:
                self.input_text.set("Error")
        else:
            self.expression += char
            self.input_text.set(self.expression)

if __name__ == "__main__":
    Calculator()