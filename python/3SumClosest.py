"""
	3Sum Closest

	Given an array S of n integers, find three integers in S such that 
	the sum is closest to a given number, target. Return the sum of 
	the three integers. You may assume that each input would have exactly one solution.


	https://leetcode.com/problems/3sum-closest/
"""


class Solution(object):
	def threeSumClosest(self, nums , target):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		length = len(nums)
		i = 0
		
		nums.sort()
		

		result = nums[0]+nums[1] + nums[length-1] 

		if result == target:
			return result

		while i <= length -3:

			j = i+1
			k = length -1
			
			
			while j < k :
				
				dt = nums[i] + nums[j] + nums[k] - target
				
				if abs(dt) < abs(result - target):
					result = nums[i] + nums[j] + nums[k] 

				if dt == 0:
					
					return target
					
					
				elif dt < 0:
					while j  < k:
						j += 1
						if nums[j] > nums[j-1]:
							break
				else:
					while j < k:
						k -= 1
						if nums[k] < nums[k+1]:
							break	
			
		

			while nums[i+1] == nums[i] and i + 1 <= length-3:
				i += 1
			
			i+=1
			

		return result


sol = Solution()
nums = [-1,2,1,-4]
nums = [1,2,4,8,16,32,64,128]
target = 82
print sol.threeSumClosest(nums, target)
