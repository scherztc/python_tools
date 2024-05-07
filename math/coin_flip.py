import random

def coin_flip_simulation():
    flips = int(input("How many times would you like to flip the coin? "))
    heads = 0
    tails = 0
    
    for _ in range(flips):
        if random.randint(0, 1) == 1:
            heads += 1
        else:
            tails += 1
    
    print(f"Heads came up {heads / flips * 100:.2f}% of the time.")
    print(f"Tails came up {tails / flips * 100:.2f}% of the time.")

# To run the function, simply call coin_flip_simulation()

coin_flip_simulation()
