"""
	51. N-Queens

	The n-queens puzzle is the problem of placing n queens on an n*n chessboard such that no two queens attack each other.



	Given an integer n, return all distinct solutions to the n-queens puzzle.

	Each solution contains a distinct board configuration of the n-queens' placement, 
	where 'Q' and '.' both indicate a queen and an empty space respectively.
"""

class Solution(object):
  def solveNQueens(self, n):
    """
    :type n: int
    :rtype: List[List[str]]
    """
    col = [0] * n
    # for diagonal \
    plusDig = [0] * (2*n)
    # for diagonal /
    minusDig = [0] * (2*n)
    board = [x[:] for x in [['.']*n]*n]
    self.res = []

    self.DFS(board, 0, n, col, plusDig, minusDig)

    return self.res



  def DFS(self, board, rowIndex, totalNum, col, plusDig, minusDig,):
    if rowIndex == totalNum:
        self.res.append([''.join(item) for item in board])
        return

    for j in range(totalNum):
        if  col[j]==0 and plusDig[rowIndex+j] ==0 and minusDig[rowIndex-j]==0:
            board[rowIndex][j] = 'Q'

            col[j]= 1
            plusDig[rowIndex+j] = 1
            minusDig[rowIndex-j] = 1

            self.DFS(board, rowIndex+1,totalNum, col,plusDig,minusDig)

            col[j]= 0
            plusDig[rowIndex+j] = 0
            minusDig[rowIndex-j] = 0

            board[rowIndex][j] = '.'




   
    """
  	def solveNQueens(self, n):
        def check(k, j):  # check if the kth queen can be put in column j!
            for i in range(k):
                if board[i]==j or abs(k-i)==abs(board[i]-j):
                    return False
            return True
        def dfs(depth, valuelist):
            if depth==n: res.append(valuelist); return
            for i in range(n):
                if check(depth,i): 
                    board[depth]=i
                    s='.'*n
                    dfs(depth+1, valuelist+[s[:i]+'Q'+s[i+1:]])
        board=[-1 for i in range(n)]
        res=[]
        dfs(0,[])
        return res
    """

 
sol = Solution()
res = sol.solveNQueens(10)
print len(res)
