print("1.For Convert Celsius to Fahrenheit")
print("2.For Fahrenheite to Celsius")
print("Choice which operation do you perform:: ")
n=int(input("Enter your choice(1-3) "))
match n:
    case 1:
        c=float(input("Enter the value of celcius:: "))
        f=(9*c)/5+32
        print("The fahrenhite::%.2f"%f)
    case 2:
        f=float(input("Enter the value of fahrenhite:: "))
        c=(32-f)*5/9
        print("The celcius:: %.2f"%c)
    case _:
        print("Invalid input")     

