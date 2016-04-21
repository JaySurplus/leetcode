"""
	51. N-Queens

	The n-queens puzzle is the problem of placing n queens on an n*n chessboard such that no two queens attack each other.



	Given an integer n, return all distinct solutions to the n-queens puzzle.

	Each solution contains a distinct board configuration of the n-queens' placement, 
	where 'Q' and '.' both indicate a queen and an empty space respectively.
"""
import itertools

class Solution(object):
    def totalNQueens2(self, n):
        solutions = []
        for solution in itertools.permutations(range(n)):
            if len(set(x-y for x,y in enumerate(solution))) == \
               len(set(x+y for x,y in enumerate(solution))) == n:
                solutions.append(solution)
        return len(solutions)

    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        col = [True] * n
        pDig = [True] * 2 * n
        nDig = [True] * 2 * n

        self.res = 0
        self.dfs(0, n , col , pDig , nDig)
        return self.res

    def dfs(self, row , n , col , pDig , nDig):

        if row == n : 
            self.res += 1
            return

        else:
            for j in range(n):
                if col[j]  and pDig[row+j]  and nDig[row-j]:

                    col[j] = False
                    pDig[row+j] = False
                    nDig[row-j] = False

                    self.dfs(row+1, n , col ,pDig, nDig)

                    col[j] = True
                    pDig[row+j] = True
                    nDig[row-j] = True







   
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
import time
 
sol = Solution()

s1 = time.time()
for i in range(1):
    res = sol.totalNQueens(10)
e1 = time.time()


s2 = time.time()
for i in range(1):
    res = sol.totalNQueens2(8)
e2 = time.time()



print e1 - s1

print e2 - s2

print res
