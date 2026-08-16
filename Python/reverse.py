n=int(input("Enter a number:: "))
s=0
m=n
while(n>0):
    r=n%10
    s=10*s+r
    n=n//10
print("The reverse of",m,"is =",s)    
 
