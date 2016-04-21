"""
	283. Move Zeroes
	

	Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

	For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

	Note:
	You must do this in-place without making a copy of the array.
	Minimize the total number of operations.

"""
import time
class Solution(object):
    def moveZeroesIII(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        

        i = 0 
        j = len(nums)-1
        count = 0
        while i <= j :
        	
        	if nums[i] == 0 and nums[j] != 0:
        		nums[i] , nums[j] = nums[j],nums[i]
        		count += 1
        		i += 1
        		j -= 1
        	elif nums[i] == 0:
        		j -= 1
        	else:
        		i += 1
        #print count

    def moveZeroesII(self, nums):
    	j = 0
    	count = 0
    	for num in nums:
    		if num != 0:
    			count += 1
    			nums[j] = num
    			j += 1

    	for i in range(j,len(nums)):
    		nums[i] = 0
    	


    def moveZeroes(self, nums):
    	count = 0
    	j = -1
    	for i in range(len(nums)):
    		if nums[i] != 0:
    			j += 1
    			count +=1 
    			nums[j], nums[i] = nums[i], nums[j]
    			
    	


sol = Solution()
nums = [0, 1, 0, 3, 12,1,1,1,1,1]
#nums = [0,0,0,0,0,0,0,0]
sol.moveZeroesIII(nums)
nums = [0, 1, 0, 3, 12,1,1,1,1,1]
end = time.time()
print nums 
print end - start