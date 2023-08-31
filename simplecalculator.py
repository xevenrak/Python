# ngambil angka ke1 trus disimpen di num1
num1 = float(input("Enter the first number: "))

# ngambil angka ke2 trus disimpen ke num2
num2 = float(input("Enter the second number: "))

# ngambil hasil operasi dari user trus disimpen di op
op = input("Enter an operation (+, -, *, /): ")

# hasill
result = 0

# ngecek operasi
if op == "+": # kalo op +
    # ditambah
    result = num1 + num2
elif op == "-": # kalo op -
    # dikurangi
    result = num1 - num2
elif op == "*": # kalo op *
    # dikali
    result = num1 * num2
elif op == "/": # kalo op /
    # dibagi
    result = num1 / num2
else: # kalo op hal lain
    # pesan error
    print("Invalid operation")

# hasil
print(num1, op, num2, "=", result)
