"""
    215. Kth Largest Element in an Array

    Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

    For example,
    Given [3,2,1,5,6,4] and k = 2, return 5.

    Note:
    You may assume k is always valid, 1 ≤ k ≤ array's length.
"""

import random
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        rand = random.randint(0,len(nums)-1)
        p = nums[rand]
        small = []
        large = []

        for i in xrange(len(nums)):
            if i != rand:
                if nums[i] < p:
                    small.append(nums[i])
                else:
                    large.append(nums[i])
        if len(large) == k - 1:
            return p
        if len(large) > k - 1:
            return self.findKthLargest(large , k )
        if len(large) < k - 1:
            return self.findKthLargest(small, k - len(large) -  1)
