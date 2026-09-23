nums = list(map(int, input().split()))
n=len(nums)


def mvalgo(nums):
        n = len(nums)
        nums.sort()

        return nums[n // 2]


print(mvalgo(nums))

