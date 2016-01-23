"""
	90. Subsets II

	Given a collection of integers that might contain duplicates, nums, return all possible subsets.

	Note:
	Elements in a subset must be in non-descending order.
	The solution set must not contain duplicate subsets.
	For example,
	If nums = [1,2,2], a solution is:

	[
  		[2],
  		[1],
  		[1,2,2],
  		[2,2],
  		[1,2],
  		[]
	]

	https://leetcode.com/problems/subsets-ii/
"""

class Solution(object):
    def subsetsWithDupII(self, S):
        dic = {}
        def dfs(depth, start, valuelist):
            t = ''.join(map(lambda x : str(x) , valuelist))
            if t not in dic:
            	res.append(valuelist)
            	dic[t] = 1
            if depth == len(S): return
            for i in range(start, len(S)):
                dfs(depth+1, i+1, valuelist+[S[i]])
        S.sort()
        res = []
        dfs(0, 0, [])
        return res

    def subsetsWithDupI(self, S):
    	res = [[]]
    	i = 0

    	while i < len(S):
    		val = S[i]
    		j = i+1
    		while j < len(S) and S[j] == val:
    			j += 1
    		k = i+1
    		tempList = []
    		while j >= k:
    			for l in res:
    				tempList.append(l+S[i:k])

    			k += 1
    		res += tempList
    		i = j 
    	return res
    
    def subsetsWithDup(self, S):
    	res = [[]]
    	S.sort()
    	for i in range(len(S)):
    		if i == 0 or S[i]!=S[i-1]:
    			previousL = len(res)
    		for j in range(len(res)-previousL, len(res)):
    			res.append(res[j]+[S[i]])
    	return res



sol = Solution()
S = [i for i in range(100)]
res =  sol.subsetsWithDup(S)
print len(res)