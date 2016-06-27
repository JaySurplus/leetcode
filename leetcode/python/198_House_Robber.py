"""
    198. House Robber

    You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

    Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the
"""

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums :
            return 0
        if len(nums) == 1:
            return nums[0]

        pp = nums[0]
        p = max(pp, nums[1])

        if len(nums) == 2:
            return max(pp, p)

        for n in nums[2:]:
            t = max(pp+n, p)
            pp = p
            p = t
        return p


