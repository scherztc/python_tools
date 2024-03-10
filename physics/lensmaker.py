n = float(input('Enter the refraction index of the lens material '))
R1 = float(input('Enter the first radius of curvature of the lens surface '))
R2 = float(input('Enter the second radius of curvature of the lens surface '))
d = float(input('Enter the thickness of the lens ' ))

f = (n-1)*(1/R1-1/R2)
fd = (n-1)*(1/R1-1/R2+(n-1)*d/(n*R1*R2))
K = (fd-f)/fd

if K>.01:
   print('This is not a thin lens')
else:
   print('This is a thin lens')
   S1 = R1/(n-1)
   S2 = -R2/(n-1)
   M0 = -S2/S1

   if (f>0 and M0<0):
      print('The converging system produces a upside-down real image')
   elif (f>0 and M0>0):
      print('The converging system produces a upright virtual image')
   elif (f<0 and M0<0):
      print('The diverging system produces a upside-down real image')
   elif (f<0 and M0>0):
      print('The diverging system produces a upright virtual image.')
   if (abs(M0)>1):
      print('The image is bigger than the object')
   elif(abs(M0<1)):
      print('The image is smaller than the object')
   else:
      print('The image is the same size as the object')
