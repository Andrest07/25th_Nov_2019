def is_palindrome(x):
    if x == reverse(x):
        print("Its a palindrome.")
    else:
        print("Its not a palindrome.")
def reverse(x):
    y = ""
    for i in range(len(x)-1,-1,-1):
        y = y + x[i]
    return y
is_palindrome(input("please input the word:"))