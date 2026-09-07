import math
a=float(input("Enter value:: "))
b=float(input("Enter value:: "))
c=float(input("Enter value:: "))
d=(b**2)-(4*a*c)
if d>0:
 sol1=(-b+math.sqrt(d))/(2*a)
 sol2=(-b-math.sqrt(d))/(2*a)
 print("the solution1:",sol1,"solution2",sol2)
elif d==0:
 sol=-b/(2*a)
 print("the solution :",sol)
else:
 print("No real root")   