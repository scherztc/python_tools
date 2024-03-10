import math
import matplotlib.pyplot as plt

def generate_tidal_data(start_date, end_date, num_points, amplitude, period):
    tidal_data = []
    for i in range(num_points):
        date = start_date + (end_date - start_date) * (i / (num_points - 1))
        tide_height = amplitude * math.sin(2 * math.pi * date / period)
        tidal_data.append((date, tide_height))
    return tidal_data

def calculate_high_and_low_tide(tidal_data):
    high_tide = max(tidal_data, key=lambda x: x[1])
    low_tide = min(tidal_data, key=lambda x: x[1])
    return high_tide, low_tide

if __name__ == "__main__":
    start_date = float(input("Enter the start date for the sine curve: "))
    end_date = float(input("Enter the end date for the sine curve: "))
    num_points = int(input("Enter the number of points (days) to generate: "))
    amplitude = float(input("Enter the amplitude of the sine curve (tide height): "))
    period = float(input("Enter the period of the sine curve: "))

    tidal_data = generate_tidal_data(start_date, end_date, num_points, amplitude, period)
    high_tide, low_tide = calculate_high_and_low_tide(tidal_data)

    print(f"High tide: Date={high_tide[0]}, Height={high_tide[1]}")
    print(f"Low tide: Date={low_tide[0]}, Height={low_tide[1]}")

    # Plotting the tidal data
    dates = [data[0] for data in tidal_data]
    heights = [data[1] for data in tidal_data]

    plt.plot(dates, heights)
    plt.xlabel('Date')
    plt.ylabel('Tide Height')
    plt.title('Tidal Data')
    plt.show()

