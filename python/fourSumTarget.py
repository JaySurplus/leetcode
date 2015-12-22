"""
	4Sum
	Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.
	https://leetcode.com/problems/4sum/
"""
import copy

class Solution(object):




	def nSum(self, nums, target , start , end ,  n  ,finalResult , subResult):
		
		if n == 2:
			
			i = start
			j = end -1
			print i , j
			while i < j :
				if nums[i] == target - nums[j]:
					subResult.append(nums[i]) 
					subResult.append(nums[j])
					finalResult.append(subResult)
					subResult = subResult[:-2]
					
					while i < j:
						i +=1 
						if nums[i] != nums[i-1]:
							break
					while i < j:
						j -= 1
						if nums[j] != nums[j+1]:
							break

				elif nums[i] <= target - nums[j]:
					while i < j:
						i +=1 
						if nums[i] != nums[i-1]:
							break
				else:
					while i < j:
						j -= 1
						if nums[j] != nums[j+1]:
							break
			
		else:
			
			for i in range(start , end-n+1):

				if i == 0:
					 
					subResult.append(nums[i])
					print "subResult" , subResult ,i
					self.nSum(nums, target-nums[i] , i+1 , end, n-1 , finalResult, subResult)
					subResult = subResult[:-1]

				else:		
				#elif nums[i] != nums[i-1]:
					if 
					print "subResult" , subResult
					subResult.append(nums[i])
				
					self.nSum(nums, target-nums[i] , i+1 , end, n-1 , finalResult, subResult)
					subResult = subResult[:-1]

		return finalResult

		
		
	def fourSum(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: List[List[int]]
		"""
		nums.sort()
		finalResult = []
		subResult = []

		return self.nSum(nums, target , 0 , len(nums), 4 , finalResult, subResult)

    



sol = Solution()
arr = [1, 0, -1, 0, -2, 2]
target = 0
print sol.fourSum(arr , target)

