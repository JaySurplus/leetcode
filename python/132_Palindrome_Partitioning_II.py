"""
	132. Palindrome Partitioning II

	Given a string s, partition s such that every substring of the partition is a palindrome.

	Return the minimum cuts needed for a palindrome partitioning of s.

	For example, given s = "aab",
	Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.
"""
class Solution(object):
    def minCutII(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == s[::-1]: 
            return 0

        for i in range(1, len(s)):
            if s[:i] == s[:i][::-1] and s[i:] == s[i:][::-1]:
               return 1


        self.dp = [ [ False  for i in range(len(s))] for i in range(len(s)) ] 
        sp = [i for i in range(len(s), -1 ,-1)]
        
        #for i in range(len(s)+1):
        #	sp[i] = len(s) - i
       
        for i in range(len(self.dp)-1,-1,-1):
        	for j in range(i, len(self.dp)):
        		if s[i] == s[j] and ( j - i < 2 or self.dp[i+1][j-1] == True ) :
        			self.dp[i][j] = True
        			sp[i] = min(sp[i] , sp[j+1]+1)

        return sp[0]-1

    def minCut(self, s):
   
        if s == s[::-1]: 
            return 0
        for i in range(1, len(s)):
            if s[:i] == s[:i][::-1] and s[i:] == s[i:][::-1]:
               return 1
    
        cut = [x for x in range(-1,len(s))]  # cut numbers in worst case (no palindrome)
        for i in range(len(s)):
            r1, r2 = 0, 0
        
        
            while i-r1 >= 0 and i+r1 < len(s) and s[i-r1] == s[i+r1]:
                cut[i+r1+1] = min(cut[i+r1+1], cut[i-r1]+1)
                r1 += 1
        
            while i-r2 >= 0 and i+r2+1 < len(s) and s[i-r2] == s[i+r2+1]:
                cut[i+r2+2] = min(cut[i+r2+2], cut[i-r2]+1)
                r2 += 1
        return cut[-1]    

    def helper(self,  currCut , ind):
    	
    	if ind == self.l:
    		if currCut < self.res:
    			self.res = currCut
    		return
    	if currCut == self.res:
    		return

    	for i in range(ind , self.l):
    		
    		
    		if self.dp[ind][i] == True:
    			if i == self.l-1:
    				self.helper(currCut, i+1)
    			else:
    				self.helper(currCut+1, i+1)
    		
    			





sol = Solution()
s = "aaaaaaaaabbbbbbbbbaaaaaaaaabbbbbbbbbaaaaaaaaabbbbbbbbbaaaaaaaaa"
s = "fifgbeajcacehiicccfecbfhhgfiiecdcjjffbghdidbhbdbfbfjccgbbdcjheccfbhafehieabbdfeigbiaggchaeghaijfbjhi"
res = sol.minCut(s)

print res