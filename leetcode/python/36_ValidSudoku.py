"""
	Valid Sudoku
	Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

	The Sudoku board could be partially filled, where empty cells are filled with the character '.'.


	https://leetcode.com/problems/valid-sudoku/
"""

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
        	for j in range(9):
        		if board[i][j] != '.':
        			#if int(board[i][j]) > 9 or int(board[i][j]) < 1:
        			#	return False
        			key = board[i][j]
        			for m in range(j+1,9):
        				if board[i][m] == key:
        					return False
        			for n in range(i+1,9):
        				if board[n][j] == key:
        					return False

        			if i % 3 < 2:
        				for m in range(i+1, (i/3+1)*3):
        					for n in range(j/3 * 3,(j/3+1)*3):
        						if n != j:
        							if board[m][n] == key:
        								return False
        				
        					
        return True

sol = Solution()
board = [".87654321","2........","3........","4........","5........","6........","7........","8........","9........"]
#board = ["....5..1.",".4.3.....",".....3..1","8......2.","..2.7....",".15......",".....2...",".2.9.....","..4......"]
#board = ["..5......","...8...3.",".5..2....",".........","........9","......4..","........7",".1.......","24....9.."]
#board = [".........","..2......",".....271.",".........",".2.......",".5.......","....9...8",".....16..","....6...."]
for i in board:
	print i
print sol.isValidSudoku(board)