# Import Libraries

import math

# Declare Variables

# type_of_machine = "Manual"
# age = 18
# weight = 220
# chr = 200

# Input

age = int(input("Enter the user age in years: "))
weight = float(input("Enter the user weight in pounds: "))
chr = float(input("Enter the user current heart rate in beats/minutes: "))
type_of_machine = input("Enter the type of machine (Manual or Automatic): ")

# Calculate

def calculate_mhr(age, type_of_machine):
    if type_of_machine == "Manual":
        return 206 - 0.88 * age
    elif type_of_machine == "Automatic":
        return 205.8 - 0.685 * age

def calculate_intensity_level(chr, mhr):
    if chr < 0.6 * mhr:
       return "Below Level"
    elif 0.6 * mhr < chr < 0.7 * mhr:
       return "Weight Loss"
    elif 0.7 * mhr < chr < 0.8 * mhr:
       return "Cardio"
    elif 0.8 * mhr < chr < 0.9 * mhr:
       return "Anaerobic (Hardcore)"
    else:
       return "Above Level"

def calculate_calories_burned(age, weight, chr, type_of_machine):
   if type_of_machine == "Manual":
       return 60 * (age * 0.074 - weight * 0.05741 + chr * 0.4472 - 20.402) / 4.184
   elif type_of_machine == "Automatic":
       return 60 * (age * 0.2017 + weight * 0.09036 + chr * 0.6309 - 55.0969) / 4.184

# Print output

def result(age, type_of_machine, chr, weight):

    mhr = calculate_mhr(age, type_of_machine)
    intensity_level = calculate_intensity_level(chr, mhr)
    calories_burned = calculate_calories_burned(age, weight, chr, type_of_machine)
    print('Calories burnt per hour is: ', f'{calories_burned:.2f}' , 'for an activity level of: ', intensity_level)

# Run Program

result(age, type_of_machine, chr, weight)
