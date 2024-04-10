# Activity Python Repitition Flow 1 : Task 3
# File: HW_13P1_TASK3_UCscherzts.py
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
# This program finds the prime and perfect numbers and the count of each for any whole number.


#Library
import math

# Input
K = int(input("Input a whole nubmer "))
C1=0
C2=0
w=2

while w < K-1:
  S=0
  n=w
  m=math.ceil(n/2)+1 
  for p in range(2,m):
    R= n % p
    if R==0:
      S=S+p
  if S==0: 
    print(f"{n} is a prime number")
    C1=C1+1
  else:
    if S==n-1:
      print(f"{n} is a perfect number")
      C2=C2+1
  w=w+1

print(f"The total number of prime numbers found is C1={C1}")
print(f"The total number of perfect numbers found is C2={C2}")


