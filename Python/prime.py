n=int(input("Enter a number:: "))

for i in range(2,n//2):
   r=n%i
   break
 
if r!=0:
     print(n,"is prime number.")
else :
     print(n,"is not prime number.")     