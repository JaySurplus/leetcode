"""
    149. Max Points on a Line

    Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.
"""


class Point(object):

    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b


class Solution(object):

    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        if len(points) == 0:
            return 0

        mm = {}
        for p in points:
            mm[(p.x, p.y)] = mm.get((p.x, p.y), 0) + 1

        P = mm.keys()
        if len(P) == 1:
            return mm[P[0]]

        m = 0
        for i in range(len(P) - 1):
            slopes = {}
            for j in range(i + 1, len(P)):
                dx = P[i][0] - P[j][0]
                dy = P[i][1] - P[j][1]
                if dx == 0:
                    slope = "#"
                elif:
                    slope = 0
                else:
                    slope = float(dy) / dx
                slopes[slope] = slopes.get(slope, 0) + mm[P[j]]
            m = max(m, mm[P[i]] + max(slopes.values()))
        return m
