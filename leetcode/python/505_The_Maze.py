"""
    505. The Maze II
    https://leetcode.com/problems/the-maze-ii/?tab=Description
"""
import heapq

class Solution(object):
    def shortestDistance(self, maze, start, d):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int
        """

        if not maze:
            return -1

        start =  tuple(start)
        d = tuple(d)

        def getNext(m,n):
            res = []
            i,j = m,n
            #up
            step = 0
            while i > 0 and maze[i-1][j] == 0:
                step += 1
                i -= 1
            if step > 0:
                res.append((step, (i,j)))

            #down
            i,j = m,n
            step = 0
            while i < len(maze) - 1 and maze[i+1][j] == 0:
                step += 1
                i += 1
            if step > 0:
                res.append((step, (i,j)))

            #left
            i,j = m,n
            step = 0
            while j > 0 and maze[i][j-1] == 0:
                step += 1
                j -= 1
            if step > 0:
                res.append((step, (i,j)))

            #right
            i,j = m,n
            step = 0
            while j < len(maze[0]) - 1 and maze[i][j+1] == 0:
                step += 1
                j += 1
            if step > 0:
                res.append((step, (i,j)))

            return res

        queue = []
        heapq.heappush(queue,(0, start))
        visited = set([])
        res = []
        while queue:

            curr_step, curr_pos = heapq.heappop(queue)
            #if curr_pos not in visited:
            if True:
                if curr_pos == d:
                    return curr_step
                    #res.append((curr_pos,curr_step))
                visited.add(curr_pos)

                for nei_step, nei_pos in getNext(curr_pos[0],curr_pos[1]):
                    if nei_pos not in visited:
                        heapq.heappush(queue, (curr_step+nei_step, nei_pos))
        return -1

sol = Solution()
maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]
s = [0,4]
d = [4,4]
print sol.shortestDistance(maze,s,d)


