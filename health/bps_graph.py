import random
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

def sort_bps(bps):
    if 50 <= bps < 90:
        return "Hypotension"
    elif 90 <= bps < 120:
        return "Normal"
    elif 120 <= bps < 210:
        return "Hypertension"
    else:
        return "Out of Range"

def generate_readings(num):
    hypotension_count = 0
    normal_count = 0
    hypertension_count = 0

    for i in range(num):
        flip = random.randint(65, 140)
        category = sort_bps(flip)

        if category == "Hypotension":
            hypotension_count += 1
        elif category == "Normal":
            normal_count += 1
        elif category == "Hypertension":
            hypertension_count += 1

    return hypotension_count, normal_count, hypertension_count

def show_results():
    try:
        num = int(entry.get())
        if num <= 0:
            raise ValueError

        hypo, norm, hyper = generate_readings(num)
        
        result_text = f"Hypotension: {hypo}\nNormal: {norm}\nHypertension: {hyper}"
        messagebox.showinfo("Results", result_text)
        
        # Plotting the results
        categories = ['Hypotension', 'Normal', 'Hypertension']
        counts = [hypo, norm, hyper]
        
        plt.figure(figsize=(8, 6))
        plt.bar(categories, counts, color=['blue', 'green', 'red'])
        plt.xlabel('Categories')
        plt.ylabel('Count')
        plt.title('BPS Readings Distribution')
        plt.show()
        
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a positive integer.")

# Setting up the GUI
root = tk.Tk()
root.title("BPS Readings Analyzer")

label = tk.Label(root, text="Enter the number of BPS readings:")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=5)

button = tk.Button(root, text="Analyze", command=show_results)
button.pack(pady=20)

root.mainloop()

