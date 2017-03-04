"""
    526. Beautiful Arrangement
    https://leetcode.com/problems/beautiful-arrangement/?tab=Description
"""
class Solution(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        l = [ i for i in range(1,N+1)]
        self.res = 0
        self.dic = {}
        self.helper(len(l)-1,l)
        t = self.dic.keys()
        t.sort()
        for i in t:
            print i
        return len(self.dic)

    def helper(self, ind, l):

        if ind == -1:
            return
        if tuple(l) in self.dic:
            return
        self.dic[tuple(l)] = 0
        for i in range(ind, len(l)):

            if (l[ind] % (i+1) == 0 and l[i] % (ind+1) == 0) or (l[ind] % (i+1) == 0 and  (ind+1) % l[i] == 0) or ((i+1) % l[ind] == 0 and l[i] % (ind+1) == 0) or ((i+1) % l[ind] == 0 and  (ind+1) % l[i] == 0):
                l[ind], l[i] = l[i] , l[ind]
                #if tuple(l) not in self.dic:
                self.helper(i,l)
                l[ind], l[i] = l[i] , l[ind]

        self.helper(ind-1,l)
        return


sol = Solution()

for i in range(4,5):
    print(sol.countArrangement(4))
