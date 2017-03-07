"""
    494. Target Sum
    https://leetcode.com/problems/target-sum/?tab=Description
"""
class Solution(object):
    def findTargetSumWaysII(self, nums, S):
        if not nums:
            return 0
        dic = {nums[0]: 1, -nums[0]: 1} if nums[0] != 0 else {0: 2}
        for i in range(1, len(nums)):
            tdic = {}
            for d in dic:
                tdic[d + nums[i]] = tdic.get(d + nums[i], 0) + dic.get(d, 0)
                tdic[d - nums[i]] = tdic.get(d - nums[i], 0) + dic.get(d, 0)
            dic = tdic
        return dic.get(S, 0)

    def findTargetSumWays(self, nums, s):
        def find(i,s):
            if (i,s) not in cache:
                r = 0
                if i == len(nums):
                    if s == 0:
                        r = 1
                else:
                    r = find(i+1,s-nums[i]) + find(i+1,s+nums[i])
                cache[(i,s)] = r
            return cache[(i,s)]
        cache = {}
        return find(0,s)

sol = Solution()
nums = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
S = 3
print sol.findTargetSumWays(nums,S)
print sol.findTargetSumWaysII(nums,S)
