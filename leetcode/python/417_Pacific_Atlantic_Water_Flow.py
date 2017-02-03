"""
    417. Pacific Atlantic Water Flow

Given an m * n matrix of non-negative integers representing the height of each unit cell in a continent, the "Pacific ocean" touches the left and top edges of the matrix and the "Atlantic ocean" touches the right and bottom edges.

Water can only flow in four directions (up, down, left, or right) from a cell to another one with height equal or lower.

Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.

Note:
The order of returned grid coordinates does not matter.
Both m and n are less than 150.
Example:

Given the following 5x5 matrix:

  Pacific ~   ~   ~   ~   ~
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * Atlantic

Return:

[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with parentheses in above matrix).
"""

class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix or not matrix[0]:
            return []
        self.m = len(matrix)
        self.n = len(matrix[0])
        self.matrix = matrix
        self.d = [(-1,0), (1,0), (0,-1), (0,1)]

        p = [[ False for _ in xrange(self.n)] for _ in xrange(self.m)]
        a = [[ False for _ in xrange(self.n)] for _ in xrange(self.m)]
        res = []

        for i in xrange(self.m):
            self.helper( i, 0, p)
            self.helper( i, self.n-1, a)

        for j in xrange(self.n):
            self.helper( 0, j, p)
            self.helper( self.m-1, j, a)

        for i in xrange(self.m):
            for j in xrange(self.n):
                if p[i][j] and a[i][j]:
                    res.append((i,j))
        return res

    def helper(self, i, j, v):
        v[i][j] = True
        for d in self.d:
            x , y= i + d[0], j + d[1]
            if x < 0 or y < 0 or x >= self.m or y >= self.n or self.matrix[x][y] < self.matrix[i][j] or v[x][y]:
                continue
            self.helper(x,y, v)
        return

"""
class SolutionII(object):
    def pacificAtlantic(self, matrix):
        if not matrix or not matrix[0]:
            return []

        self.m = len(matrix)
        self.n = len(matrix[0])
"""

sol = Solution()
matrix = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]

print(sol.pacificAtlantic(matrix))
