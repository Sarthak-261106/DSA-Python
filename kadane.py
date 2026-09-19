# n=int(input())
# givennums=[]

# for i in range(n):
#     givennums.append(int(i) for i in input().split())
#     print(givennums)

# def largestSubarraySum(givennums):
#     maxsum=0
#     currsum=0
#     start=0
#     end=0

#     while end<len(givennums):
#         while currsum<0:
#             currsum-=givennums[start]
#             start+=1

#     currsum+=givennums[end]
#     if currsum>maxsum:
#         maxsum=currsum
#     else:
#         end+=1

#     print(maxsum)
#     print(givennums[start:end+1])    
            
givennums = list(map(int, input().split()))

def largestarraysum(givennums):
    maxsum = 0
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





