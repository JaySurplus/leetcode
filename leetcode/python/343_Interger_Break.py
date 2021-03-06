"""
    343. Integer Break
"""

class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0
        if n == 2:
            return 1
        if n == 3:
            return 2
        if n % 3 == 0:
            return 3 ** (n/3)
        if n % 3 == 1:
            return 4 * 3 ** ((n-4)/3)
        return 2 * 3 ** ((n-2)/3)


