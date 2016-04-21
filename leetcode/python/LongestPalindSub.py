class Solution:
    # @param {string} s
    # @return {string}
    def longestPalindrome(self, s):
    	self.s = s
    	longest = ''
    	
    	for i in range(len(self.s)):
    		k = 1
    		if len(s[i]) > len(longest):
    			longest = s[i] 
    		while i - k >=0 and i+k < len(self.s) and len(longest) < (len(self.s)-i)*2:
    			#print i, k ,longest
    			if s[i-k] == s[i+k]:
    				if 2*k +1> len(longest):
    					longest = s[i-k:i+k+1]
    				k+=1
    			else :
    				break
    		k = 1
    		while i -k +1>= 0 and i+k < len(self.s) and len(longest) < (len(self.s)-i)*2:
    			if s[i-k+1] == s[i+k]:
    				if 2*k> len(longest):
    					longest = s[i-k+1:i+k+1]
    				k+=1
    			else :
    				break
    	return longest





def main():
	s = "abbba"

	sol = Solution()

	print sol.longestPalindrome(s)


if __name__ == '__main__':
	main()



