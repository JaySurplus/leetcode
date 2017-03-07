"""
    504. Base 7
    https://leetcode.com/problems/base-7/?tab=Description
"""
class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "0"
        n = abs(num)
        res = ""
        while n > 0:
            res = str(n%7) + res
            n /= 7

        if num < 0:
            return "-"+res
        return res

