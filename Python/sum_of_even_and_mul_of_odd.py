n=int(input("enter a Digit::"))
s=0
m=1
while n>0:
 r=n%10 
 if r%2==0:
    s=s+r
 else:
    m=m*r
 n=n//10    

print("The sum of even numbers:: ",s)
print("The Multipication of odd numbers:: ",m)