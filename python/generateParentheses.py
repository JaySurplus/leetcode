"""
	Generate Parentheses

	Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

	For example, given n = 3, a solution set is:

	"((()))", "(()())", "(())()", "()(())", "()()()"


	https://leetcode.com/problems/generate-parentheses/
"""

import time



class Solution(object):
    def generateParenthesis(self, n):
		"""
		:type n: int
		:rtype: List[str]
		"""
		if n == 0:
		    return []
		finalSol = []
        	
		self.parenthesisRecursive( n , n , '' , finalSol)
		return finalSol


    def parenthesisRecursive(self, l ,r ,  sol , finalSol ):
	    if r < l:
	        return
	    if l == 0 and r == 0:
	        finalSol.append(sol)
	    if l > 0:
	        self.parenthesisRecursive(l-1, r , sol+'(' , finalSol)
	    if r > 0:
	        self.parenthesisRecursive(l, r-1 , sol+')' , finalSol)


sol = Solution()
start = time.time()
test = sol.generateParenthesis(5)
end = time.time()

#print test
print 'running time is %f s' % (end -start)