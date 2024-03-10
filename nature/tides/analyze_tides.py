import csv

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

def calculate_high_and_low_tide(tidal_data):
    high_tide = None
    low_tide = None
    for i in range(1, len(tidal_data) - 1):
        if tidal_data[i][1] > tidal_data[i-1][1] and tidal_data[i][1] > tidal_data[i+1][1]:
            if high_tide is None or tidal_data[i][1] > high_tide[1]:
                high_tide = tidal_data[i]
        elif tidal_data[i][1] < tidal_data[i-1][1] and tidal_data[i][1] < tidal_data[i+1][1]:
            if low_tide is None or tidal_data[i][1] < low_tide[1]:
                low_tide = tidal_data[i]
    return high_tide, low_tide

if __name__ == "__main__":
    file_path = 'Ketchikan_Alaska_time.csv'  # Replace 'tidal_data.csv' with your file path
    tidal_data = read_tidal_data(file_path)
    high_tide, low_tide = calculate_high_and_low_tide(tidal_data)
    
    if high_tide:
        print(f"High tide: {high_tide[0]} - Height: {high_tide[1]}")
    else:
        print("No high tide data found.")
        
    if low_tide:
        print(f"Low tide: {low_tide[0]} - Height: {low_tide[1]}")
    else:
        print("No low tide data found.")

