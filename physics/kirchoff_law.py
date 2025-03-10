import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk

def current_in_circuit(R, L, a, t):
    return (a / R) * ((t * L / R) - (L**2 / R**2)) + (a * L**2 / R**3) * np.exp(-R * t / L)

def plot_graph(R, L, a):
    t = np.linspace(0, 10, 1000)
    i_t = current_in_circuit(R, L, a, t)
    
    # Create plot
    plt.figure(figsize=(8, 5))
    plt.plot(t, i_t, label="Current I(t)")
    plt.xlabel("Time (s)")
    plt.ylabel("Current (A)")
    plt.title("Current in RL Circuit Over Time")
    plt.legend()
    plt.grid()
    plt.show()
    
    # Update data table
    for row in tree.get_children():
        tree.delete(row)
    for i in range(0, len(t), 50):  # Sample every 50 points
        tree.insert("", "end", values=(round(t[i], 2), round(i_t[i], 4)))

def submit():
    try:
        R = float(resistance_entry.get())
        L = float(inductance_entry.get())
        a = float(a_entry.get())
        plot_graph(R, L, a)
    except ValueError:
        print("Please enter valid numerical values.")

# Create Tkinter window
root = tk.Tk()
root.title("RL Circuit Current Calculator")

# Input fields
tk.Label(root, text="Resistance (R) [ohms]:").grid(row=0, column=0)
resistance_entry = tk.Entry(root)
resistance_entry.grid(row=0, column=1)

tk.Label(root, text="Inductance (L) [henries]:").grid(row=1, column=0)
inductance_entry = tk.Entry(root)
inductance_entry.grid(row=1, column=1)

tk.Label(root, text="Constant a [V/s]:").grid(row=2, column=0)
a_entry = tk.Entry(root)
a_entry.grid(row=2, column=1)

# Submit button
tk.Button(root, text="Calculate", command=submit).grid(row=3, columnspan=2)

# Data table
tree = ttk.Treeview(root, columns=("Time", "Current"), show="headings")
tree.heading("Time", text="Time (s)")
tree.heading("Current", text="Current (A)")
tree.grid(row=4, columnspan=2)

root.mainloop()

