n=int(input("Enter a number:: "))

p=n
q=n
c=0
s=0

while p > 0:
 r=p%10
 c=c+1
 p=p//10

while q > 0:
 r1=q%10
 s=s+pow(r1,c)
 q=q//10

if n==s:
  print("It is Armstrong Number")
else:
  print("it is not")   
