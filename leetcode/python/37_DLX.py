#! /usr/bin/env python
from itertools import product
import time
def solve(X,Y,solution=[]):
    if not X:
        yield list(solution)
    else:
        c=min(X,key=lambda c: len(X[c]))
        for r in list(X[c]):
            solution.append(r)
            cols=select(X,Y,r)
            for s in solve(X,Y,solution):
                yield s
            deselect(X,Y,r,cols)
            solution.pop()

def select(X,Y,r):
    cols=[]
    for j in Y[r]:
        for  i in X[j]:
            for k in Y[i]:
                if k!=j:
                    X[k].remove(i)
        cols.append(X.pop(j))
    return cols

def deselect(X,Y,r,cols):
    for j in reversed(Y[r]):
        X[j]=cols.pop()
        for i in X[j]:
            for k in Y[i]:
                if k!=j:
                    X[k].add(i)

def T(Y):
    X={}
    for i,j in Y.items():
        for k in j:
            if k in X:
                X[k].append(i)
            else:
                X[k]=[i]
    return X

def exact_cover(X,Y):
    X = {j:set() for j in X}
    for i,row in Y.items():
        for j in row:
            X[j].add(i)
    return X,Y

def solve_sudoku(size,grid):
    start = time.time()
    R,C=size
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
    X,Y=exact_cover(X,Y)
    for i,row in enumerate(grid):
        for j,n in enumerate(row):
            if n:
                select(X, Y, (i, j, n))
    for solution in solve(X, Y, []):
        for (r, c, n) in solution:
            grid[r][c] = n
        yield grid


if __name__=='__main__':
    board = ["8........","..36.....",".7..9.2..",".5...7...","....457..","...1...3.","..1....68","..85...1.",".9....4.."]

    sudoku = [list(row) for row in board]
    for i in range(9):
        sudoku[i] = [int(x) if x != '.' else 0 for x in sudoku[i]]    
    print sudoku

    start = time.time()
    result = solve_sudoku((3,3),sudoku)
    end = time.time()
    print (end - start)*1000
    for  s in result:
        for i in s:
            print i