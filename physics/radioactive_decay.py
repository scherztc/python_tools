import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt

# Function to calculate decay chain dynamics
def calculate_decay_chain(mean_lives, initial_counts, time_range):
    mean_lives = np.array(mean_lives)
    initial_counts = np.array(initial_counts)
    num_species = len(mean_lives)
    time_points = np.linspace(0, time_range, 1000)
    
    populations = np.zeros((len(time_points), num_species))
    populations[0] = initial_counts

    dt = time_points[1] - time_points[0]
    for i in range(1, len(time_points)):
        for j in range(num_species):
            decay_rate = populations[i-1, j] / mean_lives[j]
            populations[i, j] = populations[i-1, j] - decay_rate * dt
            if j < num_species - 1:
                populations[i, j+1] += decay_rate * dt

    return time_points, populations

# Function to handle graph plotting
def plot_results(mean_lives, initial_counts, time_range):
    time_points, populations = calculate_decay_chain(mean_lives, initial_counts, time_range)

    plt.figure(figsize=(10, 6))
    for i in range(len(mean_lives)):
        plt.plot(time_points, populations[:, i], label=f"Species {i+1}")

    plt.title("Decay Chain Dynamics")
    plt.xlabel("Time")
    plt.ylabel("Number of Particles")
    plt.legend()
    plt.grid(True)
    plt.show()

# Function to gather inputs and trigger computation
def submit():
    try:
        mean_lives = list(map(float, mean_lives_entry.get().split(',')))
        initial_counts = list(map(float, initial_counts_entry.get().split(',')))
        time_range = float(time_range_entry.get())

        if len(mean_lives) != len(initial_counts):
            raise ValueError("Mean lives and initial counts must have the same number of elements.")

        plot_results(mean_lives, initial_counts, time_range)
    except ValueError as e:
        error_label.config(text=f"Error: {str(e)}")

# Tkinter GUI setup
root = tk.Tk()
root.title("Radioactive Decay Chain Calculator")

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Input fields
mean_lives_label = ttk.Label(frame, text="Mean Lives (comma-separated, e.g., 5,10,20):")
mean_lives_label.grid(row=0, column=0, sticky=tk.W)
mean_lives_entry = ttk.Entry(frame, width=30)
mean_lives_entry.grid(row=0, column=1)

initial_counts_label = ttk.Label(frame, text="Initial Counts (comma-separated, e.g., 100,0,0):")
initial_counts_label.grid(row=1, column=0, sticky=tk.W)
initial_counts_entry = ttk.Entry(frame, width=30)
initial_counts_entry.grid(row=1, column=1)

time_range_label = ttk.Label(frame, text="Time Range (e.g., 100):")
time_range_label.grid(row=2, column=0, sticky=tk.W)
time_range_entry = ttk.Entry(frame, width=30)
time_range_entry.grid(row=2, column=1)

# Error label
error_label = ttk.Label(frame, text="", foreground="red")
error_label.grid(row=3, column=0, columnspan=2)

# Submit button
submit_button = ttk.Button(frame, text="Calculate and Plot", command=submit)
submit_button.grid(row=4, column=0, columnspan=2)

# Start the GUI loop
root.mainloop()

