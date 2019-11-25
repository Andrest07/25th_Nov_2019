def max_of_three(x,y,z):
    if x > y and x > z:
        print("X is the largest.")
    elif y > x and y > z:
        print("Y is the largest.")
    elif z > x and z > y:
        print("Z is the largest.")
    else:
        print("They are all equal.")
max_of_three(input("Please input X:"), input("Please input Y:"), input("Please input Z:"))