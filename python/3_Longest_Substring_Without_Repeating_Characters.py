"""
	3. Longest Substring Without Repeating Characters

	Given a string, find the length of the longest substring without repeating characters.

	Examples:

	Given "abcabcbb", the answer is "abc", which the length is 3.

	Given "bbbbb", the answer is "b", with the length of 1.

	Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


class Solution(object):

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        start = 0
        dic = {}
        res = 0
        for i in xrange(len(s)):
            if s[i] in dic:
                start = dic[s[i]]+1 if dic[s[i]] >= start else start
            dic[s[i]] = i
            res = res if res >= i - start + 1 else i - start + 1
        return res

sol = Solution()
s = "abcabcbb"
s = "pwwkew"
print sol.lengthOfLongestSubstring(s)
