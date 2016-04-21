"""
	97. Interleaving String

	Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

	For example,
	Given:
	s1 = "aabcc",
	s2 = "dbbca",

	When s3 = "aadbbcbcac", return true.
	When s3 = "aadbbbaccc", return false.


"""
class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        res = ((0,0))

        if len(s1) + len(s2) != len(s3):
        	return False

        if len(s1) == len(s2) == len(s3) == 0:
        	return True
        if s1 and s1[0] == s3[0] and self.isInterleave(s1[1:], s2 , s3[1:]):
        	return True
        if s2 and s2[0] == s3[0] and self.isInterleave(s1, s2[1:] , s3[1:]):
        	return True
        return False

    #O(mn) space DP
    def isInterleaveII(self, s1 ,s2, s3):

    	def dfs( i , j , s3):
    		if i + j == len(s3):
    			return 
    		if i < len(s2) and dp[i+1][j] == 0 and s2[i] == s3[i+j]:
    			dp[i+1][j] = dp[i][j]
    			dfs(i+1,j,s3)
    		if j < len(s1) and dp[i][j+1] == 0 and s1[j] == s3[i+j]:
    			dp[i][j+1] = dp[i][j]
    			dfs(i,j+1,s3)
    		return 
    	if len(s1) + len(s2) != len(s3):
    		return False

    	dp = [[0 for j in xrange(len(s1)+1)] for i in xrange(len(s2)+1) ]
    	dp[0][0] = True
    	
    	dfs(0,0,s3)
    	for k in dp:
    		print k

    	return dp[-1][-1] != 0

    # O(2n) space

    def isInterleaveVI(self, s1, s2, s3):
    	if len(s1) + len(s2) != len(s3):
    		return False

    	dp1 = [0 for j in xrange(len(s1)+1)] 
    	dp2 = [0 for j in xrange(len(s1)+1)]
    	dp1[0] = True
    	for i in range(len(s1)):
    		dp1[i+1] = dp1[i] and s1[i] == s3[i]
        print dp1
    	j = 0
    	while j < len(s2):
    		dp2[0] = (dp1[0] and s2[j] == s3[j])
    		for i in range(1,len(s1)+1):
    			dp2[i] = (s1[i-1] == s3[i+j] and dp2[i-1]) or (s2[j] == s3[i+j] and dp1[i])
    		j+= 1
    		dp1 = dp2
    		print dp1
    	return dp1[-1]

	#O(n) space
    def isInterleaveV(self, s1, s2, s3):
    	if len(s1) + len(s2) != len(s3):
    		return False

    	dp= [0 for j in xrange(len(s1)+1)]
    	dp[0] = True
    	for i in range(len(s1)):
    		dp[i+1] = dp[i] and s1[i] == s3[i]
    	j = 0
    	print dp
    	while j < len(s2):
    		dp[0] = (dp[0] and s2[j] == s3[j])
    		for i in range(1, len(s1)+1):
    			dp[i] = (s1[i-1] == s3[i+j] and dp[i-1]) or (s2[j] == s3[i+j] and dp[i])
    		j += 1
    		print dp
    	return dp[-1]
    # Recursive with trim.
    def isInterleaveIII(self, s1 ,s2, s3):
    	def dfs( i , j , s3):
    		if i + j == len(s3):
    			return True
    		if i < len(s2) and s2[i] == s3[i+j] and (i+1,j) not in v:
    			v.add((i+1,j))
    			if dfs(i+1, j ,s3):
    				return True
    		if j < len(s1) and s1[j] == s3[i+j] and (i,j+1) not in v:
    			v.add((i,j+1))
    			if dfs(i, j+1 ,s3):
    				return True
    		return False

    	if len(s1) + len(s2) != len(s3):
    		return False

    	v = set((0,0))
    	
    	res = dfs(0,0,s3)
    		
    	return res




sol = Solution()      
s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
s4 = "aadbbbaccc"
s1 = "a"
s2 = "abc"
s3 = "abac"
print sol.isInterleaveV(s1,s2,s3)