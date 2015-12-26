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
        
        l = 0
        curr = 0
        while curr < len(nums):
        	if curr + l - 1 == len(nums):
        		break

        	else:
        		if nums[curr] == val:
        			l 

        return curr
        		
        		
        		
