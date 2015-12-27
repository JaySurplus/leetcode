"""
	Search For a Range

	Given a sorted array of integers, find the starting and ending position of a given target value.

	Your algorithm's runtime complexity must be in the order of O(log n).

	If the target is not found in the array, return [-1, -1].

	For example,
	Given [5, 7, 7, 8, 8, 10] and target value 8,
	return [3, 4].

	https://leetcode.com/problems/search-for-a-range/
"""

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = 0
        r = len(nums)-1

        while l <= r:
        	m = (l + r)/2

        	if nums[m] < target:
        		l = m + 1
        	elif nums[m] > target:
        		r = m - 1
        	else:     ### List must contain target.

        		## Find left bound
        		ll = 0
        		lr = m - 1
        		while ll <= lr:
        			lm = (ll + lr)/2
        			if nums[lm] == target:
        				lr = lm - 1
        			else:
        				ll = lm + 1
        		if nums[lm] == target:
        			l = lm
        		else:
        			l = lm+1
        		


        		rl = m + 1
        		rr = len(nums)-1
        		while rl <= rr:
        			rm = (rl+rr)/2
        			if nums[rm] == target:
        				rl = rm + 1
        			else:
        				rr = rm - 1
        		if nums[rm] == target:
        			r = rm
        		else:
        			r = rm - 1
        		return [l , r]
        		

        return [-1,-1]




sol = Solution()
nums = [5,7,7,8,8,10]
nums = [8,8,8,8,8,8,8,8]
target = 8
print sol.searchRange(nums, target)




