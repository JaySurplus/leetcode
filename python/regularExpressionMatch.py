"""
	Regular Expression Matching 
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

        if p_length == 0 or p[0] == '*':
            return False


        while i < s_length and j < p_length:
            if p[j] != '*' or p[j] != '.':
                if p[j] == s[i]:
                    j += 1
                    i += 1
                else:
                    return False
            else:
                return True




       # return True


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