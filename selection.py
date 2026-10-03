n=int(input())
mylist=[int(x) for x in input().split()]

def selectionsort(mylist):
    for i in range(n):
        minindex=i
        for j in range(i,n):
            if mylist[j]<mylist[minindex]:
                minindex=j
        mylist[i], mylist[minindex] = mylist[minindex], mylist[i]
    return mylist

print(selectionsort(mylist))
