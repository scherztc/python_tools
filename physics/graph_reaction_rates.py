import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import simpledialog

# Function to calculate the reaction rate, k
def reaction_rate(A, E_a, R, T):
    return A * np.exp(-E_a / (R * T))

# Function to calculate concentration, C(t)
def concentration(C_0, k, t):
    return C_0 * np.exp(-k * t)

def plot_results():
    # Get user inputs
    E_a = float(entry_Ea.get())
    A = float(entry_A.get())
    C_0 = float(entry_C0.get())
    temperatures_C = [float(entry_temp1.get()), float(entry_temp2.get()), float(entry_temp3.get())]
    temperatures_K = [T + 273.15 for T in temperatures_C]  # Convert to Kelvin

    # Time points (in seconds)
    time = np.linspace(0, 500, 100)

    # Calculate reaction rates for each temperature
    reaction_rates = [reaction_rate(A, E_a, 8.314, T) for T in temperatures_K]

    # Calculate concentrations over time for each temperature
    concentrations = [concentration(C_0, k, time) for k in reaction_rates]

    # Plotting the results
    plt.figure(figsize=(10, 6))

    for i, T in enumerate(temperatures_C):
        plt.plot(time, concentrations[i], label=f'Temperature = {T}°C')

    plt.xlabel('Time (seconds)')
    plt.ylabel('Concentration (M)')
    plt.title('Decomposition of Hydrogen Peroxide over Time')
    plt.legend()
    plt.grid(True)
    plt.show()

# Setting up the Tkinter GUI
root = tk.Tk()
root.title("Decomposition of Hydrogen Peroxide")

tk.Label(root, text="Activation Energy (J/mol):").grid(row=0)
tk.Label(root, text="Frequency Factor (s^-1):").grid(row=1)
tk.Label(root, text="Initial Concentration (M):").grid(row=2)
tk.Label(root, text="Temperature 1 (°C):").grid(row=3)
tk.Label(root, text="Temperature 2 (°C):").grid(row=4)
tk.Label(root, text="Temperature 3 (°C):").grid(row=5)

entry_Ea = tk.Entry(root)
entry_A = tk.Entry(root)
entry_C0 = tk.Entry(root)
entry_temp1 = tk.Entry(root)
entry_temp2 = tk.Entry(root)
entry_temp3 = tk.Entry(root)

entry_Ea.grid(row=0, column=1)
entry_A.grid(row=1, column=1)
entry_C0.grid(row=2, column=1)
entry_temp1.grid(row=3, column=1)
entry_temp2.grid(row=4, column=1)
entry_temp3.grid(row=5, column=1)

tk.Button(root, text='Plot', command=plot_results).grid(row=6, column=0, columnspan=2)

root.mainloop()

