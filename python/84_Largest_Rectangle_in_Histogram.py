"""
	84. Largest Rectangle in Histogram



	Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

	Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].

	The largest rectangle is shown in the shaded area, which has area = 10 unit.

	For example,
	Given heights = [2,1,5,6,2,3],
	return 10.

	https://leetcode.com/problems/largest-rectangle-in-histogram/
"""

class Solution(object):
    def largestRectangleAreaII(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        res = 0
        dp = [[0 for i in range(len(heights))] for i in range(len(heights))]
        #$print dp
        #dp[0][0] = heights[0]
        res = 0
        #m = dp[0][0]
        
        for i in range(len(heights)):
        	dp[i][i] = heights[i]
        	m = dp[i][i]
        	for j in range(i+1,len(heights)):
        		m = min(m,heights[j])
        		dp[i][j] = m * (j-i+1)
        		res = max(dp[i][j],res)
        print res

    def largestRectangleArea(self, height):
       	height.append(0)
       	stack = [-1]
       	res = 0
       	for i in xrange(len(height)):
       		while height[i] < height[stack[-1]]:
       			h = height[stack.pop()]
       			w = i - stack[-1] - 1
       			res = max(res, h*w)

       		stack.append(i)
       		
       	return res

sol = Solution()
heights = [2,1,5,6,2,3]
heights = [1,2,3,4,5,6,7,8,9,0]
heights = [2,1,2]
print sol.largestRectangleArea(heights)

