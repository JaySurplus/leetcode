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

      
        l = len(intervals) - 1
        ind = 0
        res = [intervals[0]]
        for i in intervals[1:]:
        	if res[-1].end >= i.start:
        		if res[-1].end < i.end :
        			res[-1].end = i.end
        	else:
        		res.append(i)

        return res
        	

a = Interval(1,3)
b = Interval(2,6)
c = Interval(8,10)
d = Interval(15,18)


intervals = [a, b, c,d]

sol = Solution()
res = sol.merge(intervals)
print [ (i.start , i.end) for i in res]
