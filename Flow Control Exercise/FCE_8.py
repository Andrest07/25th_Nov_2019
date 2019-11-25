def generate_n_chars(n,c):
    y = ""
    for i in range(n):
        y = y + c
    print(y)
generate_n_chars(int(input("Please input the amount:")),input("Please input the letter:"))