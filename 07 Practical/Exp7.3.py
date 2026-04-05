# Shreyas Rajendra Shigwan , Roll no. 90, CSE(AIML)
# Experiment 7.3: College Admission Registration Form

import tkinter as tk
from tkinter import messagebox

def submit_form():
    name = entry_name.get()
    branch = var_branch.get()
    
    games = []
    if var_cricket.get(): games.append("Cricket")
    if var_football.get(): games.append("Football")
    if var_badminton.get(): games.append("Badminton")
    
    if not name:
        messagebox.showwarning("Validation", "Please enter Student Name")
        return
        
    game_str = " and ".join(games) if games else "no games"
    
    # Matches the output format in the image
    result_text = f"Your name is {name}.\n"
    result_text += f"{name} is from {branch} Department.\n"
    result_text += f"{name} is from {branch} Department and enjoy playing {game_str}."
    
    lbl_output.config(text=result_text)

root = tk.Tk()
root.title("College Admission Registration Form")
root.geometry("500x400")

# Header
tk.Label(root, text="TK", font=("Arial", 14, "bold"), fg="red", anchor="w").pack(fill="both", padx=20, pady=5)

form_frame = tk.Frame(root, padx=20, pady=10)
form_frame.pack(fill="both")

# Name
tk.Label(form_frame, text="Enter Student Name:").grid(row=0, column=0, sticky="w", pady=5)
entry_name = tk.Entry(form_frame, width=30)
entry_name.grid(row=0, column=1, columnspan=3, sticky="w")
entry_name.insert(0, "Shreyas") # Default value as per image

# Branch
tk.Label(form_frame, text="Select Your Branch:").grid(row=1, column=0, sticky="w", pady=5)
var_branch = tk.StringVar(value="CSE(AIML)")
tk.Radiobutton(form_frame, text="CSE(AIML)", variable=var_branch, value="CSE(AIML)").grid(row=1, column=1, sticky="w")
tk.Radiobutton(form_frame, text="Information Technology", variable=var_branch, value="Information Technology").grid(row=1, column=2, sticky="w")

# Games
tk.Label(form_frame, text="Select Favorite Games:").grid(row=2, column=0, sticky="w", pady=5)
var_cricket = tk.BooleanVar(value=True)
var_football = tk.BooleanVar()
var_badminton = tk.BooleanVar()

tk.Checkbutton(form_frame, text="Cricket", variable=var_cricket).grid(row=2, column=1, sticky="w")
tk.Checkbutton(form_frame, text="Football", variable=var_football).grid(row=2, column=2, sticky="w")
tk.Checkbutton(form_frame, text="Badminton", variable=var_badminton).grid(row=2, column=3, sticky="w")

# Submit Button
tk.Button(root, text="Submit", command=submit_form).pack(pady=10)

# Output Section
tk.Label(root, text="OUTPUT:", fg="blue", font=("Arial", 10, "bold"), anchor="w").pack(fill="both", padx=20)
lbl_output = tk.Label(root, text="", justify="left", anchor="w")
lbl_output.pack(fill="both", padx=20)

tk.Label(root, text="# code by Shreyas Shigwan", fg="gray").pack(side=tk.BOTTOM, pady=10)

root.mainloop()