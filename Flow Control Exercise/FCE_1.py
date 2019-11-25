def max(x,y):
    if x > y:
        print("X is larger.")
    elif y > x:
        print("Y is larger.")
    else:
        print("They are equal.")
max(input("Please input x:"), input("Please input y:"))