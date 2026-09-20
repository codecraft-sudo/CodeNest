# Check even and odd numbers from a given list.

n=[10,11,14,23,44,45,66,68,87,92]
even=[]
odd=[]

print("The original list",n)

for i in n:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)

print("The even numbers:",even)
print("The odd numbers:",odd)
