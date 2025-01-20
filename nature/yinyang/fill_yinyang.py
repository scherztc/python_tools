import matplotlib.pyplot as plt
import numpy as np

# Create figure and axes
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_aspect('equal')
ax.axis('off')  # Hide axes

# Define colors
yin_color = "black"
yang_color = "white"

# Draw the main circle outline (yin-yang symbol outline)
main_circle = plt.Circle((0, 0), 1, color="black", fill=False, linewidth=2)
ax.add_artist(main_circle)

# Draw the yin (black) half
yin_half = plt.Circle((0, 0.5), 0.5, color=yin_color)
ax.add_artist(yin_half)

# Draw the yang (white) half
yang_half = plt.Circle((0, -0.5), 0.5, color=yang_color)
ax.add_artist(yang_half)

# Draw the small yang (white) circle in the yin (black) half
yang_dot = plt.Circle((0, 0.5), 0.125, color=yang_color)
ax.add_artist(yang_dot)

# Draw the small yin (black) circle in the yang (white) half
yin_dot = plt.Circle((0, -0.5), 0.125, color=yin_color)
ax.add_artist(yin_dot)

# Draw the separating curved line by overlaying two semi-circles with opposite colors
yin_yang_border_top = plt.Circle((0, 0), 0.5, color=yin_color, clip_on=True, edgecolor=yin_color, linewidth=0)
yang_yang_border_bottom = plt.Circle((0, 0), 0.5, color=yang_color, clip_on=True, edgecolor=yang_color, linewidth=0)
ax.add_artist(yin_yang_border_top)
ax.add_artist(yang_yang_border_bottom)

# Display the figure
plt.show()

