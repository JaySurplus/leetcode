"""
    506. Relative Ranks
    https://leetcode.com/problems/relative-ranks/?tab=Description
"""
class Solution(object):
    def findRelativeRanksII(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        res = [""] * len(nums)

        score = {1:"Gold Medal", 2:"Silver Medal", 3:"Bronze Medal"}

        val_ind = [[nums[i],i] for i in range(len(nums))]
        val_ind.sort(reverse=True)

        for i in xrange(len(nums)):
            val, ind = val_ind[i]
            if i + 1 in score:
                res[ind] = score[i+1]
            else:
                res[ind] = str(i+1)
        return res
    def findRelativeRanks(self, nums):
        sort = sorted(nums)[::-1]
        rank = ["Gold Medal", "Silver Medal", "Bronze Medal"] + map(str, range(4, len(nums) + 1))

        return map(dict(zip(sort, rank)).get, nums)

sol = Solution()
nums = [5, 4, 3, 2, 1]
print sol.findRelativeRanks(nums)

