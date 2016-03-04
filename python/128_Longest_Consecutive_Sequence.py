"""
	128. Longest Consecutive Sequence

	Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

	For example,
	Given [100, 4, 200, 1, 3, 2],
	The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

	Your algorithm should run in O(n) complexity.
"""

import time
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        dic = {}
        #for i in nums:
        #	print i

        best = 0

        while nums:
        	m = n = nums.pop()
        	while m - 1 in nums:
        		nums.remove(m-1)
        		m -= 1
        	while n + 1 in nums:
        		nums.remove(n+1)
        		n += 1
        	best = max(best , n - m +1)
        	
        return best


sol = Solution()
nums = [100,101,102,103 ,5,4,200,6,8,201,7,1,3,2 , 105 ,104]
#nums = [1,-8,7,-2,-4,-4,6,3,-4,0,-7,-1,5,1,-9,-3]
#nums = [1,2,3,4,5,0, -1]
res = sol.longestConsecutive(nums)

print res
