"""
    386 Lexicographical Number

    Given an integer n, return 1 - n in lexicographical order.

    For example, given 13, return: [1,10,11,12,13,2,3,4,5,6,7,8,9].

    Please optimize your algorithm to use less time and space. The input size may be as large as 5,000,000.
"""
class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        def helper(k, res):
            if k <= n:
                res.append(k)
                t = 10 * k
                if t <= n:
                    for i in range(1,10):
                        helper(t+i, res)
            return
        
        res = []
        for i in range(10):
            helper(i,res)
        return res

sol = Solution()
n = 13
res = sol.lexicalOrder(n)