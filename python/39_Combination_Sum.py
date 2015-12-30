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
      				for i in range(len(candidates)):
      					sol.append(candidates[i])
      					self.combi(candidates[i:] , target - candidates[i] , sol , allSol)
      					sol.remove(candidates[i])
"""

class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def DFS(self, candidates, target, start, valuelist):
        length = len(candidates)
        if target == 0:
            return Solution.ret.append(valuelist)
        for i in range(start, length):
            if target < candidates[i]:
                return
            self.DFS(candidates, target - candidates[i], i, valuelist + [candidates[i]])
        
    def combinationSum(self, candidates, target):
    	candidates = list(set(candidates))
        candidates.sort()
        Solution.ret = []
        self.DFS(candidates, target, 0, [])
        return Solution.ret


sol = Solution()
candidates = [1,2,4,6,8]
target = 9
result = sol.combinationSum(candidates, target)
print result


target = 40
#candidates = [1,3,9,27]
#result = sol.combinationSum(candidates, target)
print result