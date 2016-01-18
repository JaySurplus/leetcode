"""	
	75. Sort Colors

	Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

	Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

	Note:
	You are not suppose to use the library's sort function for this problem.

"""

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """ 
        #if len(nums) == 0:
        #	return

        r = 0
        b = len(nums) - 1

        i = 0

        while i <= b:
            if nums[i] == 1:
                i += 1
            elif nums[i] == 0:
                temp = nums[i]
                nums[i] = nums[r]
                nums[r] = temp
                r += 1
                i += 1

        
            else:
                temp = nums[i]
                nums[i] = nums[b]
                nums[b] = temp
                b -= 1

sol = Solution()

nums = [0]
sol.sortColors(nums)
print nums

nums = [1,2,2,2,1,1,0,0,1,0,1,2,0,0,0,2,2,2,1,1,1,0]
nums = []
sol.sortColors(nums)
print nums