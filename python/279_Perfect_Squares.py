"""
	279. Perfect Squares

	Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

	For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.
"""
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1:
            return 0
        s_l = map(lambda x:x**2 , range(1,int(n**0.5)))
        print s_l

        def k_sum(k,s):
        	pass

        
sol = Solution()
sol.numSquares(100)