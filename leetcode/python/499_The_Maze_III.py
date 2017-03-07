"""
    499. The Maze III
    https://leetcode.com/problems/the-maze-iii/?tab=Description
"""
import heapq
class Solution(object):
    def findShortestWay(self,maze,ball,hole):
        """
        :type maze: List[List[int]]
        :type ball: List[int]
        :type hole: List[int]
        :rtype: str
        """
        if not maze:
            return "impossible"

        start = tuple(ball)
        end = tuple(hole)
        res = ""

        def getNext(m,n,end):
            res = []
            i,j = m,n
            #up
            step = 0
            while i > 0 and maze[i-1][j] == 0 and (end[0] != i or end[1] != j):
                step += 1
                i -= 1
            if step > 0:
                res.append((step, (i,j), "u"))

            #down
            i,j = m,n
            step = 0
            while i < len(maze) - 1 and maze[i+1][j] == 0 and (end[0] != i or end[1] != j):
                step += 1
                i += 1
            if step > 0:
                res.append((step, (i,j), "d"))

            #left
            i,j = m,n
            step = 0
            while j > 0 and maze[i][j-1] == 0 and (end[0] != i or end[1] != j):
                step += 1
                j -= 1
            if step > 0:
                res.append((step, (i,j), "l"))

            #right
            i,j = m,n
            step = 0
            while j < len(maze[0]) - 1 and maze[i][j+1] == 0 and (end[0] != i or end[1] != j):
                step += 1
                j += 1
            if step > 0:
                res.append((step, (i,j), "r"))

            return res

        queue = []
        heapq.heappush(queue,(0, start,''))
        res = []
        visited = set([])

        while queue:
            curr_step, curr_pos, d = heapq.heappop(queue)
            #if curr_pos not in visited:

            if curr_pos == end:
                if res and curr_step > res[-1][0]:
                    break
                res.append((curr_step,d))

            visited.add(curr_pos)
            for next_step, next_pos, next_d in getNext(curr_pos[0],curr_pos[1],end):
                if next_pos not in visited:
                    heapq.heappush(queue, (curr_step+next_step, next_pos, d+next_d))
        if not res:
            return "impossible"
        res.sort(key = lambda x:x[1])
        return res[0][1]

sol = Solution()
maze =[[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]
ball = [0,4]
hole = [0,1]
print sol.findShortestWay(maze, ball, hole)
