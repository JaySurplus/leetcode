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
import collections
class Solution(object):
	def solve(self, board):
		"""
		:type board: List[List[str]]
		:rtype: void Do not return anything, modify board in-place instead.
		"""
		if len(board) < 3 or len(board[0]) < 3:
			return
		self.displacements = [[1, 0], [-1, 1], [-1, -1], [1, -1]]
		m , n = len(board) , len(board[0])

		# 1. Check elements on outer layer . If it is 'O' , do a BFS and mark all connect 'O' to any other symbol , such as 'V'.
		# 2. iterate all elements and mark all 'O' to 'X'
		# 3. iterate all elements and mark all 'V' to 'X'

		# or Use extra space.
		# 2. iterate all elements and mark all 'O' to 'X' and all 'V' to 'O' on new board.
		#

		#new_board = [['X' for i in xrange(n)] for j in xrange(m)]

		for i in [0 , m-1]:
		    for j in xrange(n):
		        if board[i][j] == 'O':
		            self.bfs(i, j ,board)
		            
		for i in xrange(1,m-1):
		    for j in [0, n-1]:
		        if board[i][j] == 'O':
		        	self.bfs(i, j , board)

		for i in xrange(m):
		    for j in xrange(n):
		    	if board[i][j] == 'O':
		    		board[i][j] = 'X' 
		    	elif board[i][j] == 'V':
		    	    board[i][j] = 'O'
	
        def bfs(self, i , j , board):
                stack = []
                #stack = collections.deque([[i,j]])
                stack.append((i,j))
                board[i][j] = 'V'
                while stack:
                        a , b = stack.pop(0)
                        
                        """
                        for di, dj in self.displacements:
                        	a += di
                        	b += dj
                        	if 0 <= a < len(board) and 0 <= b < len(board[0]) and board[a][b] == 'O':
                        		stack.append((a,b))
                        		board[a][b] = 'V'
                        """
                        
                        
                        if a > 0 and board[a-1][b] == 'O':
                                stack.append((a-1,b))
                                board[a-1][b] = 'V'
                        if a < len(board)-1 and board[a+1][b] == 'O':
                                stack.append((a+1,b))
                                board[a+1][b] = 'V'
                        if b > 0 and board[a][b-1] == 'O':
                                stack.append((a, b -1))
                                board[a][b-1] = 'V'
                        if b < len(board[0])-1 and board[a][b+1] == 'O':
                                stack.append((a, b+1))
                                board[a][b+1] = 'V'
                    

def p(board):
	for b in board:
		print b
board = [['X','X','X','X'], ['X','O','O','X'], ['X','X','X','X'], ['X','O','O','X']]
#board = [['X' , 'X' , 'X'],['X' , 'O' , 'X'],['X' , 'O' , 'X']]
p(board)


sol = Solution()
res = sol.solve(board)

#res[0][0] = 'V'
print
p(board)
