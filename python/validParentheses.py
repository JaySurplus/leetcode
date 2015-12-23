"""
	Valid Parentheses

	Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

	The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

	https://leetcode.com/problems/valid-parentheses/		

"""
class Solution(object):
	def __init__(self):
		self.parentheseOpen = ["(" , "[" , "{"]
		self.parentheseClose =  [")" , "]" , "}"]
		self.parentheses = {")" : "(" ,
							"}" : "{",
							"]" : "["}


	def isValid(self, s):
		

		ls = []

		for i in xrange(len(s)):
			if s[i] in self.parentheseOpen:
				ls.append(s[i])

			elif s[i] in self.parentheseClose:

				if len(ls) == 0:
					return False

				elif self.parentheses[s[i]] != ls.pop():
					return False

		
			
		return len(ls) == 0

sol = Solution()
test = sol.isValid("()()()")
print test
