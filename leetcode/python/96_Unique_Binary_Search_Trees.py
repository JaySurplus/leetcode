"""
	96. Unique Binary Search Trees
"""

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 0:
        	return 0
        if n <=1:
        	return 1
        dp = [1,1]

        for i in range(2,n+1):
        	dp.append(0)
        	for j in range(0,i):
        		dp[i] += dp[j]*dp[i-j-1]
        return dp[-1]

sol = Solution()
n = 4
print sol.numTrees(n)