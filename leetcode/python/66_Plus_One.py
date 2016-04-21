"""
	66. Plus One

	https://leetcode.com/problems/plus-one/

	Given a non-negative number represented as an array of digits, plus one to the number.

	The digits are stored such that the most significant digit is at the head of the list.
"""

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        dig = 0
        i = len(digits)-1
   
        while i >= 0 and carry != 0:
        	s = digits[i] + carry
        	digits[i] = s%10
        	carry = s/10
        	i -= 1
        if carry == 1:
        	digits = [1] + digits
        return digits

    def plusOneII(self, digits):
    	return list(str(int(''.join(map(lambda x : str(x),digits)))+1))

sol = Solution()
digits = [9,9,9,9,7,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9]
print sol.plusOneII(digits)

 