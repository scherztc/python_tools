# Import libraries

import math


# Calculations

def calculate_water_fountain(v0, angle):
    g = 9.81  
    angle_rad = math.radians(angle)  

    # Maximum height calculation
    max_height_meters = (v0**2) * (math.sin(angle_rad)**2) / (2 * g)
    max_height_inches = max_height_meters * 39.3701

    # Distance traveled calculation
    distance_meters = (v0**2) * math.sin(2 * angle_rad) / g
    distance_inches = distance_meters * 39.3701

    return round(max_height_inches, 2), round(distance_inches, 2)

# User Input and Output
initial_velocity = float(input("Enter the initial velocity (m/s): "))
angle = float(input("Enter the angle of projection (degrees): "))


max_height, distance = calculate_water_fountain(initial_velocity, angle)

print(f"Maximum height: {max_height} inches")
print(f"Distance traveled: {distance} inches")
