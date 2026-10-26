# str1=str(input("Enter a string of parentheses: "))


# def isValid(s):
#     stack = []
#     mapping = {")": "(", "}": "{", "]": "["}
#     for char in s:
#         if char in mapping:
#             top_element = stack.pop() if stack else '#'
#             if mapping[char] != top_element:
#                 return False
#         else:
#             stack.append(char)
#     return not stack

opening=['(', '[', '{']
closing=[')', ']', '}']

def balanced(givenstr):
    stack = []
    for i in givenstr:
        if i in opening:
            stack.append(i)
        else:
            if len(stack)==0:
                return "Not balanced"
            index=closing.index(i)
            if opening[index]==stack[-1]:
                stack.pop()
            else:
                print("Not balanced")

    if len(stack)==0:
        return "Balanced"
    else:
        return "Not balanced"     

strr='(())}'

print(balanced(strr))