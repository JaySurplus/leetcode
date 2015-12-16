"""
/*
		Integer to Roman
		Given an integer, convert it to a roman numeral.

		Input is guaranteed to be within the range from 1 to 3999.

		https://leetcode.com/problems/integer-to-roman/
*/
"""

class Solution(object):
  def intToRoman(self, num):
    result = ''
    roman_numerals = {1000:'M',
                      900: 'CM',
                      500: 'D',
                      400: 'CD',
                      100: 'C',
                      90: 'XC',
                      50: 'L',
                      40: 'XL',
                      10: 'X',
                      9: 'IX',
                      5: 'V',
                      4: 'IV',
                      1: 'I'
    }
    for key in sorted(roman_numerals.keys() , reverse = True):
      
      result += roman_numerals[key]*(num / key)
   
      num = num% key

    return result


      

sol = Solution()
print sol.intToRoman(3999)
