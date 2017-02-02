"""
    415. Add Strings

    Given two non-negative numbers num1 and num2 represented as string, return the sum of num1 and num2.

    Note:

        The length of both num1 and num2 is < 5100.
        Both num1 and num2 contains only digits 0-9.
        Both num1 and num2 does not contain any leading zero.
        You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res = ""
        carry = 0
        if len(num1) < len(num2):
            num1 = "0" * (len(num2) - len(num1)) + num1
        else:
            num2 = "0" * (len(num1) - len(num2)) + num2
        for i in range(1,len(num2)+1):
            temp = int(num1[-i]) + int(num2[-i]) + carry
            res += str(temp%10)
            carry = temp//10
        if carry:
            res += str(carry)
        return res[::-1]

sol = Solution()
num1 = "43214"
num2 = "31412"
print(sol.addStrings(num1,num2))
print(str(int(num1)+int(num2)))

