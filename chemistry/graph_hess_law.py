import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

def calculate_enthalpy_change(h1, h2):
    h2_reversed = -h2
    delta_h = h1 + h2_reversed
    return delta_h

def on_calculate():
    try:
        h1 = float(entry_h1.get())
        h2 = float(entry_h2.get())
        delta_h = calculate_enthalpy_change(h1, h2)
        result_label.config(text=f"Enthalpy change: {delta_h} kJ")
        plot_graph(h1, h2, delta_h)
    except ValueError:
        messagebox.showerror("Input error", "Please enter valid numbers for enthalpy changes.")

def plot_graph(h1, h2, delta_h):
    reactions = ['C + O2 -> CO2', 'CO + 1/2 O2 -> CO2', 'C + 1/2 O2 -> CO']
    enthalpies = [h1, h2, delta_h]

    plt.figure(figsize=(8, 6))
    plt.bar(reactions, enthalpies, color=['blue', 'green', 'red'])
    plt.xlabel('Reactions')
    plt.ylabel('Enthalpy Change (kJ)')
    plt.title('Enthalpy Changes of Reactions')
    plt.grid(True)
    plt.show()

# Create the main window
root = tk.Tk()
root.title("Hess's Law Calculator")

# Create and place the widgets
tk.Label(root, text="Enter the enthalpy change for reaction C + O2 -> CO2 (kJ):").grid(row=0, column=0, padx=10, pady=10)
entry_h1 = tk.Entry(root)
entry_h1.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Enter the enthalpy change for reaction CO + 1/2 O2 -> CO2 (kJ):").grid(row=1, column=0, padx=10, pady=10)
entry_h2 = tk.Entry(root)
entry_h2.grid(row=1, column=1, padx=10, pady=10)

calculate_button = tk.Button(root, text="Calculate", command=on_calculate)
calculate_button.grid(row=2, column=0, columnspan=2, pady=20)

result_label = tk.Label(root, text="Enthalpy change: ")
result_label.grid(row=3, column=0, columnspan=2, pady=10)

# Run the GUI event loop
root.mainloop()

