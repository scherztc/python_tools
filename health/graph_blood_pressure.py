import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np

# Function to determine the blood pressure category
def categorize_bp(systolic, diastolic):
    if systolic < 90 or diastolic < 60:
        return "Hypotension"
    elif 90 <= systolic <= 120 and 60 <= diastolic <= 80:
        return "Normal"
    elif systolic > 120 or diastolic > 80:
        return "Hypertension"
    else:
        return "Normal"

# Function to determine the most severe category
def most_severe_category(systolic, diastolic):
    systolic_category = categorize_bp(systolic, diastolic)
    diastolic_category = categorize_bp(diastolic, systolic)  # Just a placeholder to call the function

    # Determine the most severe category
    if "Hypertension" in [systolic_category, diastolic_category]:
        return "Hypertension"
    elif "Hypotension" in [systolic_category, diastolic_category]:
        return "Hypotension"
    else:
        return "Normal"

# Function to display the results
def display_results():
    try:
        systolic = float(systolic_entry.get())
        diastolic = float(diastolic_entry.get())

        category = categorize_bp(systolic, diastolic)
        severe_category = most_severe_category(systolic, diastolic)
        
        result_label.config(text=f"Category: {category}\nMost Severe Category: {severe_category}")
        
        plot_graph(systolic, diastolic, category, severe_category)
    
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter numeric values for blood pressure readings.")

# Function to plot the graph
def plot_graph(systolic, diastolic, category, severe_category):
    categories = ['Hypotension', 'Normal', 'Hypertension']
    systolic_range = np.linspace(50, 180, 500)
    diastolic_range = np.linspace(30, 120, 500)

    plt.figure(figsize=(10, 6))
    
    # Plotting the regions
    plt.fill_between(systolic_range, 30, 60, color='blue', alpha=0.2, label='Hypotension')
    plt.fill_between(systolic_range, 60, 80, color='green', alpha=0.2, label='Normal')
    plt.fill_between(systolic_range, 80, 120, color='red', alpha=0.2, label='Hypertension')
    plt.fill_betweenx(diastolic_range, 50, 90, color='blue', alpha=0.2)
    plt.fill_betweenx(diastolic_range, 90, 120, color='green', alpha=0.2)
    plt.fill_betweenx(diastolic_range, 120, 180, color='red', alpha=0.2)

    # Plotting the input point
    plt.scatter([systolic], [diastolic], color='black', zorder=5)
    plt.text(systolic, diastolic, f'  {category}\n  {severe_category}', fontsize=12, verticalalignment='bottom')
    
    plt.xlabel('Systolic Blood Pressure')
    plt.ylabel('Diastolic Blood Pressure')
    plt.title('Blood Pressure Categories')
    plt.legend()
    plt.grid(True)
    plt.show()

# Setting up the GUI
root = tk.Tk()
root.title("Blood Pressure Categorizer")

tk.Label(root, text="Systolic BP:").grid(row=0, column=0, padx=10, pady=10)
systolic_entry = tk.Entry(root)
systolic_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Diastolic BP:").grid(row=1, column=0, padx=10, pady=10)
diastolic_entry = tk.Entry(root)
diastolic_entry.grid(row=1, column=1, padx=10, pady=10)

result_label = tk.Label(root, text="", font=("Helvetica", 12))
result_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

tk.Button(root, text="Submit", command=display_results).grid(row=3, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()

