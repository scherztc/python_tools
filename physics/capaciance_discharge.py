import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt

def plot_discharge():
    try:
        # Get user inputs
        E0 = float(entry_E0.get())
        R = float(entry_R.get())
        C = float(entry_C.get())
        
        if R <= 0 or C <= 0:
            raise ValueError("Resistance and capacitance must be positive.")
        
        # Time range
        time_constant = R * C
        t = np.linspace(0, 5 * time_constant, 1000)  # 5 time constants
        E = E0 * np.exp(-t / time_constant)  # Discharge equation

        # Select key points for the table (0, 1τ, 2τ, ..., 5τ)
        key_times = np.arange(0, 5 * time_constant + 1, time_constant)
        key_voltages = E0 * np.exp(-key_times / time_constant)

        # Plot the graph
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(t, E, label=f"E(t) = {E0} * exp(-t / ({time_constant:.2f}))")
        ax.set_title("Capacitor Discharge")
        ax.set_xlabel("Time (s)")
        ax.set_ylabel("Voltage (V)")
        ax.grid(True)
        ax.legend()

        # Add table
        table_data = [[f"{time:.2f}", f"{voltage:.2f}"] for time, voltage in zip(key_times, key_voltages)]
        column_labels = ["Time (s)", "Voltage (V)"]
        table = ax.table(cellText=table_data, colLabels=column_labels, loc="bottom", cellLoc="center", bbox=[0.2, -0.4, 0.6, 0.3])
        table.auto_set_font_size(False)
        table.set_fontsize(10)

        # Adjust plot to fit the table
        plt.subplots_adjust(bottom=0.3)
        plt.show()
    except ValueError as e:
        messagebox.showerror("Invalid Input", str(e))

# Create the Tkinter window
root = tk.Tk()
root.title("Capacitor Discharge Calculator")

# Input fields
tk.Label(root, text="Initial Voltage (E0):").grid(row=0, column=0, padx=10, pady=5)
entry_E0 = tk.Entry(root)
entry_E0.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Resistance (R) [Ohms]:").grid(row=1, column=0, padx=10, pady=5)
entry_R = tk.Entry(root)
entry_R.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Capacitance (C) [Farads]:").grid(row=2, column=0, padx=10, pady=5)
entry_C = tk.Entry(root)
entry_C.grid(row=2, column=1, padx=10, pady=5)

# Calculate button
btn_calculate = tk.Button(root, text="Plot Discharge", command=plot_discharge)
btn_calculate.grid(row=3, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()

