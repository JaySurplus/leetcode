"""
    361. Bomb Enemy

"""


class Solution(object):
    def maxKilledEnemies(self, grid):
        def hits(grid):
            return [[h
                     for block in ''.join(row).split('W')
                     for h in [block.count('E')] * len(block) + [0]]
                    for row in grid]

        rowhits = hits(grid)
        colhits = zip(*hits(zip(*grid)))
        print rowhits , colhits
        return max([rh + ch
                    for row in zip(grid, rowhits, colhits)
                    for cell, rh, ch in zip(*row)
                    if cell == '0'] or [0])

    def maxKilledEnemiesII(self, grid):
        """

        :type grid: List[List[str]]

        :rtype: int

        """

        if not grid or not grid[0]:

            return 0

        r = len(grid)

        c = len(grid[0])

        if r > c:
            m = r
            n = c
        else:
            m = c
            n = r

        rowHits = 0

        colHits = [0] * n

        res = 0

        for i in range(m):

            for j in range(n):

                if j == 0 or grid[i][j - 1] == 'W':

                    k = j

                    rowHits = 0

                    while k < c and grid[i][k] != 'W':

                        if grid[i][k] == 'E':

                            rowHits += 1

                        k += 1

                if i == 0 or grid[i - 1][j] == 'W':

                    k = i

                    colHits[j] = 0

                    while k < r and grid[k][j] != 'W':

                        if grid[k][j] == 'E':

                            colHits[j] += 1

                        k += 1

                if grid[i][j] == '0':

                    res = max(res, rowHits + colHits[j])

        return res


sol = Solution()
grid = ["EE0WEE0","E0EEEWE"]
res = sol.maxKilledEnemies(grid)
