"""
    Build a Palindrome
    https://www.hackerrank.com/challenges/challenging-palindromes
"""

class Solution(object):
    def build_a_palindrome(self, s1, s2):

        m1 = {}
        m2 = {}

        for i in range(len(s1)):
            for j in range(i+1,len(s2)+1):
                m1[s1[i:j]] = 0
        for i in range(len(s2)):
            for j in range(i+1, len(s2)+1):
                m2[s2[i:j]] = 0

        l = len(s1)+len(s2)
        i = l
        res = ""
        while i > 1:
            shift = l - i
            left = len(s1)
            right = len(s2)

            














sol = Solution()
s1 = ""
s2 = ""
res = sol.build_a_palindrome(s1,s2)
print res
