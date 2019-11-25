def piglatin(x):
    if not type(x) is str:
        raise TypeError("Only alphabetical letters are allowed.")
    else:
        a = x[0].lower()
        x = x[0:0:] + x[1::] + a + "ay"
        print(x.title())
piglatin(input("Please input a word:"))