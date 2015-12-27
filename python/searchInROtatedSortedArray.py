"""
	Search in Rotated Sorted Array

	Suppose a sorted array is rotated at some pivot unknown to you beforehand.

	(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

	You are given a target value to search. If found in the array return its index, otherwise return -1.

	You may assume no duplicate exists in the array

	https://leetcode.com/problems/search-in-rotated-sorted-array/

"""


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums)-1
        

        while l <= r:
        	m = (r + l)/2
        	if nums[m] == target:
        		return m

        	if nums[l] <= nums[m]:
        		if target >= nums[l] and target < nums[m]:
        			r = m - 1
        		else:
        			l = m + 1 

        	else:
        		if target > nums[m] and target <= nums[r]:
        			l = m + 1
        		else:
        			r = m - 1

        	

        return -1

sol = Solution()
nums= [4,5,6,7,1,2,3]
target = 2
print sol.search(nums,target)