"""
	131. Palindrome Partitioning

	Given a string s, partition s such that every substring of the partition is a palindrome.

	Return all possible palindrome partitioning of s.

	For example, given s = "aab",
	Return

  	[
    	["aa","b"],
    	["a","a","b"]
  	]

"""

class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        self.l = len(s)
        self.dp = [[False for i in range(self.l) ] for j in range(self.l) ]

       

        for i in range(len(s)-1,-1,-1):
        	for j in range(i, len(s)):
        		if i == j:
                            self.dp[i][j] = True
                        else:
                            self.dp[i][j] = (self.dp[i+1][j-1] or j == i+1) and s[i] == s[j]


       # for d in self.dp:
        #    print d
        self.s = s
        self.res = []
        self.helper([], 0 )
        return self.res


    def helper(self,tempRes , currIndex):
        if currIndex == self.l:
            self.res.append(tempRes)
            return
        for i in range(currIndex , self.l):
            if self.dp[currIndex][i] == True:
                self.helper(tempRes + [self.s[currIndex:i+1]] , i+1)



    def partition_rec(self, result, tempRes,startIndex):
        for i in range(startIndex,len(tempRes)-1):
            if tempRes[i] == tempRes[i+1]:
                anotherResult = tempRes[:i]+[tempRes[i]+tempRes[i+1]]+tempRes[i+2:]
                result += [anotherResult]
                self.partition_rec(result, anotherResult,i)
            if i>0 and tempRes[i-1] == tempRes[i+1]:
                anotherResult = tempRes[:i-1]+[tempRes[i-1]+tempRes[i]+tempRes[i+1]]+tempRes[i+2:]
                result += [anotherResult]
                self.partition_rec(result, anotherResult,i-1)

    def partitionII(self, s):
        if len(s) == 0:
            return []
        result = []
        tempRes = []
        for i in range(len(s)):
            tempRes += [s[i]]
        result += [tempRes]
        print result
        self.partition_rec(result, result[0], 0)
        return result






sol = Solution()
s = "aaaaa"

res = sol.partitionII(s)
#print res
