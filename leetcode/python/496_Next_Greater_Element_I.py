"""
    496. Next Greater Element I
    https://leetcode.com/problems/next-greater-element-i/?tab=Description
"""
class Solution(object):
    def nextGreaterElementII(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """

        res = [-1] * len(findNums)
        dic = dict(zip(nums,range(len(nums))))
        for i in range(len(findNums)):
            j = dic[findNums[i]] + 1
            while j < len(nums):
                if nums[j] > findNums[i]:
                    res[i] = nums[j]
                    break
                j += 1
        return res

    def nextGreaterElement(self, findNums, nums):
        res = [-1] * len(findNums)
        stack = []
        dic = {}
        for i in range(len(nums)):
            num = nums[i]
            while stack and nums[stack[0]] < num:
                dic[nums[stack.pop(0)]] = num
            stack = [i] + stack
        for i in range(len(findNums)):
            if findNums[i] in dic:
                res[i] = dic[findNums[i]]
        return res


sol = Solution()
findNums =  [4,1,2]
nums = [1,3,4,2]

#findNums = [2,4]
#nums = [1,2,3,4]
print sol.nextGreaterElement(findNums, nums)
