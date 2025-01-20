import matplotlib.pyplot as plt
import numpy as np

# Create a figure and axis
fig, ax = plt.subplots(figsize=(6, 6))

# Draw the main black circle
main_circle = plt.Circle((0, 0), 1, color='black', ec='black', lw=2)
ax.add_patch(main_circle)

# Draw the top white half-circle
theta = np.linspace(0, np.pi, 100)
x_top = 0.5 * np.cos(theta)
y_top = 0.5 * np.sin(theta) + 0.5
ax.fill_between(x_top, y_top, color='white')

# Draw the bottom black half-circle
x_bottom = 0.5 * np.cos(theta)
y_bottom = -0.5 * np.sin(theta) - 0.5
ax.fill_between(x_bottom, y_bottom, color='black')

# Draw the small black circle in the white half
black_dot = plt.Circle((0, 0.5), 0.15, color='black')
ax.add_patch(black_dot)

# Draw the small white circle in the black half
white_dot = plt.Circle((0, -0.5), 0.15, color='white')
ax.add_patch(white_dot)

# Set limits and aspect ratio
ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-1.2, 1.2)
ax.set_aspect('equal', 'box')
ax.axis('off')  # Turn off the axis

# Show the plot
plt.show()

