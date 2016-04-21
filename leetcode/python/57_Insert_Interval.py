"""
	57. Insert Interval

	Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

	You may assume that the intervals were initially sorted according to their start times.

	Example 1:
	Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].

	Example 2:
	Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].

	This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].
"""

# Definition for an interval.
class Interval(object):
     def __init__(self, s=0, e=0):
         self.start = s
         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        if len(intervals) == 0:
        	intervals.append(newInterval)
        	return intervals
        l = [i.start for i in intervals]

        #newInterval should compare with interval in intervals at index 'ind'.
        ind = self.binary(0 , len(l) -1 , l , newInterval.start) 
        
        if newInterval.start < intervals[ind].start:
        	intervals.insert(ind , newInterval)
        	res = intervals[:ind+1]
        else:
        	intervals.insert(ind +1, newInterval)
        	res = intervals[:ind+1]

      
      
        for i in intervals[ind+1:]:
        	if res[-1].end >= i.start:
        		if res[-1].end < i.end :
        			res[-1].end = i.end
        	else:
        		res.append(i)
      
        return res

    def binary(self, s , e , l , target):
    	if s >= e :
    		return s


    	m = (s+e)/2
    	if target >= l[m] and target < l[m+1]:
    		return m
    	else:
    		if target < l[m]:
    			return self.binary(s, m-1, l ,target)
    		else:
    			#print m ,e
    			return self.binary(m+1, e, l ,target)




intervals = [Interval(1,3) ,Interval(6,9)]
intervalsII = [Interval(1,2) ,Interval(3,5),Interval(6,7),Interval(8,10),Interval(12,16)]
newInterval = Interval(2,5)
newIntervalII = Interval(4,9)

sol = Solution()
#resI = sol.insert(intervals, newInterval)
resII = sol.insert(intervalsII, newIntervalII )
#print  [ (i.start , i.end) for i in resI]
print  [ (i.start , i.end) for i in resII]
