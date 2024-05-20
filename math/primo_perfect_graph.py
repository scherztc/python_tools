import math
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import simpledialog

# Function to check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Function to check if a number is perfect
def is_perfect(num):
    divisors_sum = sum(i for i in range(1, num) if num % i == 0)
    return divisors_sum == num

# Function to find perfect numbers and prime numbers up to K
def find_perfect_numbers_and_primes(K):
    perfect_numbers = []
    prime_numbers = []
    trace_table = []

    for num in range(2, K):
        if is_prime(num):
            prime_numbers.append(num)
            trace_table.append((num, 'Prime'))
        elif is_perfect(num):
            perfect_numbers.append(num)
            trace_table.append((num, 'Perfect'))

    return prime_numbers, perfect_numbers, trace_table

# Function to display results in a new window
def display_results(prime_numbers, perfect_numbers, trace_table):
    # Creating a new Tkinter window
    result_window = tk.Tk()
    result_window.title("Results")

    # Displaying the prime numbers
    prime_label = tk.Label(result_window, text="Prime Numbers:")
    prime_label.pack()
    prime_text = tk.Text(result_window, height=10, width=50)
    prime_text.pack()
    prime_text.insert(tk.END, ", ".join(map(str, prime_numbers)))

    # Displaying the perfect numbers
    perfect_label = tk.Label(result_window, text="Perfect Numbers:")
    perfect_label.pack()
    perfect_text = tk.Text(result_window, height=10, width=50)
    perfect_text.pack()
    perfect_text.insert(tk.END, ", ".join(map(str, perfect_numbers)))

    # Displaying the trace table
    trace_label = tk.Label(result_window, text="Trace Table:")
    trace_label.pack()
    trace_text = tk.Text(result_window, height=10, width=50)
    trace_text.pack()
    for entry in trace_table:
        trace_text.insert(tk.END, f"{entry[0]}: {entry[1]}\n")

    result_window.mainloop()

# Function to plot the results
def plot_results(prime_numbers, perfect_numbers):
    # Plotting the prime numbers
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.plot(prime_numbers, 'ro-', label='Prime Numbers')
    plt.xlabel('Index')
    plt.ylabel('Prime Number')
    plt.title('Prime Numbers')
    plt.legend()

    # Plotting the perfect numbers
    plt.subplot(1, 2, 2)
    plt.plot(perfect_numbers, 'bo-', label='Perfect Numbers')
    plt.xlabel('Index')
    plt.ylabel('Perfect Number')
    plt.title('Perfect Numbers')
    plt.legend()

    plt.tight_layout()
    plt.show()

# Main code
def main():
    # Creating a Tkinter window to get input
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Getting input from the user
    K = simpledialog.askinteger("Input", "Input a whole number")

    if K is not None:
        prime_numbers, perfect_numbers, trace_table = find_perfect_numbers_and_primes(K)

        # Displaying the results in a new window
        display_results(prime_numbers, perfect_numbers, trace_table)

        # Plotting the results
        plot_results(prime_numbers, perfect_numbers)

        # Printing the total number of prime and perfect numbers found
        print(f"The total number of prime numbers found is C1={len(prime_numbers)}")
        print(f"The total number of perfect numbers found is C2={len(perfect_numbers)}")

if __name__ == "__main__":
    main()

