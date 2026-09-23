nums = list(map(int, input().split()))
n=len(nums)


# def mvalgo(nums):
#         n = len(nums)
#         nums.sort()

#         return nums[n // 2]

def mvalgo(nums):
    nums.sort()
    majority_ele=nums[0]
    max_count=0
    count=1

    for i in range(n-1):
        if nums[i]!=nums[i+1]:
            if max_count<count:
                majority_ele=nums[i]
                max_count=count
            count=1
        else:
            count+=1        
            

    return majority_ele,max_count  


print(mvalgo(nums))

