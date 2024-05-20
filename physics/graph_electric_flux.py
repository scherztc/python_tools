import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt

def calculate_electric_flux_density(rho, r):
    a = 3  # Internal radius in cm
    b = 6  # External radius in cm
    
    if r <= 0:
        return "Invalid input: r must be greater than 0"
    
    if 0 < r <= a:
        D = (rho * r) / 2
    elif a < r < b:
        D = (rho * a**2) / (2 * r)
    else:
        D = 0

    return D

def plot_graph(rho):
    r_values = [i for i in range(1, 10)]
    D_values = [calculate_electric_flux_density(rho, r) for r in r_values]
    
    plt.figure(figsize=(10, 5))
    plt.plot(r_values, D_values, marker='o')
    plt.title(f'Electric Flux Density D vs Radial Distance r for rho = {rho} nC/cm^3')
    plt.xlabel('Radial Distance r (cm)')
    plt.ylabel('Electric Flux Density D (nC/cm^2)')
    plt.grid(True)
    plt.show()

def update_trace_table(rho):
    rows = []
    for r in range(1, 10):
        D = calculate_electric_flux_density(rho, r)
        rows.append((r, D))
    
    for row in trace_table.get_children():
        trace_table.delete(row)
    
    for row in rows:
        trace_table.insert("", "end", values=row)

def on_calculate():
    try:
        rho = float(rho_entry.get())
        r = float(r_entry.get())
        
        D = calculate_electric_flux_density(rho, r)
        
        result_label.config(text=f"The electric flux density D at r = {r} cm is: {D} nC/cm^2")
        
        plot_graph(rho)
        update_trace_table(rho)
    
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter numerical values.")

# Create the main window
root = tk.Tk()
root.title("Electric Flux Density Calculator")

# Create and place the widgets
ttk.Label(root, text="Enter the charge density (rho) in nC/cm^3:").grid(column=0, row=0, padx=10, pady=10)
rho_entry = ttk.Entry(root)
rho_entry.grid(column=1, row=0, padx=10, pady=10)

ttk.Label(root, text="Enter the radial distance (r) in cm:").grid(column=0, row=1, padx=10, pady=10)
r_entry = ttk.Entry(root)
r_entry.grid(column=1, row=1, padx=10, pady=10)

calculate_button = ttk.Button(root, text="Calculate", command=on_calculate)
calculate_button.grid(column=0, row=2, columnspan=2, padx=10, pady=10)

result_label = ttk.Label(root, text="")
result_label.grid(column=0, row=3, columnspan=2, padx=10, pady=10)

# Trace Table
ttk.Label(root, text="Trace Table:").grid(column=0, row=4, columnspan=2, padx=10, pady=10)

trace_table = ttk.Treeview(root, columns=("r", "D"), show="headings")
trace_table.heading("r", text="Radial Distance r (cm)")
trace_table.heading("D", text="Electric Flux Density D (nC/cm^2)")

trace_table.grid(column=0, row=5, columnspan=2, padx=10, pady=10)

# Start the main event loop
root.mainloop()

