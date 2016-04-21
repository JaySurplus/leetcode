"""
	Combination Sum

	Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

	The same repeated number may be chosen from C unlimited number of times.

	Note:
	All numbers (including target) will be positive integers.
	Elements in a combination (a1, a2, ... , ak) must be in non-descending order. (ie, a1 <= a2 <= ... <= ak).
	The solution set must not contain duplicate combinations.
	For example, given candidate set 2,3,6,7 and target 7, 
	A solution set is: 
	[7] 
	[2, 2, 3] 

	https://leetcode.com/problems/combination-sum/
"""

import copy
class Solution(object):
    def combinationSum(self, candidates, target):

      	if len(candidates) == 0:
      		return []

      	candidates = list(set(candidates))
        candidates.sort()
     
      	sol = []
      	allSol = []

      	self.combi(candidates, target , 0,sol , allSol)
      	return allSol

    def combi(self, candidates, target,  ind,sol , allSol):
        #print candidates , target 
        if target == 0:
          allSol.append(sol)

        else:
          if target < candidates[0]:
            return
          else:
            for i in range(ind , len(candidates)):
              self.combi(candidates, target - candidates[i], i, sol + [candidates[i]] , allSol )



sol = Solution()
#candidates = [1,1,2,2,4,6,8]
candidates = [1,2,3,3,4,5,5,5,6,7,8,8,9]
target = 9
result = sol.combinationSum(candidates, target)
print result


target = 40
#candidates = [1,3,9,27]
#result = sol.combinationSum(candidates, target)
#print result