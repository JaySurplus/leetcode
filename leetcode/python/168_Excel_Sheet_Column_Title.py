"""
    168. Excel Sheet Column Title

    Given a positive integer, return its corresponding column title as appear in an Excel sheet.

    For example:

        1 -> A
        2 -> B
        3 -> C
        ...
        26 -> Z
        27 -> AA
        28 -> AB

"""


class Solution(object):

    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = ''
        base = ord('A')
        while n:
            n, r = divmod(n - 1, 26)
            res = chr(base + r) + res
        return res


sol = Solution()
i = 852

print sol.convertToTitle(i)



