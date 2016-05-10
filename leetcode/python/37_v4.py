from itertools import product
import time
class Solution(object):
    def solveSudoku(self, board):
        #for i in range(9):
        #    board[i] = [int(x) if x != '.' else 0 for x in board[i]]


        R,C=3,3
        N=R*C
        X=([("rc", rc) for rc in product(range(N), range(N))] +
             [("rn", rn) for rn in product(range(N), range(1, N + 1))] +
             [("cn", cn) for cn in product(range(N), range(1, N + 1))] +
             [("bn", bn) for bn in product(range(N), range(1, N + 1))])
        Y={}
        for r, c, n in product(range(N), range(N), range(1, N + 1)):
            b=(r // R) * R + (c // C) # Box number
            Y[(r, c, n)] = [
                ("rc", (r, c)),
                ("rn", (r, n)),
                ("cn", (c, n)),
                ("bn", (b, n))]
        X,Y=self.exact_cover(X,Y)
        for i,row in enumerate(board):
            for j,n in enumerate(row):
                if n:
                    self.select(X, Y, (i, j, n))
        for solution in self.solve(X, Y, []):
            for (r, c, n) in solution:
                board[r][c] = n
            yield board
        #for i in range(9):
        #   board[i] = [str(x) for x in board[i]]


        return


    def solve(self,X,Y,solution=[]):
        if not X:
            yield list(solution)
        else:
            c=min(X,key=lambda c: len(X[c]))
            for r in list(X[c]):
                solution.append(r)
                cols=self.select(X,Y,r)
                for s in self.solve(X,Y,solution):
                    yield s
                self.deselect(X,Y,r,cols)
                solution.pop()

    def select(self,X,Y,r):
        cols=[]
        for j in Y[r]:
            for  i in X[j]:
                for k in Y[i]:
                    if k!=j:
                        X[k].remove(i)
            cols.append(X.pop(j))
        return cols

    def deselect(self,X,Y,r,cols):
        for j in reversed(Y[r]):
            X[j]=cols.pop()
            for i in X[j]:
                for k in Y[i]:
                    if k!=j:
                        X[k].add(i)

    def T(self,Y):
        X={}
        for i,j in Y.items():
            for k in j:
                if k in X:
                    X[k].append(i)
                else:
                    X[k]=[i]
        return X

    def exact_cover(self,X,Y):
        X = {j:set() for j in X}
        for i,row in Y.items():
            for j in row:
                X[j].add(i)
        return X,Y

board = ["8........","..36.....",".7..9.2..",".5...7...","....457..","...1...3.","..1....68","..85...1.",".9....4.."]

sudoku = [list(row) for row in board]
for i in range(9):
    sudoku[i] = [int(x) if x != '.' else 0 for x in sudoku[i]]
#print sudoku

sol = Solution()
start = time.time()
sol.solveSudoku(sudoku)
end = time.time()
print end - start
#for  s in result:
##    for i in s:
 #       print i
print sudoku

