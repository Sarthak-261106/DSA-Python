def nextgreater(nums):
    stack = []
    result = [-1] * len(nums)

    for i in range(len(nums)):
        while stack and nums[i] > nums[stack[-1]]:
            index = stack.pop()
            result[index] = nums[i]
        stack.append(i)

    return result



class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        nge = {}

        for num in nums2:
            while stack and num > stack[-1]:
                nge[stack.pop()] = num

            stack.append(num)

        ans = []
        for num in nums1:
            ans.append(nge.get(num, -1))

        return ans
