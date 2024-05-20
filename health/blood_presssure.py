# Function to determine the blood pressure category
def categorize_bp(systolic, diastolic):
    if systolic < 90 and diastolic < 60:
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

# Test cases
test_cases = [
    (85, 55),
    (95, 65),
    (130, 85),
    (100, 75),
    (90, 60),
    (115, 80),
    (150, 95),
    (80, 50),
    (140, 90),
    (120, 80)
]

# Run test cases
for systolic, diastolic in test_cases:
    category = categorize_bp(systolic, diastolic)
    severe_category = most_severe_category(systolic, diastolic)
    print(f"Systolic: {systolic}, Diastolic: {diastolic} => Category: {category}, Most Severe Category: {severe_category}")

