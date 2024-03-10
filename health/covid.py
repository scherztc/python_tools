# Import Math Tools

import math

# Declare Variables

# sigma = .14
# mu = .001
# gamma = .0026
# delta = .0011
# beta1 = .0024
# beta2 = .051
# alpha = .01


# Input

sigma = float(input('Enter the coefficient sigma ='))
mu = float(input('Enter the coefficient mu ='))
gamma = float(input('Enter the coefficient gamma ='))
delta = float(input('Enter the coefficient delta ='))
beta1 = float(input('Enter the coefficient beta1 ='))
beta2 = float(input('Enter the coefficient beta2 ='))
alpha = float(input('Enter the parameter alpha ='))

# Calculate
num = (delta*(beta1*sigma+(gamma+mu)*beta2))
den = (sigma+mu)*(gamma+mu)*mu
F = num/den
R = (1-alpha)*F
Ac = 1 -(1/F)

# Conditionals

if R == 1:
    print("The outbreak will become endemic.")
    if alpha < Ac:
      print('Endemic State, increase public health')
    else:
      print('No change in public health')   
elif R > 1:
    print("The outbreak will expand.")
    if alpha < Ac:
      print('Disease expansion state, Increase Public Health Measures')
    else:
      print('No change in public health measures')
else:
    print("The outbreak will die out.")
    if alpha > Ac:
       print('Disease controlled, Decrease Public Health Measures')
    else:
       print('No change in public health measures')

# Output

# print('F = ', F)
# print('R = ', R)
# print('Ac = ', Ac)





