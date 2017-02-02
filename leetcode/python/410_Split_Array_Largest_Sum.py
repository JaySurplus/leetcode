"""
    410. Split Array Largest Sum
    Given an array which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays. Write an algorithm to minimize the largest sum among these m subarrays.

Note:
    Given m satisfies the following constraint: 1 <= m <= length(nums) <= 14,000.

Examples:

Input:
nums = [7,2,5,10,8]
m = 2

Output:
18

Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.
"""
import heapq
class Solution(object):
    def split(self,item ):
        s = -item[0]
        nums = item[1]
        if len(nums) == 1:
            return [(-s,nums)]
        max_sum = s
        l = 0
        r = s
        for i in range(len(nums)):
            if max(l+nums[i],r-nums[i]) < max_sum:
                l += nums[i]
                r -= nums[i]
                max_sum = max(l,r)
            else:
                return [(-l,nums[:i]),(-r,nums[i:])]




    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        l = []
        heapq.heappush(l,(-sum(nums),nums))
        while m > 1:
            m -= 1
            item = heapq.heappop(l)
            res = self.split(item)
            if len(res) == 1:
                return -res[0][0]
            else:
                heapq.heappush(l,res[0])
                heapq.heappush(l,res[1])
        return -heapq.heappop(l)[0]



if __name__ == '__main__':
    nums = [7, 2, 5, 10, 8,21,33,32]
    m = 4
    sol = Solution()
    res = sol.splitArray(nums, m)
    print("Output:\n%d" % (res))

