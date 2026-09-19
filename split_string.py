s=input("Enter a binary string of even lenght: ")

p1=s[0:len(s)//2]
p2=s[len(s)//2:len(s)]

if p1.count('0')==p2.count('0') and p1.count('1')==p2.count('1'):
    print(f"yes s can be divided into two parts with equal 0 and 1 ie {p1} and {p2}")
else:
    print('not even lenght or not equal 0 and 1 in both parts')    



