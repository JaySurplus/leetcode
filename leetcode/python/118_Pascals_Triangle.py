"""
    118. Pascal's Triangle
    Given numRows, generate the first numRows of Pascal's triangle.

    For example, given numRows = 5,
    Return

    [
        [1],
       [1,1],
      [1,2,1],
     [1,3,3,1],
    [1,4,6,4,1]
    ]
"""
class Solution(object):
    def generateII(self, numRows):
        if numRows <= 0:
            return []
        res = []
        self.helper(res,[1],numRows)
        return res

    def helper(self, r, t , n):
        if n == 0:
            return
        else:
            r.append(t)
            for i in xrange(len(t)-2, 0 , -1):
                t[i] += t[i-1]
            self.helper(r, t+[1], n-1)

    def generate(self, numRows):
        if numRows <= 0:
            return []

        res = [[1]]

        while numRows > 1:
            temp = res[-1][:-1]+[1]
            for i in range(len(temp)-1, 0 , -1):
                temp[i] += temp[i-1]
            res.append(temp+[1])
            numRows -= 1
        return res

sol = Solution()
num = 7
result = sol.generate(num)

print result
#for i in res:
#    print i
