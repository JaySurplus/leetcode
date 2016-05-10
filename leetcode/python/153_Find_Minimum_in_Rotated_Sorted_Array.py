"""
    153. Find Minimum in Rotated Sorted Array


    Suppose a sorted array is rotated at some pivot unknown to you beforehand.

    (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

    Find the minimum element.

    You may assume no duplicate exists in the array.

"""
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return min(nums)

        l = 0
        r = len(nums)-1

        while l <= r:
            povit = (l+r)/2
            if nums[povit] >= nums[r]:
                l = povit + 1
            else:
                r = povit
        return nums[r]


    def findMinII(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return min(nums)
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return min(nums)

        pivot = len(nums)/2
        if nums[pivot] < nums[-1]:
            return self.findMin(nums[:pivot+1])

        if nums[pivot] > nums[-1]:
            return self.findMin(nums[pivot:])

        #if nums[pivot] > nums[0] and nums[pivot] < nums[-1]:
         #   return nums[0]

sol = Solution()
nums = [3,4,5,6,7,0,1,1,1,1,1,1,1,1]
print sol.findMinII(nums)


