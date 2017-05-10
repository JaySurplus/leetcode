"""
    516. Longest Palindromic Subsequence
    https://leetcode.com/problems/longest-palindromic-subsequence/?tab=Solutions
"""
class Solution(object):
    def longestPalindromeSubseqII(self, s):
        """
        :type s: str
        :rtype: int
        """
        cache = {}
        def helper(s):
            if s not in cache:
                maxL = 0
                for c in set(s):
                    i, j = s.find(c), s.rfind(c)
                    maxL = max(maxL, 1 if i == j else 2 + helper(s[i+1:j]))
                cache[s] = maxL
            return cache[s]
        return helper(s)


    def longestPalindromeSubseq(self, s):
        dp = [1] * len(s)
        res = 0
        for i in range(1,len(s)):
            pre = dp[i]
            for j in range(i-1,-1,-1):
                tmp = dp[j]
                if s[i] == s[j]:
                    dp[j] = 2 + pre if i - j >= 2 else 2
                else:
                    dp[j] = max(dp[j+1],dp[j])
                pre = tmp
        return dp[0]

sol = Solution()
s = "abbc"
print sol.longestPalindromeSubseq(s)
