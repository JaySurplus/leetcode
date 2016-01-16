"""
	63. Unique Paths II

	Follow up for "Unique Paths":

	Now consider if some obstacles are added to the grids. How many unique paths would there be?

	An obstacle and empty space is marked as 1 and 0 respectively in the grid.

	For example,
	There is one obstacle in the middle of a 3x3 grid as illustrated below.

	[
  	 [0,0,0],
  	 [0,1,0],
  	 [0,0,0]
	]
The total number of unique paths is 2.

"""
class Solution(object):
	""" Time exceeded.
    def uniquePathsWithObstacles(self, obstacleGrid):
        
        #:type obstacleGrid: List[List[int]]
        #:rtype: int
        
        self.res = 0
        self.oG = obstacleGrid
        self.m = len(obstacleGrid)
        if self.m == 0:
        	return 0

        self.n = len(obstacleGrid[0])
        self.dfs(0,0)
        print self.res

 
    def dfs(self, i , j ):
    	if i == self.m -1 and j == self.n-1:
    		self.res += 1
    		return
    	else:
    		if i + 1 < self.m and self.oG[i+1][j] != 1:
    			self.dfs(i+1,j)
    		if j + 1 < self.n and self.oG[i][j+1] != 1:
    			self.dfs(i,j+1)
    """
	def uniquePathsWithObstacles(self, obstacleGrid):
		self.m = len(obstacleGrid)
		self.n = len(obstacleGrid[0])
		self.o = obstacleGrid

		if self.o[0][0] == 1 or self.o[-1][-1] == 1:
			return 0

		
		self.o[0][0] = 1

		for i in range(1,self.n):
			self.o[0][i] = self.o[0][i-1]*(1-self.o[0][i])
		
		for i in range(1,self.m):
			self.o[i][0] = self.o[i-1][0]*(1-self.o[i][0])
		
		for i in range(1,self.m):
			for j in range(1,self.n):
				self.o[i][j] = (self.o[i-1][j] + self.o[i][j-1]) * (1-self.o[i][j])

		return self.o[-1][-1]

sol = Solution()
oG = [ [0,1,0],[0,1,0],[0,0,0]]
oG = [[0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],[0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0],[1,1,1,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,1,1,0,0,0,0,0,0,0,0,1,0,0,1],[0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0],[0,0,0,1,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,1,0],[1,0,1,1,1,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,1,0,0,0,1,0,1,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,0],[0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,1,0,0,0,0,0],[0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],[1,0,1,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,1,0,0,0,1,0,1,0,0,0,0,1],[0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0,0,1,1,0,0,0,0,0],[0,1,0,1,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,0,0,0,0,0],[0,1,0,0,0,0,0,0,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,1,0,1],[1,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,1,0,0,1,0,0,0,0,0,0],[0,0,1,0,0,0,0,0,0,0,1,0,0,1,0,0,1,0,0,0,0,0,0,1,1,0,1,0,0,0,0,1,1],[0,1,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,0,1,0,1],[1,1,1,0,1,0,0,0,0,1,0,0,0,0,0,0,1,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,1,1],[0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,1,0,0,0,1,0,0,0]]
oG = [[0,1,0],[0,0,1],[0,1,0]]
print sol.uniquePathsWithObstacles(oG)