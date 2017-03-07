"""
    495. Teemo Attacking
    https://leetcode.com/problems/teemo-attacking/?tab=Description
"""
class Solution(object):
    def findPoisonedDurationII(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        res = 0
        endTime = 0
        for startTime in timeSeries:
            if startTime >= endTime:
                endTime = startTime + duration
                res += duration
            else:
                res += duration - (endTime - startTime)
                endTime = startTime + duration
        return res

    def findPoisonedDuration(self, timeSeries, duration):
        res = duration * len(timeSeries)
        for i in range(1,len(timeSeries)):
            res -= max(0, duration - (timeSeries[i]-timeSeries[i-1]))
        return res

sol = Solution()
timeSeries = [1,4]
duration = 2
print sol.findPoisonedDuration(timeSeries, duration)
