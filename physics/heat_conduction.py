import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk

def heat_conduction(T0, alpha, L, x, t):
    return T0 * np.exp(-alpha * (np.pi / L)**2 * t) * np.cos(np.pi * x / L)

def plot_graph(T0, alpha, L):
    x = np.linspace(0, L, 100)
    t = np.linspace(0, 10, 1000)
    X, T_grid = np.meshgrid(x, t)
    u = heat_conduction(T0, alpha, L, X, T_grid)
    
    # Create plot
    plt.figure(figsize=(8, 5))
    plt.imshow(u, extent=[0, L, 0, 10], aspect='auto', origin='lower', cmap='inferno')
    plt.colorbar(label="Temperature")
    plt.xlabel("Position (x)")
    plt.ylabel("Time (t)")
    plt.title("Heat Conduction in a Rod")
    plt.show()
    
    # Update data table
    for row in tree.get_children():
        tree.delete(row)
    for i in range(0, len(t), 50):  # Sample every 50 points
        tree.insert("", "end", values=(round(t[i], 2), round(u[i, 50], 4)))

def submit():
    try:
        T0 = float(temp_entry.get())
        alpha = float(alpha_entry.get())
        L = float(length_entry.get())
        plot_graph(T0, alpha, L)
    except ValueError:
        print("Please enter valid numerical values.")

# Create Tkinter window
root = tk.Tk()
root.title("Heat Conduction Calculator")

# Input fields
tk.Label(root, text="Initial Temperature (T0) [°C]:").grid(row=0, column=0)
temp_entry = tk.Entry(root)
temp_entry.grid(row=0, column=1)

tk.Label(root, text="Thermal Diffusivity (alpha) [m²/s]:").grid(row=1, column=0)
alpha_entry = tk.Entry(root)
alpha_entry.grid(row=1, column=1)

tk.Label(root, text="Rod Length (L) [m]:").grid(row=2, column=0)
length_entry = tk.Entry(root)
length_entry.grid(row=2, column=1)

# Submit button
tk.Button(root, text="Calculate", command=submit).grid(row=3, columnspan=2)

# Data table
tree = ttk.Treeview(root, columns=("Time", "Temperature"), show="headings")
tree.heading("Time", text="Time (s)")
tree.heading("Temperature", text="Temperature (°C)")
tree.grid(row=4, columnspan=2)

root.mainloop()

