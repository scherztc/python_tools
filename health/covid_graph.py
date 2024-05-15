import math
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt

# Function to calculate and display the results
def calculate():
    sigma = float(entry_sigma.get())
    mu = float(entry_mu.get())
    gamma = float(entry_gamma.get())
    delta = float(entry_delta.get())
    beta1 = float(entry_beta1.get())
    beta2 = float(entry_beta2.get())
    alpha = float(entry_alpha.get())

    # Calculate
    num = delta * (beta1 * sigma + (gamma + mu) * beta2)
    den = (sigma + mu) * (gamma + mu) * mu
    F = num / den
    R = (1 - alpha) * F
    Ac = 1 - (1 / F)

    # Update the labels with the results
    label_F.config(text=f'F = {F:.4f}')
    label_R.config(text=f'R = {R:.4f}')
    label_Ac.config(text=f'Ac = {Ac:.4f}')

    # Determine the conditionals
    if R == 1:
        result = "The outbreak will become endemic."
        if alpha < Ac:
            advice = "Endemic State, increase public health"
        else:
            advice = "No change in public health"
    elif R > 1:
        result = "The outbreak will expand."
        if alpha < Ac:
            advice = "Disease expansion state, Increase Public Health Measures"
        else:
            advice = "No change in public health measures"
    else:
        result = "The outbreak will die out."
        if alpha > Ac:
            advice = "Disease controlled, Decrease Public Health Measures"
        else:
            advice = "No change in public health measures"

    # Update the labels with the conditionals
    label_result.config(text=result)
    label_advice.config(text=advice)

    # Plot the values
    plot_values(F, R, Ac)

def plot_values(F, R, Ac):
    fig, ax = plt.subplots()
    ax.bar(['F', 'R', 'Ac'], [F, R, Ac], color=['blue', 'green', 'red'])
    ax.set_ylabel('Values')
    ax.set_title('Epidemiological Parameters')
    plt.show()

# Create the main window
root = tk.Tk()
root.title("Epidemiological Model Calculator")

# Create and place the labels and entries for input
labels = ["sigma", "mu", "gamma", "delta", "beta1", "beta2", "alpha"]
entries = []
for i, label_text in enumerate(labels):
    label = ttk.Label(root, text=f"Enter the {label_text} coefficient:")
    label.grid(row=i, column=0, padx=5, pady=5)
    entry = ttk.Entry(root)
    entry.grid(row=i, column=1, padx=5, pady=5)
    entries.append(entry)

entry_sigma, entry_mu, entry_gamma, entry_delta, entry_beta1, entry_beta2, entry_alpha = entries

# Create and place the calculate button
button_calculate = ttk.Button(root, text="Calculate", command=calculate)
button_calculate.grid(row=len(labels), column=0, columnspan=2, pady=10)

# Create and place the labels for results
label_F = ttk.Label(root, text="F = ")
label_F.grid(row=len(labels) + 1, column=0, columnspan=2, pady=5)
label_R = ttk.Label(root, text="R = ")
label_R.grid(row=len(labels) + 2, column=0, columnspan=2, pady=5)
label_Ac = ttk.Label(root, text="Ac = ")
label_Ac.grid(row=len(labels) + 3, column=0, columnspan=2, pady=5)

label_result = ttk.Label(root, text="")
label_result.grid(row=len(labels) + 4, column=0, columnspan=2, pady=5)
label_advice = ttk.Label(root, text="")
label_advice.grid(row=len(labels) + 5, column=0, columnspan=2, pady=5)

# Start the main event loop
root.mainloop()

