import matplotlib.pyplot as plt
import numpy as np

# Constants
PLANCK_CONSTANT = 6.62607015e-34  # Planck's constant in J·s
SPEED_OF_LIGHT = 2.998e8  # Speed of light in m/s

def energy_of_photon(wavelength_nm):
    """
    Calculate the energy of a photon given its wavelength.
    
    Parameters:
    wavelength_nm (float): Wavelength in nanometers (nm)
    
    Returns:
    float: Energy of the photon in joules (J)
    """
    wavelength_m = wavelength_nm * 1e-9  # Convert wavelength from nm to m
    energy = (PLANCK_CONSTANT * SPEED_OF_LIGHT) / wavelength_m
    return energy

def plot_energy_vs_wavelength(wavelength_range_nm):
    """
    Plot the energy of photons as a function of wavelength.
    
    Parameters:
    wavelength_range_nm (tuple): Range of wavelengths in nanometers (start, end)
    """
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
    """
    Plot the emission spectrum.
    
    Parameters:
    wavelengths_nm (list): List of wavelengths in nanometers
    intensities (list): Corresponding intensities of the emitted light
    """
    plt.figure(figsize=(10, 6))
    plt.bar(wavelengths_nm, intensities, color='red', width=1)
    plt.xlabel('Wavelength (nm)')
    plt.ylabel('Intensity')
    plt.title('Emission Spectrum')
    plt.grid(True)
    plt.show()

def absorption_spectrum(wavelengths_nm, absorbances):
    """
    Plot the absorption spectrum.
    
    Parameters:
    wavelengths_nm (list): List of wavelengths in nanometers
    absorbances (list): Corresponding absorbances of the substance
    """
    plt.figure(figsize=(10, 6))
    plt.plot(wavelengths_nm, absorbances, color='green')
    plt.xlabel('Wavelength (nm)')
    plt.ylabel('Absorbance')
    plt.title('Absorption Spectrum')
    plt.grid(True)
    plt.show()

# Example usage
wavelength = 500  # Example wavelength in nm
energy = energy_of_photon(wavelength)
print(f"The energy of a photon with a wavelength of {wavelength} nm is {energy:.3e} J")

# Plot the relationship between wavelength and photon energy
plot_energy_vs_wavelength((100, 1000))

# Example emission spectrum data
emission_wavelengths = [400, 450, 500, 550, 600, 650]
emission_intensities = [10, 50, 30, 70, 20, 60]
emission_spectrum(emission_wavelengths, emission_intensities)

# Example absorption spectrum data
absorption_wavelengths = np.linspace(200, 800, 600)
absorption_absorbances = np.exp(-((absorption_wavelengths - 500) ** 2) / (2 * 50 ** 2))
absorption_spectrum(absorption_wavelengths, absorption_absorbances)

