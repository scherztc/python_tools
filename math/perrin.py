#Library
import math

#Input Values
n=int(input('Enter the number of Perrin prime numbers'))

#Initial Values
w=4
x=0
y=3
count=0

#Find and Print z

while count<n:
    z=w+x
    m=math.ceil(z/2)+1
    S=0
    for i in range (2,m):
        R=z % i
        if R==0:
            S=S+1
    if S==0 and z!=y:
        print(z)
        count=count+1
    w=x
    x=y
    y=z

    print(w)
    print(x)
    print(y)
    print(z) 
  
# def trace_table():
#   trace_table = []
#   for i in range(6):
#      row = []
#      row.append(i)
#      row.append(find_z())
#      trace_table.append(row)
#   print(trace_table)

