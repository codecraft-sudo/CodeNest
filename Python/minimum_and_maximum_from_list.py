# Find minimum and maximum from a list.

a=[25,19,10,34,82,54,12,67]
min=a[0]
max=a[0]

print("The original list",a)

for i in a :
    if i<min:
        min=i
    if i>max:
        max=i
print("The minimum value:",max)
print("The maximum valeu:",min)            