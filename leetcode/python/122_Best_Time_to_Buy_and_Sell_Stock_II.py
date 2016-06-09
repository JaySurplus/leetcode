"""
	122. Best Time to Buy and Sell Stock II

	Say you have an array for which the ith element is the price of a given stock on day i.

	Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
"""
class Solution(object):
    def maxProfitII(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
        	return 0

       	min_p_ind = 0


       	res = 0
       	for i in range(1,len(prices)):

       		if prices[i] < prices[i-1]:
       			if prices[i-1] > prices[min_p_ind]:
       				res += prices[i-1] - prices[min_p_ind]
       				min_p_ind = i
       		if prices[i] > prices[i-1] :
       			if prices[i-1] < prices[min_p_ind]:
       				min_p_ind = i-1

       	if prices[i] > prices[min_p_ind]:
       		res += prices[i] - prices[min_p_ind]
       	return res

    def maxProfit(self, prices):
        return sum(prices[i]-prices[i-1] for i in xrange(1,len(prices)) if prices[i]>prices[i-1])

    def maxProfitIII(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0

        profit = 0
        curr_profit = 0
        for i in xrange(1,len(prices)):
            if prices[i] < prices[i-1]:
                profit += curr_profit
                curr_profit = 0
            else:
                curr_profit += prices[i] - prices[i-1]
        profit += curr_profit
        return profit

sol = Solution()
p = [1,2,1,2,1,2,1,2,1]
p = [1,1,1,1,1,1,1,2,100]
print sol.maxProfit(p)
print sol.maxProfitII(p)
print sol.maxProfitIII(p)
