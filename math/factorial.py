def compute_factorial():
    # Prompting for a non-negative integer
    while True:
        n = int(input("Enter a non-negative integer for factorial computation: "))
        if n < 0:
            print("Please enter a non-negative integer.")
        else:
            break

    # Calculating factorial
    factorial = 1
    for i in range(2, n + 1):
        factorial *= i

    print(f"{n}! = {factorial}")

# To run the function, simply call compute_factorial()

