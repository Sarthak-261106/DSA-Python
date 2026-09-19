# s=input("Enter a binary string of even lenght: ")

# p1=s[0:len(s)//2]
# p2=s[len(s)//2:len(s)]

# if p1.count('0')==p2.count('0') and p1.count('1')==p2.count('1'):
#     print(f"yes s can be divided into two parts with equal 0 and 1 ie {p1} and {p2}")
# else:
#     print('not even lenght or not equal 0 and 1 in both parts')    

# givenstr=input()

# countone=0
# countzero=0

# for i in givenstr:
#     if i=='1':
#         countone+=1
#     else:
#         countzero+=1

# if countone%2==1 and countzero%2==1:
#     print("-1")
# else:
#     currone=0
#     currzero=0
#     for i in range(len(givenstr)//2):
#         if givenstr[i] == '1':
#             currone+=1
#         else:
#             currzero+=1

# if currone==countone//2 and currzero==countzero//2:
#     for i in range(len(givenstr)//2):
#         print(givenstr[i], end="")

#         print()

#         for i in range(len(givenstr)//2, len(givenstr)):
#             print(givenstr[i], end="")

#         print()

# else:
#     print("-1")


givenstr = input()

countone = 0
countzero = 0

for i in givenstr:
    if i == '1':
        countone += 1
    else:
        countzero += 1

if countone % 2 == 1 or countzero % 2 == 1:
    print("-1")
else:
    currone = 0
    currzero = 0

    for i in range(len(givenstr) // 2):
        if givenstr[i] == '1':
            currone += 1
        else:
            currzero += 1

    if currone == countone // 2 and currzero == countzero // 2:
        for i in range(len(givenstr) // 2):
            print(givenstr[i], end="")
        
        print()

        for i in range(len(givenstr) // 2, len(givenstr)):
            print(givenstr[i], end="")
        
        print()
    else:
        print("-1")






