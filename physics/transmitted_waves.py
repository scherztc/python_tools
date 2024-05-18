# Activity Python 1: Task 3
# File: HW_10P2_TASK3_UCscherzts.py
# Date:    2 Nov 2023
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
# A program for calculating the amplitued fo the reflected and transmitted wave for oblique incidence.  
# This program will generate the angle of the transmitted wave, the amplitude of the reflected wave, and the amplitude of the transmitted wave.
# This program will use v1,y1,f,d,g=9.81, and y2

# import the math libraries

import math

#define  test libraries
# Ei0 = 20
# mat1 = 377.14
# mat2 = 1131.42
# theta_i = 17
# med1 = 1
# med2 = 1.33

#get all of the input variables

Ei0 = float(input("Enter the amplitude fo the incident wave, Ei0 (V/m) "))
mat1 = float(input("Enter the intrinsic impedence of material 1,  (ohms) "))
mat2 = float(input("Enter the intrinsic impedence of material 2,  (ohms) "))
theta_i = float(input("Enter the angle of incidence, Theta_i (deg) "))
med1 = float(input("Enter the refractive index of medium 1 "))
med2 = float(input("Enter the refractive index of medium 2 "))

#calculate

def angle_trans_wave(theta_i,med1,med2):

   theta_rad = math.radians(theta_i)
   theta_sin = (med1 / med2) * math.sin(theta_rad)
   angle_t_radians = math.asin(theta_sin)
   theta_t = math.degrees(angle_t_radians)
   return theta_t

def amp_trans_wave(theta_i, mat1, mat2, Ei0, med1, med2):

     theta_t = angle_trans_wave(theta_i,med1,med2)
     result = (mat2 * math.cos(theta_i) - mat1 * math.cos(theta_t)) / (mat2 * math.cos(theta_i) + mat1 * math.cos(theta_t)) * Ei0
     print('The amplitude of the reflected wave is Er  = ' , result, ' V/m')


def amp_reflect_wave(theta_i, mat1, mat2, Ei0, med1, med2):
    Et = 2*Ei0*(math.cos(theta_i)/(mat2*math.cos(theta_i))+mat1*math.cos(angle_trans_wave(theta_i,med1,med2)))
    print('The amplitude of the transmitteed wave is Et  = ' , Et, ' V/m')

#display ending investment after each year during 10-year period

print('The angle of the transmitted wave is Theta_t  = ' , angle_trans_wave(theta_i,med1,med2), ' Degrees')
amp_trans_wave(theta_i, mat1, mat2, Ei0, med1, med2)
amp_reflect_wave(theta_i, mat1, mat2, Ei0, med1, med2)
