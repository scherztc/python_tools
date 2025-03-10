import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk

def displacement_in_loaded_string(T, mu, A0, x, t):
    c = np.sqrt(T / mu)
    return A0 * np.sin(np.pi * x) * np.cos(c * t)

def plot_graph(T, mu, A0):
    x = np.linspace(0, 1, 100)
    t = np.linspace(0, 10, 1000)
    X, T_grid = np.meshgrid(x, t)
    u = displacement_in_loaded_string(T, mu, A0, X, T_grid)
    
    # Create plot
    plt.figure(figsize=(8, 5))
    plt.imshow(u, extent=[0, 1, 0, 10], aspect='auto', origin='lower', cmap='viridis')
    plt.colorbar(label="Displacement")
    plt.xlabel("Position (x)")
    plt.ylabel("Time (t)")
    plt.title("Displacement in a Loaded String")
    plt.show()
    
    # Update data table
    for row in tree.get_children():
        tree.delete(row)
    for i in range(0, len(t), 50):  # Sample every 50 points
        tree.insert("", "end", values=(round(t[i], 2), round(u[i, 50], 4)))

def submit():
    try:
        T = float(tension_entry.get())
        mu = float(mass_density_entry.get())
        A0 = float(amplitude_entry.get())
        plot_graph(T, mu, A0)
    except ValueError:
        print("Please enter valid numerical values.")

# Create Tkinter window
root = tk.Tk()
root.title("Loaded String Displacement Calculator")

# Input fields
tk.Label(root, text="Tension (T) [N]:").grid(row=0, column=0)
tension_entry = tk.Entry(root)
tension_entry.grid(row=0, column=1)

tk.Label(root, text="Mass Density (mu) [kg/m]:").grid(row=1, column=0)
mass_density_entry = tk.Entry(root)
mass_density_entry.grid(row=1, column=1)

tk.Label(root, text="Initial Amplitude (A0) [m]:").grid(row=2, column=0)
amplitude_entry = tk.Entry(root)
amplitude_entry.grid(row=2, column=1)

# Submit button
tk.Button(root, text="Calculate", command=submit).grid(row=3, columnspan=2)

# Data table
tree = ttk.Treeview(root, columns=("Time", "Displacement"), show="headings")
tree.heading("Time", text="Time (s)")
tree.heading("Displacement", text="Displacement (m)")
tree.grid(row=4, columnspan=2)

root.mainloop()

