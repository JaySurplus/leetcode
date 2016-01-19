"""
	78. Subsets

	Given a set of distinct integers, nums, return all possible subsets.

	Note:
	Elements in a subset must be in non-descending order.
	The solution set must not contain duplicate subsets.
	For example,
	If nums = [1,2,3], a solution is:

	[
	  [3],
	  [1],
	  [2],
	  [1,2,3],
	  [1,3],
	  [2,3],
	  [1,2],
	  []
	]

	https://leetcode.com/problems/subsets/
"""

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []
        n = len(nums)
        self.dfs(nums,n,[])
        return self.res

    def dfs(self, nums , n , temp):
    	if n == 0:
    		if len(temp) > 1:
    			temp.sort()
    		self.res.append(temp)
    	else:
    		for i in range(len(nums)-n+1):
    			self.dfs(nums[i+1:] , n-1 , temp + [nums[i]])
    			self.dfs(nums[i+1:] , n-1 , temp )

sol = Solution()
nums = [4,1,0,-1]

print sol.subsets(nums)
