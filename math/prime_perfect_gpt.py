#Library
import math

# Input
K = int(input("Input a whole nubmer"))
C1=0
C2=0

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_perfect(num):
    divisors_sum = sum(i for i in range(1, num) if num % i == 0)
    return divisors_sum == num

def find_perfect_numbers_and_primes(K):
    perfect_numbers = []
    prime_numbers = []

    for num in range(2, K):
        if is_prime(num):
            prime_numbers.append(num)
            print(f"The number n={num} is prime")
        elif is_perfect(num):
            perfect_numbers.append(num)
            print(f"The number n={num} is perfect")

    return prime_numbers, perfect_numbers

# Find and print perfect numbers and prime numbers
prime_numbers, perfect_numbers = find_perfect_numbers_and_primes(K)

# Print the total number of prime and perfect numbers found
print(f"The total number of prime numbers found is C1={len(prime_numbers)}")
print(f"The total number of perfect numbers found is C2={len(perfect_numbers)}")

