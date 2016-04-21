"""
	3Sum

	Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

		


	https://leetcode.com/problems/3sum/

"""

class Solution(object):
	def threeSum(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		length = len(nums)
		i = 0
		result = []
		nums.sort()
	
		while i <= length -3:

			j = i+1
			k = length -1
			
			
			while j < k :
				
				
				if nums[i] + nums[j] == -nums[k]:
					
					result.append((nums[i] , nums[j] , nums[k]))

					j+=1 
					k-=1
					while nums[j-1] == nums[j] and j < k:
						j+=1
					while nums[k+1] == nums[k] and j < k:
						k-=1
					
					
				
				elif nums[i] + nums[j] < -nums[k]:
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

"""
class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        num.sort()
        res = []
        for i in range(len(num)-2):
            if i == 0 or num[i] > num[i-1]:
                left = i + 1; right = len(num) - 1
                while left < right:
                    if num[left] + num[right] == -num[i]:
                        res.append([num[i], num[left], num[right]])
                        left += 1; right -= 1
                        while left < right and num[left] == num[left-1]: left +=1
                        while left < right and num[right] == num[right+1]: right -= 1
                    elif num[left] + num[right] < -num[i]:
                        while left < right:
                            left += 1
                            if num[left] > num[left-1]: break
                    else:
                        while left < right:
                            right -= 1
                            if num[right] < num[right+1]: break
        return res
"""
sol = Solution()

nums = [-1 , 0 ,1 ,2 ,-1 ,-4]
nums = [-2,0,0,2,2]
#nums = [-2,0,1,1,2]
print sol.threeSum(nums)