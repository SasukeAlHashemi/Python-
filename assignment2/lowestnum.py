# Initialize a list to store the numbers
numbers = []

# Input 10 numbers from the user
for i in range(10):
    num = int(input("Enter number: "))
    numbers.append(num)

# Sort the list to easily find the lowest and second lowest numbers
numbers.sort()

# The first element is the lowest, and the second element is the second lowest
lowest = numbers[0]
second_lowest = numbers[1]

# Print the results
print(f"The lowest number is: {lowest}")
print(f"The second lowest number is: {second_lowest}")