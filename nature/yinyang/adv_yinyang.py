import matplotlib.pyplot as plt
import numpy as np

def draw_yin_yang():
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Draw the outer circle
    outer_circle = plt.Circle((0, 0), 1, color='black', fill=False, linewidth=2)
    ax.add_artist(outer_circle)
    
    # Draw the black half
    black_half = plt.Circle((0, 0.5), 0.5, color='black', fill=True)
    ax.add_artist(black_half)
    
    # Draw the white half
    white_half = plt.Circle((0, -0.5), 0.5, color='white', fill=True)
    ax.add_artist(white_half)
    
    # Draw the small black dot
    small_black_dot = plt.Circle((0, -0.5), 0.1, color='black', fill=True)
    ax.add_artist(small_black_dot)
    
    # Draw the small white dot
    small_white_dot = plt.Circle((0, 0.5), 0.1, color='white', fill=True)
    ax.add_artist(small_white_dot)
    
    # Set limits for the display area
    ax.set_xlim(-1.1, 1.1)
    ax.set_ylim(-1.1, 1.1)
    
    plt.show()

# Run the function to draw the symbol
draw_yin_yang()

