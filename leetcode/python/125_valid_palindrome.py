"""
	125. Valid Palindrome
	Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

	For example,
	"A man, a plan, a canal: Panama" is a palindrome.
	"race a car" is not a palindrome.
	
	Note:
	Have you consider that the string might be empty? This is a good question to ask during an interview.
	
	For the purpose of this problem, we define empty string as valid palindrome.
"""
import re
class Solution(object):
	def isPalindrome(self, s):
		"""
		:type s: str
		:rtype: bool
		"""
		if len(s)==0:
			return True

		i = 0
		j = len(s)-1

		while i < j:

			while (not s[i].isalnum() ) and i < j:
				i += 1

			while (not s[j].isalnum() ) and i < j:
				j -= 1

			if i <= j:
				if s[i].lower() != s[j].lower():
					return False
				else:
					i += 1
					j -= 1



		return True


sol = Solution()
s = "A man, a plan, a canal: Panama"
#s = "race a car"
print sol.isPalindrome(s)