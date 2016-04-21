"""
	137. Single Number II

	Given an array of integers, every element appears three times except for one. Find that single one.

	Note:
	Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

	Good explaination
	https://leetcode.com/discuss/81165/explanation-manipulation-method-might-easier-understand
	https://leetcode.com/discuss/43377/the-simplest-solution-ever-with-clear-explanation
"""

class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, nums):
    	one , two = 0,0,0

    	for num in nums:

    		two |= num & one
    		one ^= num
    		
    		three = ~(one & two)

    		one &= three
    		two &= three
    	return one
    def singleNumberII(self, nums):
    	one , two = 0,0
    	for num in nums:
    		one = (one ^ num) & (~two)
    		two = (two ^ num) & (~one)
    	return one
sol = Solution()
nums = [1,2,1,1,2,2,3]
res = sol.singleNumberII(nums)
print res
        
