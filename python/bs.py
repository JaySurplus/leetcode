class Solution(object):
	def bs(self, nums,target):
		l = 0
		r = len(nums) - 1
		while l <= r:
			m = (l+r)/2
			if nums[m] == target:
				return m
			elif nums[m] < target:
				l += 1
			else:
				r -= 1
		return -1

nums = [1,2,3,4,5,6,7,8,9,10]
sol = Solution()
target = 10
print sol.bs(nums,target)