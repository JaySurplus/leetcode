"""
	64. Minimum Path Sum

	Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

	Note: You can only move either down or right at any point in time.

	Subscribe to see which companies asked this question
"""

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid) == 0:
        	return 0

        for i in range(1, len(grid[0])):
        	grid[0][i] = grid[0][i-1]+grid[0][i]

        
        for i in range(1, len(grid)):
        	
        	grid[i][0] = grid[i-1][0]+grid[i][0]

        for i in range(1, len(grid)):
        	for j in range(1,len(grid[0])):
        		grid[i][j] = min(grid[i-1][j] , grid[i][j-1]) + grid[i][j]
        return grid[-1][-1]

sol = Solution()
grid = [[1,2,5],[3,2,1]]
print sol.minPathSum(grid)