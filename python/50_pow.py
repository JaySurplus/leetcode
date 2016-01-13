"""
	50.Pow(x, n)
"""

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
        	return 1./self.myPow(x,-n)

        elif n == 0:
        	return 1

        else:
        	res = self.myPow(x,n/2)
        	if n%2 == 0:
        		return res**2
        	else:
        		return res**2 * x


sol = Solution()
print sol.myPow(3,-2)