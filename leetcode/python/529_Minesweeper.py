#!/usr/local/bin/python3
class Solution(object):
    def updateBoard(self, board, click):
        if not board or not board[0]:
            return board

        r, c = len(board), len(board[0])

        def helper(m, n):
            for i in range(-1,2):
                for j in range(-1, 2):
                    if (i or j) and m + i < r and m + i >= 0 and n + j < c and n + j >= 0:
                        yield m + i, n + j

        visited = {tuple(click)}
        stack = [click]

        while stack:
            c_i, c_j = stack.pop()
            if board[c_i][c_j] == 'M':
                board[c_i][c_j] = 'X'
            else:
                count = sum( board[ni][nj] in 'MX' for ni, nj in helper(c_i, c_j) )
                if count:
                    #board[c_i][c_j] = str(count)
                    board[c_i] = board[c_i][:c_j] + str(count) + board[c_i][c_j+1:]
                else:
                    board[c_i] = board[c_i][:c_j] + 'B' + board[c_i][c_j+1:]
                    for n in helper(c_i, c_j):
                        if board[n[0]][n[1]] in 'ME' and n not in visited:
                            stack.append(n)
                            visited.add(n)
        return board



    def updateBoardII(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        if not board or not board[0]:
            return board
        self.board = board
        self.m, self.n  = len(board), len(board[0])
        #i, j = click
        self.visited = {}
        self.dirs = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]

        self.helper(click)
        return board

    def helper(self, click):
        i, j = click
        if i < 0 or i >= self.m or j < 0 or j >= self.n:
            return
        if self.board[i][j] == 'B' or (self.board[i][j] >= '1' and self.board[i][j] <= '8'):
            return
        if self.board[i][j] == 'M':
            self.board[i] = self.board[i][:j] + 'X' + self.board[i][j+1:]
            return
        self.board[i] = self.board[i][:j] + 'B' + self.board[i][j+1:]
        stack = [(i,j)]
        while stack:
            i, j = stack.pop(0)
            if (i, j) in self.visited:
                continue
            temp = []
            count = 0
            for d in self.dirs:
                if i+d[0] < 0 or i+d[0] >= self.m or j+d[1] < 0 or j + d[1] >= self.n:
                    continue
                if self.board[i+d[0]][j+d[1]] == 'M':
                    count += 1

                if self.board[i+d[0]][j+d[1]] == 'E':
                    temp.append((i+d[0], j+d[1]))
            if count == 0:

                stack += temp
                self.board[i] = self.board[i][:j] + 'B' + self.board[i][j+1:]
            else:
                self.board[i] = self.board[i][:j] + [str(count)] + self.board[i][j+1:]

            self.visited[(i,j)] = 0
        return
sol = Solution()

board = ["EEEEE","EEMEE","EEEEE","EEEEE"]
click = [3,0]

board = ["EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE","EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE","EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE","EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE","EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE","EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE","EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE","EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE","EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE","EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE","EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE","EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE","EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE","EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE","EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE","EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE","EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE","EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE","EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE","EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE","EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE","EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE","EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE","EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE","EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE","EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE","EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE","EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE","EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE","EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE","EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE","EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE","EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE","EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE","EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE","EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE","EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE","EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE","EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE","EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE","EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE","EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE","EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE","EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE","EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE","EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE","EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE","EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE","EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE","EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE"]
click = [29,2]


print(sol.updateBoard(board, click))
print(["B1E1B","B1M1B","B111B","BBBBB"])

