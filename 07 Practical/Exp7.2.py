# Shreyas Rajendra Shigwan , Roll no. 90, CSE(AIML)
# Experiment 7.2: GUI for Calculating Areas of Geometric Figures

import tkinter as tk
from tkinter import ttk, messagebox
import math

def calculate():
    shape = combo_shape.get()
    try:
        if shape == "Circle":
            r = float(entry_p1.get())
            area = math.pi * r * r
            result_label.config(text=f"Area: {area:.2f}")
        elif shape == "Rectangle":
            l = float(entry_p1.get())
            w = float(entry_p2.get())
            area = l * w
            result_label.config(text=f"Area: {area:.2f}")
        elif shape == "Triangle":
            b = float(entry_p1.get())
            h = float(entry_p2.get())
            area = 0.5 * b * h
            result_label.config(text=f"Area: {area:.2f}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

def update_fields(event):
    shape = combo_shape.get()
    entry_p1.delete(0, tk.END)
    entry_p2.delete(0, tk.END)
    result_label.config(text="Area: ")
    
    if shape == "Circle":
        lbl_p1.config(text="Radius:")
        entry_p2.config(state='disabled')
        lbl_p2.config(text="N/A")
    elif shape == "Rectangle":
        lbl_p1.config(text="Length:")
        lbl_p2.config(text="Width:")
        entry_p2.config(state='normal')
    elif shape == "Triangle":
        lbl_p1.config(text="Base:")
        lbl_p2.config(text="Height:")
        entry_p2.config(state='normal')

root = tk.Tk()
root.title("Area Calculator")
root.geometry("350x250")

tk.Label(root, text="Select Shape:").pack(pady=5)
combo_shape = ttk.Combobox(root, values=["Circle", "Rectangle", "Triangle"])
combo_shape.pack()
combo_shape.bind("<<ComboboxSelected>>", update_fields)
combo_shape.current(0)

frame = tk.Frame(root, pady=10)
frame.pack()

lbl_p1 = tk.Label(frame, text="Radius:")
lbl_p1.grid(row=0, column=0)
entry_p1 = tk.Entry(frame)
entry_p1.grid(row=0, column=1)

lbl_p2 = tk.Label(frame, text="N/A")
lbl_p2.grid(row=1, column=0)
entry_p2 = tk.Entry(frame, state='disabled')
entry_p2.grid(row=1, column=1)

tk.Button(root, text="Calculate Area", command=calculate).pack(pady=10)
result_label = tk.Label(root, text="Area: ", font=("Arial", 12, "bold"))
result_label.pack()

tk.Label(root, text="# code by Shreyas Shigwan ", fg="blue").pack(side=tk.BOTTOM, pady=5)

root.mainloop()
