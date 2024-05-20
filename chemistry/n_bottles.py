def distribute_volume(total_volume, num_bottles):
    if num_bottles <= 0:
        raise ValueError("Number of bottles must be a positive integer.")
    if total_volume < 0:
        raise ValueError("Total volume must be a non-negative number.")
    
    volume_per_bottle = total_volume / num_bottles
    distribution = [volume_per_bottle] * num_bottles
    
    return distribution

# Example usage:
total_volume = 100.0  # total volume in liters (or any unit)
num_bottles = 5       # number of bottles

distribution = distribute_volume(total_volume, num_bottles)
print(f"Each of the {num_bottles} bottles will contain {distribution[0]:.2f} liters.")

