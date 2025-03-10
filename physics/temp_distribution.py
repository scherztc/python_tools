import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk

def wave_propagation(A0, c, L, x, t):
    return A0 * np.sin(np.pi * (x - c * t) / L)

def plot_graph(A0, c, L):
    x = np.linspace(0, L, 100)
    t = np.linspace(0, 10, 1000)
    X, T_grid = np.meshgrid(x, t)
    u = wave_propagation(A0, c, L, X, T_grid)
    
    # Create plot
    plt.figure(figsize=(8, 5))
    plt.imshow(u, extent=[0, L, 0, 10], aspect='auto', origin='lower', cmap='plasma')
    plt.colorbar(label="Wave Amplitude")
    plt.xlabel("Position (x)")
    plt.ylabel("Time (t)")
    plt.title("Wave Propagation in One Direction")
    plt.show()
    
    # Update data table
    for row in tree.get_children():
        tree.delete(row)
    for i in range(0, len(t), 50):  # Sample every 50 points
        tree.insert("", "end", values=(round(t[i], 2), round(u[i, 50], 4)))

def submit():
    try:
        A0 = float(amplitude_entry.get())
        c = float(speed_entry.get())
        L = float(length_entry.get())
        plot_graph(A0, c, L)
    except ValueError:
        print("Please enter valid numerical values.")

# Create Tkinter window
root = tk.Tk()
root.title("Wave Propagation Calculator")

# Input fields
tk.Label(root, text="Initial Amplitude (A0) [m]:").grid(row=0, column=0)
amplitude_entry = tk.Entry(root)
amplitude_entry.grid(row=0, column=1)

tk.Label(root, text="Wave Speed (c) [m/s]:").grid(row=1, column=0)
speed_entry = tk.Entry(root)
speed_entry.grid(row=1, column=1)

tk.Label(root, text="Domain Length (L) [m]:").grid(row=2, column=0)
length_entry = tk.Entry(root)
length_entry.grid(row=2, column=1)

# Submit button
tk.Button(root, text="Calculate", command=submit).grid(row=3, columnspan=2)

# Data table
tree = ttk.Treeview(root, columns=("Time", "Amplitude"), show="headings")
tree.heading("Time", text="Time (s)")
tree.heading("Amplitude", text="Amplitude (m)")
tree.grid(row=4, columnspan=2)

root.mainloop()

