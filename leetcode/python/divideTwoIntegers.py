"""
	Divide Two Integers

	Divide two integers without using multiplication, division and mod operator.

	If it is overflow, return MAX_INT.

	https://leetcode.com/problems/divide-two-integers/
"""

class Solution(object):
	def di(self, dividend, divisor):
		"""
		:type dividend: int
		:type divisor: int
		:rtype: int
		"""
		
		
		if dividend < 0 :
			return -self.di(-dividend, divisor)
		if divisor < 0 :
			return -self.di(dividend , -divisor)

		

		i = 0
		result = 0
		temp = divisor
		while dividend >= divisor:
			if dividend >= temp<<1:
				temp = temp << 1
				i += 1
			else:
				dividend = dividend - temp
				result += 1<<i
				temp = divisor
				i = 0
		return result

	def divide(self,dividend, divisor):
		Max_int32 = (1<<31)-1
		Min_int32 = -(1<<31)

		result = self.di(dividend, divisor)
		
		if result > Max_int32:
			result = Max_int32
			
		elif result < Min_int32:
			result = Min_int32

		return result
		
		



sol = Solution()
dividend = 15


dividsor = 3

print sol.divide(dividend, dividsor)

