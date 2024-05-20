import math
import time
import tkinter as tk
from tkinter import messagebox, filedialog
import matplotlib.pyplot as plt

def calculate_prime_and_perfect_numbers():
    try:
        K = int(entry_K.get())

        if K <= 1:
            raise ValueError("The input number must be greater than 1.")

        # Initial Values
        C1 = 0
        C2 = 0
        w = 2

        primes = []
        perfects = []
        trace_table = []
        start_time = time.time()

        # Loop through numbers
        while w < K:
            S = 0
            n = w
            m = math.ceil(n / 2) + 1
            for p in range(2, m):
                if n % p == 0:
                    S += p
            trace_table.append((w, S))

            if S == 0:
                primes.append(n)
                C1 += 1
            elif S == n:
                perfects.append(n)
                C2 += 1

            w += 1

        end_time = time.time()
        elapsed_time = end_time - start_time

        result_text = (f"The total number of prime numbers found is {C1}\n"
                       f"The total number of perfect numbers found is {C2}\n"
                       f"Computation Time: {elapsed_time:.2f} seconds")
        messagebox.showinfo("Results", result_text)
        
        save_results(primes, perfects, trace_table, elapsed_time)
        display_trace_table(trace_table)
        plot_numbers(primes, perfects)

    except ValueError as e:
        messagebox.showerror("Input Error", str(e))

def save_results(primes, perfects, trace_table, elapsed_time):
    try:
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, 'w') as file:
                file.write(f"The total number of prime numbers found is {len(primes)}\n")
                file.write(f"The total number of perfect numbers found is {len(perfects)}\n")
                file.write(f"Computation Time: {elapsed_time:.2f} seconds\n\n")
                file.write("Prime Numbers:\n")
                file.write(', '.join(map(str, primes)) + '\n\n')
                file.write("Perfect Numbers:\n")
                file.write(', '.join(map(str, perfects)) + '\n\n')
                file.write("Trace Table (w, S):\n")
                for w, S in trace_table:
                    file.write(f"{w}: {S}\n")
            messagebox.showinfo("Save Success", f'Results saved to {file_path}')
    except Exception as e:
        messagebox.showerror("Save Error", str(e))

def display_trace_table(trace_table):
    trace_window = tk.Toplevel()
    trace_window.title("Trace Table")
    tk.Label(trace_window, text="w").grid(row=0, column=0)
    tk.Label(trace_window, text="S").grid(row=0, column=1)
    
    for i, (w, S) in enumerate(trace_table, start=1):
        tk.Label(trace_window, text=str(w)).grid(row=i, column=0)
        tk.Label(trace_window, text=str(S)).grid(row=i, column=1)

def plot_numbers(primes, perfects):
    plt.figure(figsize=(10, 6))
    if primes:
        plt.scatter(primes, [1]*len(primes), color='b', label='Prime Numbers')
    if perfects:
        plt.scatter(perfects, [1]*len(perfects), color='r', label='Perfect Numbers')

    plt.title('Prime and Perfect Numbers')
    plt.xlabel('Number')
    plt.ylabel('Category')
    plt.yticks([1], ['Numbers'])
    plt.grid(True)
    plt.legend()
    
    try:
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
        if file_path:
            plt.savefig(file_path)
            messagebox.showinfo("Save Success", f'Graph saved to {file_path}')
    except Exception as e:
        messagebox.showerror("Save Error", str(e))

    plt.show()

# Create the GUI window
root = tk.Tk()
root.title("Prime and Perfect Number Calculator")

tk.Label(root, text="Input a whole number").grid(row=0)

entry_K = tk.Entry(root)
entry_K.grid(row=0, column=1)

tk.Button(root, text='Calculate', command=calculate_prime_and_perfect_numbers).grid(row=1, column=1, pady=4)

root.mainloop()

