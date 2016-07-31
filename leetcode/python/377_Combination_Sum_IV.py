"""
    377. Combination Sum IV
    https://leetcode.com/problems/combination-sum-iv/

    Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.

    Example:

        nums = [1, 2, 3]
        target = 4

        The possible combination ways are:
            (1, 1, 1, 1)
            (1, 1, 2)
            (1, 2, 1)
            (1, 3)
            (2, 1, 1)
            (2, 2)
            (3, 1)

            Note that different sequences are counted as different combinations.

            Therefore the output is 7.
            Follow up:
                What if negative numbers are allowed in the given array?
                How does it change the problem?
                What limitation we need to add to the question to allow negative numbers?
"""

class Solution(object):
    def combinationSum4(self,nums,target):
        nums.sort()
        res = [0] * (target + 1)
        res[0] = 1
        for i in xrange(1,target+1):
            for num in nums:
                if num > i :
                    break
                res[i] += res[i-num]
        return res[target]
    def combinationSum4_2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0
        nums.sort()
        print nums
        self.nums = nums
        self.res = 0
        self.helper(0,0,target)
        return self.res

    def helper(self, currSum, currInd,target):
        if currSum == target:
            self.res += 1
            return
        else:
            for i in xrange(currInd,len(self.nums)):
                if currSum + self.nums[i] > target:
                    break
                self.helper(currSum + self.nums[i],i + 1,target)
            return

nums = [3,2,1]
sol = Solution()
print sol.combinationSum4(nums,4)
