# A program for calculating compound interest, based off of Original principal sum P, Annual interest factor r, compounding frequency n, and time interest is applied t.
# This program will generate will display interest rate, Principal, Final Amount, and Interest Earnings.

# import the math libraries

import math

#define  test principal, interest rate, compounding periods per year, and total years
# P = 1000.27
# r = 2
# n = 10
# t = 20

#get principal, interest rate, compounding periods per year, and total years

P = round(float(input("Enter P (original principal sum) ")), 2)
x = int(input("Enter (annual interest factor) "))
n = int(input("Enter n (compounding frequency) "))
t = int(input("Enter t (time interest is applied) "))

#calculate the interest rate, r

r = (1 / (n**2)) * abs(math.sin(x) / x)
rounded_r = round(r, 4)

def sum_final(P,r,n,t):
    amount = P*(pow((1+r), n*t))
    rounded_amount = round(amount, 2)
    I = amount - P
    rounded_I = round(I, 2)
    rounded_P = round(P, 2)
    print('Interest rate = ' , rounded_r,', Principal = $', f'{P:.2f}')
    print('Final Amount : $', rounded_amount, ', Interest Earnings = $', rounded_I)

#display ending investment after each year during 10-year period
sum_final(P, r, n, t)
