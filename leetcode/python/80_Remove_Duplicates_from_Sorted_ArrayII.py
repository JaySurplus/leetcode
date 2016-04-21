"""
	80. Remove Duplicates from Sorted Array II

	https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

	Follow up for "Remove Duplicates":
	What if duplicates are allowed at most twice?

	For example,
	Given sorted array nums = [1,1,1,2,2,3],

	Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3. It doesn't matter what you leave beyond the new length.
"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
    

      	if len(nums) <= 2:
      		return 2

      	count = 2
        for i in range(2,len(nums)):
        	if nums[i] != nums[count-2]:
        		nums[count] = nums[i]
        		count += 1
        return count

sol = Solution()
nums = [1,1,1,2,2,3,4,4,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,8,8,8]

res=  sol.removeDuplicates(nums)
print nums[:res]
print nums