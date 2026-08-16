n=int(input("Enter how many numbers:"))
l=int(input("Enter number 1:"))
for i in range(2,n+1):
    n2=int(input("Enter number"+str(i)+":"))

if n2>l:
    l=n2
    print("Largest number: ",l)