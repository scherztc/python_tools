import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class BuildingWeightEstimator:
    MATERIAL_DENSITIES = {
        'concrete': 2400,  # kg/m^3
        'steel': 7850,     # kg/m^3
        'wood': 600,       # kg/m^3
        'brick': 1800      # kg/m^3
    }

    def __init__(self, material, length, width, height, empty_space_percentage, windows_area_percentage):
        if material not in self.MATERIAL_DENSITIES:
            raise ValueError(f"Material '{material}' is not supported.")
        if not (0 <= empty_space_percentage <= 100):
            raise ValueError("Empty space percentage must be between 0 and 100.")
        if not (0 <= windows_area_percentage <= 100):
            raise ValueError("Windows area percentage must be between 0 and 100.")
        
        self.material = material
        self.length = length
        self.width = width
        self.height = height
        self.empty_space_percentage = empty_space_percentage
        self.windows_area_percentage = windows_area_percentage

    def volume(self):
        total_volume = self.length * self.width * self.height
        empty_space_volume = total_volume * (self.empty_space_percentage / 100)
        windows_volume = total_volume * (self.windows_area_percentage / 100)
        return total_volume - empty_space_volume - windows_volume

    def density(self):
        return self.MATERIAL_DENSITIES[self.material]

    def weight(self):
        volume = self.volume()
        density = self.density()
        weight = volume * density
        return weight

class BuildingEstimatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Building Weight Estimator")

        # Creating widgets
        self.create_widgets()

    def create_widgets(self):
        frame = ttk.Frame(self.root, padding="10")
        frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Material selection
        ttk.Label(frame, text="Material:").grid(row=0, column=0, sticky=tk.W)
        self.material = ttk.Combobox(frame, values=list(BuildingWeightEstimator.MATERIAL_DENSITIES.keys()))
        self.material.grid(row=0, column=1, sticky=(tk.W, tk.E))
        self.material.current(0)

        # Dimensions
        ttk.Label(frame, text="Length (m):").grid(row=1, column=0, sticky=tk.W)
        self.length = ttk.Entry(frame)
        self.length.grid(row=1, column=1, sticky=(tk.W, tk.E))

        ttk.Label(frame, text="Width (m):").grid(row=2, column=0, sticky=tk.W)
        self.width = ttk.Entry(frame)
        self.width.grid(row=2, column=1, sticky=(tk.W, tk.E))

        ttk.Label(frame, text="Height (m):").grid(row=3, column=0, sticky=tk.W)
        self.height = ttk.Entry(frame)
        self.height.grid(row=3, column=1, sticky=(tk.W, tk.E))

        # Empty space percentage
        ttk.Label(frame, text="Empty space percentage (%):").grid(row=4, column=0, sticky=tk.W)
        self.empty_space_percentage = ttk.Entry(frame)
        self.empty_space_percentage.grid(row=4, column=1, sticky=(tk.W, tk.E))

        # Windows area percentage
        ttk.Label(frame, text="Windows area percentage (%):").grid(row=5, column=0, sticky=tk.W)
        self.windows_area_percentage = ttk.Entry(frame)
        self.windows_area_percentage.grid(row=5, column=1, sticky=(tk.W, tk.E))

        # Calculate button
        self.calculate_button = ttk.Button(frame, text="Calculate", command=self.calculate_weight)
        self.calculate_button.grid(row=6, column=0, columnspan=2)

        # Output label
        self.output_label = ttk.Label(frame, text="")
        self.output_label.grid(row=7, column=0, columnspan=2)

        # Drawing canvas
        self.fig = plt.figure(figsize=(5, 4))
        self.ax = self.fig.add_subplot(111, projection='3d')
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas.get_tk_widget().grid(row=1, column=0)

    def calculate_weight(self):
        try:
            material = self.material.get()
            length = float(self.length.get())
            width = float(self.width.get())
            height = float(self.height.get())
            empty_space_percentage = float(self.empty_space_percentage.get())
            windows_area_percentage = float(self.windows_area_percentage.get())

            estimator = BuildingWeightEstimator(material, length, width, height, empty_space_percentage, windows_area_percentage)
            estimated_weight = estimator.weight()

            self.output_label.config(text=f"Estimated weight of the building: {estimated_weight:.2f} kg")

            self.draw_building(length, width, height, empty_space_percentage, windows_area_percentage)
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def draw_building(self, length, width, height, empty_space_percentage, windows_area_percentage):
        self.ax.clear()

        # Draw building
        building_color = 'gray'
        empty_space_color = 'white'
        windows_color = 'blue'

        # Calculate actual volumes
        total_volume = length * width * height
        empty_space_volume = total_volume * (empty_space_percentage / 100)
        windows_volume = total_volume * (windows_area_percentage / 100)
        building_volume = total_volume - empty_space_volume - windows_volume

        # Draw the building
        self.ax.bar3d(0, 0, 0, length, width, height, color=building_color, alpha=0.6)

        # Draw the empty space and windows as smaller rectangles within the building
        empty_length = length * (empty_space_percentage / 100)
        empty_width = width * (empty_space_percentage / 100)
        empty_height = height * (empty_space_percentage / 100)

        windows_length = length * (windows_area_percentage / 100)
        windows_width = width * (windows_area_percentage / 100)
        windows_height = height * (windows_area_percentage / 100)

        self.ax.bar3d(0, 0, 0, empty_length, empty_width, empty_height, color=empty_space_color, alpha=0.3)
        self.ax.bar3d(0, 0, 0, windows_length, windows_width, windows_height, color=windows_color, alpha=0.3)

        self.ax.set_xlabel('Length')
        self.ax.set_ylabel('Width')
        self.ax.set_zlabel('Height')

        self.canvas.draw()

if __name__ == "__main__":
    root = tk.Tk()
    app = BuildingEstimatorApp(root)
    root.mainloop()

