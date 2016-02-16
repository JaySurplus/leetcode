"""
	121. Best Time to Buy and Sell Stock

	Say you have an array for which the ith element is the price of a given stock on day i.

	If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.
"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
        	return 0
        res = 0

        min_p_ind = 0
        max_p_ind = 0
        for i in xrange(1,len(prices)):
        	if prices[i] > prices[max_p_ind]:
        		max_p_ind = i
        	if prices[i] < prices[min_p_ind]:
        		if max_p_ind > min_p_ind:
        			res = max(res, prices[max_p_ind] - prices[min_p_ind])
        		max_p_ind = i
        		min_p_ind = i
        res = max(res, prices[max_p_ind] - prices[min_p_ind])
        return res


sol = Solution()
price = [9,3,4,5,6,3,7,8,9,2,3,2,44]
print sol.maxProfit(price)
