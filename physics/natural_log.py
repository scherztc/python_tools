import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Generating synthetic data for demonstration purposes
# Time (s)
time = np.array([0, 50, 100, 150, 200, 250, 300])

# Concentration values (arbitrary units) for each temperature
concentration_300 = np.array([1.00, 0.90, 0.81, 0.73, 0.66, 0.60, 0.55])
concentration_304 = np.array([1.00, 0.88, 0.77, 0.68, 0.60, 0.53, 0.47])
concentration_308 = np.array([1.00, 0.85, 0.72, 0.61, 0.52, 0.44, 0.37])
concentration_312 = np.array([1.00, 0.83, 0.69, 0.57, 0.47, 0.38, 0.31])
concentration_316 = np.array([1.00, 0.80, 0.64, 0.51, 0.40, 0.31, 0.24])

# Creating a DataFrame to store the data
data = {
    'Time (s)': time,
    'Concentration (300 K)': concentration_300,
    'Concentration (304 K)': concentration_304,
    'Concentration (308 K)': concentration_308,
    'Concentration (312 K)': concentration_312,
    'Concentration (316 K)': concentration_316
}

df = pd.DataFrame(data)

# Calculate the natural log of the concentration values
for temp in [300, 304, 308, 312, 316]:
    df[f'ln(Concentration) ({temp} K)'] = np.log(df[f'Concentration ({temp} K)'])

# Function to plot data and linear trendline
def plot_with_trendline(x, y, temp):
    plt.figure(figsize=(10, 6))
    plt.scatter(x, y, label='Data')
    
    # Fit linear regression model
    slope, intercept, r_value, p_value, std_err = linregress(x, y)
    plt.plot(x, intercept + slope * x, 'r', label=f'Fitted line: y={slope:.4f}x+{intercept:.4f}\nR²={r_value**2:.4f}')
    
    plt.xlabel('Time (s)')
    plt.ylabel(f'ln(Concentration) ({temp} K)')
    plt.title(f'Temperature = {temp} K')
    plt.legend()
    plt.grid(True)
    plt.show()
    
    return slope, intercept, r_value**2

# Store results in a dictionary
results = {
    'Temperature (K)': [],
    'Equation': [],
    'Estimated Reaction Rate, k (s^-1)': [],
    'R² Value': []
}

# Calculate and plot for each temperature
for temp in [300, 304, 308, 312, 316]:
    x = df['Time (s)']
    y = df[f'ln(Concentration) ({temp} K)']
    slope, intercept, r_squared = plot_with_trendline(x, y, temp)
    
    results['Temperature (K)'].append(temp)
    results['Equation'].append(f'ln(C(t)) = {slope:.4f}t + {intercept:.4f}')
    results['Estimated Reaction Rate, k (s^-1)'].append(slope)
    results['R² Value'].append(r_squared)

# Convert results to DataFrame and display
results_df = pd.DataFrame(results)
import ace_tools as tools; tools.display_dataframe_to_user(name="Reaction Rate Results", dataframe=results_df)

