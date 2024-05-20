import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

def aggressive_savings(days):
    total_pennies = 0
    daily_deposit = 1  # Start with 1 penny on day 1
    savings_over_time = []

    for day in range(1, days + 1):
        total_pennies += daily_deposit
        savings_over_time.append(total_pennies / 100)  # Convert pennies to dollars for each day
        daily_deposit *= 2  # Double the deposit for the next day

    return savings_over_time

def plot_savings(days):
    savings = aggressive_savings(days)
    days_list = list(range(1, days + 1))

    plt.figure(figsize=(10, 6))
    plt.plot(days_list, savings, marker='o')
    plt.title('Aggressive Savings Over Time')
    plt.xlabel('Day')
    plt.ylabel('Total Savings ($)')
    plt.grid(True)
    plt.show()

def calculate_savings():
    try:
        days = int(entry_days.get())
        if days <= 0:
            raise ValueError("Number of days must be positive")
        savings = aggressive_savings(days)[-1]
        messagebox.showinfo("Total Savings", f"Total savings after {days} days: ${savings:.2f}")
        plot_savings(days)
    except ValueError as e:
        messagebox.showerror("Invalid Input", str(e))

# Set up the GUI
root = tk.Tk()
root.title("Aggressive Savings Plan Calculator")

tk.Label(root, text="Enter number of days:").pack(pady=5)
entry_days = tk.Entry(root)
entry_days.pack(pady=5)

tk.Button(root, text="Calculate Savings", command=calculate_savings).pack(pady=20)

root.mainloop()

