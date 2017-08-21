# Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution:
    # @param {Pint[]} points a list of points
    # @param {Point} origin a point
    # @param {int} k an integer
    # @return {Pint[]} the k closest points
    def kClosest(self, points, origin, k):
        # Write your code here
        import heapq

        def dist(a, b):
            a_p = (a.x, a.y)
            b_p = (b.x, b.y)

            return reduce(lambda x, y: x + y,
                map(lambda x: (x[0]-x[1])**2, zip(a_p, b_p)))
        l = []
        for point in points:
            heapq.heappush(l, (dist(origin, point), point))

        temp =  heapq.nsmallest(k, l)
        temp.sort(key = lambda x: (x[0], x[1].x))


        return [p[1] for p in temp]



points = [Point(4,6),Point(4,7),Point(4,4),Point(2,5),Point(1,1)]
origin = Point(0,0)
k = 3

sol = Solution()
print(sol.kClosest(points, origin, k))


