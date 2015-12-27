"""
	Next Permutation
	

	Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

	If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

	The replacement must be in-place, do not allocate extra memory.

	Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
	1,2,3 - 1,3,2
	3,2,1 - 1,2,3
	1,1,5 - 1,5,1

	https://leetcode.com/problems/next-permutation/

"""

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        curr_max = len(nums)-1
        curr_min = curr_max
        i = curr_max - 1
        
        while i >= 0:
       
        	if nums[i] < nums[curr_max]:
        		if nums[i] < nums[curr_min]:
        			nums[i] ,nums[curr_min] = nums[curr_min] , nums[i]  
        			
        		else:
        			for j in range(i+1, len(nums)-1):
        				print nums[j]
        				if nums[j] > nums[i] and nums[j+1] <= nums[i]:
        					nums[i] ,nums[j] = nums[j] , nums[i]  
        		break
        	else:
        		curr_max = i 
        	i -= 1

        start = i + 1
        
        
        for i in range(len(nums[start:])/2):
        	
        	temp = nums[start+i]
        	nums[start+i] = nums[start+len(nums[start:])-1-i]
        	nums[start+len(nums[start:])-1-i]= temp

        

sol = Solution()
nums = [1,3,5,4,2]
#nums = [7,6,6,6,6,4,3,2]
#nums = [1,3,1]
sol.nextPermutation(nums)
print nums