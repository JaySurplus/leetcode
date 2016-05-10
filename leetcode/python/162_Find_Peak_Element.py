"""
    162. Find Peak Element

    A peak element is an element that is greater than its neighbors.

Given an input array where num[i] != num[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that num[-1] = num[n] = -inf.

For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.


"""
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = (l+r)/2
            #if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
            #    return mid

            if nums[mid] < nums[mid+1]:
                l = mid+1
            else:
                r = mid

        return l

sol = Solution()
nums = [3,3,3,3]
#nums.reverse()
print nums
print sol.findPeakElement(nums)
