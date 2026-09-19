import sys

def getnum(char):
    if char=='0':
        return 1
    else:
        return -1

     
givenstr = input()

def flipbits(givenstr):
    ans=0
    
    for i in givenstr:
        if i=='1':
            ans+=1


    maxsum = -sys.maxsize -1
    currsum = 0
    start = 0
    end = 0

    n=len(givenstr)

    while end<n:
        while currsum<0:
            currsum-=getnum(givenstr[start])
            start+=1

        currsum+=getnum(givenstr[end])
        end+=1    

        maxsum=max(maxsum, currsum)
    return ans+maxsum    

print(flipbits(givenstr))