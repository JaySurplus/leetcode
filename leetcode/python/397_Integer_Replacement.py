"""
    397. Integer Replacement

    Given a positive integer n and you can do operations as follow:

        If n is even, replace n with n/2.
        If n is odd, you can replace n with either n + 1 or n - 1.
        What is the minimum number of replacements needed for n to become 1?

    Example 1:

        Input:
        8

        Output:
        3

        Explanation:
        8 -> 4 -> 2 -> 1
    Example 2:

        Input:
        7

        Output:
        4

    Explanation:
    7 -> 8 -> 4 -> 2 -> 1
    or
    7 -> 6 -> 3 -> 2 -> 1
"""
class Solution(object):
    def __init__(self):
        self.dic = {1:0}

    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1:
            return -1
        if n in self.dic:
            return self.dic[n]
        if n % 2 == 0:
            res = 1 + self.integerReplacement(n/2)
        else:
            res = 1 + min(self.integerReplacement(n+1), self.integerReplacement(n-1))
        self.dic[n] = res
        return res

if __name__ == '__main__':
    sol = Solution()

    for n in range(1,100):
        print "Test 1 n = %d , result = %d" % (n, sol.integerReplacement(n))

