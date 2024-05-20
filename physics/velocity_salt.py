import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Define the data
time = np.array([10, 20, 30, 40, 50, 60]).reshape(-1, 1)
velocity = np.array([18.1, 31.2, 68.4, 82.5, 123, 135])

# Plot the data
plt.scatter(time, velocity, color='blue', label='Data points')
plt.xlabel('Time (s)')
plt.ylabel('Velocity (m/s)')
plt.title('Velocity over Time')
plt.grid(True)

# Fit a linear trendline
model = LinearRegression()
model.fit(time, velocity)
trendline = model.predict(time)

# Plot the trendline
plt.plot(time, trendline, color='red', label='Trendline')

# Display the equation of the trendline
slope = model.coef_[0]
intercept = model.intercept_
equation = f'Equation: y = {slope:.2f}x + {intercept:.2f}'
plt.text(20, 60, equation, color='red')

# Calculate the R² value
r2 = r2_score(velocity, trendline)
r2_text = f'R² value: {r2:.2f}'
plt.text(20, 50, r2_text, color='red')

# Show the plot
plt.legend()
plt.show()

# Print correlation characterization
if r2 >= 0.75:
    correlation = "Very High"
elif r2 >= 0.50:
    correlation = "High"
elif r2 >= 0.25:
    correlation = "Moderate"
elif r2 >= 0.10:
    correlation = "Low"
else:
    correlation = "Little or No correlation"

print(f"The R² value for your trendline is {r2:.2f}. This indicates a {correlation} correlation.")

