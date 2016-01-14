"""
	54. Spiral Matrix

	Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

	For example,
	Given the following matrix:

	[
 		[ 1, 2, 3 ],
 		[ 4, 5, 6 ],
 		[ 7, 8, 9 ]
	]

	You should return [1,2,3,6,9,8,7,4,5].
"""

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0:
        	return matrix
        l = 0 
        r = len(matrix[0]) 
        up = 0
        down = len(matrix)
        res = []

        n = min(r , down)
   
        t = 0
        while t < n/2 :
        
        	res += matrix[up][l:r]

        	up+=1
        	
        	for i in range(up, down):
        		res.append(matrix[i][r-1])
        	r -=1

        	res += reversed(matrix[down-1][l:r])
        	down-=1

        	for i in range(down -1 , up -1 , -1):
        		res.append(matrix[i][l])
        	l+=1

        	t += 1
   
        if n % 2 == 1:
        	if len(matrix) == n:
        		res += matrix[up][l:r]
        	#elif len(matrix[0])  == n:
        	else:
        		for i in range(up, down):
        			res.append(matrix[i][l])
        return res
    """
	def spiralOrder(self, matrix):
        
        if len(matrix) == 0:
        	return matrix

        l = 0 
        r = len(matrix[0]) 
        up = 0
        down = len(matrix)
        res = []

        #n = min(r , down)
   
        #t = 0
        while l < r and up < down :
        
        	res += matrix[up][l:r]
        	up+=1
        	
        	for i in range(up, down):
        		res.append(matrix[i][r-1])
        	r -=1

        	if up < down:
        		res += reversed(matrix[down-1][l:r])
        		#for i in range(r -1 , l -1 , -1):
        		#	res.append(matrix[down-1][i])
        		down-=1
        	
        	if l < r:
        		for i in range(down -1  , up - 1, -1):
        			res.append(matrix[i][l])
        		l+=1

        	
        return res
    """



sol = Solution()

matrix = [ [ 1, 2, 3 ,4],[  5, 6 ,7,8]]#,[  9 ,10 ,11,12 ] ]#,[ 13,14,15,16] ]
matrix =[ [ 1, 2, 3 ,3],[ 4, 5, 6 ,3], [ 7, 8, 9 ,3], [ 7, 8, 9 ,3]]
#matrix = [[1,2,3],[4,5,6],[7,8,9]]
#matrix = [[2,3]]
#matrix = [[1,2],[2,3],[3,4]]
res = sol.spiralOrder(matrix)
print res
