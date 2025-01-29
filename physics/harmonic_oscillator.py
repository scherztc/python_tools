import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Equations of motion for a spring-mass system
def harmonic_oscillator(t, y, k, m):
    x, v = y  # Displacement and velocity
    dxdt = v
    dvdt = - (k/m) * x  # Hooke's Law: F = -kx
    return [dxdt, dvdt]

# Function to plot the motion
def plot_motion():
    try:
        m = float(mass_entry.get())
        k = float(spring_const_entry.get())
        x0 = float(init_disp_entry.get())
        v0 = float(init_vel_entry.get())
    except ValueError:
        error_label.config(text="Please enter valid numbers")
        return
    
    error_label.config(text="")
    y0 = [x0, v0]  # Initial conditions
    t_span = (0, 10)  # Time range (seconds)
    t_eval = np.linspace(0, 10, 1000)  # Time points
    
    sol = solve_ivp(harmonic_oscillator, t_span, y0, t_eval=t_eval, 
args=(k, m))
    
    plt.figure(figsize=(8, 5))
    plt.plot(sol.t, sol.y[0], label='Displacement (m)')
    plt.xlabel('Time (s)')
    plt.ylabel('Displacement (m)')
    plt.title('Harmonic Oscillator Motion')
    plt.legend()
    plt.grid()
    plt.show()

# Create the Tkinter GUI
root = tk.Tk()
root.title("Harmonic Oscillator Simulator")

frame = ttk.Frame(root, padding=10)
frame.grid(row=0, column=0)

ttk.Label(frame, text="Mass (kg):").grid(row=0, column=0)
mass_entry = ttk.Entry(frame)
mass_entry.grid(row=0, column=1)


ttk.Label(frame, text="Spring Constant (N/m):").grid(row=1, column=0)
spring_const_entry = ttk.Entry(frame)
spring_const_entry.grid(row=1, column=1)


ttk.Label(frame, text="Initial Displacement (m):").grid(row=2, column=0)
init_disp_entry = ttk.Entry(frame)
init_disp_entry.grid(row=2, column=1)


ttk.Label(frame, text="Initial Velocity (m/s):").grid(row=3, column=0)
init_vel_entry = ttk.Entry(frame)
init_vel_entry.grid(row=3, column=1)

plot_button = ttk.Button(frame, text="Plot Motion", command=plot_motion)
plot_button.grid(row=4, column=0, columnspan=2, pady=10)

error_label = ttk.Label(frame, text="", foreground="red")
error_label.grid(row=5, column=0, columnspan=2)

root.mainloop()

