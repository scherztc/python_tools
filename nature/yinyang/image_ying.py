import matplotlib.pyplot as plt
import numpy as np

# Create a figure and axis
fig, ax = plt.subplots(figsize=(6, 6))

# Draw the main circle
main_circle = plt.Circle((0, 0), 1, color='black', ec='black', lw=2)
ax.add_patch(main_circle)

# Draw the top white half
top_half = plt.Circle((0, 0.5), 0.5, color='white', ec='black', lw=2)
ax.add_patch(top_half)

# Draw the bottom black half
bottom_half = plt.Circle((0, -0.5), 0.5, color='black', ec='black', lw=2)
ax.add_patch(bottom_half)

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

