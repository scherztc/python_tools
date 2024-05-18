import math
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np

def calculate_wave_properties():
    try:
        Ei0 = float(entry_Ei0.get())
        mat1 = float(entry_mat1.get())
        mat2 = float(entry_mat2.get())
        theta_i = float(entry_theta_i.get())
        med1 = float(entry_med1.get())
        med2 = float(entry_med2.get())

        theta_t = angle_trans_wave(theta_i, med1, med2)
        Er = amp_trans_wave(theta_i, mat1, mat2, Ei0, med1, med2)
        Et = amp_reflect_wave(theta_i, mat1, mat2, Ei0, med1, med2)

        result_text = (f'Angle of the transmitted wave (Theta_t): {theta_t:.2f} degrees\n'
                       f'Amplitude of the reflected wave (Er): {Er:.2f} V/m\n'
                       f'Amplitude of the transmitted wave (Et): {Et:.2f} V/m')

        messagebox.showinfo("Wave Properties", result_text)
        
        plot_wave_graph(theta_i, theta_t, Ei0, Er, Et)

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values.")

def angle_trans_wave(theta_i, med1, med2):
    theta_rad = math.radians(theta_i)
    theta_sin = (med1 / med2) * math.sin(theta_rad)
    angle_t_radians = math.asin(theta_sin)
    theta_t = math.degrees(angle_t_radians)
    return theta_t

def amp_trans_wave(theta_i, mat1, mat2, Ei0, med1, med2):
    theta_t = angle_trans_wave(theta_i, med1, med2)
    theta_rad = math.radians(theta_i)
    theta_t_rad = math.radians(theta_t)
    Er = (mat2 * math.cos(theta_rad) - mat1 * math.cos(theta_t_rad)) / (mat2 * math.cos(theta_rad) + mat1 * math.cos(theta_t_rad)) * Ei0
    return Er

def amp_reflect_wave(theta_i, mat1, mat2, Ei0, med1, med2):
    theta_t = angle_trans_wave(theta_i, med1, med2)
    theta_rad = math.radians(theta_i)
    theta_t_rad = math.radians(theta_t)
    Et = 2 * Ei0 * (math.cos(theta_rad) / (mat2 * math.cos(theta_rad)) + mat1 * math.cos(theta_t_rad))
    return Et

def plot_wave_graph(theta_i, theta_t, Ei0, Er, Et):
    fig, ax = plt.subplots()
    ax.axhline(0, color='black',linewidth=0.5)
    ax.axvline(0, color='black',linewidth=0.5)
    ax.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
    
    # Incident wave
    incident_x = np.linspace(0, np.cos(math.radians(theta_i)), 100)
    incident_y = np.linspace(0, np.sin(math.radians(theta_i)), 100) * Ei0
    ax.plot(incident_x, incident_y, label='Incident Wave')
    
    # Reflected wave
    reflected_x = np.linspace(0, -np.cos(math.radians(theta_i)), 100)
    reflected_y = np.linspace(0, -np.sin(math.radians(theta_i)), 100) * Er
    ax.plot(reflected_x, reflected_y, label='Reflected Wave')
    
    # Transmitted wave
    transmitted_x = np.linspace(0, np.cos(math.radians(theta_t)), 100)
    transmitted_y = np.linspace(0, np.sin(math.radians(theta_t)), 100) * Et
    ax.plot(transmitted_x, transmitted_y, label='Transmitted Wave')
    
    ax.set(xlabel='Position', ylabel='Amplitude',
           title='Wave Amplitudes and Angles')
    ax.legend()

    plt.show()

# Create the GUI window
root = tk.Tk()
root.title("Wave Property Calculator")

tk.Label(root, text="Amplitude of the incident wave (Ei0)").grid(row=0)
tk.Label(root, text="Intrinsic impedance of material 1 (ohms)").grid(row=1)
tk.Label(root, text="Intrinsic impedance of material 2 (ohms)").grid(row=2)
tk.Label(root, text="Angle of incidence (Theta_i in degrees)").grid(row=3)
tk.Label(root, text="Refractive index of medium 1").grid(row=4)
tk.Label(root, text="Refractive index of medium 2").grid(row=5)

entry_Ei0 = tk.Entry(root)
entry_mat1 = tk.Entry(root)
entry_mat2 = tk.Entry(root)
entry_theta_i = tk.Entry(root)
entry_med1 = tk.Entry(root)
entry_med2 = tk.Entry(root)

entry_Ei0.grid(row=0, column=1)
entry_mat1.grid(row=1, column=1)
entry_mat2.grid(row=2, column=1)
entry_theta_i.grid(row=3, column=1)
entry_med1.grid(row=4, column=1)
entry_med2.grid(row=5, column=1)

tk.Button(root, text='Calculate', command=calculate_wave_properties).grid(row=6, column=1, pady=4)

root.mainloop()

