import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Equations of motion for two coupled harmonic oscillators
def coupled_oscillators(t, y, k1, k2, m1, m2):
    x1, v1, x2, v2 = y  # Displacements and velocities
    dx1dt = v1
    dv1dt = -(k1/m1) * x1 + (k2/m1) * (x2 - x1)  # Coupling force
    dx2dt = v2
    dv2dt = -(k2/m2) * (x2 - x1) - (k1/m2) * x2  # Coupling force
    return [dx1dt, dv1dt, dx2dt, dv2dt]

# Function to plot the motion
def plot_motion():
    try:
        m1 = float(mass1_entry.get())
        m2 = float(mass2_entry.get())
        k1 = float(spring_const1_entry.get())
        k2 = float(spring_const2_entry.get())
        x1_0 = float(init_disp1_entry.get())
        v1_0 = float(init_vel1_entry.get())
        x2_0 = float(init_disp2_entry.get())
        v2_0 = float(init_vel2_entry.get())
    except ValueError:
        error_label.config(text="Please enter valid numbers")
        return
    
    error_label.config(text="")
    y0 = [x1_0, v1_0, x2_0, v2_0]  # Initial conditions
    t_span = (0, 10)  # Time range (seconds)
    t_eval = np.linspace(0, 10, 1000)  # Time points
    
    sol = solve_ivp(coupled_oscillators, t_span, y0, t_eval=t_eval, args=(k1, k2, m1, m2))
    
    plt.figure(figsize=(8, 5))
    plt.plot(sol.t, sol.y[0], label='Mass 1 Displacement (m)')
    plt.plot(sol.t, sol.y[2], label='Mass 2 Displacement (m)')
    plt.xlabel('Time (s)')
    plt.ylabel('Displacement (m)')
    plt.title('Coupled Harmonic Oscillators Motion')
    plt.legend()
    plt.grid()
    plt.show()

# Create the Tkinter GUI
root = tk.Tk()
root.title("Coupled Harmonic Oscillators Simulator")

frame = ttk.Frame(root, padding=10)
frame.grid(row=0, column=0)

ttk.Label(frame, text="Mass 1 (kg):").grid(row=0, column=0)
mass1_entry = ttk.Entry(frame)
mass1_entry.grid(row=0, column=1)

ttk.Label(frame, text="Mass 2 (kg):").grid(row=1, column=0)
mass2_entry = ttk.Entry(frame)
mass2_entry.grid(row=1, column=1)

ttk.Label(frame, text="Spring Constant 1 (N/m):").grid(row=2, column=0)
spring_const1_entry = ttk.Entry(frame)
spring_const1_entry.grid(row=2, column=1)

ttk.Label(frame, text="Spring Constant 2 (N/m):").grid(row=3, column=0)
spring_const2_entry = ttk.Entry(frame)
spring_const2_entry.grid(row=3, column=1)

ttk.Label(frame, text="Initial Displacement Mass 1 (m):").grid(row=4, column=0)
init_disp1_entry = ttk.Entry(frame)
init_disp1_entry.grid(row=4, column=1)

ttk.Label(frame, text="Initial Velocity Mass 1 (m/s):").grid(row=5, column=0)
init_vel1_entry = ttk.Entry(frame)
init_vel1_entry.grid(row=5, column=1)

ttk.Label(frame, text="Initial Displacement Mass 2 (m):").grid(row=6, column=0)
init_disp2_entry = ttk.Entry(frame)
init_disp2_entry.grid(row=6, column=1)

ttk.Label(frame, text="Initial Velocity Mass 2 (m/s):").grid(row=7, column=0)
init_vel2_entry = ttk.Entry(frame)
init_vel2_entry.grid(row=7, column=1)

plot_button = ttk.Button(frame, text="Plot Motion", command=plot_motion)
plot_button.grid(row=8, column=0, columnspan=2, pady=10)

error_label = ttk.Label(frame, text="", foreground="red")
error_label.grid(row=9, column=0, columnspan=2)

root.mainloop()

