"""
	56. Merge Intervals

	Given a collection of intervals, merge all overlapping intervals.

	For example,
		Given [1,3],[2,6],[8,10],[15,18],
		return [1,6],[8,10],[15,18].
"""

# Definition for an interval.
class Interval(object):
	def __init__(self, s=0, e=0):
		self.start = s
		self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals.sort(key = lambda x : x.start)

        #print [ (i.start , i.end) for i in intervals]
        for i in range():
        	pass

a = Interval(1,3)
b = Interval(2,6)
c = Interval(8,10)
d = Interval(15,18)


intervals = [a, b, c,d]

sol = Solution()
sol.merge(intervals)
print a
