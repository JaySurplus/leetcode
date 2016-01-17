"""
	73. Set Matrix Zeroes

	Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.

	https://leetcode.com/problems/set-matrix-zeroes/
"""
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        row = [False for i in matrix]
        col = [False for i in matrix[0]]

        for i in range(len(matrix)):
        	for j in range(len(matrix[0])):
        		if matrix[i][j] == 0:
        			row[i] = True
        			col[j] = True

        for i in range(len(matrix)):
        	for j in range(len(matrix[0])):
        		if row[i] == True or col[j] == True:
        			matrix[i][j] = 0			




