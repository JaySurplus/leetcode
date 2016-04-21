"""
	Problem statement
		Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

		Note: You may not slant the container.

		Subscribe to see which companies asked this question

		
	https://leetcode.com/problems/container-with-most-water/
"""

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        result = 0

        while left < right:
			rh = height[right]
			lh = height[left]
			result = max(result , min(rh, lh) * (right - left) )
			if lh <= rh:
				left += 1
			else:
				right -= 1
		return result
