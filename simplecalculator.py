num1 = float(input("Enter the first number: "))

num2 = float(input("Enter the second number: "))

op = input("Enter an operation (+, -, *, /): ")

result = 0

if op == "+": 
    result = num1 + num2

elif op == "-": 
    result = num1 - num2

elif op == "*": 
    result = num1 * num2

elif op == "/": 
    result = num1 / num2

else: 
    print("Invalid operation")

print(num1, op, num2, "=", result)
