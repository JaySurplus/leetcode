"""
    The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

    1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

    Let us list the factors of the first seven triangle numbers:

     1: 1
     3: 1,3
     6: 1,2,3,6
    10: 1,2,5,10
    15: 1,3,5,15
    21: 1,3,7,21
    28: 1,2,4,7,14,28
    We can see that 28 is the first triangle number to have over five divisors.

    What is the value of the first triangle number to have over five hundred divisors?

"""

import time

class Solution(object):

    def highlyDivisibleTriangularNumber(self, c):

        dp = {}
        n = 1

        while True:
            if n % 2 == 0:
                if n / 2 not in dp:
                    dp[n / 2] = self.findDivisor(n / 2)
                if n + 1 not in dp:
                    dp[n + 1] = self.findDivisor(n + 1)
                res = dp[n / 2] * dp[n + 1]
                dp[n / 2 * (n + 1)] = res
            else:
                if n not in dp:
                    dp[n] = self.findDivisor(n)
                if (n + 1) / 2 not in dp:
                    dp[(n + 1) / 2] = self.findDivisor((n + 1) / 2)
                res = dp[(n + 1) / 2] * dp[n]
                dp[(n + 1) / 2 * n] = res

            if res > c:
                return n
            n += 1

    def findDivisor(self, n):
        count = 0

        for i in range(1, int(n**0.5)+1):
            if n % i == 0:
                count += 2
        if i ** 2 == n:
            count -= 1
        return count


sol = Solution()
n = 3
start = time.time()
res = sol.highlyDivisibleTriangularNumber(n)
end = time.time()




print "the %dth triangle number %d, is the 1st have over %d divisiors." % (res , res * (res + 1) / 2 , n)

print "Running time is ", end-start
