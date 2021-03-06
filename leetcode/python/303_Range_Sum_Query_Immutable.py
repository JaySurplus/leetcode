"""
    303. Range Sum Query - Immutable
    Given an integer array nums, find the sum of the elements between indices i and j (i <= j), inclusive.

    Example:
        Given nums = [-2, 0, 3, -5, 2, -1]

        sumRange(0, 2) -> 1
        sumRange(2, 5) -> -1
        sumRange(0, 5) -> -3
        Note:
            You may assume that the array does not change.
            There are many calls to sumRange function.
"""

class Solution(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.matrix = [0] * (len(nums)+1)
        for i in xrange(len(nums)):
            self.matrix[i+1] = self.matrix[i] + nums[i]

    def sumRange(self, i, j):
        """
        sum of elements nums[i .. j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.matrix[j+1] - self.matrix[i]
nums = [-2,0,3,-5,2,-1]
sol = Solution(nums)
print sol.sumRange(1,4)

