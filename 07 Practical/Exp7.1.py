# Shreyas Rajendra Shigwan , Roll no. 90, CSE(AIML)
# Experiment 7.1: GUI for Developing Conversion Utilities

import tkinter as tk
from tkinter import messagebox

def convert_currency():
    try:
        val = float(entry_currency.get())
        res = val / 94.86
        lbl_currency_res.config(text=f"{res:.2f} USD")
    except ValueError:
        messagebox.showerror("Error", "Invalid Input")

def convert_temp():
    try:
        val = float(entry_temp.get())
        res = (val * 9/5) + 32
        lbl_temp_res.config(text=f"{res:.2f} °F")
    except ValueError:
        messagebox.showerror("Error", "Invalid Input")

def convert_length():
    try:
        val = float(entry_length.get())
        res = val / 12.0
        lbl_length_res.config(text=f"{res:.2f} Feet")
    except ValueError:
        messagebox.showerror("Error", "Invalid Input")

root = tk.Tk()
root.title("Conversion Utilities")
root.geometry("400x300")

frame1 = tk.Frame(root, pady=10)
frame1.pack()
tk.Label(frame1, text="Rupees:").pack(side=tk.LEFT)
entry_currency = tk.Entry(frame1)
entry_currency.pack(side=tk.LEFT)
tk.Button(frame1, text="Convert to USD", command=convert_currency).pack(side=tk.LEFT, padx=5)
lbl_currency_res = tk.Label(frame1, text="")
lbl_currency_res.pack(side=tk.LEFT)

frame2 = tk.Frame(root, pady=10)
frame2.pack()
tk.Label(frame2, text="Celsius:").pack(side=tk.LEFT)
entry_temp = tk.Entry(frame2)
entry_temp.pack(side=tk.LEFT)
tk.Button(frame2, text="Convert to Fahrenheit", command=convert_temp).pack(side=tk.LEFT, padx=5)
lbl_temp_res = tk.Label(frame2, text="")
lbl_temp_res.pack(side=tk.LEFT)

frame3 = tk.Frame(root, pady=10)
frame3.pack()
tk.Label(frame3, text="Inches:").pack(side=tk.LEFT)
entry_length = tk.Entry(frame3)
entry_length.pack(side=tk.LEFT)
tk.Button(frame3, text="Convert to Feet", command=convert_length).pack(side=tk.LEFT, padx=5)
lbl_length_res = tk.Label(frame3, text="")
lbl_length_res.pack(side=tk.LEFT)

tk.Label(root, text="#Code by Shreyas Shigwan", fg="blue").pack(side=tk.BOTTOM, pady=10)

root.mainloop()