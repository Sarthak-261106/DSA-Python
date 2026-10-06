n=int(input())
mylist=[int(x) for x in input().split()]

# def quicksort(mylist):
#     if len(mylist)<=1:
#         return mylist
#     else:
#         pivot=mylist[0]
#         left=[x for x in mylist[1:] if x<=pivot]
#         right=[x for x in mylist[1:] if x>pivot]
#         return quicksort(left)+[pivot]+quicksort(right)

def partition(mylist,left,right):
    pivot=mylist[right]
    i=left
    j=right-1
    
    while i<j:
        while i<right and mylist[i]<=pivot:
            i+=1
        while j>left and mylist[j]>pivot:
            j-=1    
        if i<=j:
            mylist[i],mylist[j]=mylist[j],mylist[i]
    if mylist[i]>pivot:
        mylist[i],mylist[right]=mylist[right],mylist[i]   
    return i




def quicksort(mylist,left,right):
    if left<right:
        partionPos=partition(mylist,left,right)
        quicksort(mylist,left,partionPos-1)
        quicksort(mylist,partionPos+1,right)
    return mylist    



print(quicksort(mylist,0,n-1))    