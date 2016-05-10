"""
    174. Dungeon Game

    https://leetcode.com/problems/dungeon-game/


    The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of M x N rooms laid out in a 2D grid. Our valiant knight (K) was initially positioned in the top-left room and must fight his way through the dungeon to rescue the princess.

    The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.

    Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering these rooms; other rooms are either empty (0's) or contain magic orbs that increase the knight's health (positive integers).

    In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.

    Notes:

        The knight's health has no upper bound.
        Any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where the princess is imprisoned.
"""


class Solution(object):

    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        min_life = 1

        col_range = len(dungeon[0])
        row_range = len(dungeon)

        i = 0
        j = 0

        dp = [[0 for i in range(col_range)] for j in range(row_range)]
        dp[row_range - 1][col_range - 1] = 1
        for j in range(row_range - 2, -1, -1):
            dp[j][-1] = dp[j + 1][-1] - dungeon[j + 1][-1] if dp[j +
                                                                 1][-1] - dungeon[j + 1][-1] > 0 else 1

        for i in range(col_range - 2, -1, -1):
            dp[-1][i] = dp[-1][i + 1] - dungeon[-1][i +
                                                    1] if dp[-1][i + 1] - dungeon[-1][i + 1] > 0 else 1

        for j in range(row_range - 2, -1, -1):
            for i in range(col_range - 2, -1, -1):
                down_val = dp[j + 1][i] - dungeon[j +
                                                  1][i] if dp[j + 1][i] - dungeon[j + 1][i] > 0 else 1
                right_val = dp[j][i + 1] - dungeon[j][i +
                                                      1] if dp[j][i + 1] - dungeon[j][i + 1] > 0 else 1

                dp[j][i] = min(down_val, right_val)
                # print down_val , right_val  , dp[i]
                pass
        res = dp[0][0] - dungeon[0][0] if dp[0][0] - dungeon[0][0] > 0 else 1
        print res
        return dp

    def calculateMinimumHPIII(self, d):

        col_range = len(d[0])
        row_range = len(d)

        dp = [0 for i in range(col_range)]


        dp[-1] = 1 if d[-1][-1] >= 0 else 1 - d[-1][-1]

        for j in range(col_range-2,-1,-1):
            dp[j] = 1 if dp[j+1] - d[-1][j] <= 0 else dp[j+1] - d[-1][j]

        for j in range(row_range - 2, -1, -1):
            dp[-1] = 1 if dp[-1] - d[j][-1] <= 0 else dp[-1] - d[j][-1]
            for i in range(col_range - 2, - 1, -1):
                MIN = min(dp[i], dp[i + 1])
                dp[i] = 1 if MIN - d[j][i] <= 0 else MIN - d[j][i]
        return dp[0]

    def calculateMinimumHPII(self, d):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        m, n = len(d), len(d[0])
        dp = []
        dp.append(1 if d[m - 1][n - 1] >= 0 else -d[m - 1][n - 1] + 1)
        for i in range(n - 2, -1, -1):
            dp.append(1 if d[m - 1][i] >= dp[-1] else dp[-1] - d[m - 1][i])
        dp = dp[::-1]

        for i in range(m - 2, -1, -1):
            dp[n - 1] = 1 if d[i][n - 1] >= dp[n - 1] else dp[n - 1] - d[i][n - 1]
            for j in range(n - 2, -1, -1):
                MIN = min(dp[j], dp[j + 1])
                dp[j] = 1 if d[i][j] >= MIN else MIN - d[i][j]

        return dp[0]


sol = Solution()
dungeon = [[-2, -3, 3, 6],
           [-5, -10, 1, -10],
           [10, 30, -5, 1]]
#dungeon = [[0,0,0],[-1,1,-1]]
#dungeon = [[3,-20,30],[-3,4,0]]
#dungeon = [[1,-3,3],[0,-2,1],[-3,-3,-3]]
dungeon = [[1, -3, 3], [0, -2, 0], [-3, -3, -3]]
for i in dungeon:
    print i
res = sol.calculateMinimumHPIII(dungeon)
print res
print sol.calculateMinimumHPII(dungeon)
print
# for i in res:
#    print i
