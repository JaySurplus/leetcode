"""
	59. Spiral Matrix II

	Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

	For example	,
	Given n = 3,

	You should return the following matrix:
"""

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = [[ 0 for i in range(n)] for j in range(n)]
        l = 0
        r = n 
        u = 0
        b = n

        v = 1

        while l < r and u < b:
        	for i in range(l , r):
        		res[u][i] = v
        		v += 1
        	u += 1

        	for i in range(u, b):
        		res[i][r-1] = v
        		v += 1 
        	r -= 1

        	for i in range(r -1 , l -1 , -1):
        		res[b-1][i] = v
        		v += 1
        	b -= 1

        	for i in range(b -1 , u - 1 , -1):
        		res[i][l] = v
        		v+= 1
        	l += 1
        return res
        

sol = Solution()
n = 0
res = sol.generateMatrix(n)
print res