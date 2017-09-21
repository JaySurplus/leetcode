"""
    Bowling Pins
    https://www.hackerrank.com/challenges/bowling-pins/problem
"""
from functools import reduce

class Solution():
    def solver(self, s):
        s = filter(lambda x: x != '', s.split("X"))
        self.mex = {0: 0 ,1: 1, 2: 2}
        res = self.helper(s)
        return "LOSE" if res == 0 else "WIN"

    def helper(self, s):
        def getRes(t):

            if t in self.mex:
                return self.mex[t]
            else:
                mex_set = set()
                for l in [1, 2]:
                    for i in range((t - l) // 2 + 1):
                        mex_set.add(getRes(i) ^ getRes(t - i - l))
                r = 0
                while r in mex_set:
                    r += 1
                self.mex[t] = r
                return self.mex[t]
        mex_list = list(map(lambda x: getRes(len(x)), s))
        res = reduce(lambda x, y: x ^ y, mex_list)
        return res

sol = Solution()

test_cases = ["IIXXIIIIII", "IXIXI", "XXIXXI", "IIXII", "XIIIII", "XIXIIXII", "IIXIII"]

for test in test_cases:
    print(sol.solver(test))
