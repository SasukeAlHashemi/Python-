number = int(input("Enter number: "))
n, result = number, 1
while n > 0:
    result = result * n
    n = n - 1
factorial = result
print("Factorial of", number, "is", factorial)

