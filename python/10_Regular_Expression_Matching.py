"""
	10. Regular Expression Matching 
	https://leetcode.com/problems/regular-expression-matching/


	'.' Matches any single character.
	'*' Matches zero or more of the preceding element.

	The matching should cover the entire input string (not partial).	

	The function prototype should be:
	bool isMatch(const char *s, const char *p)	

	Some examples:
	isMatch("aa","a") -> false
	isMatch("aa","aa") -> true
	isMatch("aaa","aa") -> false
	isMatch("aa", "a*") -> true
	isMatch("aa", ".*") -> true
	isMatch("ab", ".*") -> true
	isMatch("aab", "c*a*b") -> true

	https://leetcode.com/problems/regular-expression-matching/

"""
"""
class Solution:
    # @return a boolean
    def isMatch(self, s, p):
        dp=[[False for i in range(len(p)+1)] for j in range(len(s)+1)]
        print dp
        dp[0][0]=True
        for i in range(1,len(p)+1):
            if p[i-1]=='*':
                if i>=2:
                    dp[0][i]=dp[0][i-2]
        for i in range(1,len(s)+1):
            for j in range(1,len(p)+1):
                if p[j-1]=='.':
                    dp[i][j]=dp[i-1][j-1]
                elif p[j-1]=='*':
                    dp[i][j]=dp[i][j-1] or dp[i][j-2] or (dp[i-1][j] and (s[i-1]==p[j-2] or p[j-2]=='.'))
                else:
                    dp[i][j]=dp[i-1][j-1] and s[i-1]==p[j-1]
        return dp[len(s)][len(p)]
"""

test = Solution()
print test.isMatch('','a')
print test.isMatch('aa','a')
print test.isMatch('aa','aa')
print test.isMatch('aab', 'c*a*b')
print test.isMatch("aa", ".*")
print test.isMatch("ab", ".*")
print test.isMatch("a", "b")
print test.isMatch("ab", ".*c")

