n=int(input("enter a number::"))
c=0
while(n>0):
    r=n%10
    c=c+1
    n=n//10
print("The total digit of this digit is:: ",c)    