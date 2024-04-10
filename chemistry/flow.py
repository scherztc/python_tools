def calculate_reynolds_number(v, l, mu, rho):
    if mu == 0:
        print("Error – Out of Bounds")
        exit()
    rn = (rho * v * l) / mu
    return round(rn)

def determine_flow(rn):
    if rn < 2300:
        return "Likely Laminar"
    elif rn <= 4000:
        return "In Transition"
    else:
        return "Likely Turbulent"

# User Input in units of measurement
v = float(input("Enter v the fluid velocity (m/s): "))
l = float(input("Enter l the typical length (m): "))
mu = float(input("Enter mu the dynamic viscosity (kg/(m·s)): "))
rho = float(input("Enter rho the density of the fluid (kg/m³): "))

rn = calculate_reynolds_number(v, l, mu, rho)

if mu != 0:
    print(f"Reynolds number: {rn}")
    flow_regime = determine_flow(rn)
    print(f"Flow regime: {flow_regime}")
