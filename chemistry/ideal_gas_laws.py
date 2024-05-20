def calculate_pressure(n, V, T):
    R = 8.314  # J/(mol·K)
    P = (n * R * T) / V
    return P

def calculate_volume(n, P, T):
    R = 8.314  # J/(mol·K)
    V = (n * R * T) / P
    return V

def calculate_temperature(n, P, V):
    R = 8.314  # J/(mol·K)
    T = (P * V) / (n * R)
    return T

def calculate_moles(P, V, T):
    R = 8.314  # J/(mol·K)
    n = (P * V) / (R * T)
    return n

# Example usage:
def main():
    while True:
        print("Ideal Gas Law Calculator")
        print("1. Calculate Pressure")
        print("2. Calculate Volume")
        print("3. Calculate Temperature")
        print("4. Calculate Moles")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            n = float(input("Enter the number of moles (n): "))
            V = float(input("Enter the volume (V) in liters: "))
            T = float(input("Enter the temperature (T) in Kelvin: "))
            P = calculate_pressure(n, V, T)
            print(f"The pressure (P) is: {P} Pa")

        elif choice == '2':
            n = float(input("Enter the number of moles (n): "))
            P = float(input("Enter the pressure (P) in Pascals: "))
            T = float(input("Enter the temperature (T) in Kelvin: "))
            V = calculate_volume(n, P, T)
            print(f"The volume (V) is: {V} liters")

        elif choice == '3':
            n = float(input("Enter the number of moles (n): "))
            P = float(input("Enter the pressure (P) in Pascals: "))
            V = float(input("Enter the volume (V) in liters: "))
            T = calculate_temperature(n, P, V)
            print(f"The temperature (T) is: {T} Kelvin")

        elif choice == '4':
            P = float(input("Enter the pressure (P) in Pascals: "))
            V = float(input("Enter the volume (V) in liters: "))
            T = float(input("Enter the temperature (T) in Kelvin: "))
            n = calculate_moles(P, V, T)
            print(f"The number of moles (n) is: {n} mol")

        elif choice == '5':
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

