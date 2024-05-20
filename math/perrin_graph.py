import math
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

def calculate_perrin_primes():
    try:
        n = int(entry_n.get())

        if n <= 0:
            raise ValueError("The number must be a positive integer.")

        # Initial Values
        w = 4
        x = 0
        y = 3
        count = 0
        perrin_primes = []

        while count < n:
            z = w + x
            m = math.ceil(z / 2) + 1
            S = 0
            for i in range(2, m):
                R = z % i
                if R == 0:
                    S += 1
            if S == 0 and z != y:
                perrin_primes.append(z)
                count += 1
            w, x, y = x, y, z

        result_text = f'The first {n} Perrin prime numbers are:\n' + ', '.join(map(str, perrin_primes))
        messagebox.showinfo("Perrin Prime Numbers", result_text)
        
        plot_perrin_primes(perrin_primes)

    except ValueError as e:
        messagebox.showerror("Input Error", str(e))

def plot_perrin_primes(perrin_primes):
    plt.figure(figsize=(10, 6))
    plt.plot(perrin_primes, marker='o', linestyle='-', color='b', label='Perrin Primes')
    plt.title('Perrin Prime Numbers')
    plt.xlabel('Index')
    plt.ylabel('Perrin Prime')
    plt.grid(True)
    plt.legend()
    plt.show()

# Create the GUI window
root = tk.Tk()
root.title("Perrin Prime Number Calculator")

tk.Label(root, text="Enter the number of Perrin prime numbers").grid(row=0)

entry_n = tk.Entry(root)
entry_n.grid(row=0, column=1)

tk.Button(root, text='Calculate', command=calculate_perrin_primes).grid(row=1, column=1, pady=4)

root.mainloop()

