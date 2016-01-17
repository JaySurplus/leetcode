"""
	72. Edit Distance

	https://leetcode.com/problems/edit-distance/

	Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)

	You have the following 3 operations permitted on a word:

	a) Insert a character
	b) Delete a character
	c) Replace a character
"""

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """

        dp = [ [ i  if j == 0 else 0 for i in range(len(word1)+1)  ] for j in range(len(word2)+1)]
        for i in range(len(word2)+1):
        	dp[i][0] = i
        
        for i in range(1,len(word2)+1):
        	for j in range(1,len(word1)+1):
        		
        		if word1[j-1] == word2[i-1]:
        			dp[i][j] = dp[i-1][j-1]
        		else:
        			dp[i][j] = min( min(dp[i-1][j-1], dp[i-1][j]) , dp[i][j-1]) + 1
       
       	return dp[-1][-1]

    def minDistanceII(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        def _dp(x, y):
            if distance[x][y] is None:
                if x == 0:
                    # boundary condition
                    distance[x][y] = y
                elif y == 0:
                    # boundary condition
                    distance[x][y] = x
                elif word1[x-1] == word2[y-1]:
                    distance[x][y] = _dp(x-1, y-1)
                else:
                    distance[x][y] = min(_dp(x-1, y), _dp(x, y-1), _dp(x-1, y-1)) + 1

            return distance[x][y]

        len1, len2 = len(word1), len(word2)
        distance = [[None] * (len2+1) for _ in range(len1+1)]
        
        return _dp(len1, len2)



sol = Solution()

word1 = "thisis"
word2 = "thisiis"

print sol.minDistanceII(word1, word2)