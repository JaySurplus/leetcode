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

import copy
class Solution(object):
    def combinationSum(self, candidates, target):

        if len(candidates) == 0:
          return []

       
        candidates.sort()
     
        sol = []
        allSol = []
        self.combi(candidates, target , sol , allSol)
        return allSol

    def combi(self, candidates, target, sol , allSol):
      #print candidates , target 
      if len(candidates) == 0:
        return  

      else:
        if candidates[-1] == target:
          temp = copy.deepcopy(sol)
          temp.append(candidates[-1])
          allSol.append(temp)
          self.combi(candidates[:-1], target , sol , allSol)


        else:
            if candidates[-1] + candidates[0] > target:
              self.combi(candidates[:-1], target , sol , allSol)
            

            else:
              for i in range(len(candidates)-1,-1,-1):
                sol.append(candidates[i])
                self.combi(candidates[:i] , target - candidates[i] , sol , allSol)
                sol.remove(candidates[i])

sol = Solution()
candidates = [10,1,2,7,6,1,5]

target = 8
result = sol.combinationSum(candidates, target)
print result
