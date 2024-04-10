# Activity Python Repitition Flow 1 : Task 2
# File: HW_13P1_TASK2_UCscherzts.py
# Date:    28 Nov 2023
# By:      Tre Scherz
# Section: 014
# Team:    236
#
# ELECTRONIC SIGNATURE
#  Tre Scherz
#
# The electronic signature above indicatees the scripts
# submitted for evaluation is my individual work, and I
# have a general understaning of all apsects of its
# development and execution.
#
# A BRIEF DESCRIPTION OF WHAT THE SCRIPT OR FUNCTION DOES
# This program sort trial runs of BPS into three categories and counts the number of records in each category.



import random

def sort_bps(bps):
    if 50 <= bps < 90:
        return "Hypotension"
    elif 90 <= bps < 120:
        return "Normal"
    elif 120 <= bps < 210:
        return "Hypertension"
    else:
        return "Out of Range"

def main():
    num = int(input("Enter the number of BPS readings: "))

    hypotension_count = 0
    normal_count = 0
    hypertension_count = 0

    for i in range(num):
        flip = random.randint(65, 140)
        category = sort_bps(flip)

        if category == "Hypotension":
            hypotension_count += 1
        elif category == "Normal":
            normal_count += 1
        elif category == "Hypertension":
            hypertension_count += 1

    print("Hypotension:", hypotension_count)
    print("Normal:", normal_count)
    print("Hypertension:", hypertension_count)

main()

