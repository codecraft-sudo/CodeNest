a=float(input("Enter first number::: "))
b=float(input("Enter second number:: "))

op=input("Enter an operator(+,-,*,/): ")
if op == "+":
    print("Result =",a+b)
elif op == "-":
    print("Result =",a-b)
elif op == "*":
    print("The result =",a*b)
elif op == "/":
   if b!=0: 
    print("The result =",a/b)
   else:
    print("Cann't devide by zero")           
else:
   print("Invalid operator")       