def calculate_enthalpy_change(h1, h2):
    # According to Hess's Law, we can rearrange the given reactions to find the desired reaction.
    # For the reaction: C + 1/2 O2 -> CO
    # We use: C + O2 -> CO2 (H1) and CO + 1/2 O2 -> CO2 (H2)
    # The desired reaction can be obtained by reversing the second reaction and adding it to the first one.
    
    # Reversing the second reaction: CO2 -> CO + 1/2 O2
    # The enthalpy change for the reverse reaction is -H2.
    h2_reversed = -h2
    
    # Adding the first reaction to the reversed second reaction:
    # C + O2 -> CO2 (H1)
    # CO2 -> CO + 1/2 O2 (-H2)
    # The overall reaction: C + 1/2 O2 -> CO
    
    # The enthalpy change for the overall reaction:
    delta_h = h1 + h2_reversed
    return delta_h

# Given enthalpy changes for the reactions
delta_h1 = -393.5  # kJ
delta_h2 = -283.0  # kJ

# Calculate the enthalpy change for the desired reaction
delta_h_desired = calculate_enthalpy_change(delta_h1, delta_h2)

print(f"The enthalpy change for the reaction C + 1/2 O2 -> CO is {delta_h_desired} kJ")

