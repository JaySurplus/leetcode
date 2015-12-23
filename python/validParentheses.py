"""
	Valid Parentheses

	Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

	The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

	https://leetcode.com/problems/valid-parentheses/		

"""
class Solution(object):
	def isValid(self, s):
		parentheses = {")" : "(" ,
						"}" : "{",
						"]" : "["}
		
		parentheseOpen = ["(" , "[" , "{"]
		parentheseClose = [")" , "]" , "}"]

		ls = []

		for i in range(len(s)):
			if s[i] in parentheseOpen:
				ls.append(s[i])

			elif s[i] in parentheseClose:
				
				if len(ls) == 0:
					return False

				if parentheses[s[i]] != ls.pop():
					return False

		if len(ls) != 0:
			return False
		return True


