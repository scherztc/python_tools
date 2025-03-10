import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Time-dependent spring constant function k(t)
def k(t):
    return 1 + 0.5 * np.sin(0.1 * t)  # Example of time-varying spring constant

# Time-dependent external force function F(t)
def F(t, A=1.0, omega=1.0):
    return A * np.sin(omega * t)  # Sinusoidal force

# Define the equation of motion: m * d^2x/dt^2 + k(t) * x = F(t)
# This can be rewritten as a system of first-order differential equations:
# dx/dt = v
# dv/dt = -k(t) * x / m + F(t) / m

def equation_of_motion(t, y, m, A, omega):
    x, v = y
    dxdt = v
    dvdt = -k(t) * x / m + F(t, A, omega) / m
    return [dxdt, dvdt]

# Parameters
m = 1.0  # mass of the particle
x0 = 1.0  # initial position
v0 = 0.0  # initial velocity
A = 1.0  # amplitude of the external force
omega = 1.0  # frequency of the external force

# Initial conditions: [x0, v0]
initial_conditions = [x0, v0]

# Time span for the solution
t_span = (0, 50)  # from t = 0 to t = 50
t_eval = np.linspace(0, 50, 1000)  # evaluate at these time points

# Solve the differential equation
solution = solve_ivp(equation_of_motion, t_span, initial_conditions, t_eval=t_eval, args=(m, A, omega))

# Extract the solution
t = solution.t
x = solution.y[0]
v = solution.y[1]

# Plot the position and velocity of the particle over time
plt.figure(figsize=(12, 6))

# Position plot
plt.subplot(2, 1, 1)
plt.plot(t, x, label='Position (x)', color='blue')
plt.xlabel('Time (t)')
plt.ylabel('Position (x)')
plt.title('Time Dependent Inhomogeneous Equation of Motion')
plt.legend()

# Velocity plot
plt.subplot(2, 1, 2)
plt.plot(t, v, label='Velocity (v)', color='red')
plt.xlabel('Time (t)')
plt.ylabel('Velocity (v)')
plt.legend()

plt.tight_layout()
plt.show()

