"""
    problem 323
"""
class Solution(object):
    def cdf(self,n):
        return (1-0.5**n)**32

    def res(self):
        ans = 0.0
        i = 1
        n_p = 0.0
        while True:
            n_c = self.cdf(i)
            p = n_c - n_p
            if p < 1e-20:
                break
            ans += i*p
            n_p = n_c
            i += 1
        return "{:.10f}".format(ans)
sol = Solution()
res = sol.res()
print res
