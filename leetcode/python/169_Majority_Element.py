"""
    169. Majority Element

    Given an array of size n, find the majority element. The majority element is the element that appears more than floor(n/2) times.

    You may assume that the array is non-empty and the majority element always exist in the array.
"""
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr = 0
        count = 0
        for num in nums:
            if count == 0:
                curr = num
                count = 1
            elif num == curr:
                count += 1
            else:
                count -= 1
        return curr
sol = Solution()
nums = [1,2,3,3,3,3,3,1]
print sol.majorityElement(nums)




