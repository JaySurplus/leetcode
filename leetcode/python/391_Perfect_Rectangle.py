"""
    391 Perfect Rectangle

    Given N axis-aligned rectangles where N > 0, determine if they all together form an exact cover of a rectangular region.

    Each rectangle is represented as a bottom-left point and a top-right point. For example, a unit square is represented as [1,1,2,2]. (coordinate of bottom-left point is (1, 1) and top-right point is (2, 2)).
"""

class Solution(object):
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        pass

if __name__ == '__main__':
    sol = Solution()
    rec1 = [
          [1,1,3,3],
          [3,1,4,2],
          [3,2,4,4],
          [1,3,2,4],
          [2,3,3,4]
    ]

    rec2 = [
          [1,1,2,3],
          [1,3,2,4],
          [3,1,4,2],
          [3,2,4,4]
    ]

    rec3 = [
          [1,1,3,3],
          [3,1,4,2],
          [1,3,2,4],
          [3,2,4,4]
    ]

    rec4 = [
          [1,1,3,3],
          [3,1,4,2],
          [1,3,2,4],
          [2,2,4,4]
    ]

    print sol.isRectangleCover(rec1)
    print sol.isRectangleCover(rec2)
    print sol.isRectangleCover(rec3)
    print sol.isRectangleCover(rec4)
