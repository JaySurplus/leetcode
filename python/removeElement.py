"""
	Remove Element
	Given an array and a value, remove all instances of that value in place and return the new length.

	The order of elements can be changed. It doesn't matter what you leave beyond the new length.
"""


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        j = len(nums) - 1
        for i in range(len(nums)-1, -1 ,-1):
        	if nums[i] == val:
        		temp = nums[i]
        		nums[i] = nums[j]
        		nums[j] = temp
        		j -= 1
        return j+1 , nums[:j+1]
       
        		
sol = Solution()
nums = [1,1,2,3,4,45,5,6,2,1,1,2]
val = 45
print sol.removeElement(nums, val)