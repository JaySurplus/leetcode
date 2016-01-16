"""
	65. Valid Number

	Validate if a given string is numeric.

	Some examples:
		"0" => true
		" 0.1 " => true
		"abc" => false
		"1 a" => false
		"2e10" => true
	Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one.
"""

import re
class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #pattern = r'^\ *(-|\+)?[0-9]+((.|e(-|\+)?)?[1-9]+)?\ *$'
        p = r'^\ *(-|\+)?([0-9]+|([0-9]*\.[0-9]+)|[0-9]+[e](-|\+)?[1-9]+)\ *$'
        res =  re.match(p , s)
    
        if res != None:
        	return True
        return False
sol = Solution()
s = 'f9'

print sol.isNumber(s)