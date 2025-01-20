import matplotlib.pyplot as plt
import numpy as np

# Create figure and axes
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_aspect('equal')
ax.axis('off')  # Hide axes

# Define colors
yin_color = "black"
yang_color = "white"

# Draw the main circle (yin-yang outline)
main_circle = plt.Circle((0, 0), 1, color="black", fill=False, linewidth=2)
ax.add_artist(main_circle)

# Draw the top half (yin)
yin_half = plt.Circle((0, 0.5), 0.5, color=yin_color, ec="black")
ax.add_artist(yin_half)

# Draw the bottom half (yang)
yang_half = plt.Circle((0, -0.5), 0.5, color=yang_color, ec="black")
ax.add_artist(yang_half)

# Draw the small circle in the yin half (yang dot)
yang_dot = plt.Circle((0, 0.5), 0.125, color=yang_color)
ax.add_artist(yang_dot)

# Draw the small circle in the yang half (yin dot)
yin_dot = plt.Circle((0, -0.5), 0.125, color=yin_color)
ax.add_artist(yin_dot)

# Display the figure
plt.show()

