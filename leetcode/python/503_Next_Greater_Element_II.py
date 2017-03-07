"""
    503. Next Greater Element II
    https://leetcode.com/problems/next-greater-element-ii/?tab=Description
"""
class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [-1] * len(nums)
        stack = []
        for i in range(len(nums) * 2):

            n = nums[i%len(nums)]
            while stack and nums[stack[0]] < n:
                res[stack.pop(0)] = n
            if i < len(nums):
                stack = [i] + stack
        return res

sol = Solution()
nums = [1,2,1]
print sol.nextGreaterElements(nums)
