"""
	74. Search a 2D Matrix

	https://leetcode.com/problems/search-a-2d-matrix/

	Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

	Integers in each row are sorted from left to right.
	The first integer of each row is greater than the last integer of the previous row.
	For example,

	Consider the following matrix:

	[	
  		[1,   3,  5,  7],
  		[10, 11, 16, 20],
  		[23, 30, 34, 50]
	]
	Given target = 3, return true.
"""

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """


        s = 0
        e = len(matrix) - 1

        if target >= matrix[-1][0]:
        	m = len(matrix) - 1
        elif target <= matrix[0][-1]:
        	m = 0

        else:
        	while s <= e  :
        		m = (s+e) /2 
        		#print s , e , m , target
        		if target >= matrix[m][0] and target < matrix[m+1][0]:
        			#print matrix[m][0] , target , matrix[m+1][0]
        			break
        		else:
        			if target < matrix[m][0]:
        				e = m - 1
        			else:
        				s = m + 1 
      
        s = 0
        e = len(matrix[m]) - 1
        while s <= e:

        	n = (s+e)/2
        
        	if target == matrix[m][n]:
        		return True
        	else:
        		if target < matrix[m][n]:
        			e = n - 1
        		else:
        			s = n + 1
        return False

    def searchMatrixII(self, matrix, target):
    	l = 0
    	r = len(matrix) * len(matrix[0]) - 1

    	while l <= r:
    		m = (l + r)/2
    		if target == matrix[m/len(matrix[0])][m%len(matrix[0])]:
    			return True
    		else:
    			if target < matrix[m/len(matrix[0])][m%len(matrix[0])]:
    				r = m - 1
    			else:
    				l = m + 1
    	return False

 
sol = Solution()
matrix = [	[1,   3,  5,  7],[10, 11, 16, 20],[23, 30, 34, 50],[53, 60, 64, 70]]
matrix =[[-10,-10],[-9,-9],[-8,-6],[-4,-2],[0,1],[3,3],[5,5],[6,8]]
#matrix = [1]
print sol.searchMatrixII(matrix,-9)
        