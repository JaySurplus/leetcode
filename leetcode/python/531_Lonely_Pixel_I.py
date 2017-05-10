class Solution(object):
    def findLonelyPixel(self, picture):
        """
        :type picture: List[List[str]]
        :rtype: int
        """
        res = 0
        row = [len([i for i in r if i == 'B']) for r in picture]
        for i in range(len(row)):
            if row[i] == 1:
                j = 0
                while j  < len(picture) and picture[i][j] != 'B':
                    j += 1
                t = 0
                r = 0
                while r < len(picture) and t < 2:
                    if picture[r][j] == 'B':
                        t += 1
                    r += 1
                if t == 1:
                    res += 1
        return res


sol = Solution()
picture = [['W', 'W', 'B'],
 ['W', 'B', 'W'],
 ['B', 'W', 'W']]


print sol.findLonelyPixel(picture)
