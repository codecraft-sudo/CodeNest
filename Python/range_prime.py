a = int(input("Enter starting range: "))
b = int(input("Enter ending range: "))

for num in range(a, b + 1):
    n = 0
    for i in range(2, num):
        if num % i == 0:
            n = 1
            break

    if n == 0:
        print(num, "is prime number.")
   
