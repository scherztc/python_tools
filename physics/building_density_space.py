# python building_weight_estimator.py concrete 10 20 30 20

class BuildingWeightEstimator:
    MATERIAL_DENSITIES = {
        'concrete': 2400,  # kg/m^3
        'steel': 7850,     # kg/m^3
        'wood': 600,       # kg/m^3
        'brick': 1800      # kg/m^3
    }

    def __init__(self, material, length, width, height, empty_space_percentage):
        if material not in self.MATERIAL_DENSITIES:
            raise ValueError(f"Material '{material}' is not supported.")
        if not (0 <= empty_space_percentage <= 100):
            raise ValueError("Empty space percentage must be between 0 and 100.")
        
        self.material = material
        self.length = length
        self.width = width
        self.height = height
        self.empty_space_percentage = empty_space_percentage

    def volume(self):
        total_volume = self.length * self.width * self.height
        empty_space_volume = total_volume * (self.empty_space_percentage / 100)
        return total_volume - empty_space_volume

    def density(self):
        return self.MATERIAL_DENSITIES[self.material]

    def weight(self):
        volume = self.volume()
        density = self.density()
        weight = volume * density
        return weight

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 6:
        print("Usage: python building_weight_estimator.py <material> <length> <width> <height> <empty_space_percentage>")
        sys.exit(1)

    material = sys.argv[1]
    length = float(sys.argv[2])
    width = float(sys.argv[3])
    height = float(sys.argv[4])
    empty_space_percentage = float(sys.argv[5])

    estimator = BuildingWeightEstimator(material, length, width, height, empty_space_percentage)
    estimated_weight = estimator.weight()

    print(f"Estimated weight of the building: {estimated_weight:.2f} kg")

