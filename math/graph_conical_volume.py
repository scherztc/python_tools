import tkinter as tk
from tkinter import ttk
import math
import matplotlib.pyplot as plt

def calculate_height(initial_height, growth_rate, time):
    """
    Calculate the height of the conical pile at a given time.
    
    Parameters:
    initial_height (float): The initial height of the conical pile.
    growth_rate (float): The growth rate of the height (per unit time).
    time (float): The time at which to calculate the height.
    
    Returns:
    float: The height of the conical pile at the given time.
    """
    return initial_height + growth_rate * time

def calculate_conical_pile_volume(height):
    """
    Calculate the volume of a conical pile of gravel where the radius
    is twice the height.
    
    Parameters:
    height (float): The height of the conical pile.
    
    Returns:
    float: The volume of the conical pile.
    """
    radius = 2 * height
    volume = (1/3) * math.pi * (radius**2) * height
    return volume

def plot_graphs(initial_height, growth_rate, time):
    """
    Plot graphs of height and volume over time.
    
    Parameters:
    initial_height (float): The initial height of the conical pile.
    growth_rate (float): The growth rate of the height (per unit time).
    time (float): The time up to which to calculate the height and volume.
    """
    times = list(range(0, int(time)+1))
    heights = [calculate_height(initial_height, growth_rate, t) for t in times]
    volumes = [calculate_conical_pile_volume(h) for h in heights]
    
    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    plt.plot(times, heights, label='Height (m)')
    plt.xlabel('Time')
    plt.ylabel('Height (m)')
    plt.title('Height of Conical Pile Over Time')
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.plot(times, volumes, label='Volume (cubic meters)', color='orange')
    plt.xlabel('Time')
    plt.ylabel('Volume (cubic meters)')
    plt.title('Volume of Conical Pile Over Time')
    plt.legend()

    plt.tight_layout()
    plt.show()

def calculate_and_display():
    initial_height = float(initial_height_entry.get())
    growth_rate = float(growth_rate_entry.get())
    time = float(time_entry.get())

    height_at_time = calculate_height(initial_height, growth_rate, time)
    volume_at_time = calculate_conical_pile_volume(height_at_time)

    result_label.config(text=f"At time {time:.2f}, the height of the conical pile is {height_at_time:.2f} meters.\n"
                             f"The volume of the conical pile at this time is {volume_at_time:.2f} cubic meters.")
    
    plot_graphs(initial_height, growth_rate, time)

# Create the main window
root = tk.Tk()
root.title("Conical Pile Volume Calculator")

# Create and place the input fields and labels
ttk.Label(root, text="Initial Height (meters):").grid(column=0, row=0, padx=10, pady=5)
initial_height_entry = ttk.Entry(root)
initial_height_entry.grid(column=1, row=0, padx=10, pady=5)

ttk.Label(root, text="Growth Rate (meters per time unit):").grid(column=0, row=1, padx=10, pady=5)
growth_rate_entry = ttk.Entry(root)
growth_rate_entry.grid(column=1, row=1, padx=10, pady=5)

ttk.Label(root, text="Time (time units):").grid(column=0, row=2, padx=10, pady=5)
time_entry = ttk.Entry(root)
time_entry.grid(column=1, row=2, padx=10, pady=5)

# Create and place the calculate button
calculate_button = ttk.Button(root, text="Calculate", command=calculate_and_display)
calculate_button.grid(column=0, row=3, columnspan=2, padx=10, pady=10)

# Create and place the result label
result_label = ttk.Label(root, text="")
result_label.grid(column=0, row=4, columnspan=2, padx=10, pady=10)

# Run the application
root.mainloop()

