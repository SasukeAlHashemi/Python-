weight = float(input("enter your weight in kgs"))
height = float(input("enter your height in meters"))
BMI = weight/(height**2)
print(BMI)

if BMI < 18.5:
    print("The person is underweight")

elif BMI >= 18.5 and BMI <= 24.9:
    print("The person is of normal weight")

elif BMI >= 25 and BMI <= 29.9:
    print("The person is overweight")

else:
    print("The person is obese")

