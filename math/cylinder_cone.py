import sympy as sp

def max_cylinder_volume_in_cone(x, y):
    R = y / 2  # Radius of the cone's base
    h = sp.Symbol('h')  # Height of the cylinder
    
    # Volume of the cylinder in terms of h
    V = sp.pi * (R * (x - h) / x)**2 * h
    
    # Differentiate V with respect to h
    dV_dh = sp.diff(V, h)
    
    # Solve dV_dh = 0 for h
    h_opt = sp.solve(dV_dh, h)
    
    # Select the positive solution for h
    h_opt = [sol.evalf() for sol in h_opt if sol.is_real and sol > 0][0]
    
    # Calculate the corresponding radius r
    r_opt = R * (x - h_opt) / x
    
    # Calculate the maximum volume
    max_volume = V.subs(h, h_opt).evalf()
    
    return float(h_opt), float(r_opt), float(max_volume)

# Example usage
x = float(input("Enter the height of the cone (x): "))
y = float(input("Enter the base diameter of the cone (y): "))

optimal_height, optimal_radius, max_volume = max_cylinder_volume_in_cone(x, y)

print(f"Optimal height of the cylinder: {optimal_height:.2f} inches")
print(f"Optimal radius of the cylinder: {optimal_radius:.2f} inches")
print(f"Maximum volume of the cylinder: {max_volume:.2f} cubic inches")

