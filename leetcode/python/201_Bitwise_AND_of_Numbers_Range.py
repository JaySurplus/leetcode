"""
	201. Bitwise AND of Numbers Range


	Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

	For example, given the range [5, 7], you should return 4.


"""
import math
class Solution(object):
	def rangeBitwiseAndII(self, m, n):
		"""
		:type m: int
		:type n: int
		:rtype: int
		"""
		"""
		power = int(math.log(n,2))
		

		if m < 2**power:

			return 0

		if m == 2**power:
			return m
		
		count = 0
		"""

		while n != m:
			n >>= 1
			m >>= 1
			count += 1
		res = n << count

		return res
	def rangeBitwiseAnd(self, m , n):
		while n > m:
			n = n & (n-1)
		return n

		

sol = Solution()
m , n = 247,255

res = sol.rangeBitwiseAnd(m,n)

print res

print reduce(lambda a , b : a&b , range(m,n))

