def grosspay(x,y):
    z = 0
    if x > 40:
        z= (y * 1.5) * x
    else:
        z = y * x
    print("Pay:" + str(z))
grosspay(int(input("Enter Hours:")),int(input("Rate:")))