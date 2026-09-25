# def binarysearch(mylist,target):
#     low=0
#     high=len(mylist)-1
#     while low<=high:
#         mid=(low+high)//2
#         if mylist[mid]==target:
#             return True
#         elif mylist[mid]<target:
#             low=mid+1
#         else:
#             high=mid-1
#     return False




# n=int(input())
# target=int(input())
# mylist=[int(x) for x in input().split()]
# mylist.sort()

# found=False
# for i in mylist:
#     if i==target:
#         found=True
#         break

# if found:
#     print("YES")
# else:
#     print("NO")
mylist=[]
target=0

def binarysearch(start,end):
    global mylist,target
    if end-start<=1:
        if mylist[start]==target:
            return start
        if mylist[end]==target:
            return end
        return-1

    middle=(start+end)//2

    if mylist[middle]>target:
        return binarysearch(start,middle)

    return binarysearch(middle,end)


        