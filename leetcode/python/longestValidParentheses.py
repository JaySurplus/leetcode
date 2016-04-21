"""
	Longest Valid Parentheses

	Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

	For "(()", the longest valid parentheses substring is "()", which has length = 2.

	Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.

	https://leetcode.com/problems/longest-valid-parentheses/



"""

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        m = 0
        last = -1
        stack = []
        """        
        for i in range(len(s)):
        	if stack and s[i] == ')' and s[stack[-1]]=='(':
        		stack.pop() 
        	else:
        		if stack :
        			if i - stack[-1] - 1 > m:
        				m = i - stack[-1] - 1
        		else:
        			m = i 
        		stack.append(i)
        

       	if len(stack) == 0:
       		return len(s)

      
        if len(s) - stack[-1] - 1 > m:
        	m = len(s) - stack[-1]-1
        return m
        """
        for i in range(len(s)):
        	if s[i] == '(':
        		stack.append(i)
        	else:
        		if stack == []:
        			last = i
        		else:
        			stack.pop()
        			if stack == []:
        				m = max(m , i - last)
        			else:
        				m = max(m , i - stack[-1])
        return m
sol = Solution()
s = "()(()))"
print sol.longestValidParentheses(s)

		