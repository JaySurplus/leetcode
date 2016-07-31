class NumMatrix(object):

    def __init__(self, matrix):
        if matrix:
            self.dp = [[0] * (len(matrix[0]) + 1) for i in range(len(matrix)+1)]
            for i in xrange(1,len(matrix)+1):
                for j in xrange(1,len(matrix[0])+1):
                        self.dp[i][j] = self.dp[i-1][j] + self.dp[i][j-1] + matrix[i-1][j-1] - self.dp[i-1][j-1]



    def sumRegion(self, row1, col1, row2, col2):

        return self.dp[row2+1][col2+1] + self.dp[row1][col1] - self.dp[row1][col2+1] - self.dp[row2+1][col1]



# Your NumMatrix object will be instantiated and called as such:
matrix = [[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]
for m in matrix:
    print m
print
numMatrix = NumMatrix(matrix)
print numMatrix.sumRegion(2, 1, 4, 3)
print numMatrix.sumRegion(1, 2, 3, 4)
