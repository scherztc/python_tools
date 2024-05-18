class BuildingWeightEstimator:
    MATERIAL_DENSITIES = {
        'concrete': 2400,  # kg/m^3
        'steel': 7850,     # kg/m^3
        'wood': 600,       # kg/m^3
        'brick': 1800      # kg/m^3
    }

    def __init__(self, material, length, width, height):
        if material not in self.MATERIAL_DENSITIES:
            raise ValueError(f"Material '{material}' is not supported.")
        self.material = material
        self.length = length
        self.width = width
        self.height = height

    def volume(self):
        return self.length * self.width * self.height

    def density(self):
        return self.MATERIAL_DENSITIES[self.material]

    def weight(self):
        volume = self.volume()
        density = self.density()
        weight = volume * density
        return weight

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 5:
        print("Usage: python building_weight_estimator.py <material> <length> <width> <height>")
        sys.exit(1)

    material = sys.argv[1]
    length = float(sys.argv[2])
    width = float(sys.argv[3])
    height = float(sys.argv[4])

    estimator = BuildingWeightEstimator(material, length, width, height)
    estimated_weight = estimator.weight()

    print(f"Estimated weight of the building: {estimated_weight:.2f} kg")

