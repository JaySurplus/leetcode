"""
    357 Count Numbers with Unique Digits


    Given a non-negative integer n, count all numbers with unique digits, x, where 0 <= x < 10n.

    Example:
    Given n = 2, return 91. (The answer should be the total numbers in the range of 0 <= x < 100, excluding [11,22,33,44,55,66,77,88,99])
"""
class Solution(object):
    def countNumbersWithUniqueDigits(self,n):
        if n == 0:
            return 1
        if n == 1:
            return 10
        if n > 10:
            n = 10

        total = 10
        temp = 9
        for i in range(2,n+1):
            temp *= (11-i)
            total += temp
        return total


sol = Solution()
for i in range(11):
    print i, ":" ,sol.countNumbersWithUniqueDigits(i) ,  ","

