import csv
import numpy as np
from scipy.optimize import curve_fit

def read_tidal_data(file_path):
    tidal_data = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            date_time = row[0]  # Assuming the first column contains date and time
            tide_height = float(row[1])  # Assuming the second column contains tide height
            tidal_data.append((date_time, tide_height))
    return tidal_data

def fit_sine_curve(tidal_data):
    times = np.arange(len(tidal_data))
    heights = np.array([data[1] for data in tidal_data])
    
    # Define the sine function to fit the data
    def sine_func(x, a, b, c, d):
        return a * np.sin(b * x + c) + d
    
    # Fit the sine function to the data
    params, _ = curve_fit(sine_func, times, heights)
    
    return params

def predict_tide_at_time(params, time):
    a, b, c, d = params
    predicted_height = a * np.sin(b * time + c) + d
    return predicted_height

if __name__ == "__main__":
    file_path = 'Ketchikan_Alaska_date.csv'  # Replace 'tidal_data.csv' with your file path
    tidal_data = read_tidal_data(file_path)
    
    # Fit a sine curve to the tidal data
    params = fit_sine_curve(tidal_data)
    
    # Predict tide heights for future times
    future_times = np.arange(len(tidal_data), len(tidal_data) + 24)  # Assuming 24 hours of prediction
    predicted_tides = [predict_tide_at_time(params, t) for t in future_times]
    
    # Print the predicted tide heights
    for i, tide in enumerate(predicted_tides):
        print(f"Predicted tide height at hour {i+1}: {tide:.2f} meters")

