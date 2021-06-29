num1 = float(input("Enter the first number : "))
num2 = float(input("Enter the second number : "))
op = input("Enter the Operator : ")
if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1/num2)
elif op == "*":
    print(num1*num2)
else:
    print("Invalid Operator")

