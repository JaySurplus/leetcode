"""
    172. Factorial Trailing Zeroes
"""


class Solution(object):

    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 5:
            return 0
        res = 0
        base = 5
        while base <= n:
            res += n / (base)
            base *= 5
        return res

    def trailingZeroesII(self, n):
        """
        :type n: int
        :rtype: int
        """
        n /= 5
        res = 0
        while n:
            res += n
            n /= 5
        return res
sol = Solution()
n = [12, 32, 234, 1234,21321412,412421345,43147420146428462427481290424125123542421412521]
for i in n:
    print sol.trailingZeroesII(i)
