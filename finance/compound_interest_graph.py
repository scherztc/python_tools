import math
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

def calculate_compound_interest():
    try:
        P = round(float(entry_P.get()), 2)
        x = int(entry_x.get())
        n = int(entry_n.get())
        t = int(entry_t.get())

        # Calculate the interest rate, r
        r = (1 / (n**2)) * abs(math.sin(x) / x)
        rounded_r = round(r, 4)

        # Calculate final amount and interest earnings
        amount = P * (pow((1 + r), n * t))
        rounded_amount = round(amount, 2)
        I = amount - P
        rounded_I = round(I, 2)
        rounded_P = round(P, 2)

        result_text = (f'Interest rate = {rounded_r}, Principal = ${rounded_P:.2f}\n'
                       f'Final Amount: ${rounded_amount:.2f}, Interest Earnings = ${rounded_I:.2f}')
        
        messagebox.showinfo("Compound Interest Results", result_text)

        plot_compound_interest(P, r, n, t)

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values.")

def plot_compound_interest(P, r, n, t):
    years = list(range(t + 1))
    amounts = [P * (pow((1 + r), n * year)) for year in years]

    plt.figure(figsize=(10, 6))
    plt.plot(years, amounts, marker='o')
    plt.title('Compound Interest Growth Over Time')
    plt.xlabel('Years')
    plt.ylabel('Amount ($)')
    plt.grid(True)
    plt.show()

# Create the GUI window
root = tk.Tk()
root.title("Compound Interest Calculator")

tk.Label(root, text="Original principal sum (P)").grid(row=0)
tk.Label(root, text="Annual interest factor (x)").grid(row=1)
tk.Label(root, text="Compounding frequency per year (n)").grid(row=2)
tk.Label(root, text="Time interest is applied (t)").grid(row=3)

entry_P = tk.Entry(root)
entry_x = tk.Entry(root)
entry_n = tk.Entry(root)
entry_t = tk.Entry(root)

entry_P.grid(row=0, column=1)
entry_x.grid(row=1, column=1)
entry_n.grid(row=2, column=1)
entry_t.grid(row=3, column=1)

tk.Button(root, text='Calculate', command=calculate_compound_interest).grid(row=4, column=1, pady=4)

root.mainloop()

