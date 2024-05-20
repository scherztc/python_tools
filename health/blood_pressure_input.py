# Function to determine the blood pressure category
def categorize_bp(systolic, diastolic):
    if systolic < 90 or diastolic < 60:
        return "Hypotension"
    elif 90 <= systolic <= 120 and 60 <= diastolic <= 80:
        return "Normal"
    elif systolic > 120 or diastolic > 80:
        return "Hypertension"
    else:
        return "Normal"

# Function to determine the most severe category
def most_severe_category(systolic, diastolic):
    systolic_category = categorize_bp(systolic, diastolic)
    diastolic_category = categorize_bp(diastolic, systolic)  # Just a placeholder to call the function

    # Determine the most severe category
    if "Hypertension" in [systolic_category, diastolic_category]:
        return "Hypertension"
    elif "Hypotension" in [systolic_category, diastolic_category]:
        return "Hypotension"
    else:
        return "Normal"

# Function to prompt user for input and determine the category
def get_user_input_and_categorize():
    try:
        systolic = float(input("Enter the systolic blood pressure reading: "))
        diastolic = float(input("Enter the diastolic blood pressure reading: "))

        category = categorize_bp(systolic, diastolic)
        severe_category = most_severe_category(systolic, diastolic)
        
        print(f"Systolic: {systolic}, Diastolic: {diastolic} => Category: {category}, Most Severe Category: {severe_category}")
    
    except ValueError:
        print("Invalid input. Please enter numeric values for blood pressure readings.")

# Main function to run the program
def main():
    get_user_input_and_categorize()

if __name__ == "__main__":
    main()

