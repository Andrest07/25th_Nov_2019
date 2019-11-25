def is_palindrome(x):
    y = ""
    for i in range(len(x)):
        if x[i].isalpha():
            y = y + x[i].lower()
    if y == reverse(x):
        print("Its a palindrome.")
    else:
        print("Its not a palindrome.")
def reverse(x):
    y = ""
    for i in range(len(x)-1,-1,-1):
        if x[i].isalpha():
            y = y + x[i].lower()
    return y
is_palindrome(input("please input the word:"))