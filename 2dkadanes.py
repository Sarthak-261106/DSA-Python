import sys

def largestrectsum(givennums):
    maxsum = -sys.maxsize-1
    currsum = 0
    start = 0
    end = 0

    n=len(givennums)

    while end<n:
        while currsum<0:
            currsum-=givennums[start]
            start+=1

        currsum+=givennums[end]
        end+=1    

        maxsum=max(maxsum, currsum)
    return maxsum

x=int(input())

matrix=[]
for i in range(x):
    matrix.append([int(i) for i in input().split()])

n=len(matrix)
m=len(matrix[0])
ans= -sys.maxsize-1


for i in range(m):
    temp=[]
    for j in range(n):
        temp.append(matrix[j][i])

    ans=max(ans, largestrectsum(temp))    

    for j in(i+1,m):
        for k in range(n):
            temp[k]+=matrix[k][j]
        ans=max(ans, largestrectsum(temp))      

print(ans)



    





