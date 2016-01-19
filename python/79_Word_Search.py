"""
	79. Word Search

	Given a 2D board and a word, find if the word exists in the grid.

	The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

	For example,
	Given board =

	[
	  ['A','B','C','E'],
	  ['S','F','C','S'],
	  ['A','D','E','E']
	]
	word = "ABCCED", -> returns true,
	word = "SEE", -> returns true,
	word = "ABCB", -> returns false.

	https://leetcode.com/problems/word-search/
"""

class Solution(object):
    def exist(self, board, word):
    	if not word:
    		return True
    	if not board:
    		return False
    	checker = [0 for i in range(len(board)*len(board[0]))] 
    	k = 0
    	for i in range(len(board)):
    		for j in range(len(board[0])):
    			if self.exist_helper(board, word, checker , i, j , k):
    				return True
    	return False

    def exist_helper(self, board, word,checker , i, j , k):
    	
    	if board[i][j] == word[k] :
    		if k == len(word)-1:
    			return True
    		board[i][j] = " " 
    		
    		if i > 0 and self.exist_helper(board, word, checker,i-1, j , k+1):
    			return True
    		if i < len(board)-1 and self.exist_helper(board,word ,checker, i+1, j,k+1):
    			return True
    		if j > 0 and self.exist_helper(board, word,checker ,i, j-1,k+1):
    			return True
    		if j < len(board[0])-1 and self.exist_helper(board, word, checker,i, j+1,k+1):
    			return True
    		#board[i][j] = word[0] # update the cell to its original value
    		board[i][j] = " " 
    		return False
    	else:
    		return False
    
sol = Solution()
word = "ABCCED"
word = "SEE"
#word = "ABCB"
board = [['A','B','C','E'],['S','F','C','S'],['A','D','E','E']]
board = ["b","a","b"]
word = "bbabab"
print sol.exist(board, word)
