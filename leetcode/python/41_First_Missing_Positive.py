"""
	41. First Missing Positive

	Given an unsorted integer array, find the first missing positive integer.

	For example,
	Given [1,2,0] return 3,
	and [3,4,-1,1] return 2.

	Your algorithm should run in O(n) time and uses constant space.

"""

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        i = 0
        while i < n:
        	#
        	if nums[i] > 0 and nums[i] < n:
     
        		if nums[nums[i]-1] != nums[i]:
        			temp = nums[i]
        			nums[i] = nums[nums[i]-1]
        			nums[temp-1] = temp
        			i -= 1
        	i+=1			
     
        for i in range(n):
        	if nums[i] != i+1:
        		return i+1
        return n+1

sol = Solution()
nums = [-1,4,2,1,9,10]
print sol.firstMissingPositive(nums)


