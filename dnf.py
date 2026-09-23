givennums = list(map(int, input().split()))
n=len(givennums)


def dnfalgo(givennums):
    low=0
    mid=0
    high=n-1

    while mid<=high:
        if givennums[mid]==0:
            givennums[low], givennums[mid] = givennums[mid], givennums[low]
            low+=1
            mid+=1
        if givennums[mid]==1:
            mid+=1
        if givennums[mid]==2:
            givennums[mid], givennums[high] = givennums[high], givennums[mid]
            high-=1
                  


    return givennums     

print(dnfalgo(givennums))
