# A program for calculating the speed of a roller coaster at the bottom of the hill.  Using the car speed at position1, the friction coeffecient, the 
# distance traveled, the initial elevation and the final elevation.
# This program will generate use v1,y1,f,d,g=9.81, and y2

# import the math libraries

import math

#define  test libraries
# v1 = 1.7
# y1 = 32
# f = .46
# d = 45
# g = 9.81
# y2 = 0

#get all of the input variables

v1 = float(input("Enter the car speed at position 1, v1 "))
f = float(input("Enter the friction coefficient, f "))
d = float(input("Enter the traveled distance, d "))
y1 = float(input("Enter the initial elevation, y1 "))
y2 = float(input("Enter the final elevation, y2 "))

#calculate

def calculate_final_speed(v1,f,d,y1,y2):

    y1_y2 = y1 - y2
    delta_y_g = y1_y2 * 9.81
    delta_y_g_2 = delta_y_g * 2

    f_d = f*d
    f_d_g = f_d * 9.81
    v1_square = v1 * v1

    v1_f_d_g = v1_square - f_d_g
    
    v2_squared = delta_y_g_2 + v1_f_d_g
    v2_final = math.sqrt(v2_squared)   
    rounded_v2 = round(v2_final, 2)

    print('The Value of v2 = ' , rounded_v2, ' m/s')

#display ending investment after each year during 10-year period
calculate_final_speed(v1,f,d,y1,y2)
