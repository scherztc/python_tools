import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk

def voltage_in_lumped_rc(R, C, V0, t):
    return V0 * np.exp(-t / (R * C))

def plot_graph(R, C, V0):
    t = np.linspace(0, 10, 1000)
    v_t = voltage_in_lumped_rc(R, C, V0, t)
    
    # Create plot
    plt.figure(figsize=(8, 5))
    plt.plot(t, v_t, label="Voltage V(t)")
    plt.xlabel("Time (s)")
    plt.ylabel("Voltage (V)")
    plt.title("Voltage Decay in Lumped RC Line")
    plt.legend()
    plt.grid()
    plt.show()
    
    # Update data table
    for row in tree.get_children():
        tree.delete(row)
    for i in range(0, len(t), 50):  # Sample every 50 points
        tree.insert("", "end", values=(round(t[i], 2), round(v_t[i], 4)))

def submit():
    try:
        R = float(resistance_entry.get())
        C = float(capacitance_entry.get())
        V0 = float(voltage_entry.get())
        plot_graph(R, C, V0)
    except ValueError:
        print("Please enter valid numerical values.")

# Create Tkinter window
root = tk.Tk()
root.title("Lumped RC Line Voltage Calculator")

# Input fields
tk.Label(root, text="Resistance (R) [ohms]:").grid(row=0, column=0)
resistance_entry = tk.Entry(root)
resistance_entry.grid(row=0, column=1)

tk.Label(root, text="Capacitance (C) [farads]:").grid(row=1, column=0)
capacitance_entry = tk.Entry(root)
capacitance_entry.grid(row=1, column=1)

tk.Label(root, text="Initial Voltage (V0) [volts]:").grid(row=2, column=0)
voltage_entry = tk.Entry(root)
voltage_entry.grid(row=2, column=1)

# Submit button
tk.Button(root, text="Calculate", command=submit).grid(row=3, columnspan=2)

# Data table
tree = ttk.Treeview(root, columns=("Time", "Voltage"), show="headings")
tree.heading("Time", text="Time (s)")
tree.heading("Voltage", text="Voltage (V)")
tree.grid(row=4, columnspan=2)

root.mainloop()

