# Reverse a given list
A = [1, 2, 3, 4, 5]

print("The original list:", A)

B = []

for i in range(0, 5):
    B.append(A[4-i])

print("The reversed list:", B)