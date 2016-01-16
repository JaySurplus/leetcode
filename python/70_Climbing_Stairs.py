"""
	70. Climbing Stairs

	https://leetcode.com/problems/climbing-stairs/

	You are climbing a stair case. It takes n steps to reach to the top.

	Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        """
        dp = [0] * (n+1)
        dp[0] = 1
        if n == 0:
        	return dp[0]
        dp[1] = 1

        for i in range(2, n+1):
        	dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]
        """
        if n == 0 or n == 1:
        	return 1
        a = 1 
        b = 1
        for i in range(2,n+1):
        	res = a + b
        	a = b
        	b = res
        return res


    def climbStairsFib(self, n ):
    	import math

        """
        :type n: int
        :rtype: int
        """
        sqrt5 = math.sqrt(5)
        return int((((1+sqrt5)/2)**(n+1)-((1-sqrt5)/2)**(n+1))/sqrt5)

sol = Solution()
n = 7
print sol.climbStairs(n)