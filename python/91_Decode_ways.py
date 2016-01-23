"""
	91. Decode Ways

	A message containing letters from A-Z is being encoded to numbers using the following mapping:

	'A' -> 1
	'B' -> 2
	...
	'Z' -> 26
	Given an encoded message containing digits, determine the total number of ways to decode it.

	For example,
	Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

	The number of ways decoding "12" is 2.
"""

class Solution(object):
    def numDecodingsII(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.res = 0
        self.dfs(s)
        return self.res

    def dfs(self, s):
    	if len(s) == 0:
    		self.res += 1
    		return
    	elif len(s) == 1:
    		if s == '0':
    			return
    		else:
    			self.dfs(s[1:])
    			return
    	else:
    		if s[0] == '0':
    			return
    		else:
    			self.dfs(s[1:])
    			if int(s[:2]) <= 26:
    				self.dfs(s[2:])
    			return

    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # if s begin with 0, return 0.
        if not len(s) or s[0] == '0':
            return 0

        total = 1
        pre = 1

        for i in range(1, len(s)):

            # when 0 appear, revert total to pre.
            if s[i] == '0':
                if not s[i-1] in '12':
                    return 0
                total = pre
                

            # if 2-digits num can be decoded, add pre to total,
            # and save the previous total to pre.
            elif int(s[i-1:i+1]) < 27 and s[i-1] != '0':
                pre, total = total, total+pre

            # all-is-well! forward to next step.
            else:
                pre = total

        return total

 
    		
sol = Solution()
s = "6065812287883668764831544958683283296479682877898293612168136334983851946827579555449329483852397155"
#s = "1122"
s = "4757562545844617494555774581341211511296816786586787755257741178599337186486723247528324612117156948"
#s = "9999999991919191991919919191919199191999999999999999999999999999999999999999999999999999999999999999999999999991999999"
s = "120345"
print sol.numDecodings(s)