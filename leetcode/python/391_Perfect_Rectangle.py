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
        curr_rec = []
        #rectangle vector representation. [(x0,x1), (y0,y1)]
        for rec in rectangles:
            curr_rec.append([[rec[0],rec[2]],[rec[1],rec[3]]])
        temp_rec = []
        while len(curr_rec) > 1:
            num_recs = len(curr_rec)
            while curr_rec:
                temp = curr_rec.pop(0)
                i = 0
                flag = True
                while temp_rec and i < len(temp_rec):
                    if temp_rec[i][0] == temp[0]:
                        if temp_rec[i][1][1] == temp[1][0] :
                            temp_rec[i][1][1] = temp[1][1]
                            flag = False
                            break
                        elif temp_rec[i][1][0] == temp[1][1]:
                            temp_rec[i][1][0] = temp[1][0]
                            flag = False
                            break
                    elif temp_rec[i][1] == temp[1]:
                        if temp_rec[i][0][1] == temp[0][0]:
                            temp_rec[i][0][1] = temp[0][1]
                            flag = False
                            break
                        elif temp_rec[i][0][0] == temp[0][1]:
                            temp_rec[i][0][0] = temp[0][0]
                            flag = False
                            break
                    i += 1
                if flag:
                    temp_rec.append(temp)
            if len(temp_rec) == num_recs:
                return False

            curr_rec = temp_rec
            temp_rec = []
        return True


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
