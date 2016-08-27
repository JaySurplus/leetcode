"""
    309. Best Time to Buy and Sell Stock with Cooldown

    Say you have an array for which the ith element is the price of a given stock on day i.

    Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

        You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
        After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
        Example:

            prices = [1, 2, 3, 0, 2]
            maxProfit = 3
            transactions = [buy, sell, cooldown, buy, sell]
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype : int
        """
        size = len(prices)
        if size < 2:
            return 0
        sell = [0] * size
        buy = [0] * size
        sell[0] = 0
        buy[0] = -prices[0]
        sell[1] = max(0 , prices[1]-prices[0])
        buy[1] = max(-prices[0],-prices[1])

        for i in xrange(2,size):
            sell[i] = max(sell[i-1],buy[i-1]+prices[i])
            buy[i] = max(buy[i-1],sell[i-2] - prices[i])
        return sell[-1]

sol = Solution()
prices = [1,2,3,0,2]
print sol.maxProfit(prices)


