"""
    171. Excel Sheet Column Number
"""
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        for i in range(len(s)):
            res += (ord(s[i])-ord('A')+1) * 26**(len(s)-1-i)
        return res

sol = Solution()
s = "AFT"
print sol.titleToNumber(s)
