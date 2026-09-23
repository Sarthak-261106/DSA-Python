givennums = list(map(int, input().split()))
n=len(givennums)




def dnfalgo(givennums):
    n=len(givennums)
    low=0
    mid=0
    high=n-1

    while mid<=high:
        if givennums[mid]==0:
            givennums[low], givennums[mid] = givennums[mid], givennums[low]
            low+=1
            mid+=1
        elif givennums[mid]==1:
            mid+=1
        else:
            givennums[mid], givennums[high] = givennums[high], givennums[mid]
            high-=1
                  


    return givennums     

print(dnfalgo(givennums))
