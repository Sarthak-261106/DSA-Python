n=int(input())
mylist=[int(x) for x in input().split()]

def merge(left,right):
    result=[]
    i=j=0
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result+=left[i:]
    result+=right[j:]
    return result


def mergeSort(mylist):
    if len(mylist)<=1:
        return mylist
    else:
        mid=len(mylist)//2
        left=mergeSort(mylist[:mid])
        right=mergeSort(mylist[mid:])
        return merge(left,right)

print(mergeSort(mylist))    