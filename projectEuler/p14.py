"""
    project Euler 14: Longest Collatz Sequence
"""

class Solution(object):
    def longestCollatzSequence(self, n):
        if n == 0:
            return 0

        self.dp = [0]
        m = 0
        for i in range(1,n+1):
            self.dp[i] = self.helper(i)
            if self.dp[i] > self.dp[m]


