for i in range(1,101):
    grade=float(input("Whats the student's percentage? "))

    if grade >= 90:
        print("Thats an A+ !")

    elif grade >= 80 and grade < 90:
        print("Thats an A !")

    elif grade >= 60 and grade < 80:
        print("Thats an A-")

    else:
        print("You failed !")
