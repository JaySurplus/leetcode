"""
    239. Sliding Window Maximum

    Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

    For example,
    Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

    Window position                Max
    ---------------               -----
    [1  3  -1] -3  5  3  6  7       3
     1 [3  -1  -3] 5  3  6  7       3
     1  3 [-1  -3  5] 3  6  7       5
     1  3  -1 [-3  5  3] 6  7       5
     1  3  -1  -3 [5  3  6] 7       6
     1  3  -1  -3  5 [3  6  7]      7
    Therefore, return the max sliding window as [3,3,5,5,6,7].
"""


class Solution(object):

    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if len(nums) <= 1:
            return nums
        self.max_count = 0
        self.max_num = -10000
        res = []

        def rebuild(i):
            self.max_num = max(nums[i+1-k:i+1])
            self.max_count = len(filter(lambda x: x == self.max_num , nums[i+1-k:i+1]))

        rebuild(k-1)
        res.append(self.max_num)

        for i in range(k,len(nums)):
            if nums[i] == self.max_num:
                self.max_count += 1
            elif nums[i] > self.max_num:
                self.max_count = 1
                self.max_num = nums[i]
            else:
                if nums[i-k] == self.max_num:
                    self.max_count -= 1
                    if self.max_count == 0:
                        rebuild(i)

            res.append(self.max_num)

        return res

    def maxSlidingWindowII(self, nums, k):
        if len(nums) <= 1:
            return nums

        max_num = max(nums[:k])
        max_pos = nums.index(max_num)

        res = [max_num]

        for i in range(k, len(nums)):
            next_val = nums[i]

            if next_val >= max_num:
                max_num = next_val
                max_pos = k - 1
            elif max_pos == 0:
                max_num = max(nums[i-k+1:i+1])
                max_pos = nums[i-k+1:i+1].index(max_num)
            else:
                max_pos -= 1
            res.append(max_num)

        return res


nums = [1,3,-1,-3,5,3,6,7]
k = 3

sol = Solution()
print sol.maxSlidingWindowII(nums,k)



