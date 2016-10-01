"""
    4405. Convert a Number to Hexadecimal
"""


class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        table = { 10: 'a', 11: 'b', 12:'c', 13:'d', 14:'e', 15:'f'}
        if num == 0:
            return "0"
        else:
            num &= 2**32-1
            mask = 15
            res = ''
            while num != 0:
                temp = num & mask
                if temp < 10:
                    res = str(temp) + res
                else:
                    res = table[temp] + res
                num >>= 4
            return res

