"""
	139. Word Break

	Given a string s and a dictionary of words dict, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

	For example, given
	s = "leetcode",
	dict = ["leet", "code"].

	Return true because "leetcode" can be segmented as "leet code".

	Subscribe to see which companies asked this question

	https://leetcode.com/problems/word-break/
"""
class Solution(object):
	def wordBreak(self, s, wordDict):
		"""
		:type s: str
		:type wordDict: Set[str]
		:rtype: bool
		"""
		dp = [False] * (len(s) + 1)
		dp[0] = True
		for i in range(1,len(s)+1):
			for j in range(i):
				if dp[j] and s[j:i] in wordDict:
					dp[i] = True
					break
		return dp[len(s)]

s = "leetcode"
dict = ["leet" , "code"]

sol = Solution()
print sol.wordBreak(s,dict)