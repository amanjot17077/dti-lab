import math
import tkinter as tk
from tkinter import messagebox

def press(key):
    current = entry_var.get()
    try:
        if key == "C":
            entry_var.set("")
        elif key == "±":
            if current.startswith("-"):
                entry_var.set(current[1:])
            else:
                entry_var.set("-" + current)
        elif key == "%":
            result = float(current) / 100
            entry_var.set(str(result))
        elif key == "=":
            result = eval(current)
            entry_var.set(str(result))
        elif key == "sin":
            result = math.sin(math.radians(float(current)))
            entry_var.set(str(result))
        elif key == "cos":
            result = math.cos(math.radians(float(current)))
            entry_var.set(str(result))
        elif key == "tan":
            result = math.tan(math.radians(float(current)))
            entry_var.set(str(result))
        elif key == "log":
            result = math.log10(float(current))
            entry_var.set(str(result))
        elif key == "ln":
            result = math.log(float(current))
            entry_var.set(str(result))
        elif key == "sqrt":
            result = math.sqrt(float(current))
            entry_var.set(str(result))
        elif key == "π":
            entry_var.set(current + str(math.pi))
        elif key == "e":
            entry_var.set(current + str(math.e))
        else:
            entry_var.set(current + str(key))
    except Exception:
        messagebox.showerror("Error", "Invalid input")

# GUI Setup
root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("420x600")
root.configure(bg="black")

entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=("Helvetica", 32),
                 bd=0, bg="black", fg="white", justify="right")
entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=20)

frame = tk.Frame(root, bg="black")
frame.pack(expand=True, fill="both")

# Buttons layout (scientific + standard)
buttons = [
    ["sin", "cos", "tan", "log"],
    ["ln", "sqrt", "π", "e"],
    ["C", "±", "%", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "="]
]

def make_button(text, row, col, colspan=1):
    btn = tk.Button(frame, text=text, font=("Helvetica", 20),
                    fg="white", bg="#333333", activebackground="#666666",
                    bd=0, relief="flat", command=lambda: press(text))
    if text in ["+", "-", "*", "/", "="]:
        btn.configure(bg="#FF9500", activebackground="#FFB84D")
    if text in ["C", "±", "%"]:
        btn.configure(bg="#A6A6A6", fg="black", activebackground="#D9D9D9")
    btn.grid(row=row, column=col, columnspan=colspan,
             sticky="nsew", padx=2, pady=2)

for r, row in enumerate(buttons):
    for c, char in enumerate(row):
        if char == "0":
            make_button(char, r, c, colspan=2)
        else:
            make_button(char, r, c + (1 if r == 6 and c > 0 else 0))

# Configure grid weights
for i in range(len(buttons)):
    frame.grid_rowconfigure(i, weight=1)
for j in range(4):
    frame.grid_columnconfigure(j, weight=1)

root.mainloop()
