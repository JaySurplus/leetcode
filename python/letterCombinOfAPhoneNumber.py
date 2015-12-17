"""
	Letter Combinations of a Phone Number

	Given a digit string, return all possible letter combinations that the number could represent.


	A mapping of digit to letters (just like on the telephone buttons) is given below.


	https://leetcode.com/problems/letter-combinations-of-a-phone-number/
"""

import copy
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        self.numAlpha = {"2":['a','b','c'],
        				 "3":['d','e','f'],
        				 "4":['g','h','i'],
        				 "5":['j','k','l'],
        				 "6":['m','n','o'],
        				 "7":['p','q','r','s'],
        				 "8":['t','u','v'],
        				 "9":['w','x','y','z'],
        				 "0":[' ']}
        if len(digits) == 0:
        	return []

        def letterComb(s , l):
        	return map(lambda x:x+l,s)

        result = self.numAlpha[digits[0]]

        for i in range(1,len(digits)):
        	temp = []
        	for l in self.numAlpha[digits[i]]:
        		temp += letterComb(result, l)
        	result = temp
        	
        return result
	

sol = Solution()
print sol.letterCombinations("23456789")