def aggressive_savings(days):
    total_pennies = 0
    daily_deposit = 1  # Start with 1 penny on day 1

    for day in range(1, days + 1):
        total_pennies += daily_deposit
        daily_deposit *= 2  # Double the deposit for the next day

    total_dollars = total_pennies / 100  # Convert pennies to dollars
    return total_dollars

# Example usage:
days = 30  # Change this value for different amounts of days
savings = aggressive_savings(days)
print(f"Total savings after {days} days: ${savings:.2f}")

