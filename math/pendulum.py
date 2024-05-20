import numpy as np
import matplotlib.pyplot as plt

def pendulum_motion(length, theta0, time_duration):
    # Constants
    g = 9.81  # acceleration due to gravity in m/s^2
    
    # Period of the pendulum
    T = 2 * np.pi * np.sqrt(length / g)
    
    # Frequency of the pendulum
    f = 1 / T
    
    # Time array
    t = np.linspace(0, time_duration, 1000)
    
    # Angular displacement over time
    theta_t = theta0 * np.cos(np.sqrt(g / length) * t)
    
    # Plotting the motion
    plt.figure(figsize=(10, 6))
    plt.plot(t, theta_t)
    plt.title('Pendulum Motion Over Time')
    plt.xlabel('Time (s)')
    plt.ylabel('Angular Displacement (rad)')
    plt.grid(True)
    plt.show()
    
    return T, f

# User inputs
length = float(input("Enter the length of the pendulum (in meters): "))
theta0 = float(input("Enter the initial angular displacement (in radians): "))
time_duration = float(input("Enter the duration of time for the simulation (in seconds): "))

# Calculate and plot
T, f = pendulum_motion(length, theta0, time_duration)

# Display the period and frequency
print(f"Period of the pendulum: {T:.2f} seconds")
print(f"Frequency of the pendulum: {f:.2f} Hz")

