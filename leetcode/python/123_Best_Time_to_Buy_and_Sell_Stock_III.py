"""
	123. Best Time to Buy and Sell Stock III

	Say you have an array for which the ith element is the price of a given stock on day i.

	Design an algorithm to find the maximum profit. You may complete at most two transactions.

	Note:
	You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
        	return 0
        l1 = [0 for i in range(len(prices))]
        l2 = [0 for i in range(len(prices))]

        minV = prices[0]
        
        for i in xrange(1,len(prices)):
        	minV = min(minV, prices[i])
        	l1[i] = max(l1[i] , prices[i] - minV)

        maxV = prices[-1]
        for i in xrange(len(prices)-2, -1, -1):
        	maxV = max(maxV, prices[i])
        	l2[i] = max(l2[i+1],maxV-prices[i])

        res = 0
        for i in xrange(len(prices)):
        	if l1[i] + l2[i] > res:
        		res = l1[i] + l2[i]
        return res

sol = Solution()
prices = [1,2,3,4,43,23,4,32,53,53,12,123]
print sol.maxProfit(prices)