import math
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np

def calculate_final_speed():
    try:
        v1 = float(entry_v1.get())
        f = float(entry_f.get())
        d = float(entry_d.get())
        y1 = float(entry_y1.get())
        y2 = float(entry_y2.get())

        y1_y2 = y1 - y2
        delta_y_g = y1_y2 * 9.81
        delta_y_g_2 = delta_y_g * 2

        f_d = f * d
        f_d_g = f_d * 9.81
        v1_square = v1 * v1

        v1_f_d_g = v1_square - f_d_g
        
        v2_squared = delta_y_g_2 + v1_f_d_g
        v2_final = math.sqrt(v2_squared)
        rounded_v2 = round(v2_final, 2)

        result_text = f'The final speed (v2) is {rounded_v2} m/s'
        messagebox.showinfo("Roller Coaster Speed", result_text)
        
        plot_speed_graph(v1, f, d, y1, y2, rounded_v2)

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values.")

def plot_speed_graph(v1, f, d, y1, y2, v2_final):
    distances = np.linspace(0, d, 100)
    speeds = []

    for distance in distances:
        y1_y2 = y1 - y2
        delta_y_g = y1_y2 * 9.81
        delta_y_g_2 = delta_y_g * 2

        f_d = f * distance
        f_d_g = f_d * 9.81
        v1_square = v1 * v1

        v1_f_d_g = v1_square - f_d_g
        
        v2_squared = delta_y_g_2 + v1_f_d_g
        v2 = math.sqrt(v2_squared)
        speeds.append(v2)

    plt.figure(figsize=(10, 6))
    plt.plot(distances, speeds, label='Speed of the Roller Coaster')
    plt.axhline(y=v2_final, color='r', linestyle='--', label=f'Final Speed: {v2_final} m/s')
    plt.title('Roller Coaster Speed Over Distance')
    plt.xlabel('Distance (m)')
    plt.ylabel('Speed (m/s)')
    plt.legend()
    plt.grid(True)
    plt.show()

# Create the GUI window
root = tk.Tk()
root.title("Roller Coaster Speed Calculator")

tk.Label(root, text="Car speed at position 1 (v1)").grid(row=0)
tk.Label(root, text="Friction coefficient (f)").grid(row=1)
tk.Label(root, text="Traveled distance (d)").grid(row=2)
tk.Label(root, text="Initial elevation (y1)").grid(row=3)
tk.Label(root, text="Final elevation (y2)").grid(row=4)

entry_v1 = tk.Entry(root)
entry_f = tk.Entry(root)
entry_d = tk.Entry(root)
entry_y1 = tk.Entry(root)
entry_y2 = tk.Entry(root)

entry_v1.grid(row=0, column=1)
entry_f.grid(row=1, column=1)
entry_d.grid(row=2, column=1)
entry_y1.grid(row=3, column=1)
entry_y2.grid(row=4, column=1)

tk.Button(root, text='Calculate', command=calculate_final_speed).grid(row=5, column=1, pady=4)

root.mainloop()

