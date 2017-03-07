"""
    498. Diagonal Traverse
    https://leetcode.com/problems/diagonal-traverse/?tab=Description
"""
class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype:  List[int]
        """
        if not matrix:
            return []
        res = []
        direction = [[-1,1],[1,-1]]
        n = 0
        i, j = 0, 0
        d = 0
        while n < len(matrix) * len(matrix[0]):

            res.append(matrix[i][j])

            n += 1
            i, j = i + direction[d][0], j+direction[d][1]

            if i == -1 or j == -1 or i == len(matrix) or j == len(matrix[0]):
                if i == -1:
                    if j == len(matrix[0]):
                        j -= 1
                        i +=2
                    else:
                        i += 1
                if j == -1:
                    if i == len(matrix):
                        i -= 1
                        j += 2
                    else:
                        j += 1
                if i == len(matrix):
                    i -= 1
                    j += 2
                if j == len(matrix[0]):
                    i += 2
                    j -= 1

                d = (d+1)%2


        return res

sol = Solution()
matrix = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
matrix = [[1,2,3],[4,5,6]]
print sol.findDiagonalOrder(matrix)


