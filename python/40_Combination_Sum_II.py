"""
	Combination Sum II


	Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

	Each number in C may only be used once in the combination.

	Note:
	All numbers (including target) will be positive integers.
	Elements in a combination (a1, a2, .... , ak) must be in non-descending order. (ie, a1 <= a2  <= ... ak).
	The solution set must not contain duplicate combinations.
	For example, given candidate set 10,1,2,7,6,1,5 and target 8, 
	A solution set is: 
	[1, 7] 
	[1, 2, 5] 
	[2, 6] 
	[1, 1, 6] 



"""


class Solution(object):
    def combinationSum2(self, candidates, target):

        if len(candidates) == 0:
          return []

       
        candidates.sort()
     
        sol = []
        allSol = []
        self.combi(candidates, target , 0 ,sol , allSol)

        return allSol

    def combi(self, candidates, target, ind ,sol , allSol):

        if target == 0:
         	if sol not in allSol:
          		allSol.append(sol)

        for i in range(ind , len(candidates)):
            if target < candidates[i]:
            	return
            self.combi(candidates , target - candidates[i] ,ind + 1 , sol + [candidates[i]], allSol)
            	

sol = Solution()
candidates = [10,1,2,7,6,1,5]
candidates = [1]
target = 1
result = sol.combinationSum2(candidates, target)
print result
