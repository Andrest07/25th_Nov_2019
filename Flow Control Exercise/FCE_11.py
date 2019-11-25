def distance_from_zero(x):
    if isinstance(x,int) or isinstance(x,float):
        print(abs(x))
    else:
        print("Nope")
distance_from_zero(eval(input("Please input the value:")))