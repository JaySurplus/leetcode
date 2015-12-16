"""
	Trapping Rain Water
	
	Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

	For example, 
	Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.


	https://leetcode.com/submissions/detail/48204970/
"""


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        current_max = 0
        i = 0 
        j = len(height) - 1 
        result = 0

        while i <= j :
        	current_max = max(current_max , min(height[i] , height[j]))
        	if (height[i] <= height[j]):
        		result += current_max - height[i]
        		i += 1
        	else:
        		result += current_max - height[j]
        		j -= 1

        return result




test = Solution();
aList =  [0,1,0,2,1,0,1,3,2,1,2,1]
print test.trap(aList)