# A program for calculating compound interest, based off of Original principal sum P, Annual interest factor r, compounding frequency n, and time interest is applied t.
# This program will generate will display interest rate, Principal, Final Amount, and Interest Earnings.

# import the math libraries

import math

#define  test principal, interest rate, compounding periods per year, and total years

P = 1000
x = 2
n = 10
t = 20

#get principal, interest rate, compounding periods per year, and total years

r = (1 / (n**2)) * abs(math.sin(x) / x)
round_r = round(r, 4)
print('Interest = ', round_r) 

A=P*(1+r)**(n*t)
round_A = round(A, 2)
print ('Final Amount = $', round_A)

I= A - P
print ('Interest Earnings = ', I)

#calculate the interest rate, r

#display ending investment after each year during 10-year period
