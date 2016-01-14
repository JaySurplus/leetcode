"""
	53.Maximum Subarray

	Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

	For example, given the array [-2,1,-3,4,-1,2,1,-5,4]
	the contiguous subarray [4,-1,2,1] has the largest sum = 6

"""

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
       
     
        s = 0
        m = nums[0]

     

        for i in nums:
        	s += i
        	if s > m:
        		m = s
        	if s < 0:
        		s = 0
        return m
        
        """
    	s = 0
    	m = nums[0]
    	for i in nums:
        	s += i
        	m = max(s,m)
        	s = max(0,s)
    	return m
    	"""
sol = Solution()

nums = [-2,1,-3,4,-1,2,1,-5,4]
nums = [-2]
print sol.maxSubArray(nums)
