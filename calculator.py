import tkinter as tk
from tkinter import messagebox

class calculator:
    def __init__(self,root):
        self.root= root
        self.root.title("Mwamburi's Calculator")
        self.root.geometry("400x600")
        self.root.resizable(True,True)

        #color palette
        self.bg_color="#2C3E50"
        self.display_color="#34495E"
        self.text_color="#ECF0F1"
        self.button_color="#2980B9"
        self.operator_color="#E67E22"
        self.equal_color="#27AE60"

        self.root.configure(bg=self.bg_color)

        # Display variable
        self.equation = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        """Creates the display and the button grid"""    
        #display screen
        display_frame = tk.Frame(self.root, bg=self.display_color, bd=0, highlightthickness=0)
        display_frame.pack(expand=True, fill="both")

        entry = tk.Entry(
            display_frame, 
            textvariable=self.equation, 
            font=("Helvetica", 32), 
            bg=self.display_color, 
            fg=self.text_color, 
            bd=0, 
            justify="right",
            insertbackground=self.text_color # cursor color
        )
        entry.pack(expand=True, fill="both", padx=20, pady=20)

        #buttons frame
        btn_frame = tk.Frame(self.root, bg=self.bg_color)
        btn_frame.pack(expand=True, fill="both")

        # Button labels organized by rows
        buttons = [
            ['C', '(', ')', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '.', '=', '']
        ]

         # Configure grid weight so buttons resize with window
        for i in range(4):
            btn_frame.grid_columnconfigure(i, weight=1)
        for i in range(5):
            btn_frame.grid_rowconfigure(i, weight=1)

        for row_idx, row in enumerate(buttons):
            for col_idx, label in enumerate(row):
                if label == '':
                    continue
                
                # Special colors for specific buttons
                color = self.button_color
                fg = "#2d3436"
                
                if label in ['/', '*', '-', '+', '(', ')']:
                    color = self.operator_color
                    fg = "white"
                elif label == '=':
                    color = self.equal_color
                    fg = "white"
                elif label == 'C':
                    color = "#ff7675"
                    fg = "white"

                btn = tk.Button(
                    btn_frame, 
                    text=label, 
                    font=("Helvetica", 16, "bold"),
                    bg=color, 
                    fg=fg,
                    relief="flat",
                    command=lambda l=label: self.on_button_click(l)
                )
                
                btn.grid(row=row_idx, column=col_idx, sticky="nsew", padx=2, pady=2)
    
        def on_button_click(self, char):
            """Logic for handling button presses."""
            if char == 'C':
                self.equation.set("")
            elif char == '=':
                try:
                    # eval() handles the math string conversion to result
                    expression = self.equation.get()
                    result = eval(expression)
                    self.equation.set(result)
                except ZeroDivisionError:
                    messagebox.showerror("Math Error", "Cannot divide by zero")
                    self.equation.set("")
                except Exception:
                    messagebox.showerror("Error", "Invalid Expression")
                    self.equation.set("")
            else:
                current = self.equation.get()
                self.equation.set(current + str(char))

if __name__ == "__main__":
    root = tk.Tk()
    app = calculator(root)
    root.mainloop()