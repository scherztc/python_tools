def sum_to_limit():
    limit = float(input("Enter the numeric limit: "))
    # If the limit is not an integer, convert to the nearest integer towards zero
    if limit < 0:
        limit = int(limit)  # This will floor negative numbers
    else:
        limit = int(limit)  # This will floor positive numbers
    
    total_sum = sum(range(limit + 1)) if limit >= 0 else sum(range(limit, 1))
    print(f"The sum from 0 to {limit} is {total_sum}")

# To run the function, simply call sum_to_limit()
