n=int(input())

matrix=[]
for i in range(n):
    matrix.append([int(i) for i in input().split()])

print(matrix)    

for i in range(n):
    for j in range(n):
        if j>i:
            temp=matrix[j][i]
            matrix[j][i]=matrix[i][j]
            matrix[i][j]=temp

print(matrix)
