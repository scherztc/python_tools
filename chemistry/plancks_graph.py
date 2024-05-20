import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np

# Constants
PLANCK_CONSTANT = 6.62607015e-34  # Planck's constant in J·s
SPEED_OF_LIGHT = 2.998e8  # Speed of light in m/s

def energy_of_photon(wavelength_nm):
    wavelength_m = wavelength_nm * 1e-9  # Convert wavelength from nm to m
    energy = (PLANCK_CONSTANT * SPEED_OF_LIGHT) / wavelength_m
    return energy

def plot_energy_vs_wavelength(wavelength_range_nm):
    wavelengths_nm = np.linspace(wavelength_range_nm[0], wavelength_range_nm[1], 1000)
    energies_j = [energy_of_photon(wl) for wl in wavelengths_nm]
    
    plt.figure(figsize=(10, 6))
    plt.plot(wavelengths_nm, energies_j, color='blue')
    plt.xlabel('Wavelength (nm)')
    plt.ylabel('Energy (J)')
    plt.title('Photon Energy vs Wavelength')
    plt.grid(True)
    plt.show()

def emission_spectrum(wavelengths_nm, intensities):
    plt.figure(figsize=(10, 6))
    plt.bar(wavelengths_nm, intensities, color='red', width=1)
    plt.xlabel('Wavelength (nm)')
    plt.ylabel('Intensity')
    plt.title('Emission Spectrum')
    plt.grid(True)
    plt.show()

def absorption_spectrum(wavelengths_nm, absorbances):
    plt.figure(figsize=(10, 6))
    plt.plot(wavelengths_nm, absorbances, color='green')
    plt.xlabel('Wavelength (nm)')
    plt.ylabel('Absorbance')
    plt.title('Absorption Spectrum')
    plt.grid(True)
    plt.show()

def beers_law(absorptivity, concentration, path_length):
    absorbance = absorptivity * concentration * path_length
    return absorbance

def plot_beers_law(absorptivity, path_length, concentration_range):
    concentrations = np.linspace(concentration_range[0], concentration_range[1], 100)
    absorbances = [beers_law(absorptivity, c, path_length) for c in concentrations]
    
    plt.figure(figsize=(10, 6))
    plt.plot(concentrations, absorbances, color='purple')
    plt.xlabel('Concentration (mol/L)')
    plt.ylabel('Absorbance')
    plt.title("Absorbance vs Concentration (Beer's Law)")
    plt.grid(True)
    plt.show()

def show_energy_vs_wavelength():
    start = float(entry_start_wavelength.get())
    end = float(entry_end_wavelength.get())
    plot_energy_vs_wavelength((start, end))

def show_emission_spectrum():
    wavelengths = list(map(float, entry_emission_wavelengths.get().split(',')))
    intensities = list(map(float, entry_emission_intensities.get().split(',')))
    emission_spectrum(wavelengths, intensities)

def show_absorption_spectrum():
    wavelengths = np.linspace(200, 800, 600)
    absorbances = np.exp(-((wavelengths - 500) ** 2) / (2 * 50 ** 2))
    absorption_spectrum(wavelengths, absorbances)

def show_beers_law_plot():
    absorptivity = float(entry_absorptivity.get())
    path_length = float(entry_path_length.get())
    start_concentration = float(entry_start_concentration.get())
    end_concentration = float(entry_end_concentration.get())
    plot_beers_law(absorptivity, path_length, (start_concentration, end_concentration))

# Create main window
root = tk.Tk()
root.title("Photon Exploration")

# Energy vs Wavelength
frame1 = ttk.Frame(root, padding="10")
frame1.grid(row=0, column=0, padx=10, pady=10)
ttk.Label(frame1, text="Energy vs Wavelength").grid(row=0, column=0, columnspan=2)
ttk.Label(frame1, text="Start Wavelength (nm):").grid(row=1, column=0)
entry_start_wavelength = ttk.Entry(frame1)
entry_start_wavelength.grid(row=1, column=1)
ttk.Label(frame1, text="End Wavelength (nm):").grid(row=2, column=0)
entry_end_wavelength = ttk.Entry(frame1)
entry_end_wavelength.grid(row=2, column=1)
ttk.Button(frame1, text="Show Plot", command=show_energy_vs_wavelength).grid(row=3, column=0, columnspan=2)

# Emission Spectrum
frame2 = ttk.Frame(root, padding="10")
frame2.grid(row=1, column=0, padx=10, pady=10)
ttk.Label(frame2, text="Emission Spectrum").grid(row=0, column=0, columnspan=2)
ttk.Label(frame2, text="Wavelengths (nm, comma separated):").grid(row=1, column=0)
entry_emission_wavelengths = ttk.Entry(frame2)
entry_emission_wavelengths.grid(row=1, column=1)
ttk.Label(frame2, text="Intensities (comma separated):").grid(row=2, column=0)
entry_emission_intensities = ttk.Entry(frame2)
entry_emission_intensities.grid(row=2, column=1)
ttk.Button(frame2, text="Show Plot", command=show_emission_spectrum).grid(row=3, column=0, columnspan=2)

# Absorption Spectrum
frame3 = ttk.Frame(root, padding="10")
frame3.grid(row=2, column=0, padx=10, pady=10)
ttk.Label(frame3, text="Absorption Spectrum").grid(row=0, column=0, columnspan=2)
ttk.Button(frame3, text="Show Plot", command=show_absorption_spectrum).grid(row=1, column=0, columnspan=2)

# Beer's Law
frame4 = ttk.Frame(root, padding="10")
frame4.grid(row=3, column=0, padx=10, pady=10)
ttk.Label(frame4, text="Beer's Law").grid(row=0, column=0, columnspan=2)
ttk.Label(frame4, text="Molar Absorptivity (L/(mol*cm)):").grid(row=1, column=0)
entry_absorptivity = ttk.Entry(frame4)
entry_absorptivity.grid(row=1, column=1)
ttk.Label(frame4, text="Path Length (cm):").grid(row=2, column=0)
entry_path_length = ttk.Entry(frame4)
entry_path_length.grid(row=2, column=1)
ttk.Label(frame4, text="Start Concentration (mol/L):").grid(row=3, column=0)
entry_start_concentration = ttk.Entry(frame4)
entry_start_concentration.grid(row=3, column=1)
ttk.Label(frame4, text="End Concentration (mol/L):").grid(row=4, column=0)
entry_end_concentration = ttk.Entry(frame4)
entry_end_concentration.grid(row=4, column=1)
ttk.Button(frame4, text="Show Plot", command=show_beers_law_plot).grid(row=5, column=0, columnspan=2)

# Run the application
root.mainloop()

