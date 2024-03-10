import csv
import datetime
import matplotlib.pyplot as plt

def read_csv(file_path):
    """
    Read data from the CSV file.

    Args:
    - file_path: Path to the CSV file.

    Returns:
    - List of tuples containing date and tide level.
    """
    data = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            date = datetime.datetime.strptime(row[0], '%Y-%m-%d').date()
            tide_level = float(row[1])
            data.append((date, tide_level))
    return data

def predict_tides(data):
    """
    Predict high tide and low tide levels.

    Args:
    - data: List of tuples containing date and tide level.

    Returns:
    - Lists of dates, high tide levels, and low tide levels.
    """
    dates = [item[0] for item in data]
    tide_levels = [item[1] for item in data]
    # Simple prediction: Assume high tide occurs when tide level is maximum and low tide occurs when tide level is minimum
    high_tides = [max(tide_levels)] * len(data)
    low_tides = [min(tide_levels)] * len(data)
    return dates, high_tides, low_tides

def plot_tides(dates, high_tides, low_tides):
    """
    Plot predicted high tide and low tide levels against dates.

    Args:
    - dates: List of dates.
    - high_tides: List of high tide levels.
    - low_tides: List of low tide levels.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(dates, high_tides, label='High Tide', color='blue')
    plt.plot(dates, low_tides, label='Low Tide', color='green')
    plt.title('Tide Prediction')
    plt.xlabel('Date')
    plt.ylabel('Tide Level')
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()

def main():
    file_path = 'Ketchikan_Alaska_date.csv'  # Path to your CSV file
    data = read_csv(file_path)
    dates, high_tides, low_tides = predict_tides(data)
    plot_tides(dates, high_tides, low_tides)

if __name__ == "__main__":
    main()

