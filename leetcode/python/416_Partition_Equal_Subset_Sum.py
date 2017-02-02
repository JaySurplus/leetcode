"""
    416. Partition Equal Subset Sum
    Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

    Note:
        Each of the array element will not exceed 100.
        The array size will not exceed 200.
        Example 1:

            Input: [1, 5, 11, 5]

            Output: true

            Explanation: The array can be partitioned as [1, 5, 5] and [11].
            Example 2:

                Input: [1, 2, 3, 5]

                Output: false

                Explanation: The array cannot be partitioned into equal sum subsets.
"""

class Solution(object):
    def canPartitionII(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total = sum(nums)
        if total % 2 != 0:
            return False
        dp = [True] + [False] * (total//2)
        for i in range(len(nums)):
            for j in range(total//2,0,-1):
                dp[j] = dp[j] or (j - nums[i] >= 0 and dp[j-nums[i]])
        return dp[-1]
    def canPartition(self, nums):
        total = sum(nums)
        if total % 2 != 0:
            return False
        return self.helper(total//2, 0, nums, {})
    def helper(self, target, index, nums, dp):
        if target in dp:
            return dp[target]
        if target == 0:
            dp[target] = True
            return dp[target]
        else:
            dp[target] = False
            for j in range(index, len(nums)):
                if target - nums[j] >= 0:
                    if self.helper(target - nums[j], j + 1, nums, dp):
                        dp[target] = True
                        break
            return dp[target]

sol = Solution()
nums = [1,5,11,5]
nums2 = [1,2,3,5]
nums3 = [1,2,3,6]
nums4 = [1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,100,99,100]
print(sol.canPartition(nums))
print(sol.canPartition(nums2))
print(sol.canPartition(nums3))
print(sol.canPartition(nums4))

