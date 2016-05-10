"""
    166 Fraction to Recurring Decimal

    Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

    If the fractional part is repeating, enclose the repeating part in parentheses.

    For example,

    Given numerator = 1, denominator = 2, return "0.5".
    Given numerator = 2, denominator = 1, return "2".
    Given numerator = 2, denominator = 3, return "0.(6)".
"""


class Solution(object):

    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """

        res = ""
        deno = []
        dic = {}
        decimal = "" # Store the decimal part
        sign = True

        if numerator == 0:
            return "0"


        if numerator < 0:
            sign = not sign
            numerator = -numerator
        if denominator < 0:
            sign = not sign
            denominator = -denominator

        if not sign:
            res += "-"


        quotient = numerator / denominator
        res += str(quotient)
        numerator = numerator % denominator


        if numerator == 0:
            return res

        res += '.'

        i = 0
        while  numerator != 0:
            if numerator in dic.keys():
                index = dic[numerator]
                repeat = decimal[index:]
                non_repeat = decimal[:index]
                return res + non_repeat + '('+repeat+')'

            else:
                deno.append(numerator)
                dic[numerator] = i
                i += 1
                time_ten = numerator * 10

                decimal +=str(time_ten/denominator)
                numerator = time_ten % denominator


        return res + decimal

sol = Solution()
numerator = 313213
denominator = 1
res = sol.fractionToDecimal(numerator, denominator)
print res
print len(res)
