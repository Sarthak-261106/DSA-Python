# str1=input("Enter a string: ")

# def is_palindrome(s):
#     if s == s[::-1]:
#         print("The string is a palindrome.")
#     else:
#         print("The string is not a palindrome.")

# is_palindrome(str1)

givenstr=input("Enter a string: ")

isPalindrome = True

for i in range(len(givenstr)//2):
    if givenstr[i] != givenstr[len(givenstr)-1-i]:
        isPalindrome = False
        break
if isPalindrome:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
