"""
    514. Freedom Trail
    https://leetcode.com/problems/freedom-trail/?tab=Description
"""
class Solution(object):
    def findRotateSteps(self, ring, key):
        n = len(ring)

        def dist(i,j):
            return min(abs(i-j), n - abs(i-j))

        dic = {}
        for i in range(n):
            if ring[i] not in dic:
                dic[ring[i]] = [i]
            else:
                dic[ring[i]].append(i)

        curr_pos = [[0,0]]
        for k in key:
            #pl_k = dic[k]
            next_pos = [[p,0] for p in dic[k]]

            for ps in next_pos:
                p = ps[0]
                #cmin = dist(p,curr_pos[0][0]) + curr_pos[0][1]
                cmin = 2**31-1
                for curr_p in curr_pos:
                    cmin = min(cmin, dist(curr_p[0], p) + curr_p[1])
                ps[1] = cmin
            curr_pos = next_pos

        #cmin = curr_pos[0][1]
        cmin = 2**31-1
        for curr_p in curr_pos:
            cmin = min(cmin, curr_p[1])
        return len(key) + cmin

sol = Solution()
ring = "daudr"
key = "urdda"
print sol.findRotateSteps(ring, key)
