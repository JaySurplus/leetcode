"""
	77. Combinations

	https://leetcode.com/problems/combinations/

	Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

	For example,
	If n = 4 and k = 2, a solution is:

	[
  		[2,4],
  		[3,4],
  		[2,3],
  		[1,2],
  		[1,3],
  		[1,4],
	]

"""

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        self.res = []
        nL = [i for i in range(1,n+1)]
        self.dfs(nL , k , [])
        return self.res

    def dfs(self, n , k , temp):
    	if k == 0:
    		self.res.append(temp)
    	else:
    		for i in range(len(n)-k+1):
    			self.dfs(n[i+1:], k-1, temp+[n[i]])


sol = Solution()
n = 4
k = 4

print sol.combine(n , k)