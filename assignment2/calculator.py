num1 = float(input("enter first number: "))
num2 = float(input("enter second number: "))

print("Press 1 to add")
print("Press 2 to subtract")
print("Press 3 to multiply")
print("Press 4 to divide")

choice = int(input("enter your choice: "))

if choice==1:
    print("Sum of the two numbers is ", num1 + num2)

elif choice==2:
    print("Difference of the two numbers is ", num1 - num2)

elif choice==3:
    print("Product of the two numbers is ", num1 * num2)

elif choice==4:
    print("Division of the two numbers is ", num1 / num2)

else:
    print("Enter a Valid Choice")

