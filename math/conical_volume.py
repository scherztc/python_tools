import math

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
height = float(input("Enter the height of the conical pile (in meters): "))
volume = calculate_conical_pile_volume(height)
print(f"The volume of the conical pile is {volume:.2f} cubic meters.")

