"""
	119. Pascal's Triangle II
	Given an index k, return the kth row of the Pascal's triangle.

	For example, given k = 3,
	Return [1,3,3,1].

	Note:
	Could you optimize your algorithm to use only O(k) extra space?
"""

class Solution(object):
	def getRow(self, rowIndex):
		if rowIndex < 0:
			return []

		res = [1]

		while rowIndex > 0:
			for i in xrange(len(res)-1 , 0 , -1):
				res[i] += res[i-1]
			res += [1]
			rowIndex -= 1
		return res

sol = Solution()
n = 3
res = sol.getRow(n)
print res