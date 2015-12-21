"""
	4Sum
	Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.
	https://leetcode.com/problems/4sum/
"""


class Solution(object):
	def nSum(self, nums, target , start , end ,  n = 4):
		
		print "n----" , n
		if n == 1:
			for i in range(start ,end ):
				if nums[i] == target :
					print nums[i]
					return nums[i]
			return None
		else:
			for i in range(start , end-n+1):
				#print "i" , i
				#print nums[i:end]
				if nums[i] != nums[i+1]:
					#result.append(nums[i])
					#print start , i ,nums[i]
					print "i" , i
					print (nums[i] , self.nSum( nums, target - nums[i] , i+1 , end, n-1))

	def fourSum(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: List[List[int]]
		"""
		nums.sort()
		print nums
		return self.nSum(nums, target , 0 , len(nums) , 4)

    



sol = Solution()
arr = [1, 0, -1, 0, -2, 2]
target = 0
print sol.fourSum(arr , target)

