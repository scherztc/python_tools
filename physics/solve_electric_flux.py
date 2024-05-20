def calculate_electric_flux_density(rho, r):
    a = 3  # Internal radius in cm
    b = 6  # External radius in cm
    
    if r <= 0:
        return "Invalid input: r must be greater than 0"
    
    if 0 < r <= a:
        D = (rho * r) / 2
    elif a < r < b:
        D = (rho * a**2) / (2 * r)
    else:
        D = 0

    return D

def main():
    try:
        rho = float(input("Enter the charge density (rho) in nC/cm^3: "))
        r = float(input("Enter the radial distance (r) in cm: "))
        
        D = calculate_electric_flux_density(rho, r)
        
        print(f"The electric flux density D at r = {r} cm is: {D} nC/cm^2")
    
    except ValueError:
        print("Invalid input. Please enter numerical values.")

if __name__ == "__main__":
    main()

