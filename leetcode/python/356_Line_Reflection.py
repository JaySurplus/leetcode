"""
    356. Line Reflection

    Given n points on a 2D plane, find if there is such a line parallel to y-axis that reflect the given points.

    Example 1:
    Given points = [[1,1],[-1,1]], return true.

    Example 2:
    Given points = [[1,1],[-1,-1]], return false.
"""

class Solution(object):
    def isReflected(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        if len(points) == 0 or len(points) == 1:
            return True

        dic = {}



        points.sort(key = lambda x: x[0])


        #Reduce duplicates
        pt = [points[0]]
        for i in xrange(1,len(points)):
            if points[i] != points[i-1]:
                pt.append(points[i])



        points = pt
        length = len(points)


        if len(points) % 2== 1:
            mid = 1.* points[length/2][0]
            l = length/2 - 1
            r = length/2 + 1


        else:
            pos = len(points)/2

            l = pos-1
            r = pos
            mid = 1.*(points[l][0] + points[r][0])/2



        # Skip all points that x = mid, meanwhile points[:l+1] and points[r:] must have same length
        while l>= 0 and r < length and 1.*points[l][0] == mid and 1.*points[l][0] == mid:
            l-=1
            r+=1

        if l < 0 and r == length:
            return True
        if 1.*points[l][0] == mid or  1.*points[l][0] == mid:
            return False

        dic = {}
        while l >= 0:

            dic[str(2*mid-points[l][0]) + "+" + str(points[l][1])] = 1
            l -= 1

        while r < length:
            if str(1.*points[r][0]) + "+" + str(points[r][1]) not in dic:
                return False
            r += 1

        return True


sol = Solution()
s = [[1,2],[2,2],[1,4],[2,4]]
res = sol.isReflected(s)
print res



