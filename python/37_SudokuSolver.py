"""
    37. Sudoku Solver

    Write a program to solve a Sudoku puzzle by filling the empty cells.

    Empty cells are indicated by the character '.'.

    You may assume that there will be only one unique solution.

    https://leetcode.com/problems/sudoku-solver/
"""
from collections import defaultdict
class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        result = [False]
        self.update(board, result)
        
        
        
      
    def update(self, board,result):
        valid_num = set(["1","2","3","4","5","6","7","8","9"])
        row = defaultdict(set)
        col = defaultdict(set)
        squ = defaultdict(set)
        poss = []

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    row[i].add(board[i][j])
                    col[j].add(board[i][j])
                    squ[i/3*3+j/3].add(board[i][j])

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    poss.append( ( (i,j),valid_num - (row[i]|col[j]|squ[i/3*3+j/3])))
                    

        poss_list = [(key , list(val)) for key , val in poss]

        if  len(poss_list) == 0:
            result[0] = not result[0]
            return 
        else:
            poss_list.sort(key = lambda x:len(x[1]))
           
            if len(poss_list[0][1]) != 0:
                
                ind , vals = poss_list[0]
                i , j = ind

                for val in vals:
                    temp = board[i][j]
                    board[i][j] = val
                    self.update(board,result)
                    if result[0]:
                        return
                    board[i][j] = temp
                   

            else:
                return
                
                
        
        

    def test(self, board):
        board = [list(i) for i in board]
        valid_num = set(["1","2","3","4","5","6","7","8","9"])
        for i in range(9):
            if len(set(board[i])) != 9:
                return False

            col = [row[i] for row in board]
            if len(set(col)) != 9:
                return False

            block = [ row[i%3*3: i%3*3+3] for row in board[i/3*3 : i/3*3+3]]
            block = [ val for sublist in block for val in sublist]
            if len(set(block)) != 9:
                return False

        return True
        
        
        

        
        
sol = Solution()
board = [".........","..2......",".....271.",".........",".2.......",".5.......","....9...8",".....16..","....6...."]
board = ["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."]
board = ["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."]
board = [list(i) for i in board]

#board = [".87654321","2........",".........","4........","5........","6........","7........","8........","1........"]
#valid_num = set(['1','2','3','4','5','6','7','8','9'])
for i in board:
    print i
sol.solveSudoku(board)

#print sol.test(board)
#print poss
print 

for i in board:
    print i


