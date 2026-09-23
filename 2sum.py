givennums = list(map(int, input().split()))
givennums.sort()
n=len(givennums)

target=int(input())

def twoSum(self, givennums, target):
    left=0
    right=n-1

    while left<right:
        currsum=givennums[left]+givennums[right]

        if currsum==target:
            return [left, right]
        elif currsum<target:
            left+=1
        else:
            right-=1
    return []

