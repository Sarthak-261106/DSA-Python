str1=input("Enter a string: ")

def is_palindrome(s):
    if s == s[::-1]:
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")

is_palindrome(str1)

