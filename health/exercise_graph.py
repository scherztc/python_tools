import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

# Functions

def calculate_mhr(age, type_of_machine):
    if type_of_machine == "Manual":
        return 206 - 0.88 * age
    elif type_of_machine == "Automatic":
        return 205.8 - 0.685 * age

def calculate_intensity_level(chr, mhr):
    if chr < 0.6 * mhr:
       return "Below Level"
    elif 0.6 * mhr < chr < 0.7 * mhr:
       return "Weight Loss"
    elif 0.7 * mhr < chr < 0.8 * mhr:
       return "Cardio"
    elif 0.8 * mhr < chr < 0.9 * mhr:
       return "Anaerobic (Hardcore)"
    else:
       return "Above Level"

def calculate_calories_burned(age, weight, chr, type_of_machine):
   if type_of_machine == "Manual":
       return 60 * (age * 0.074 - weight * 0.05741 + chr * 0.4472 - 20.402) / 4.184
   elif type_of_machine == "Automatic":
       return 60 * (age * 0.2017 + weight * 0.09036 + chr * 0.6309 - 55.0969) / 4.184

def plot_graph(age, type_of_machine, chr):
    mhr = calculate_mhr(age, type_of_machine)
    
    plt.figure(figsize=(10, 5))
    plt.axhline(y=mhr, color='r', linestyle='--', label='Maximum Heart Rate (MHR)')
    plt.axhline(y=chr, color='g', linestyle='-', label='Current Heart Rate (CHR)')
    plt.title('Heart Rate Analysis')
    plt.xlabel('Time')
    plt.ylabel('Heart Rate (beats per minute)')
    plt.legend()
    plt.grid(True)
    plt.show()

def display_results():
    try:
        age = int(age_entry.get())
        weight = float(weight_entry.get())
        chr = float(chr_entry.get())
        type_of_machine = type_of_machine_var.get()

        mhr = calculate_mhr(age, type_of_machine)
        intensity_level = calculate_intensity_level(chr, mhr)
        calories_burned = calculate_calories_burned(age, weight, chr, type_of_machine)
        
        result_text.set(f'Calories burnt per hour: {calories_burned:.2f}\nActivity level: {intensity_level}')
        
        plot_graph(age, type_of_machine, chr)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values.")

# GUI Setup

root = tk.Tk()
root.title("Heart Rate and Calories Burned Calculator")

tk.Label(root, text="Enter your age in years:").grid(row=0, column=0, padx=10, pady=10)
age_entry = tk.Entry(root)
age_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Enter your weight in pounds:").grid(row=1, column=0, padx=10, pady=10)
weight_entry = tk.Entry(root)
weight_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Enter your current heart rate (beats/minute):").grid(row=2, column=0, padx=10, pady=10)
chr_entry = tk.Entry(root)
chr_entry.grid(row=2, column=1, padx=10, pady=10)

tk.Label(root, text="Select the type of machine:").grid(row=3, column=0, padx=10, pady=10)
type_of_machine_var = tk.StringVar(value="Manual")
tk.Radiobutton(root, text="Manual", variable=type_of_machine_var, value="Manual").grid(row=3, column=1, padx=10, pady=5)
tk.Radiobutton(root, text="Automatic", variable=type_of_machine_var, value="Automatic").grid(row=3, column=2, padx=10, pady=5)

result_text = tk.StringVar()
tk.Label(root, textvariable=result_text, font=('Helvetica', 12), fg='blue').grid(row=5, column=0, columnspan=3, padx=10, pady=10)

tk.Button(root, text="Calculate", command=display_results).grid(row=4, column=0, columnspan=3, padx=10, pady=10)

root.mainloop()

