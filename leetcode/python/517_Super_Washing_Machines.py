"""
    517 Super Washing Machines
    https://leetcode.com/problems/super-washing-machines/?tab=Description
"""
class Solution(object):
    def findMinMoves(self, machines):
        """
        :type machines: List[int]
        :rtype: int
        """
        total = sum(machines)
        if total % len(machines) != 0:
            return -1
        avg = total / len(machines)
        #s = [0]
        #for i in range(len(machines)):
        #    s.append(s[-1] + machines[i])

        res = 0
        l = 0
        for i in range(len(machines)):
            r = machines[i] - avg - l
            res = max(res, l , r , l + r)
            #r = (len(machines) - i - 1) * avg - (s[len(machines)] - s[i+1])
            l = -r



        return res

sol = Solution()
machines = [1,0,5]
print sol.findMinMoves(machines)
