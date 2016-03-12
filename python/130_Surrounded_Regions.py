"""
	130. Surrounded Regions

	Given a 2D board containing 'X' and 'O', capture all regions surrounded by 'X'.

	A region is captured by flipping all 'O's into 'X's in that surrounded region.

	For example,
		X X X X
		X O O X
		X X O X
		X O X X

	After running your function, the board should be:

		X X X X
		X X X X
		X X X X
		X O X X

	https://leetcode.com/problems/surrounded-regions/
"""
class Solution(object):
	def solve(self, board):
		"""
		:type board: List[List[str]]
		:rtype: void Do not return anything, modify board in-place instead.
		"""
		m , n = len(board) , len(board[0])

		# 1. Check elements on outer layer . If it is 'O' , do a BFS and mark all connect 'O' to any other symbol , such as 'V'.
		# 2. iterate all elements and mark all 'O' to 'X'
		# 3. iterate all elements and mark all 'V' to 'X'

		# or Use extra space.
		# 2. iterate all elements and mark all 'O' to 'X' and all 'V' to 'O' on new board.
		#

		new_board = [['X' for i in xrange(n)] for j in xrange(m)]

		for i in [0 , m-1]:
                        for j in xrange(n):
                                if board[i][j] == 'O':
                                        self.dfs(i , j , board)

                for i in xrange(1,m-1):
                        for j in [0, n-1]:
                                if board[i][j] == 'O':
                                        self.dfs(i , j , board)

                for i in xrange(m):
                        for j in xrange(n):
                               # if board[i][j] == 'O':
                               #         new_board[i][j] = 'X'
                                if board[i][j] == 'V':
                                        new_board[i][j] = 'O'
                return new_board

        def dfs(self, i , j , board):
                if board[i][j] == 'O':
                        board[i][j] = 'V'

                        if i > 0 and board[i-1][j] == 'O':
                                self.dfs(i-1, j , board)
                        if i < len(board)-1 and board[i+1][j] == 'O':
                                self.dfs(i+1, j , board)
                        if j > 0 and board[i][j-1] == 'O':
                                self.dfs(i, j-1 , board)
                        if j < len(board[0])-1 and board[i][j+1] == 'O':
                                self.dfs(i, j+1 , board)

                return

def p(board):
	for b in board:
		print b
board = [['X','X','X','X'], ['X','O','O','X'], ['X','X','X','X'], ['X','O','O','X']]
board = [['X' , 'X' , 'X'],['X' , 'O' , 'X'],['X' , 'O' , 'X']]
p(board)


sol = Solution()
res = sol.solve(board)

#res[0][0] = 'V'
print
p(res)
