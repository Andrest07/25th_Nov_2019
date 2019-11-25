def vowel(ch):
    if ch.upper() == "A" or ch.upper() == "I" or ch.upper() == "E" or ch.upper() == "O" or ch.upper() == "U":
        print(ch + " is a vowel.")
    else:
        print(ch + " is not a vowel.")
vowel(input("Please input the letter:"))