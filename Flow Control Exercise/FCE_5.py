def reverse(x):
    y = ""
    for i in range(len(x)-1,-1,-1):
        y = y + x[i]
    print(y)
reverse(input("Please input the sentence:"))