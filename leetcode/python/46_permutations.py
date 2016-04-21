"""
	46. Permutations

	
	Given a collection of distinct numbers, return all possible permutations.

	For example,

	[1,2,3] have the following permutations:

	[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].

"""

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
      
        finalSol = []
        self.per(nums, [], finalSol)
        return finalSol

    def per(self, nums , result, finalSol):
    	if len(nums) == 0:
    		finalSol.append(result)
    		return
    	else:
    		for i in range(len(nums)):
    			self.per(nums[:i]+nums[i+1:], result+[nums[i]] , finalSol)
    			

    def permute2(self, nums):
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [nums]
        result = []
        for i in range(len(nums)):
        	for j in self.permute2(nums[:i] + nums[i+1:]):
        		result.append([nums[i]]+j)
        return result



sol = Solution()

nums = [1,1,2,2,3,4,5,6,8]
import time

start1 = time.time()
for i in range(1):
	sol.permute(nums)
end1 = time.time()

start2 = time.time()
for i in range(1):
	sol.permute2(nums)
end2 = time.time()

print end1-start1
print end2-start2