import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Time-dependent spring constant function k(t)
def k(t):
    return 1 + 0.5 * np.sin(0.1 * t)  # Example of time-varying spring constant

# Define the equation of motion: m * d^2x/dt^2 + k(t) * x = 0
# This can be rewritten as a system of first-order differential equations:
# Let v = dx/dt, then we have the system:
# dx/dt = v
# dv/dt = -k(t) * x / m

def equation_of_motion(t, y, m):
    x, v = y
    dxdt = v
    dvdt = -k(t) * x / m
    return [dxdt, dvdt]

# Parameters
m = 1.0  # mass of the particle
x0 = 1.0  # initial position
v0 = 0.0  # initial velocity

# Initial conditions: [x0, v0]
initial_conditions = [x0, v0]

# Time span for the solution
t_span = (0, 50)  # from t = 0 to t = 50
t_eval = np.linspace(0, 50, 1000)  # evaluate at these time points

# Solve the differential equation
solution = solve_ivp(equation_of_motion, t_span, initial_conditions, t_eval=t_eval, args=(m,))

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
plt.title('Time Dependent Homogeneous Equation of Motion')
plt.legend()

# Velocity plot
plt.subplot(2, 1, 2)
plt.plot(t, v, label='Velocity (v)', color='red')
plt.xlabel('Time (t)')
plt.ylabel('Velocity (v)')
plt.legend()

plt.tight_layout()
plt.show()

