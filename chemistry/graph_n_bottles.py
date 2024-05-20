import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

def distribute_volume(total_volume, num_bottles):
    if num_bottles <= 0:
        raise ValueError("Number of bottles must be a positive integer.")
    if total_volume < 0:
        raise ValueError("Total volume must be a non-negative number.")
    
    volume_per_bottle = total_volume / num_bottles
    distribution = [volume_per_bottle] * num_bottles
    
    return distribution

def plot_distribution(distribution):
    plt.figure(figsize=(10, 6))
    plt.bar(range(1, len(distribution) + 1), distribution, color='blue')
    plt.xlabel('Bottle Number')
    plt.ylabel('Volume')
    plt.title('Volume Distribution Among Bottles')
    plt.show()

def on_calculate():
    try:
        total_volume = float(total_volume_entry.get())
        num_bottles = int(num_bottles_entry.get())
        
        distribution = distribute_volume(total_volume, num_bottles)
        
        result_label.config(text=f"Each of the {num_bottles} bottles will contain {distribution[0]:.2f} liters.")
        plot_distribution(distribution)
        
    except ValueError as e:
        messagebox.showerror("Input Error", str(e))

# Set up the main application window
root = tk.Tk()
root.title("N-Bottle Problem Solver")

# Create and place the labels and entries
tk.Label(root, text="Total Volume (e.g., in liters):").grid(row=0, column=0, padx=10, pady=10)
total_volume_entry = tk.Entry(root)
total_volume_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Number of Bottles:").grid(row=1, column=0, padx=10, pady=10)
num_bottles_entry = tk.Entry(root)
num_bottles_entry.grid(row=1, column=1, padx=10, pady=10)

# Create and place the calculate button
calculate_button = tk.Button(root, text="Calculate", command=on_calculate)
calculate_button.grid(row=2, columnspan=2, padx=10, pady=10)

# Create and place the result label
result_label = tk.Label(root, text="")
result_label.grid(row=3, columnspan=2, padx=10, pady=10)

# Start the GUI event loop
root.mainloop()

