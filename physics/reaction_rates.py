import numpy as np
import matplotlib.pyplot as plt

# Constants given in the document
E_a = 75.3 * 10**3  # Activation Energy (J/mol)
A = 10**11  # Frequency Factor (s^-1)
R = 8.314  # Ideal Gas Constant (J/(mol*K))
C_0 = 10  # Initial Concentration (M)
temperatures_C = [25, 45, 65]  # Temperatures in Celsius
temperatures_K = [T + 273.15 for T in temperatures_C]  # Convert to Kelvin

# Time points (in seconds)
time = np.linspace(0, 500, 100)

# Function to calculate the reaction rate, k
def reaction_rate(A, E_a, R, T):
    return A * np.exp(-E_a / (R * T))

# Function to calculate concentration, C(t)
def concentration(C_0, k, t):
    return C_0 * np.exp(-k * t)

# Calculate reaction rates for each temperature
reaction_rates = [reaction_rate(A, E_a, R, T) for T in temperatures_K]

# Calculate concentrations over time for each temperature
concentrations = [concentration(C_0, k, time) for k in reaction_rates]

# Plotting the results
plt.figure(figsize=(10, 6))

for i, T in enumerate(temperatures_C):
    plt.plot(time, concentrations[i], label=f'Temperature = {T}°C')

plt.xlabel('Time (seconds)')
plt.ylabel('Concentration (M)')
plt.title('Decomposition of Hydrogen Peroxide over Time')
plt.legend()
plt.grid(True)
plt.show()

