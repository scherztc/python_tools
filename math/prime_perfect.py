#Library
import math

#Input Values
K=int(input('Input a whole number'))

#Initial Values
C1=0
C2=0
w=2
p=2


#Loop through numbers
while w < K-1:
  S=0
  n=w
  m=math.ceil(n/2)+1
  for p in range(2,m-1):
    R=n%p
    p=p+1  
    if R==0:
      S=S+p 
  w=w+1
  if S==0: 
    print(f"{n} is a Prime number" )
    C1=C1+1 
  elif:
    if S==n-1:
       print(f"{n} is a Perfect number" )
       C2=C2+1
print(f"The total number of prime numbers found is C1= {C1}" )
print(f"The total number of perfect numbers found is C2= {C2}" )


