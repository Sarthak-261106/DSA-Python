n=int(input())
mylist=[int(x) for x in input().split()]

def bubblesort(mylist):
    global n
    for i in range(n):
        for j in range(n-1):
            if mylist[j]>mylist[j+1]:
                mylist[j],mylist[j+1]=mylist[j+1],mylist[j]
    return mylist

print(bubblesort(mylist))