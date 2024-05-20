import math

def calculate_height(initial_height, growth_rate, time):
    """
    Calculate the height of the conical pile at a given time.
    
    Parameters:
    initial_height (float): The initial height of the conical pile.
    growth_rate (float): The growth rate of the height (per unit time).
    time (float): The time at which to calculate the height.
    
    Returns:
    float: The height of the conical pile at the given time.
    """
    return initial_height + growth_rate * time

def calculate_conical_pile_volume(height):
    """
    Calculate the volume of a conical pile of gravel where the radius
    is twice the height.
    
    Parameters:
    height (float): The height of the conical pile.
    
    Returns:
    float: The volume of the conical pile.
    """
    radius = 2 * height
    volume = (1/3) * math.pi * (radius**2) * height
    return volume

# Example usage
initial_height = float(input("Enter the initial height of the conical pile (in meters): "))
growth_rate = float(input("Enter the growth rate of the height (in meters per time unit): "))
time = float(input("Enter the time (in time units): "))

height_at_time = calculate_height(initial_height, growth_rate, time)
volume_at_time = calculate_conical_pile_volume(height_at_time)

print(f"At time {time:.2f}, the height of the conical pile is {height_at_time:.2f} meters.")
print(f"The volume of the conical pile at this time is {volume_at_time:.2f} cubic meters.")

