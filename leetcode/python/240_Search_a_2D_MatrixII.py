"""
    240. Search a 2D Matrix II

    Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

    Integers in each row are sorted in ascending from left to right.
    Integers in each column are sorted in ascending from top to bottom.
    For example,

    Consider the following matrix:

    [
        [1,   4,  7, 11, 15],
        [2,   5,  8, 12, 19],
        [3,   6,  9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
    Given target = 5, return true.

    Given target = 20, return false.
"""


class Solution(object):

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row = 0
        col = len(matrix[0])-1

        while row < len(matrix) and col >= 0:
            if matrix[row][col] < target:
                row += 1
            elif matrix[row][col] > target:
                col -= 1
            else:
                return True
        return False

    def searchMatrixII(self, matrix, target):

        if not matrix or not matrix[0]:
            return False

        def binary_search(l,r,matrix, target):
            if l > r:
                return False

            mid = (l+r)/2
            if matrix[mid] == target:
                return True
            if target < matrix[mid] :
                return binary_search(l,mid-1,matrix, target)
            return binary_search(mid+1,r,matrix, target)

        def helper(t , b , matrix, target):
            if t > b:
                return False
            mid = (t+b)/2
            if matrix[mid][0]<= target and target <= matrix[mid][-1]:
                if binary_search(0,len(matrix[mid])-1,matrix[mid], target):
                    return True

            if helper(mid+1,b,matrix,target):
                return True
            if helper(t,mid-1,matrix,target):
                return True
            return False

        return helper(0,len(matrix)-1,matrix,target)



        return helper(0,len(matrix)-1,matrix,target)


    def searchMatrixIII(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False

        def helper(l,r,t,b, matrix ,traget):

            if l > r or t > b:
                return False

            r_mid = (t+b)/2
            c_mid = (l+r)/2

            if matrix[r_mid][c_mid] == target:
                return True

            if target < matrix[r_mid][c_mid]:
                return helper(l,c_mid-1,t,r_mid,matrix,target) or helper(l,c_mid-1, r_mid+1 ,b,matrix,target) or helper(c_mid,r,t,r_mid-1,matrix,target)

            if target > matrix[r_mid][c_mid]:
                return helper(l,c_mid,r_mid+1,b,matrix,target) or helper(c_mid+1,r,r_mid+1,b,matrix, target)  or  helper(c_mid+1,r,t,r_mid,matrix,target)

        return helper(0,len(matrix[0])-1,0,len(matrix)-1,matrix,target)











matrix = [
        [1,   4,  7, 11, 15],
        [2,   5,  8, 12, 19],
        [3,   6,  9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]

matrixII = [
        [1,2,3,4,5],
        [6,7,8,9,10],
        [11,12,13,14,15],
        [16,17,18,19,20],
        [21,22,23,24,25]
        ]



matrixIII = [[1,1]]
matrixVI = [[1,4],[2,5]]
sol = Solution()


print sol.searchMatrixII(matrixVI,2)



