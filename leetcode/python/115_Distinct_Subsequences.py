"""
	115. Distinct Subsequences

	Given a string S and a string T, count the number of distinct subsequences of T in S.

	A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

	Here is an example:
	S = "rabbbit", T = "rabbit"

	Return 3.


"""

class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        if len(s) < len(t):
        	return 0
        if len(s) == len(t):
        	if s == t:
        		return 1
        	return 0

        res = [0 for i in range(len(s))]
        res[0] = 1 if s[1:] == t else 0
        for i in xrange(1,len(s)):
        	res[i] =  1 if res[i-1] or s[:i]+s[i+1:] == t else 0
        print res
        return sum(res)

sol = Solution()
print sol.numDistinct('rababait','rabbit')