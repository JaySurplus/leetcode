"""
	93. Restore IP Addresses

	Given a string containing only digits, restore it by returning all possible valid IP address combinations.

	For example:
	Given "25525511135",

	return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)
"""

class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def dfs(i,s , temp):
        	if len(s) < (4-i)*1 or len(s) > (4-i)*3:
        		return 
        	if i == 3 :
        		if int(s) <= 255:
        			temp += str(int(s))
        			if temp not in res:
        				res.append(temp)
        		return
        	for j in range(1,4):
        		if j == 3:
        			if int(s[:j]) > 255:
        				return
        		dfs(i+1,s[j:],temp+str(int(s[:j]))+'.')
        		#dfs(i+1,s[j:],temp+s[:j]+'.')
        	return
        res = []
        dfs(0,s,'')
        return res

sol = Solution()
s = "010010"
print sol.restoreIpAddresses(s)
