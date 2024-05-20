import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import matplotlib.pyplot as plt

def calculate_pressure(n, V, T):
    R = 8.314  # J/(mol·K)
    P = (n * R * T) / V
    return P

def calculate_volume(n, P, T):
    R = 8.314  # J/(mol·K)
    V = (n * R * T) / P
    return V

def calculate_temperature(n, P, V):
    R = 8.314  # J/(mol·K)
    T = (P * V) / (n * R)
    return T

def calculate_moles(P, V, T):
    R = 8.314  # J/(mol·K)
    n = (P * V) / (R * T)
    return n

def plot_graph(x, y, x_label, y_label, title):
    plt.figure()
    plt.plot(x, y, marker='o')
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.grid(True)
    plt.show()

def on_calculate():
    try:
        n = float(entry_n.get())
        V = float(entry_V.get())
        T = float(entry_T.get())
        P = float(entry_P.get())
        
        if calculation_choice.get() == "Pressure":
            result = calculate_pressure(n, V, T)
            plot_graph([T], [result], "Temperature (K)", "Pressure (Pa)", "Pressure vs Temperature")
        elif calculation_choice.get() == "Volume":
            result = calculate_volume(n, P, T)
            plot_graph([T], [result], "Temperature (K)", "Volume (L)", "Volume vs Temperature")
        elif calculation_choice.get() == "Temperature":
            result = calculate_temperature(n, P, V)
            plot_graph([V], [result], "Volume (L)", "Temperature (K)", "Temperature vs Volume")
        elif calculation_choice.get() == "Moles":
            result = calculate_moles(P, V, T)
            plot_graph([V], [result], "Volume (L)", "Moles (mol)", "Moles vs Volume")

        result_label.config(text=f"Result: {result:.2f}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values.")

# Create the main window
root = tk.Tk()
root.title("Ideal Gas Law Calculator")

calculation_choice = tk.StringVar(value="Pressure")

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Input fields
ttk.Label(frame, text="Number of moles (n):").grid(row=0, column=0, sticky=tk.W)
entry_n = ttk.Entry(frame)
entry_n.grid(row=0, column=1, sticky=(tk.W, tk.E))

ttk.Label(frame, text="Volume (V) in liters:").grid(row=1, column=0, sticky=tk.W)
entry_V = ttk.Entry(frame)
entry_V.grid(row=1, column=1, sticky=(tk.W, tk.E))

ttk.Label(frame, text="Temperature (T) in Kelvin:").grid(row=2, column=0, sticky=tk.W)
entry_T = ttk.Entry(frame)
entry_T.grid(row=2, column=1, sticky=(tk.W, tk.E))

ttk.Label(frame, text="Pressure (P) in Pascals:").grid(row=3, column=0, sticky=tk.W)
entry_P = ttk.Entry(frame)
entry_P.grid(row=3, column=1, sticky=(tk.W, tk.E))

# Calculation choice
ttk.Label(frame, text="Calculate:").grid(row=4, column=0, sticky=tk.W)
calculation_menu = ttk.OptionMenu(frame, calculation_choice, "Pressure", "Pressure", "Volume", "Temperature", "Moles")
calculation_menu.grid(row=4, column=1, sticky=(tk.W, tk.E))

# Calculate button
calculate_button = ttk.Button(frame, text="Calculate", command=on_calculate)
calculate_button.grid(row=5, column=0, columnspan=2, sticky=(tk.W, tk.E))

# Result label
result_label = ttk.Label(frame, text="Result:")
result_label.grid(row=6, column=0, columnspan=2, sticky=(tk.W, tk.E))

# Add padding to all child widgets
for child in frame.winfo_children():
    child.grid_configure(padx=5, pady=5)

root.mainloop()

