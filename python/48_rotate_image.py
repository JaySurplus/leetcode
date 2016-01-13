"""
	48. Rotate Image

	You are given an n x n 2D matrix representing an image.

	Rotate the image by 90 degrees (clockwise).

	Follow up:
	Could you do this in-place?
"""

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) <= 1:
        	return
        else:
        	n = len(matrix)
        	for i in range(n/2):
       	
        		for j in range(i , n-i-1):
        			temp = matrix[j][n-1-i]
        			matrix[j][n-1-i] = matrix[i][j]

        			matrix[i][j] = matrix[n-1-j][i]
        			matrix[n-1-j][i] = matrix[n-1-i][n-1-j]
        			matrix[n-1-i][n-1-j] = temp
    def rotate2(self, matrix):
    	
        n = len(matrix)
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(n):
            matrix[i].reverse()
        return matrix

sol = Solution()
matrix = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
#matrix = [[1,2,3,4],[6,7,8,9],[11,12,13,14],[16,17,18,19]]

import time

start1 = time.time()
for i in range(10000):
	sol.rotate(matrix)
end1 = time.time()

start2 = time.time()
for i in range(10000):
	sol.rotate2(matrix)
end2 = time.time()

print end1-start1
print end2-start2
