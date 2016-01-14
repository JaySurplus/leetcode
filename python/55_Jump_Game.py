"""
	55. Jump Game

	Given an array of non-negative integers, you are initially positioned at the first index of the array.

	Each element in the array represents your maximum jump length at that position.

	Determine if you are able to reach the last index.

	For example:
		A = [2,3,1,1,4], return true.

		A = [3,2,1,0,4], return false.


"""

class Solution:
	
	def canJumpI(self, nums):

		

		m = 0
		l = len(nums) - 1

		for i in range(len(nums)):
			if m < i:
				return False
			else:
				m = max(m , i + nums[i])
				if m >= l:
					return True


	def canJump(self, nums):

		check = True
		ind = 0
		for i in range(len(nums)-1):
			if nums[i]==0:
				check=False
				for x in range(ind ,i):
					if nums[x] + x > i:
						if nums[x] + x >= len(nums) -1:
							return True
						check = True
				ind = x 
				if check == False:
					return False
		return True
        
		

sol = Solution()
nums = [2,3,1,1,4]

#print sol.canJump(nums)

nums = [3,2,1,0,4]
#print sol.canJump(nums)

nums = [1,0]
#print sol.canJump(nums)

nums = [0,1]
#print sol.canJump(nums)

nums = [2,4523,0 ,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0] 
print sol.canJump(nums)