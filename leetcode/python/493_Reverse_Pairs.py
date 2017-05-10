"""
    493 Reverse Pairs
    https://leetcode.com/problems/reverse-pairs/?tab=Description
"""
import bisect
class Solution(object):
    def reversePairsII(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.res = 0
        def msort(nums):
            l = len(nums)
            if len(nums) <= 1:
                return nums
            else:
                return merge(msort(nums[:int(l/2)]), msort(nums[int(l/2):]))

        def merge(left,right):
            l, r = 0, 0
            while l < len(left) and r < len(right):
                if left[l] <= 2*right[r]:
                    l += 1
                else:
                    self.res += len(left) - l
                    r += 1
            return sorted(left+right)

        msort(nums)
        return self.res

    def reversePairs(self, nums):
        return self.helper(nums, 0, len(nums))

    def helper(self, nums, l, r):
        mid = l + r >> 1
        if mid == l: return 0
        total = self.helper(nums, l, mid) + self.helper(nums, mid, r)
        prev_total = 0
        for i in range(l, mid):
            target = nums[i] - 1 >> 1
            idx = bisect.bisect_right(nums, target, mid, r)
            prev_total += idx - mid
            mid = idx
            total += prev_total
        nums[l: r] = sorted(nums[l: r])
        return total


sol = Solution()
nums = [1,3,2,3,1]
print sol.reversePairs(nums)
