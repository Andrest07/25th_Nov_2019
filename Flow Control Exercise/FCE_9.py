def grade(x):
    if x >= 0.9 and x <= 1.0:
        print("Your grade is A.")
    elif x >= 0.8 and x <= 1.0:
        print("Your grade is B.")
    elif x >= 0.7 and x <= 1.0:
        print("Your grade is C.")
    elif x >= 0.6 and x <= 1.0:
        print("Your grade is D.")
    elif x < 0.6:
        print("Your grade is F.")
    else:
        print("Error: Score is out of range.")
grade(float(input("Please input your score:")))
