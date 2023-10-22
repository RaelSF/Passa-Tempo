import tkinter as tk
from tkinter import ttk

# Define a class for the calculator application
class CalculatorApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # Set the title of the window
        self.title("Calculator")

        # Set the size of the window
        self.geometry("400x500")

        # Create a frame to hold the widgets
        self.frame = ttk.Frame(self, padding="10")
        self.frame.grid(row=0, column=0, sticky=tk.W+tk.E+tk.N+tk.S)

        # Create a variable to store the text of the entry widget
        self.entry_text = tk.StringVar()

        # Create an entry widget to display the calculation
        self.entry = ttk.Entry(self.frame, textvariable=self.entry_text, width=25)
        self.entry.grid(row=0, column=0, columnspan=4)

        # Define the function to perform the calculation
        def calculate():
            try:
                self.entry_text.set(eval(self.entry_text.get()))
            except Exception as e:
                self.entry_text.set("Error")

        # Create buttons for numbers, operators, and calculations
        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("C", 4, 2), ("+", 4, 3),
            ("=", 5, 2)
        ]

        # Create the buttons and add them to the grid layout
        for text, row, column in buttons:
            command = None

            if text == "C":
                command = lambda: self.entry_text.set("")
            elif text == "=":
                command = calculate
            else:
                command = lambda text=text: self.entry_text.set(self.entry_text.get() + text)

            button = ttk.Button(self.frame, text=text, command=command)
            button.grid(row=row, column=column, padx=5, pady=5)

        # Bind the 'Enter' key to the calculate function
        self.bind("<Return>", lambda event: calculate())

# Create an instance of the calculator application and run it
app = CalculatorApp()
app.mainloop()