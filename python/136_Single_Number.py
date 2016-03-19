"""
	136. Single Number

	Given an array of integers, every element appears twice except for one. Find that single one.
	Note:
	Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
"""

class Solution(object):
	def singleNumberII(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		res = reduce(lambda a , b : a^b , nums)
		return res

	# Or
	
	def singleNumber(self, nums):
		res = nums[0]
		for num in nums[1:]:
			res ^= num
		return res


sol = Solution()
nums = [1,1,2,2,3,3,4,4,5,5,6,6,5,5,7,7,999,10,10]
res = sol.singleNumber(nums)
print res