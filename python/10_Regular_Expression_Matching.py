"""
	10. Regular Expression Matching 
	https://leetcode.com/problems/regular-expression-matching/


	'.' Matches any single character.
	'*' Matches zero or more of the preceding element.

	The matching should cover the entire input string (not partial).	

	The function prototype should be:
	bool isMatch(const char *s, const char *p)	

	Some examples:
	isMatch("aa","a") -> false
	isMatch("aa","aa") -> true
	isMatch("aaa","aa") -> false
	isMatch("aa", "a*") -> true
	isMatch("aa", ".*") -> true
	isMatch("ab", ".*") -> true
	isMatch("aab", "c*a*b") -> true

	https://leetcode.com/problems/regular-expression-matching/

"""

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        
        p_length = len(p)
        s_length = len(s)
        i = 0
        j = 0

       	# invalid state.
        if p_length == 0 or p[0] == '*':
            return False

        # will match anything
        if p == ".*":   
        	return True


        while i < s_length :
            if p[i] == '.':
            	if i < p_length-1:
            		if p[i+1] != '*':
            			test = self.isMatch(s[i+1:], p[i+1])
            			if not test:
            				return False
            		else:

            	else:
            		return True

            elif p[i] == '*':
            	pre = p[i-1]
            	
            	
            
            
            
            
            
            
        return True


def main():
	test = Solution()
    
	print test.isMatch('','a')
	print test.isMatch('aa','a')
	print test.isMatch('aab', 'c*a*b')
	print test.isMatch("aa", ".*")
	print test.isMatch("ab", ".*")
	print test.isMatch("a", "b")
	print test.isMatch("ab", ".*c")

if __name__ == '__main__':
	main()