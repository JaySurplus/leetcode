"""
	69. Sqrt(x)

	Implement int sqrt(int x).

	Compute and return the square root of x.

	https://leetcode.com/problems/sqrtx/
"""

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
        	return None

        

        s = 0
        e = x
    	
        while s <= e:
        	m = (e + s)/2
        	if m**2 <= x and (m+1)**2 >x:
        		return m
        	else:
        		if m**2 < x:
        			s = m+1
        		else:
        			e = m -1
        return m
    def mySqrtNewton(self, x):
    	s = x

    	while s**2 > x:
    		s = 1.*(s+x/s)/2
    	return s

sol = Solution()
n = 23

print sol.mySqrtNewton(n)

import math
print math.sqrt(n)