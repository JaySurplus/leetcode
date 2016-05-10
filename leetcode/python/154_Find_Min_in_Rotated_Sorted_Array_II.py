"""
    154. Find Minimum in Rotated Sorted Array II


"""


class Solution(object):

    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return min(nums)

        l = 0
        r = len(nums) - 1



        while l <= r:

            while l < r and nums[l] == nums[l+1]:
                l += 1

            while l < r and nums[r] == nums[r-1]:
                r -= 1

            povit = (l + r) / 2
            if nums[povit] >= nums[r]:
                l = povit + 1
            else:
                r = povit
        return nums[r]


sol = Solution()
nums = [1,3,1,1]
print sol.findMin(nums)
