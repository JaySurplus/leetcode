"""
	47. Permutations II

	Given a collection of numbers that might contain duplicates, return all possible unique permutations.

	For example,
		[1,1,2] have the following unique permutations:
		[1,1,2], [1,2,1], and [2,1,1].

"""

class Solution(object):
    def permuteUnique(self,nums):
    	nums.sort()
    	return self.permuteUniqueSort(nums)
    def permuteUniqueSort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
        	return []
        if len(nums) == 1:
        	return [nums]

        result = []
        dic = {}
        pre = None
        for i in range(len(nums)):
        	#if nums[i] not in dic.keys():
        	if nums[i] != pre:
        		#dic[nums[i]] = 1
        		pre = nums[i]
        		for j in self.permuteUnique(nums[:i]+nums[i+1:]):
        			result.append([nums[i]]+j)
        return result

    def permuteUniqueII(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
      	nums.sort()
        finalSol = []
        self.per(nums, [], finalSol)
        return finalSol

    def per(self, nums , result, finalSol):
    	if len(nums) == 0:
    		finalSol.append(result)
    		return
    	else:
    		pre = None
    		for i in range(len(nums)):
    			if nums[i] != pre:
    				self.per(nums[:i]+nums[i+1:], result+[nums[i]] , finalSol)
    				pre = nums[i]
sol = Solution() 
nums = [1,1,2,2,3,4,5,6,8]




import time

start1 = time.time()
for i in range(1):
	sol.permuteUniqueII(nums)
end1 = time.time()

start2 = time.time()
for i in range(1):
	sol.permuteUnique(nums)
end2 = time.time()

print end1-start1
print end2-start2